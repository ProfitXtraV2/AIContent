#!/usr/bin/env python3
"""Build the generic published/ feed from approved articles. Deterministic, stdlib-only.

Reads VsichkiKazina/content-queue.md, selects status: approved rows, pulls each article's
final files from its content/<folder> git branch, and writes published/<slug>/ + index.json.
Run from repo root:  python3 scripts/build_feed.py
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_dashboard as bd  # reuse parse_queue

AUTHOR = "Георги Тодоров"
SCHEMA_VERSION = 1
ARTICLES_DIR = "VsichkiKazina/articles"


def slug_from_folder(folder):
    """Article slug = folder with any leading YYYY-MM-DD- stripped."""
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", folder.strip())


def parse_final_draft(md_text):
    """Split a 05b draft into its 'Title tag:'/'Meta description:' header and the body
    (from the first H1 on). Missing header fields return empty strings."""
    parts = md_text.split("\n---\n", 1)
    if len(parts) == 2:
        head, rest = parts
    else:
        head, rest = "", md_text
    title_tag = meta_description = ""
    for line in head.splitlines():
        low = line.lower()
        if low.startswith("title tag:"):
            title_tag = line.split(":", 1)[1].strip()
        elif low.startswith("meta description:"):
            meta_description = line.split(":", 1)[1].strip()
    body_lines = rest.strip().splitlines()
    # body starts at the first H1 if present, else the whole remainder
    start = next((i for i, l in enumerate(body_lines) if l.startswith("# ")), 0)
    body = "\n".join(body_lines[start:]).strip()
    h1 = ""
    for line in body.splitlines():
        if line.startswith("# "):
            h1 = line[2:].strip()
            break
    return {"title_tag": title_tag, "meta_description": meta_description,
            "h1": h1, "body": body}


_MD_IMG = re.compile(r"!\[([^\]]*)\]\((images/[^)]+)\)")
_HTML_IMG = re.compile(r'<img[^>]*?src="(images/[^"]+)"[^>]*?alt="([^"]*)"')


def extract_images(body_markdown):
    """All local image refs (markdown + <img>), ordered, de-duped by path."""
    found = []
    for m in _MD_IMG.finditer(body_markdown):
        found.append({"path": m.group(2).strip(), "alt": m.group(1).strip()})
    for m in _HTML_IMG.finditer(body_markdown):
        found.append({"path": m.group(1).strip(), "alt": m.group(2).strip()})
    seen, out = set(), []
    for img in found:
        if img["path"] in seen:
            continue
        seen.add(img["path"])
        out.append(img)
    return out


def build_meta(row, draft, images):
    """Assemble the per-article meta.json (without content_hash) from a queue row + draft."""
    title = draft.get("title_tag") or draft.get("h1") or row.get("query", "")
    kws = [k.strip() for k in (row.get("keywords_or_terms", "") or "").split(",") if k.strip()]
    return {
        "schema_version": SCHEMA_VERSION,
        "slug": slug_from_folder(row["folder"]),
        "title": title,
        "meta_description": draft.get("meta_description", ""),
        "body_path": "article.md",
        "author": AUTHOR,
        "date_published": row.get("drafted_date", ""),
        "date_modified": row.get("drafted_date", ""),
        "keywords": kws,
        "images": images,
        "section_hint": row.get("type", ""),
        "status": "approved",
    }


def content_hash(body, meta):
    """Deterministic sha256 over (meta without content_hash) + body."""
    m = {k: v for k, v in meta.items() if k != "content_hash"}
    payload = json.dumps(m, ensure_ascii=False, sort_keys=True) + "\n" + body
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
