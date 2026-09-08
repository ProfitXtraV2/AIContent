import json
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


def test_write_feed_idempotent(tmp_path, monkeypatch):
    monkeypatch.setattr(bf, "list_branch_images", lambda folder: [])
    monkeypatch.setattr(bf, "read_branch_bytes", lambda folder, p: b"")

    meta = bf.build_meta(ROW, DRAFT4, [])
    meta["content_hash"] = bf.content_hash(DRAFT4["body"], meta)
    entry = {"meta": meta, "body": DRAFT4["body"], "folder": ROW["folder"]}

    # First write — files must be created.
    bf.write_feed([entry], tmp_path)

    slug_dir = tmp_path / meta["slug"]
    article_path = slug_dir / "article.md"
    meta_path = slug_dir / "meta.json"
    index_path = tmp_path / "index.json"

    assert article_path.exists()
    assert meta_path.exists()
    assert index_path.exists()

    index_data = json.loads(index_path.read_text(encoding="utf-8"))
    assert index_data["count"] == 1
    assert index_data["articles"][0]["content_hash"] == meta["content_hash"]

    # Trailing newline on index.json.
    assert index_path.read_text(encoding="utf-8").endswith("\n")

    # Idempotency — second call must not touch article.md.
    mtime_before = article_path.stat().st_mtime_ns
    bf.write_feed([entry], tmp_path)
    assert article_path.stat().st_mtime_ns == mtime_before, (
        "article.md was rewritten on second call despite unchanged content_hash"
    )

    # _existing_hash must agree with what we wrote.
    assert bf._existing_hash(slug_dir) == meta["content_hash"]


def test_read_article_md_fallback(tmp_path, monkeypatch):
    """When git show raises CalledProcessError, read_article_md reads from the local working tree."""
    import subprocess as _sp

    folder = "2026-09-07-fallback-test"

    # Patch subprocess.run to raise CalledProcessError for git show
    original_run = _sp.run
    def fake_run(args, **kwargs):
        if isinstance(args, list) and len(args) >= 2 and args[0] == "git" and args[1] == "show":
            raise _sp.CalledProcessError(128, args, output=b"", stderr=b"fatal: not a git repo")
        return original_run(args, **kwargs)
    monkeypatch.setattr(_sp, "run", fake_run)

    # Monkeypatch _repo_root so the fallback path uses tmp_path (isolated, no real-tree pollution)
    monkeypatch.setattr(bf, "_repo_root", lambda: tmp_path)

    # Create the local fallback file under tmp_path
    local_path = tmp_path / bf.ARTICLES_DIR / folder / "05b-final-draft.md"
    local_path.parent.mkdir(parents=True, exist_ok=True)
    local_path.write_text("# Fallback content\n\nLocal body.", encoding="utf-8")

    result = bf.read_article_md(folder)
    assert "# Fallback content" in result
