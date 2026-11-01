import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_library as bl  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "social"     # the boards as shipped, not the live ones

QUEUE = """# Content Queue
| id | status | type | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vk-0001 | posted | guide | Бакара | бакара, бакара правила | 100 | 10 | research | 2026-09-08 | 2026-09-09 | 2026-09-08-bakara-pravila | #1 | human 85 |  |
| vk-0002 | approved | guide | Разиграване | разиграване | 100 | 10 | research | 2026-09-08 |  | 2026-09-08-razigravane | #2 | human 85 |  |
| vk-0003 | posted | guide | Безплатни игри | игри | 100 | 10 | research | 2026-09-07 | 2026-09-08 | 2026-09-07-bezplatni | #3 | human 85 |  |
| vk-0004 | drafted | guide | Чернова | x | 100 | 10 | research | 2026-09-08 |  | 2026-09-08-chernova | #4 |  |  |
| vk-0005 | approved | guide | NV Casino бонус | nv casino | 100 | 10 | research | 2026-09-08 |  | 2026-09-08-nv-casino-bonus | #5 |  |  |
| vk-0119 | approved | hub-intro | HUB INTRO | плащания |  |  | backlog | 2026-09-19 |  | 2026-09-19-hub-intro-casino-payments | #140 |  |  |
"""

DRAFT = """Title tag: Бакара: правила и залози
Meta description: Правилата на бакара просто.

# Бакара: правила, залози

Банко 1:1 минус 5% комисиона.

![Трите залога: Банко ~1,06%](images/bakara-zalozi.svg)
<img src="images/bakara-hero.webp" alt="Две карти на везни" width="600">
"""

REVIEW = "# Image review pass 1\n\nScore: 100/100 (SVG) / 95/100 (hero) — PASS\n\nNo integrity failures.\n"


def make_repo(tmp):
    (tmp / "VsichkiKazina" / "social").mkdir(parents=True)
    (tmp / "VsichkiKazina" / "content-queue.md").write_text(QUEUE, encoding="utf-8")
    shutil.copy(FIXTURES / "settings.md", tmp / "VsichkiKazina" / "social" / "settings.md")
    (tmp / "VsichkiKazina" / "affiliate-links.md").write_text(
        "| operator | affiliate_url |\n|---|---|\n| NV Casino | https://vsichkikazina.bg/go/nv/ |\n", encoding="utf-8")
    for folder, draft in (("2026-09-08-bakara-pravila", DRAFT), ("2026-09-08-razigravane", "# Разиграване\n\nx40 на бонуса.\n"),
                          ("2026-09-08-nv-casino-bonus", "Title tag: NV Casino бонус 100% до €2000\n\n# NV\n\nтекст\n"),
                          ("2026-09-19-hub-intro-casino-payments", "Интро без H1.\n")):
        d = tmp / "VsichkiKazina" / "articles" / folder
        (d / "images").mkdir(parents=True)
        (d / "05b-final-draft.md").write_text(draft, encoding="utf-8")
    d = tmp / "VsichkiKazina" / "articles" / "2026-09-08-bakara-pravila"
    (d / "images" / "bakara-zalozi.svg").write_text("<svg>~1,06%</svg>", encoding="utf-8")
    (d / "images" / "bakara-hero.webp").write_bytes(b"RIFFhero")
    (d / "08-image-review-1.md").write_text("Score: 60/100 — NEEDS WORK", encoding="utf-8")
    (d / "08-image-review-2.md").write_text(REVIEW, encoding="utf-8")
    return tmp


def test_library_holds_approved_and_live_items_only(tmp_path):
    root = make_repo(tmp_path)
    items, missing = bl.build(root, now="2026-11-01T00:00:00Z")
    by_id = {e["item"]["id"]: e["item"] for e in items}
    assert sorted(by_id) == ["vk-0001", "vk-0002", "vk-0005", "vk-0119"]       # drafted vk-0004 is left out
    assert missing == [{"id": "vk-0003", "slug": "bezplatni", "board_status": "posted",
                        "reason": "no final draft (05b-final-draft.md)"}]
    one = by_id["vk-0001"]
    assert (one["slug"], one["kind"], one["board_status"], one["live"]) == ("bakara-pravila", "article", "posted", True)
    assert one["title"] == "Бакара: правила и залози" and one["meta_description"] == "Правилата на бакара просто."
    assert one["keywords"] == ["бакара", "бакара правила"]
    assert [(i["name"], i["review"]["score"], i["review"]["integrity_ok"], i["review"]["source"]) for i in one["images"]] == [
        ("bakara-zalozi.svg", 100, True, "08-image-review-2.md"), ("bakara-hero.webp", 95, True, "08-image-review-2.md")]
    assert one["images"][0]["path"] == "VsichkiKazina/articles/2026-09-08-bakara-pravila/images/bakara-zalozi.svg"
    assert by_id["vk-0119"]["kind"] == "hub-intro" and by_id["vk-0119"]["slug"] == "hub-intro-casino-payments"
    assert by_id["vk-0005"]["operator_or_bonus"] is True
    assert by_id["vk-0002"]["operator_or_bonus"] is False and by_id["vk-0002"]["live"] is False


def test_article_version_ignores_status_and_dates(tmp_path):
    root = make_repo(tmp_path)
    before = {e["item"]["id"]: e["item"]["article_version"] for e in bl.build(root)[0]}
    q = root / "VsichkiKazina" / "content-queue.md"
    q.write_text(QUEUE.replace("| vk-0002 | approved |", "| vk-0002 | posted |").replace("2026-09-08 |  | 2026-09-08-razigravane",
                                                                                          "2026-09-08 | 2026-11-02 | 2026-09-08-razigravane"),
                 encoding="utf-8")
    after = {e["item"]["id"]: e["item"] for e in bl.build(root)[0]}
    assert after["vk-0002"]["live"] is True
    assert after["vk-0002"]["article_version"] == before["vk-0002"]          # going live alone changes nothing
    d = root / "VsichkiKazina" / "articles" / "2026-09-08-razigravane" / "05b-final-draft.md"
    d.write_text("# Разиграване\n\nx35 на бонуса.\n", encoding="utf-8")
    assert {e["item"]["id"]: e["item"] for e in bl.build(root)[0]}["vk-0002"]["article_version"] != before["vk-0002"]


def test_write_is_idempotent_and_drops_unapproved_items(tmp_path):
    root = make_repo(tmp_path)
    lib = root / "library" / "vsichkikazina"
    items, missing = bl.build(root, now="2026-11-01T00:00:00Z")
    index = bl.write(lib, items, missing, "vsichkikazina")
    assert [i["id"] for i in index["items"]] == ["vk-0001", "vk-0002", "vk-0005", "vk-0119"]
    assert (lib / "bakara-pravila" / "article.md").read_text(encoding="utf-8").startswith("# Бакара: правила, залози")
    first = (lib / "bakara-pravila" / "item.json").read_text(encoding="utf-8")
    items, missing = bl.build(root, now="2026-11-05T00:00:00Z")
    bl.write(lib, items, missing, "vsichkikazina")
    assert (lib / "bakara-pravila" / "item.json").read_text(encoding="utf-8") == first   # built_utc kept
    q = root / "VsichkiKazina" / "content-queue.md"
    q.write_text(QUEUE.replace("| vk-0002 | approved |", "| vk-0002 | drafted |"), encoding="utf-8")
    items, missing = bl.build(root)
    bl.write(lib, items, missing, "vsichkikazina")
    assert not (lib / "razigravane").exists()
    item, text = bl.load_item(root, "vsichkikazina", "bakara-pravila")
    assert item["id"] == "vk-0001" and "Банко 1:1" in text


def test_review_scores_are_taken_only_when_unambiguous():
    names = ["a-hero.webp", "b.svg", "c.svg"]
    assert bl.review_scores("Score: 100/100 (SVG) / 95/100 (hero) — PASS", names) == {"a-hero.webp": 95}
    assert bl.review_scores("Score: 90/100 — PASS", ["only.webp"]) == {"only.webp": 90}
    assert bl.review_scores("Score: 90/100 — PASS", ["a.webp", "b.svg"]) == {}
    assert bl.review_scores("Score: 100/100 — PASS (both images)", ["a.webp", "b.svg"]) == {"a.webp": 100, "b.svg": 100}
    assert bl.review_scores("### pragmatic-hero.webp — SCORE 82/100 · PASS\n### chart.svg — SCORE 70/100",
                            ["pragmatic-hero.webp", "chart.svg"]) == {"pragmatic-hero.webp": 82, "chart.svg": 70}
    assert bl.integrity("No integrity failures on any image.") is True
    assert bl.integrity("**INTEGRITY FAILURE on the hero** (fake UI).") is False
    assert bl.integrity("Neither is an integrity failure.") is True
    assert bl.integrity("Looks fine.") is None


def test_svg_line_ends_do_not_change_the_article_version(tmp_path):
    """A Windows checkout turns an SVG's LF into CRLF; the library must not see a new version."""
    root = make_repo(tmp_path)
    svg = root / "VsichkiKazina" / "articles" / "2026-09-08-bakara-pravila" / "images" / "bakara-zalozi.svg"
    svg.write_bytes(b"<svg>\n~1,06%\n</svg>\n")
    lf = {e["item"]["id"]: e["item"]["article_version"] for e in bl.build(root)[0]}
    svg.write_bytes(b"<svg>\r\n~1,06%\r\n</svg>\r\n")
    crlf = {e["item"]["id"]: e["item"]["article_version"] for e in bl.build(root)[0]}
    assert lf == crlf
    assert bl.image_sha256("a.webp", b"x\r\n") != bl.image_sha256("a.webp", b"x\n")    # binary images as they are
