import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import board, mdtable  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "social"     # the boards as shipped, not the live ones

REQ = """# Requests

## Requests

| id | kind | target | angle | target_page | accounts | earliest | status | reason | pack_id | added |
|---|---|---|---|---|---|---|---|---|---|---|
| vk-req-001 | keyword | бакара | | | | | done | | vk-req-001-p1 | 2026-11-01 |
|  | article | vk-0003 | a second angle | | fb-vsichkikazina | 2026-11-20 | | | | |
|  | intro | hub-intro-casino-payments | | | | | | | | |

## Commands

| id | command | post_id | date | status | note |
|---|---|---|---|---|---|
|  | fix | vk-0300-p1-fb-1 | | | |
|  | not before | vk-0300-p1-x-1 | 2026-12-01 | | |
|  | delete | vk-0300-p1-x-1 | | | |
"""


def test_new_rows_get_ids():
    text, new = board.assign_ids(REQ, "vk", date="2026-11-05")
    assert new == ["vk-req-002", "vk-req-003", "vk-cmd-001", "vk-cmd-002", "vk-cmd-003"]
    reqs, cmds = board.parse_requests(text)
    assert [(r["id"], r["kind"], r["status"], r["added"]) for r in reqs] == [
        ("vk-req-001", "keyword", "done", "2026-11-01"), ("vk-req-002", "article", "open", "2026-11-05"),
        ("vk-req-003", "intro", "open", "2026-11-05")]
    assert reqs[1]["accounts"] == "fb-vsichkikazina" and reqs[1]["earliest"] == "2026-11-20"
    assert [(c["id"], c["command"], c["status"]) for c in cmds] == [
        ("vk-cmd-001", "fix", "open"), ("vk-cmd-002", "not before", "open"), ("vk-cmd-003", "delete", "open")]
    assert board.assign_ids(text, "vk")[1] == []                       # nothing new the second time
    assert "## Commands" in text and text.startswith("# Requests")


def test_commands_are_read_strictly():
    _, cmds = board.parse_requests(board.assign_ids(REQ, "vk")[0])
    assert board.parse_command(cmds[0]) == ({"id": "vk-cmd-001", "kind": "fix", "post_id": "vk-0300-p1-fb-1", "date": ""}, "")
    assert board.parse_command(cmds[1])[0]["date"] == "2026-12-01"
    assert board.parse_command(cmds[2]) == (None, "unknown command 'delete' (fix, cancel, not before, post now or post at)")
    assert board.parse_command({"id": "vk-cmd-9", "command": "post now", "post_id": "vk-0300-p1-fb-1"})[0]["kind"] == "post now"
    assert board.parse_command({"command": "not before", "post_id": "vk-0300-p1-x-1", "date": "soon"}) == \
        (None, "not before needs a date (YYYY-MM-DD)")
    assert board.parse_command({"command": "cancel", "post_id": "nope"}) == (None, "unknown post ID 'nope'")


def test_request_and_command_updates():
    text, _ = board.assign_ids(REQ, "vk")
    text = board.set_request(text, "vk-req-002", status="failed", reason="not in the approved feed")
    text = board.set_command(text, "vk-cmd-003", "ignored", "unknown command")
    reqs, cmds = board.parse_requests(text)
    assert (reqs[1]["status"], reqs[1]["reason"]) == ("failed", "not in the approved feed")
    assert (cmds[2]["status"], cmds[2]["note"]) == ("ignored", "unknown command")


def test_pack_registry():
    text = (FIXTURES / "packs.md").read_text(encoding="utf-8")
    assert board.parse_packs(text) == []
    text = board.upsert_pack(text, {"pack_id": "vk-0300-p1", "source": "vk-0300", "title": "Бакара", "pr": "#410",
                                    "branch": "social/vk/vk-0300-p1", "status": "open", "posts": "3",
                                    "created": "2026-11-03"})
    text = board.upsert_pack(text, {"pack_id": "vk-0064", "source": "vk-0064", "status": "skipped",
                                    "note": "operator or bonus article"})
    text = board.upsert_pack(text, {"pack_id": "vk-0300-p1", "status": "merged", "updated": "2026-11-03"})
    rows = board.parse_packs(text)
    assert [(r["pack_id"], r["status"], r["pr"]) for r in rows] == [("vk-0300-p1", "merged", "#410"),
                                                                     ("vk-0064", "skipped", "")]
    assert [r["pack_id"] for r in board.packs_of_source(rows, "vk-0300")] == ["vk-0300-p1"]
    shipped_requests = (FIXTURES / "requests.md").read_text(encoding="utf-8")
    assert board.parse_requests(shipped_requests) == ([], [])


def test_the_test_copies_keep_the_live_layout():
    """The tests use fixed copies of the boards (fixtures/social): the live files gain rows and
    settings as the team works, but every column they have is in the copies, in the same order.
    (A live table may lack a newer optional column, e.g. slides or sources: it reads as empty.)"""
    for name in ("settings.md", "packs.md", "requests.md"):
        live = mdtable.tables((REPO / "VsichkiKazina" / "social" / name).read_text(encoding="utf-8"))
        shipped = mdtable.tables((FIXTURES / name).read_text(encoding="utf-8"))
        assert len(live) == len(shipped), name
        for lt, st_ in zip(live, shipped):
            assert [c for c in st_["header"] if c in lt["header"]] == lt["header"], (name, lt["header"])


def test_requests_with_format_slides_and_sources():
    reqs, _ = board.parse_requests(REQ)                               # a table without the newer columns
    assert (reqs[0]["format"], reqs[0]["slides"], reqs[0]["sources"]) == ("", "", "")
    new = (FIXTURES / "requests.md").read_text(encoding="utf-8")
    t = mdtable.find(new, "kind", "target")
    assert t["header"] == board.REQUEST_COLS
    row = {"kind": "topic", "target": "7 грешки при рулетката", "format": "Carousel", "slides": "7",
           "sources": "https://example.org/ruletka, sources/2026-10-24-ruletka.md"}
    reqs, _ = board.parse_requests(mdtable.replace(new, t, [row]))
    r = reqs[0]
    assert (r["kind"], r["format"], r["slides"]) == ("topic", "carousel", "7") and board.request_problem(r) == ""
    assert board.request_sources(r) == ["https://example.org/ruletka", "sources/2026-10-24-ruletka.md"]
    assert board.request_format(r, {"format": "single", "slides": 5}) == ("carousel", 7)
    assert board.request_format({"format": "", "slides": ""}, {"format": "carousel", "slides": 5}) == ("carousel", 5)
    for bad, why in ((dict(r, slides="12"), "slides must be 3–10"), (dict(r, format="reel"), "format must be"),
                     (dict(r, sources="ruletka.md"), "a source must be"), (dict(r, kind="video"), "unknown kind")):
        assert board.request_problem(bad).startswith(why), bad


def test_post_at_and_whole_packs():
    cmd, why = board.parse_command({"id": "vk-cmd-001", "command": "post at", "post_id": "vk-0300-p1", "date": "2026-11-05 17:15"})
    assert why == "" and cmd["pack_id"] == "vk-0300-p1" and cmd["post_id"] is None and cmd["date"] == "2026-11-05 17:15"
    cmd, why = board.parse_command({"command": "post now", "post_id": "vk-0300-p1-ig-1"})
    assert why == "" and cmd["post_id"] == "vk-0300-p1-ig-1" and "pack_id" not in cmd
    assert board.parse_command({"command": "post at", "post_id": "vk-0300-p1-ig-1", "date": "2026-11-05"})[1] ==         "post at needs a day and a time (YYYY-MM-DD HH:MM)"
    assert board.parse_command({"command": "cancel", "post_id": "vk-0300-p1"})[1] == "unknown post ID 'vk-0300-p1'"
