"""The publishing check, scenario by scenario (product spec acceptance criteria 42–82, 88, 89),
against a fake GitHub, publisher, site and Postiz (social/replay.py)."""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import pack as packmod, postiz, replay  # noqa: E402
from social.replay import ARTICLE, COMPLIANCE, DRAFT_0300, LINE_ODDS, LINE_PAY, PAGE  # noqa: E402

FB, IG, X = "vk-0300-p1-fb-1", "vk-0300-p1-ig-1", "vk-0300-p1-x-1"
URL = "https://vsichkikazina.bg/blog/ruletka-shansove/"
GOOD_PAGE = PAGE.format(pay=LINE_PAY, odds=LINE_ODDS)


def u(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)


def world(tmp, live=True, **kw):
    """vk-0300 approved by Nikolay's merge (Tue 3 Nov, 13:00 Sofia); live from Wed 4 Nov 06:45 UTC."""
    w = replay.World(tmp, **kw)
    w.article("vk-0300", "2026-11-02-ruletka-shansove", ARTICLE)
    w.draft(DRAFT_0300)
    w.merge_pack("vk-0300-p1", "2026-11-03T11:00:00Z", number=301)
    if live:
        w.deploy("ruletka-shansove", html=GOOD_PAGE)
        w.set_status("vk-0300", "posted", posted="2026-11-04")
    return w


def scheduled(w):
    """Run the morning of Wed 4 Nov up to the hand-over for 12:30 Sofia (10:30 UTC)."""
    w.check(u("2026-11-04 07:10"))
    w.check(u("2026-11-04 08:10"))


def tool_post(w, post_id):
    pid = w.post(post_id)["handover"]["postiz_post_id"]
    return w.postiz.items.get(pid)


def events(w, post_id):
    return [r["event"] for r in w.db.audit_rows(brand="vsichkikazina", post_id=post_id)]


# --- the walk-through of flow 0 ----------------------------------------------------------------

def test_recorded_day_vk0300(tmp_path):
    w, timeline = replay.vk0300(tmp_path)
    states = [{pid: s for pid, (s, _) in step["posts"].items()} for step in timeline]
    assert states[0] == {FB: "waiting_for_article", IG: "waiting_for_article", X: "waiting_for_article"}
    assert states[1] == {FB: "planned", IG: "planned", X: "planned"}
    assert states[2] == states[3] == {FB: "scheduled", IG: "scheduled", X: "scheduled"}
    assert states[4] == {FB: "published", IG: "published", X: "published"}
    assert {when for _, when in timeline[1]["posts"].values()} == {"2026-11-04T10:30:00Z"}     # 12:30 Sofia
    # the hand-over happened at 10:10 Sofia, inside 09:30–12:00, for 12:30
    fb = w.post(FB)
    assert fb["handover"]["utc"] == "2026-11-04T08:10:00Z" and fb["handover"]["slot_utc"] == "2026-11-04T10:30:00Z"
    sent = {p["channel_id"]: postiz.normalize_content(p["content"]) for p in w.postiz.items.values()}
    tagged = URL + "?utm_source=facebook&utm_medium=social&utm_campaign=ruletka-shansove&utm_content=" + FB
    assert sent["ch-fb"] == f"{LINE_ODDS}\n\nКакво значи това за всеки ваш залог: {tagged}\n\n{COMPLIANCE}\n\n#рулетка"
    assert "utm_source=x&" in sent["ch-x"] and "http" not in sent["ch-ig"]                  # Instagram: no link
    settings = {p["channel_id"]: p["settings"] for p in w.postiz.items.values()}
    assert settings["ch-x"]["who_can_reply_post"] == "everyone" and settings["ch-ig"]["__type"] == "instagram"
    assert len({p["group"] for p in w.postiz.items.values()}) == 3                            # one group per post
    # audit trail (AC 88): merge by Nikolay, approved text = handed-over text apart from the link, published
    rows = {r["event"]: r for r in w.db.audit_rows(brand="vsichkikazina", post_id=FB)}
    assert rows["approved"]["merged_by"] == "AmigoNiko" and rows["approved"]["pr"] == 301
    handed = rows["handed over"]
    assert handed["payload_text"].replace(handed["link_tagged"], "[[LINK]]") == handed["approved_text"]
    assert all(c["ok"] for c in handed["checks"]) and handed["live_page"]["missing"] == []
    assert rows["published"]["network_url"].startswith("https://facebook.example.test/p/")
    # ledger and dashboard data (G2)
    led = w.ledger()
    assert {p["post_id"]: p["state"] for p in led["posts"]} == {FB: "published", IG: "published", X: "published"}
    assert led["last_check_utc"] == "2026-11-04T11:10:00Z" and led["banners"] == []
    sched = json.loads((tmp_path / "docs" / "data" / "social" / "vsichkikazina-schedule.json").read_text(encoding="utf-8"))
    assert {r["time_local"] for r in sched["rows"]} == {"2026-11-04 12:30"}
    assert sched["counters"]["published_this_month"] == 3
    assert w.repo.pushed[-1] == "social: publishing check 2026-11-04T11:10:00Z (vsichkikazina)"
    assert len(w.postiz.calls) and "create" in w.postiz.calls


# --- go-live (F2) -------------------------------------------------------------------------------

def test_waits_for_the_article_and_uses_the_record_when_write_back_lags(tmp_path):
    w = world(tmp_path, live=False)
    w.check(u("2026-11-03 12:10"))
    assert set(w.states().values()) == {"waiting_for_article"}
    assert w.post(FB)["reason"].startswith("waiting:not deployed yet")
    w.deploy("ruletka-shansove", html=GOOD_PAGE)            # deployed 06:45 UTC; the queue row stays approved (AC 49)
    w.check(u("2026-11-04 07:10"))
    assert set(w.states().values()) == {"planned"} and w.post(FB)["planned_slot_utc"] == "2026-11-04T10:30:00Z"
    w.check(u("2026-11-04 08:10"))
    assert set(w.states().values()) == {"scheduled"}


# --- approval (E4; AC 42, 43, 44) ----------------------------------------------------------------

def test_closed_pack_is_rejected(tmp_path):
    w = replay.World(tmp_path)
    w.article("vk-0300", "2026-11-02-ruletka-shansove", ARTICLE)
    w.draft(DRAFT_0300)
    n = w.open_pack("vk-0300-p1", "2026-11-03T08:00:00Z")
    w.close_pack(n, "2026-11-03T12:00:00Z")
    w.check(u("2026-11-03 12:10"))
    assert set(w.states().values()) == {"rejected"} and w.postiz.items == {}


def test_merged_by_someone_else_is_not_approved(tmp_path):
    w = replay.World(tmp_path)
    w.article("vk-0300", "2026-11-02-ruletka-shansove", ARTICLE)
    w.draft(DRAFT_0300)
    w.merge_pack("vk-0300-p1", "2026-11-03T11:00:00Z", by="setup-person")
    w.deploy("ruletka-shansove", html=GOOD_PAGE)
    for t in ("2026-11-04 07:10", "2026-11-04 08:10"):
        w.check(u(t))
    assert set(w.states().values()) == {"needs_fix"} and w.post(FB)["reason"] == "needs_fix:merged_by_other"
    assert any("merged by @setup-person, who cannot approve" in b["text"] for b in w.ledger()["banners"])
    assert w.postiz.items == {}


def test_anyone_of_the_team_approves_and_changes_the_settings(tmp_path):
    """A merge by anyone with write access approves (Ivana, not the person who set things up); a
    settings change counts from her merge too, and from a bot's merge never."""
    w = replay.World(tmp_path)
    w.article("vk-0300", "2026-11-02-ruletka-shansove", ARTICLE)
    w.draft(dict(DRAFT_0300, posts=DRAFT_0300["posts"][:1]))
    w.merge_pack("vk-0300-p1", "2026-11-03T11:00:00Z", by="Ivana")
    w.deploy("ruletka-shansove", html=GOOD_PAGE)
    w.set_status("vk-0300", "posted", posted="2026-11-04")
    w.check(u("2026-11-04 07:10"))
    assert w.post(FB)["approval"]["merged_by"] == "Ivana" and w.post(FB)["state"] == "planned"
    w.gh.perms["px-bot[bot]"] = "write"
    w.set_settings(replay.SETTINGS + "\n<!-- a bot's change -->\n", by="px-bot[bot]", at="2026-11-04T07:20:00Z")
    w.check(u("2026-11-04 08:10"))
    assert any(b["text"].startswith("settings changed without approval") for b in w.ledger()["banners"])
    w.set_settings(replay.SETTINGS + "\n<!-- Ivana's change -->\n", by="Ivana", at="2026-11-04T08:30:00Z")
    w.check(u("2026-11-04 09:10"))
    assert not any(b["text"].startswith("settings changed without approval") for b in w.ledger()["banners"])
    assert w.db.accepted_settings("vsichkikazina")["merged_by"] == "Ivana"
    assert w.post(FB)["state"] == "scheduled"                               # her merge still allows the hand-over


def test_github_down_while_asking_who_merged_changes_nothing(tmp_path):
    w = replay.World(tmp_path)
    w.article("vk-0300", "2026-11-02-ruletka-shansove", ARTICLE)
    w.draft(dict(DRAFT_0300, posts=DRAFT_0300["posts"][:1]))
    w.merge_pack("vk-0300-p1", "2026-11-03T11:00:00Z", by="Ivana")
    known = w.gh.permission

    def down(user):
        raise replay.pc.github.GitHubError("GitHub cannot be reached")
    w.gh.permission = down
    w.check(u("2026-11-03 12:10"))
    assert w.post(FB) is None                                               # the PR is read again next time
    w.gh.permission = known
    w.check(u("2026-11-03 13:10"))
    assert w.post(FB)["approval"]["merged_by"] == "Ivana"


def test_a_check_failing_after_merge_stops_only_that_post(tmp_path):
    w = replay.World(tmp_path)
    w.article("vk-0300", "2026-11-02-ruletka-shansove", ARTICLE)
    w.draft(DRAFT_0300)
    # merged a minute after the compliance line was removed, before the PR checks reran (AC 44)
    w.edit_post("vk-0300-p1", X, text="Рулетка: 37 полета и 2,7% предимство за казиното. [[LINK]]")
    w.merge_pack("vk-0300-p1", "2026-11-03T11:00:00Z")
    w.deploy("ruletka-shansove", html=GOOD_PAGE)
    scheduled(w)
    assert w.states() == {FB: "scheduled", IG: "scheduled", X: "needs_fix"}
    assert w.post(X)["reason"] == "needs_fix:check_failed"
    assert [c["check"] for c in w.db.audit_rows(post_id=X)[0]["checks"] if not c["ok"]] == ["compliance"]


# --- hand-over (F5; AC 51, 53, 54, 55) -------------------------------------------------------------

def test_text_changed_after_merge_is_never_handed_over(tmp_path):
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))
    # a later commit on main, not a fix PR merged by Nikolay, changes the approved text
    w.edit_post("vk-0300-p1", FB, text=f"{LINE_ODDS}\n\nДруг текст: [[LINK]]\n\n{COMPLIANCE}")
    w.check(u("2026-11-04 08:10"))
    assert w.states()[FB] == "needs_fix" and w.post(FB)["reason"] == "needs_fix:text_differs_from_approved"
    assert {p["channel_id"] for p in w.postiz.items.values()} == {"ch-ig", "ch-x"}


def test_no_live_link(tmp_path):
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))
    w.pages[URL] = (404, "")                                    # the page went away after go-live
    w.check(u("2026-11-04 08:10"))
    assert w.states()[FB] == "held" and w.post(FB)["reason"] == "held:no_live_link"
    assert w.states()[X] == "held" and w.states()[IG] == "held"   # IG has no link, but its live page check fails
    assert w.post(IG)["reason"] == "held:live_page_differs"
    w.pages[URL] = (200, GOOD_PAGE)
    w.check(u("2026-11-04 09:10"))                             # each check looks again: back, still inside the window
    assert set(w.states().values()) == {"scheduled"}
    assert {w.post(p)["planned_slot_utc"] for p in (FB, IG, X)} == {"2026-11-04T10:30:00Z"}


def test_live_page_differs(tmp_path):
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))
    # edited on the site only: 2,7% became 2,70% (AC 51)
    w.pages[URL] = (200, PAGE.format(pay=LINE_PAY, odds=LINE_ODDS.replace("2,7%", "2,70%")))
    w.check(u("2026-11-04 08:10"))
    assert w.states() == {FB: "held", IG: "scheduled", X: "held"}
    assert w.post(FB)["reason"] == "held:live_page_differs" and w.post(FB)["missing_lines"] == ["2,7%"]
    banner = [b["text"] for b in w.ledger()["banners"] if b["kind"] == "live page"]
    assert banner == [f"posts held because the live page differs: {FB}, {X}"]
    w.check(u("2026-11-04 09:10"))
    assert w.states()[FB] == "held"                            # checked again at every check
    w.pages[URL] = (200, GOOD_PAGE)
    w.check(u("2026-11-04 14:10"))                             # the page matches again: the next free slot, 19:30
    assert w.states()[FB] == "planned" and w.post(FB)["planned_slot_utc"] == "2026-11-04T17:30:00Z"
    w.check(u("2026-11-04 15:10"))                             # first check inside 16:30–19:00 Sofia
    assert w.states()[FB] == "scheduled" and w.post(FB)["missing_lines"] == []


# --- the tool (F6, F8, F9; AC 68, 69, 78, 79, 80) -------------------------------------------------------

def test_changes_in_the_tool(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    tool_post(w, FB)["date"] = "2026-11-04T17:30:00.000Z"      # Nikolay moved it to 19:30
    tool_post(w, X)["content"] = "<p>Нов текст без реда за отговорна игра</p>"
    x_id = w.post(X)["handover"]["postiz_post_id"]
    w.check(u("2026-11-04 09:10"))
    fb = w.post(FB)
    assert fb["state"] == "scheduled" and fb["planned_slot_utc"] == "2026-11-04T17:30:00Z"
    assert "changed_in_tool" in fb["markers"]
    assert w.post(X)["state"] == "needs_fix" and w.post(X)["reason"] == "needs_fix:changed_in_tool"
    assert x_id not in w.postiz.items                          # pulled back
    assert any(b["text"].startswith("posts changed in the tool: ") for b in w.ledger()["banners"])


def test_published_text_that_breaks_a_rule(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    p = tool_post(w, IG)
    w.postiz.advance(u("2026-11-04 10:30"))
    p["content"] = "<p>Единичното число плаща 35:1.</p>"       # edited in the tool, compliance line removed
    w.check(u("2026-11-04 11:10"))
    ig = w.post(IG)
    assert ig["state"] == "published" and "published_breaks_a_rule" in ig["markers"]
    assert any(b["level"] == "red" and b["text"].startswith("published post breaks a rule") for b in w.ledger()["banners"])
    checked = [r for r in w.db.audit_rows(post_id=IG) if r["event"] == "published text checked"][0]
    assert [c["check"] for c in checked["checks"] if not c["ok"]] == ["compliance"]


def test_post_not_from_a_pack(tmp_path):
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))
    w.postiz.add_foreign("ch-fb", "<p>Пуснато на ръка</p>", "2026-11-04T09:00:00Z")
    w.check(u("2026-11-04 08:10"))
    foreign = [r for r in w.db.posts("vsichkikazina") if r["state"] == "not_from_pack"]
    assert len(foreign) == 1 and foreign[0]["account_id"] == "fb-vsichkikazina"
    assert any(b["kind"] == "not from a pack" and b["level"] == "red" for b in w.ledger()["banners"])


def test_temporary_errors_are_retried_twice_then_failed(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    slots = []
    for attempt, (fail_at, check_at) in enumerate([("2026-11-04 10:30", "2026-11-04 11:10"),
                                                   ("2026-11-04 17:30", "2026-11-04 18:10"),
                                                   ("2026-11-05 10:30", "2026-11-05 11:10")]):
        pid = w.post(FB)["handover"]["postiz_post_id"]
        slots.append(w.post(FB)["handover"]["slot_utc"])
        w.postiz.fail_next[pid] = "HTTP 503 Service Unavailable"
        w.check(u(check_at))
        rec = w.post(FB)
        if attempt < 2:
            assert rec["state"] == "planned" and rec["retries"] == attempt + 1 and pid not in w.postiz.items
            # handed over again at the first check inside the next window
            for h in range(4):
                w.check(u(check_at[:11] + "15:10") if attempt == 0 else u("2026-11-05 08:10"))
                if w.post(FB)["state"] == "scheduled":
                    break
        else:
            assert rec["state"] == "failed" and rec["reason"] == "failed:HTTP 503 Service Unavailable"
    assert slots == ["2026-11-04T10:30:00Z", "2026-11-04T17:30:00Z", "2026-11-05T10:30:00Z"]
    assert w.states()[IG] == "published"


def test_expired_login_holds_one_account(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    w.postiz.fail_next[w.post(X)["handover"]["postiz_post_id"]] = "Error validating access token: Session has expired"
    w.check(u("2026-11-04 11:10"))
    assert w.states() == {FB: "published", IG: "published", X: "held"}
    assert w.post(X)["reason"] == "held:reconnect_account"
    assert {"kind": "reconnect", "text": "reconnect account x-vsichkikazina", "level": "red"} in w.ledger()["banners"]


def test_missed_slot_when_the_tool_was_down(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    pid = w.post(FB)["handover"]["postiz_post_id"]
    w.postiz.publish_delay_min[pid] = 10_000                   # Postiz was off at 12:30 and kept it queued
    w.check(u("2026-11-04 12:10"))
    fb = w.post(FB)
    assert fb["state"] == "planned" and "missed_slot" in fb["markers"] and fb["retries"] == 0
    assert pid not in w.postiz.items and fb["planned_slot_utc"] == "2026-11-04T17:30:00Z"


def test_a_stop_between_intent_and_create_never_doubles_a_post(tmp_path):
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))
    real = w.postiz.create

    def created_then_timed_out(*a, **k):
        real(*a, **k)
        raise postiz.PostizError("create: timed out", "temporary")

    w.postiz.create = created_then_timed_out
    w.check(u("2026-11-04 08:10"))
    w.postiz.create = real
    assert w.states()[FB] == "planned" and w.post(FB)["handover"]["postiz_post_id"] is None
    w.check(u("2026-11-04 09:10"))
    assert set(w.states().values()) == {"scheduled"}
    assert sorted(p["channel_id"] for p in w.postiz.items.values()) == ["ch-fb", "ch-ig", "ch-x"]   # three, not six
    assert "hand-over found in the tool after a stop" in events(w, FB)


# --- pauses, article changes, commands (F6, F7, A6, A9; AC 73, 74, 77, 81, 82) ---------------------------

def test_settings_pause_pulls_back_and_lifting_replans(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    w.set_settings(replay.SETTINGS.replace("| social | on |", "| social | on |\n| pause | on |"), at="2026-11-04T08:30:00Z")
    w.check(u("2026-11-04 09:10"))
    assert set(w.states().values()) == {"held"} and w.post(FB)["reason"] == "held:paused"
    assert w.postiz.items == {}
    assert {"kind": "paused", "text": "Всички Казина is paused: settings", "level": "red"} in w.ledger()["banners"]
    assert w.ledger()["brand_state"]["badges"] == ["Paused (settings)"]
    w.set_settings(replay.SETTINGS, at="2026-11-04T12:00:00Z")
    w.check(u("2026-11-04 12:10"))
    assert set(w.states().values()) == {"planned"}
    assert {w.post(p)["planned_slot_utc"] for p in (FB, IG, X)} == {"2026-11-04T17:30:00Z"}


def test_settings_changed_without_approval(tmp_path):
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))
    w.set_settings(replay.SETTINGS.replace("daily 12:30, 19:30 | 2 | light |  | 2026-11-02 Ana, phone | |\n| ig",
                                           "daily 09:00 | 2 | light |  | 2026-11-02 Ana, phone | |\n| ig"), merged=False)
    w.check(u("2026-11-04 08:10"))
    assert w.post(FB)["state"] == "scheduled" and w.post(FB)["planned_slot_utc"] == "2026-11-04T10:30:00Z"
    assert {"kind": "settings", "text": "settings changed without approval: the earlier settings stay in force",
            "level": "red"} in w.ledger()["banners"]


def test_article_changes(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    folder = tmp_path / "VsichkiKazina" / "articles" / "2026-11-02-ruletka-shansove" / "05b-final-draft.md"
    folder.write_text(ARTICLE + "\nНов абзац без числа.\n", encoding="utf-8")       # every source line still there
    w.rebuild()
    w.check(u("2026-11-04 09:10"))
    assert set(w.states().values()) == {"scheduled"}
    assert "article version changed: every source line is still there" in events(w, FB)
    folder.write_text(ARTICLE.replace(LINE_ODDS, "Европейската рулетка има 37 полета."), encoding="utf-8")
    w.rebuild()
    w.check(u("2026-11-04 10:10"))
    assert w.states() == {FB: "article_changed", IG: "scheduled", X: "article_changed"}
    assert w.post(FB)["missing_lines"] == [LINE_ODDS] and len(w.postiz.items) == 1


def test_article_unapproved(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    w.set_status("vk-0300", "drafted")
    w.check(u("2026-11-04 09:10"))
    assert set(w.states().values()) == {"held"} and w.post(IG)["reason"] == "held:article_unapproved"
    assert w.postiz.items == {}


def test_commands(tmp_path):
    w = world(tmp_path, live=False)
    w.check(u("2026-11-03 12:10"))
    req = tmp_path / "VsichkiKazina" / "social" / "requests.md"
    text = req.read_text(encoding="utf-8")
    rows = ("| vk-cmd-001 | cancel | vk-0300-p1-fb-1 |  | open |  |\n"
            "| vk-cmd-002 | not before | vk-0300-p1-x-1 | 2026-11-06 | open |  |\n"
            "| vk-cmd-003 | cancel | vk-0999-p1-fb-1 |  | open |  |\n"
            "| vk-cmd-004 | fix | vk-0300-p1-ig-1 |  | open |  |\n")
    req.write_text(text.rstrip("\n") + "\n" + rows, encoding="utf-8")
    w.check(u("2026-11-03 13:10"))
    assert w.states() == {FB: "cancelled", IG: "needs_fix", X: "waiting_for_article"}
    assert w.post(X)["not_before_utc"] == "2026-11-05T22:00:00Z"               # local midnight in Sofia
    after = req.read_text(encoding="utf-8")
    assert "| vk-cmd-001 | cancel | vk-0300-p1-fb-1 |  | done |  |" in after
    assert "| vk-cmd-003 | cancel | vk-0999-p1-fb-1 |  | ignored | not approved yet" in after
    assert "| vk-cmd-004 | fix | vk-0300-p1-ig-1 |  | open |  |" in after          # the drafting run takes it
    w.deploy("ruletka-shansove", html=GOOD_PAGE)
    w.check(u("2026-11-04 07:10"))
    assert w.post(X)["planned_slot_utc"] == "2026-11-06T10:30:00Z"


def test_follow_up_expires(tmp_path):
    w = replay.World(tmp_path, settings_text=replay.SETTINGS.replace(
        "| fb-vsichkikazina | facebook | ch-fb | on | 1 |", "| fb-vsichkikazina | facebook | ch-fb | on | 2 |"))
    w.article("vk-0300", "2026-11-02-ruletka-shansove", ARTICLE)
    two = dict(DRAFT_0300, posts=[DRAFT_0300["posts"][0], dict(DRAFT_0300["posts"][0], role="follow-up")])
    w.draft(two)
    w.merge_pack("vk-0300-p1", "2026-11-03T11:00:00Z")
    w.deploy("ruletka-shansove", html=GOOD_PAGE)
    scheduled(w)
    follow = "vk-0300-p1-fb-2"
    assert w.post(follow)["planned_slot_utc"] == "2026-11-18T10:30:00Z"           # 14 days after the launch
    w.set_settings(replay.SETTINGS.replace("| social | on |", "| social | on |\n| pause | on |"), at="2026-11-05T08:00:00Z")
    w.check(u("2026-11-05 09:10"))
    assert w.post(follow)["state"] == "held"
    w.check(u("2027-01-18 09:10"))                                              # 60 days after its earliest time
    assert w.post(follow)["state"] == "expired" and w.post("vk-0300-p1-fb-1")["state"] == "published"


# --- safety (I1, flow 14; AC 56, 89) and the dry run -----------------------------------------------------

def test_a_leaked_key_stops_hand_overs_until_it_is_replaced(tmp_path):
    w = world(tmp_path)
    secret = {"postiz-key": "pz-0123456789-secret"}
    w.check(u("2026-11-04 07:10"), own_secrets=secret)
    w.repo.sha, w.repo.diff = "c1", "+ debug: pz-0123456789-secret\n"
    w.check(u("2026-11-04 08:10"), own_secrets=secret)
    assert set(w.states().values()) == {"planned"} and w.postiz.items == {}
    assert {"kind": "key", "text": "replace the postiz-key: it was found in the repository", "level": "red"} in \
        w.ledger()["banners"]
    assert "pz-0123456789-secret" not in (tmp_path / "VsichkiKazina" / "social" / "ledger.json").read_text(encoding="utf-8")
    w.check(u("2026-11-04 09:10"), own_secrets={"postiz-key": "pz-new-value-987654"})   # replaced in the guest
    assert set(w.states().values()) == {"scheduled"}


def test_github_unreachable_no_hand_over_but_known_pull_backs_run(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    w.db.set_switches("vsichkikazina", "2026-11-04T08:20:00Z", stop_now=True)   # stop-now seen by the control loop
    w.gh.down, w.repo.ok = True, False
    w.check(u("2026-11-04 09:10"))
    assert set(w.states().values()) == {"held"} and w.postiz.items == {}
    assert any(b["kind"] == "github" for b in w.ledger()["banners"])


def test_dry_run_sends_nothing(tmp_path):
    w = world(tmp_path, dry_run=True)
    scheduled(w)
    assert set(w.states().values()) == {"scheduled"} and w.postiz.items == {}
    assert "handed over (dry run: nothing was sent)" in events(w, FB)
    w.check(u("2026-11-04 11:10"))
    assert set(w.states().values()) == {"published"} and "dry_run" in w.post(FB)["markers"]
    assert any(b["kind"] == "dry run" for b in w.ledger()["banners"])


def test_the_approved_files_are_frozen(tmp_path):
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))
    fb = w.post(FB)
    assert fb["approval"]["approved_files_sha256"] and fb["approval"]["merge_sha"] == "m301"
    d = tmp_path / "VsichkiKazina" / "social" / "packs" / "vk-0300-p1"
    meta = json.loads((d / "pack.json").read_text(encoding="utf-8"))
    meta["posts"][0]["link"]["campaign"] = "other-campaign"                        # a machine field, not the text
    (d / "pack.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    w.check(u("2026-11-04 08:10"))
    assert w.states()[FB] == "needs_fix" and w.states()[IG] == "scheduled"
    assert packmod.load(d)["meta"]["posts"][0]["post_id"] == FB


def test_an_approval_before_the_settings_are_accepted_still_counts(tmp_path):
    """The pack is merged by the approver while settings.md still waits for its PR: the merge is
    left unprocessed until the settings are accepted, then the posts are approved and handed over."""
    w = replay.World(tmp_path, settings_text=replay.SETTINGS.replace("| social | on |", "| social | off |"))
    w.gh.prs.clear(); w.gh.path_commits.clear(); w.gh.commit_prs.clear()     # settings.md never came through a PR
    w.article("vk-0300", "2026-11-02-ruletka-shansove", ARTICLE)
    w.draft(dict(DRAFT_0300, posts=DRAFT_0300["posts"][:1]))
    w.set_settings(replay.SETTINGS.replace("| social | on |", "| social | off |"), merged=False)
    w.merge_pack("vk-0300-p1", "2026-11-03T11:00:00Z")
    w.deploy("ruletka-shansove", html=GOOD_PAGE)
    w.set_status("vk-0300", "posted", posted="2026-11-04")
    w.check(u("2026-11-04 07:10"))
    assert w.post(FB) is None                                                # the approval waits for settings
    assert any(b["text"].startswith("approvals wait") for b in w.ledger()["banners"])
    w.set_settings(replay.SETTINGS, at="2026-11-04T07:30:00Z")
    w.check(u("2026-11-04 08:10"))
    rec = w.post(FB)
    assert rec["approval"]["merged_by"] == "AmigoNiko" and rec["state"] == "scheduled"


def add_command(tmp_path, row):
    req = tmp_path / "VsichkiKazina" / "social" / "requests.md"
    req.write_text(req.read_text(encoding="utf-8").rstrip("\n") + "\n" + row + "\n", encoding="utf-8")
    return req


def test_post_now(tmp_path):
    """A 'post now' line sends an approved post at once (Postiz type now), with every check kept."""
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))                                   # planned for 12:30 Sofia
    req = add_command(tmp_path, "| vk-cmd-001 | post now | vk-0300-p1-fb-1 |  | open |  |\n"
                                "| vk-cmd-002 | post now | vk-0999-p1-fb-1 |  | open |  |")
    w.check(u("2026-11-04 07:20"))
    fb = w.post(FB)
    assert fb["state"] == "scheduled" and fb["planned_slot_utc"] == "2026-11-04T07:20:00Z"
    sent = tool_post(w, FB)
    assert sent["type"] == "now" and sent["date"] == "2026-11-04T07:20:00Z"
    assert w.states()[IG] == "planned" and w.states()[X] == "planned"   # the others keep their slot
    text = req.read_text(encoding="utf-8")
    assert "| vk-cmd-001 | post now | vk-0300-p1-fb-1 |  | done | goes out at once |" in text
    assert "| vk-cmd-002 | post now | vk-0999-p1-fb-1 |  | ignored | not approved yet: approve the pack first |" in text
    handed = [r for r in w.db.audit_rows(post_id=FB) if r["event"] == "handed over"][-1]
    assert handed["payload"]["type"] == "now" and handed["live_page"]["missing"] == []
    w.check(u("2026-11-04 07:30"))                                   # the tool published it at once
    assert w.post(FB)["state"] == "published" and "late" not in w.post(FB)["markers"]


def test_post_now_pulls_a_scheduled_post_back_and_sends_it_at_once(tmp_path):
    w = world(tmp_path)
    scheduled(w)
    old = w.post(IG)["handover"]["postiz_post_id"]
    add_command(tmp_path, "| vk-cmd-001 | post now | vk-0300-p1-ig-1 |  | open |  |")
    w.check(u("2026-11-04 08:20"))
    ig = w.post(IG)
    assert old not in w.postiz.items and ig["state"] == "scheduled" and tool_post(w, IG)["type"] == "now"
    assert "pulled back to go out at once" in events(w, IG)


def test_post_now_keeps_the_pause(tmp_path):
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))
    w.set_settings(replay.SETTINGS.replace("| social | on |", "| social | on |\n| pause | on |"), at="2026-11-04T07:12:00Z")
    add_command(tmp_path, "| vk-cmd-001 | post now | vk-0300-p1-fb-1 |  | open |  |")
    w.check(u("2026-11-04 07:20"))
    assert w.post(FB)["state"] == "held" and w.postiz.items == {}


# --- the time chosen for a pack: at once, or a day and time (post now / post at) ---------------

def register_open(tmp, pack_id):
    from social import board
    p = tmp / "VsichkiKazina" / "social" / "packs.md"
    p.write_text(board.upsert_pack(p.read_text(encoding="utf-8"), {"pack_id": pack_id, "source": pack_id[:7],
                                                                   "status": "open", "pr": "#301"}), encoding="utf-8")


def test_a_time_chosen_before_the_merge_waits_for_it(tmp_path):
    """'post now vk-0300-p1' written while the pack is still in review stays open; after the merge
    every post of the pack goes out at once."""
    w = replay.World(tmp_path)
    w.article("vk-0300", "2026-11-02-ruletka-shansove", ARTICLE)
    w.draft(DRAFT_0300)
    w.deploy("ruletka-shansove", html=GOOD_PAGE)
    w.set_status("vk-0300", "posted", posted="2026-11-04")
    register_open(tmp_path, "vk-0300-p1")
    req = add_command(tmp_path, "| vk-cmd-001 | post now | vk-0300-p1 |  | open |  |")
    w.check(u("2026-11-04 07:10"))                                   # not merged yet: the line waits
    assert "| vk-cmd-001 | post now | vk-0300-p1 |  | open |  |" in req.read_text(encoding="utf-8") and w.states() == {}
    w.merge_pack("vk-0300-p1", "2026-11-04T07:15:00Z", number=301)
    w.check(u("2026-11-04 07:20"))
    assert all(r["state"] == "scheduled" and tool_post(w, r["post_id"])["type"] == "now" for r in w.db.posts("vsichkikazina"))
    assert "| vk-cmd-001 | post now | vk-0300-p1 |  | done | goes out at once when it can (it is waiting for article) "            "(3 of 3 posts) |" in req.read_text(encoding="utf-8")         # the go-live step comes after the commands


def test_post_at_a_day_and_time(tmp_path):
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))                                   # planned for 12:30 Sofia
    req = add_command(tmp_path, "| vk-cmd-001 | post at | vk-0300-p1-fb-1 | 2026-11-05 17:15 |  |  |\n"
                                "| vk-cmd-002 | post at | vk-0300-p1-x-1 | tomorrow |  |  |")
    w.check(u("2026-11-04 07:20"))
    text = req.read_text(encoding="utf-8")
    assert "| vk-cmd-001 | post at | vk-0300-p1-fb-1 | 2026-11-05 17:15 | done | goes out at 2026-11-05 17:15 |" in text
    assert "| vk-cmd-002 | post at | vk-0300-p1-x-1 | tomorrow | ignored | post at needs a day and a time (YYYY-MM-DD HH:MM) |" in text
    assert w.post(FB)["planned_slot_utc"] == "2026-11-05T15:15:00Z"              # 17:15 Sofia (EET)
    w.check(u("2026-11-05 13:10"))                                   # 3 hours before: handed over for its time
    sent = tool_post(w, FB)
    assert w.post(FB)["state"] == "scheduled" and (sent["type"], sent["date"]) == ("schedule", "2026-11-05T15:15:00Z")
