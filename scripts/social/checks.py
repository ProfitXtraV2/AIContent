#!/usr/bin/env python3
"""The checks on a pack (product spec E3; tech spec flow 2, "Check | Rule | How").

    python3 scripts/social/checks.py <pack dir> [--brand vsichkikazina] [--root <main checkout>]
                                     [--pr-body <file>] [--json <out>] [--markdown <out>]

Reads the pack as data (it never runs anything from it), and settings, the library and the
operator list from --root (the main checkout). Exit 0 when every check passes, 1 otherwise.
The same code runs in the PR workflow, after merge, and again in the guest at hand-over.

Checks per post: length, hashtags, link, compliance, advertising, numbers, sources, verify,
instagram-url, carousel, images-fresh, visual; per pack: review-view. The English reference is
not a check: the drafting agent writes it, and the review view says when an edit outdated it.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_library  # noqa: E402
from social import brands, links, operators, pack as packmod, settings as settingsmod
from social import postnumbers as numbers  # noqa: E402

FLAG_RE = re.compile(r"\[(?:VERIFY|DATA NEEDED|CONFLICT|LINK NEEDED)\b[^\]\n]*\]")
VIEW_MARKER = re.compile(r"<!--\s*view:([0-9a-f]{64})\s*-->")
POST_CHECKS = ["length", "hashtags", "link", "compliance", "advertising", "numbers", "sources",
               "verify", "instagram-url", "carousel", "images-fresh", "visual"]


def norm(text):
    """Whitespace and non-breaking spaces made plain, for word-for-word comparisons."""
    return re.sub(r"\s+", " ", numbers.normalize(text)).strip()


def md_plain(md):
    """Markdown reduced to its words: emphasis, links and image syntax removed (the alt text
    and link text stay), so a sentence can be found word for word."""
    t = str(md or "")
    t = re.sub(r"<img[^>]*?alt=\"([^\"]*)\"[^>]*>", r"\1", t)
    t = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"(\*\*|__|\*|`)", "", t)
    t = re.sub(r"^\s{0,3}(#{1,6}|>|[-*+]|\d+\.)\s+", "", t, flags=re.M)
    t = t.replace("|", " ")
    return norm(t)


def source_text(item, article_text):
    """Everything a post drafted from a library item may quote: title, description, body and
    image alt texts (the article version, A8)."""
    parts = [item.get("title", ""), item.get("meta_description", ""), md_plain(article_text)]
    parts += [i.get("alt", "") for i in item.get("images", [])]
    return norm("\n".join(parts))


def expected_address(meta, post, brand_settings, brand_key):
    """The address the post will link to, as far as it is known at drafting: the article's
    address by pattern, a section intro's category page, or the recorded page."""
    src = meta.get("source") or {}
    target = (post.get("link") or {}).get("target")
    if target:
        return target
    if src.get("kind") == "intro" or str(src.get("slug", "")).startswith("hub-intro-"):
        cat = str(src.get("slug", "")).replace("hub-intro-", "", 1)
        return f"{brands.brand(brand_key)['site']}/blog/{cat}/"
    if src.get("slug"):
        return links.address_for(src["slug"], brand_settings)
    return None


class Context:
    """What the checks compare a pack with."""

    def __init__(self, brand_key, settings, operator_names, item=None, article_text="", pr_body=None):
        self.brand_key, self.settings, self.ops = brand_key, settings, operator_names
        self.item, self.article_text, self.pr_body = item, article_text, pr_body
        self.brand = brands.brand(brand_key)
        self.source_all = source_text(item, article_text) if item else ""


def _r(check, ok, detail=""):
    return {"check": check, "ok": bool(ok), "detail": detail}


def check_post(pack, post, fields, ctx):
    """[{check, ok, detail}] for one post."""
    b = ctx.settings.brand
    net = post.get("network", "")
    account = ctx.settings.account(post.get("account_id")) or {}
    netinfo = brands.NETWORKS.get(net, {})
    out = []
    text = fields.get("text", "")
    image_lines = fields.get("image_text") or []
    alt = fields.get("alt_text", "")
    tags = fields.get("hashtags") or []
    meta = pack["meta"]
    src = meta.get("source") or {}
    link = post.get("link") or {}
    source_lines = [s.get("line", "") for s in post.get("sources") or []]

    # length (B2)
    address = expected_address(meta, post, b, ctx.brand_key)
    tagged = links.tagged(address, net, link.get("campaign") or "", post["post_id"]) if address and net in brands.NETWORKS else ""
    full = packmod.publish_text(fields)
    n = numbers.length(full, net, link_length=len(tagged) if tagged else None)
    limit = netinfo.get("limit", 0)
    aim = netinfo.get("aim", (0, 0))
    out.append(_r("length", net in brands.NETWORKS and n <= limit,
                  f"{n} / {limit}" + (f" (aim {aim[0]}–{aim[1]})" if net != "x" else " (weighted, link 23)")))

    # hashtags (B2, D2): own hashtags within the account's max, total within the network's
    brand_tags = [t.lower() for t in b.get("brand_hashtags") or []]
    own = [t for t in tags if t.lower() not in brand_tags]
    inline = re.findall(r"(?<![\w#])#\w+", text)
    total = len(set(t.lower() for t in tags + inline))
    net_max = netinfo.get("hashtags", (0, 5))[1]
    acc_max = account.get("max_hashtags", net_max)
    missing_brand = [t for t in b.get("brand_hashtags") or [] if t.lower() not in [x.lower() for x in tags]]
    ok = total <= net_max and len(own) <= acc_max and not missing_brand
    detail = f"{total} (account max {acc_max} + {len(brand_tags)} brand, {net} max {net_max})"
    if missing_brand:
        detail += "; missing brand hashtag " + ", ".join(missing_brand)
    out.append(_r("hashtags", ok, detail))

    # link (B6)
    count = text.count(links.LINK)
    if link.get("mode") == "placeholder":
        ok, why = (links.allowed(address, ctx.brand_key, b, ctx.ops) if address else (False, "no address"))
        problems = []
        if count != 1:
            problems.append(f"[[LINK]] appears {count} times (once expected)")
        if not ok:
            problems.append(f"target {address}: {why}")
        if net == "instagram":
            problems.append("Instagram posts carry no link (link in profile)")
        if account.get("link") == "none":
            problems.append("this account is set to Link: none")
        want_campaign = src.get("slug") or src.get("request_id") or ""
        if link.get("campaign") != want_campaign:
            problems.append(f"utm_campaign {link.get('campaign')!r} should be {want_campaign!r}")
        if link.get("content") != post["post_id"]:
            problems.append(f"utm_content {link.get('content')!r} should be {post['post_id']!r}")
        out.append(_r("link", not problems, "; ".join(problems) or f"{address} (filled in when live)"))
    else:
        reason = link.get("reason", "")
        problems = []
        if reason not in links.NO_LINK_REASONS:
            problems.append(f"no link, and no allowed reason ({reason!r})")
        if net == "instagram" and reason != "link in profile":
            problems.append("an Instagram post's reason is 'link in profile'")
        if count:
            problems.append("the text holds [[LINK]] but the post has no link")
        out.append(_r("link", not problems, "; ".join(problems) or reason))

    # compliance (B5): the brand line word for word (the short form is allowed on X)
    lines_ok = [b.get("compliance_long", "")] + ([b.get("compliance_short", "")] if net == "x" else [])
    if not b.get("compliance_long"):                    # a topic with no line (sport, general): nothing to find
        out.append(_r("compliance", True, "n/a: the brand has no compliance line"))
    else:
        ok = any(line and norm(line) in norm(text) for line in lines_ok)
        out.append(_r("compliance", ok, "" if ok else f"missing the line: {lines_ok[-1]}"))

    # advertising (B5): no operator, no amount next to an offer word, no call to register or deposit
    fields_text = {"text": text, "image text": "\n".join(image_lines), "hashtags": " ".join(tags),
                   "alt text": alt, "link": address or ""}
    problems = []
    for where, value in fields_text.items():
        for name in operators.named(value.replace("-", " ") if where == "link" else value, ctx.ops):
            problems.append(f"{where} names {name}")
        amt = operators.offer_amount(value, b.get("offer_words") or [])
        if amt:
            problems.append(f"{where} states an offer amount ({amt})")
        low = value.lower()
        for w in b.get("register_words") or []:
            if re.search(r"(?<![\w])" + re.escape(w) + r"(?![\w])", low):
                problems.append(f"{where} invites to register or deposit ({w!r})")
    out.append(_r("advertising", not problems, "; ".join(dict.fromkeys(problems))))

    # numbers (B4): every number in text, image text and alt text in a recorded source line
    names = (b.get("allowed_number_names") or [])
    missing = numbers.unmatched(text, source_lines, "text", names)
    missing += numbers.unmatched("\n".join(image_lines), source_lines, "image", names)
    missing += numbers.unmatched(alt, source_lines, "text", names)
    joined_src = "\n".join(source_lines)
    bad_tags = [t for t in tags + inline if not numbers.hashtag_ok(t, names, joined_src)]
    problems = [f"{m} is not in a source line" for m in dict.fromkeys(missing)] + \
               [f"hashtag {t} has a number the source does not name" for t in bad_tags]
    out.append(_r("numbers", not problems, "; ".join(problems)))

    # sources (A9, A2): every recorded source line is in the article version or a source record
    # (a page of ours, a page or text the request gave, or an article of ours)
    problems = []
    if src.get("kind") == "page":
        recorded = {norm(line) for rec in src.get("records") or [] for line in rec.get("lines") or []}
        for line in source_lines:
            if norm(line) not in recorded:
                problems.append(f"not a recorded source line: {line[:80]}")
    else:
        if ctx.item is None:
            problems.append("the library item of this pack is missing")
        elif src.get("article_version") and src["article_version"] != ctx.item.get("article_version"):
            problems.append("the article changed since drafting (article version differs)")
        for line in source_lines:
            if ctx.item is not None and md_plain(line) not in ctx.source_all:
                problems.append(f"not in the article: {line[:80]}")
    out.append(_r("sources", not problems, "; ".join(problems)))
    return out + _post_checks_after_sources(pack, post, fields, ctx, net, netinfo, text, image_lines, alt, tags)


def _post_checks_after_sources(pack, post, fields, ctx, net, netinfo, text, image_lines, alt, tags):
    """verify, instagram-url, carousel, visual and images-fresh for one post."""
    out = []
    # verify (A2): no flag left
    flags = [f for v in (text, "\n".join(image_lines), alt) for f in FLAG_RE.findall(v)]
    out.append(_r("verify", not flags, "; ".join(flags)))

    # instagram-url (B6)
    if net == "instagram":
        bad = links.has_web_address(text) or links.has_web_address(" ".join(tags))
        out.append(_r("instagram-url", not bad, "the text holds a web address" if bad else ""))
    else:
        out.append(_r("instagram-url", True, "n/a"))

    # carousel (C4) and visual (C5)
    visuals = post.get("visuals") or []
    vdir = Path(pack["dir"]) / "visuals"
    present = [v for v in visuals if (vdir / v["file"]).exists()]
    if post.get("format") == "carousel":
        roles = [v.get("role") for v in present]
        problems = []
        most, wanted = netinfo.get("max_slides", 10), post.get("slides")
        if not 3 <= len(present) <= most:
            problems.append(f"{len(present)} slides (3–{most} on {net})")
        elif wanted and len(present) > wanted:
            problems.append(f"{len(present)} slides, more than the {wanted} set")
        if roles[:1] != ["cover"]:
            problems.append("the first slide is not the cover")
        if roles[-1:] != ["closing"]:
            problems.append("the last slide is not the closing slide")
        if len(image_lines) != len(present):
            problems.append(f"{len(image_lines)} image text lines for {len(present)} slides")
        if not netinfo.get("carousel"):
            problems.append(f"{net} takes no carousel (single image instead)")
        if ctx.brand["mark_18"] and not all(v.get("frame", {}).get("mark_18") for v in present):
            problems.append("a slide lacks the „18+“ mark")
        if not all(v.get("frame", {}).get("domain") for v in present):
            problems.append("a slide lacks the domain")
        fewer = f" ({wanted} set: the source has fewer points)" if wanted and len(present) < wanted else ""
        out.append(_r("carousel", not problems, "; ".join(problems) or f"{len(present)} slides{fewer}"))
    else:
        out.append(_r("carousel", True, "n/a"))
    gone = [v["file"] for v in visuals if v not in present]
    out.append(_r("visual", bool(present) and not gone,
                  "no visual" if not visuals else ("missing: " + ", ".join(gone) if gone else
                                                   ", ".join(f"{v['file']} ({v.get('kind')})" for v in present))))

    # images-fresh (E3): every image that shows the image text was made from the current text
    want = packmod.image_text_hash(fields)
    stale = [v["file"] for v in present if v.get("image_text_hash") and v["image_text_hash"] != want]
    out.append(_r("images-fresh", not stale, ("images out of date: " + ", ".join(stale)) if stale else ""))
    return out


def run(pack, ctx):
    """{"ok", "posts": {post_id: [results]}, "pack": [results], "deleted": [post ids]}."""
    deleted = packmod.deleted_posts(pack)
    results = {}
    for post in pack["meta"].get("posts", []):
        pid = post["post_id"]
        if pid in deleted:
            continue
        results[pid] = check_post(pack, post, pack["posts"][pid], ctx)
    pack_results = []
    if ctx.pr_body is not None:
        m = VIEW_MARKER.search(ctx.pr_body or "")
        want = packmod.files_hash(pack["dir"])
        ok = bool(m) and m.group(1) == want
        pack_results.append(_r("review-view", ok, "" if ok else "the review view does not show the current files"))
    ok = all(r["ok"] for rs in results.values() for r in rs) and all(r["ok"] for r in pack_results)
    return {"ok": ok, "posts": results, "pack": pack_results, "deleted": deleted}


def context_for(pack, brand_key, root, pr_body=None):
    s = settingsmod.load(brand_key, root)
    ops = operators.current(brand_key, root, s.brand["operator_names_manual"])
    src = pack["meta"].get("source") or {}
    item, article = (None, "")
    if src.get("slug"):
        item, article = build_library.load_item(root, brand_key, src["slug"])
    return Context(brand_key, s, ops, item, article or "", pr_body)


def markdown(result, pack_id):
    """The sticky comment: one line per post and check."""
    lines = [f"### Social checks — {pack_id}: {'all passing ✅' if result['ok'] else 'some failing ❌'}", "",
             "| Post | " + " | ".join(POST_CHECKS) + " |", "|---|" + "|".join("---" for _ in POST_CHECKS) + "|"]
    for pid, rs in result["posts"].items():
        by = {r["check"]: r for r in rs}
        lines.append(f"| `{pid}` | " + " | ".join("✅" if by[c]["ok"] else "❌" for c in POST_CHECKS) + " |")
    fails = [(pid, r) for pid, rs in result["posts"].items() for r in rs if not r["ok"]]
    fails += [("pack", r) for r in result["pack"] if not r["ok"]]
    if fails:
        lines += ["", "**What to fix**", ""]
        lines += [f"- `{pid}` · {r['check']}: {r['detail']}" for pid, r in fails]
    if result["deleted"]:
        lines += ["", "Deleted in this PR (not part of the pack): " + ", ".join(f"`{p}`" for p in result["deleted"])]
    for r in result["pack"]:
        if r["ok"]:
            lines += ["", f"- {r['check']}: up to date"]
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pack_dir")
    ap.add_argument("--brand", default="vsichkikazina")
    ap.add_argument("--root", default=str(brands.ROOT))
    ap.add_argument("--pr-body")
    ap.add_argument("--json")
    ap.add_argument("--markdown")
    a = ap.parse_args(argv)
    p = packmod.load(a.pack_dir)
    body = Path(a.pr_body).read_text(encoding="utf-8") if a.pr_body else None
    result = run(p, context_for(p, a.brand, Path(a.root), body))
    if a.json:
        Path(a.json).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md = markdown(result, p["meta"].get("pack_id", Path(a.pack_dir).name))
    if a.markdown:
        Path(a.markdown).write_text(md, encoding="utf-8")
    else:
        print(md)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
