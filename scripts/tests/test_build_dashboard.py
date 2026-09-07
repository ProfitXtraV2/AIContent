import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_dashboard as bd

SAMPLE = """# Content Queue
| id | status | type | query | keywords_or_terms | source | drafted_date | posted_date | folder | pr | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | drafted | review | Spin City | spin city | research | 2026-09-07 |  | 2026-09-07-spin-city | #1 |  |
| 2 | approved | guide | Wagering | wagering | backlog | 2026-09-06 |  | 2026-09-06-wagering | #2 |  |
| 3 | posted | news | Licence update | licence | research | 2026-09-01 | 2026-09-03 | 2026-09-01-licence | #3 |  |
| 4 | failed | review | Broken Casino | x | research | 2026-09-05 |  | 2026-09-05-broken | #4 | gate FAIL |
"""

BACKLOG_SAMPLE = """# Topic Backlog
| priority | type | query | keywords_or_terms | status | notes |
|---|---|---|---|---|---|
| 1 | guide | Wagering explainer | wagering | open | evergreen |
| 2 | comparison | Best bonuses | bonus | open |  |
"""

RESEARCH_SAMPLE = """# Research Topics Bank
| type | query | researched_keywords | source_rationale | status | date_researched |
|---|---|---|---|---|---|
| review | Palms Bet | palms bet казино | НАП register | candidate | 2026-09-07 |
"""

# Enriched (Ahrefs) layouts — 11 columns
RESEARCH_ENRICHED = """# Research Topics Bank
| type | query | researched_keywords | volume | kd | intent | trend | checked | suggestion | status | date_researched |
|---|---|---|---|---|---|---|---|---|---|---|
| guide | Как да четем RTP | rtp, връщане | 1300 | 8 | informational | up | ahrefs | strong: high vol, low KD | candidate | 2026-09-07 |
| guide | Волатилност слотове | волатилност | 90 | 55 | informational | flat | web | weak; try long-tail | candidate | 2026-09-07 |
"""

BACKLOG_ENRICHED = """# Topic Backlog
| priority | type | query | keywords_or_terms | volume | kd | intent | checked | ahrefs_note | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | guide | Wagering | wagering | 500 | 15 | informational | ahrefs | good pick | open | x |
"""


def test_parse_queue_row_count():
    rows = bd.parse_queue(SAMPLE)
    assert len(rows) == 4


def test_parse_queue_fields():
    rows = bd.parse_queue(SAMPLE)
    assert rows[0]["status"] == "drafted"
    assert rows[0]["type"] == "review"
    assert rows[0]["query"] == "Spin City"
    assert rows[0]["folder"] == "2026-09-07-spin-city"
    assert rows[0]["gemini"] == ""   # legacy 11-col rows get an empty gemini field


QUEUE_GEMINI = """# Content Queue
| id | status | type | query | keywords_or_terms | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | drafted | guide | Free games | free | research | 2026-09-07 |  | 2026-09-07-free | #4 | human 84 |  |
| 2 | drafted | guide | No deposit | nodep | research | 2026-09-07 |  | 2026-09-07-nodep | #5 | ai 68 |  |
| 3 | drafted | guide | Skipped one | x | research | 2026-09-07 |  | 2026-09-07-x | #6 | skipped |  |
"""


def test_parse_queue_gemini_column():
    rows = bd.parse_queue(QUEUE_GEMINI)
    assert rows[0]["gemini"] == "human 84"
    assert rows[1]["gemini"] == "ai 68"
    assert rows[2]["gemini"] == "skipped"


def test_parse_backlog():
    bl = bd.parse_backlog(BACKLOG_SAMPLE)
    assert len(bl) == 2
    assert bl[0]["priority"] == "1"
    assert bl[0]["query"] == "Wagering explainer"


def test_build_status_includes_backlog_and_articles_base():
    status = bd.build_status(bd.parse_queue(SAMPLE),
                             backlog=bd.parse_backlog(BACKLOG_SAMPLE), target=10)
    assert len(status["backlog"]) == 2
    assert status["articles_base_url"].endswith("/VsichkiKazina/articles/")


def test_parse_research_and_included_in_status():
    research = bd.parse_research(RESEARCH_SAMPLE)
    assert len(research) == 1
    assert research[0]["query"] == "Palms Bet"
    assert research[0]["researched_keywords"] == "palms bet казино"
    status = bd.build_status(bd.parse_queue(SAMPLE), research=research, target=10)
    assert len(status["research"]) == 1


def test_build_status_buffer_counts_drafted_and_approved():
    status = bd.build_status(bd.parse_queue(SAMPLE), target=10)
    assert status["buffer"]["count"] == 2      # drafted + approved
    assert status["buffer"]["target"] == 10
    assert status["buffer"]["deficit"] == 8


def test_build_status_status_breakdown():
    status = bd.build_status(bd.parse_queue(SAMPLE), target=10)
    assert status["counts"]["posted"] == 1
    assert status["counts"]["failed"] == 1


def test_build_status_is_json_serialisable():
    status = bd.build_status(bd.parse_queue(SAMPLE), target=10)
    json.dumps(status)  # must not raise


def test_build_status_includes_meta_schedule_and_links():
    status = bd.build_status(bd.parse_queue(SAMPLE), target=10)
    assert status["meta"]["schedule"]["cron_utc_hour"] == 4
    assert status["meta"]["links"]["repo"].startswith("https://github.com/")
    assert "routine" in status["meta"]["links"]


def test_opportunity_scoring():
    strong = bd.opportunity(1300, 8)      # high volume, low KD
    weak = bd.opportunity(90, 55)         # low volume, high KD
    assert strong["band"] == "Strong" and strong["score"] >= 70
    assert weak["band"] in ("Weak", "Moderate") and weak["score"] < strong["score"]
    assert bd.opportunity("", "") is None            # no data
    assert bd.opportunity("1,300", "8")["band"] == "Strong"  # comma/str tolerated


def test_parse_research_enriched_and_checked():
    r = bd.parse_research(RESEARCH_ENRICHED)
    assert len(r) == 2
    assert r[0]["volume"] == "1300" and r[0]["kd"] == "8"
    assert r[0]["checked"] == "ahrefs"
    assert r[1]["checked"] == "web"
    status = bd.build_status(bd.parse_queue(SAMPLE), research=r, target=10)
    assert status["research"][0]["opportunity"]["band"] == "Strong"


def test_parse_backlog_enriched_has_opportunity():
    bl = bd.parse_backlog(BACKLOG_ENRICHED)
    assert bl[0]["checked"] == "ahrefs" and bl[0]["volume"] == "500"
    status = bd.build_status(bd.parse_queue(SAMPLE), backlog=bl, target=10)
    assert status["backlog"][0]["opportunity"]["score"] >= 45  # good/strong


def test_legacy_rows_still_parse_with_empty_metrics():
    bl = bd.parse_backlog(BACKLOG_SAMPLE)     # legacy 6-col
    r = bd.parse_research(RESEARCH_SAMPLE)    # legacy 6-col
    assert bl[0]["volume"] == "" and bl[0]["checked"] == ""
    assert r[0]["volume"] == "" and r[0]["checked"] == ""
    status = bd.build_status(bd.parse_queue(SAMPLE), backlog=bl, research=r, target=10)
    assert status["backlog"][0]["opportunity"] is None
