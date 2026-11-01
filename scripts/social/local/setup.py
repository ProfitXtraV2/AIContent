#!/usr/bin/env python3
"""Social posts on this computer: the setup wizard (it speaks Bulgarian to the person).

    python setup.py                  # the setup; every step is skipped once it is done
    python setup.py team-code [--from <folder of a working Postiz>] [--repo owner/name]
    python setup.py link             # link this Postiz's channels to a brand's accounts (again)
    python setup.py tasks            # the scheduled runs, again

install.ps1 runs it after installing Git, Python, GitHub CLI, ngrok and Docker Desktop. What is
personal stays in %USERPROFILE%\\px-social (or PX_SOCIAL_HOME), never in the repository:
  config.env     the Postiz key, the tunnel's address, the GitHub login
  team.json      the team's app keys, from the team code one person shares (`team-code`)
  postiz/        Postiz in Docker (gitroomhq/postiz-docker-compose, pinned, and our override)
  code/          the repository, reset to main before every run
  state.sqlite   the publishing check's record;  logs/  what each run did
Linking a brand opens the issue "social: settings <brand>" (the same one the dashboard opens):
the brand's `publisher` becomes this person's login and its accounts get this Postiz's channel
IDs. Merging that PR is what makes this computer the one that publishes the brand.
"""
import argparse
import base64
import json
import os
import re
import secrets
import subprocess
import sys
import tempfile
import time
import urllib.request
import webbrowser
from pathlib import Path

HOME = Path(os.environ.get("PX_SOCIAL_HOME") or Path.home() / "px-social")
REPO = os.environ.get("PX_SOCIAL_REPO") or "ProfitXtraV2/AIContent"
CODE = HOME / "code"
POSTIZ = HOME / "postiz"
PORT = 4007
COMPOSE_REPO = "https://github.com/gitroomhq/postiz-docker-compose"
COMPOSE_COMMIT = "dd4969e"                    # the compose the team's first Postiz ran (2026-10)
TEAM_KEYS = ("INSTAGRAM_APP_ID", "INSTAGRAM_APP_SECRET", "FACEBOOK_APP_ID", "FACEBOOK_APP_SECRET",
             "LINKEDIN_CLIENT_ID", "LINKEDIN_CLIENT_SECRET", "X_API_KEY", "X_API_SECRET")
NETWORK_OF = {"instagram": "instagram", "instagram-standalone": "instagram", "facebook": "facebook", "x": "x",
              "linkedin-page": "linkedin-page", "linkedin": "linkedin-profile"}
OVERRIDE = """# Written by scripts/social/local/setup.py: Postiz on this computer for the social posts.
# The values come from .env next to this file (never committed, never shared).
services:
  postiz:
    image: "${POSTIZ_IMAGE:-ghcr.io/gitroomhq/postiz-app:latest}"
    ports: !override
      - "127.0.0.1:%(port)d:5000"
    environment:
      MAIN_URL: "${PUBLIC_URL}"
      FRONTEND_URL: "${PUBLIC_URL}"
      NEXT_PUBLIC_BACKEND_URL: "${PUBLIC_URL}/api"
      JWT_SECRET: "${JWT_SECRET}"
      DISABLE_REGISTRATION: "${DISABLE_REGISTRATION:-false}"
      # the tunnel's address is a public suffix (ngrok-free.dev): the browser refuses a cookie for
      # it, so Postiz also sends the login in a header
      NOT_SECURED: "${NOT_SECURED:-}"
      API_LIMIT: 600
%(keys)s
  temporal-admin-tools:
    profiles: [debug]
  temporal-ui:
    profiles: [debug]
""" % {"port": PORT, "keys": "\n".join(f'      {k}: "${{{k}:-}}"' for k in TEAM_KEYS)}


# --- small helpers ------------------------------------------------------------------------------

def say(text=""):
    print(text, flush=True)


def step(n, text):
    say(f"\n== {n}. {text}")


def ask(prompt, default=""):
    got = input(f"{prompt}{f' [{default}]' if default else ''}: ").strip()
    return got or default


def yes(prompt, default=True):
    got = input(f"{prompt} ({'Д/н' if default else 'д/Н'}): ").strip().lower()
    return default if not got else got in ("д", "да", "y", "yes")


def run(cmd, cwd=None, check=True, capture=True, env=None):
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=capture, text=True, encoding="utf-8",
                          errors="replace", env=env)


def read_env(path):
    out = {}
    try:
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                out[k.strip()] = v.strip()
    except OSError:
        pass
    return out


def write_env(path, values, header):
    lines = [f"# {header}", "# Stays on this computer: never paste these values in a chat or commit them."]
    lines += [f"{k}={v}" for k, v in values.items()]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def config():
    return read_env(HOME / "config.env")


def save_config(**changes):
    values = dict(config(), **{k: str(v) for k, v in changes.items()})
    write_env(HOME / "config.env", values, "Social posts on this computer (scripts/social/local/setup.py)")
    return values


# --- the team code: the shared app keys, copied once from a working setup --------------------------

def encode_team(team):
    return "PXS1-" + base64.urlsafe_b64encode(json.dumps(team, separators=(",", ":")).encode("utf-8")).decode("ascii").rstrip("=")


def decode_team(code):
    code = re.sub(r"\s+", "", str(code or ""))
    if not code.startswith("PXS1-"):
        raise ValueError("това не е код на екипа (започва с PXS1-)")
    raw = code[5:] + "=" * (-len(code[5:]) % 4)
    try:
        team = json.loads(base64.urlsafe_b64decode(raw.encode("ascii")).decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        raise ValueError("кодът е непълен: копирай го целия") from None
    if not isinstance(team, dict) or not team.get("repo"):
        raise ValueError("кодът няма хранилище")
    team["env"] = {k: v for k, v in (team.get("env") or {}).items() if k in TEAM_KEYS}
    return team


def team_from(folder, repo):
    """The team code's content from a working Postiz folder: its app keys and its Postiz image."""
    env = read_env(Path(folder) / ".env")
    image = ""
    override = Path(folder) / "docker-compose.override.yaml"
    if override.exists():
        m = re.search(r"^\s*image:\s*\"?([^\s\"$]+)", override.read_text(encoding="utf-8"), re.M)
        image = m.group(1) if m else ""
    return {"v": 1, "repo": repo, "compose_commit": COMPOSE_COMMIT, "postiz_image": image or env.get("POSTIZ_IMAGE", ""),
            "env": {k: env[k] for k in TEAM_KEYS if env.get(k)}}


def team():
    try:
        return json.loads((HOME / "team.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


# --- the steps ------------------------------------------------------------------------------------

def step_team():
    step(1, "Кодът на екипа")
    if team():
        say("Вече е поставен.")
        return team()
    say("Поискай „кода на екипа“ от колега, който вече публикува (кодът се взима с\n"
        "`python setup.py team-code`). В него са общите ключове на приложенията ни. Не го пращай публично.")
    while True:
        try:
            got = decode_team(input("Постави кода тук и натисни Enter: "))
            break
        except ValueError as e:
            say(f"  {e}. Опитай пак.")
    HOME.mkdir(parents=True, exist_ok=True)
    (HOME / "team.json").write_text(json.dumps(got, ensure_ascii=False, indent=2), encoding="utf-8")
    say("Записан.")
    return got


def github_login():
    return run(["gh", "api", "user", "--jq", ".login"]).stdout.strip()


def step_github(repo):
    step(2, "GitHub")
    if run(["gh", "auth", "status"], check=False).returncode != 0:
        say("Ще се отвори браузърът: влез в GitHub и потвърди кода, който виждаш тук.")
        run(["gh", "auth", "login", "--web", "-h", "github.com", "-p", "https"], capture=False)
    run(["gh", "auth", "setup-git"], check=False)              # git pushes the check's record with this login
    login = github_login()
    perm = run(["gh", "api", f"repos/{repo}/collaborators/{login}/permission", "--jq", ".permission"], check=False).stdout.strip()
    say(f"Влязъл си като @{login} (право: {perm or 'няма'}).")
    if perm not in ("admin", "maintain", "write"):
        say("  ⚠ Нямаш право Write в хранилището. Поискай го от собственика: без него не можеш да одобряваш и\n"
            "    публикуваш. Продължавам с настройката.")
    save_config(GITHUB_LOGIN=login, REPO=repo)
    return login


def step_tunnel():
    step(3, "Адрес в интернет (ngrok)")
    cfg = config()
    if cfg.get("NGROK_DOMAIN"):
        say(f"Вече е настроен: https://{cfg['NGROK_DOMAIN']}")
        return cfg["NGROK_DOMAIN"]
    say("Instagram трябва да може да вземе снимките от твоя компютър. За това ти трябва безплатен ngrok акаунт:\n"
        "  1) Влез или се регистрирай в ngrok (отваря се сега).\n"
        "  2) Копирай „Authtoken“ и го постави тук.\n"
        "  3) В „Domains“ натисни „+ New Domain“ (безплатен е) и копирай адреса му.")
    webbrowser.open("https://dashboard.ngrok.com/get-started/your-authtoken")
    token = ask("Authtoken")
    run(["ngrok", "config", "add-authtoken", token])
    webbrowser.open("https://dashboard.ngrok.com/domains")
    domain = re.sub(r"^https?://|/.*$", "", ask("Адресът (напр. нещо-нещо.ngrok-free.dev)")).lower()
    save_config(NGROK_DOMAIN=domain)
    return domain


def step_postiz(domain, team_data):
    step(4, "Postiz (инструментът, който публикува)")
    if not (POSTIZ / ".git").exists():
        say("Свалям Postiz…")
        run(["git", "clone", "-q", COMPOSE_REPO, str(POSTIZ)])
        run(["git", "-C", str(POSTIZ), "checkout", "-q", team_data.get("compose_commit") or COMPOSE_COMMIT])
    env = read_env(POSTIZ / ".env")
    env.update({"PUBLIC_URL": f"https://{domain}", "JWT_SECRET": env.get("JWT_SECRET") or secrets.token_hex(32),
                "NOT_SECURED": "true", "DISABLE_REGISTRATION": env.get("DISABLE_REGISTRATION", "false")})
    if team_data.get("postiz_image"):
        env["POSTIZ_IMAGE"] = team_data["postiz_image"]
    env.update(team_data.get("env") or {})
    write_env(POSTIZ / ".env", env, "Postiz on this computer (scripts/social/local/setup.py)")
    (POSTIZ / "docker-compose.override.yaml").write_text(OVERRIDE, encoding="utf-8")
    say("Пускам Postiz в Docker (първия път сваля около 2 GB, може да отнеме 5–10 минути)…")
    run(["docker", "compose", "up", "-d"], cwd=POSTIZ, capture=False)
    for _ in range(120):
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{PORT}/", timeout=5)
            say("Postiz работи.")
            return
        except OSError:
            time.sleep(5)
    say("  ⚠ Postiz още не отговаря. Изчакай малко и пусни `python setup.py` отново.")
    sys.exit(1)


def step_start():
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import run as runner                                       # noqa: E402  (next to this file)
    runner.start(quiet=True)


def step_meta(domain):
    step(5, "Meta (Instagram и Facebook)")
    say("Изпрати тези два адреса на човека, който управлява Meta приложението ни, за да ги добави веднъж\n"
        "(Meta for Developers → приложението → Instagram и Facebook Login → Valid OAuth Redirect URIs):\n"
        f"  https://{domain}/integrations/social/instagram-standalone\n"
        f"  https://{domain}/integrations/social/facebook\n"
        "Ако приложението още не е публично (Live), там се добавят и твоите профили като тестери.")
    input("Натисни Enter, когато е готово (може и по-късно: тогава пусни `python setup.py` отново)… ")


def step_channels(domain):
    step(6, "Профилите в Postiz")
    say(f"Отваря се Postiz: https://{domain}\n"
        "  1) Първия път натисни „Sign up“ и си направи акаунт (той е само на този компютър).\n"
        "  2) Натисни „Add Channel“ и свържи профилите, които ще публикуваш (Instagram, Facebook…).")
    webbrowser.open(f"https://{domain}")
    input("Натисни Enter, когато профилите са свързани… ")


def postiz_client(key):
    sys.path.insert(0, str(CODE / "scripts"))
    from social import postiz                                  # noqa: E402
    return postiz.Postiz(f"http://127.0.0.1:{PORT}/api/public/v1", key)


def step_api_key(domain):
    step(7, "Ключът за Postiz")
    key = config().get("POSTIZ_API_KEY")
    if key:
        try:
            postiz_client(key).integrations()
            say("Вече е поставен и работи.")
            return key
        except Exception:                                      # noqa: BLE001
            say("Ключът, който е записан, не работи. Постави нов.")
    say("В Postiz отвори Settings → Public API и копирай ключа (отваря се сега).")
    webbrowser.open(f"https://{domain}/settings")
    while True:
        key = ask("Ключът")
        try:
            got = postiz_client(key).integrations()
            say(f"Работи: виждам {len(got)} профил(а).")
            save_config(POSTIZ_API_KEY=key)
            return key
        except Exception as e:                                 # noqa: BLE001
            say(f"  Не работи ({type(e).__name__}). Провери, че е целият ключ, и опитай пак.")


def matches(accounts, channels):
    """{account_id: channel} for every account whose network has exactly one channel here, and
    {account_id: [channels]} for the ones that have several (the person chooses)."""
    by_net = {}
    for c in channels:
        net = NETWORK_OF.get(str(c.get("identifier") or "").lower())
        if net and not c.get("disabled"):
            by_net.setdefault(net, []).append(c)
    sure, choose = {}, {}
    for a in accounts:
        found = by_net.get(a.get("network"), [])
        current = [c for c in found if c["id"] == a.get("postiz_channel_id")]
        if current or len(found) == 1:
            sure[a["account_id"]] = (current or found)[0]
        elif found:
            choose[a["account_id"]] = found
    return sure, choose


def settings_issue_body(brand_key, brand_changes, account_changes):
    data = {"brand": brand_key, "brand_changes": brand_changes, "account_changes": account_changes}
    block = json.dumps(data, ensure_ascii=False).replace("-->", "--\\u003e")
    lines = [f"- {k}: {v}" for k, v in brand_changes.items()]
    lines += [f"- {a} · {k}: {v}" for a, f in account_changes.items() for k, v in f.items()]
    return (f"<!-- social:settings {block} -->\n"
            "**Промяна на настройките (от локалната инсталация):**\n" + "\n".join(lines) +
            "\n\nСлед около минута GitHub Action отговаря тук с линк към PR с промяната: натисни **Merge** в него, "
            "за да влезе в сила.\n")


def link(login=None, key=None, repo=None):
    step(8, "Марките, които публикува този компютър")
    cfg = config()
    login, key, repo = login or cfg.get("GITHUB_LOGIN") or github_login(), key or cfg["POSTIZ_API_KEY"], repo or cfg.get("REPO") or REPO
    sys.path.insert(0, str(CODE / "scripts"))
    from social import brands, settings as settingsmod        # noqa: E402
    keys = [k for k in brands.BRANDS if (CODE / brands.BRANDS[k]["dir"] / "social" / "settings.md").exists()]
    if not keys:
        say("Още няма марки с настройки за постове.")
        return
    loaded = {k: settingsmod.load(k, CODE) for k in keys}
    for i, k in enumerate(keys, 1):
        who = loaded[k].brand.get("publisher") or "никой"
        say(f"  {i}) {brands.BRANDS[k]['name']} ({brands.BRANDS[k]['site']}) · публикува: {who}")
    picked = ask("Кои ще публикуваш от този компютър? Номерата, със запетая")
    chosen = [keys[int(x) - 1] for x in re.findall(r"\d+", picked) if 0 < int(x) <= len(keys)]
    channels = postiz_client(key).integrations()
    for k in chosen:
        s = loaded[k]
        say(f"\n{brands.BRANDS[k]['name']}:")
        other = s.brand.get("publisher")
        if other and other.lower() != login.lower():
            say(f"  ⚠ Сега я публикува @{other}. Ако продължиш, компютърът на @{other} спира да я публикува, щом\n"
                f"    PR-ът се мърджне. Постовете, които вече са в Postiz на @{other}, остават там: нека @{other} ги прегледа.")
            if not yes("  Продължавам ли?", default=False):
                continue
        sure, choose = matches(s.accounts, channels)
        for aid, options in choose.items():
            for i, c in enumerate(options, 1):
                say(f"    {i}) {c.get('name')} ({c.get('identifier')})")
            n = ask(f"  Кой от тези е {aid}? Номерът (Enter: никой)")
            if n.isdigit() and 0 < int(n) <= len(options):
                sure[aid] = options[int(n) - 1]
        account_changes = {}
        for a in s.accounts:
            c = sure.get(a["account_id"])
            if c and c["id"] != a.get("postiz_channel_id"):
                account_changes[a["account_id"]] = {"postiz_channel_id": c["id"]}
                say(f"  {a['account_id']} ← {c.get('name')} ({c.get('identifier')})")
            elif not c:
                say(f"  {a['account_id']}: тук няма такъв профил ({a['network']}); остава както е")
        brand_changes = {} if (s.brand.get("publisher") or "").lower() == login.lower() else {"publisher": login}
        if not brand_changes and not account_changes:
            say("  Всичко вече е свързано.")
            continue
        if not yes("  Да запиша ли това в настройките на марката?"):
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
            fh.write(settings_issue_body(k, brand_changes, account_changes))
        try:
            url = run(["gh", "issue", "create", "--repo", repo, "--title", f"social: settings {k}", "--body-file", fh.name]).stdout.strip()
        finally:
            os.unlink(fh.name)
        say(f"  Готово: {url}\n  След около минута там идва линк към PR: натисни Merge. После в таблото включи профилите\n"
            f"  (Включен: да), щом видиш тестов пост на живо.")


def step_control_issue(repo):
    if config().get("PX_SOCIAL_CONTROL_ISSUE"):
        return
    got = run(["gh", "issue", "list", "--repo", repo, "--search", 'in:title "Social control"', "--state", "open",
               "--json", "number", "--jq", ".[0].number"], check=False).stdout.strip()
    if got.isdigit():
        save_config(PX_SOCIAL_CONTROL_ISSUE=got)


def tasks():
    step(9, "Да работи само")
    pyw = Path(sys.executable).with_name("pythonw.exe")
    py = str(pyw if pyw.exists() else Path(sys.executable))
    runner = CODE / "scripts" / "social" / "local" / "run.py"
    if os.name != "nt":
        say("Добави в crontab:\n"
            f"  10 * * * * {sys.executable} {runner} check\n  */5 * * * * {sys.executable} {runner} control\n"
            f"  @reboot {sys.executable} {runner} start")
        return
    for name, schedule, what in (("check", ["/SC", "HOURLY", "/ST", "00:10"], "check"),
                                 ("control", ["/SC", "MINUTE", "/MO", "5"], "control")):
        run(["schtasks", "/Create", "/F", "/TN", f"PX Social {name}", *schedule, "/TR", f'"{py}" "{runner}" {what}'])
    startup = Path(os.environ["APPDATA"]) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup" / "px-social-start.cmd"
    startup.write_text(f'@echo off\r\nstart "" "{py}" "{runner}" start\r\n', encoding="utf-8")
    say("Проверката тръгва всеки час в :10, спирането се чете на всеки 5 минути, а Postiz и адресът тръгват,\n"
        "щом влезеш в Windows. Компютърът трябва да е включен, когато постовете трябва да излязат.")


def setup():
    say("Постове в социалните мрежи: настройка на този компютър. Всяка готова стъпка се пропуска.")
    team_data = step_team()
    repo = team_data.get("repo") or REPO
    login = step_github(repo)
    domain = step_tunnel()
    step_postiz(domain, team_data)
    step_start()
    step_meta(domain)
    step_channels(domain)
    key = step_api_key(domain)
    link(login, key, repo)
    step_control_issue(repo)
    tasks()
    say("\nГотово. `python run.py status` показва какво публикува този компютър.")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("what", nargs="?", default="setup", choices=["setup", "team-code", "link", "tasks"])
    ap.add_argument("--from", dest="source", help="team-code: the folder of a working Postiz (its .env)")
    ap.add_argument("--repo", default=REPO)
    a = ap.parse_args(argv)
    if a.what == "team-code":
        if not a.source:
            say("Кажи папката на работещия Postiz: --from <папка>")
            return 2
        say("Кодът на екипа (прати го само лично, не в общ чат: в него са ключовете на приложенията):\n")
        say(encode_team(team_from(a.source, a.repo)))
        return 0
    if a.what == "link":
        link()
        return 0
    if a.what == "tasks":
        tasks()
        return 0
    setup()
    return 0


if __name__ == "__main__":
    sys.exit(main())
