#!/usr/bin/env python3
"""What a person asks for in a GitHub issue the dashboard opened for them (the page holds no key).

    python3 scripts/social/intake.py <issue number>

social-intake.yml runs this when an issue is opened whose title starts with "social:". Only people
with write access to the repository count; anyone else gets a comment and nothing happens.
  social: post now <post or pack ID> · post at <post or pack ID> <YYYY-MM-DD HH:MM> · cancel <post ID>
        · fix <post ID> · not before <post ID> <date>
        a line in the Commands table of <Brand>/social/requests.md (for a pack still in review, the
        publishing check keeps the line until the merge)
  social: request
        the request in the issue (its fields in <!-- social:request {…} -->, a pasted source text
        between <!-- source --> and <!-- /source -->): a line in the Requests table (the text is
        saved under <Brand>/social/sources/)
  social: settings
        a change of <Brand>/social/settings.md from the dashboard's form (its fields in
        <!-- social:settings {…} -->): checked, committed on its own branch settings/<brand>-<issue>
        and opened as a PR. It counts once someone with write access merges it (the person who
        asked may); the publishing check takes it at its next run.
  social: new brand
        a new brand (its fields in <!-- social:brand {"name", "site", "topic", "language"} -->):
        new_brand.py writes it on the branch settings/new-brand-<key>-<issue>, opened as a PR.
The issue gets a comment saying what happened and is closed. Commits go to main as github-actions;
a push with GITHUB_TOKEN starts no workflow, so this gives new rows their IDs and rebuilds the
dashboard data itself. The issue's text is data: nothing in it is ever run.
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import board, brands, build_social_dashboard as dash, github, ids, new_brand, settings as settingsmod  # noqa: E402

WRITE = {"admin", "maintain", "write"}
COMMAND_RE = re.compile(r"^(post now|post at|cancel|fix|not before)\s+(\S+)(?:\s+(.+))?$", re.I)


def data_block(body, kind):
    """The fields the dashboard put in <!-- social:<kind> {…} --> ({} when there are none)."""
    m = re.search(rf"<!--\s*social:{kind}\s+(\{{.*?\}})\s*-->", body or "", re.S)
    try:
        return json.loads(m.group(1)) if m else {}
    except ValueError:
        return {}


def section(body, name):
    """The text between <!-- name --> and <!-- /name --> ("" when there is none)."""
    m = re.search(rf"<!--\s*{name}\s*-->(.*?)<!--\s*/{name}\s*-->", body or "", re.S)
    return m.group(1).strip() if m else ""


def brand_of(post_id=None, data=None):
    """The brand a command or a request is for: its post ID's prefix, else the issue's own field."""
    prefix = ((ids.parse_post_id(post_id or "") or ids.parse_pack_id(post_id or "") or {}).get("source") or "")[:2]
    by_prefix = {b["prefix"]: k for k, b in brands.BRANDS.items()}
    key = by_prefix.get(prefix) or (data or {}).get("brand") or "vsichkikazina"
    return key if key in brands.BRANDS else "vsichkikazina"


class Git:
    """The main checkout the workflow made (its credentials let it push)."""

    def __init__(self, root):
        self.root = Path(root)

    def __call__(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, capture_output=True, encoding="utf-8",
                              errors="replace", check=True).stdout.strip()

    def commit_to_main(self, paths, message):
        self("add", "--", *paths)
        if not self("status", "--porcelain", "--", *paths):
            return False
        self("commit", "-m", message)
        try:
            self("push", "origin", "HEAD:main")
        except subprocess.CalledProcessError:
            self("pull", "--no-rebase", "--no-edit", "origin", "main")
            self("push", "origin", "HEAD:main")
        return True

    def commit_to_branch(self, paths, message, branch):
        """A new branch from this commit, with the paths committed on it and pushed (main stays as it is)."""
        self("checkout", "-b", branch)
        self("add", "--", *paths)
        self("commit", "-m", message)
        self("push", "origin", f"HEAD:refs/heads/{branch}")


def refresh(root, brand_key, git, message, extra=()):
    """The new rows' IDs, the dashboard data, and the commit to main."""
    req = board.requests_path(brand_key, root)
    text, _new = board.assign_ids(board._read(req), brands.brand(brand_key)["prefix"])
    req.write_text(text, encoding="utf-8")
    dash.write(root, brand_key, *dash.build(root, brand_key))
    rel = lambda p: str(Path(p).relative_to(root)).replace("\\", "/")  # noqa: E731
    return git.commit_to_main([rel(req), "docs/data/social", *[rel(p) for p in extra]], message)


def do_command(root, brand_key, git, parts, who, number):
    command, post_id, date = parts[0].lower(), parts[1], parts[2] or ""
    row = {"command": command, "post_id": post_id, "date": date}
    _parsed, why = board.parse_command(row)
    if why:
        return f"Не стана: {why}."
    req = board.requests_path(brand_key, root)
    req.write_text(board.add_commands(board._read(req), [dict(row, note=f"#{number} @{who}")]), encoding="utf-8")
    refresh(root, brand_key, git, f"social: {command} {post_id} (#{number}, @{who})")
    soon = {"post now": "излиза до около 5 минути (ако постът още чака одобрение: 5 минути след Merge)",
            "post at": f"излиза в {date} (ако постът още чака одобрение: след Merge)",
            "fix": "следващото писане на AI прави поправка"}
    return f"Готово: „{command} {post_id}“ е записано; {soon.get(command, 'проверката го прилага при следващото си минаване')}."


def source_file(target, text, stamp):
    """(rel path under <Brand>/social/, text) of a pasted source (docs/social-md.js sourceFile)."""
    slug = re.sub(r"[^\w]+", "-", str(target or "source").lower()).strip("-_")[:40].strip("-_") or "source"
    clean = re.sub(r"\s+", " ", str(target or "")).replace("|", "/").strip()
    return f"sources/{stamp}-{slug}.md", f"# Source for: {clean}\n\n{str(text).strip()}\n"


def do_request(root, brand_key, git, data, body, who, number, created):
    row = {k: str(data.get(k) or "").strip() for k in ("kind", "target", "angle", "format", "slides", "target_page",
                                                       "earliest")}
    row["accounts"] = ", ".join(data.get("accounts") or [])
    sources = [s for s in data.get("sources") or [] if re.match(r"^https?://\S+$", str(s))]
    extra = []
    pasted = section(body, "source")
    if pasted:
        rel, text = source_file(row["target"], pasted, created.strftime("%Y%m%dT%H%M%S"))
        path = brands.social_dir(brand_key, root) / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        sources.append(rel)
        extra.append(path)
    row["sources"] = ", ".join(sources)
    parsed = dict(row, kind=row["kind"].lower() or "keyword", format=row["format"].lower())
    problem = board.request_problem(parsed) or ("" if row["target"] else "no article, keyword or topic")
    if problem:
        return f"Не стана: {problem}."
    req = board.requests_path(brand_key, root)
    req.write_text(board.add_request(board._read(req), row, created.strftime("%Y-%m-%d")), encoding="utf-8")
    refresh(root, brand_key, git, f"social: request posts for {row['target']} (#{number}, @{who})", extra)
    return (f"Готово: заявката за „{row['target']}“ е записана. Следващото писане на AI прави постовете; "
            f"те идват в „Постове за преглед“.")


def change_lines(brand_changes, account_changes):
    """'- key: value' lines of a settings change, for the commit, the PR and the answer."""
    out = [f"- {k}: {v or '(empty)'}" for k, v in brand_changes.items()]
    for aid, fields in account_changes.items():
        out += [f"- {aid} · {k}: {v or '(empty)'}" for k, v in fields.items()]
    return out


def do_settings(root, brand_key, gh, git, data, who, number):
    brand_changes = {str(k).strip().lower(): str(v) for k, v in (data.get("brand_changes") or {}).items()}
    account_changes = {str(a).strip(): {str(k).strip().lower(): str(v) for k, v in (f or {}).items()}
                       for a, f in (data.get("account_changes") or {}).items() if f}
    path = brands.social_dir(brand_key, root) / "settings.md"
    text = path.read_text(encoding="utf-8")
    try:
        new = settingsmod.update(text, brand_changes, account_changes)
    except ValueError as e:
        return f"Не стана: {e}."
    if new == text:
        return "Не стана: нищо не се променя (стойностите са същите като сега)."
    before = {e["message"] for e in settingsmod.parse(text, brand_key).errors}
    errors = [e["message"] for e in settingsmod.parse(new, brand_key).errors if e["message"] not in before]
    if errors:
        return "Не стана: " + "; ".join(errors) + ". Нищо не е променено."
    path.write_text(new, encoding="utf-8")
    lines = change_lines(brand_changes, account_changes)
    branch = f"settings/{brand_key}-{number}"
    title = f"social: settings of {brands.brand(brand_key)['name']} (#{number}, @{who})"
    git.commit_to_branch([str(path.relative_to(root)).replace("\\", "/")], title + "\n\n" + "\n".join(lines), branch)
    body = (f"The settings change @{who} asked for in #{number}, from the dashboard:\n\n" + "\n".join(lines) +
            "\n\n**Merge** applies it: a merge by anyone with write access to this repository counts (the person "
            "who asked may merge it). The publishing check takes it at its next run (minute :10). Close the PR to "
            "drop the change.")
    try:
        pr = gh.create_pull(branch, title, body)
    except github.GitHubError:                 # "Allow GitHub Actions to create … pull requests" is off
        url = f"https://github.com/{gh.repo}/compare/main...{branch}?expand=1"
        return (f"Готово: промяната е в клона `{branch}`. Отвори {url}, натисни „Create pull request“, "
                f"после **Merge**, за да влезе в сила.")
    return (f"Готово: промяната е в PR #{pr['number']}: {pr['html_url']}\n\nНатисни **Merge** там, за да влезе в "
            f"сила (проверката я взима в :10). Ако се откажеш, затвори PR-а.\n\n" + "\n".join(lines))


def do_new_brand(root, gh, git, data, who, number):
    try:
        key, written = new_brand.create(root, data.get("name"), data.get("site"), data.get("topic"),
                                        data.get("language") or "bg")
    except ValueError as e:
        return f"Не стана: {e}. Нищо не е създадено."
    name = brands.load_registry(Path(root) / "social" / "brands.json")[key]["name"]
    branch = f"settings/new-brand-{key}-{number}"
    title = f"social: new brand {name} ({key}, #{number}, @{who})"
    git.commit_to_branch(written, title, branch)
    body = (f"A new brand for social posts, asked for by @{who} in #{number} from the dashboard: **{name}** "
            f"({data.get('site')}), topic `{data.get('topic')}`, language `{data.get('language') or 'bg'}`.\n\n"
            + "\n".join(f"- `{p}`" for p in written) +
            "\n\nEverything starts switched off. **Merge** adds the brand to the dashboard; then fill in its Settings "
            "(the red fields) and link its accounts with the local setup. Close the PR to drop it.")
    try:
        pr = gh.create_pull(branch, title, body)
    except github.GitHubError:
        url = f"https://github.com/{gh.repo}/compare/main...{branch}?expand=1"
        return (f"Готово: марката „{name}“ е в клона `{branch}`. Отвори {url}, натисни „Create pull request“, "
                f"после **Merge**.")
    return (f"Готово: марката „{name}“ е в PR #{pr['number']}: {pr['html_url']}\n\nНатисни **Merge** там. После в "
            f"таблото избери марката, попълни червените полета в „Настройки“ и свържи профилите ѝ с локалната "
            f"инсталация. Всичко започва изключено.")


def handle(gh, git, root, number):
    """(comment, closed?) for one issue."""
    issue = gh.issue(number)
    title, body = (issue.get("title") or "").strip(), issue.get("body") or ""
    who = ((issue.get("user") or {}).get("login") or "")
    if not title.lower().startswith("social:"):
        return None
    if gh.permission(who) not in WRITE:
        return "Само хора с право на запис в това хранилище могат да правят това. Нищо не е направено."
    created = datetime.strptime(issue.get("created_at") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                                "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    what = re.sub(r"\s+", " ", title[len("social:"):]).strip()
    m = COMMAND_RE.match(what)
    if m:
        return do_command(root, brand_of(m.group(2)), git, [m.group(1), m.group(2), m.group(3)], who, number)
    if what.lower().startswith("request"):
        data = data_block(body, "request")
        return do_request(root, brand_of(data=data), git, data, body, who, number, created)
    if what.lower().startswith("settings"):
        data = data_block(body, "settings")
        return do_settings(root, brand_of(data=data), gh, git, data, who, number)
    if what.lower().startswith("new brand"):
        return do_new_brand(root, gh, git, data_block(body, "brand"), who, number)
    return f"Не разбирам „{what}“. Отвори го отново от таблото."


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("number", type=int)
    a = ap.parse_args(argv)
    gh = github.from_env()
    if gh is None:
        print("no GITHUB_TOKEN")
        return 2
    try:
        message = handle(gh, Git(brands.ROOT), brands.ROOT, a.number)
    except Exception as e:  # noqa: BLE001 (the person gets told; the run shows the trace)
        gh.comment(a.number, f"Не стана: грешка ({type(e).__name__}). Пробвай пак от таблото или пиши на одобряващия.")
        raise
    if message is None:
        return 0
    gh.comment(a.number, message)
    gh.close_issue(a.number, "completed" if message.startswith("Готово") else "not_planned")
    print(message)
    return 0


if __name__ == "__main__":
    sys.exit(main())
