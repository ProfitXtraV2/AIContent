#!/usr/bin/env python3
"""Every identity that can push to or merge in AIContent (product spec I6; tech spec, Setup,
step 2.5). The setup person runs it with their own GitHub token and pastes the output into
SOCIAL-SETUP.md under "Identities"; Nikolay confirms that none of them acts as Nikolay's account.

    GH_TOKEN=$(gh auth token) python3 scripts/social/list_identities.py [--days 30] [--repo owner/name]

Lists: collaborators and their permission; deploy keys; GitHub Apps installed for the
organisation (needs an owner's token, else it says so); the actors of workflow runs; commit
authors and committers of the last 30 days; and whether auto-merge is off (boundary 3). It reads
only; nothing is changed, and no token is printed.
"""
import argparse
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import github  # noqa: E402


def gather(gh, repo, days=30, now=None):
    now = now or datetime.now(timezone.utc)
    since = (now - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    org = repo.split("/")[0]
    out = {"repo": repo, "since": since, "notes": []}
    info = gh._call("GET", f"/repos/{repo}") or {}
    out["auto_merge_allowed"] = bool(info.get("allow_auto_merge"))
    out["collaborators"] = sorted(
        ({"login": c["login"], "role": c.get("role_name") or _role(c.get("permissions") or {})}
         for c in gh._pages(f"/repos/{repo}/collaborators", {"affiliation": "all"})),
        key=lambda c: c["login"].lower())
    out["deploy_keys"] = [{"title": k.get("title"), "read_only": k.get("read_only"), "created_at": k.get("created_at")}
                          for k in gh._pages(f"/repos/{repo}/keys")]
    try:
        got = gh._call("GET", f"/orgs/{org}/installations", params={"per_page": 100}) or {}
        out["apps"] = [{"app": i.get("app_slug"), "repositories": i.get("repository_selection"),
                        "permissions": i.get("permissions")} for i in got.get("installations", [])]
    except github.GitHubError as e:
        out["apps"] = []
        out["notes"].append(f"installed apps not listed ({e}); an organisation owner's token can list them")
    runs = gh._call("GET", f"/repos/{repo}/actions/runs",
                    params={"created": f">={since[:10]}", "per_page": 100}) or {}
    actors = {}
    for r in runs.get("workflow_runs", []):
        for key in ("actor", "triggering_actor"):
            login = (r.get(key) or {}).get("login")
            if login:
                actors.setdefault(login, set()).add(r.get("name") or "")
    out["workflow_actors"] = [{"login": k, "workflows": sorted(v)} for k, v in sorted(actors.items())]
    people = {}
    for c in gh._pages(f"/repos/{repo}/commits", {"since": since}, limit=10):
        commit = c.get("commit") or {}
        for key in ("author", "committer"):
            login = (c.get(key) or {}).get("login")
            name = (commit.get(key) or {}).get("name") or ""
            label = login or f"(no account) {name}"
            people.setdefault(label, {"as": set(), "commits": 0})
            people[label]["as"].add(key)
        label = (c.get("author") or {}).get("login") or f"(no account) {(commit.get('author') or {}).get('name') or ''}"
        people[label]["commits"] += 1
    out["commit_identities"] = [{"identity": k, "as": sorted(v["as"]), "commits": v["commits"]}
                                for k, v in sorted(people.items(), key=lambda x: x[0].lower())]
    return out


def _role(perms):
    for role in ("admin", "maintain", "push", "triage", "pull"):
        if perms.get(role):
            return {"push": "write", "pull": "read"}.get(role, role)
    return "none"


def markdown(data, now=None):
    now = now or datetime.now(timezone.utc)
    lines = [f"### Identities — {data['repo']}, {now.strftime('%Y-%m-%d')} (commits and runs since {data['since'][:10]})", ""]
    lines.append(f"- Auto-merge allowed: **{'yes — switch it off (Settings → General)' if data['auto_merge_allowed'] else 'no'}**")
    lines += ["", "| Collaborator | Permission |", "|---|---|"]
    lines += [f"| {c['login']} | {c['role']} |" for c in data["collaborators"]] or ["| (none) | |"]
    lines += ["", "| Deploy key | Read only | Created |", "|---|---|---|"]
    lines += [f"| {k['title']} | {k['read_only']} | {k['created_at']} |" for k in data["deploy_keys"]] or ["| (none) | | |"]
    lines += ["", "| Installed app | Repositories | Permissions |", "|---|---|---|"]
    lines += [f"| {a['app']} | {a['repositories']} | {', '.join(f'{k}: {v}' for k, v in sorted((a['permissions'] or {}).items()))} |"
              for a in data["apps"]] or ["| (not listed) | | |"]
    lines += ["", "| Workflow actor | Workflows |", "|---|---|"]
    lines += [f"| {a['login']} | {', '.join(a['workflows'])} |" for a in data["workflow_actors"]] or ["| (none) | |"]
    lines += ["", "| Commit identity | As | Commits |", "|---|---|---|"]
    lines += [f"| {c['identity']} | {', '.join(c['as'])} | {c['commits']} |" for c in data["commit_identities"]] or ["| (none) | | |"]
    lines += [""] + [f"> {n}" for n in data["notes"]]
    lines += ["", "Nikolay confirms that none of these acts as Nikolay's own account: ☐ (date, initials)"]
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=github.REPO)
    ap.add_argument("--days", type=int, default=30)
    a = ap.parse_args(argv)
    gh = github.from_env()
    if gh is None:
        print("set GH_TOKEN (for example GH_TOKEN=$(gh auth token))", file=sys.stderr)
        return 2
    gh.repo = a.repo
    print(markdown(gather(gh, a.repo, a.days)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
