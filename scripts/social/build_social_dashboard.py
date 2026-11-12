#!/usr/bin/env python3
"""Dashboard data for the two social tabs (product spec G1–G3; tech spec flow 12).

    python3 scripts/social/build_social_dashboard.py [brand]

Writes docs/data/social/<brand>-review.json   (Posts for review: one row per pack or fix PR,
                                               failed requests, skipped operator/bonus articles)
       docs/data/social/<brand>-schedule.json (Scheduled & published: one row per post, the
                                               counters and the banners, from the ledger the
                                               publishing check exports)
       docs/data/social/<brand>-board.json    (New post and Settings: the settings as written, the
                                               articles a request may name, requests and commands)
The pages read these from GitHub Pages; the review tab also lists open social/ PRs live and the
schedule tab reads its file fresh through the contents API, like docs/index.html does today. The
page holds no key: everything it does goes through GitHub pages a person confirms (intake.py).
"""
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import board, brands, github, settings as settingsmod  # noqa: E402

BADGES = {"in_review": "In review", "rejected": "Rejected", "needs_fix": "Needs fix", "in_fix_pr": "Needs fix",
          "article_changed": "Article changed", "waiting_for_article": "Waiting for article", "planned": "Planned",
          "scheduled": "Scheduled", "held": "Held", "published": "Published", "failed": "Failed",
          "expired": "Expired", "cancelled": "Cancelled", "not_from_pack": "Not from a pack"}
MARKERS = {"changed_in_tool": "changed in the tool", "article_changed_after_publishing": "article changed after publishing",
           "waited_14_days": "waited 14 days", "waiting_long": "waiting long",
           "waiting_long_for_article": "waiting long for article", "missed_window": "missed window",
           "missed_slot": "missed slot", "late": "late", "published_breaks_a_rule": "breaks a rule",
           "dry_run": "dry run: nothing was sent"}
REASONS = {
    "held:paused": "paused", "held:social_off": "social is off or the settings have errors",
    "held:account_off": "the account is off or has a settings error", "held:reconnect_account": "reconnect account",
    "held:channel_disabled": "channel disabled in the tool", "held:article_unapproved": "article un-approved",
    "held:live_page_differs": "live page differs", "held:no_live_link": "no live link", "held:no_visual": "no visual",
    "needs_fix:merged_by_other": "merged by someone who cannot approve", "needs_fix:check_failed": "a check failed",
    "needs_fix:text_differs_from_approved": "text differs from approved",
    "needs_fix:changed_in_tool": "text changed in the tool", "needs_fix:fix_line": "fix line",
    "article_changed": "a line the post quotes is no longer in the article",
    "cancelled:in_the_tool": "cancelled in the tool", "cancelled:cancel_line": "cancel line",
    "cancelled:fix_pr_closed": "fix PR closed", "cancelled:moved_to_drafts_in_the_tool": "moved to drafts in the tool",
    "expired:follow_up_60_days": "follow-up 60 days past its earliest date",
    "expired:fix_pr_not_merged_in_30_days": "fix PR not merged within 30 days",
}
REPO_URL = f"https://github.com/{github.REPO}"


def reason_text(reason):
    """The reason as the dashboard shows it (G2)."""
    reason = str(reason or "")
    if reason in REASONS:
        return REASONS[reason]
    for prefix in ("waiting:", "failed:"):
        if reason.startswith(prefix):
            return reason[len(prefix):]
    return reason.split(":", 1)[-1].replace("_", " ")


def _iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse(ts):
    try:
        return datetime.strptime(str(ts)[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
    except ValueError:
        try:
            return datetime.strptime(str(ts)[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except ValueError:
            return None


def _git_show(root, ref, path):
    try:
        return subprocess.run(["git", "show", f"{ref}:{path}"], cwd=root, capture_output=True, check=True,
                              timeout=30).stdout.decode("utf-8", "replace")
    except (OSError, subprocess.SubprocessError):
        return None


def pack_summary(root, brand_key, row):
    """{accounts, posts, formats} of a pack from main, else from its branch."""
    rel = f"{brands.brand(brand_key)['dir']}/social/packs/{row['pack_id'].split('-fix-')[0]}/pack.json"
    local = Path(root) / rel
    raw = local.read_text(encoding="utf-8") if local.exists() else _git_show(root, f"origin/{row.get('branch', '')}", rel)
    try:
        meta = json.loads(raw) if raw else None
    except ValueError:
        meta = None
    if not meta:
        return {"accounts": [], "posts": int(row.get("posts") or 0) if str(row.get("posts", "")).isdigit() else None,
                "formats": []}
    posts = meta.get("posts", [])
    return {"accounts": sorted({p["account_id"] for p in posts}), "posts": len(posts),
            "formats": sorted({p.get("format", "single") for p in posts})}


def review_data(root, brand_key, now):
    reg = board.parse_packs(board._read(board.packs_path(brand_key, root)))
    reqs, _cmds = board.parse_requests(board._read(board.requests_path(brand_key, root)))
    rows, skipped = [], []
    for r in reg:
        status = r.get("status", "")
        if status == "skipped":
            skipped.append({"item_id": r.get("source") or r.get("pack_id"), "reason": r.get("note", "")})
            continue
        created = _parse(r.get("created"))
        age = max(0, (now - created).days) if created else None
        number = "".join(ch for ch in r.get("pr", "") if ch.isdigit())
        s = pack_summary(root, brand_key, r)
        rows.append({
            "pack_id": r["pack_id"], "kind": "fix" if "-fix-" in r["pack_id"] else "pack",
            "source": r.get("source", ""), "title": r.get("title", ""), **s,
            "pr": int(number) if number else None, "pr_url": f"{REPO_URL}/pull/{number}" if number else "",
            "status": {"open": "in review"}.get(status, status), "created": r.get("created", ""),
            "age_days": age, "waiting_long": status == "open" and age is not None and age >= 14,
            "note": r.get("note", ""),
        })
    failed = [{"id": q["id"], "kind": q.get("kind", ""), "target": q.get("target", ""), "reason": q.get("reason", "")}
              for q in reqs if q.get("status") == "failed"]
    return {"generated_utc": _iso(now), "brand": brand_key, "rows": rows, "failed_requests": failed,
            "skipped": skipped,
            "open_requests": [{"id": q["id"], "target": q.get("target", "")} for q in reqs if q.get("status") == "open"]}


def schedule_data(root, brand_key, now, tz_name):
    import zoneinfo
    tz = zoneinfo.ZoneInfo(tz_name)
    ledger_path = brands.social_dir(brand_key, root) / "ledger.json"
    try:
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        ledger = {}
    rows, counters = [], {"in_review": 0, "scheduled_next_7_days": 0, "published_this_month": 0, "failed": 0}
    for p in ledger.get("posts", []):
        state = p.get("state", "")
        when = _parse(p.get("published_utc") or p.get("planned_slot_utc") or "")
        local = when.astimezone(tz).strftime("%Y-%m-%d %H:%M") if when else ""
        rows.append({
            "post_id": p["post_id"], "network": p.get("network", ""), "account_id": p.get("account_id", ""),
            "pack_id": p.get("pack_id", ""), "source": p.get("source", ""), "title": p.get("title", ""),
            "state": state, "badge": BADGES.get(state, state), "reason": p.get("reason", ""),
            "reason_text": reason_text(p.get("reason", "")),
            "missing_lines": p.get("missing_lines") or [],
            "markers": [MARKERS.get(m, m) for m in p.get("markers") or []],
            "time_local": local, "published": bool(p.get("published_utc")),
            "network_url": p.get("network_url", ""), "article_url": p.get("article_url", ""),
        })
        if state == "in_review":
            counters["in_review"] += 1
        if state == "failed":
            counters["failed"] += 1
        if state in ("planned", "scheduled") and when and now <= when <= now + timedelta(days=7):
            counters["scheduled_next_7_days"] += 1
        if state == "published" and when and when.astimezone(tz).strftime("%Y-%m") == now.astimezone(tz).strftime("%Y-%m"):
            counters["published_this_month"] += 1
    rows.sort(key=lambda r: (r["time_local"] or "9999", r["post_id"]), reverse=False)
    return {"generated_utc": _iso(now), "brand": brand_key, "time_zone": tz_name,
            "last_check_utc": ledger.get("last_check_utc"), "rows": rows, "counters": counters,
            "banners": ledger.get("banners") or [], "brand_state": ledger.get("brand_state") or {}}


def build(root, brand_key, now=None):
    now = now or datetime.now(timezone.utc)
    s = settingsmod.load(brand_key, root)
    review = review_data(root, brand_key, now)
    schedule = schedule_data(root, brand_key, now, s.brand["time_zone"])
    # G3 / AC 86: the pack and fix PRs in review, and how many posts they hold
    open_rows = [r for r in review["rows"] if r["status"] == "in review"]
    schedule["counters"]["in_review"] = len(open_rows)
    schedule["counters"]["in_review_posts"] = sum(r["posts"] or 0 for r in open_rows)
    schedule["banners"] = schedule["banners"] + [{"kind": "invalid settings", "text": e["message"]} for e in s.errors]
    spend = brands.social_dir(brand_key, root) / "image-spend.json"
    try:
        month = now.strftime("%Y-%m")
        entry = json.loads(spend.read_text(encoding="utf-8"))["months"].get(month, {}).get(brand_key, {})
    except (OSError, ValueError, KeyError):
        entry = {}
    if entry.get("credits_exhausted"):
        schedule["banners"].append({"kind": "credits", "text": "social image credits exhausted"})
    if entry and entry.get("usd", 0) >= s.brand["image_budget_usd"]:
        schedule["banners"].append({"kind": "budget", "text": "image budget reached"})
    schedule["image_spend"] = {"month": now.strftime("%Y-%m"), "usd": round(entry.get("usd", 0.0), 2),
                               "budget_usd": s.brand["image_budget_usd"]}
    return review, schedule


def board_data(root, brand_key, now=None):
    """What the New post and Settings tabs show, so the page reads no file through the API: the
    settings as written (brand values and account rows), the articles a request may name, and the
    requests and commands with their status."""
    from social import mdtable
    root = Path(root)
    text = board._read(settingsmod.path(brand_key, root))
    bt, at = mdtable.find(text, "key", "value"), mdtable.find(text, "account_id", "network")
    brand = {r["key"].strip().lower(): r.get("value", "").strip() for r in (bt["rows"] if bt else []) if r.get("key")}
    accounts = [r for r in (at["rows"] if at else []) if r.get("account_id")]
    try:
        index = json.loads((root / "library" / brand_key / "index.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        index = {"items": []}
    library = [{k: i.get(k) for k in ("id", "slug", "title", "kind", "board_status", "live", "operator_or_bonus")}
               for i in index.get("items", [])]
    reqs, cmds = board.parse_requests(board._read(board.requests_path(brand_key, root)))
    return {"generated_utc": _iso(now or datetime.now(timezone.utc)), "brand": brand_key, "repo": github.REPO,
            "settings": {"brand": brand, "accounts": accounts,
                         "errors": [e["message"] for e in settingsmod.parse(text, brand_key).errors]},
            "library": library, "requests": reqs, "commands": cmds}


def write(root, brand_key, review, schedule, board_json=None):
    out = Path(root) / "docs" / "data" / "social"
    out.mkdir(parents=True, exist_ok=True)
    files = [(f"{brand_key}-review.json", review), (f"{brand_key}-schedule.json", schedule)]
    files += [(f"{brand_key}-board.json", board_json if board_json is not None else board_data(root, brand_key))]
    for name, data in files:
        f = out / name
        old = None
        try:
            old = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pass
        if old and {k: v for k, v in old.items() if k != "generated_utc"} == \
                {k: v for k, v in data.items() if k != "generated_utc"}:
            continue                                   # unchanged: no churn
        f.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    brand_key = sys.argv[1] if len(sys.argv) > 1 else "vsichkikazina"
    if brand_key not in brands.BRANDS:
        print(__doc__)
        return 2
    review, schedule = build(brands.ROOT, brand_key)
    write(brands.ROOT, brand_key, review, schedule)
    print(f"social dashboard: {len(review['rows'])} PR row(s), {len(schedule['rows'])} post row(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
