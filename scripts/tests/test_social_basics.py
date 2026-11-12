import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import ids, links, operators  # noqa: E402
from social import postnumbers as numbers  # noqa: E402

BRAND = {"allowed_link_areas": ["/blog/"], "address_pattern": "https://vsichkikazina.bg/blog/{slug}/"}
OPS = ["Betano", "NV Casino", "Winbet", "Ефбет"]


# --- IDs (B6) -----------------------------------------------------------------------------

def test_post_and_pack_ids():
    assert ids.post_id("vk-0300", 1, "facebook", 1) == "vk-0300-p1-fb-1"
    assert ids.post_id("vk-req-012", 1, "instagram", 1) == "vk-req-012-p1-ig-1"
    assert ids.post_id("vk-0300", 2, "linkedin-page", 3) == "vk-0300-p2-li-3"
    assert ids.parse_post_id("vk-0300-p1-x-2") == {"source": "vk-0300", "pack": 1, "net": "x", "k": 2,
                                                   "pack_id": "vk-0300-p1"}
    assert ids.parse_post_id("vk-0300-p1-tw-2") is None


def test_ids_are_never_reused():
    known = ["vk-0300-p1-fb-1", "vk-0300-p1-fb-3", "vk-0300-p1-ig-1", "vk-0301-p1-fb-9"]
    assert ids.next_post_ids("vk-0300", 1, "facebook", 2, known) == ["vk-0300-p1-fb-4", "vk-0300-p1-fb-5"]
    assert ids.next_pack_number("vk-0300", ["vk-0300-p1", "vk-0300-p3", "vk-0301-p7"]) == 4
    assert ids.next_request_id("vk", ["vk-req-009", "vk-req-012", "dv-req-099"]) == "vk-req-013"
    assert ids.next_request_id("vk", []) == "vk-req-001"


# --- links (B6, B7) -----------------------------------------------------------------------

def test_allowed_links():
    ok = lambda u: links.allowed(u, "vsichkikazina", BRAND, OPS)  # noqa: E731
    assert ok("https://vsichkikazina.bg/blog/bakara-pravila/") == (True, "")
    assert ok("https://vsichkikazina.bg/blog/casino-payments/") == (True, "")
    assert ok("https://vsichkikazina.bg/blog/") == (True, "")
    assert ok("https://vsichkikazina.bg/blog/bonus-bez-depozit-2026/") == (True, "")  # a year is no amount
    assert ok("https://vsichkikazina.bg/casino/betano/")[0] is False
    assert ok("https://vsichkikazina.bg/sravni-kazina/")[0] is False
    assert ok("https://vsichkikazina.bg/blog/a/b/")[0] is False
    assert ok("http://vsichkikazina.bg/blog/x/")[0] is False
    assert ok("https://example.com/blog/x/")[0] is False
    assert ok("https://vsichkikazina.bg/blog/nv-casino-zakonno-li-e/") == (False, "the address names the operator NV Casino")
    assert ok("https://vsichkikazina.bg/blog/efbet-bonus/") == (False, "the address names the operator Ефбет")
    assert ok("https://vsichkikazina.bg/blog/bonus-100-evro/") == (False, "the address shows a bonus amount")


def test_tags_and_profile_link():
    url = links.tagged("https://vsichkikazina.bg/blog/bakara-pravila/", "facebook", "bakara-pravila", "vk-0300-p1-fb-1")
    assert url == ("https://vsichkikazina.bg/blog/bakara-pravila/?utm_source=facebook&utm_medium=social"
                   "&utm_campaign=bakara-pravila&utm_content=vk-0300-p1-fb-1")
    assert links.tagged("https://vsichkikazina.bg/blog/x/", "linkedin-page", "x", "p").count("utm_source=linkedin") == 1
    assert links.profile_link("vsichkikazina", "ig-vsichkikazina") == (
        "https://vsichkikazina.bg/blog/?utm_source=instagram&utm_medium=social&utm_campaign=profile"
        "&utm_content=ig-vsichkikazina")
    assert links.address_for("bakara-pravila", BRAND) == "https://vsichkikazina.bg/blog/bakara-pravila/"


def test_web_addresses_in_text():
    assert links.has_web_address("Прочетете в профила ни.") is False
    assert links.has_web_address("Вижте vsichkikazina.bg/blog/x") is True
    assert links.has_web_address("Линк: [[LINK]]") is True
    assert links.has_web_address("https://x.y") is True


# --- numbers (B4) and length (B2) ---------------------------------------------------------

SOURCE = ["Банко 1:1 минус 5% комисиона с домашно предимство ~1,06%.",
          "Пример: €1 000 оборот, очаквана загуба Банко ~€11, Равенство ~€144.",
          "Изискване за разиграване x40 на бонуса."]


def test_number_tokens():
    assert numbers.tokens("Банко 1:1 и ~1,06% при €1 000, x40 и 3/6. 18+") == \
        ["1:1", "~1,06%", "€1 000", "x40", "3/6", "18+"]
    assert numbers.tokens("Линк [[LINK]] и https://x.bg/blog/a-2026/?utm_content=vk-0300-p1-fb-1") == []


def test_numbers_must_appear_exactly():
    assert numbers.unmatched("Комисионата е 5%, а предимството ~1,06%.", SOURCE) == []
    assert numbers.unmatched("Предимството е 1,06%.", SOURCE) == []           # found inside ~1,06%
    assert numbers.unmatched("Предимството е 1.06%.", SOURCE) == ["1.06%"]    # formatting differs
    assert numbers.unmatched("Оборот €1000.", SOURCE) == ["€1000"]
    assert numbers.unmatched("Загуба €14.", SOURCE) == ["€14"]                 # not inside €144
    assert numbers.unmatched("Само 10 думи.", ["100 думи"]) == ["10"]


def test_b4_exceptions():
    assert numbers.unmatched("18+ Играйте отговорно.", SOURCE) == []
    assert numbers.unmatched("3/6", SOURCE, where="image") == []
    assert numbers.unmatched("3/6", SOURCE, where="text") == ["3/6"]
    names = ["Gates of Olympus 1000"]
    assert numbers.unmatched("Новото в Gates of Olympus 1000", [], names=names) == []
    assert numbers.hashtag_ok("#GatesOfOlympus1000", names, "") is True
    assert numbers.hashtag_ok("#20SuperHot", [], "Играта 20 Super Hot има 5 линии") is True
    assert numbers.hashtag_ok("#Бонус100", [], "нищо") is False
    assert numbers.hashtag_ok("#бакара", [], "") is True


def test_x_length():
    assert numbers.x_length("Бакара: правила") == 15
    assert numbers.x_length("Прочетете: [[LINK]]") == 11 + 23
    assert numbers.x_length("👍") == 2
    assert numbers.x_length("👍🏽") == 2                     # skin tone is part of the emoji
    assert numbers.x_length("👨‍👩‍👧") == 2                   # one family emoji
    assert numbers.x_length("中文") == 4
    assert numbers.x_length("a–b") == 3                      # en dash weighs 1
    assert numbers.length("abc [[LINK]]", "facebook", link_length=100) == 104


# --- operators (A7, B5) -------------------------------------------------------------------

AFFILIATE = """| operator | affiliate_url | landing | status | source_page | last_checked |
|---|---|---|---|---|---|
| Betano | https://vsichkikazina.bg/go/betano/ | welcome bonus | active | /casino/betano/ | 2026-09-13 |
| Elitbet | https://vsichkikazina.bg/go/elitbet/ | spins | active | /casino/elitbet/ | 2026-09-19 |
"""

SITEMAP = """<urlset><url><loc>https://vsichkikazina.bg/casino/</loc></url>
<url><loc>https://vsichkikazina.bg/casino/nv-casino/</loc></url>
<url><loc>https://vsichkikazina.bg/casino/efbet/</loc></url>
<url><loc>https://vsichkikazina.bg/blog/bakara-pravila/</loc></url></urlset>"""


def test_operator_list_sources():
    assert operators.from_affiliate(AFFILIATE) == ["Betano", "Elitbet"]
    assert operators.casino_pages(SITEMAP) == ["https://vsichkikazina.bg/casino/efbet/",
                                               "https://vsichkikazina.bg/casino/nv-casino/"]
    assert operators.h1_of("<html><h1 class='t'>Ефбет <span>казино ревю</span> 2026</h1></html>") == "Ефбет казино ревю 2026"
    assert operators.name_from_h1("Ефбет казино ревю 2026 — бонуси и мнения") == "Ефбет"
    names = operators.build_list(["Betano"], [("https://vsichkikazina.bg/casino/efbet/", "Ефбет казино ревю")],
                                 ["betano", "Palms Bet"])
    assert names == ["Betano", "Palms Bet", "efbet", "Ефбет"]


def test_refresh_keeps_the_last_good_site_list(tmp_path):
    (tmp_path / "VsichkiKazina" / "social").mkdir(parents=True)
    (tmp_path / "VsichkiKazina" / "affiliate-links.md").write_text(AFFILIATE, encoding="utf-8")
    pages = {"https://vsichkikazina.bg/sitemap.xml": SITEMAP,
             "https://vsichkikazina.bg/casino/nv-casino/": "<h1>NV Casino ревю</h1>",
             "https://vsichkikazina.bg/casino/efbet/": "<h1>Ефбет казино</h1>"}
    names = operators.refresh("vsichkikazina", tmp_path, manual=["Palms Bet"], get=pages.__getitem__)
    assert names == ["Betano", "Elitbet", "Palms Bet", "efbet", "Ефбет", "nv casino"]

    def down(url):
        raise OSError("site down")
    assert operators.refresh("vsichkikazina", tmp_path, get=down) == ["Betano", "Elitbet", "efbet", "Ефбет", "nv casino"]
    assert operators.current("vsichkikazina", tmp_path) == ["Betano", "Elitbet", "efbet", "Ефбет", "nv casino"]


def test_a7_screen():
    offer = ["бонус", "оферта", "free spins"]
    s = lambda t, slug="x", kw=(): operators.screen(t, slug, kw, OPS, offer)  # noqa: E731
    assert s("NV Casino: законно ли е?", "nv-casino-zakonno-li-e") == (True, "names the operator NV Casino")
    assert s("NV Casino бонус: какво реално означава 100% до €2000 при x40")[0] is True
    assert s("Бонус без депозит 2026: как работят", "bonus-bez-depozit-2026") == (False, "")
    assert s("Как работи разиграването", "kak-raboti-razigravaneto") == (False, "")
    assert s("Ръководство", "efbet-pravila") == (False, "")      # slug words are Latin, the name Cyrillic
    assert s("Ръководство", "winbet-pravila") == (True, "names the operator Winbet")
    assert s("Бонус до €500 за нови играчи") == (True, "its title states a bonus amount (€500)")
    assert s("Как се играе", kw=["betano вход"]) == (True, "names the operator Betano")
    assert operators.named("Бетано не е Betano-та", OPS) == ["Betano"]
    assert operators.offer_amount("Пример: €1 000 оборот при x40.", offer) == ""
