#!/usr/bin/env python3
"""The drafting run's work list (product spec A1–A5, A7, E5, E7, F11; tech spec flow 1, step 3).

    python3 scripts/social/worklist.py [brand] [--json out]

New packs: approved articles of an eligible type (not hub-intro), approved after the team's
settings merge switched social on, with no pack yet and not an operator or bonus article,
oldest approval first; then open requests, in the order they were added. At most "packs per
run" of these. Always, uncapped: redo notes, image redraws, redrafts of changed articles in open
pack PRs, and fix PRs.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_library  # noqa: E402
from social import board, brands, github, ids, operators, settings as settingsmod  # noqa: E402

REDO_RE = re.compile(rf"^\s*/redo\s+((?:{ids.SOURCE}-p\d+-(?:fb|ig|x|li)-\d+[\s,]*)+)(.*)$", re.I | re.S)
FIX_STATES = {"needs_fix", "article_changed"}


def parse_redo(body):
    """(post ids, note) from a PR comment „/redo <post ID> [<post ID> …] <note>“, or None."""
    m = REDO_RE.match(str(body or "").strip())
    if not m:
        return None
    pids = [p for p in re.split(r"[\s,]+", m.group(1)) if ids.parse_post_id(p)]
    return (pids, m.group(2).strip()) if pids else None


def pr_number(value):
    m = re.search(r"\d+", str(value or ""))
    return int(m.group(0)) if m else None


def work_list(settings, index, items, registry, requests, operator_names, social_on_since,
              merged_at, open_prs=(), ledger_posts=(), commands=()):
    """The run's work. items: {slug: item}; merged_at(pr_number) → ISO time or None;
    open_prs: [{pack_id, number, comments: [{id, body}], images_out_of_date: [post ids],
    source_version, handled: [comment ids]}]; ledger_posts: [{post_id, pack_id, state, markers}]."""
    out = {"brand_off": "", "new": [], "requests": [], "failed_requests": [], "skipped": [], "waiting": 0,
           "redo": [], "redraw": [], "redraft": [], "fixes": []}
    if not settings.social_on:
        out["brand_off"] = "social is off" if settings.brand_ok else "the brand settings have errors"
    elif not settings.usable_accounts():
        out["brand_off"] = "no active account"
    b = settings.brand
    in_registry = {r.get("source") for r in registry}
    by_id = {i["id"]: i for i in items.values()}

    # 1. approved articles, oldest approval first (A1, A5)
    candidates = []
    if not out["brand_off"]:
        for entry in index.get("items", []):
            item = items.get(entry["slug"])
            if not item or item["board_status"] != "approved" or item["kind"] != "article":
                continue
            if item["type"].lower() not in b["eligible_types"] or item["id"] in in_registry:
                continue
            flagged, why = operators.screen(item["title"], item["slug"], item["keywords"], operator_names,
                                            b["offer_words"])
            if flagged:
                out["skipped"].append({"item_id": item["id"], "slug": item["slug"],
                                       "reason": f"operator or bonus article ({why})"})
                continue
            when = merged_at(pr_number(item.get("pr")))
            if not when:
                continue                                      # approval time unknown: next run
            if social_on_since and when <= social_on_since:
                continue                                      # approved before social was on (A4, A5)
            candidates.append((when, item))
    candidates.sort(key=lambda c: (c[0], c[1]["id"]))
    queue = [{"kind": "article", "item_id": i["id"], "slug": i["slug"], "approved_utc": w} for w, i in candidates]

    # 2. open requests, in the order they were added (A2, A4)
    for r in requests:
        if r.get("status") != "open" or not r.get("id"):
            continue
        kind, target = r.get("kind", "keyword"), (r.get("target") or "").strip()
        problem = board.request_problem(r)
        if problem:
            out["failed_requests"].append({"id": r["id"], "reason": problem})
            continue
        asked = {"format": r.get("format", ""), "slides": r.get("slides", ""), "sources": board.request_sources(r)}
        if kind in ("article", "intro"):
            item = by_id.get(target) or items.get(target) or items.get(target.removeprefix("hub-intro-"))
            if item is None:
                out["failed_requests"].append({"id": r["id"], "reason": "not in the approved feed"})
                continue
            if kind == "intro" and item["kind"] != "hub-intro":
                out["failed_requests"].append({"id": r["id"], "reason": "not a section intro"})
                continue
            flagged, why = operators.screen(item["title"], item["slug"], item["keywords"], operator_names,
                                            b["offer_words"])
            if flagged:
                out["failed_requests"].append({"id": r["id"], "reason": "operator or bonus article"})
                continue
            queue.append({"kind": "request", "request_id": r["id"], "request_kind": kind,
                          "item_id": item["id"], "slug": item["slug"], "angle": r.get("angle", ""),
                          "accounts": r.get("accounts", ""), "earliest": r.get("earliest", ""), **asked})
        elif kind == "topic":                                 # a free topic: facts from the sources and our articles
            queue.append({"kind": "request", "request_id": r["id"], "request_kind": "topic",
                          "topic": target, "angle": r.get("angle", ""), "target_page": r.get("target_page", ""),
                          "accounts": r.get("accounts", ""), "earliest": r.get("earliest", ""), **asked})
        else:
            queue.append({"kind": "request", "request_id": r["id"], "request_kind": "keyword",
                          "keywords": target, "angle": r.get("angle", ""), "target_page": r.get("target_page", ""),
                          "accounts": r.get("accounts", ""), "earliest": r.get("earliest", ""), **asked})
    if not out["brand_off"]:
        cap = b["packs_per_run"]
        take = queue[:cap]
        out["new"] = [q for q in take if q["kind"] == "article"]
        out["requests"] = [q for q in take if q["kind"] == "request"]
        out["waiting"] = max(0, len(queue) - cap)

    # 3. always, uncapped: redo notes, image redraws, redrafts of changed articles (E5, E3, A9)
    for pr in open_prs:
        handled = set(pr.get("handled") or [])
        for c in pr.get("comments") or []:
            got = parse_redo(c.get("body"))
            if got and c.get("id") not in handled:
                out["redo"].append({"pack_id": pr["pack_id"], "pr": pr["number"], "comment_id": c["id"],
                                    "post_ids": got[0], "note": got[1]})
        if pr.get("images_out_of_date"):
            out["redraw"].append({"pack_id": pr["pack_id"], "pr": pr["number"], "post_ids": pr["images_out_of_date"]})
        src = pr.get("source") or {}
        item = by_id.get(src.get("item_id"))
        if item and src.get("article_version") and item["article_version"] != src["article_version"]:
            out["redraft"].append({"pack_id": pr["pack_id"], "pr": pr["number"], "item_id": item["id"],
                                   "from_version": src["article_version"], "to_version": item["article_version"]})

    # 4. fix PRs (E7): posts that need Nikolay again, and `fix` commands
    fix = {}
    for p in ledger_posts:
        if p.get("state") in FIX_STATES or "changed_in_tool" in (p.get("markers") or []):
            fix.setdefault(p["pack_id"], []).append({"post_id": p["post_id"], "why": p.get("reason") or p.get("state")})
    for c in commands:
        if c.get("kind") == "fix":
            parsed = ids.parse_post_id(c["post_id"])
            if parsed:
                fix.setdefault(parsed["pack_id"], []).append({"post_id": c["post_id"], "why": f"fix line {c.get('id')}"})
    out["fixes"] = [{"pack_id": k, "posts": v} for k, v in sorted(fix.items())]
    return out


def social_on_since(gh, brand_key):
    """When the team's settings merge switched social on (the merge time), from GitHub's record:
    the newest merged PR, by someone with write access, that changed settings.md. None without
    GitHub."""
    if gh is None:
        return None
    team = github.Team(gh)
    path = f"{brands.brand(brand_key)['dir']}/social/settings.md"
    for c in gh.commits(path):
        for simple in gh.commit_pulls(c["sha"]):
            if not simple.get("merged_at"):
                continue
            pr = gh.pull(simple["number"])               # the list form carries no merged_by
            if team.merged(pr):
                return pr["merged_at"]
    return None


def _git_show(root, ref, path):
    import subprocess
    try:
        return subprocess.run(["git", "show", f"{ref}:{path}"], cwd=root, capture_output=True, check=True,
                              timeout=30).stdout.decode("utf-8", "replace")
    except (OSError, subprocess.SubprocessError):
        return None


def branch_pack_state(root, brand_key, row):
    """{source, images_out_of_date, handled} of an open pack PR, read from its branch."""
    from social import pack as packmod
    rel = f"{brands.brand(brand_key)['dir']}/social/packs/{row['pack_id']}"
    ref = f"origin/{row.get('branch') or ''}"
    raw = _git_show(root, ref, f"{rel}/pack.json")
    if raw is None:
        return None
    meta = json.loads(raw)
    stale, handled = [], []
    for p in meta.get("posts", []):
        md = _git_show(root, ref, f"{rel}/posts/{p['post_id']}.md")
        if md is None:
            continue
        want = packmod.image_text_hash(packmod.parse_post_md(md))
        if any(v.get("image_text_hash") and v["image_text_hash"] != want for v in p.get("visuals") or []):
            stale.append(p["post_id"])
        handled += p.get("redo_notes") or []
    return {"source": meta.get("source"), "images_out_of_date": stale, "handled": handled}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("brand", nargs="?", default="vsichkikazina")
    ap.add_argument("--json")
    a = ap.parse_args(argv)
    root = brands.ROOT
    s = settingsmod.load(a.brand, root)
    ops = operators.current(a.brand, root, s.brand["operator_names_manual"])
    index = build_library.load_index(root, a.brand)
    items = {}
    for e in index.get("items", []):
        item, _ = build_library.load_item(root, a.brand, e["slug"])
        if item:
            items[e["slug"]] = item
    registry = board.parse_packs(board._read(board.packs_path(a.brand, root)))
    reqs, cmds = board.parse_requests(board._read(board.requests_path(a.brand, root)))
    commands = [c for c in (board.parse_command(r)[0] for r in cmds if r.get("status") == "open") if c]
    ledger = brands.social_dir(a.brand, root) / "ledger.json"
    ledger_posts = json.loads(ledger.read_text(encoding="utf-8")).get("posts", []) if ledger.exists() else []
    gh = github.from_env()
    since = social_on_since(gh, a.brand)

    def merged_at(n):
        if gh is None or n is None:
            return None
        try:
            pr = gh.pull(n)
        except github.GitHubError:
            return None
        return pr.get("merged_at")

    open_prs = []
    for row in registry:
        n = pr_number(row.get("pr"))
        if row.get("status") != "open" or n is None:
            continue
        state = branch_pack_state(root, a.brand, row) or {}
        comments = []
        if gh is not None:
            try:
                comments = [{"id": c["id"], "body": c.get("body", "")} for c in gh.issue_comments(n)]
            except github.GitHubError:
                comments = []
        open_prs.append({"pack_id": row["pack_id"], "number": n, "comments": comments, **state})
    result = work_list(s, index, items, registry, reqs, ops, since, merged_at, open_prs=open_prs,
                       ledger_posts=ledger_posts, commands=commands)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if a.json:
        Path(a.json).write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
