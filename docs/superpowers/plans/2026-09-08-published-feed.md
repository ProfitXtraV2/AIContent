# Published Feed (AIContent) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a generic, git-native `published/` feed to AIContent that exposes every
`approved` (ready-to-deploy) article as markdown + `meta.json` + images, plus an `index.json`
manifest, so any target site can pull and render it.

**Architecture:** One deterministic, stdlib-only script `scripts/build_feed.py` reads
`VsichkiKazina/content-queue.md` (reusing `build_dashboard.parse_queue`), selects rows with
`status: approved`, pulls each article's final files from its `content/<folder>` git branch,
and writes `published/<slug>/{article.md,meta.json,images/*}` + `published/index.json`. Pure
functions (parsing, meta, hashing, indexing) are unit-tested; a thin git/IO layer reads
branches and writes the tree.

**Tech Stack:** Python 3 (stdlib only: `json`, `re`, `hashlib`, `subprocess`, `pathlib`),
pytest (mirrors `scripts/tests/test_build_dashboard.py`), git.

## Global Constraints

- Stdlib-only — no pip dependencies (matches `build_dashboard.py`).
- Feed contains ONLY `status: approved` articles ("ready to deploy"); never `drafted`.
- Producer stays brand/target-agnostic: `section_hint` = the article's generic `type`
  (`guide`/`review`/`comparison`/`news`), NEVER a target site's category.
- `author` is always exactly `Георги Тодоров`.
- `schema_version` = `1` on every `meta.json` and on `index.json`.
- Deterministic output: same inputs → byte-identical files (except `index.json` `generated_utc`).
- Slug = article folder with a leading `YYYY-MM-DD-` stripped.
- Never fabricate content: the feed only ever copies what the article's branch already contains.

---

## File Structure

- Create `scripts/build_feed.py` — the feed builder (pure functions + IO layer + `main()`).
- Create `scripts/tests/test_build_feed.py` — pytest unit tests for the pure functions.
- Create `docs/PUBLISHED_FEED.md` — the human-readable contract (schema + example).
- Generated at runtime (not hand-authored): `published/index.json`,
  `published/<slug>/article.md`, `published/<slug>/meta.json`, `published/<slug>/images/*`.

---

## Task 1: Scaffolding + `slug_from_folder`

**Files:**
- Create: `scripts/build_feed.py`
- Test: `scripts/tests/test_build_feed.py`

**Interfaces:**
- Produces: `slug_from_folder(folder: str) -> str`; module constants `AUTHOR="Георги Тодоров"`,
  `SCHEMA_VERSION=1`, `ARTICLES_DIR="VsichkiKazina/articles"`.

- [ ] **Step 1: Write the failing test**

```python
# scripts/tests/test_build_feed.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_feed as bf

def test_slug_strips_leading_date():
    assert bf.slug_from_folder("2026-09-07-kak-raboti-razigravaneto") == "kak-raboti-razigravaneto"
    assert bf.slug_from_folder("2026-09-08-bakara-pravila") == "bakara-pravila"

def test_slug_without_date_is_unchanged():
    assert bf.slug_from_folder("some-slug") == "some-slug"

def test_module_constants():
    assert bf.AUTHOR == "Георги Тодоров"
    assert bf.SCHEMA_VERSION == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest scripts/tests/test_build_feed.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'build_feed'`.

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/build_feed.py
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest scripts/tests/test_build_feed.py -v`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/build_feed.py scripts/tests/test_build_feed.py
git commit -m "feat(feed): scaffold build_feed.py + slug_from_folder"
```

---

## Task 2: `parse_final_draft`

**Files:**
- Modify: `scripts/build_feed.py`
- Test: `scripts/tests/test_build_feed.py`

**Interfaces:**
- Produces: `parse_final_draft(md_text: str) -> dict` with keys
  `title_tag, meta_description, h1, body` (all strings; `body` is the markdown from the H1 on).

- [ ] **Step 1: Write the failing test**

```python
DRAFT = """Title tag: Как работи разиграването
Meta description: Кратко описание на разиграването и множителя.

---

# Как работи изискването за разиграване

Първи параграф с числа €100 и x30.

## Секция
Още текст.
"""

def test_parse_final_draft_fields():
    d = bf.parse_final_draft(DRAFT)
    assert d["title_tag"] == "Как работи разиграването"
    assert d["meta_description"] == "Кратко описание на разиграването и множителя."
    assert d["h1"] == "Как работи изискването за разиграване"
    assert d["body"].startswith("# Как работи изискването за разиграване")
    assert "Title tag:" not in d["body"]

def test_parse_final_draft_no_header():
    d = bf.parse_final_draft("# Само заглавие\n\nтекст")
    assert d["title_tag"] == ""
    assert d["h1"] == "Само заглавие"
    assert d["body"].startswith("# Само заглавие")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest scripts/tests/test_build_feed.py::test_parse_final_draft_fields -v`
Expected: FAIL — `AttributeError: module 'build_feed' has no attribute 'parse_final_draft'`.

- [ ] **Step 3: Write minimal implementation** (append to `scripts/build_feed.py`)

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest scripts/tests/test_build_feed.py -v`
Expected: PASS (5 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/build_feed.py scripts/tests/test_build_feed.py
git commit -m "feat(feed): parse_final_draft (title tag / meta / body)"
```

---

## Task 3: `extract_images`

**Files:**
- Modify: `scripts/build_feed.py`
- Test: `scripts/tests/test_build_feed.py`

**Interfaces:**
- Produces: `extract_images(body_markdown: str) -> list[dict]` — ordered, de-duped by `path`,
  each `{"path": "images/...", "alt": "..."}`. Handles both markdown `![alt](images/..)` and
  HTML `<img src="images/.." alt="..">`.

- [ ] **Step 1: Write the failing test**

```python
BODY_IMG = '''# Заглавие

![Инфографика за разиграване](images/razigravane.svg)

Текст.

<img src="images/hero.webp" alt="Декоративен банер" width="600">

![дубликат](images/razigravane.svg)
'''

def test_extract_images_md_and_html_deduped():
    imgs = bf.extract_images(BODY_IMG)
    assert imgs == [
        {"path": "images/razigravane.svg", "alt": "Инфографика за разиграване"},
        {"path": "images/hero.webp", "alt": "Декоративен банер"},
    ]

def test_extract_images_none():
    assert bf.extract_images("# Няма изображения\n\nтекст") == []
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest scripts/tests/test_build_feed.py::test_extract_images_md_and_html_deduped -v`
Expected: FAIL — `AttributeError: ... 'extract_images'`.

- [ ] **Step 3: Write minimal implementation** (append)

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest scripts/tests/test_build_feed.py -v`
Expected: PASS (7 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/build_feed.py scripts/tests/test_build_feed.py
git commit -m "feat(feed): extract_images (markdown + html, deduped)"
```

---

## Task 4: `build_meta` + `content_hash`

**Files:**
- Modify: `scripts/build_feed.py`
- Test: `scripts/tests/test_build_feed.py`

**Interfaces:**
- Consumes: a content-queue row dict (keys from `build_dashboard.COLUMNS`), a `parse_final_draft`
  dict, and an `extract_images` list.
- Produces: `build_meta(row: dict, draft: dict, images: list) -> dict` (no `content_hash` key)
  and `content_hash(body: str, meta: dict) -> str` (sha256 hex, ignores any `content_hash` key).

- [ ] **Step 1: Write the failing test**

```python
ROW = {
    "status": "approved", "type": "guide",
    "query": "Как работи изискването за разиграване (wagering)",
    "keywords_or_terms": "разиграване, wagering, бонус условия",
    "drafted_date": "2026-09-07", "folder": "2026-09-07-kak-raboti-razigravaneto",
}
DRAFT4 = {"title_tag": "Как работи разиграването",
          "meta_description": "Кратко описание.", "h1": "Как работи разиграването",
          "body": "# Как работи разиграването\n\nтекст €3,000"}
IMAGES4 = [{"path": "images/x.svg", "alt": "инфографика"}]

def test_build_meta_fields():
    meta = bf.build_meta(ROW, DRAFT4, IMAGES4)
    assert meta["schema_version"] == 1
    assert meta["slug"] == "kak-raboti-razigravaneto"
    assert meta["title"] == "Как работи разиграването"     # title_tag wins
    assert meta["meta_description"] == "Кратко описание."
    assert meta["author"] == "Георги Тодоров"
    assert meta["date_published"] == "2026-09-07"
    assert meta["keywords"] == ["разиграване", "wagering", "бонус условия"]
    assert meta["images"] == IMAGES4
    assert meta["section_hint"] == "guide"                 # generic type, not a site category
    assert meta["status"] == "approved"
    assert meta["body_path"] == "article.md"

def test_content_hash_is_deterministic_and_hash_key_independent():
    meta = bf.build_meta(ROW, DRAFT4, IMAGES4)
    h1 = bf.content_hash(DRAFT4["body"], meta)
    meta_with_hash = dict(meta, content_hash="ignored")
    h2 = bf.content_hash(DRAFT4["body"], meta_with_hash)
    assert h1 == h2 and len(h1) == 64
    h3 = bf.content_hash(DRAFT4["body"] + " changed", meta)
    assert h3 != h1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest scripts/tests/test_build_feed.py::test_build_meta_fields -v`
Expected: FAIL — `AttributeError: ... 'build_meta'`.

- [ ] **Step 3: Write minimal implementation** (append)

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest scripts/tests/test_build_feed.py -v`
Expected: PASS (9 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/build_feed.py scripts/tests/test_build_feed.py
git commit -m "feat(feed): build_meta + deterministic content_hash"
```

---

## Task 5: `select_approved` + `build_index`

**Files:**
- Modify: `scripts/build_feed.py`
- Test: `scripts/tests/test_build_feed.py`

**Interfaces:**
- Produces: `select_approved(queue_md: str) -> list[dict]` (rows with `status==approved` AND a
  non-empty `folder`); `build_index(entries: list[dict]) -> dict` where each entry is
  `{"meta": <meta-with-content_hash>}`.

- [ ] **Step 1: Write the failing test**

```python
QUEUE_MD = """# Content Queue
| id | status | type | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | approved | guide | A | a | 100 | 10 | research | 2026-09-07 |  | 2026-09-07-a | #1 | human 85 |  |
| 2 | drafted | guide | B | b | 200 | 20 | research | 2026-09-07 |  | 2026-09-07-b | #2 | human 84 |  |
| 3 | approved | review | C | c | 300 | 30 | research | 2026-09-06 |  | 2026-09-06-c | #3 | human 90 |  |
"""

def test_select_approved_only():
    rows = bf.select_approved(QUEUE_MD)
    assert [r["folder"] for r in rows] == ["2026-09-07-a", "2026-09-06-c"]

def test_build_index_shape():
    entries = [{"meta": {"slug": "a", "title": "A", "date_modified": "2026-09-07",
                         "content_hash": "h1", "status": "approved"}}]
    idx = bf.build_index(entries)
    assert idx["schema_version"] == 1 and idx["count"] == 1
    assert idx["articles"][0] == {"slug": "a", "title": "A",
                                  "date_modified": "2026-09-07",
                                  "content_hash": "h1", "status": "approved"}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest scripts/tests/test_build_feed.py::test_select_approved_only -v`
Expected: FAIL — `AttributeError: ... 'select_approved'`.

- [ ] **Step 3: Write minimal implementation** (append)

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest scripts/tests/test_build_feed.py -v`
Expected: PASS (11 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/build_feed.py scripts/tests/test_build_feed.py
git commit -m "feat(feed): select_approved (ready-to-deploy) + build_index"
```

---

## Task 6: Git IO layer (`read_article_md`, `list_branch_images`, `read_branch_bytes`)

**Files:**
- Modify: `scripts/build_feed.py`

**Interfaces:**
- Produces:
  - `read_article_md(folder: str) -> str` — the `05b-final-draft.md` text from `origin/content/<folder>`.
  - `list_branch_images(folder: str) -> list[str]` — repo-relative image paths under the article's `images/`.
  - `read_branch_bytes(folder: str, repo_rel_path: str) -> bytes` — raw bytes of a file on that branch.
- Note: these wrap `git` and are covered by the Task 8 integration/dry-run, not unit tests
  (they require a real repo with branches). Keep them tiny so `main()` stays testable-by-eye.

- [ ] **Step 1: Implement the IO layer** (append)

```python
def _ref(folder):
    return f"origin/content/{folder}"


def read_article_md(folder):
    ref, path = _ref(folder), f"{ARTICLES_DIR}/{folder}/05b-final-draft.md"
    return subprocess.run(["git", "show", f"{ref}:{path}"],
                          capture_output=True, text=True, check=True).stdout


def list_branch_images(folder):
    ref, base = _ref(folder), f"{ARTICLES_DIR}/{folder}/images/"
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", base],
                         capture_output=True, text=True).stdout
    return [l for l in out.splitlines() if l.strip()]


def read_branch_bytes(folder, repo_rel_path):
    ref = _ref(folder)
    return subprocess.run(["git", "show", f"{ref}:{repo_rel_path}"],
                          capture_output=True, check=True).stdout  # bytes (no text=True)
```

- [ ] **Step 2: Sanity-check import (no runtime call yet)**

Run: `python3 -c "import sys; sys.path.insert(0,'scripts'); import build_feed; print('ok')"`
Expected: prints `ok` (module still imports; new funcs defined).

- [ ] **Step 3: Commit**

```bash
git add scripts/build_feed.py
git commit -m "feat(feed): git IO layer to read approved articles from content branches"
```

---

## Task 7: `main()` + `write_feed` + contract doc

**Files:**
- Modify: `scripts/build_feed.py`
- Create: `docs/PUBLISHED_FEED.md`

**Interfaces:**
- Consumes: everything above.
- Produces: `write_feed(entries, out_root: Path) -> None` (writes `published/<slug>/…` +
  `index.json`, only rewriting files whose `content_hash` changed); `main() -> int`.

- [ ] **Step 1: Implement `write_feed` + `main`** (append)

```python
from datetime import datetime, timezone


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
        (slug_dir / "article.md").write_text(body, encoding="utf-8")
        (slug_dir / "meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        for repo_path in list_branch_images(folder):
            (slug_dir / "images" / Path(repo_path).name).write_bytes(
                read_branch_bytes(folder, repo_path))
    index = build_index(entries)
    index["generated_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (out_root / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


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
```

- [ ] **Step 2: Write the contract doc**

Create `docs/PUBLISHED_FEED.md`:

````markdown
# Published Feed — the contract

`published/` is AIContent's generic, git-native feed of **approved (ready-to-deploy)**
articles. Any target site pulls it and renders it. Built by `scripts/build_feed.py`.

## Layout
```
published/
  index.json                 # manifest (see below)
  <slug>/
    article.md               # final body (markdown, from the H1 on)
    meta.json                # metadata (schema below)
    images/…                 # the article's images (svg/webp)
```

## meta.json (schema_version 1)
| field | type | notes |
|---|---|---|
| schema_version | int | 1 |
| slug | string | folder minus leading YYYY-MM-DD- |
| title | string | title-tag (else H1, else query) |
| meta_description | string | ~120–160 chars |
| body_path | string | always "article.md" |
| author | string | "Георги Тодоров" |
| date_published / date_modified | string | ISO date |
| keywords | string[] | target keywords |
| images | array | {path, alt} |
| section_hint | string | generic type (guide/review/comparison/news) — NOT a site category |
| content_hash | string | sha256 of meta(minus hash)+body; drives idempotency |
| status | string | always "approved" (only ready-to-deploy articles are in the feed) |

## index.json
`{schema_version, count, generated_utc, articles:[{slug,title,date_modified,content_hash,status}]}`
— consumers diff `content_hash` to find new/changed articles.
````

- [ ] **Step 3: Run the full unit suite**

Run: `python3 -m pytest scripts/tests/test_build_feed.py -v`
Expected: PASS (11 tests — `main`/`write_feed`/IO are covered by the Task 8 dry-run).

- [ ] **Step 4: Commit**

```bash
git add scripts/build_feed.py docs/PUBLISHED_FEED.md
git commit -m "feat(feed): main + write_feed (idempotent) + PUBLISHED_FEED contract doc"
```

---

## Task 8: End-to-end dry-run + wire into the flow

**Files:**
- Modify: `VsichkiKazina/automation/daily-run.md` (add a feed-build step reference)

**Interfaces:**
- Consumes: a real repo with `origin/content/<folder>` branches and `content-queue.md`.

- [ ] **Step 1: Fetch branches and run the builder for real**

```bash
git fetch origin -q
python3 scripts/build_feed.py
```
Expected: prints `feed: N approved article(s) written to published/`. (N may be 0 if no rows
are `approved` yet — that is a valid result; the feed just has an empty `index.json`.)

- [ ] **Step 2: Verify the output shape**

```bash
python3 -c "import json;d=json.load(open('published/index.json'));print(d['schema_version'],d['count']);[print(a['slug'],a['status'],a['content_hash'][:8]) for a in d['articles']]"
```
Expected: `1 <count>` then one line per approved article; every `status` is `approved`.

- [ ] **Step 3: Verify idempotency (second run is a no-op on content)**

```bash
python3 scripts/build_feed.py
git status --porcelain published/
```
Expected: only `published/index.json` may show as modified (its `generated_utc` changes);
no `article.md`/`meta.json`/image churn for unchanged articles.

- [ ] **Step 4: Add the feed-build step to the daily run**

In `VsichkiKazina/automation/daily-run.md`, in the board-commit step (step 8), add this line
so the feed is refreshed whenever the board changes:

```markdown
- **Refresh the published feed.** Run `git fetch origin -q && python3 scripts/build_feed.py`
  and commit `published/` alongside the board — this exposes every `approved` article to
  consumers (the target-site publisher). It only ever includes `approved` (ready-to-deploy)
  articles; approving an article (status → approved) is what adds it to the feed.
```

- [ ] **Step 5: Commit**

```bash
git add published docs VsichkiKazina/automation/daily-run.md
git commit -m "feat(feed): wire build_feed into the daily run + first feed build"
```

---

## Self-Review

**1. Spec coverage (§2 of the spec — the contract):** feed layout (Task 7), `meta.json` schema
incl. `schema_version`/`slug`/`title`/`meta_description`/`author`/dates/`keywords`/`images`/
`section_hint`/`content_hash`/`status` (Task 4/7), `index.json` manifest (Task 5/7),
approved-only (Task 5), `build_feed.py` deterministic + stdlib (all tasks), wired into the flow
(Task 8). `section_hint` kept generic per the Global Constraints. ✅ No gaps.

**2. Placeholder scan:** no TBD/TODO; every code step has complete code; every test has real
assertions; commands have expected output. ✅

**3. Type consistency:** `parse_final_draft` returns `{title_tag, meta_description, h1, body}`
used identically in Task 4/7; `build_meta(row, draft, images)` and `content_hash(body, meta)`
signatures match their tests and `main()`; `entries` items are `{"meta","body","folder"}`
consumed the same way by `build_index` (via `e["meta"]`) and `write_feed`. ✅

---

## Next plan (not this one)
Sub-project 2 — **VsichkiKazina publisher** (brand-book, template, link-map, category-map,
`publish-run.md`, `seo_inspect.py`, `deploy_ftp.py`, state, scheduled routine). Gets its own
plan after this feed lands, since it consumes this contract.
