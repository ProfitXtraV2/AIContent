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


def test_main_accepts_queue_option(tmp_path, monkeypatch, capsys):
    q = tmp_path / "queue.md"
    q.write_text(QUEUE, encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["mark_approved.py", "--queue", str(q), "2026-09-07-a"])
    ma.main()
    assert "| approved | guide | A |" in q.read_text(encoding="utf-8")
