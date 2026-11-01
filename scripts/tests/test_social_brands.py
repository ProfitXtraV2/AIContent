"""Brands as data (social/brands.json, social/topics/), a new brand from the dashboard, and the
setup on a person's computer (scripts/social/local/)."""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "social" / "local"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_library  # noqa: E402
import run as local_run  # noqa: E402
import setup as local_setup  # noqa: E402
from social import brands, checks, intake, new_brand, settings as st  # noqa: E402
from test_social_drafting import repo_on  # noqa: E402
from test_social_intake import FakeGit, FakeGitHub  # noqa: E402


def with_social(tmp_path):
    """A repository with the article fixtures, plus the real brand list, topics and templates."""
    root = repo_on(tmp_path)
    shutil.copytree(ROOT / "social", root / "social", dirs_exist_ok=True)
    return root


def use_registry(monkeypatch, root):
    monkeypatch.setattr(brands, "BRANDS", brands.load_registry(root / "social" / "brands.json"))


# --- the brand list and the topics ---------------------------------------------------------------

def test_the_brands_and_topics_are_data():
    assert {"vsichkikazina", "dentalvia"} <= set(brands.BRANDS)
    assert brands.brand("vsichkikazina")["prefix"] == "vk" and brands.topic("vsichkikazina")["mark_18"] is True
    topics = brands.topics()
    assert {"casino", "betting", "sport", "dental", "general"} <= set(topics)
    for key, t in topics.items():
        assert t["label"]["bg"] and t["label"]["en"], key
        assert set(t["settings"]) >= {"bg", "en"}, key
        for values in t["settings"].values():
            assert set(values) <= set(st.BRAND_DEFAULTS), key       # only keys settings.md knows
    listed = brands.dashboard_list()
    assert [b["key"] for b in listed["brands"]][:2] == ["vsichkikazina", "dentalvia"]
    assert listed["brands"][0]["social"] is True and listed["brands"][1]["social"] is False   # DentalVia: no settings yet
    assert {t["key"] for t in listed["topics"]} == set(topics)


# --- a new brand -----------------------------------------------------------------------------------

def test_a_new_brand_of_each_kind(tmp_path, monkeypatch):
    root = with_social(tmp_path)
    key, written = new_brand.create(root, "Футбол 24", "https://www.futbol24.bg/", "sport", "bg")
    assert key == "futbol24"
    assert written[0] == "social/brands.json" and "Futbol24/social/settings.md" in written
    use_registry(monkeypatch, root)
    b = brands.brand("futbol24")
    assert (b["dir"], b["prefix"], b["domain"], b["topic"], b["mark_18"]) == ("Futbol24", "fu", "futbol24.bg", "sport", False)
    for rel in written:
        assert not re.search(r"\{\{\w+\}\}", (root / rel).read_text(encoding="utf-8")), rel   # every blank filled
    s = st.load("futbol24", root)
    assert s.errors == [] and s.brand["social"] is False and s.brand["compliance_long"] == ""   # sport: no line needed
    assert [a["account_id"] for a in s.accounts] == ["fb-futbol24", "ig-futbol24", "x-futbol24", "li-futbol24"]
    assert not any(a["active"] for a in s.accounts)
    prompt = (root / "Futbol24/social/prompts/post-writing.md").read_text(encoding="utf-8")
    assert "No betting: no odds, tips, bookmakers or calls to bet." in prompt and "Language:** Bulgarian" in prompt
    review = (root / "Futbol24/social/prompts/visual-review.md").read_text(encoding="utf-8")
    assert "18+" not in review                                       # no age mark for sport
    assert (root / "Futbol24/social/requests.md").read_text(encoding="utf-8").startswith("# Social requests and commands — Футбол 24")
    assert build_library.build(root, "futbol24") == ([], [])        # no article pipeline: posts on request only
    # a casino brand in German: the topic has no German lines, so the required one shows as missing
    key2, _ = new_brand.create(root, "Casino DE", "https://casino-info.de", "casino", "de")
    use_registry(monkeypatch, root)
    assert brands.brand(key2)["prefix"] not in ("vk", "dv", "fu") and brands.brand(key2)["mark_18"] is True
    assert [e["message"] for e in st.load(key2, root).errors] == ["compliance_long (the brand's compliance line) is empty"]
    # a betting brand in Bulgarian: 18+ and the betting words
    key3, _ = new_brand.create(root, "Залози", "https://zalozi.bg", "betting", "bg")
    use_registry(monkeypatch, root)
    s3 = st.load(key3, root)
    assert s3.errors == [] and s3.brand["compliance_long"].startswith("18+ Залаганията") and "фрийбет" in s3.brand["offer_words"]


def test_a_new_brand_that_cannot_be(tmp_path):
    root = with_social(tmp_path)
    for name, site, topic, language, why in (
            ("", "https://a.bg", "sport", "bg", "needs a name"),
            ("A", "http://a.bg", "sport", "bg", "must be an address like"),
            ("A", "https://a.bg", "poker", "bg", "unknown topic"),
            ("A", "https://a.bg", "sport", "bulgarian", "two-letter code"),
            ("Again", "https://www.vsichkikazina.bg", "casino", "bg", "already there")):
        try:
            new_brand.create(root, name, site, topic, language)
            raise AssertionError(f"created: {name} {site}")
        except ValueError as e:
            assert why in str(e), (why, str(e))
    assert json.loads((root / "social/brands.json").read_text(encoding="utf-8"))["brands"].keys() == {"vsichkikazina", "dentalvia"}


def test_the_dashboard_asks_for_a_new_brand(tmp_path):
    root = with_social(tmp_path)
    data = {"name": "Футбол 24", "site": "https://futbol24.bg", "topic": "sport", "language": "bg"}
    issue = {"title": "social: new brand Футбол 24", "user": {"login": "Ivana"},
             "body": f"<!-- social:brand {json.dumps(data, ensure_ascii=False)} -->\n**New brand:** …"}
    gh = FakeGitHub(issue)
    git = FakeGit(root, gh)
    msg = intake.handle(gh, git, root, 7)
    assert msg.startswith("Готово: марката „Футбол 24“ е в PR #12")
    branch, title, paths = git.log[0]
    assert branch == "settings/new-brand-futbol24-7" and title.startswith("social: new brand Футбол 24 (futbol24, #7, @Ivana)")
    assert "social/brands.json" in paths and "Futbol24/social/settings.md" in paths
    assert gh.pulls[0]["head"] == branch and "Everything starts switched off" in gh.pulls[0]["body"]
    # the same brand again is refused, nothing written
    msg2 = intake.handle(FakeGitHub(issue), FakeGit(root, gh), root, 7)
    assert msg2.startswith("Не стана: the brand futbol24 (futbol24.bg) is already there")


# --- settings: who publishes, and a topic with no compliance line ----------------------------------

def test_the_publisher_and_a_brand_without_a_compliance_line(tmp_path, monkeypatch):
    root = repo_on(tmp_path)
    path = root / "VsichkiKazina/social/settings.md"
    text = st.update(path.read_text(encoding="utf-8"), {"publisher": "@Ivana"})
    assert st.parse(text).brand["publisher"] == "Ivana" and st.parse(text).errors == []
    bad = st.update(text, {"publisher": "not a login!"})
    assert "publisher 'not a login!' is not a GitHub login" in [e["message"] for e in st.parse(bad).errors]
    # the compliance check: nothing to find when the brand has no line (sport, general)
    from test_social_drafting import DRAFT, offline
    from social import make_pack, pack as packmod
    d, _ = make_pack.build(DRAFT, "vsichkikazina", root, gemini=None, fetch=offline)
    path.write_text(st.update(path.read_text(encoding="utf-8"), {"compliance_long": "", "compliance_short": ""}), encoding="utf-8")
    p = packmod.load(d)
    r = checks.run(p, checks.context_for(p, "vsichkikazina", root))
    got = [x for rs in r["posts"].values() for x in rs if x["check"] == "compliance"]
    assert got and all(x["ok"] and x["detail"] == "n/a: the brand has no compliance line" for x in got)


# --- the setup on a person's computer ---------------------------------------------------------------

def test_the_team_code(tmp_path):
    folder = tmp_path / "postiz"
    folder.mkdir()
    (folder / ".env").write_text("PUBLIC_URL=https://x.ngrok-free.dev\nJWT_SECRET=secret-of-that-pc\n"
                                 "INSTAGRAM_APP_ID=123\nINSTAGRAM_APP_SECRET=abc\n", encoding="utf-8")
    (folder / "docker-compose.override.yaml").write_text('services:\n  postiz:\n    image: "ghcr.io/gitroomhq/postiz-app:v2.8.1"\n',
                                                         encoding="utf-8")
    team = local_setup.team_from(folder, "ProfitXtraV2/AIContent")
    assert team["env"] == {"INSTAGRAM_APP_ID": "123", "INSTAGRAM_APP_SECRET": "abc"}     # never that PC's own secret
    assert team["postiz_image"] == "ghcr.io/gitroomhq/postiz-app:v2.8.1"
    code = local_setup.encode_team(team)
    assert code.startswith("PXS1-") and local_setup.decode_team("  " + code[:30] + "\n" + code[30:]) == team
    for bad, why in (("hello", "PXS1-"), ("PXS1-@@@", "непълен")):
        try:
            local_setup.decode_team(bad)
            raise AssertionError(bad)
        except ValueError as e:
            assert why in str(e)


def test_linking_the_channels_of_this_postiz(tmp_path):
    accounts = [{"account_id": "fb-vk", "network": "facebook", "postiz_channel_id": ""},
                {"account_id": "ig-vk", "network": "instagram", "postiz_channel_id": ""},
                {"account_id": "x-vk", "network": "x", "postiz_channel_id": "x-old"},
                {"account_id": "li-vk", "network": "linkedin-page", "postiz_channel_id": ""}]
    channels = [{"id": "c-ig", "name": "@profit.xtra", "identifier": "instagram-standalone"},
                {"id": "c-fb1", "name": "Page one", "identifier": "facebook"},
                {"id": "c-fb2", "name": "Page two", "identifier": "facebook"},
                {"id": "x-old", "name": "@vk", "identifier": "x"},
                {"id": "c-li", "name": "Off", "identifier": "linkedin-page", "disabled": True}]
    sure, choose = local_setup.matches(accounts, channels)
    assert {a: c["id"] for a, c in sure.items()} == {"ig-vk": "c-ig", "x-vk": "x-old"}
    assert [c["id"] for c in choose["fb-vk"]] == ["c-fb1", "c-fb2"] and "li-vk" not in sure and "li-vk" not in choose
    # the issue it opens is the dashboard's: intake turns it into the settings change
    root = repo_on(tmp_path)
    body = local_setup.settings_issue_body("vsichkikazina", {"publisher": "Ivana"},
                                           {"ig-vsichkikazina": {"postiz_channel_id": "c-ig"}})
    data = intake.data_block(body, "settings")
    assert data == {"brand": "vsichkikazina", "brand_changes": {"publisher": "Ivana"},
                    "account_changes": {"ig-vsichkikazina": {"postiz_channel_id": "c-ig"}}}
    issue = {"title": "social: settings vsichkikazina", "user": {"login": "Ivana"}, "body": body}
    gh = FakeGitHub(issue)
    assert intake.handle(gh, FakeGit(root, gh), root, 7).startswith("Готово: промяната е в PR #12")
    s = st.load("vsichkikazina", root)
    assert s.brand["publisher"] == "Ivana" and s.account("ig-vsichkikazina")["postiz_channel_id"] == "c-ig"


def test_a_computer_publishes_only_its_own_brands(tmp_path, monkeypatch):
    root = repo_on(tmp_path)
    monkeypatch.setattr(local_run, "CODE", root)
    path = root / "VsichkiKazina/social/settings.md"
    assert local_run.my_brands(brands, st, "Ivana") == []                   # nobody named yet
    path.write_text(st.update(path.read_text(encoding="utf-8"), {"publisher": "Ivana"}), encoding="utf-8")
    assert local_run.my_brands(brands, st, "ivana") == ["vsichkikazina"]    # GitHub logins ignore case
    assert local_run.my_brands(brands, st, "AmigoNiko") == []
