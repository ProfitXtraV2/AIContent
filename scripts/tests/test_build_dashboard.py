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


def test_parse_queue_row_count():
    rows = bd.parse_queue(SAMPLE)
    assert len(rows) == 4


def test_parse_queue_fields():
    rows = bd.parse_queue(SAMPLE)
    assert rows[0]["status"] == "drafted"
    assert rows[0]["type"] == "review"
    assert rows[0]["query"] == "Spin City"
    assert rows[0]["folder"] == "2026-09-07-spin-city"


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
