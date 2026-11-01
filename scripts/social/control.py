#!/usr/bin/env python3
"""The control loop (product spec F7; tech spec flow 7). Runs in the guest every 5 minutes,
under the same lock as the publishing check (`flock -w 240 /run/px-social.lock`).

    python3 scripts/social/control.py [--brand vsichkikazina] [--dry-run]

- `/stop-now <brand>` on the pinned issue "Social control": accepted from anyone whose
  repository permission is write, maintain or admin. Every Postiz post of the brand is deleted
  at once and the brand shows "Paused (stop now)".
- `/lift <brand>`: counts from the same people (the team: write access). It ends stop-now, and it
  ends "Paused (tool)" when the channels are enabled again. From anyone else the brand stays
  paused and the dashboard shows "lift ignored: @<author> has no write access".
- When GitHub cannot say who someone is, the comment is left for the next pass.
- Comments are processed once, by comment ID. A comment whose updated_at differs from its
  created_at when it is first read is ignored, so an edit of someone else's comment cannot forge
  a command; later edits are never read again.
- Channels: when every active channel of a brand is disabled in Postiz, the brand becomes
  "Paused (tool)"; the queued posts of a disabled channel are deleted, so they are gone within
  5 minutes even if Postiz kept them queued.
- `post now <post ID>` lines in the request list: the loop runs the publishing check at once
  instead of waiting for minute :10, so such a post goes out within about 5 minutes.
The check exports what this loop records (switches, events) at its next run.
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import brands, github, ledger as ledgermod, postiz, settings as settingsmod  # noqa: E402

COMMAND = re.compile(r"^\s*/(stop-now|lift)\s+([A-Za-z0-9_-]+)\s*$")
STOP_PERMISSIONS = {"write", "maintain", "admin"}


def iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_command(body):
    """(command, brand key) from the first line of a comment, or None."""
    first = (str(body or "").strip().splitlines() or [""])[0]
    m = COMMAND.match(first)
    return (m.group(1).lower(), m.group(2).lower()) if m else None


def accounts_of(db, brand_key):
    acc = db.accepted_settings(brand_key)
    return settingsmod.parse(acc["text"], brand_key).accounts if acc else []


def pull_back(db, client, brand_key, utc, why, channel_ids=None, dry_run=False, reason="held:paused"):
    """Delete the brand's posts from the tool (all of them, or those of some channels): every
    post the check handed over, and anything else queued on the brand's channels."""
    accounts = {a["postiz_channel_id"]: a for a in accounts_of(db, brand_key) if a["postiz_channel_id"]}
    chans = set(channel_ids) if channel_ids is not None else set(accounts)
    deleted = []
    for r in db.posts(brand_key, ["scheduled"]):
        h = r.get("handover") or {}
        if h.get("channel_id") not in chans or not h.get("postiz_post_id"):
            continue
        if not dry_run and not h.get("dry_run"):
            client.delete(h["postiz_post_id"])
        deleted.append(h["postiz_post_id"])
        r.setdefault("handover_history", []).append(h)
        r.update({"handover": None, "state": "held", "reason": reason, "planned_slot_utc": None,
                  "held_since_utc": utc, "updated_utc": utc})
        db.save(r)
        db.audit(utc, brand_key, r["post_id"], "pulled back from the tool", actor="control-loop", why=why,
                 postiz_post_id=h["postiz_post_id"])
    now = datetime.strptime(utc, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    for p in client.posts(now - timedelta(days=2), now + timedelta(days=90)):
        if p["channel_id"] in chans and p["state"] == "QUEUE" and p["id"] not in deleted:
            if not dry_run:
                client.delete(p["id"])
            deleted.append(p["id"])
            db.audit(utc, brand_key, None, "deleted a queued post from the tool", actor="control-loop", why=why,
                     postiz_post_id=p["id"])
    return deleted


def run(db, gh, client, issue, brand_keys, now=None, dry_run=False):
    """One pass: commands first, then the channels. Returns what happened, for the log."""
    now = now or datetime.now(timezone.utc)
    utc = iso(now)
    out = {"commands": [], "deleted": [], "tool_pause": {}}
    for c in gh.issue_comments(issue) if gh is not None and issue else []:
        cid = c["id"]
        if db.control_seen(cid):
            continue
        author = ((c.get("user") or {}).get("login") or "").strip()
        got = parse_command(c.get("body"))
        if not got:
            db.control_event(cid, None, None, author, "", False, utc, "not a command")
            continue
        command, brand_key = got
        if c.get("updated_at") and c.get("created_at") and c["updated_at"] != c["created_at"]:
            db.control_event(cid, brand_key, command, author, "", False, utc, "ignored: edited before it was read")
            out["commands"].append((cid, command, brand_key, "ignored: edited"))
            continue
        if brand_key not in brand_keys:
            db.control_event(cid, brand_key, command, author, "", False, utc, f"ignored: unknown brand {brand_key}")
            continue
        try:
            perm = gh.permission(author)
        except github.GitHubError:
            out["commands"].append((cid, command, brand_key, "waits: GitHub could not say who wrote it"))
            continue
        ok = perm in STOP_PERMISSIONS
        if command == "stop-now":
            note = "stop now accepted" if ok else f"ignored: {author} has {perm} permission"
            db.control_event(cid, brand_key, command, author, perm, ok, utc, note)
            if ok:
                db.set_switches(brand_key, utc, stop_now=True)
                db.audit(utc, brand_key, None, "stop now", actor="control-loop", author=author, comment=cid)
                db.commit()
            out["commands"].append((cid, command, brand_key, note))
        else:
            if not ok or author.lower().endswith("[bot]"):         # a person of the team lifts it, never a bot
                db.control_event(cid, brand_key, command, author, perm, False, utc, f"lift ignored: {author} has {perm} permission")
                out["commands"].append((cid, command, brand_key, f"lift ignored: {author} has {perm} permission"))
                continue
            changes = {"stop_now": False}
            chans = _brand_channels(db, client, brand_key)
            if not chans or not all(ch.get("disabled") for ch in chans):
                changes["tool_pause"] = False
            db.set_switches(brand_key, utc, **changes)
            note = "lifted" + ("" if "tool_pause" in changes else " (stop now only: the channels are still disabled)")
            db.control_event(cid, brand_key, command, author, perm, True, utc, note)
            db.audit(utc, brand_key, None, "lift", actor="control-loop", author=author, comment=cid, note=note)
            out["commands"].append((cid, command, brand_key, note))
    for brand_key in brand_keys:
        try:
            chans = _brand_channels(db, client, brand_key)
            disabled = [ch["id"] for ch in chans if ch.get("disabled")]
            if chans and len(disabled) == len(chans) and not db.switches(brand_key)["tool_pause"]:
                db.set_switches(brand_key, utc, tool_pause=True)
                db.audit(utc, brand_key, None, "paused in the tool", actor="control-loop", channels=disabled)
            out["tool_pause"][brand_key] = db.switches(brand_key)["tool_pause"]
            sw = db.switches(brand_key)
            if sw["stop_now"] or sw["tool_pause"]:            # again at every pass, until the stop is lifted
                out["deleted"] += pull_back(db, client, brand_key, utc, "stop now" if sw["stop_now"] else "paused in the tool",
                                            dry_run=dry_run)
            elif disabled:
                out["deleted"] += pull_back(db, client, brand_key, utc, "channel disabled in the tool", disabled,
                                            dry_run, reason="held:channel_disabled")
        except postiz.PostizError as e:                       # the next pass, 5 minutes later, tries again
            db.audit(utc, brand_key, None, "control loop: the tool could not be reached", actor="control-loop",
                     detail=str(e))
            out.setdefault("errors", []).append(str(e))
        db.commit()
    return out


def pending_post_now(gh, brand_key):
    """True when the brand's request list on main holds an open 'post now' line."""
    from social import board
    try:
        raw = gh.file_at(f"{brands.brand(brand_key)['dir']}/social/requests.md", "main")
    except github.GitHubError:
        return False
    if not raw:
        return False
    _, cmds = board.parse_requests(raw.decode("utf-8"))
    return any(c.get("command") == "post now" and c.get("status") == "open" for c in cmds)


def _brand_channels(db, client, brand_key):
    active = {a["postiz_channel_id"] for a in accounts_of(db, brand_key) if a["active"] and a["postiz_channel_id"]}
    return [c for c in client.integrations() if c["id"] in active]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--brand", action="append")
    ap.add_argument("--dry-run", action="store_true", default=os.environ.get("DRY_RUN") == "1")
    a = ap.parse_args(argv)
    from social import github_app
    token, _ = github_app.installation_token(os.environ["PX_SOCIAL_APP_ID"], os.environ["PX_SOCIAL_INSTALLATION_ID"],
                                             Path(os.environ["PX_SOCIAL_APP_KEY_FILE"]).read_text(encoding="utf-8"))
    db = ledgermod.Ledger(os.environ.get("PX_SOCIAL_DB", "/var/lib/px-social/state.sqlite"))
    client = postiz.Postiz(os.environ["POSTIZ_API_URL"], os.environ["POSTIZ_API_KEY"])
    keys = a.brand or [x.strip() for x in os.environ.get("PX_SOCIAL_ENABLED_BRANDS", "").split(",") if x.strip()] \
        or list(brands.BRANDS)
    gh = github.GitHub(token)
    out = run(db, gh, client, int(os.environ.get("PX_SOCIAL_CONTROL_ISSUE", "0") or 0), keys,
              dry_run=a.dry_run)
    db.close()
    for brand_key in keys:                            # 'post now' does not wait for minute :10
        if pending_post_now(gh, brand_key):
            from social import publishing_check
            out.setdefault("checks", []).append(publishing_check.main(["--brand", brand_key] + (["--dry-run"] if a.dry_run else [])))
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
