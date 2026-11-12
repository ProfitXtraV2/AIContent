"""The guest's deployment files and the identities list (tech spec, Setup; I1, I5, I6)."""
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import list_identities, secret_scan  # noqa: E402

DEPLOY = Path(__file__).resolve().parents[1] / "social" / "deploy"


def read(name):
    return (DEPLOY / name).read_text(encoding="utf-8")


def test_timers_and_the_shared_lock():
    assert "OnCalendar=*-*-* *:10:00" in read("px-social-check.timer")
    assert "OnCalendar=*:0/5" in read("px-social-control.timer")
    for t in ("px-social-check.timer", "px-social-control.timer", "px-social-backup.timer"):
        assert "Persistent=true" in read(t)
    for s in ("px-social-check.service", "px-social-control.service"):
        text = read(s)
        assert "flock -w 240 /run/px-social/lock" in text and "User=px-social" in text
        assert "EnvironmentFile=/etc/px-social/env" in text and "ProtectSystem=strict" in text


def test_the_tool_is_reachable_only_through_two_step_sign_in():
    caddy = read("Caddyfile")
    assert re.search(r"@public_api path /api/public/\*\s+handle @public_api \{\s+respond 403", caddy)
    assert "forward_auth authelia:9091" in caddy and "@uploads path /uploads/*" in caddy
    assert "trusted_proxies static 172.30.0.10/32" in caddy and "client_ip_headers Cf-Connecting-IP" in caddy
    compose = read("docker-compose.override.yml")
    published = re.findall(r'^\s+- "([^"]+:\d+:\d+)"', compose, re.M)
    assert published == ["127.0.0.1:5000:5000"]                    # no port on the LAN
    assert 'API_LIMIT: "600"' in compose and "ipv4_address: 172.30.0.10" in compose
    assert all("@sha256:" in line for line in re.findall(r"^\s+image: (.+)$", compose, re.M))   # pinned
    authelia = read("authelia-configuration.yml")
    assert "default_policy: deny" in authelia and "policy: two_factor" in authelia
    assert "http_status:404" in read("cloudflared.yml")


def test_no_secret_in_the_deploy_files():
    assert secret_scan.scan_paths([DEPLOY]) == []
    for line in read("env.example").splitlines():
        if re.match(r"^(POSTIZ_API_KEY|WEBPORTALS_READ_TOKEN|PX_SOCIAL_APP_ID|PX_SOCIAL_INSTALLATION_ID)=", line):
            assert line.endswith("="), line                        # names only, never values
    assert "DRY_RUN=1" in read("env.example")


def test_release_must_be_signed():
    deploy = read("deploy.sh")
    assert "verify-tag" in deploy and "gpg.ssh.allowedSignersFile" in deploy
    assert deploy.index("verify-tag") < deploy.index("git -C \"$SRC\" archive")


def test_host_scripts_are_plain_ascii():
    """Windows PowerShell 5.1 reads a file without BOM in the ANSI code page."""
    for name in ("qualify-host.ps1", "audit-host.ps1"):
        assert all(b < 128 for b in (DEPLOY / name).read_bytes()), name
        text = read(name)
        assert "S-1-5-32-544" in text and "S-1-5-32-578" in text    # groups by SID, any Windows language


class FakeGH:
    def _call(self, method, path, body=None, params=None):
        if path.endswith("/installations"):
            return {"installations": [{"app_slug": "px-publishing-check", "repository_selection": "selected",
                                       "permissions": {"contents": "write", "pull_requests": "read"}}]}
        if path.endswith("/actions/runs"):
            return {"workflow_runs": [{"name": "social-pr", "actor": {"login": "profitxtra-agent"},
                                       "triggering_actor": {"login": "profitxtra-agent"}},
                                      {"name": "approve-on-merge", "actor": {"login": "AmigoNiko"}}]}
        return {"allow_auto_merge": True}

    def _pages(self, path, params=None, limit=10):
        if path.endswith("/collaborators"):
            return [{"login": "profitxtra-agent", "role_name": "write"}, {"login": "AmigoNiko", "role_name": "admin"}]
        if path.endswith("/keys"):
            return []
        return [{"author": {"login": "profitxtra-agent"}, "committer": {"login": "web-flow"},
                 "commit": {"author": {"name": "agent"}, "committer": {"name": "GitHub"}}},
                {"author": None, "committer": None, "commit": {"author": {"name": "github-actions[bot]"},
                                                             "committer": {"name": "github-actions[bot]"}}}]


def test_identities_list():
    now = datetime(2026, 11, 1, tzinfo=timezone.utc)
    data = list_identities.gather(FakeGH(), "ProfitXtraV2/AIContent", 30, now)
    assert data["since"] == "2026-10-02T00:00:00Z" and data["auto_merge_allowed"] is True
    assert [c["login"] for c in data["collaborators"]] == ["AmigoNiko", "profitxtra-agent"]
    assert data["workflow_actors"] == [{"login": "AmigoNiko", "workflows": ["approve-on-merge"]},
                                       {"login": "profitxtra-agent", "workflows": ["social-pr"]}]
    md = list_identities.markdown(data, now)
    assert "Auto-merge allowed: **yes — switch it off" in md
    assert "| (no account) github-actions[bot] | author, committer | 1 |" in md
    assert "| px-publishing-check | selected | contents: write, pull_requests: read |" in md
