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
           "source", "drafted_date", "posted_date", "folder", "pr", "notes"]
BACKLOG_COLUMNS = ["priority", "type", "query", "keywords_or_terms", "status", "notes"]
RESEARCH_COLUMNS = ["type", "query", "researched_keywords", "source_rationale",
                    "status", "date_researched"]


def _parse_table(md_text, columns):
    """Parse a markdown table with the given column order into row dicts."""
    rows = []
    for line in md_text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != len(columns):
            continue
        if cells[0].lower() == columns[0].lower():   # header row
            continue
        if set(cells[0]) <= set("-: "):               # separator row
            continue
        rows.append(dict(zip(columns, cells)))
    return rows

# Schedule: the daily cron fires at this UTC hour (04:00 UTC ≈ 07:00 Europe/Sofia).
SCHEDULE = {"cron_utc_hour": 4, "cron_utc_minute": 0,
            "label": "Daily · 07:00 Europe/Sofia"}

# Maintain all dashboard links in one place.
LINKS = {
    "site": "https://vsichkikazina.bg",
    "repo": "https://github.com/ProfitXtraV2/AIContent",
    "prs": "https://github.com/ProfitXtraV2/AIContent/pulls",
    "routine": "https://claude.ai/code/routines/trig_011f3su1Brcj5QHNCo4zqBEY",
    "backlog": "https://github.com/ProfitXtraV2/AIContent/blob/main/VsichkiKazina/topic-backlog.md",
    "queue": "https://github.com/ProfitXtraV2/AIContent/blob/main/VsichkiKazina/content-queue.md",
}


# Legacy 10-column queue (pre-`folder`). Parsed for backward compatibility.
COLUMNS_LEGACY = [c for c in COLUMNS if c != "folder"]


def parse_queue(md_text):
    """Parse the content-queue table, tolerating both the 11-column (with `folder`)
    and legacy 10-column layouts. Legacy rows get an empty `folder`."""
    rows = []
    for line in md_text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and cells[0].lower() == "id":          # header row
            continue
        if cells and set(cells[0]) <= set("-: "):         # separator row
            continue
        if len(cells) == len(COLUMNS):
            rows.append(dict(zip(COLUMNS, cells)))
        elif len(cells) == len(COLUMNS_LEGACY):
            row = dict(zip(COLUMNS_LEGACY, cells))
            row["folder"] = ""
            rows.append(row)
    return rows


def parse_backlog(md_text):
    """Parse the topic-backlog markdown table into row dicts (data rows only)."""
    return _parse_table(md_text, BACKLOG_COLUMNS)


def parse_research(md_text):
    """Parse the research-topics (AI backlog) markdown table into row dicts."""
    return _parse_table(md_text, RESEARCH_COLUMNS)


def build_status(rows, backlog=None, research=None, target=10):
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
        "backlog": backlog or [],
        "research": research or [],
        "articles_base_url": LINKS["repo"] + "/tree/main/VsichkiKazina/articles/",
        "meta": {
            "brand": "VsichkiKazina",
            "schedule": SCHEDULE,
            "links": LINKS,
        },
    }


def main():
    root = Path(__file__).resolve().parents[1]
    queue = root / "VsichkiKazina" / "content-queue.md"
    backlog_f = root / "VsichkiKazina" / "topic-backlog.md"
    research_f = root / "VsichkiKazina" / "research-topics.md"
    out = root / "docs" / "data" / "status.json"
    md = queue.read_text(encoding="utf-8") if queue.exists() else ""
    bl = backlog_f.read_text(encoding="utf-8") if backlog_f.exists() else ""
    rs = research_f.read_text(encoding="utf-8") if research_f.exists() else ""
    status = build_status(parse_queue(md), backlog=parse_backlog(bl),
                          research=parse_research(rs), target=10)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out} — buffer {status['buffer']['count']}/{status['buffer']['target']}")


if __name__ == "__main__":
    sys.exit(main())
