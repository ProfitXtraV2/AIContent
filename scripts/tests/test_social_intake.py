"""The issues the dashboard opens for a person (intake.py): commands and requests."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from social import board, github, intake, settings as st  # noqa: E402
from test_social_drafting import repo_on  # noqa: E402

CREATED = "2026-11-04T07:00:00Z"


class FakeGitHub:
    repo = "AmigoNiko/AIContent-social-test"

    def __init__(self, issue, permission="write", pulls_allowed=True):
        self.issues, self.perm = {7: dict(issue, number=7, created_at=CREATED)}, permission
        self.comments, self.closed, self.pulls, self.pulls_allowed = [], [], [], pulls_allowed

    def issue(self, n):
        return self.issues[n]

    def permission(self, user):
        return self.perm

    def comment(self, n, body):
        self.comments.append((n, body))

    def close_issue(self, n, reason="completed"):
        self.closed.append((n, reason))

    def create_pull(self, head, title, body, base="main"):
        if not self.pulls_allowed:          # "Allow GitHub Actions to create and approve pull requests" is off
            raise github.GitHubError("POST /pulls: HTTP 403", 403)
        self.pulls.append({"head": head, "title": title, "body": body})
        return {"number": 12, "html_url": f"https://github.com/{self.repo}/pull/12"}



class FakeGit:
    def __init__(self, root, gh):
        self.root, self.gh, self.log = Path(root), gh, []

    def commit_to_main(self, paths, message):
        self.log.append(("main", message, sorted(paths)))
        return True

    def commit_to_branch(self, paths, message, branch):
        self.log.append((branch, message, sorted(paths)))


def run(root, issue, permission="write", pulls_allowed=True):
    gh = FakeGitHub(issue, permission, pulls_allowed)
    git = FakeGit(root, gh)
    return intake.handle(gh, git, root, 7), gh, git


def test_commands(tmp_path):
    root = repo_on(tmp_path)
    msg, gh, git = run(root, {"title": "social: post now vk-0012-p1-ig-1", "body": "", "user": {"login": "Ivana"}})
    assert msg.startswith("Готово: „post now vk-0012-p1-ig-1“") and git.log[0][0] == "main"
    _, cmds = board.parse_requests(board._read(board.requests_path("vsichkikazina", root)))
    assert (cmds[-1]["id"], cmds[-1]["command"], cmds[-1]["post_id"], cmds[-1]["status"], cmds[-1]["note"]) == \
        ("vk-cmd-001", "post now", "vk-0012-p1-ig-1", "open", "#7 @Ivana")
    assert (root / "docs" / "data" / "social" / "vsichkikazina-board.json").exists()      # the dashboard data too
    msg, _, _ = run(root, {"title": "social:  not before vk-0012-p1-ig-1 2026-11-09", "body": "", "user": {"login": "Ivana"}})
    assert msg.startswith("Готово")
    _, cmds = board.parse_requests(board._read(board.requests_path("vsichkikazina", root)))
    assert (cmds[-1]["command"], cmds[-1]["date"]) == ("not before", "2026-11-09")
    msg, _, git = run(root, {"title": "social: cancel vk-12", "body": "", "user": {"login": "Ivana"}})
    assert msg.startswith("Не стана: unknown post ID") and git.log == []


def test_a_time_for_a_whole_pack(tmp_path):
    root = repo_on(tmp_path)
    msg, _, git = run(root, {"title": "social: post at vk-0012-p1 2026-11-05 17:15", "body": "", "user": {"login": "Ivana"}})
    assert msg.startswith("Готово") and git.log[0][0] == "main"
    _, cmds = board.parse_requests(board._read(board.requests_path("vsichkikazina", root)))
    assert (cmds[-1]["command"], cmds[-1]["post_id"], cmds[-1]["date"]) == ("post at", "vk-0012-p1", "2026-11-05 17:15")
    msg, _, git = run(root, {"title": "social: post at vk-0012-p1 tomorrow", "body": "", "user": {"login": "Ivana"}})
    assert msg.startswith("Не стана: post at needs a day and a time") and git.log == []


def test_only_people_who_may_write(tmp_path):
    root = repo_on(tmp_path)
    msg, gh, git = run(root, {"title": "social: post now vk-0012-p1-ig-1", "body": "", "user": {"login": "stranger"}},
                       permission="read")
    assert msg.startswith("Само хора с право на запис") and git.log == []
    assert run(root, {"title": "Bug: the page is slow", "body": "", "user": {"login": "x"}})[0] is None


def test_a_request_with_a_pasted_source(tmp_path):
    root = repo_on(tmp_path)
    data = {"brand": "vsichkikazina", "kind": "topic", "target": "7 грешки при рулетката", "angle": "мит или факт",
            "format": "carousel", "slides": "7", "sources": ["https://example.org/ruletka"], "accounts": ["ig-vsichkikazina"]}
    body = (f"<!-- social:request {json.dumps(data, ensure_ascii=False)} -->\n**Тема:** 7 грешки при рулетката\n\n"
            "<!-- source -->\nЗелената нула е 1 от 37 полета.\n<!-- /source -->\n")
    msg, gh, git = run(root, {"title": "social: request 7 грешки при рулетката", "body": body, "user": {"login": "Ivana"}})
    assert msg.startswith("Готово: заявката за „7 грешки при рулетката“")
    reqs, _ = board.parse_requests(board._read(board.requests_path("vsichkikazina", root)))
    r = reqs[-1]
    assert (r["id"], r["kind"], r["format"], r["slides"], r["accounts"], r["status"]) == \
        ("vk-req-001", "topic", "carousel", "7", "ig-vsichkikazina", "open")
    src = "sources/20261104T070000-7-грешки-при-рулетката.md"
    assert board.request_sources(r) == ["https://example.org/ruletka", src]
    assert (root / "VsichkiKazina" / "social" / src).read_text(encoding="utf-8") == \
        "# Source for: 7 грешки при рулетката\n\nЗелената нула е 1 от 37 полета.\n"
    assert "VsichkiKazina/social/" + src in git.log[0][2]



def settings_issue(brand_changes=None, account_changes=None, who="Ivana"):
    data = {"brand": "vsichkikazina", "brand_changes": brand_changes or {}, "account_changes": account_changes or {}}
    return {"title": "social: settings vsichkikazina", "user": {"login": who},
            "body": f"<!-- social:settings {json.dumps(data, ensure_ascii=False)} -->\n**Settings change:** …"}


def test_a_settings_change_becomes_a_pr_its_author_merges(tmp_path):
    root = repo_on(tmp_path)
    path = root / "VsichkiKazina" / "social" / "settings.md"
    msg, gh, git = run(root, settings_issue({"pause": "on"}, {"ig-vsichkikazina": {"slots": "daily 12:45, 18:30"}}))
    assert msg.startswith("Готово: промяната е в PR #12: https://github.com/AmigoNiko/AIContent-social-test/pull/12")
    assert git.log == [("settings/vsichkikazina-7", git.log[0][1], ["VsichkiKazina/social/settings.md"])]
    assert git.log[0][1].startswith("social: settings of Всички Казина (#7, @Ivana)")
    assert "- pause: on" in git.log[0][1] and "- ig-vsichkikazina · slots: daily 12:45, 18:30" in gh.pulls[0]["body"]
    assert gh.pulls[0]["head"] == "settings/vsichkikazina-7" and "the person who asked may merge it" in gh.pulls[0]["body"]
    s = st.parse(path.read_text(encoding="utf-8"))
    assert s.brand["pause"] is True and s.account("ig-vsichkikazina")["slots_text"] == "daily 12:45, 18:30"


def test_a_settings_change_that_would_break_a_rule_is_refused(tmp_path):
    root = repo_on(tmp_path)
    before = (root / "VsichkiKazina" / "social" / "settings.md").read_text(encoding="utf-8")
    for issue, why in ((settings_issue(account_changes={"ig-vsichkikazina": {"link": "in post"}}),
                        "Не стана: ig-vsichkikazina: Instagram posts cannot carry a link"),
                       (settings_issue({"approver": "Ivana"}), "Не стана: unknown setting 'approver'."),
                       (settings_issue({"social": "on"}), "Не стана: нищо не се променя")):
        msg, gh, git = run(root, issue)
        assert msg.startswith(why) and git.log == [] and gh.pulls == []
    assert (root / "VsichkiKazina" / "social" / "settings.md").read_text(encoding="utf-8") == before
    msg, _, git = run(root, settings_issue({"pause": "on"}, who="stranger"), permission="read")
    assert msg.startswith("Само хора с право на запис") and git.log == []


def test_without_the_pr_permission_the_branch_waits_for_its_pr(tmp_path):
    root = repo_on(tmp_path)
    msg, gh, git = run(root, settings_issue({"packs_per_run": "3"}), pulls_allowed=False)
    assert msg.startswith("Готово: промяната е в клона `settings/vsichkikazina-7`")
    assert "https://github.com/AmigoNiko/AIContent-social-test/compare/main...settings/vsichkikazina-7?expand=1" in msg
    assert git.log[0][0] == "settings/vsichkikazina-7"
