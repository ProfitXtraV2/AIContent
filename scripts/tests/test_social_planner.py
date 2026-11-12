import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import liveness, planner, settings as st  # noqa: E402

DAILY = st.parse_slots("daily 12:30, 19:30")
ACC = {"fb": {"slots": DAILY, "max_per_day": 2}}


def u(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)


def local(dt, tz="Europe/Sofia"):
    import zoneinfo
    return dt.astimezone(zoneinfo.ZoneInfo(tz)).strftime("%a %Y-%m-%d %H:%M")


# --- slots and local time (F10; AC 83, 84) --------------------------------------------------

def test_slots_keep_local_time_across_clock_changes():
    for day, utc_time in (("2026-10-24", "09:30"), ("2026-10-27", "10:30"), ("2027-03-30", "09:30")):
        slots = planner.expand(st.parse_slots("daily 12:30"), "Europe/Sofia", u(f"{day} 00:00"), days=0)
        assert [s.strftime("%Y-%m-%d %H:%M") for s in slots] == [f"{day} {utc_time}"]
        assert local(slots[0]).endswith("12:30")
    # the night the clocks go back (25 Oct 2026) and forward (28 Mar 2027)
    around = planner.expand(DAILY, "Europe/Sofia", u("2026-10-24 00:00"), days=2)
    assert [local(s) for s in around] == ["Sat 2026-10-24 12:30", "Sat 2026-10-24 19:30", "Sun 2026-10-25 12:30",
                                          "Sun 2026-10-25 19:30", "Mon 2026-10-26 12:30", "Mon 2026-10-26 19:30"]
    spring = planner.expand(DAILY, "Europe/Sofia", u("2027-03-27 00:00"), days=1)
    assert [s.strftime("%H:%M") for s in spring] == ["10:30", "17:30", "09:30", "16:30"]


def test_brand_time_zone():
    # DentalVia 10:00 Europe/Berlin is 11:00 in Sofia, summer and winter
    for day in ("2026-11-10", "2027-06-10"):
        s = planner.expand(st.parse_slots("daily 10:00"), "Europe/Berlin", u(f"{day} 00:00"), days=0)[0]
        assert local(s, "Europe/Berlin").endswith("10:00") and local(s).endswith("11:00")


def test_window():
    # a post for Thursday 19:30 Sofia goes to the tool between 16:30 and 19:00 (AC 53)
    slot = u("2026-11-05 17:30")
    assert local(slot) == "Thu 2026-11-05 19:30"
    assert not planner.in_window(slot, u("2026-11-05 14:29"))
    assert planner.in_window(slot, u("2026-11-05 14:30")) and planner.in_window(slot, u("2026-11-05 17:00"))
    assert not planner.in_window(slot, u("2026-11-05 17:01"))
    # checks at minute 10: two of them fall inside (15:10 and 16:10 UTC = 17:10 and 18:10 Sofia)
    checks = [u("2026-11-05 00:10") + timedelta(hours=h) for h in range(24)]
    assert [local(c)[-5:] for c in checks if planner.in_window(slot, c)] == ["17:10", "18:10"]


# --- order and assignment (F3, F4; AC 48, 59, 74, 75) -------------------------------------------

def test_launch_then_follow_up():
    now = u("2026-11-04 07:10")
    waiting = [{"post_id": "vk-0300-p1-fb-1", "account_id": "fb", "kind": "launch", "went_live": now},
               {"post_id": "vk-0300-p1-fb-2", "account_id": "fb", "kind": "follow-up", "after": "vk-0300-p1-fb-1",
                "delay_days": 14}]
    got, last = planner.plan(waiting, ACC, [], now, "Europe/Sofia")
    assert local(got["vk-0300-p1-fb-1"]["slot"]) == "Wed 2026-11-04 12:30"       # first slot ≥ live + 30 min
    assert local(got["vk-0300-p1-fb-2"]["slot"]) == "Wed 2026-11-18 12:30"       # ≥ 14 days after the launch
    assert got["vk-0300-p1-fb-2"]["earliest"] == got["vk-0300-p1-fb-1"]["slot"] + timedelta(days=14)
    # go-live seen at 12:05: 12:30 is less than 30 minutes away, so 19:30
    got, _ = planner.plan(waiting[:1], ACC, [], u("2026-11-04 10:05"), "Europe/Sofia")
    assert local(got["vk-0300-p1-fb-1"]["slot"]) == "Wed 2026-11-04 19:30"


def test_one_post_per_slot_and_the_daily_maximum():
    now = u("2026-11-04 07:10")
    held = [{"post_id": f"vk-03{i:02d}-p1-fb-1", "account_id": "fb", "kind": "launch", "went_live": now - timedelta(days=1)}
            for i in range(6)]
    one_a_day = {"fb": {"slots": DAILY, "max_per_day": 1}}
    taken = [{"account_id": "fb", "slot": u("2026-11-05 10:30")}]               # a post in the tool keeps its slot
    got, _ = planner.plan(held, one_a_day, taken, now, "Europe/Sofia")
    days = [local(got[p["post_id"]]["slot"]) for p in held]
    assert days == ["Wed 2026-11-04 12:30", "Fri 2026-11-06 12:30", "Sat 2026-11-07 12:30", "Sun 2026-11-08 12:30",
                    "Mon 2026-11-09 12:30", "Tue 2026-11-10 12:30"]


def test_priority_and_move_up():
    now = u("2026-11-20 07:10")
    waiting = [
        {"post_id": "vk-req-001-p1-fb-1", "account_id": "fb", "kind": "request", "eligible": now - timedelta(days=15)},
        {"post_id": "vk-0400-p1-fb-1", "account_id": "fb", "kind": "launch", "went_live": now - timedelta(hours=1)},
        {"post_id": "vk-req-002-p1-fb-1", "account_id": "fb", "kind": "request", "eligible": now - timedelta(days=2)},
        {"post_id": "vk-0300-p1-fb-2", "account_id": "fb", "kind": "follow-up", "after": "vk-0300-p1-fb-1",
         "delay_days": 14}]
    known = {"vk-0300-p1-fb-1": u("2026-11-04 10:30")}                       # published 16 days ago
    got, _ = planner.plan(waiting, ACC, [], now, "Europe/Sofia", known)
    order = sorted(got, key=lambda pid: got[pid]["slot"])
    assert order == ["vk-req-001-p1-fb-1", "vk-0400-p1-fb-1", "vk-req-002-p1-fb-1", "vk-0300-p1-fb-2"]
    assert got["vk-req-001-p1-fb-1"]["waited_14_days"] is True and got["vk-req-002-p1-fb-1"]["waited_14_days"] is False


def test_schedule_full():
    now = u("2026-11-01 07:10")
    many = [{"post_id": f"vk-{1000 + i}-p1-fb-1", "account_id": "fb", "kind": "launch", "went_live": now} for i in range(70)]
    got, last = planner.plan(many, ACC, [], now, "Europe/Sofia")
    assert planner.schedule_full(last, now) == ["fb"]                         # 70 posts, 2 a day: 35 days ahead
    assert all(g["slot"] for g in got.values())
    assert planner.schedule_full(planner.plan(many[:10], ACC, [], now, "Europe/Sofia")[1], now) == []


def test_not_before():
    now = u("2026-11-04 07:10")
    got, _ = planner.plan([{"post_id": "a", "account_id": "fb", "kind": "launch", "went_live": now,
                            "not_before": u("2026-11-09 22:00")}], ACC, [], now, "Europe/Sofia")
    assert local(got["a"]["slot"]) == "Tue 2026-11-10 12:30"


# --- go-live and the live page (F2, F5; AC 49, 50, 51) ------------------------------------------

BRAND = st.parse((Path(__file__).resolve().parent / "fixtures" / "social" / "settings.md")
                 .read_text(encoding="utf-8")).brand


def site(pages):
    return liveness.Site("vsichkikazina", get=lambda url: pages.get(url, (404, "")))


def test_is_live():
    art = {"slug": "ruletka-shansove", "kind": "article", "board_status": "approved"}
    page = {"https://vsichkikazina.bg/blog/ruletka-shansove/": (200, "<article>ok</article>")}
    assert liveness.is_live(art, {}, BRAND, "vsichkikazina", site(page))[0] is False          # not deployed
    record = {"ruletka-shansove": {"path": "blog/ruletka-shansove", "deployed_utc": "t"}}
    assert liveness.is_live(art, record, BRAND, "vsichkikazina", site(page))[:2] == \
        (True, "https://vsichkikazina.bg/blog/ruletka-shansove/")                             # record, write-back late
    posted = dict(art, board_status="posted")
    assert liveness.is_live(posted, {}, BRAND, "vsichkikazina", site(page))[0] is True         # vk-0003: posted, no record
    assert liveness.is_live(posted, {}, BRAND, "vsichkikazina", site({}))[0] is False           # does not answer
    intro = {"slug": "hub-intro-casino-payments", "kind": "hub-intro", "board_status": "approved"}
    assert liveness.is_live(intro, {}, BRAND, "vsichkikazina", site(page))[0] is False
    rec = {"hub-intro-casino-payments": {"path": "blog/casino-payments"}}
    live = {"https://vsichkikazina.bg/blog/casino-payments/": (200, "<main>ok</main>")}
    assert liveness.is_live(intro, rec, BRAND, "vsichkikazina", site(live))[:2] == \
        (True, "https://vsichkikazina.bg/blog/casino-payments/")                              # never /blog/hub-intro-…/
    assert liveness.live_address(intro, {"hub-intro-casino-payments": {"path": "blog/other"}}, BRAND, "vsichkikazina") is None


def test_redirects_stay_on_the_brand_domain():
    pages = {"https://vsichkikazina.bg/blog/a/": (301, "/blog/b/"), "https://vsichkikazina.bg/blog/b/": (200, "ok"),
             "https://vsichkikazina.bg/blog/c/": (302, "https://elsewhere.example/blog/c/")}
    s = site(pages)
    assert s.fetch("https://vsichkikazina.bg/blog/a/")["ok"] is True
    assert s.fetch("https://vsichkikazina.bg/blog/c/") == {"ok": False, "status": 0, "url": "https://elsewhere.example/blog/c/",
                                                           "text": "", "error": "leaves the brand's domain"}


def test_live_page_check():
    fields = {"text": "Възвръщаемостта е „96,48%“ при 37 полета. [[LINK]] 18+ Играйте отговорно.",
              "image_text": ["37 полета", "2/4"], "alt_text": "Колело"}
    page = "Рулетка\nВъзвръщаемостта е 96,50% при 37 полета."
    assert liveness.missing_on_pages(fields, [page]) == ["96,48%"]                         # AC 51
    assert liveness.missing_on_pages(fields, ["Възвръщаемостта е 96,48% при 37 полета."]) == []
    quoted = {"text": "Казват, че „бакара е лесна“.", "image_text": [], "alt_text": ""}
    assert liveness.missing_on_pages(quoted, ["Нищо такова."]) == ["бакара е лесна"]
