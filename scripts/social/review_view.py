#!/usr/bin/env python3
"""The review view: a pack PR's description, built from its files (product spec E2).

    python3 scripts/social/review_view.py <pack dir> [--brand …] [--root <main>] [--sha <commit>]
                                          [--checks <checks.json>] [--out <file>]

In English. A summary table (post, account, network, format, provisional slot, characters
against the limit, hashtags, link or why there is none, checks), the source the pack was drafted
from, then each post: its own-language text, the English reference (the drafting agent's, marked
when an edit made it out of date), the image text, the images
(by commit-pinned raw address), the link with its tags and where every number comes from. The
hidden marker <!-- view:<sha256 of the pack files> --> lets the `review-view` check see whether
the description shows the current files. The workflow replaces the description with this, so
edits made in the description are overwritten (AC 38): edit the files instead.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import brands, checks, links, pack as packmod, settings as settingsmod  # noqa: E402

LANG = {"bg": "Bulgarian", "de": "German", "en": "English"}
NET_LABEL = {"facebook": "Facebook", "instagram": "Instagram", "x": "X", "linkedin-page": "LinkedIn Page",
             "linkedin-profile": "LinkedIn profile"}
RAW = "https://raw.githubusercontent.com/{repo}/{sha}/{path}"


def _quote(text):
    return "\n".join("> " + ln if ln else ">" for ln in str(text or "").strip().splitlines()) or "> (empty)"


def render(pack, result, settings, brand_key, commit_sha=None, repo="ProfitXtraV2/AIContent"):
    meta = pack["meta"]
    b = brands.brand(brand_key)
    lang = LANG.get(settings.brand.get("language", ""), settings.brand.get("language", ""))
    src = meta.get("source") or {}
    rel_dir = f"{b['dir']}/social/packs/{meta['pack_id']}"
    deleted = set(packmod.deleted_posts(pack))
    lines = [f"## Social pack `{meta['pack_id']}` — {b['name']}", ""]
    if src.get("kind") == "page":
        lines.append(f"**Source:** request `{src.get('request_id', '')}`, answered from the source records below "
                     f"(the brand's own pages and articles, and the sources the request named).")
    else:
        lines.append(f"**Source:** {src.get('kind', 'article')} `{src.get('item_id', '')}` "
                     f"(`{src.get('slug', '')}`), article version `{str(src.get('article_version', ''))[:12]}…`.")
    if meta.get("angle"):
        lines.append(f"**Angle:** {meta['angle']}")
    if meta.get("earlier_angles"):
        lines.append("**Earlier packs' angles:** " + "; ".join(meta["earlier_angles"]))
    lines += ["", "Edit the post files under **Files changed**; this description is rebuilt from them. "
              "Merge to approve (a merge by anyone with write access counts), close to reject.", ""]
    lines += ["| Post | Account | Network | Format | Slot | Characters | Hashtags | Link | Checks |",
              "|---|---|---|---|---|---|---|---|---|"]
    by_post = (result or {}).get("posts", {})
    for post in meta.get("posts", []):
        pid = post["post_id"]
        if pid in deleted:
            continue
        f = pack["posts"][pid]
        net = post["network"]
        rs = by_post.get(pid, [])
        passed = sum(1 for r in rs if r["ok"])
        length = next((r["detail"].split(" (")[0] for r in rs if r["check"] == "length"), "")
        link = post.get("link") or {}
        link_cell = "article link, filled in when live" if link.get("mode") == "placeholder" else link.get("reason", "")
        fmt = post.get("format", "single") + (" (fallback)" if post.get("carousel_fallback_note") else "")
        lines.append(f"| `{pid}` | {post['account_id']} | {NET_LABEL.get(net, net)} | {fmt} | first free slot after go-live "
                     f"| {length} | {len(f.get('hashtags') or [])} | {link_cell} | "
                     f"{'✅' if rs and passed == len(rs) else '❌'} {passed}/{len(rs)} |")
    if deleted:
        lines += ["", "Deleted in this PR (not part of the pack): " + ", ".join(f"`{d}`" for d in sorted(deleted))]
    for note in meta.get("notes") or []:
        lines.append(f"- Note: {note}")

    if src.get("kind") == "page":
        lines += ["", "### Source records", ""]
        for rec in src.get("records") or []:
            kind = rec.get("kind", "page")
            what = rec.get("url") if kind != "text" else (rec.get("file") or f"article `{rec.get('item_id', '')}`")
            label = {"page": "our page", "outside": "a page the request named", "text": "a text"}.get(kind, kind)
            lines.append(f"- {what} ({label}, read {rec.get('fetched_utc') or rec.get('read_utc') or '?'})"
                         + (f" ⚠️ {rec['error']}" if rec.get("error") else ""))
            lines += [f"  - „{ln}“" for ln in rec.get("lines") or []]
            lines += [f"  - ⚠️ not found in it: „{ln}“" for ln in rec.get("missing") or []]

    for post in meta.get("posts", []):
        pid = post["post_id"]
        if pid in deleted:
            continue
        f = pack["posts"][pid]
        net = post["network"]
        lines += ["", f"### `{pid}` · {NET_LABEL.get(net, net)} · {post['account_id']} · {post.get('role', '')}", ""]
        lines += [f"**Post text ({lang})**", "", _quote(packmod.publish_text(f)), ""]
        lines += ["**English reference (for review only, never published; written by the AI with the post)**", ""]
        if f.get("english") and not packmod.english_current(post, f):
            lines += ["> ⚠️ Written before the last edit of the text or the image text: it does not show that edit.", ">"]
        lines += [_quote(f.get("english") or "(none: the AI did not write one)"), ""]
        if f.get("image_text"):
            lines += ["**Image text**", ""] + [f"{i}. {t}" for i, t in enumerate(f["image_text"], 1)] + [""]
        if f.get("alt_text"):
            lines += [f"**Alt text:** {f['alt_text']}", ""]
        vis = post.get("visuals") or []
        if vis:
            lines.append("**Images**")
            lines.append("")
            for v in vis:
                path = f"{rel_dir}/visuals/{v['file']}"
                label = v.get("kind", "") + (f" — {v['fallback_case']}" if v.get("fallback_case") else "") + \
                    (f" — review {v['score']}" if v.get("score") is not None else "")
                if commit_sha:
                    lines.append(f"<img src=\"{RAW.format(repo=repo, sha=commit_sha, path=path)}\" width=\"220\" "
                                 f"alt=\"{v['file']}\"> `{v['file']}` ({label})")
                else:
                    lines.append(f"- `{v['file']}` ({label})")
            lines.append("")
        else:
            lines += ["**Images:** none — Held: no visual", ""]
        link = post.get("link") or {}
        if link.get("mode") == "placeholder":
            address = checks.expected_address(meta, post, settings.brand, brand_key) or "(address unknown)"
            lines += [f"**Link (filled in when live):** {links.tagged(address, net, link.get('campaign', ''), pid)}", ""]
        else:
            lines += [f"**Link:** none — {link.get('reason', '')}", ""]
        srcs = post.get("sources") or []
        if srcs:
            lines.append("**Where each number comes from**")
            lines.append("")
            for i, s in enumerate(srcs):
                nums = [n["value"] for n in post.get("numbers") or [] if n.get("source_index") == i]
                lines.append(f"- {', '.join(f'`{n}`' for n in nums) or '(no number)'} — „{s.get('line', '')}“ "
                             f"({s.get('where', '')})")
            lines.append("")
        for note in post.get("notes") or []:
            lines.append(f"- Note: {note}")
        fails = [r for r in by_post.get(pid, []) if not r["ok"]]
        if fails:
            lines += ["", "**Checks failing:** " + "; ".join(f"{r['check']}: {r['detail']}" for r in fails)]
    lines += ["", f"<!-- view:{packmod.files_hash(pack['dir'])} -->"]
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pack_dir")
    ap.add_argument("--brand", default="vsichkikazina")
    ap.add_argument("--root", default=str(brands.ROOT))
    ap.add_argument("--sha")
    ap.add_argument("--checks")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    p = packmod.load(a.pack_dir)
    s = settingsmod.load(a.brand, Path(a.root))
    result = json.loads(Path(a.checks).read_text(encoding="utf-8")) if a.checks else \
        checks.run(p, checks.context_for(p, a.brand, Path(a.root)))
    body = render(p, result, s, a.brand, a.sha)
    if a.out:
        Path(a.out).write_text(body, encoding="utf-8")
    else:
        print(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
