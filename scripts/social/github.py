"""A small GitHub REST client for the social scripts (standard library only).

The token comes from the caller: GITHUB_TOKEN in Actions, the machine user's in drafting, the
GitHub App installation token in the guest (github_app.py). It is sent only to api.github.com
and never printed. Tests pass a fake with the same methods.
"""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
# The repository the scripts act on: SOCIAL_REPO if set, else the one GitHub Actions runs in,
# else AIContent (so a copy of the repository never reads or writes the original).
REPO = os.environ.get("SOCIAL_REPO") or os.environ.get("GITHUB_REPOSITORY") or "ProfitXtraV2/AIContent"


class GitHubError(Exception):
    def __init__(self, message, status=None):
        super().__init__(message)
        self.status = status                     # the HTTP status, None when GitHub was not reached


class GitHub:
    def __init__(self, token, repo=REPO, api=API):
        self.token, self.repo, self.api = token, repo, api

    def _call(self, method, path, body=None, params=None):
        url = path if path.startswith("http") else f"{self.api}{path}"
        if params:
            url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers={
            "Authorization": f"Bearer {self.token}", "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "px-social",
            **({"Content-Type": "application/json"} if data else {})})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as e:
            raise GitHubError(f"{method} {path}: HTTP {e.code}", e.code) from None
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            raise GitHubError(f"{method} {path}: {e}") from None

    def _pages(self, path, params=None, limit=10):
        out = []
        for page in range(1, limit + 1):
            got = self._call("GET", path, params={**(params or {}), "per_page": 100, "page": page})
            out += got or []
            if not got or len(got) < 100:
                break
        return out

    # pulls
    def pull(self, number):
        return self._call("GET", f"/repos/{self.repo}/pulls/{int(number)}")

    def pulls(self, state="open", base="main", sort="updated", direction="desc", limit=3):
        return self._pages(f"/repos/{self.repo}/pulls", {"state": state, "base": base, "sort": sort,
                                                          "direction": direction}, limit)

    def pull_files(self, number):
        return self._pages(f"/repos/{self.repo}/pulls/{int(number)}/files")

    def update_pull(self, number, body=None, title=None):
        data = {k: v for k, v in (("body", body), ("title", title)) if v is not None}
        return self._call("PATCH", f"/repos/{self.repo}/pulls/{int(number)}", data)

    def add_labels(self, number, labels):
        return self._call("POST", f"/repos/{self.repo}/issues/{int(number)}/labels", {"labels": list(labels)})

    def remove_label(self, number, label):
        try:
            return self._call("DELETE", f"/repos/{self.repo}/issues/{int(number)}/labels/{urllib.parse.quote(label)}")
        except GitHubError:
            return None

    def sticky_comment(self, number, marker, body):
        """Create or update the one comment that holds `marker` (an HTML comment)."""
        body = f"{marker}\n{body}"
        for c in self.issue_comments(number):
            if marker in (c.get("body") or ""):
                return self.update_comment(c["id"], body)
        return self.comment(number, body)

    # commits
    def commits(self, path, since=None, sha="main"):
        params = {"path": path, "sha": sha}
        if since:
            params["since"] = since
        return self._pages(f"/repos/{self.repo}/commits", params, limit=3)

    def commit_pulls(self, sha):
        return self._call("GET", f"/repos/{self.repo}/commits/{sha}/pulls") or []

    def file_at(self, path, ref):
        """The bytes of a file at a commit, or None."""
        try:
            got = self._call("GET", f"/repos/{self.repo}/contents/{urllib.parse.quote(path)}", params={"ref": ref})
        except GitHubError:
            return None
        import base64
        return base64.b64decode(got["content"]) if got and got.get("content") is not None else None

    # issues and comments
    def issue_comments(self, number, since=None):
        params = {"since": since} if since else None
        return self._pages(f"/repos/{self.repo}/issues/{int(number)}/comments", params)

    def comment(self, number, body):
        return self._call("POST", f"/repos/{self.repo}/issues/{int(number)}/comments", {"body": body})

    def update_comment(self, comment_id, body):
        return self._call("PATCH", f"/repos/{self.repo}/issues/comments/{int(comment_id)}", {"body": body})

    def issue(self, number):
        return self._call("GET", f"/repos/{self.repo}/issues/{int(number)}")

    def close_issue(self, number, reason="completed"):
        return self._call("PATCH", f"/repos/{self.repo}/issues/{int(number)}", {"state": "closed", "state_reason": reason})

    def create_pull(self, head, title, body, base="main"):
        return self._call("POST", f"/repos/{self.repo}/pulls", {"head": head, "base": base, "title": title, "body": body})

    def permission(self, user):
        """admin | maintain | write | read | none. "none" for an unknown login; GitHubError when
        GitHub cannot answer, so a failed lookup is never taken for a refusal."""
        try:
            got = self._call("GET", f"/repos/{self.repo}/collaborators/{urllib.parse.quote(user)}/permission")
        except GitHubError as e:
            if e.status == 404:
                return "none"
            raise
        return (got or {}).get("permission", "none")

    def status(self, sha, state, context, description, target_url=None):
        body = {"state": state, "context": context, "description": description[:140]}
        if target_url:
            body["target_url"] = target_url
        return self._call("POST", f"/repos/{self.repo}/statuses/{sha}", body)

    def contents_json(self, repo, path, ref="main"):
        """A JSON file of another repository (the publisher record in WebPortals), or None."""
        try:
            got = self._call("GET", f"/repos/{repo}/contents/{urllib.parse.quote(path)}", params={"ref": ref})
        except GitHubError:
            return None
        import base64
        try:
            return json.loads(base64.b64decode(got["content"]).decode("utf-8"))
        except (KeyError, ValueError, TypeError):
            return None


def from_env():
    """A client from GITHUB_TOKEN (Actions, drafting), or None when there is no token."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    return GitHub(token) if token else None


TEAM = {"admin", "maintain", "write"}


class Team:
    """Who approves (boundary 3): anyone whose permission on the repository is write, maintain or
    admin, never a bot. Their merge approves a pack or a settings change, and their /lift ends a
    stop. Each login is asked once per run; GitHubError when GitHub cannot answer."""

    def __init__(self, gh):
        self.gh, self.known = gh, {}

    def has(self, login):
        login = (login or "").strip()
        if not login or login.lower().endswith("[bot]") or self.gh is None:
            return False
        if login.lower() not in self.known:
            self.known[login.lower()] = self.gh.permission(login) in TEAM
        return self.known[login.lower()]

    def merged(self, pr):
        """True when the PR was merged by someone of the team."""
        return bool(pr and pr.get("merged_at")) and self.has((pr.get("merged_by") or {}).get("login"))
