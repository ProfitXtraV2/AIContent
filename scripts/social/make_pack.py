#!/usr/bin/env python3
"""Turn the drafting agent's posts into a pack (tech spec flow 1, steps 5–6).

    python3 scripts/social/make_pack.py build <draft.json> [--brand vsichkikazina] [--out <dir>]
    python3 scripts/social/make_pack.py register <pack-id> --pr <n> --branch <branch> [--title …] [--posts N]
    python3 scripts/social/make_pack.py skip <item-id> --reason "<why>"
    python3 scripts/social/make_pack.py request <request-id> --status done|failed [--reason …] [--pack <pack-id>]
    python3 scripts/social/make_pack.py redraw <pack dir> --post <id> […]      # images out of date
    python3 scripts/social/make_pack.py fix-start <pack dir> --post <id> […] --why "<reason>"
    python3 scripts/social/make_pack.py handled <pack dir> --post <id> --comment <comment id>   # a /redo note
    python3 scripts/social/make_pack.py english <pack dir> <english.json>     # after rewriting posts

`build` assigns the post IDs, applies the account and link rules, confirms source records on
the live pages (A2), makes the visuals (flow 11), writes pack.json and posts/*.md with the
agent's English references, runs the checks and prints the PR title, branch and a first review
view. The agent then commits the folder on its branch, opens the PR, and calls `register` on
main. The full review view is added by the PR workflow (social-pr.yml).

The draft (written by the agent, see VsichkiKazina/social/prompts/post-writing.md):
  {"brand", "source": {"kind": "article"|"intro", "item_id"} | {"kind": "page", "request_id",
   "pages": [{"url", "lines": [...]}], "texts": [{"ref": "sources/<file>.md"|<library item ID>,
   "lines": [...]}]}, "request_id": null|id, "angle", "earlier_angles": [...],
   "posts": [{"account_id", "role", "angle", "text", "hashtags", "image_text", "alt_text",
              "english": {"text", "image_text": [...]},
              "art_idea", "slide_ideas": [...], "sources": [{"line", "where"}],
              "no_link_reason": null|"no link: no fitting page",
              "target_page": null|url, "earliest": null|"YYYY-MM-DD"}]}
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_library  # noqa: E402
from social import postnumbers as numbers  # noqa: E402
from social import (board, brands, checks, ids, links, operators, pack as packmod,  # noqa: E402
                    review_view, settings as settingsmod, source_record, spend as spendmod, visuals)


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def known_ids(root, brand_key, registry):
    """Every pack and post ID already given in this brand: registry rows and pack folders."""
    pack_ids = [r["pack_id"] for r in registry]
    post_ids = []
    packs = brands.social_dir(brand_key, root) / "packs"
    for d in (packs.iterdir() if packs.exists() else []):
        pack_ids.append(d.name)
        try:
            post_ids += [p["post_id"] for p in json.loads((d / "pack.json").read_text(encoding="utf-8"))["posts"]]
        except (OSError, ValueError, KeyError):
            pass
    ledger = brands.social_dir(brand_key, root) / "ledger.json"
    if ledger.exists():
        try:
            post_ids += [p["post_id"] for p in json.loads(ledger.read_text(encoding="utf-8")).get("posts", [])]
        except ValueError:
            pass
    return pack_ids, post_ids


def link_for(account, network, draft_post, source, post_id, source_id):
    """B6: the post's link mode (placeholder or none) and its tags or its reason."""
    if network == "instagram":
        return {"mode": "none", "reason": "link in profile"}
    if account["link"] == "none":
        return {"mode": "none", "reason": "no link: account setting"}
    if draft_post.get("no_link_reason") == "no link: no fitting page":
        return {"mode": "none", "reason": "no link: no fitting page"}
    campaign = source.get("slug") or source_id
    link = {"mode": "placeholder", "campaign": campaign, "content": post_id}
    if source.get("kind") == "page" and draft_post.get("target_page"):
        link["target"] = draft_post["target_page"]
    return link


def request_row(root, brand_key, request_id):
    """The request's row on the board ({} when there is none): its format, slides and sources."""
    if not request_id:
        return {}
    reqs, _ = board.parse_requests(board._read(board.requests_path(brand_key, root)))
    return next((r for r in reqs if r.get("id") == request_id), {})


def page_records(src_in, req, brand_key, brand_settings, ops, root, fetch):
    """Source records for a draft without a feed item: the brand's own pages, the pages and text
    files the request names, and the brand's library articles (source_record.py)."""
    given = board.request_sources(req)
    records = []
    for p in src_in.get("pages") or []:
        url, lines = p["url"], p.get("lines") or []
        own = links.allowed(url, brand_key, brand_settings, ops)[0]
        records.append(source_record.record(url, lines, brand_key, brand_settings, ops, fetch=fetch,
                                            outside=not own and url in given))
    for t in src_in.get("texts") or []:
        ref, lines = t.get("ref", ""), t.get("lines") or []
        if board.SOURCE_FILE.match(ref) and ref not in given:
            records.append({"kind": "text", "file": ref, "lines": [], "missing": list(lines),
                            "error": "the request does not name this file"})
            continue
        records.append(source_record.text_record(ref, lines, brand_key, root))
    return records


def style_of(brand_key, root):
    """The visuals context's house style and mascot pictures (<brand>/social/style/)."""
    style, refs = visuals.load_style(brand_key, root)
    return {"style": style, "refs": refs}


def number_sources(text_parts, source_lines):
    """[{value, source_index}] for every number in the post that a source line backs."""
    out = []
    for value in dict.fromkeys(t for part in text_parts for t in numbers.tokens(part)):
        for i, line in enumerate(source_lines):
            if numbers.occurs(value, line):
                out.append({"value": value, "source_index": i})
                break
    return out


def build(draft, brand_key, root=brands.ROOT, out_dir=None, gemini="env", fetch=operators.fetch, now=None):
    """(pack dir, summary). gemini: "env" (social key from SOCIAL_GEMINI_API_KEY, else none), None,
    or an object with generate/review (tests)."""
    root = Path(root)
    b = brands.brand(brand_key)
    s = settingsmod.load(brand_key, root)
    ops = operators.current(brand_key, root, s.brand["operator_names_manual"])
    registry = board.parse_packs(board._read(board.packs_path(brand_key, root)))
    src_in = draft["source"]
    item, article = None, ""
    if src_in["kind"] in ("article", "intro"):
        index = build_library.load_index(root, brand_key)
        slug = next((e["slug"] for e in index.get("items", []) if e["id"] == src_in["item_id"]), None)
        item, article = build_library.load_item(root, brand_key, slug) if slug else (None, None)
        if item is None:
            raise SystemExit(f"{src_in['item_id']} is not in the library")
        source_id = item["id"]
        source = {"kind": src_in["kind"], "item_id": item["id"], "slug": item["slug"],
                  "article_version": item["article_version"]}
    req = request_row(root, brand_key, draft.get("request_id") or src_in.get("request_id"))
    if src_in["kind"] not in ("article", "intro"):
        source_id = draft.get("request_id") or src_in.get("request_id")
        records = page_records(src_in, req, brand_key, s.brand, ops, root, fetch)
        source = {"kind": "page", "request_id": source_id, "pages": [p["url"] for p in src_in.get("pages") or []],
                  "records": records}
    if draft.get("request_id"):
        source["request_id"] = draft["request_id"]
    pack_ids, post_ids = known_ids(root, brand_key, registry)
    number = ids.next_pack_number(source_id, pack_ids)
    pack_id = ids.pack_id(source_id, number)
    pack_dir = Path(out_dir) if out_dir else brands.social_dir(brand_key, root) / "packs" / pack_id
    (pack_dir / "visuals").mkdir(parents=True, exist_ok=True)

    usable = {a["account_id"]: a for a in s.usable_accounts()}
    accounts = {a["account_id"]: a for a in s.accounts}
    if gemini == "env":
        key = os.environ.get("SOCIAL_GEMINI_API_KEY")
        gemini = visuals.Gemini(key, root, brands.social_dir(brand_key, root) / "prompts" / "visual-review.md") if key else None
    spend = spendmod.Spend(brands.social_dir(brand_key, root) / "image-spend.json", brand_key, s.brand["image_budget_usd"])
    art = (brands.social_dir(brand_key, root) / "prompts" / "visual-art.md")
    vctx = visuals.Ctx(brand_key, pack_dir, s, spend, gemini, item, root, ops,
                       art.read_text(encoding="utf-8") if art.exists() else "{idea}", fetch=fetch,
                       page_url=visuals.page_url_for(item, s.brand, brand_key), **style_of(brand_key, root))
    confirmed = {ln for rec in source.get("records") or [] for ln in rec.get("lines") or []}
    posts_meta, posts_fields, notes = [], {}, []
    for dp in draft["posts"]:
        aid = dp["account_id"]
        if aid not in usable:
            notes.append(f"{aid}: not an active account without errors; post dropped")
            continue
        acc = accounts[aid]
        net = acc["network"]
        pid = ids.next_post_ids(source_id, number, net, 1, post_ids)[0]
        post_ids.append(pid)
        text = dp["text"].strip()
        source_lines = [x["line"] for x in dp.get("sources") or []]
        if source["kind"] == "page":
            unconfirmed = [ln for ln in source_lines if ln not in confirmed]
            for ln in unconfirmed:                        # A2: never scheduled until resolved
                text += f"\n[VERIFY: not found in the recorded source: {ln[:80]}]"
        fields = {"text": text, "hashtags": [h if h.startswith("#") else "#" + h for h in dp.get("hashtags") or []],
                  "image_text": [ln.strip() for ln in dp.get("image_text") or [] if ln.strip()],
                  "alt_text": dp.get("alt_text", "").strip(), "english": ""}
        for tag in s.brand["brand_hashtags"]:
            if tag.lower() not in [h.lower() for h in fields["hashtags"]]:
                fields["hashtags"].append(tag)
        post = {"post_id": pid, "account_id": aid, "network": net, "role": dp.get("role", "launch"),
                "angle": dp.get("angle", ""), "art_idea": dp.get("art_idea", ""),
                "slide_ideas": [str(x).strip() for x in dp.get("slide_ideas") or [] if str(x).strip()],
                "link": link_for(acc, net, dp, source, pid, source_id),
                "sources": dp.get("sources") or [],
                "numbers": number_sources([text, "\n".join(fields["image_text"]), fields["alt_text"]], source_lines),
                "en_reference_of": "", "redo_notes": [], "notes": []}
        if not packmod.set_english(post, fields, dp.get("english")):
            notes.append(f"{pid}: no English reference in the draft")
        if dp.get("earliest"):
            post["earliest_utc"] = f"{dp['earliest']}T00:00:00Z"
        want_format, want_slides = board.request_format(req, acc)            # the request's, else the account's
        vis, vnotes, fmt = visuals.make(post, fields, vctx, account_format=want_format)
        post["visuals"], post["format"], post["notes"] = vis, fmt, vnotes
        if fmt == "carousel":
            post["slides"] = want_slides
        if fmt == "single" and want_format in ("carousel", "auto") and net in ("x", "linkedin-profile") \
                and len(fields["image_text"]) >= 4:
            post["carousel_fallback_note"] = f"carousel not offered on {net}: single image"
        posts_meta.append(post)
        posts_fields[pid] = fields
    meta = {"pack_id": pack_id, "brand": brand_key, "number": number, "angle": draft.get("angle", ""),
            "earlier_angles": draft.get("earlier_angles") or [], "source": source,
            "created_utc": now or now_utc(), "run_url": os.environ.get("RUN_URL", ""), "fix_round": 0,
            "posts": posts_meta, "notes": notes}
    packmod.save(pack_dir, meta, posts_fields)
    p = packmod.load(pack_dir)
    result = checks.run(p, checks.Context(brand_key, s, ops, item, article or ""))
    title = item["title"] if item else (draft.get("angle") or source_id)
    summary = {"pack_id": pack_id, "dir": str(pack_dir), "branch": f"social/{b['prefix']}/{pack_id}",
               "title": f"Social: {title} ({b['name']}) — {len(posts_meta)} post{'s' if len(posts_meta) != 1 else ''}",
               "posts": [x["post_id"] for x in posts_meta], "notes": notes, "checks_ok": result["ok"],
               "failing": [(pid, r["check"]) for pid, rs in result["posts"].items() for r in rs if not r["ok"]]}
    summary["pr_body"] = review_view.render(p, result, s, brand_key, commit_sha=None)
    return pack_dir, summary


def redraw(pack_dir, post_ids, brand_key, root=brands.ROOT, gemini="env", fetch=operators.fetch):
    """Make the visuals of the named posts again from their current image text (E3 "images out
    of date", or a redo of the images). Post IDs stay; old visual files are replaced."""
    root, pack_dir = Path(root), Path(pack_dir)
    p = packmod.load(pack_dir)
    s = settingsmod.load(brand_key, root)
    ops = operators.current(brand_key, root, s.brand["operator_names_manual"])
    src = p["meta"].get("source") or {}
    item = build_library.load_item(root, brand_key, src["slug"])[0] if src.get("slug") else None
    if gemini == "env":
        key = os.environ.get("SOCIAL_GEMINI_API_KEY")
        gemini = visuals.Gemini(key, root, brands.social_dir(brand_key, root) / "prompts" / "visual-review.md") if key else None
    spend = spendmod.Spend(brands.social_dir(brand_key, root) / "image-spend.json", brand_key, s.brand["image_budget_usd"])
    art = brands.social_dir(brand_key, root) / "prompts" / "visual-art.md"
    vctx = visuals.Ctx(brand_key, pack_dir, s, spend, gemini, item, root, ops,
                       art.read_text(encoding="utf-8") if art.exists() else "{idea}", fetch=fetch,
                       page_url=visuals.page_url_for(item, s.brand, brand_key), **style_of(brand_key, root))
    done = []
    for post in p["meta"]["posts"]:
        if post["post_id"] not in post_ids or post["post_id"] not in p["posts"]:
            continue
        for v in post.get("visuals") or []:
            (pack_dir / "visuals" / v["file"]).unlink(missing_ok=True)
        acc = s.account(post["account_id"]) or {"format": post.get("format", "single")}
        vis, notes, fmt = visuals.make(post, p["posts"][post["post_id"]], vctx, account_format=acc["format"])
        post["visuals"], post["format"], post["notes"] = vis, fmt, notes
        done.append(post["post_id"])
    packmod.save(pack_dir, p["meta"], p["posts"])
    return done


def fix_start(pack_dir, post_ids, why):
    """Raise the pack's fix round and mark the posts that go into the fix PR (E7)."""
    p = packmod.load(pack_dir)
    p["meta"]["fix_round"] = int(p["meta"].get("fix_round") or 0) + 1
    for post in p["meta"]["posts"]:
        if post["post_id"] in post_ids:
            post["fix"] = {"round": p["meta"]["fix_round"], "why": why}
    packmod.save(pack_dir, p["meta"], p["posts"])
    return p["meta"]["fix_round"]


def english(pack_dir, by_post):
    """The English references the agent wrote again after rewriting posts (a redo, a fix, a
    redraft): {post_id: {"text", "image_text"}}. Returns the post IDs updated."""
    p = packmod.load(pack_dir)
    done = []
    for post in p["meta"]["posts"]:
        pid = post["post_id"]
        if pid in by_post and pid in p["posts"] and packmod.set_english(post, p["posts"][pid], by_post[pid]):
            done.append(pid)
    packmod.save(pack_dir, p["meta"], p["posts"])
    return done


def handled(pack_dir, post_id, comment_id):
    """Record a redo note as handled, so the next run does not take it again (E5)."""
    p = packmod.load(pack_dir)
    for post in p["meta"]["posts"]:
        if post["post_id"] == post_id and int(comment_id) not in post.setdefault("redo_notes", []):
            post["redo_notes"].append(int(comment_id))
    packmod.save(pack_dir, p["meta"], p["posts"])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    rd = sub.add_parser("redraw")
    rd.add_argument("pack_dir")
    rd.add_argument("--post", action="append", required=True)
    rd.add_argument("--brand", default="vsichkikazina")
    fs = sub.add_parser("fix-start")
    fs.add_argument("pack_dir")
    fs.add_argument("--post", action="append", required=True)
    fs.add_argument("--why", required=True)
    hd = sub.add_parser("handled")
    hd.add_argument("pack_dir")
    hd.add_argument("--post", required=True)
    hd.add_argument("--comment", required=True)
    en = sub.add_parser("english")
    en.add_argument("pack_dir")
    en.add_argument("file", help='{"<post id>": {"text": "…", "image_text": ["…"]}}')
    b = sub.add_parser("build")
    b.add_argument("draft")
    b.add_argument("--brand", default="vsichkikazina")
    b.add_argument("--out")
    b.add_argument("--pr-body", help="write the first review view (the PR description) here")
    r = sub.add_parser("register")
    r.add_argument("pack_id")
    r.add_argument("--pr", required=True)
    r.add_argument("--branch", required=True)
    r.add_argument("--title", default="")
    r.add_argument("--posts", default="")
    r.add_argument("--brand", default="vsichkikazina")
    k = sub.add_parser("skip")
    k.add_argument("item_id")
    k.add_argument("--reason", required=True)
    k.add_argument("--brand", default="vsichkikazina")
    q = sub.add_parser("request")
    q.add_argument("request_id")
    q.add_argument("--status", required=True, choices=["done", "failed", "open"])
    q.add_argument("--reason", default="")
    q.add_argument("--pack", default="")
    q.add_argument("--brand", default="vsichkikazina")
    a = ap.parse_args(argv)
    if a.cmd == "redraw":
        print("redrawn: " + ", ".join(redraw(a.pack_dir, set(a.post), a.brand)))
        return 0
    if a.cmd == "fix-start":
        print(f"fix round {fix_start(a.pack_dir, set(a.post), a.why)}")
        return 0
    if a.cmd == "handled":
        handled(a.pack_dir, a.post, a.comment)
        return 0
    if a.cmd == "english":
        done = english(a.pack_dir, json.loads(Path(a.file).read_text(encoding="utf-8")))
        print("English reference: " + (", ".join(done) if done else "none updated"))
        return 0
    if a.cmd == "build":
        draft = json.loads(Path(a.draft).read_text(encoding="utf-8"))
        d, summary = build(draft, a.brand, out_dir=a.out)
        body = summary.pop("pr_body")
        if a.pr_body:
            Path(a.pr_body).write_text(body, encoding="utf-8")
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0
    if a.cmd == "register":
        p = board.packs_path(a.brand)
        src = ids.parse_pack_id(a.pack_id)
        text = board.upsert_pack(board._read(p), {
            "pack_id": a.pack_id, "source": src["source"] if src else "", "title": a.title,
            "pr": f"#{a.pr.lstrip('#')}", "branch": a.branch, "status": "open", "posts": a.posts,
            "created": board.today(), "updated": board.today()})
        p.write_text(text, encoding="utf-8")
        print(f"registered {a.pack_id} as open (#{a.pr.lstrip('#')})")
        return 0
    if a.cmd == "skip":
        p = board.packs_path(a.brand)
        p.write_text(board.upsert_pack(board._read(p), {
            "pack_id": a.item_id, "source": a.item_id, "status": "skipped", "note": a.reason,
            "created": board.today(), "updated": board.today()}), encoding="utf-8")
        print(f"skipped {a.item_id}: {a.reason}")
        return 0
    if a.cmd == "request":
        p = board.requests_path(a.brand)
        p.write_text(board.set_request(board._read(p), a.request_id, status=a.status, reason=a.reason,
                                       pack_id=a.pack), encoding="utf-8")
        print(f"{a.request_id}: {a.status}")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
