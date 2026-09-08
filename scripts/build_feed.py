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
from datetime import datetime, timezone
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
    start = next((i for i, line in enumerate(body_lines) if line.startswith("# ")), 0)
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


def select_approved(queue_md):
    """Content-queue rows that are ready to deploy: status == approved and have a folder."""
    return [r for r in bd.parse_queue(queue_md)
            if r.get("status", "").lower() == "approved" and r.get("folder")]


def build_index(entries):
    """Manifest of the feed: one lightweight row per article for cheap diffing."""
    return {
        "schema_version": SCHEMA_VERSION,
        "count": len(entries),
        "articles": [
            {"slug": e["meta"]["slug"], "title": e["meta"]["title"],
             "date_modified": e["meta"]["date_modified"],
             "content_hash": e["meta"]["content_hash"], "status": e["meta"]["status"]}
            for e in entries
        ],
    }


def _ref(folder):
    return f"origin/content/{folder}"


def read_article_md(folder):
    ref, path = _ref(folder), f"{ARTICLES_DIR}/{folder}/05b-final-draft.md"
    return subprocess.run(["git", "show", f"{ref}:{path}"],
                          capture_output=True, text=True, check=True).stdout


def list_branch_images(folder):
    ref, base = _ref(folder), f"{ARTICLES_DIR}/{folder}/images/"
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", base],
                         capture_output=True, text=True, check=True).stdout
    return [line for line in out.splitlines() if line.strip()]


def read_branch_bytes(folder, repo_rel_path):
    ref = _ref(folder)
    return subprocess.run(["git", "show", f"{ref}:{repo_rel_path}"],
                          capture_output=True, check=True).stdout  # bytes (no text=True)


def _existing_hash(slug_dir):
    meta = slug_dir / "meta.json"
    if meta.exists():
        try:
            return json.loads(meta.read_text(encoding="utf-8")).get("content_hash")
        except (ValueError, OSError):
            return None
    return None


def write_feed(entries, out_root):
    """Write published/<slug>/{article.md,meta.json,images/*} + index.json. Idempotent:
    an article whose content_hash is unchanged is skipped (no needless churn)."""
    out_root.mkdir(parents=True, exist_ok=True)
    for e in entries:
        meta, body, folder = e["meta"], e["body"], e["folder"]
        slug_dir = out_root / meta["slug"]
        if _existing_hash(slug_dir) == meta["content_hash"]:
            continue                                   # unchanged → skip
        (slug_dir / "images").mkdir(parents=True, exist_ok=True)
        (slug_dir / "article.md").write_text(body + "\n", encoding="utf-8")
        (slug_dir / "meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        # Images are expected to be flat within images/ — check for basename collisions.
        image_paths = list_branch_images(folder)
        seen_basenames: dict[str, str] = {}
        for repo_path in image_paths:
            basename = Path(repo_path).name
            if basename in seen_basenames:
                raise ValueError(
                    f"Image basename collision in article '{meta['slug']}': "
                    f"'{seen_basenames[basename]}' and '{repo_path}' both resolve to '{basename}'"
                )
            seen_basenames[basename] = repo_path
            (slug_dir / "images" / basename).write_bytes(
                read_branch_bytes(folder, repo_path))
    index = build_index(entries)
    index["generated_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (out_root / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    root = Path(__file__).resolve().parents[1]
    queue = (root / "VsichkiKazina" / "content-queue.md").read_text(encoding="utf-8")
    entries = []
    for row in select_approved(queue):
        folder = row["folder"]
        draft = parse_final_draft(read_article_md(folder))
        images = extract_images(draft["body"])
        meta = build_meta(row, draft, images)
        meta["content_hash"] = content_hash(draft["body"], meta)
        entries.append({"meta": meta, "body": draft["body"], "folder": folder})
    write_feed(entries, root / "published")
    print(f"feed: {len(entries)} approved article(s) written to published/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
