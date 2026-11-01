#!/usr/bin/env python3
"""Source records for posts without a feed item (product spec A2; tech spec flow 1).

Facts for such posts come from the brand's own live editorial pages, from the pages and texts a
request names in its `sources`, and from the brand's own library articles. Before a line can be
recorded, this reads the source and confirms the line appears in it word for word. Kinds:
  page     a live editorial page of the brand's own (the live-page check reads it again at hand-over)
  outside  a page a request names that is not the brand's own (read once, when drafting)
  text     a text file a request names (<Brand>/social/sources/…), or a library article of the brand

    python3 scripts/social/source_record.py <url> --line "…" [--line "…"] [--brand vsichkikazina]

Prints {url, lines (confirmed), missing, fetched_utc, page_sha256} as JSON; exit 1 when a line is
missing or the page is not an allowed editorial page.
"""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import board, brands, links, operators, pagetext, settings as settingsmod  # noqa: E402


def _stamp(now):
    return (now or datetime.now(timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ")


def record(url, lines, brand_key, brand_settings, operator_names=(), fetch=operators.fetch, now=None, outside=False):
    """A page record. outside=True for a page the request itself names: it need not be the brand's own."""
    if outside:
        if not re.match(r"^https?://\S+$", url or ""):
            return {"kind": "outside", "url": url, "lines": [], "missing": list(lines), "error": "not a web address"}
    else:
        ok, why = links.allowed(url, brand_key, brand_settings, operator_names)
        if not ok:
            return {"url": url, "lines": [], "missing": list(lines), "error": f"not an allowed page: {why}"}
    try:
        html = fetch(url)
    except Exception as e:  # noqa: BLE001
        return {"kind": "outside" if outside else "page", "url": url, "lines": [], "missing": list(lines),
                "error": f"cannot read the page: {e}"}
    text = pagetext.visible_text(html)
    found = [ln for ln in lines if pagetext.contains(text, ln)]
    return {"kind": "outside" if outside else "page", "url": url, "lines": found,
            "missing": [ln for ln in lines if ln not in found], "fetched_utc": _stamp(now),
            "page_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()}


def text_record(ref, lines, brand_key, root=brands.ROOT, now=None):
    """A text record. ref: "sources/<file>.md" (under <Brand>/social/) or a library item ID."""
    import build_library                                          # only text sources need these two
    from social import checks
    root = Path(root)
    if board.SOURCE_FILE.match(ref or ""):
        p = brands.social_dir(brand_key, root) / ref
        if not p.exists():
            return {"kind": "text", "file": ref, "lines": [], "missing": list(lines), "error": "no such file"}
        text = checks.md_plain(p.read_text(encoding="utf-8"))
        rec = {"kind": "text", "file": ref}
    else:
        slug = next((e["slug"] for e in build_library.load_index(root, brand_key).get("items", []) if e["id"] == ref), None)
        item, article = build_library.load_item(root, brand_key, slug) if slug else (None, None)
        if item is None:
            return {"kind": "text", "item_id": ref, "lines": [], "missing": list(lines),
                    "error": "neither a sources/ file nor a library item"}
        text = checks.source_text(item, article)
        rec = {"kind": "text", "item_id": item["id"], "slug": item["slug"], "article_version": item["article_version"]}
    found = [ln for ln in lines if checks.md_plain(ln) in text]
    rec.update({"lines": found, "missing": [ln for ln in lines if ln not in found], "read_utc": _stamp(now),
                "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()})
    return rec


def main(argv=None):
    ap = argparse.ArgumentParser(description="Confirm lines on a live page")
    ap.add_argument("url")
    ap.add_argument("--line", action="append", default=[])
    ap.add_argument("--brand", default="vsichkikazina")
    a = ap.parse_args(argv)
    s = settingsmod.load(a.brand)
    ops = operators.current(a.brand, manual=s.brand["operator_names_manual"])
    rec = record(a.url, a.line, a.brand, s.brand, ops)
    print(json.dumps(rec, ensure_ascii=False, indent=2))
    return 0 if rec["lines"] and not rec["missing"] else 1


if __name__ == "__main__":
    sys.exit(main())
