#!/usr/bin/env python3
"""Build the published/ feed from approved articles. Deterministic, stdlib-only.

Brand-aware: reads <brand>/content-queue.md, selects status: approved rows, pulls each
article's final files from its git branch, and writes the per-brand output dir + index.json.
Run from repo root:
    python3 scripts/build_feed.py               # VsichkiKazina (default)
    python3 scripts/build_feed.py dentalvia     # DentalVia → published/dentalvia/
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

FEED_BRANDS = {
    "vsichkikazina": {"dir": "VsichkiKazina", "out": "published",
                      "branch_prefix": "content/", "author": AUTHOR},   # fixed VK author
    "dentalvia":     {"dir": "DentalVia", "out": "published/dentalvia",
                      "branch_prefix": "dv-content/", "author": None},  # None → row byline
}


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


def opportunity_score(volume, kd):
    """0–100 opportunity from the target keyword's volume + KD, mirroring
    build_dashboard.opportunity. Returns -1 when metrics are missing/unparseable so
    the publisher (which sorts by opportunity desc) puts unscored articles last."""
    try:
        v = float(str(volume).replace(",", "").strip())
        k = float(str(kd).replace(",", "").strip())
    except (TypeError, ValueError):
        return -1
    vol_score = min(60.0, v / 20.0)          # 1200+ volume saturates at 60
    kd_score = max(0.0, 40.0 - k * 0.4)      # KD 0 → 40, KD 100 → 0
    return int(round(vol_score + kd_score))


def build_meta(row, draft, images, author=AUTHOR):
    """Assemble the per-article meta.json (without content_hash) from a queue row + draft.

    ``author`` defaults to the module-level AUTHOR constant (VsichkiKazina); pass
    ``row["byline"]`` for DentalVia articles where the author comes from the queue row.
    """
    title = draft.get("title_tag") or draft.get("h1") or row.get("query", "")
    kws = [k.strip() for k in (row.get("keywords_or_terms", "") or "").split(",") if k.strip()]
    return {
        "schema_version": SCHEMA_VERSION,
        "slug": slug_from_folder(row["folder"]),
        "title": title,
        "meta_description": draft.get("meta_description", ""),
        "body_path": "article.md",
        "author": author,
        "date_published": row.get("drafted_date", ""),
        "date_modified": row.get("drafted_date", ""),
        "keywords": kws,
        "images": images,
        "section_hint": row.get("type", ""),
        "opportunity": opportunity_score(row.get("volume"), row.get("kd")),
        "status": "approved",
    }


def content_hash(body, meta):
    """Deterministic sha256 over (meta without content_hash) + body."""
    m = {k: v for k, v in meta.items() if k != "content_hash"}
    payload = json.dumps(m, ensure_ascii=False, sort_keys=True) + "\n" + body
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def select_approved(queue_md, brand="vsichkikazina"):
    """Content-queue rows that are ready to deploy: status == approved and have a folder."""
    return [r for r in bd.parse_queue(queue_md, brand=brand)
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


def _ref(folder, branch_prefix="content/"):
    return f"origin/{branch_prefix}{folder}"


def _repo_root():
    return Path(__file__).resolve().parents[1]


def read_article_md(folder, articles_dir=None, branch_prefix="content/"):
    """Read the 05b-final-draft.md for the given folder. Tries origin/<branch_prefix><folder>
    branch first; falls back to the local working tree if the branch is absent (e.g.
    after the PR was merged and the branch deleted)."""
    if articles_dir is None:
        articles_dir = ARTICLES_DIR
    ref = _ref(folder, branch_prefix)
    branch_path = f"{articles_dir}/{folder}/05b-final-draft.md"
    try:
        return subprocess.run(["git", "show", f"{ref}:{branch_path}"],
                              capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        local = _repo_root() / articles_dir / folder / "05b-final-draft.md"
        if not local.exists():
            raise FileNotFoundError(
                f"Article not found on branch '{ref}' or locally at '{local}'"
            )
        return local.read_text(encoding="utf-8")


def list_branch_images(folder, articles_dir=None, branch_prefix="content/"):
    """List repo-relative image paths for the given folder. Tries the content branch
    first; falls back to the local working tree images/ directory."""
    if articles_dir is None:
        articles_dir = ARTICLES_DIR
    ref = _ref(folder, branch_prefix)
    base = f"{articles_dir}/{folder}/images/"
    try:
        out = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", base],
                             capture_output=True, text=True, check=True).stdout
        lines = [line for line in out.splitlines() if line.strip()]
        if lines:
            return lines
    except subprocess.CalledProcessError:
        pass
    # Fallback: read from local images/ directory
    local_images = _repo_root() / articles_dir / folder / "images"
    if not local_images.is_dir():
        return []
    return [
        f"{articles_dir}/{folder}/images/{p.name}"
        for p in sorted(local_images.iterdir())
        if p.is_file()
    ]


def read_branch_bytes(folder, repo_rel_path, branch_prefix="content/"):
    """Read a file's bytes from the content branch, falling back to the local working tree."""
    ref = _ref(folder, branch_prefix)
    try:
        return subprocess.run(["git", "show", f"{ref}:{repo_rel_path}"],
                              capture_output=True, check=True).stdout  # bytes (no text=True)
    except subprocess.CalledProcessError:
        local = _repo_root() / repo_rel_path
        if not local.exists():
            raise FileNotFoundError(
                f"File not found on branch '{ref}' or locally at '{local}'"
            )
        return local.read_bytes()


def _existing_hash(slug_dir):
    meta = slug_dir / "meta.json"
    if meta.exists():
        try:
            return json.loads(meta.read_text(encoding="utf-8")).get("content_hash")
        except (ValueError, OSError):
            return None
    return None


def write_feed(entries, out_root, _list_images=None, _read_bytes=None):
    """Write <out_root>/<slug>/{article.md,meta.json,images/*} + index.json. Idempotent:
    an article whose content_hash is unchanged is skipped (no needless churn).

    ``_list_images(folder)`` and ``_read_bytes(folder, repo_rel_path)`` are optional
    callable overrides — defaults resolve to the module-level ``list_branch_images`` /
    ``read_branch_bytes`` so that test monkeypatching of those module-level names works
    transparently.  Pass brand-aware bound functions from ``main`` for non-VK brands.
    """
    if _list_images is None:
        _list_images = list_branch_images
    if _read_bytes is None:
        _read_bytes = read_branch_bytes
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
        image_paths = _list_images(folder)
        seen_basenames: dict[str, str] = {}
        for repo_path in image_paths:
            basename = Path(repo_path).name
            if basename in seen_basenames:
                raise ValueError(
                    f"Image basename collision in article '{meta['slug']}': "
                    f"'{seen_basenames[basename]}' and '{repo_path}' both resolve to '{basename}'"
                )
            seen_basenames[basename] = repo_path
            (slug_dir / "images" / basename).write_bytes(_read_bytes(folder, repo_path))
    index = build_index(entries)
    index["generated_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (out_root / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv=None):
    """Entry point. Optional positional arg: brand name (default: vsichkikazina).

    Examples::

        python3 scripts/build_feed.py                  # VsichkiKazina (default)
        python3 scripts/build_feed.py dentalvia        # DentalVia
    """
    if argv is None:
        argv = sys.argv[1:]
    brand = argv[0] if argv else "vsichkikazina"
    if brand not in FEED_BRANDS:
        print(f"error: unknown brand '{brand}'. Choose from: {', '.join(FEED_BRANDS)}",
              file=sys.stderr)
        sys.exit(1)
    cfg = FEED_BRANDS[brand]
    articles_dir = f"{cfg['dir']}/articles"
    branch_prefix = cfg["branch_prefix"]
    root = Path(__file__).resolve().parents[1]
    queue = (root / cfg["dir"] / "content-queue.md").read_text(encoding="utf-8")
    entries = []
    for row in select_approved(queue, brand=brand):
        folder = row["folder"]
        author = cfg["author"] if cfg["author"] is not None else row.get("byline", "")
        draft = parse_final_draft(
            read_article_md(folder, articles_dir=articles_dir, branch_prefix=branch_prefix))
        images = extract_images(draft["body"])
        meta = build_meta(row, draft, images, author=author)
        meta["content_hash"] = content_hash(draft["body"], meta)
        entries.append({"meta": meta, "body": draft["body"], "folder": folder})
    out_root = root / cfg["out"]
    # Bind brand-specific image/byte helpers so write_feed stays monkeypatch-friendly.
    _list_imgs = lambda folder: list_branch_images(  # noqa: E731
        folder, articles_dir=articles_dir, branch_prefix=branch_prefix)
    _read_bts = lambda folder, path: read_branch_bytes(  # noqa: E731
        folder, path, branch_prefix=branch_prefix)
    write_feed(entries, out_root, _list_images=_list_imgs, _read_bytes=_read_bts)
    print(f"feed: {len(entries)} approved article(s) written to {cfg['out']}/")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
