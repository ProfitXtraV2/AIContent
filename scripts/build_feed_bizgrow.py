#!/usr/bin/env python3
"""Build the Xtra AI (BizGrow folder) article feed. Deterministic, stdlib-only.

Reads BizGrow/content-queue.md and lists approved/posted /saveti/ articles whose content file
is on main, for the biz-grow publisher routine. Writes BizGrow/published/index.json.
Run from repo root:  python3 scripts/build_feed_bizgrow.py
"""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_dashboard as bd  # reuse parse_queue (same 14-column table as VsichkiKazina)

SCHEMA_VERSION = 1
_TOML_LINE = re.compile(r'^(title|locale|last_updated)\s*=\s*"(.*)"\s*$')


def _front_matter(text):
    m = re.match(r"^\+\+\+\r?\n(.*?)\r?\n\+\+\+", text, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        hit = _TOML_LINE.match(line.strip())
        if hit:
            out[hit.group(1)] = hit.group(2)
    return out


def build(root, now=None):
    root = Path(root)
    queue = (root / "BizGrow" / "content-queue.md").read_text(encoding="utf-8")
    articles = []
    for r in bd.parse_queue(queue):
        query = (r.get("query") or "").strip()
        if r.get("status") not in ("approved", "posted") or not query.startswith("/saveti/"):
            continue
        slug = query.strip("/").split("/")[-1]
        folder = (r.get("folder") or "").strip()
        rel = f"BizGrow/articles/{folder}/content/{slug}.md"
        path = root / rel
        if not folder or not path.is_file():
            print(f"skip {slug}: {rel} not found", file=sys.stderr)
            continue
        raw = path.read_bytes()
        fm = _front_matter(raw.decode("utf-8"))
        articles.append({
            "slug": slug,
            "folder": folder,
            "locale": fm.get("locale", "bg"),
            "path": f"/saveti/{slug}/",
            "title": fm.get("title", slug),
            "content_path": rel,
            "content_hash": hashlib.sha256(raw).hexdigest(),
            "date_modified": fm.get("last_updated", ""),
            "status": "approved",
        })
    articles.sort(key=lambda a: a["slug"])
    return {
        "schema_version": SCHEMA_VERSION,
        "brand": "bizgrow",
        "count": len(articles),
        "generated_utc": now or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "articles": articles,
    }


def write(root, feed):
    out = Path(root) / "BizGrow" / "published" / "index.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(feed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    repo = Path(__file__).resolve().parents[1]
    print(write(repo, build(repo)))
