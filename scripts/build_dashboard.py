#!/usr/bin/env python3
"""Build docs/data/status.json from VsichkiKazina/content-queue.md.

Deterministic, stdlib-only. Run from repo root:
    python3 scripts/build_dashboard.py
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

BUFFER_STATES = {"drafted", "approved"}
ALL_STATES = ["in-progress", "drafted", "approved", "posted", "failed"]
COLUMNS = ["id", "status", "type", "query", "keywords_or_terms",
           "source", "drafted_date", "posted_date", "pr", "notes"]


def parse_queue(md_text):
    """Parse the markdown table into a list of row dicts (data rows only)."""
    rows = []
    for line in md_text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != len(COLUMNS):
            continue
        if cells[0].lower() == "id":          # header row
            continue
        if set(cells[0]) <= set("-: "):        # separator row
            continue
        rows.append(dict(zip(COLUMNS, cells)))
    return rows


def build_status(rows, target=10):
    counts = {s: 0 for s in ALL_STATES}
    for r in rows:
        st = r.get("status", "").lower()
        if st in counts:
            counts[st] += 1
    buffer_count = counts["drafted"] + counts["approved"]
    return {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "buffer": {
            "count": buffer_count,
            "target": target,
            "deficit": max(0, target - buffer_count),
            "ok": buffer_count >= target,
        },
        "counts": counts,
        "rows": rows,
    }


def main():
    root = Path(__file__).resolve().parents[1]
    queue = root / "VsichkiKazina" / "content-queue.md"
    out = root / "docs" / "data" / "status.json"
    md = queue.read_text(encoding="utf-8") if queue.exists() else ""
    status = build_status(parse_queue(md), target=10)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out} — buffer {status['buffer']['count']}/{status['buffer']['target']}")


if __name__ == "__main__":
    sys.exit(main())
