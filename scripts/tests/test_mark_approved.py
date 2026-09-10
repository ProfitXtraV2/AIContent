import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import mark_approved as ma

QUEUE = """# Content Queue
| id | status | type | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | drafted | guide | A | a | 100 | 10 | research | 2026-09-07 |  | 2026-09-07-a | #1 | human 85 |  |
| 2 | posted | guide | B | b | 200 | 20 | research | 2026-09-06 | 2026-09-08 | 2026-09-06-b | #2 | human 90 |  |
"""

def test_marks_drafted_folder_approved():
    out, upd = ma.mark_approved(QUEUE, {"2026-09-07-a"})
    assert upd == ["2026-09-07-a"]
    assert "| approved | guide | A |" in out

def test_ignores_non_drafted_and_unknown():
    out, upd = ma.mark_approved(QUEUE, {"2026-09-06-b", "nope"})
    assert upd == [] and out == QUEUE

DV_QUEUE = """# Content Queue — DentalVia
| id | status | type | byline | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| dv-0001 | drafted | comparison | Georgi Todorov | Veneers-Kosten 2026 | veneers kosten | 7500 | 30 | backlog | 2026-09-11 |  | 2026-09-11-veneers-kosten | #48 | human 85 |  |
"""

def test_dv_queue_row_marked_approved():
    new_md, updated = ma.mark_approved(DV_QUEUE, {"2026-09-11-veneers-kosten"})
    assert updated == ["2026-09-11-veneers-kosten"]
    assert "| approved |" in new_md and "| drafted |" not in new_md

def test_main_resolves_brand_queue_path(tmp_path, monkeypatch):
    (tmp_path / "DentalVia").mkdir()
    q = tmp_path / "DentalVia" / "content-queue.md"
    q.write_text(DV_QUEUE, encoding="utf-8")
    monkeypatch.setattr(ma, "repo_root", lambda: tmp_path)
    ma.main(["2026-09-11-veneers-kosten", "--brand", "dentalvia"])
    assert "| approved |" in q.read_text(encoding="utf-8")
