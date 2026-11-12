import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import settings as st  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SHIPPED = Path(__file__).resolve().parent / "fixtures" / "social" / "settings.md"

GOOD = """# Social settings

## Brand
| key | value |
|---|---|
| social | on |
| pause | off |
| time_zone | Europe/Sofia |
| language | bg |
| compliance_long | 18+ Хазартът може да пристрасти. Играйте отговорно. |
| compliance_short | 18+ Играйте отговорно. |
| eligible_types | guide, comparison, review, news |
| allowed_link_areas | /blog/ |
| address_pattern | https://vsichkikazina.bg/blog/{slug}/ |
| brand_hashtags | #ВсичкиКазина |
| identities_verified | 2026-11-01 (SOCIAL-SETUP.md#identities) |
| offer_words | бонус, оферта |

## Accounts
| account_id | network | postiz_channel_id | active | posts_per_article | followup_delay_days | format | max_hashtags | link | slots | max_per_day | emoji | tone_override | test_post_seen | profile_link_set |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fb-vk | facebook | ch1 | on | 2 | 14 | auto | 2 | in post | daily 12:30, 19:30 | 2 | light |  | 2026-11-02 Ana, logged out |  |
| ig-vk | instagram | ch2 | on | 1 | 14 | carousel | 5 | profile | mon-fri 10:00; sat 11:00 | 1 | light |  | 2026-11-02 Ana | 2026-11-03 |
"""


def test_the_live_settings_are_valid():
    """On or off, whatever the team has set in the repository parses without an error."""
    s = st.load("vsichkikazina", ROOT)
    assert s.errors == []


def test_the_shipped_settings_are_valid_and_off():
    s = st.parse(SHIPPED.read_text(encoding="utf-8"))
    assert s.errors == []
    assert s.brand["social"] is False and s.social_on is False
    assert "approver" not in s.brand                       # the team approves: anyone with write access
    assert [a["account_id"] for a in s.accounts] == ["fb-vsichkikazina", "ig-vsichkikazina",
                                                     "x-vsichkikazina", "li-vsichkikazina"]
    assert not any(a["active"] for a in s.accounts)
    assert s.brand["compliance_long"] == "18+ Хазартът може да пристрасти. Играйте отговорно."


def test_good_settings_parse():
    s = st.parse(GOOD)
    # brand hashtag counts toward the limit: instagram 5 + 1 is over 5 (D4)
    assert s.account_errors("ig-vk") == ["ig-vk: hashtags: 5 + 1 brand hashtag(s) is above the instagram limit of 5"]
    assert s.brand_ok and s.social_on
    fb = s.account("fb-vk")
    assert fb["slots"] == [{"days": [0, 1, 2, 3, 4, 5, 6], "times": ["12:30", "19:30"]}]
    assert [a["account_id"] for a in s.usable_accounts()] == ["fb-vk"]
    assert s.account("ig-vk")["slots"] == [{"days": [0, 1, 2, 3, 4], "times": ["10:00"]},
                                           {"days": [5], "times": ["11:00"]}]
    assert fb["slides"] == 5                                                   # no slides column: the default


def test_art():
    md = SHIPPED.read_text(encoding="utf-8")
    assert st.parse(md).brand["art"] == "every slide"
    assert st.parse(md.replace("| art | every slide |", "| art | Cover |")).brand["art"] == "cover"
    assert "art must be every slide or cover" in [e["message"] for e in st.parse(md.replace("| art | every slide |", "| art | all |")).errors]
    assert st.parse(md.replace("| art | every slide |\n", "")).brand["art"] == "every slide"     # a file from before the key


def test_slides():
    t = st.mdtable.find(GOOD, "account_id", "network")
    with_col = st.mdtable.replace(GOOD, dict(t, header=t["header"][:7] + ["slides"] + t["header"][7:]),
                                  [dict(r, slides="12" if r["account_id"] == "fb-vk" else "7") for r in t["rows"]])
    s = st.parse(with_col)
    assert "fb-vk: slides must be 3–10 (a carousel: cover, points, closing)" in s.account_errors("fb-vk")
    assert s.account("ig-vk")["slides"] == 7


def _with(text, old, new):
    assert old in text
    return text.replace(old, new)


def test_d4_examples():
    bad = _with(GOOD, "| fb-vk | facebook | ch1 | on | 2 |", "| fb-vk | myspace | ch1 | on | 7 |")
    bad = _with(bad, "mon-fri 10:00; sat 11:00", "mon-fri 25:00")
    bad = _with(bad, "| eligible_types | guide, comparison, review, news |", "| eligible_types | guide, hub-intro |")
    bad = _with(bad, "| allowed_link_areas | /blog/ |", "| allowed_link_areas | /blog/, https://evil.example/x/ |")
    s = st.parse(bad)
    msgs = [e["message"] for e in s.errors]
    assert "fb-vk: unknown network 'myspace' (one of facebook, instagram, x, linkedin-page, linkedin-profile)" in msgs
    assert "fb-vk: posts per article must be 1–5" in msgs
    assert "ig-vk: slot '25:00' is outside 00:00–23:59" in msgs
    assert "hub-intro can never be an eligible article type (section intros get posts only on request)" in msgs
    assert any("outside the brand's own domain" in m for m in msgs)
    assert not s.brand_ok and s.usable_accounts() == []


def test_active_account_needs_a_test_post_and_a_channel():
    s = st.parse(_with(GOOD, "| ch1 | on | 2 | 14 | auto | 2 | in post | daily 12:30, 19:30 | 2 | light |  | 2026-11-02 Ana, logged out |",
                       "|  | on | 2 | 14 | auto | 2 | in post | daily 12:30, 19:30 | 2 | light |  |  |"))
    assert s.account_errors("fb-vk") == [
        "fb-vk: active, but no visible test post is recorded (test_post_seen, D3)",
        "fb-vk: active, but no publishing tool channel is set (postiz_channel_id)"]


def test_social_on_needs_identities():
    s = st.parse(_with(GOOD, "| identities_verified | 2026-11-01 (SOCIAL-SETUP.md#identities) |", "| identities_verified |  |"))
    msgs = [e["message"] for e in s.errors if e["scope"] == "brand"]
    assert any("identities are verified" in m for m in msgs)
    assert s.social_on is False
    old = st.parse(_with(GOOD, "| pause | off |", "| approver | AmigoNiko |\n| pause | off |"))   # a file from before the team
    assert old.errors == st.parse(GOOD).errors and "approver" not in old.brand


def test_a_change_from_the_dashboard():
    """settings.update: what the Settings form sends, written into the tables (intake.py)."""
    md = SHIPPED.read_text(encoding="utf-8")
    new = st.update(md, {"pause": "on", "voice_notes": "Кратко | ясно\nи учтиво"},
                    {"ig-vsichkikazina": {"slots": "daily 12:45, 18:30", "format": "carousel"}})
    s = st.parse(new)
    assert s.brand["pause"] is True and s.brand["voice_notes"] == "Кратко / ясно и учтиво"     # one line, no bare pipe
    ig = s.account("ig-vsichkikazina")
    assert (ig["slots_text"], ig["format"]) == ("daily 12:45, 18:30", "carousel")
    assert s.account("fb-vsichkikazina") == st.parse(md).account("fb-vsichkikazina")          # other rows untouched
    assert new.split("## Brand")[0] == md.split("## Brand")[0]                                  # the text above, byte for byte
    no_art = _with(md, "| art | every slide |\n", "")
    assert st.parse(st.update(no_art, {"art": "cover"})).brand["art"] == "cover"                # a key the file lacks: a new row
    for brand, accounts, why in (({"approver": "x"}, {}, "unknown setting 'approver'"),
                                 ({}, {"tt-vk": {"active": "on"}}, "unknown account 'tt-vk'"),
                                 ({}, {"ig-vsichkikazina": {"network": "x"}}, "unknown account field 'network'")):
        with pytest.raises(ValueError, match=why):
            st.update(md, brand, accounts)


def test_instagram_cannot_link_in_post_and_unknown_channels_are_flagged():
    s = st.parse(_with(GOOD, "| 5 | profile |", "| 4 | in post |"))
    assert "ig-vk: Instagram posts cannot carry a link: set link to profile (or none)" in s.account_errors("ig-vk")
    s = st.check_channels(st.parse(GOOD), {"ch2"})
    assert "fb-vk: the publishing tool has no channel 'ch1'" in s.account_errors("fb-vk")


def test_slot_rules():
    assert st.parse_slots("mon,wed,fri 09:00") == [{"days": [0, 2, 4], "times": ["09:00"]}]
    assert st.parse_slots("sat-mon 9:05") == [{"days": [0, 5, 6], "times": ["09:05"]}]
    with pytest.raises(ValueError):
        st.parse_slots("someday 10:00")
    with pytest.raises(ValueError):
        st.parse_slots("")
