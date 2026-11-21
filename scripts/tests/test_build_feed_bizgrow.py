import hashlib
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_feed_bizgrow as bf

HEADER = "| id | status | type | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
CONTENT = '+++\ntitle = "Ключови думи | BizGrow"\nslug = "klyuchovi-dumi"\nlocale = "bg"\nlast_updated = "2026-11-15"\n+++\n\n## H {#hero}\n\nLead.\n'

def make_repo(tmp_path, rows):
    (tmp_path / "BizGrow").mkdir()
    (tmp_path / "BizGrow" / "content-queue.md").write_text("# Q\n" + HEADER + rows, encoding="utf-8")
    c = tmp_path / "BizGrow" / "articles" / "2026-11-15-klyuchovi-dumi" / "content"
    c.mkdir(parents=True)
    (c / "klyuchovi-dumi.md").write_text(CONTENT, encoding="utf-8")
    return tmp_path

def row(status, query, folder="2026-11-15-klyuchovi-dumi"):
    return f"| bz-0001 | {status} | new-page | {query} | k | 80 | 0 | backlog | 2026-11-15 |  | {folder} | #1 | skipped |  |\n"

def test_approved_article_enters_feed(tmp_path):
    root = make_repo(tmp_path, row("approved", "/saveti/klyuchovi-dumi/"))
    feed = bf.build(root, now="2026-11-21T08:00:00Z")
    assert feed["count"] == 1
    a = feed["articles"][0]
    assert a["slug"] == "klyuchovi-dumi" and a["path"] == "/saveti/klyuchovi-dumi/"
    assert a["content_path"] == "BizGrow/articles/2026-11-15-klyuchovi-dumi/content/klyuchovi-dumi.md"
    assert a["title"] == "Ключови думи | BizGrow" and a["locale"] == "bg"
    assert a["date_modified"] == "2026-11-15" and a["status"] == "approved"
    assert a["content_hash"] == hashlib.sha256(CONTENT.encode("utf-8")).hexdigest()

def test_drafted_and_non_article_rows_are_skipped(tmp_path):
    root = make_repo(tmp_path, row("drafted", "/saveti/klyuchovi-dumi/") + row("approved", "/reklama/"))
    assert bf.build(root, now="x")["count"] == 0

def test_missing_content_file_is_skipped(tmp_path):
    root = make_repo(tmp_path, row("approved", "/saveti/drugo/", folder="2026-11-16-drugo"))
    assert bf.build(root, now="x")["articles"] == []

def test_write_feed(tmp_path):
    root = make_repo(tmp_path, row("posted", "/saveti/klyuchovi-dumi/"))
    bf.write(root, bf.build(root, now="2026-11-21T08:00:00Z"))
    data = json.loads((root / "BizGrow" / "published" / "index.json").read_text(encoding="utf-8"))
    assert data["brand"] == "bizgrow" and data["count"] == 1
