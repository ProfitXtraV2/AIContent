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
