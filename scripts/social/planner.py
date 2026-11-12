"""Slot planner (product spec F3, F4, F10; tech spec flow 5).

Slots are local wall-clock times in the brand's time zone. Each account's slot rules are
expanded into local times for the next 45 days and converted to UTC with zoneinfo, so a 12:30
slot stays 12:30 in Sofia (or Berlin) across the clock changes.

Order of the posts that wait for a slot:
  0. requested posts that became eligible 14 or more days ago ("waited 14 days");
  1. launch posts, by go-live;
  2. other requested posts, by eligibility;
  3. follow-ups, by earliest time (the previous post of the same pack and account, planned,
     scheduled or published, plus the account's follow-up delay).
Each post takes the first free slot at or after its earliest time, one post per slot, within the
account's daily maximum. Posts already in the tool keep their slot; published posts count toward
the maximum of their local date. The plan is worked out again at every check, so a planned slot
is provisional until hand-over.
"""
import zoneinfo
from collections import Counter
from datetime import datetime, timedelta, timezone

HORIZON_DAYS = 45
LEAD = timedelta(minutes=30)          # the latest a post can still be handed over before its slot
LAUNCH_AFTER_LIVE = timedelta(minutes=30)
MOVE_UP_AFTER = timedelta(days=14)
FULL_AFTER = timedelta(days=30)


def expand(rules, tz_name, start_utc, days=HORIZON_DAYS):
    """The UTC times of every slot from start_utc on, for `days` local days, in order."""
    tz = zoneinfo.ZoneInfo(tz_name)
    first = start_utc.astimezone(tz).date()
    out = set()
    for i in range(days + 1):
        d = first + timedelta(days=i)
        for rule in rules:
            if d.weekday() not in rule["days"]:
                continue
            for t in rule["times"]:
                hh, mm = (int(x) for x in t.split(":"))
                out.add(datetime(d.year, d.month, d.day, hh, mm, tzinfo=tz).astimezone(timezone.utc))
    return sorted(s for s in out if s >= start_utc)


def local_date(dt, tz_name):
    return dt.astimezone(zoneinfo.ZoneInfo(tz_name)).date()


def plan(waiting, accounts, taken, now, tz_name, known_slots=None):
    """Slots for the posts that wait.

    waiting:  [{post_id, account_id, kind: launch | request | follow-up, earliest: datetime or None,
                eligible: datetime or None (requests), went_live: datetime or None (launch posts),
                after: post_id or None (follow-ups), delay_days: int, not_before: datetime or None}]
    accounts: {account_id: {"slots": rules, "max_per_day": n}}  (usable accounts only)
    taken:    [{account_id, slot: datetime}]  posts in the tool and published posts
    known_slots: {post_id: datetime}  slots or publish times of posts not in `waiting`
                 (a follow-up's previous post may be scheduled or published already)

    Returns ({post_id: {"slot", "earliest", "waited_14_days"}}, {account_id: last planned slot}).
    """
    used = {a: set() for a in accounts}
    per_day = {a: Counter() for a in accounts}
    for t in taken:
        if t["account_id"] in accounts:
            used[t["account_id"]].add(t["slot"])
            per_day[t["account_id"]][local_date(t["slot"], tz_name)] += 1
    slots = {a: expand(acc["slots"], tz_name, now) for a, acc in accounts.items()}
    known = dict(known_slots or {})
    result, last = {}, {}

    def take(p, earliest):
        acc = accounts.get(p["account_id"])
        start = max(earliest, now + LEAD) if earliest else now + LEAD
        if p.get("not_before"):
            start = max(start, p["not_before"])
        slot = None
        if acc:
            for s in slots[p["account_id"]]:
                day = local_date(s, tz_name)
                if s < start or s in used[p["account_id"]] or per_day[p["account_id"]][day] >= acc["max_per_day"]:
                    continue
                slot = s
                used[p["account_id"]].add(s)
                per_day[p["account_id"]][day] += 1
                last[p["account_id"]] = max(last.get(p["account_id"], s), s)
                break
        result[p["post_id"]] = {"slot": slot, "earliest": earliest,
                                "waited_14_days": p.get("_moved_up", False)}
        if slot:
            known[p["post_id"]] = slot

    far = datetime.max.replace(tzinfo=timezone.utc)
    requests = [p for p in waiting if p["kind"] == "request"]
    moved = [p for p in requests if p.get("eligible") and now - p["eligible"] >= MOVE_UP_AFTER]
    for p in moved:
        p["_moved_up"] = True
    others = [p for p in requests if p not in moved]
    launches = [p for p in waiting if p["kind"] == "launch"]
    for p in sorted(moved, key=lambda p: (p["eligible"], p["post_id"])):
        take(p, p.get("earliest") or p["eligible"])
    for p in sorted(launches, key=lambda p: (p.get("went_live") or far, p["post_id"])):
        take(p, p.get("earliest") or ((p["went_live"] + LAUNCH_AFTER_LIVE) if p.get("went_live") else None))
    for p in sorted(others, key=lambda p: (p.get("eligible") or far, p["post_id"])):
        take(p, p.get("earliest") or p.get("eligible"))

    # follow-ups: each after its previous post; the one that can go first goes first
    rest = [p for p in waiting if p["kind"] == "follow-up"]
    while rest:
        ready = []
        for p in rest:
            prev = known.get(p.get("after"))
            if prev is not None:
                ready.append((max(prev + timedelta(days=int(p.get("delay_days") or 0)),
                                  p.get("earliest") or prev), p))
        if not ready:
            break
        earliest, p = min(ready, key=lambda x: (x[0], x[1]["post_id"]))
        take(p, earliest)
        rest.remove(p)
    for p in rest:                                   # the previous post has no slot yet
        result[p["post_id"]] = {"slot": None, "earliest": None, "waited_14_days": False}
    return result, last


def schedule_full(last_slots, now):
    """Accounts whose last planned slot is more than 30 days ahead (F3 warning)."""
    return sorted(a for a, s in last_slots.items() if s - now > FULL_AFTER)


def in_window(slot, now):
    """True from 3 hours to 30 minutes before the slot (flow 6): the hand-over window."""
    return slot is not None and LEAD <= slot - now <= timedelta(hours=3)
