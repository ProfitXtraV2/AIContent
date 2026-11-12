#!/usr/bin/env python3
"""The social boards on main: the request list and the pack registry (tech spec, Data model).

<Brand>/social/requests.md — two tables, edited by people in GitHub's web editor:
  Requests | id | kind | target | angle | format | slides | sources | target_page | accounts | earliest
           | status | reason | pack_id | added |
  Commands | id | command | post_id | date | status | note |
    kind: keyword | article | intro | topic;  status: open | done | failed
    format: (the account's) | carousel | single;  slides: (the account's) | 3–10
    sources: web addresses and sources/<file>.md, comma-separated (the facts may come from them)
    command: fix | cancel | not before | post now | post at;  status: open | done | ignored (with the note)
    post now and post at may name a whole pack (its pack ID): every post of it. post at takes a local
    day and time (YYYY-MM-DD HH:MM). A line for a pack still in review waits for its merge.
A table written before format, slides and sources existed is read as it is (they count as empty).

<Brand>/social/packs.md — the pack registry, one row per pack or fix PR, and per skipped article:
  | pack_id | source | title | pr | branch | status | posts | created | updated | note |
    status: open | merged | closed | skipped | expired

    python3 scripts/social/board.py ids [brand]     # give new request and command rows their IDs
"""
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import brands, ids, mdtable  # noqa: E402

REQUEST_COLS = ["id", "kind", "target", "angle", "format", "slides", "sources", "target_page", "accounts",
                "earliest", "status", "reason", "pack_id", "added"]
REQUEST_KINDS = ("keyword", "article", "intro", "topic")
SOURCE_FILE = re.compile(r"^sources/[\w.-]+\.(?:md|txt)$")      # a request's text source, under <Brand>/social/
COMMAND_COLS = ["id", "command", "post_id", "date", "status", "note"]
PACK_COLS = ["pack_id", "source", "title", "pr", "branch", "status", "posts", "created", "updated", "note"]
COMMANDS = ("fix", "cancel", "not before", "post now", "post at")
PACK_COMMANDS = ("post now", "post at")                          # may name a whole pack


def today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def requests_path(brand_key, root=brands.ROOT):
    return brands.social_dir(brand_key, root) / "requests.md"


def packs_path(brand_key, root=brands.ROOT):
    return brands.social_dir(brand_key, root) / "packs.md"


def _read(p):
    return Path(p).read_text(encoding="utf-8") if Path(p).exists() else ""


# --- requests ------------------------------------------------------------------------------

def parse_requests(md_text):
    """(requests, commands) as lists of dicts. Rows with nothing in them are dropped."""
    rt = mdtable.find(md_text, "kind", "target")
    ct = mdtable.find(md_text, "command", "post_id")
    reqs = [r for r in (rt["rows"] if rt else []) if r.get("target") or r.get("id")]
    cmds = [r for r in (ct["rows"] if ct else []) if r.get("command") or r.get("post_id")]
    for r in reqs:
        r["kind"] = (r.get("kind") or "keyword").strip().lower()
        r["status"] = (r.get("status") or "open").strip().lower()
        r["format"] = (r.get("format") or "").strip().lower()
        r["slides"] = (r.get("slides") or "").strip()
        r["sources"] = (r.get("sources") or "").strip()
    for c in cmds:
        c["command"] = re.sub(r"\s+", " ", (c.get("command") or "").strip().lower())
        c["status"] = (c.get("status") or "open").strip().lower()
    return reqs, cmds


def add_request(md_text, row, date):
    """The text with a new request row (its ID and status come from assign_ids); an older table
    gains the format, slides and sources columns (docs/social-md.js addRequest)."""
    rt = mdtable.find(md_text, "kind", "target")
    if rt is None:
        raise ValueError("requests.md has no Requests table")
    new = {"id": "", "status": "", "reason": "", "pack_id": "", "added": date, **row}
    return mdtable.replace(md_text, mdtable.with_columns(rt, REQUEST_COLS), rt["rows"] + [new])


def add_commands(md_text, commands):
    """The text with command rows ({command, post_id, date?, note?}) at the end of the Commands table."""
    ct = mdtable.find(md_text, "command", "post_id")
    if ct is None:
        raise ValueError("requests.md has no Commands table")
    rows = ct["rows"] + [{"id": "", "command": c["command"], "post_id": c["post_id"], "date": c.get("date", ""),
                          "status": "", "note": c.get("note", "")} for c in commands]
    return mdtable.replace(md_text, ct, rows)


def request_sources(req):
    """The web addresses and sources/ files a request names."""
    return mdtable.split_list((req or {}).get("sources", ""))


def request_problem(req):
    """Why a request cannot be drafted as written ("" when it can): its format, slides or sources."""
    kind, fmt, slides = req.get("kind") or "keyword", req.get("format") or "", str(req.get("slides") or "")
    if kind not in REQUEST_KINDS:
        return f"unknown kind {kind!r} ({', '.join(REQUEST_KINDS)})"
    if fmt not in ("", "carousel", "single"):
        return f"format must be carousel or single (or empty for the account's), not {fmt!r}"
    if slides and not (slides.isdigit() and 3 <= int(slides) <= 10):
        return f"slides must be 3–10 (or empty for the account's), not {slides!r}"
    for s in request_sources(req):
        if not (re.match(r"^https?://\S+$", s) or SOURCE_FILE.match(s)):
            return f"a source must be a web address or sources/<file>.md, not {s!r}"
    return ""


def request_format(req, account):
    """(format, slides) for a request's posts on an account: the request's own, else the account's."""
    req = req or {}
    slides = int(req["slides"]) if str(req.get("slides") or "").isdigit() else account.get("slides") or 5
    return (req.get("format") or account.get("format") or "auto"), slides


def assign_ids(md_text, prefix, date=None):
    """The text with an ID (and `open`, and the date added) on every new request and command
    row. Returns (text, [new ids])."""
    date = date or today()
    new = []
    rt = mdtable.find(md_text, "kind", "target")
    if rt:
        rows = rt["rows"]
        known = [r.get("id", "") for r in rows]
        for r in rows:
            if not r.get("id") and r.get("target"):
                r["id"] = ids.next_request_id(prefix, known)
                known.append(r["id"])
                new.append(r["id"])
                r["status"] = r.get("status") or "open"
                r["added"] = r.get("added") or date
        md_text = mdtable.replace(md_text, rt, rows)
    ct = mdtable.find(md_text, "command", "post_id")
    if ct:
        rows = ct["rows"]
        nums = [int(m.group(1)) for m in (re.match(rf"^{prefix}-cmd-(\d+)$", r.get("id", "")) for r in rows) if m]
        n = max(nums, default=0)
        for r in rows:
            if not r.get("id") and (r.get("command") or r.get("post_id")):
                n += 1
                r["id"] = f"{prefix}-cmd-{n:03d}"
                new.append(r["id"])
                r["status"] = r.get("status") or "open"
        md_text = mdtable.replace(md_text, ct, rows)
    return md_text, new


def set_request(md_text, request_id, **fields):
    """The text with one request row changed (status, reason, pack_id)."""
    rt = mdtable.find(md_text, "kind", "target")
    rows = rt["rows"]
    for r in rows:
        if r.get("id") == request_id:
            r.update({k: v for k, v in fields.items() if k in REQUEST_COLS})
    return mdtable.replace(md_text, rt, rows)


def set_command(md_text, command_id, status, note=""):
    ct = mdtable.find(md_text, "command", "post_id")
    rows = ct["rows"]
    for r in rows:
        if r.get("id") == command_id:
            r["status"], r["note"] = status, note
    return mdtable.replace(md_text, ct, rows)


def parse_command(row):
    """{id, kind: fix|cancel|not before, post_id, date} or (None, reason) for a line people wrote."""
    kind = row.get("command", "")
    pid = (row.get("post_id") or "").strip()
    if kind not in COMMANDS:
        return None, f"unknown command {kind!r} (fix, cancel, not before, post now or post at)"
    pack = pid if kind in PACK_COMMANDS and not ids.parse_post_id(pid) and ids.parse_pack_id(pid) else None
    if not pack and not ids.parse_post_id(pid):
        return None, f"unknown post ID {pid!r}"
    date = (row.get("date") or "").strip()
    if kind == "not before" and not re.fullmatch(r"\d{4}-\d{2}-\d{2}(?:[ T]\d{2}:\d{2})?", date):
        return None, "not before needs a date (YYYY-MM-DD)"
    if kind == "post at" and not re.fullmatch(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}", date):
        return None, "post at needs a day and a time (YYYY-MM-DD HH:MM)"
    out = {"id": row.get("id"), "kind": kind, "post_id": None if pack else pid, "date": date}
    if pack:
        out["pack_id"] = pack
    return out, ""


# --- pack registry -------------------------------------------------------------------------

def parse_packs(md_text):
    t = mdtable.find(md_text, "pack_id", "status")
    return t["rows"] if t else []


def upsert_pack(md_text, row):
    """The registry text with `row` added, or merged into the row with the same pack_id."""
    t = mdtable.find(md_text, "pack_id", "status")
    if t is None:
        md_text = md_text.rstrip("\n") + "\n\n" + mdtable.render(PACK_COLS, []) + "\n"
        t = mdtable.find(md_text, "pack_id", "status")
    rows = t["rows"]
    for r in rows:
        if r.get("pack_id") == row["pack_id"]:
            r.update({k: v for k, v in row.items() if v is not None})
            break
    else:
        rows.append({c: row.get(c, "") for c in PACK_COLS})
    return mdtable.replace(md_text, t, rows)


def packs_of_source(rows, source_id):
    """Registry rows of an item or request (its packs, fix PRs and skips)."""
    return [r for r in rows if r.get("source") == source_id]


def main():
    if len(sys.argv) < 2 or sys.argv[1] != "ids":
        print(__doc__)
        return 2
    brand_key = sys.argv[2] if len(sys.argv) > 2 else "vsichkikazina"
    p = requests_path(brand_key)
    text, new = assign_ids(_read(p), brands.brand(brand_key)["prefix"])
    if new:
        p.write_text(text, encoding="utf-8")
    print("new ids: " + (", ".join(new) if new else "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
