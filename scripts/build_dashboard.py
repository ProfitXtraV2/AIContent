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
           "source", "drafted_date", "posted_date", "folder", "pr", "gemini", "notes"]
COLUMNS_L11 = [c for c in COLUMNS if c != "gemini"]                  # folder, no gemini
COLUMNS_L10 = [c for c in COLUMNS if c not in ("gemini", "folder")]  # oldest 10-col

# Human backlog. Ahrefs metrics (volume/kd/intent/checked/ahrefs_note) are enriched by the
# run; the human only fills priority/type/query/keywords/status/notes (legacy 6-col parses).
# `checked` ∈ ahrefs | web | none — how the metrics were obtained (web = Ahrefs-unavailable fallback).
BACKLOG_COLUMNS = ["priority", "type", "query", "keywords_or_terms",
                   "volume", "kd", "intent", "checked", "ahrefs_note", "status", "notes"]
BACKLOG_COLUMNS_LEGACY = ["priority", "type", "query", "keywords_or_terms", "status", "notes"]

# AI research bank. Ahrefs-driven metrics + a suggestion. Legacy 6-col still parses.
# `checked` ∈ ahrefs | web | none.
RESEARCH_COLUMNS = ["type", "query", "researched_keywords", "volume", "kd", "intent",
                    "trend", "checked", "suggestion", "status", "date_researched"]
RESEARCH_COLUMNS_LEGACY = ["type", "query", "researched_keywords", "source_rationale",
                           "status", "date_researched"]


def _parse_tolerant(md_text, specs):
    """Parse a markdown table, matching each data row to whichever column spec has the
    same cell count (specs[0] is the richest/current layout). Missing richer fields are
    filled empty so downstream code can rely on every key existing."""
    by_len = {len(c): c for c in specs}
    richest = specs[0]
    rows = []
    for line in md_text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        cols = by_len.get(len(cells))
        if not cols:
            continue
        if cells[0].lower() == cols[0].lower():        # header row
            continue
        if set(cells[0]) <= set("-: "):                 # separator row
            continue
        row = dict(zip(cols, cells))
        for c in richest:
            row.setdefault(c, "")
        rows.append(row)
    return rows


def _num(v):
    """Parse a numeric cell ('1,300', ' 42 ') to float, or None."""
    try:
        return float(str(v).replace(",", "").replace("%", "").strip())
    except (ValueError, AttributeError):
        return None


def opportunity(volume, kd):
    """Deterministic 0-100 opportunity score from search volume + keyword difficulty,
    plus a band. Higher volume and lower KD score better. None if data missing."""
    v, k = _num(volume), _num(kd)
    if v is None or k is None:
        return None
    vol_score = min(60.0, v / 20.0)          # 1200+ volume saturates at 60
    kd_score = max(0.0, 40.0 - k * 0.4)      # KD 0 → 40, KD 100 → 0
    score = int(round(vol_score + kd_score))
    band = ("Strong" if score >= 70 else "Good" if score >= 45
            else "Moderate" if score >= 25 else "Weak")
    return {"score": score, "band": band}

# Schedule: the daily cron fires at this UTC hour (04:00 UTC ≈ 07:00 Europe/Sofia).
SCHEDULE = {"cron_utc_hour": 4, "cron_utc_minute": 0,
            "label": "Daily · 07:00 Europe/Sofia"}

# Maintain all dashboard links in one place.
LINKS = {
    "site": "https://vsichkikazina.bg",
    "repo": "https://github.com/ProfitXtraV2/AIContent",
    "prs": "https://github.com/ProfitXtraV2/AIContent/pulls",
    "routine": "https://claude.ai/code/routines",
    "backlog": "https://github.com/ProfitXtraV2/AIContent/blob/main/VsichkiKazina/topic-backlog.md",
    "queue": "https://github.com/ProfitXtraV2/AIContent/blob/main/VsichkiKazina/content-queue.md",
}


def parse_queue(md_text):
    """Parse the content-queue table (12-col with `gemini`, 11-col with `folder`, or 10-col)."""
    return _parse_tolerant(md_text, [COLUMNS, COLUMNS_L11, COLUMNS_L10])


def parse_backlog(md_text):
    """Parse the topic-backlog table (enriched 11-col, or legacy human 6-col)."""
    return _parse_tolerant(md_text, [BACKLOG_COLUMNS, BACKLOG_COLUMNS_LEGACY])


def parse_research(md_text):
    """Parse the research-topics table (enriched 11-col, or legacy 6-col)."""
    return _parse_tolerant(md_text, [RESEARCH_COLUMNS, RESEARCH_COLUMNS_LEGACY])


def _with_opportunity(rows):
    """Attach a computed opportunity {score, band} to each row from volume + kd."""
    for r in rows:
        r["opportunity"] = opportunity(r.get("volume"), r.get("kd"))
    return rows


def build_status(rows, backlog=None, research=None, target=10):
    counts = {s: 0 for s in ALL_STATES}
    for r in rows:
        st = r.get("status", "").lower()
        if st in counts:
            counts[st] += 1
    buffer_count = counts["drafted"] + counts["approved"]
    backlog = _with_opportunity(backlog or [])
    research = _with_opportunity(research or [])
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
