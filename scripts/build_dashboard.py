#!/usr/bin/env python3
"""Build per-brand status.json (VsichkiKazina, DentalVia) from each brand's content-queue.md.

Brand-aware, deterministic, stdlib-only. Run from repo root:
    python3 scripts/build_dashboard.py [brand]
where brand ∈ vsichkikazina (default) | dentalvia.
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Winnability gate: a keyword whose KD is above our current domain authority is a
# future *pillar* target, not a next-write candidate. Set roughly to DR + a small
# buffer; raise as the domain's authority grows. DR 6 → 40.
SITE_MAX_WINNABLE_KD = int(os.getenv("SITE_MAX_WINNABLE_KD", "40"))

BUFFER_STATES = {"drafted", "approved"}
ALL_STATES = ["in-progress", "drafted", "approved", "posted", "failed"]

COLUMNS = ["id", "status", "type", "query", "keywords_or_terms", "volume", "kd",
           "source", "drafted_date", "posted_date", "folder", "pr", "gemini", "notes"]
COLUMNS_L12 = [c for c in COLUMNS if c not in ("volume", "kd")]                # gemini, no vol/kd
COLUMNS_L11 = [c for c in COLUMNS if c not in ("volume", "kd", "gemini")]      # folder, no gemini
COLUMNS_L10 = [c for c in COLUMNS if c not in ("volume", "kd", "gemini", "folder")]  # oldest

# DentalVia 15-col layout: same as COLUMNS but with "byline" after "type"
COLUMNS_DV = COLUMNS[:3] + ["byline"] + COLUMNS[3:]

BRANDS = {
    "vsichkikazina": {"dir": "VsichkiKazina", "brand": "VsichkiKazina",
                      "out": ("docs", "data", "status.json"),
                      "links": {"site": "https://vsichkikazina.bg",
                                "routine": "https://claude.ai/code/routines/trig_019cfW1QpXykZkwG8XrotCtQ"}},
    "dentalvia":     {"dir": "DentalVia", "brand": "DentalVia",
                      "out": ("docs", "data", "dentalvia", "status.json"),
                      "links": {"site": "https://www.dentalvia.de"}},
}

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
    winnable = k <= SITE_MAX_WINNABLE_KD
    band = ("Strong" if score >= 70 else "Good" if score >= 45
            else "Moderate" if score >= 25 else "Weak")
    # Demote high-value heads that sit above our current reach to a 'Pillar'
    # band so descending-opportunity selection cannot pick them over winnable
    # satellites. They stay visible as tracked future targets; graduate them
    # by raising SITE_MAX_WINNABLE_KD as domain authority grows.
    if not winnable and band in ("Strong", "Good"):
        band = "Pillar"
    return {"score": score, "band": band, "winnable": winnable}

# Schedule: cron fires 3×/day at these UTC hours (22:00/03:00/07:00 UTC ≈ 01:00/06:00/10:00
# Europe/Sofia in summer; drifts −1h in winter since cron is fixed-UTC).
SCHEDULE = {"cron_utc_hours": [7],
            "label": "once daily · ~10:13 Europe/Sofia (throttled 2026-10-04)"}

# Maintain all dashboard links in one place.
LINKS = {
    "site": "https://vsichkikazina.bg",
    "repo": "https://github.com/ProfitXtraV2/AIContent",
    "prs": "https://github.com/ProfitXtraV2/AIContent/pulls",
    "routine": "https://claude.ai/code/routines/trig_019cfW1QpXykZkwG8XrotCtQ",
    "backlog": "https://github.com/ProfitXtraV2/AIContent/blob/main/VsichkiKazina/topic-backlog.md",
    "queue": "https://github.com/ProfitXtraV2/AIContent/blob/main/VsichkiKazina/content-queue.md",
}


def parse_queue(md_text, brand="vsichkikazina"):
    """Parse the content-queue table.

    brand="vsichkikazina" (default): 14-col with vol/kd, or 12/11/10-col legacy.
    brand="dentalvia": 15-col with byline after type.
    """
    if brand == "dentalvia":
        return _parse_tolerant(md_text, [COLUMNS_DV])
    return _parse_tolerant(md_text, [COLUMNS, COLUMNS_L12, COLUMNS_L11, COLUMNS_L10])


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


def build_status(rows, backlog=None, research=None, target=10, brand="vsichkikazina"):
    brand_cfg = BRANDS[brand]
    counts = {s: 0 for s in ALL_STATES}
    for r in rows:
        st = r.get("status", "").lower()
        if st in counts:
            counts[st] += 1
    buffer_count = counts["drafted"] + counts["approved"]
    rows = _with_opportunity(rows)          # articles carry their target keyword's vol/kd
    backlog = _with_opportunity(backlog or [])
    research = _with_opportunity(research or [])
    repo = LINKS["repo"]
    brand_dir = brand_cfg["dir"]
    # Build per-brand links: start from shared keys, apply brand-specific overrides
    # (site, routine), then compute dynamic backlog/queue URLs for this brand.
    brand_link_overrides = brand_cfg["links"]
    links = {
        "repo": repo,
        "prs": LINKS["prs"],
        **brand_link_overrides,
        "backlog": f"{repo}/blob/main/{brand_dir}/topic-backlog.md",
        "queue": f"{repo}/blob/main/{brand_dir}/content-queue.md",
    }
    if brand == "dentalvia":
        schedule_meta = {"note": "manual runs only — not scheduled"}
    else:
        schedule_meta = SCHEDULE
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
        "articles_base_url": repo + f"/tree/main/{brand_dir}/articles/",
        "meta": {
            "brand": brand_cfg["brand"],
            "schedule": schedule_meta,
            "links": links,
        },
    }


# Unresolved fact-check flags left in a final draft for the human reviewer:
# `[VERIFY]`, `[VERIFY: what to check]`, `[DATA NEEDED: …]`.
VERIFY_FLAG_RE = re.compile(r"\[(?:VERIFY|DATA NEEDED)\b[^\]\n]*\]")


def verify_flags(text):
    """Return the [VERIFY…]/[DATA NEEDED…] flags found in a draft, in order."""
    return VERIFY_FLAG_RE.findall(text or "")


def _read_final_draft(root, brand_dir, row):
    """Text of a row's 05b-final-draft.md, or None if it can't be found. Unposted
    articles live only on their PR branch (content/<folder>), so read via git;
    posted ones (and local runs) fall back to the working tree."""
    folder = (row.get("folder") or "").strip()
    if not folder:
        return None
    rel = f"{brand_dir}/articles/{folder}/05b-final-draft.md"
    for ref in (f"origin/content/{folder}", f"content/{folder}"):
        try:
            res = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=root,
                                 capture_output=True, timeout=10)
        except (OSError, subprocess.SubprocessError):
            break
        if res.returncode == 0:
            return res.stdout.decode("utf-8", "replace")
    local = Path(root) / rel
    return local.read_text(encoding="utf-8") if local.exists() else None


def attach_verify_flags(rows, read_draft):
    """Set row['verify_flags'] (count, None = draft not found) and row['verify_samples']
    (first few flags, for the dashboard tooltip) on every article row."""
    for r in rows:
        text = read_draft(r)
        flags = verify_flags(text) if text is not None else []
        r["verify_flags"] = len(flags) if text is not None else None
        r["verify_samples"] = [f[:160] for f in flags[:5]]
    return rows


def _cluster_of(row):
    """Extract a `cluster: <tag>` marker from a backlog note / research suggestion."""
    text = f"{row.get('notes', '')} {row.get('suggestion', '')} {row.get('ahrefs_note', '')}"
    m = re.search(r"cluster:\s*([a-z0-9-]+)", text or "")
    return m.group(1) if m else "uncategorised"


def build_seo(backlog, research, seo_review):
    """SEO panel data for the dashboard: DR trend, opportunity-band mix, cluster
    breakdown, winnable-now candidates, and deferred Pillar targets. Built from the
    (opportunity-tagged) backlog + research rows plus docs/data/seo-review.json."""
    CONSUMED = {"used", "written", "posted", "approved"}
    bands, clusters, winnable, pillars = {}, {}, [], []
    for src, rows in (("backlog", backlog or []), ("research", research or [])):
        for r in rows:
            opp = r.get("opportunity")
            st = (r.get("status") or "open").lower()
            if not opp or st in CONSUMED:
                continue
            band = opp["band"]
            bands[band] = bands.get(band, 0) + 1
            cl = _cluster_of(r)
            item = {
                "query": r.get("query", ""),
                "keywords": r.get("keywords_or_terms") or r.get("researched_keywords") or "",
                "volume": r.get("volume"), "kd": r.get("kd"),
                "intent": r.get("intent", ""), "band": band, "score": opp["score"],
                "winnable": opp.get("winnable"), "cluster": cl, "status": st, "src": src,
            }
            c = clusters.setdefault(cl, {"winnable": 0, "pillar": 0, "total": 0})
            c["total"] += 1
            if band == "Pillar":
                pillars.append(item); c["pillar"] += 1
            elif opp.get("winnable"):
                winnable.append(item); c["winnable"] += 1
    winnable.sort(key=lambda x: -(x["score"] or 0))
    pillars.sort(key=lambda x: -((x["volume"] or 0)))
    return {
        "max_winnable_kd": seo_review.get("max_winnable_kd", SITE_MAX_WINNABLE_KD),
        "last_monthly_review": seo_review.get("last_monthly_review"),
        "trend": seo_review.get("trend", []),
        "bands": bands,
        "clusters": clusters,
        "winnable": winnable,
        "pillars": pillars,
        "tracking": seo_review.get("tracking", []),
        "counts": {"winnable": len(winnable), "pillars": len(pillars)},
    }


def main():
    brand = sys.argv[1].lower() if len(sys.argv) > 1 else "vsichkikazina"
    if brand not in BRANDS:
        sys.exit(f"unknown brand {brand!r} — must be one of: {', '.join(BRANDS)}")
    brand_cfg = BRANDS[brand]
    root = Path(__file__).resolve().parents[1]
    brand_dir = brand_cfg["dir"]
    queue = root / brand_dir / "content-queue.md"
    backlog_f = root / brand_dir / "topic-backlog.md"
    research_f = root / brand_dir / "research-topics.md"
    out = root.joinpath(*brand_cfg["out"])
    md = queue.read_text(encoding="utf-8") if queue.exists() else ""
    bl = backlog_f.read_text(encoding="utf-8") if backlog_f.exists() else ""
    rs = research_f.read_text(encoding="utf-8") if research_f.exists() else ""
    status = build_status(parse_queue(md, brand=brand), backlog=parse_backlog(bl),
                          research=parse_research(rs), target=10, brand=brand)
    attach_verify_flags(status["rows"], lambda r: _read_final_draft(root, brand_dir, r))
    if brand == "vsichkikazina":
        sr_f = root / "docs" / "data" / "seo-review.json"
        seo_review = json.loads(sr_f.read_text(encoding="utf-8")) if sr_f.exists() else {}
        status["seo"] = build_seo(status["backlog"], status["research"], seo_review)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out} — buffer {status['buffer']['count']}/{status['buffer']['target']}")


if __name__ == "__main__":
    sys.exit(main())
