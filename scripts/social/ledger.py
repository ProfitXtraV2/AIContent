"""The publishing check's own record (tech spec, Data model: "Post ledger record" and "Other
guest tables").

SQLite in the guest is the authoritative copy (/var/lib/px-social/state.sqlite). After each run
the check exports it to the repository: <Brand>/social/ledger.json (one record per post, the
banners and the brand's switches) and <Brand>/social/audit/<YYYY-MM>.jsonl (the audit trail).

    posts(post_id, brand, pack_id, state, data)          one record per post; data is its JSON
    audit(id, utc, brand, post_id, event, actor, data)   append only (I3)
    prs_seen(pr, brand, head_ref, merged_by, merged_at, merge_sha, closed_utc)
    settings_versions(id, brand, accepted_sha, file_sha256, merged_by, accepted_utc, text)
    control_events(comment_id, brand, command, author, permission, accepted, utc, note)
    brand_switches(brand, settings_pause, stop_now, tool_pause, since_utc, data)
    commands_seen(command_id, brand, utc, result)
    runs(id, utc_start, utc_end, kind, result)           the heartbeat (23 runs a day guardrail)
    kv(key, value)                                       last check time, banners, scan position
"""
import json
import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS posts (post_id TEXT PRIMARY KEY, brand TEXT NOT NULL, pack_id TEXT,
    state TEXT NOT NULL, data TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS posts_brand_state ON posts (brand, state);
CREATE TABLE IF NOT EXISTS audit (id INTEGER PRIMARY KEY AUTOINCREMENT, utc TEXT NOT NULL, brand TEXT,
    post_id TEXT, event TEXT NOT NULL, actor TEXT NOT NULL, data TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS prs_seen (pr INTEGER PRIMARY KEY, brand TEXT, head_ref TEXT, merged_by TEXT,
    merged_at TEXT, merge_sha TEXT, closed_utc TEXT);
CREATE TABLE IF NOT EXISTS settings_versions (id INTEGER PRIMARY KEY AUTOINCREMENT, brand TEXT NOT NULL,
    accepted_sha TEXT, file_sha256 TEXT NOT NULL, merged_by TEXT, accepted_utc TEXT, text TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS control_events (comment_id INTEGER PRIMARY KEY, brand TEXT, command TEXT,
    author TEXT, permission TEXT, accepted INTEGER, utc TEXT, note TEXT);
CREATE TABLE IF NOT EXISTS brand_switches (brand TEXT PRIMARY KEY, settings_pause INTEGER DEFAULT 0,
    stop_now INTEGER DEFAULT 0, tool_pause INTEGER DEFAULT 0, since_utc TEXT, data TEXT DEFAULT '{}');
CREATE TABLE IF NOT EXISTS commands_seen (command_id TEXT PRIMARY KEY, brand TEXT, utc TEXT, result TEXT);
CREATE TABLE IF NOT EXISTS runs (id INTEGER PRIMARY KEY AUTOINCREMENT, utc_start TEXT, utc_end TEXT,
    kind TEXT, result TEXT);
CREATE TABLE IF NOT EXISTS kv (key TEXT PRIMARY KEY, value TEXT);
"""

# What ledger.json shows of a post. Texts, payloads and check results stay in the audit trail.
EXPORT_FIELDS = ["post_id", "pack_id", "brand", "account_id", "network", "role", "source", "title", "state",
                 "reason", "missing_lines", "markers", "approval", "fix_pr", "matched_version", "went_live_utc",
                 "eligible_utc", "earliest_utc", "not_before_utc", "planned_slot_utc", "handover", "published_utc",
                 "network_url", "article_url", "retries"]
HANDOVER_EXPORT = ["utc", "slot_utc", "payload_hash", "postiz_post_id", "postiz_group", "dry_run"]
APPROVAL_EXPORT = ["pr", "merge_sha", "merged_by", "merged_at", "approved_files_sha256"]


class Ledger:
    def __init__(self, path=":memory:"):
        if path != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(path))
        self.db.executescript(SCHEMA)
        self.db.commit()

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.commit()
        self.db.close()

    # posts
    def post(self, post_id):
        row = self.db.execute("SELECT data FROM posts WHERE post_id = ?", (post_id,)).fetchone()
        return json.loads(row[0]) if row else None

    def posts(self, brand=None, states=None):
        q, args = "SELECT data FROM posts", []
        where = []
        if brand:
            where.append("brand = ?")
            args.append(brand)
        if states:
            where.append("state IN (%s)" % ",".join("?" * len(states)))
            args += list(states)
        if where:
            q += " WHERE " + " AND ".join(where)
        return [json.loads(r[0]) for r in self.db.execute(q + " ORDER BY post_id", args)]

    def save(self, rec):
        self.db.execute("INSERT INTO posts (post_id, brand, pack_id, state, data) VALUES (?, ?, ?, ?, ?) "
                        "ON CONFLICT(post_id) DO UPDATE SET brand = excluded.brand, pack_id = excluded.pack_id, "
                        "state = excluded.state, data = excluded.data",
                        (rec["post_id"], rec["brand"], rec.get("pack_id"), rec["state"],
                         json.dumps(rec, ensure_ascii=False, sort_keys=True)))

    # audit
    def audit(self, utc, brand, post_id, event, actor="publishing-check", **data):
        self.db.execute("INSERT INTO audit (utc, brand, post_id, event, actor, data) VALUES (?, ?, ?, ?, ?, ?)",
                        (utc, brand, post_id, event, actor, json.dumps(data, ensure_ascii=False, sort_keys=True)))

    def audit_rows(self, brand=None, post_id=None, since_id=0):
        q, args = "SELECT id, utc, brand, post_id, event, actor, data FROM audit WHERE id > ?", [since_id]
        if brand:
            q += " AND brand = ?"
            args.append(brand)
        if post_id:
            q += " AND post_id = ?"
            args.append(post_id)
        return [{"id": r[0], "utc": r[1], "brand": r[2], "post_id": r[3], "event": r[4], "actor": r[5],
                 **json.loads(r[6])} for r in self.db.execute(q + " ORDER BY id", args)]

    # PRs already processed (boundary 3)
    def pr_seen(self, number):
        return self.db.execute("SELECT 1 FROM prs_seen WHERE pr = ?", (int(number),)).fetchone() is not None

    def mark_pr(self, number, brand, head_ref, merged_by, merged_at, merge_sha, closed_utc):
        self.db.execute("INSERT OR REPLACE INTO prs_seen VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (int(number), brand, head_ref, merged_by, merged_at, merge_sha, closed_utc))

    # settings accepted from merges by the team (write access; boundary 4)
    def accepted_settings(self, brand):
        row = self.db.execute("SELECT accepted_sha, file_sha256, merged_by, accepted_utc, text FROM settings_versions "
                              "WHERE brand = ? ORDER BY id DESC LIMIT 1", (brand,)).fetchone()
        return dict(zip(("accepted_sha", "file_sha256", "merged_by", "accepted_utc", "text"), row)) if row else None

    def accept_settings(self, brand, accepted_sha, file_sha256, merged_by, utc, text):
        self.db.execute("INSERT INTO settings_versions (brand, accepted_sha, file_sha256, merged_by, accepted_utc, text) "
                        "VALUES (?, ?, ?, ?, ?, ?)", (brand, accepted_sha, file_sha256, merged_by, utc, text))

    # control loop (flow 7)
    def control_seen(self, comment_id):
        return self.db.execute("SELECT 1 FROM control_events WHERE comment_id = ?", (int(comment_id),)).fetchone() is not None

    def control_event(self, comment_id, brand, command, author, permission, accepted, utc, note=""):
        self.db.execute("INSERT OR IGNORE INTO control_events VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (int(comment_id), brand, command, author, permission, 1 if accepted else 0, utc, note))

    def control_events(self, brand=None):
        q = "SELECT comment_id, brand, command, author, permission, accepted, utc, note FROM control_events"
        rows = self.db.execute(q + (" WHERE brand = ?" if brand else "") + " ORDER BY utc, comment_id",
                               (brand,) if brand else ()).fetchall()
        return [dict(zip(("comment_id", "brand", "command", "author", "permission", "accepted", "utc", "note"), r))
                for r in rows]

    def switches(self, brand):
        row = self.db.execute("SELECT settings_pause, stop_now, tool_pause, since_utc, data FROM brand_switches "
                              "WHERE brand = ?", (brand,)).fetchone()
        if not row:
            return {"settings_pause": False, "stop_now": False, "tool_pause": False, "since_utc": None, "data": {}}
        return {"settings_pause": bool(row[0]), "stop_now": bool(row[1]), "tool_pause": bool(row[2]),
                "since_utc": row[3], "data": json.loads(row[4] or "{}")}

    def set_switches(self, brand, utc, **changes):
        sw = self.switches(brand)
        before = {k: sw[k] for k in ("settings_pause", "stop_now", "tool_pause")}
        for k, v in changes.items():
            sw[k] = v
        after = {k: sw[k] for k in ("settings_pause", "stop_now", "tool_pause")}
        if before != after:
            sw["since_utc"] = utc
        self.db.execute("INSERT OR REPLACE INTO brand_switches VALUES (?, ?, ?, ?, ?, ?)",
                        (brand, int(sw["settings_pause"]), int(sw["stop_now"]), int(sw["tool_pause"]), sw["since_utc"],
                         json.dumps(sw.get("data") or {}, ensure_ascii=False)))
        return before != after

    # commands of the request list (F6)
    def command_seen(self, command_id):
        return self.db.execute("SELECT 1 FROM commands_seen WHERE command_id = ?", (command_id,)).fetchone() is not None

    def mark_command(self, command_id, brand, utc, result):
        self.db.execute("INSERT OR REPLACE INTO commands_seen VALUES (?, ?, ?, ?)", (command_id, brand, utc, result))

    # heartbeat
    def run_start(self, kind, utc):
        cur = self.db.execute("INSERT INTO runs (utc_start, kind) VALUES (?, ?)", (utc, kind))
        self.db.commit()
        return cur.lastrowid

    def run_end(self, run_id, utc, result):
        self.db.execute("UPDATE runs SET utc_end = ?, result = ? WHERE id = ?", (utc, result, run_id))
        self.db.commit()

    def runs(self, kind=None, since=None):
        q, args = "SELECT utc_start, utc_end, kind, result FROM runs WHERE 1 = 1", []
        if kind:
            q += " AND kind = ?"
            args.append(kind)
        if since:
            q += " AND utc_start >= ?"
            args.append(since)
        return [dict(zip(("utc_start", "utc_end", "kind", "result"), r)) for r in self.db.execute(q + " ORDER BY id", args)]

    def last_run(self, kind, result=None):
        q = "SELECT utc_start, utc_end, result FROM runs WHERE kind = ? AND utc_end IS NOT NULL"
        args = [kind]
        if result:
            q += " AND result = ?"
            args.append(result)
        row = self.db.execute(q + " ORDER BY id DESC LIMIT 1", args).fetchone()
        return dict(zip(("utc_start", "utc_end", "result"), row)) if row else None

    # small values
    def get(self, key, default=None):
        row = self.db.execute("SELECT value FROM kv WHERE key = ?", (key,)).fetchone()
        return json.loads(row[0]) if row else default

    def set(self, key, value):
        self.db.execute("INSERT OR REPLACE INTO kv VALUES (?, ?)", (key, json.dumps(value, ensure_ascii=False)))


def public(rec):
    """A post record as ledger.json shows it."""
    out = {k: rec[k] for k in EXPORT_FIELDS if rec.get(k) not in (None, "", [], {})}
    if rec.get("handover"):
        out["handover"] = {k: rec["handover"][k] for k in HANDOVER_EXPORT if rec["handover"].get(k) not in (None, "")}
    if rec.get("approval"):
        out["approval"] = {k: rec["approval"][k] for k in APPROVAL_EXPORT if rec["approval"].get(k) not in (None, "")}
    out.setdefault("markers", [])
    return out


def export(ledger, brand_key, social_dir, now_iso, banners, brand_state):
    """Write ledger.json and append the new audit rows to their month files. Returns (paths
    written, id of the last audit row exported). The caller records that id only once the
    files reached main, so a failed push loses no audit row."""
    social_dir = Path(social_dir)
    social_dir.mkdir(parents=True, exist_ok=True)
    data = {"exported_utc": now_iso, "last_check_utc": now_iso, "brand": brand_key,
            "posts": [public(r) for r in ledger.posts(brand=brand_key)], "banners": banners,
            "brand_state": brand_state}
    written = []
    f = social_dir / "ledger.json"
    f.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    written.append(f)
    done = ledger.get(f"audit_exported:{brand_key}", 0)
    rows = ledger.audit_rows(brand=brand_key, since_id=done)
    for month in sorted({r["utc"][:7] for r in rows}):
        out = social_dir / "audit" / f"{month}.jsonl"
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("a", encoding="utf-8", newline="\n") as fh:
            for r in rows:
                if r["utc"][:7] == month:
                    fh.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
        written.append(out)
    return written, (rows[-1]["id"] if rows else None)
