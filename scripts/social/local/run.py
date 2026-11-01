#!/usr/bin/env python3
"""The publishing check and the control loop on this computer (the scheduled runs call these).

    python run.py start      # Postiz in Docker and the tunnel (at logon)
    python run.py check      # the publishing check, for the brands this computer publishes (hourly, :10)
    python run.py control    # the control loop: /stop-now and /lift (every 5 minutes)
    python run.py channels   # this Postiz's channels
    python run.py status     # who this computer is, what it publishes, the last runs

A brand is this computer's when its settings say `publisher` = this person's GitHub login (setup.py
link asks for it). The code and the data are one clone of the repository (code/), reset to
origin/main before every run, so the check always runs main's code on main's files. The record
stays in state.sqlite; the check pushes its export (ledger.json, the audit trail, the dashboard
data) with this person's GitHub login. Settings come from config.env next to it (setup.py).
"""
import json
import os
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HOME = Path(os.environ.get("PX_SOCIAL_HOME") or Path.home() / "px-social")
CODE = HOME / "code"
PORT = 4007
LOCK_STALE_S = 15 * 60
NO_WINDOW = 0x08000000 if os.name == "nt" else 0           # CREATE_NO_WINDOW


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


def log(what, text):
    """Print, and keep it in logs/<what>.log (pythonw has no console)."""
    d = HOME / "logs"
    d.mkdir(parents=True, exist_ok=True)
    f = d / f"{what}.log"
    if f.exists() and f.stat().st_size > 1_000_000:
        f.replace(d / f"{what}.old.log")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with f.open("a", encoding="utf-8") as fh:
        fh.write(f"{stamp} {text}\n")
    if sys.stdout:
        try:
            print(text, flush=True)
        except (OSError, ValueError):
            pass


def sh(cmd, cwd=None, check=True):
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", creationflags=NO_WINDOW)


class Busy(Exception):
    pass


class Lock:
    """One run at a time (the check and the control loop share Postiz and the record)."""

    def __init__(self):
        self.path = HOME / "run.lock"

    def __enter__(self):
        try:
            if time.time() - self.path.stat().st_mtime > LOCK_STALE_S:
                self.path.unlink()
        except OSError:
            pass
        try:
            os.close(os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
        except FileExistsError:
            raise Busy() from None
        return self

    def __exit__(self, *exc):
        try:
            self.path.unlink()
        except OSError:
            pass


def update_code():
    """main's code and files (the check's data clone is this same clone)."""
    try:
        sh(["git", "-C", str(CODE), "fetch", "-q", "origin", "main"])
        sh(["git", "-C", str(CODE), "reset", "-q", "--hard", "origin/main"])
    except (subprocess.CalledProcessError, OSError) as e:
        log("update", f"could not update the code ({e}); running the copy there is")


def modules(repo):
    os.environ["SOCIAL_REPO"] = repo
    sys.path.insert(0, str(CODE / "scripts"))
    from social import brands, control, github, ledger, postiz, publishing_check, settings  # noqa: E402
    return brands, control, github, ledger, postiz, publishing_check, settings


def my_brands(brands, settings, login):
    """The brands whose settings name this person as their publisher."""
    out = []
    for key, b in brands.BRANDS.items():
        if not (CODE / b["dir"] / "social" / "settings.md").exists():
            continue
        if (settings.load(key, CODE).brand.get("publisher") or "").lower() == (login or "").lower():
            out.append(key)
    return out


def tunnel_up(domain):
    try:
        with urllib.request.urlopen("http://127.0.0.1:4040/api/tunnels", timeout=3) as r:
            return any(domain in (t.get("public_url") or "") for t in json.load(r).get("tunnels", []))
    except (OSError, ValueError):
        return False


def start(quiet=False):
    cfg = read_env(HOME / "config.env")
    try:
        sh(["docker", "compose", "up", "-d"], cwd=HOME / "postiz")
        log("start", "Postiz: up")
    except (subprocess.CalledProcessError, OSError) as e:
        log("start", f"Postiz did not start: is Docker Desktop running? ({e})")
    domain = cfg.get("NGROK_DOMAIN")
    if domain and not tunnel_up(domain):
        flags = (0x00000008 | NO_WINDOW) if os.name == "nt" else 0          # DETACHED_PROCESS
        subprocess.Popen(["ngrok", "http", f"--url={domain}", f"127.0.0.1:{PORT}", "--log", str(HOME / "logs" / "ngrok.log")],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=flags,
                         start_new_session=os.name != "nt")
        log("start", f"tunnel: https://{domain}")
    elif domain:
        log("start", "tunnel: already up")
    return 0


def main(argv=None):
    what = (argv if argv is not None else sys.argv[1:])[:1] or ["status"]
    what = what[0]
    if what == "start":
        return start()
    cfg = read_env(HOME / "config.env")
    repo = cfg.get("REPO") or "ProfitXtraV2/AIContent"
    try:
        with Lock():
            if what in ("check", "control"):
                update_code()
            brands, control, github, ledger, postiz, pc, settings = modules(repo)
            client = postiz.Postiz(f"http://127.0.0.1:{PORT}/api/public/v1", cfg.get("POSTIZ_API_KEY", ""))
            if what == "channels":
                for c in client.integrations():
                    print(json.dumps(c, ensure_ascii=False))
                return 0
            login = cfg.get("GITHUB_LOGIN", "")
            mine = my_brands(brands, settings, login)
            if what == "status":
                print(f"GitHub: @{login or '?'} · repository {repo}")
                print("Publishes: " + (", ".join(brands.BRANDS[k]["name"] for k in mine) or "nothing yet (setup.py link)"))
                for name in ("check", "control", "start"):
                    f = HOME / "logs" / f"{name}.log"
                    if f.exists():
                        print(f"-- {name}: " + (f.read_text(encoding="utf-8").strip().splitlines() or [""])[-1])
                return 0
            if not mine:
                log(what, "no brand names this computer as its publisher: nothing to do")
                return 0
            token = sh(["gh", "auth", "token"]).stdout.strip()
            gh = github.GitHub(token, repo)
            db = ledger.Ledger(HOME / "state.sqlite")
            try:
                if what == "control":
                    out = control.run(db, gh, client, int(cfg.get("PX_SOCIAL_CONTROL_ISSUE") or 0), mine)
                    log("control", json.dumps(out, ensure_ascii=False))
                    return 0
                if what == "check":
                    env = pc.Env(CODE, db, client, gh, pc.Repo(CODE, token), lambda brand: None, enabled_brands=set(mine),
                                 own_secrets={"postiz-key": cfg.get("POSTIZ_API_KEY", "")},
                                 dry_run=cfg.get("DRY_RUN", "0") == "1",
                                 content_format=cfg.get("POSTIZ_CONTENT_FORMAT", "html"), push=True)
                    for key in mine:
                        out = pc.Run(env, key).go()
                        log("check", f"{key}: " + json.dumps(out, ensure_ascii=False)[:2000])
                    return 0
            finally:
                db.close()
    except Busy:
        log(what, "another run is still going: this one is skipped")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
