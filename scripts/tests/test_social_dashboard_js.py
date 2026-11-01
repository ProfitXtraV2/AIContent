"""The dashboard writes the same bytes the Python side writes (docs/social-md.js against
scripts/social): post files, board rows, settings, slots, lengths and tagged links. A change made
from the dashboard must look to the checks and the publishing check exactly like one made in GitHub."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import links, mdtable, pack as packmod, settings as st  # noqa: E402
from social import postnumbers as numbers  # noqa: E402

DOCS = Path(__file__).resolve().parents[2] / "docs"
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "social"     # the boards as shipped, not the live ones
pytestmark = pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")


def js(calls):
    """Run [(function, args)] through docs/social-md.js in node; returns the results."""
    script = ("const MD = require(%s);\nconst calls = JSON.parse(require('fs').readFileSync(0, 'utf8'));\n"
              "const out = calls.map(([fn, args]) => { try { return {ok: MD[fn](...args)}; } catch (e) { return {err: e.message}; } });\n"
              "process.stdout.write(JSON.stringify(out));") % json.dumps(str(DOCS / "social-md.js"))
    got = subprocess.run(["node", "-e", script], input=json.dumps(calls), capture_output=True, text=True, encoding="utf-8")
    assert got.returncode == 0, got.stderr
    return json.loads(got.stdout)


FIELDS = {"text": "Банко около 1,06%, равенство около 14,36%.\n\nВтори абзац с [[LINK]] 🎲\n\n18+ Хазартът може да пристрасти. Играйте отговорно.",
          "hashtags": ["#бакара", "#казиноигри"], "image_text": ["Банко около 1,06%", "Пунто 1,24%"],
          "alt_text": "Две карти на везни", "english": "Banco about 1.06%…\n\nImage text:\n- Banco"}


def test_post_files_are_byte_identical():
    md = packmod.render_post_md("vk-0012-p1-ig-1", FIELDS)
    r = js([["renderPost", ["vk-0012-p1-ig-1", FIELDS]], ["parsePost", [md]], ["publishText", [FIELDS]],
            ["parsePost", ["# x\n\n## Hashtags\nбакара, #казино\n\n## Image text\n  a  \n\n b\n"]]])
    assert r[0]["ok"] == md
    assert r[1]["ok"] == packmod.parse_post_md(md)
    assert r[2]["ok"] == packmod.publish_text(FIELDS)
    assert r[3]["ok"] == packmod.parse_post_md("# x\n\n## Hashtags\nбакара, #казино\n\n## Image text\n  a  \n\n b\n")


def test_board_rows_match_the_python_tables():
    requests_md = (FIXTURES / "requests.md").read_text(encoding="utf-8")
    req = {"kind": "article", "target": "vk-0012", "angle": "мит | факт", "target_page": "", "accounts": ["ig-vsichkikazina"],
           "earliest": "2026-11-01"}
    r = js([["addRequest", [requests_md, req, "2026-10-22"]],
            ["addCommand", [requests_md, {"command": "not before", "post_id": "vk-0012-p1-ig-1", "date": "2026-11-05"}]],
            ["addCommand", [requests_md, {"command": "not before", "post_id": "vk-0012-p1-ig-1", "date": "5 Nov"}]],
            ["addCommand", [requests_md, [{"command": "post now", "post_id": "vk-0012-p1-ig-1"},
                                          {"command": "post now", "post_id": "vk-0012-p1-fb-1"}]]]])
    t = mdtable.find(requests_md, "kind", "target")
    want = mdtable.replace(requests_md, t, t["rows"] + [{
        "id": "", "kind": "article", "target": "vk-0012", "angle": "мит | факт", "target_page": "", "accounts": "ig-vsichkikazina",
        "earliest": "2026-11-01", "status": "", "reason": "", "pack_id": "", "added": "2026-10-22"}])
    assert r[0]["ok"] == want
    from social import board
    reqs, _ = board.parse_requests(r[0]["ok"])
    assert reqs[-1]["angle"] == "мит / факт" and reqs[-1]["target"] == "vk-0012"   # a bare pipe never breaks the table
    _, cmds = board.parse_requests(r[1]["ok"])
    assert (cmds[-1]["command"], cmds[-1]["post_id"], cmds[-1]["date"]) == ("not before", "vk-0012-p1-ig-1", "2026-11-05")
    assert board.parse_command(cmds[-1])[0]["kind"] == "not before"
    assert "needs a date" in r[2]["err"]
    _, cmds = board.parse_requests(r[3]["ok"])
    assert [(c["command"], c["post_id"]) for c in cmds] == [("post now", "vk-0012-p1-ig-1"), ("post now", "vk-0012-p1-fb-1")]
    assert all(board.parse_command(c)[0]["kind"] == "post now" for c in cmds)


def test_a_post_at_line_matches_the_python_reading():
    requests_md = (FIXTURES / "requests.md").read_text(encoding="utf-8")
    r = js([["addCommand", [requests_md, {"command": "post at", "post_id": "vk-0012-p1", "date": "2026-11-05 17:15"}]],
            ["addCommand", [requests_md, {"command": "post at", "post_id": "vk-0012-p1", "date": "2026-11-05"}]]])
    from social import board
    _, cmds = board.parse_requests(r[0]["ok"])
    cmd, why = board.parse_command(cmds[-1])
    assert why == "" and (cmd["kind"], cmd["pack_id"], cmd["date"]) == ("post at", "vk-0012-p1", "2026-11-05 17:15")
    assert "needs a day and a time" in r[1]["err"]


def test_settings_changes_parse_back():
    md = (FIXTURES / "settings.md").read_text(encoding="utf-8")
    r = js([["updateSettings", [md, {"social": "on", "pause": "on"},
                                {"ig-vsichkikazina": {"active": "on", "slots": "daily 18:30, 19:30", "postiz_channel_id": "ch-1"}}]],
            ["parseSettings", [md]]])
    s = st.parse(r[0]["ok"])
    assert s.brand["social"] is True and s.brand["pause"] is True
    ig = s.account("ig-vsichkikazina")
    assert (ig["active"], ig["slots_text"], ig["postiz_channel_id"]) == (True, "daily 18:30, 19:30", "ch-1")
    assert s.account("fb-vsichkikazina")["active"] is False                       # other rows untouched
    before = md.split("## Brand")[0]
    assert r[0]["ok"].startswith(before)                                         # the text above the tables is kept byte for byte
    parsed = r[1]["ok"]
    assert parsed["brand"]["social"] == "off" and [a["account_id"] for a in parsed["accounts"]][:2] == \
        ["fb-vsichkikazina", "ig-vsichkikazina"]


def test_the_form_and_intake_write_the_same_file():
    """What the dashboard's updateSettings writes and what intake.py writes (settings.update) are one text."""
    md = (FIXTURES / "settings.md").read_text(encoding="utf-8")
    brand, accounts = {"pause": "on", "art": "cover"}, {"ig-vsichkikazina": {"slides": "7", "slots": "daily 12:45"}}
    r = js([["updateSettings", [md, brand, accounts]]])
    assert r[0]["ok"] == st.update(md, brand, accounts)


def test_slides_in_a_settings_file_from_before_the_column():
    """Setting the slides adds the column after `format`; the other accounts read the default 5."""
    md = (FIXTURES / "settings.md").read_text(encoding="utf-8")
    t = mdtable.find(md, "account_id", "network")
    older = mdtable.replace(md, dict(t, header=[h for h in t["header"] if h != "slides"]), t["rows"])
    assert "slides" not in mdtable.find(older, "account_id", "network")["header"]
    assert st.parse(older).account("fb-vsichkikazina")["slides"] == 5
    r = js([["updateSettings", [older, {}, {"ig-vsichkikazina": {"slides": "7"}}]]])
    s = st.parse(r[0]["ok"])
    assert s.errors == [] and s.account("ig-vsichkikazina")["slides"] == 7 and s.account("fb-vsichkikazina")["slides"] == 5
    assert mdtable.find(r[0]["ok"], "account_id", "network")["header"][6:9] == ["format", "slides", "max_hashtags"]


def test_topic_requests_and_older_tables():
    from social import board
    requests_md = (FIXTURES / "requests.md").read_text(encoding="utf-8")
    old_md = ("## Requests\n\n| id | kind | target | angle | target_page | accounts | earliest | status | reason | pack_id | added |\n"
              "|---|---|---|---|---|---|---|---|---|---|---|\n| vk-req-001 | keyword | бакара |  |  |  |  | done |  | vk-req-001-p1 | 2026-10-01 |\n")
    req = {"kind": "topic", "target": "7 грешки при рулетката", "format": "carousel", "slides": "7",
           "sources": ["https://example.org/ruletka", "sources/20261024T101530-7-грешки-при-рулетката.md"]}
    r = js([["addRequest", [requests_md, req, "2026-10-24"]], ["addRequest", [old_md, req, "2026-10-24"]],
            ["sourceFile", ["7 грешки при рулетката | „кратко“", "Зелената нула е 1 от 37 полета.\n", "20261024T101530"]]])
    for text in (r[0]["ok"], r[1]["ok"]):
        new = board.parse_requests(text)[0][-1]
        assert (new["kind"], new["target"], new["format"], new["slides"]) == ("topic", "7 грешки при рулетката", "carousel", "7")
        assert board.request_sources(new) == req["sources"] and board.request_problem(new) == ""
    assert mdtable.find(r[1]["ok"], "kind", "target")["header"] == board.REQUEST_COLS     # the older table gained the columns
    assert board.parse_requests(r[1]["ok"])[0][0]["status"] == "done"                   # its rows kept their values
    f = r[2]["ok"]
    assert f["path"] == "sources/20261024T101530-7-грешки-при-рулетката-кратко.md" and board.SOURCE_FILE.match(f["path"])
    assert f["text"] == "# Source for: 7 грешки при рулетката / „кратко“\n\nЗелената нула е 1 от 37 полета.\n"


def test_slots_lengths_and_links_agree():
    slots = ["daily 12:30, 19:30", "mon-fri 10:00, 18:30; sat 11:00", "fri-mon 9:05", "daily 25:00", "every 10:00", "", "mon"]
    texts = [("Рулетка: 37 полета и 2,7% предимство за казиното. [[LINK]] 18+ Играйте отговорно. 🎲👍🏽", "x"),
             ("Short one https://vsichkikazina.bg/blog/x/?utm_source=x 🇧🇬", "x"),
             ("Текст с [[LINK]] и емоджи 🎲", "facebook"), ("ﾃｽﾄ 中文 text", "x")]
    calls = [["parseSlots", [s]] for s in slots] + [["length", [t, n, 160]] for t, n in texts] + \
            [["tagged", ["https://vsichkikazina.bg/blog/bakara-pravila/", "linkedin-page", "bakara-pravila", "vk-0012-p1-li-1"]],
             ["tagged", ["https://vsichkikazina.bg/blog/a/?x=1", "facebook", "a", "vk-0001-p1-fb-1"]]]
    r = js(calls)
    for s, got in zip(slots, r[:len(slots)]):
        try:
            want = st.parse_slots(s)
        except ValueError:
            want = None
        assert (got.get("ok") if want is not None else got.get("err") is not None) == (want if want is not None else True), s
    for (t, n), got in zip(texts, r[len(slots):len(slots) + len(texts)]):
        assert got["ok"] == numbers.length(t, n, link_length=160), t
    assert r[-2]["ok"] == links.tagged("https://vsichkikazina.bg/blog/bakara-pravila/", "linkedin-page", "bakara-pravila",
                                       "vk-0012-p1-li-1")
    assert r[-1]["ok"] == links.tagged("https://vsichkikazina.bg/blog/a/?x=1", "facebook", "a", "vk-0001-p1-fb-1")


def test_all_dashboard_scripts_parse():
    for name in ("social-md.js", "social-github.js", "social-preview.js", "social-tabs.js"):
        assert subprocess.run(["node", "--check", str(DOCS / name)], capture_output=True).returncode == 0, name

