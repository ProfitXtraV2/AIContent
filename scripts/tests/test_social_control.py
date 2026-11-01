"""The control loop (product spec F7; AC 71, 72): stop now, lift, and the tool switch."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from social import control, github  # noqa: E402
from test_social_check import scheduled, u, world  # noqa: E402

BRANDS = ["vsichkikazina"]


def comment(cid, body, author, at="2026-11-04T08:30:00Z", edited=None):
    return {"id": cid, "body": body, "user": {"login": author}, "created_at": at, "updated_at": edited or at}


def loop(w, now):
    return control.run(w.db, w.gh, w.postiz, 7, BRANDS, now=u(now))


def test_stop_now_and_who_lifts_it(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    assert len(w.postiz.items) == 3
    w.gh.perms.update({"setup-person": "maintain", "visitor": "read", "helper[bot]": "write"})
    w.gh.comments = [comment(1, "/stop-now vsichkikazina", "visitor"),
                     comment(2, "/stop-now vsichkikazina\nplease", "setup-person")]
    out = loop(w, "2026-11-04 08:35")
    assert out["commands"] == [(1, "stop-now", "vsichkikazina", "ignored: visitor has read permission"),
                               (2, "stop-now", "vsichkikazina", "stop now accepted")]
    assert w.postiz.items == {} and set(w.states().values()) == {"held"}       # within the 5-minute pass
    assert w.db.switches("vsichkikazina")["stop_now"] is True
    # a lift by someone without write access, or by a bot, is ignored, and shown
    w.gh.comments.append(comment(3, "/lift vsichkikazina", "visitor", at="2026-11-04T08:40:00Z"))
    w.gh.comments.append(comment(31, "/lift vsichkikazina", "helper[bot]", at="2026-11-04T08:41:00Z"))
    out = loop(w, "2026-11-04 08:45")
    assert [c[3] for c in out["commands"]] == ["lift ignored: visitor has read permission",
                                               "lift ignored: helper[bot] has write permission"]
    assert w.db.switches("vsichkikazina")["stop_now"] is True
    w.check(u("2026-11-04 09:10"))
    assert set(w.states().values()) == {"held"} and w.postiz.items == {}
    led = w.ledger()
    assert led["brand_state"]["badges"] == ["Paused (stop now)"]
    assert {"kind": "paused", "text": "lift ignored: @visitor has no write access", "level": "warn"} in led["banners"]
    # anyone of the team lifts it (here not the person who set things up): held posts take the next free slots
    w.gh.comments.append(comment(4, "/lift vsichkikazina", "setup-person", at="2026-11-04T09:20:00Z"))
    loop(w, "2026-11-04 09:25")
    assert w.db.switches("vsichkikazina")["stop_now"] is False
    w.check(u("2026-11-04 10:10"))
    assert set(w.states().values()) == {"planned"}
    assert {w.post(p)["planned_slot_utc"] for p in w.states()} == {"2026-11-04T17:30:00Z"}


def test_comments_count_once_and_edits_never(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    w.gh.perms["setup-person"] = "write"
    w.gh.comments = [comment(5, "/stop-now vsichkikazina", "setup-person", edited="2026-11-04T08:31:00Z")]
    out = loop(w, "2026-11-04 08:35")
    assert out["commands"] == [(5, "stop-now", "vsichkikazina", "ignored: edited")]
    assert len(w.postiz.items) == 3
    w.gh.comments[0]["updated_at"] = w.gh.comments[0]["created_at"]          # edited back: still never read again
    loop(w, "2026-11-04 08:40")
    assert len(w.postiz.items) == 3 and w.db.switches("vsichkikazina")["stop_now"] is False


def test_channels_disabled_in_the_tool(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    for ch in w.postiz.channels:
        ch["disabled"] = True
    out = loop(w, "2026-11-04 08:40")
    assert out["tool_pause"] == {"vsichkikazina": True} and w.postiz.items == {}
    for ch in w.postiz.channels:                                               # enabled again: still paused
        ch["disabled"] = False
    loop(w, "2026-11-04 08:45")
    assert w.db.switches("vsichkikazina")["tool_pause"] is True
    w.check(u("2026-11-04 09:10"))
    assert w.ledger()["brand_state"]["badges"] == ["Paused (tool)"]
    w.gh.comments = [comment(9, "/lift vsichkikazina", "AmigoNiko", at="2026-11-04T09:20:00Z")]
    loop(w, "2026-11-04 09:25")
    assert w.db.switches("vsichkikazina")["tool_pause"] is False


def test_one_disabled_channel_holds_only_its_posts(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    next(c for c in w.postiz.channels if c["id"] == "ch-x")["disabled"] = True
    loop(w, "2026-11-04 08:40")
    assert sorted(p["channel_id"] for p in w.postiz.items.values()) == ["ch-fb", "ch-ig"]
    assert w.post("vk-0300-p1-x-1")["reason"] == "held:channel_disabled"
    assert w.db.switches("vsichkikazina")["tool_pause"] is False


def test_post_now_lines_wake_the_check(tmp_path):
    class GH:
        def __init__(self, text):
            self.text = text

        def file_at(self, path, ref):
            assert path == "VsichkiKazina/social/requests.md" and ref == "main"
            return self.text.encode("utf-8") if self.text is not None else None
    base = "## Commands\n\n| id | command | post_id | date | status | note |\n|---|---|---|---|---|---|\n"
    assert control.pending_post_now(GH(base + "| vk-cmd-1 | post now | vk-0300-p1-fb-1 |  | open |  |\n"), "vsichkikazina")
    assert not control.pending_post_now(GH(base + "| vk-cmd-1 | post now | vk-0300-p1-fb-1 |  | done | goes out at once |\n"), "vsichkikazina")
    assert not control.pending_post_now(GH(base + "| vk-cmd-1 | cancel | vk-0300-p1-fb-1 |  | open |  |\n"), "vsichkikazina")
    assert not control.pending_post_now(GH(None), "vsichkikazina")



def test_a_command_waits_when_github_cannot_say_who_wrote_it(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    w.gh.comments = [comment(6, "/stop-now vsichkikazina", "AmigoNiko")]
    known = w.gh.permission

    def down(user):
        raise github.GitHubError("GitHub cannot be reached")
    w.gh.permission = down
    out = loop(w, "2026-11-04 08:35")
    assert out["commands"] == [(6, "stop-now", "vsichkikazina", "waits: GitHub could not say who wrote it")]
    assert len(w.postiz.items) == 3                                         # not lost: read again next pass
    w.gh.permission = known
    out = loop(w, "2026-11-04 08:40")
    assert out["commands"] == [(6, "stop-now", "vsichkikazina", "stop now accepted")] and w.postiz.items == {}
