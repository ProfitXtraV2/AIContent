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
