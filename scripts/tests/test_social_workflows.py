import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from social import board, build_social_dashboard as dash, make_pack, pack as packmod, pr_sync  # noqa: E402
from test_social_drafting import DRAFT, offline, repo_on  # noqa: E402


class FakeGitHub:
    def __init__(self, pr, files):
        self.pr, self.files = pr, files
        self.bodies, self.statuses, self.sticky, self.comments, self.labels = [], [], [], [], []

    def permission(self, user):
        return {"AmigoNiko": "admin", "Ivana": "write"}.get(user, "read")

    def pull(self, n):
        return self.pr

    def pull_files(self, n):
        return [{"filename": f} for f in self.files]

    def update_pull(self, n, body=None, title=None):
        self.bodies.append(body)

    def status(self, sha, state, context, description, target_url=None):
        self.statuses.append((sha, state, context, description))

    def sticky_comment(self, n, marker, body):
        self.sticky.append((marker, body))

    def comment(self, n, body):
        self.comments.append(body)

    def add_labels(self, n, labels):
        self.labels += labels


def pack_files(root, pack_id):
    d = root / "VsichkiKazina" / "social" / "packs" / pack_id
    return [str(p.relative_to(root)).replace("\\", "/") for p in d.rglob("*") if p.is_file()]


def test_review_pass_renders_and_checks_with_no_key(tmp_path, monkeypatch):
    monkeypatch.delenv("SOCIAL_TRANSLATE_KEY", raising=False)
    root = repo_on(tmp_path)
    d, summary = make_pack.build(DRAFT, "vsichkikazina", root, gemini=None, fetch=offline)
    gh = FakeGitHub({"head": {"ref": "social/vk/vk-0002-p1", "sha": "abc123"}}, pack_files(root, "vk-0002-p1"))
    results = pr_sync.review(gh, 410, root, root=root)
    assert results["vk-0002-p1"]["ok"] is True
    assert gh.statuses == [("abc123", "success", "social-checks", "all checks pass")]
    body = gh.bodies[0]
    assert body.startswith("## Social pack `vk-0002-p1` — Всички Казина")
    assert f"<!-- view:{packmod.files_hash(d)} -->" in body
    assert gh.sticky[0][0] == pr_sync.MARKER and "all passing" in gh.sticky[0][1]
    assert "Wagering x40 on the bonus is a condition" in body                       # the agent's English, as written
    # a pack whose draft had no English: the checks still pass, and the view says there is none
    bare = dict(DRAFT, request_id="vk-req-001", posts=[{k: v for k, v in dp.items() if k != "english"} for dp in DRAFT["posts"]])
    make_pack.build(bare, "vsichkikazina", root, gemini=None, fetch=offline)
    gh2 = FakeGitHub({"head": {"ref": "social/vk/vk-0002-p2", "sha": "def456"}}, pack_files(root, "vk-0002-p2"))
    pr_sync.review(gh2, 411, root, root=root)
    assert gh2.statuses[0][1] == "success" and "(none: the AI did not write one)" in gh2.bodies[0]
    # not a social PR: nothing happens
    gh3 = FakeGitHub({"head": {"ref": "content/2026-11-01-x", "sha": "1"}}, [])
    assert pr_sync.review(gh3, 1, root, root=root) == {} and gh3.bodies == []


def test_after_merge(tmp_path):
    root = repo_on(tmp_path)
    make_pack.build(DRAFT, "vsichkikazina", root, gemini=None, fetch=offline)
    p = board.packs_path("vsichkikazina", root)
    p.write_text(board.upsert_pack(p.read_text(encoding="utf-8"), {
        "pack_id": "vk-0002-p1", "source": "vk-0002", "title": "Разиграване", "pr": "#410",
        "branch": "social/vk/vk-0002-p1", "status": "open", "posts": "2", "created": "2026-11-03"}), encoding="utf-8")
    files = pack_files(root, "vk-0002-p1")
    pr = {"head": {"ref": "social/vk/vk-0002-p1"}, "merged_at": "2026-11-03T13:00:00Z", "merged_by": {"login": "someone"}}
    gh = FakeGitHub(pr, files)
    assert pr_sync.merged(gh, 410, root=root, today="2026-11-03") == "merged"
    assert gh.comments[0].startswith("⚠️ **Not approved**: this PR was merged by @someone, who has no write access")
    row = board.parse_packs(p.read_text(encoding="utf-8"))[0]
    assert (row["status"], row["note"], row["updated"]) == ("merged", "merged by someone, who cannot approve", "2026-11-03")
    for who in ("AmigoNiko", "Ivana"):                     # anyone of the team
        gh = FakeGitHub(dict(pr, merged_by={"login": who}), files)
        pr_sync.merged(gh, 410, root=root)
        assert "Not approved" not in gh.comments[0] and "After-merge checks" in gh.comments[0]
    gh = FakeGitHub({"head": {"ref": "social/vk/vk-0002-p1"}, "merged_at": None}, files)
    assert pr_sync.merged(gh, 410, root=root) == "closed" and gh.comments == []
    assert pr_sync.packs_in(["VsichkiKazina/social/packs/vk-0002-p1/pack.json", "README.md",
                             "VsichkiKazina/social/packs/vk-0002-p1/posts/a.md"]) == \
        [("vsichkikazina", "VsichkiKazina/social/packs/vk-0002-p1")]


def test_dashboard_data(tmp_path):
    root = repo_on(tmp_path)
    make_pack.build(DRAFT, "vsichkikazina", root, gemini=None, fetch=offline)
    p = board.packs_path("vsichkikazina", root)
    text = p.read_text(encoding="utf-8")
    text = board.upsert_pack(text, {"pack_id": "vk-0002-p1", "source": "vk-0002", "title": "Разиграване", "pr": "#410",
                                    "branch": "social/vk/vk-0002-p1", "status": "open", "created": "2026-11-01"})
    text = board.upsert_pack(text, {"pack_id": "vk-0005", "source": "vk-0005", "status": "skipped",
                                    "note": "operator or bonus article"})
    p.write_text(text, encoding="utf-8")
    ledger = {"last_check_utc": "2026-11-20T09:10:00Z", "banners": [{"kind": "reconnect", "text": "reconnect account ig-vsichkikazina"}],
              "posts": [
                  {"post_id": "vk-0002-p1-fb-1", "network": "facebook", "account_id": "fb-vsichkikazina", "pack_id": "vk-0002-p1",
                   "state": "scheduled", "planned_slot_utc": "2026-11-21T10:30:00Z"},
                  {"post_id": "vk-0002-p1-ig-1", "network": "instagram", "account_id": "ig-vsichkikazina", "pack_id": "vk-0002-p1",
                   "state": "published", "published_utc": "2026-11-19T17:30:00Z", "network_url": "https://instagram.com/p/x",
                   "markers": ["late"]},
                  {"post_id": "vk-0001-p1-x-1", "network": "x", "account_id": "x-vsichkikazina", "pack_id": "vk-0001-p1",
                   "state": "held", "reason": "held:live_page_differs", "missing_lines": ["5%"]},
                  {"post_id": "vk-0001-p1-fb-1", "state": "failed", "reason": "permission"}]}
    (root / "VsichkiKazina" / "social" / "ledger.json").write_text(json.dumps(ledger), encoding="utf-8")
    now = datetime(2026, 11, 20, 12, 0, tzinfo=timezone.utc)
    review, schedule = dash.build(root, "vsichkikazina", now)
    assert [(r["pack_id"], r["status"], r["age_days"], r["waiting_long"], r["posts"], r["formats"]) for r in review["rows"]] == \
        [("vk-0002-p1", "in review", 19, True, 2, ["single"])]
    assert review["skipped"] == [{"item_id": "vk-0005", "reason": "operator or bonus article"}]
    assert schedule["counters"] == {"in_review": 1, "in_review_posts": 2, "scheduled_next_7_days": 1,
                                    "published_this_month": 1, "failed": 1}
    rows = {r["post_id"]: r for r in schedule["rows"]}
    assert rows["vk-0002-p1-fb-1"]["time_local"] == "2026-11-21 12:30"                # Sofia, winter time
    assert rows["vk-0002-p1-ig-1"]["markers"] == ["late"] and rows["vk-0001-p1-x-1"]["missing_lines"] == ["5%"]
    assert rows["vk-0001-p1-x-1"]["badge"] == "Held"
    assert schedule["banners"][0]["text"] == "reconnect account ig-vsichkikazina"
    assert schedule["last_check_utc"] == "2026-11-20T09:10:00Z"
    dash.write(root, "vsichkikazina", review, schedule)
    f = root / "docs" / "data" / "social" / "vsichkikazina-schedule.json"
    first = f.read_text(encoding="utf-8")
    dash.write(root, "vsichkikazina", *dash.build(root, "vsichkikazina", now.replace(hour=13)))
    assert f.read_text(encoding="utf-8") == first                                      # unchanged data: no churn


def test_the_dashboard_preview_of_an_open_pr(tmp_path):
    """review writes docs/data/social/previews/<pack>/ (the posts, pack.json, the checks, the images) so
    the page needs no key to show them; the merge or the close removes it."""
    root = repo_on(tmp_path)
    make_pack.build(DRAFT, "vsichkikazina", root, gemini=None, fetch=offline)
    pr = {"number": 410, "title": "Social: Разиграване", "html_url": "https://github.com/x/y/pull/410",
          "head": {"ref": "social/vk/vk-0002-p1", "sha": "abc123"}}
    gh = FakeGitHub(pr, pack_files(root, "vk-0002-p1"))
    pr_sync.review(gh, 410, root, root=root, preview_root=root)
    pv = root / "docs" / "data" / "social" / "previews" / "vk-0002-p1"
    data = json.loads((pv / "preview.json").read_text(encoding="utf-8"))
    assert (data["pr"]["number"], data["pr"]["head"]["ref"], data["checks"]["state"], data["fixes"]) == \
        (410, "social/vk/vk-0002-p1", "success", [])
    assert set(data["posts"]) == {"vk-0002-p1-fb-1", "vk-0002-p1-ig-1"} and data["meta"]["pack_id"] == "vk-0002-p1"
    assert data["posts"]["vk-0002-p1-fb-1"]["fields"]["english"].startswith("Text:\nWagering x40")
    assert all((pv / f).exists() for files in data["images"].values() for f in files) and data["images"]["vk-0002-p1-fb-1"]
    closed = FakeGitHub({"head": {"ref": "social/vk/vk-0002-p1"}, "merged_at": None}, pack_files(root, "vk-0002-p1"))
    assert pr_sync.merged(closed, 410, root=root) == "closed" and not pv.exists()


def test_the_after_merge_step_needs_no_pillow():
    """social-on-merge.yml installs no Pillow: pr_sync must load without it (the images are made in review only)."""
    import subprocess
    code = ("import builtins, sys\nsys.path.insert(0, %r)\nreal = builtins.__import__\n"
            "def no_pil(name, *a, **k):\n    if name == 'PIL' or name.startswith('PIL.'):\n        raise ModuleNotFoundError(name)\n"
            "    return real(name, *a, **k)\nbuiltins.__import__ = no_pil\nfrom social import pr_sync\n") % str(Path(__file__).resolve().parents[1])
    got = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    assert got.returncode == 0, got.stderr
