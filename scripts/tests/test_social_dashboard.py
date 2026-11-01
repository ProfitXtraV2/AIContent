"""The social tabs of the dashboards (product spec G1–G4; tech spec flow 12)."""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from social import board, build_social_dashboard as dash  # noqa: E402
from test_social_check import u, world  # noqa: E402

DOCS = Path(__file__).resolve().parents[2] / "docs"
JS = DOCS / "social-tabs.js"


def test_every_page_with_the_tabs_carries_noindex():
    """G4: the page itself says noindex; robots.txt is not relied on."""
    pages = [p for p in DOCS.rglob("*.html") if "social-tabs.js" in p.read_text(encoding="utf-8")]
    assert sorted(p.relative_to(DOCS).as_posix() for p in pages) == ["dentalvia/index.html", "index.html"]
    for p in pages:
        head = p.read_text(encoding="utf-8").split("</head>")[0]
        assert re.search(r'<meta name="robots" content="noindex[^"]*">', head), p


def test_both_pages_wire_the_two_tabs():
    for rel, brand, base in (("index.html", "vsichkikazina", "./data/social"),
                             ("dentalvia/index.html", "dentalvia", "../data/social")):
        text = (DOCS / rel).read_text(encoding="utf-8")
        assert f"SocialTabs.load('{brand}'" in text and f"'{base}'" in text
        for key in ("social-review", "social-schedule", "social-requests", "social-settings"):
            assert f"label: SocialTabs.tabLabel('{key}')" in text           # the tab names follow БГ · EN


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_tabs_script_parses():
    assert subprocess.run(["node", "--check", str(JS)], capture_output=True).returncode == 0


def test_the_script_reads_only_fields_the_data_has(tmp_path):
    """Every row field social-tabs.js reads (r.<field>) is written by build_social_dashboard."""
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))
    w.check(u("2026-11-04 08:10"))
    p = board.packs_path("vsichkikazina", tmp_path)
    p.write_text(board.upsert_pack(p.read_text(encoding="utf-8"), {
        "pack_id": "vk-0302-p1", "source": "vk-0302", "title": "Блекджек", "pr": "#312", "branch": "social/vk/vk-0302-p1",
        "status": "open", "posts": "3", "created": "2026-11-01"}), encoding="utf-8")
    review, schedule = dash.build(tmp_path, "vsichkikazina", u("2026-11-04 08:30"))
    have = set(review["rows"][0]) | set(schedule["rows"][0]) | {"labels"}     # labels come from the live PR list
    used = set(re.findall(r"\br\.(\w+)", JS.read_text(encoding="utf-8")))
    assert used <= have, used - have
    assert set(schedule["counters"]) == {"in_review", "in_review_posts", "scheduled_next_7_days",
                                         "published_this_month", "failed"}
    assert {"generated_utc", "last_check_utc", "banners", "brand_state", "time_zone", "image_spend"} <= set(schedule)
    assert {"failed_requests", "skipped"} <= set(review)


def test_reasons_read_plainly():
    assert dash.reason_text("held:live_page_differs") == "live page differs"
    assert dash.reason_text("waiting:not deployed yet (board not posted, not in the publisher's record)") == \
        "not deployed yet (board not posted, not in the publisher's record)"
    assert dash.reason_text("failed:(#200) Requires pages_manage_posts permission") == \
        "(#200) Requires pages_manage_posts permission"
    assert dash.reason_text("needs_fix:text_differs_from_approved") == "text differs from approved"


def test_schedule_rows_show_local_time_and_held_lines(tmp_path):
    w = world(tmp_path)
    w.check(u("2026-11-04 07:10"))
    w.pages["https://vsichkikazina.bg/blog/ruletka-shansove/"] = (404, "")
    w.check(u("2026-11-04 08:10"))
    data = json.loads((tmp_path / "docs" / "data" / "social" / "vsichkikazina-schedule.json").read_text(encoding="utf-8"))
    rows = {r["post_id"]: r for r in data["rows"]}
    assert rows["vk-0300-p1-fb-1"]["badge"] == "Held" and rows["vk-0300-p1-fb-1"]["reason_text"] == "no live link"
    assert data["time_zone"] == "Europe/Sofia" and data["last_check_utc"] == "2026-11-04T08:10:00Z"
