#!/usr/bin/env python3
"""The publishing check (product spec F11; tech spec flow 4). Runs in the guest at minute :10 of
every hour, under `flock -w 240 /run/px-social.lock`, shared with the control loop.

    python3 scripts/social/publishing_check.py [--brand vsichkikazina] [--dry-run] [--no-push]
                                              [--fake-postiz [<state.json>]]
    python3 scripts/social/publishing_check.py --dry-run --fake-postiz --replay vk-0300

It is the only part of the product that holds the Postiz key. It follows fixed rules only: it
writes no text and takes no instructions from any page, PR or post text. It reads a data clone
of AIContent main (as data, never executed), GitHub's record of merges, the publisher's record
(read only), the brand's own live pages and Postiz.

Steps: 1 heartbeat and pull · 2 key scan · 3 settings · 4 Postiz sync · 5 approvals ·
6 commands · 7 go-live · 8 article versions · 9 pull-backs · 10 planning · 11 hand-over ·
12 expiry and markers · 13 write SQLite, export, dashboard data, commit.

DRY_RUN=1 (or --dry-run): reads everything, plans and logs the hand-overs, creates and deletes
nothing in Postiz.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_library  # noqa: E402
from social import (board, brands, build_social_dashboard as dash, checks, github, handover, ids,  # noqa: E402
                    ledger as ledgermod, links, liveness, operators, pack as packmod, planner, postiz,
                    secret_scan, settings as settingsmod)

BRANCH_RE = re.compile(rf"^social/(?P<prefix>[a-z]{{2}})/(?P<pack>{ids.SOURCE}-p\d+)(?:-fix-(?P<fix>\d+))?$")
FINAL = {"rejected", "published", "failed", "expired", "cancelled", "not_from_pack"}
RECOMPUTED = {"waiting_for_article", "planned", "held"}
HANDOVER_HOLDS = {"held:live_page_differs", "held:no_live_link", "held:no_visual"}
NO_SLOT = {"held", "needs_fix", "in_fix_pr", "article_changed", "waiting_for_article", "cancelled", "expired",
           "failed", "rejected"}
RULE_CHECKS = {"length", "hashtags", "link", "compliance", "advertising", "numbers", "verify", "instagram-url"}
SYNC_BACK, SYNC_AHEAD = timedelta(hours=48), timedelta(hours=4)
LATE = timedelta(minutes=60)
FIX_PR_EXPIRY = timedelta(days=30)
FOLLOWUP_EXPIRY = timedelta(days=60)
WAITING_LONG = timedelta(days=14)
WAITING_LONG_FOR_ARTICLE = timedelta(days=30)
MAX_RETRIES = 2
LOGIN_HOLD = timedelta(hours=6)
HANDOVER_KEYS = {"postiz-key", "github-app-key"}
PUBLISHER_REPO = os.environ.get("PX_SOCIAL_PUBLISHER_REPO", "ProfitXtraV2/WebPortals")


def iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") if dt else None


def parse(ts):
    if not ts:
        return None
    if isinstance(ts, datetime):
        return ts
    t = str(ts).strip().replace("Z", "")
    for fmt, n in (("%Y-%m-%dT%H:%M:%S", 19), ("%Y-%m-%d %H:%M", 16), ("%Y-%m-%dT%H:%M", 16), ("%Y-%m-%d", 10)):
        try:
            return datetime.strptime(t.split(".")[0][:n], fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def sha256(data):
    return hashlib.sha256(data if isinstance(data, bytes) else str(data).encode("utf-8")).hexdigest()


# --- the data clone -----------------------------------------------------------------------

class Repo:
    """The data clone of AIContent main. Only git and file reads run on it; nothing in it is
    executed. It is reset to origin/main at every run, so the check's own exports are always
    rebuilt from SQLite."""

    OUT = ("social", "docs/data/social")

    def __init__(self, root, token=None):
        self.root, self.token = Path(root), token

    def _git(self, *args, check=True, text=True):
        env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
        if self.token:
            env.update({"PX_GIT_TOKEN": self.token,
                        "GIT_ASKPASS": str(Path(__file__).resolve().parent / "deploy" / "git-askpass.sh")})
        decode = {"encoding": "utf-8", "errors": "replace"} if text else {}    # git writes UTF-8 whatever the locale
        return subprocess.run(["git", *args], cwd=self.root, capture_output=True, check=check, timeout=120, env=env,
                              **decode)

    def pull(self):
        try:
            self._git("fetch", "-q", "origin", "main")
            self._git("reset", "-q", "--hard", "origin/main")
            return True
        except (OSError, subprocess.SubprocessError):
            return False

    def head(self):
        try:
            return self._git("rev-parse", "HEAD").stdout.strip()
        except (OSError, subprocess.SubprocessError):
            return None

    def files_at(self, sha, rel_dir):
        """{path inside rel_dir: bytes} at a commit, or None when the commit is not here."""
        try:
            names = self._git("ls-tree", "-r", "--name-only", sha, "--", rel_dir).stdout.split("\n")
            out = {}
            for name in [n for n in names if n]:
                out[name[len(rel_dir) + 1:]] = self._git("show", f"{sha}:{name}", text=False).stdout
            return out or None
        except (OSError, subprocess.SubprocessError):
            return None

    def diff_since(self, sha):
        try:
            return self._git("log", "-p", "--no-color", f"{sha}..HEAD").stdout[:20_000_000]
        except (OSError, subprocess.SubprocessError):
            return ""

    def commit_and_push(self, paths, message):
        try:
            self._git("add", "--", *[str(p) for p in paths])
            if not self._git("diff", "--cached", "--quiet", check=False).returncode:
                return True                                   # nothing changed
            self._git("-c", "user.name=px-publishing-check[bot]",
                      "-c", "user.email=px-publishing-check[bot]@users.noreply.github.com",
                      "commit", "-q", "-m", message)
            for _ in range(3):
                if self._git("push", "-q", "origin", "HEAD:main", check=False).returncode == 0:
                    return True
                self._git("fetch", "-q", "origin", "main")
                if self._git("rebase", "-q", "origin/main", check=False).returncode != 0:
                    self._git("rebase", "--abort", check=False)
                    return False
            return False
        except (OSError, subprocess.SubprocessError):
            return False


class Env:
    """What the check reaches. Tests and the replay pass fakes for every part."""

    def __init__(self, root, db, postiz_client, gh, repo, publisher_record, site_get=liveness.http_get, now=None,
                 enabled_brands=(), own_secrets=None, dry_run=False, content_format="html",
                 push=True):
        self.root, self.db, self.postiz, self.gh, self.repo = Path(root), db, postiz_client, gh, repo
        self.publisher_record, self.site_get = publisher_record, site_get
        self.fixed_clock = now is not None
        self.now = now or datetime.now(timezone.utc)
        self.enabled_brands = set(enabled_brands)
        self.own_secrets = own_secrets or {}
        self.dry_run, self.content_format, self.push = dry_run, content_format, push


# --- one run for one brand ----------------------------------------------------------------

class Run:
    def __init__(self, env, brand_key):
        self.env, self.db, self.brand_key = env, env.db, brand_key
        self.root = env.root
        self.b = brands.brand(brand_key)
        self.rel_social = f"{self.b['dir']}/social"
        self.now, self.iso = env.now, iso(env.now)
        self.banners, self.no_handover, self.events = [], [], []
        self.github_ok, self.tool_ok = True, False
        self.settings, self.channels, self.ops, self.record = None, {}, [], {}
        self.site = liveness.Site(brand_key, env.site_get)
        self._items, self._articles = {}, {}
        self.team = github.Team(env.gh)               # who approves: write access to the repository
        self.settings_accepted = False

    # helpers
    def banner(self, kind, text, level="warn"):
        b = {"kind": kind, "text": text, "level": level}
        if b not in self.banners:
            self.banners.append(b)

    def audit(self, rec, event, **data):
        self.db.audit(self.iso, self.brand_key, rec["post_id"] if rec else None, event, **data)

    def set_state(self, rec, state, reason="", event=None, **data):
        before = (rec.get("state"), rec.get("reason", ""))
        rec["state"], rec["reason"] = state, reason
        if state == "held" and before != (state, reason):
            rec["held_since_utc"] = self.iso
        elif state != "held":
            rec.pop("held_since_utc", None)
        if "missing_lines" in data:
            rec["missing_lines"] = data["missing_lines"]
        elif reason != "held:live_page_differs":
            rec["missing_lines"] = []
        if state in NO_SLOT:
            rec["planned_slot_utc"] = None
        rec["updated_utc"] = self.iso
        if before != (state, reason) or event:
            self.audit(rec, event or "state", state=state, reason=reason, previous=before[0], **data)
        self.db.save(rec)

    def mark(self, rec, marker):
        if marker not in rec.setdefault("markers", []):
            rec["markers"].append(marker)
            self.audit(rec, "marker", marker=marker)

    def _item(self, slug):
        if slug not in self._items:
            item, text = build_library.load_item(self.root, self.brand_key, slug) if slug else (None, None)
            self._items[slug], self._articles[slug] = item, text or ""
        return self._items[slug]

    def check_ctx(self, pack):
        src = pack["meta"].get("source") or {}
        item = self._item(src.get("slug")) if src.get("slug") else None
        return checks.Context(self.brand_key, self.settings, self.ops, item,
                              self._articles.get(src.get("slug"), "") if item else "")

    def _retire(self, rec):
        if rec.get("handover"):
            rec.setdefault("handover_history", []).append(rec["handover"])
        rec["handover"] = None

    def _delete(self, rec, why):
        """Pull a post back from the tool. False when the tool could not be reached."""
        h = rec.get("handover") or {}
        pid = h.get("postiz_post_id")
        if pid and not h.get("dry_run"):
            try:
                self.env.postiz.delete(pid)
            except postiz.PostizError as e:
                self.audit(rec, "pull-back failed", detail=str(e), why=why)
                rec["pullback_pending"] = True
                self.db.save(rec)
                return False
        self.audit(rec, "pulled back from the tool" + (" (dry run)" if h.get("dry_run") else ""), why=why,
                   postiz_post_id=pid)
        rec.pop("pullback_pending", None)
        self._retire(rec)
        self.db.save(rec)
        return True

    def paused(self):
        """Why the brand cannot publish now, or None (F7)."""
        if not self.settings.brand_ok:
            return "the brand settings have errors"
        if not self.settings.brand["social"]:
            return "social is off"
        sw = self.db.switches(self.brand_key)
        on = [name for name, flag in (("settings", self.settings.brand["pause"]), ("stop now", sw["stop_now"]),
                                      ("tool", sw["tool_pause"])) if flag]
        return ("paused: " + ", ".join(on)) if on else None

    # 1 + 2: heartbeat, pull, key scan
    def step_keys(self):
        head = self.env.repo.head()
        last = self.db.get(f"scan_sha:{self.brand_key}")
        found = []
        if last and head and last != head:
            found = secret_scan.scan_text(self.env.repo.diff_since(last), "new commits on main", self.env.own_secrets)
        if head:
            self.db.set(f"scan_sha:{self.brand_key}", head)
        leaked = self.db.get("leaked_secrets", {})
        for f in found:
            if f["kind"] in self.env.own_secrets:
                leaked[f["kind"]] = sha256(self.env.own_secrets[f["kind"]])[:16]
            else:
                self.banner("key", f"a {f['kind']} was found in {f['where']}: replace that key", "red")
        self.db.set("leaked_secrets", leaked)
        for kind, fp in leaked.items():
            current = self.env.own_secrets.get(kind)
            if current and sha256(current)[:16] == fp:      # still the leaked value: not replaced yet
                self.banner("key", f"replace the {kind}: it was found in the repository", "red")
                if kind in HANDOVER_KEYS:
                    self.no_handover.append(f"the {kind} leaked")

    # 3: settings, accepted only from a merge by someone of the team (boundary 4)
    def step_settings(self):
        rel = f"{self.rel_social}/settings.md"
        f = self.root / rel
        current = f.read_bytes() if f.exists() else b""
        file_sha = sha256(current)
        acc = self.db.accepted_settings(self.brand_key)
        text = acc["text"] if acc else None
        if acc and acc["file_sha256"] == file_sha:
            pass
        elif not self.github_ok or self.env.gh is None:
            if current and (not acc or acc["file_sha256"] != file_sha):
                self.banner("settings", "settings changed, but GitHub could not be reached to confirm who merged them")
        else:
            found = self._settings_pr(rel, file_sha)
            if found:
                text = current.decode("utf-8")
                who = found["merged_by"]["login"]
                self.db.accept_settings(self.brand_key, found["merge_commit_sha"], file_sha, who, self.iso, text)
                self.db.audit(self.iso, self.brand_key, None, "settings accepted", pr=found["number"],
                              merged_by=who, merge_sha=found["merge_commit_sha"], file_sha256=file_sha)
            elif current and self.github_ok:
                self.banner("settings", "settings changed without approval: the earlier settings stay in force", "red")
                self.db.audit(self.iso, self.brand_key, None, "settings rejected", file_sha256=file_sha,
                              reason="no PR merged by someone with write access has this file")
        self.settings = settingsmod.parse(text or "", self.brand_key)
        self.settings_accepted = text is not None
        if text is None:
            self.settings.errors = [{"scope": "brand", "message": "no settings accepted yet: settings.md counts only "
                                     "through a PR merged by someone with write access to the repository"}]
        if self.settings.brand["social"] and self.brand_key not in self.env.enabled_brands:
            self.settings.errors.append({"scope": "brand", "message": "social is on in settings.md, but the brand "
                                         "is not switched on in the guest yet (rollout step 10)"})
        self.ops = operators.current(self.brand_key, self.root, self.settings.brand["operator_names_manual"])
        self.db.set_switches(self.brand_key, self.iso, settings_pause=bool(self.settings.brand["pause"]))

    def _settings_pr(self, rel, file_sha):
        try:
            for c in self.env.gh.commits(rel)[:20]:
                for simple in self.env.gh.commit_pulls(c["sha"]):
                    if not simple.get("merged_at") or (simple.get("base") or {}).get("ref", "main") != "main":
                        continue
                    pr = self.env.gh.pull(simple["number"])            # merged_by is only on the full PR
                    if not self.team.merged(pr):
                        continue
                    at = self.env.gh.file_at(rel, pr["merge_commit_sha"])
                    if at is not None and sha256(at) == file_sha:
                        return pr
        except github.GitHubError:
            self.github_ok = False
            self.banner("github", "GitHub could not be reached: no new hand-overs this hour")
        return None

    # 4: Postiz sync (F6, F8, F9)
    def step_sync(self):
        try:
            chans = self.env.postiz.integrations()
            listed = self.env.postiz.posts(self.now - SYNC_BACK, self.now + SYNC_AHEAD)
        except postiz.PostizError as e:
            self.tool_ok = False
            self.no_handover.append("the publishing tool could not be reached")
            if e.kind == "auth":
                self.banner("tool", "the publishing tool refused the API key: replace POSTIZ_API_KEY in the guest", "red")
            else:
                self.banner("tool", "the publishing tool could not be reached this hour")
            self.channels = {c["id"]: c for c in self.db.get(f"channels:{self.brand_key}", [])}
            return
        self.tool_ok = True
        self.channels = {c["id"]: c for c in chans}
        self.db.set(f"channels:{self.brand_key}", chans)
        settingsmod.check_channels(self.settings, set(self.channels))
        for a in self.settings.accounts:
            ch = self.channels.get(a["postiz_channel_id"])
            if a["active"] and ch and ch.get("identifier") not in postiz.PROVIDERS.get(a["network"], ()):
                self.settings.errors.append({"scope": a["account_id"], "message": f"{a['account_id']}: channel "
                                             f"{ch['id']} is a {ch.get('identifier')} channel, not {a['network']}"})
        by_id = {p["id"]: p for p in listed}
        records = self.db.posts(self.brand_key)
        for r in records:                                  # intents left by a stop between intent and create
            h = r.get("handover") or {}
            if h.get("intent_utc") and not h.get("postiz_post_id"):
                match = next((p for p in listed if p["channel_id"] == h["channel_id"] and parse(p["date"]) == parse(h["slot_utc"])
                              and postiz.content_hash(p["content"]) == h["content_hash"]), None)
                if match:
                    h.update({"postiz_post_id": match["id"], "utc": h["intent_utc"]})
                    self.set_state(r, "scheduled", "", event="hand-over found in the tool after a stop",
                                   postiz_post_id=match["id"])
                else:
                    r["handover"] = None
                    self.audit(r, "hand-over intent cleared: nothing was created")
                    self.db.save(r)
        handed = [r for r in records if r["state"] == "scheduled" and (r.get("handover") or {}).get("postiz_post_id")]
        if any(r["handover"]["postiz_post_id"] not in by_id and not r["handover"].get("dry_run") for r in handed):
            try:
                for p in self.env.postiz.posts(self.now - timedelta(days=30), self.now + timedelta(days=90)):
                    by_id.setdefault(p["id"], p)
            except postiz.PostizError:
                self.tool_ok = False
                self.no_handover.append("the publishing tool could not be reached")
                return
        for r in handed:
            self._sync_one(r, by_id.get(r["handover"]["postiz_post_id"]))
        ours = set()
        for r in self.db.posts(self.brand_key):
            for h in [r.get("handover") or {}] + (r.get("handover_history") or []):
                if h.get("postiz_post_id"):
                    ours.add(h["postiz_post_id"])
            if r.get("postiz_id"):
                ours.add(r["postiz_id"])
        accounts = {a["postiz_channel_id"]: a for a in self.settings.accounts if a["postiz_channel_id"]}
        for p in listed:
            if p["channel_id"] in accounts and p["id"] not in ours:
                a = accounts[p["channel_id"]]
                rec = {"post_id": f"tool-{p['id']}", "brand": self.brand_key, "pack_id": None, "postiz_id": p["id"],
                       "account_id": a["account_id"], "network": a["network"], "markers": [], "retries": 0,
                       "state": "not_from_pack", "reason": "", "planned_slot_utc": iso(parse(p["date"])),
                       "published_utc": iso(parse(p["date"])) if p["state"] == "PUBLISHED" else None,
                       "network_url": p.get("release_url") or "", "created_utc": self.iso}
                self.db.save(rec)
                self.audit(rec, "not from a pack", content=postiz.normalize_content(p["content"]), tool_state=p["state"])

    def _sync_one(self, r, p):
        h = r["handover"]
        slot = parse(h.get("slot_utc") or r.get("planned_slot_utc"))
        if h.get("dry_run"):
            if self.now >= slot:
                r["published_utc"] = iso(slot)
                self.mark(r, "dry_run")
                self.set_state(r, "published", "", event="slot passed (dry run: nothing was sent)")
            return
        if p is None:
            self._retire(r)
            self.set_state(r, "cancelled", "cancelled:in_the_tool", event="cancelled in the tool")
            return
        if p["state"] == "QUEUE":
            if postiz.content_hash(p["content"]) != h["content_hash"]:
                self.mark(r, "changed_in_tool")
                self._delete(r, "text changed in the tool")
                self.set_state(r, "needs_fix", "needs_fix:changed_in_tool", event="text changed in the tool",
                               tool_text=postiz.normalize_content(p["content"]))
                return
            tool_date = parse(p["date"])
            if tool_date and slot and abs((tool_date - slot).total_seconds()) > 60:
                self.mark(r, "changed_in_tool")
                self.audit(r, "rescheduled in the tool", from_utc=iso(slot), to_utc=iso(tool_date))
                h["slot_utc"] = r["planned_slot_utc"] = iso(tool_date)
                slot = tool_date
            if slot and self.now - slot > LATE and not p.get("release_url"):
                self.mark(r, "missed_slot")
                self._delete(r, "still queued an hour after its slot")
                self.set_state(r, "planned", "", event="missed slot: planned again")
                return
            self.db.save(r)
        elif p["state"] == "PUBLISHED" or p.get("release_url"):
            when = parse(p["date"]) or self.now
            if slot and when - slot > LATE:
                self.mark(r, "late")
            r.update({"published_utc": iso(when), "network_url": p.get("release_url") or "",
                      "published_text_hash": postiz.content_hash(p["content"])})
            differs = r["published_text_hash"] != h["content_hash"]
            self.set_state(r, "published", "", event="published", network_url=r["network_url"],
                           published_text=postiz.normalize_content(p["content"]) if differs else None)
            if differs:
                self.mark(r, "changed_in_tool")
                self._check_published(r, postiz.normalize_content(p["content"]))
                self.db.save(r)
        elif p["state"] == "ERROR":
            kind = postiz.classify(p.get("error"))
            self._delete(r, f"error in the tool ({kind})")
            if kind == "login":
                self.db.set(f"login_error:{self.brand_key}:{r['account_id']}", self.iso)
                self.set_state(r, "held", "held:reconnect_account", event="the network refused the login", error=p.get("error"))
            elif kind == "temporary" and int(r.get("retries") or 0) < MAX_RETRIES:
                r["retries"] = int(r.get("retries") or 0) + 1
                self.set_state(r, "planned", "", event="temporary error: planned again", error=p.get("error"),
                               retry=r["retries"])
            else:
                self.set_state(r, "failed", "failed:" + (str(p.get("error") or kind)[:300]), event="failed",
                               error=p.get("error"), kind=kind)
        elif p["state"] == "DRAFT":
            self._delete(r, "moved to drafts in the tool")
            self.set_state(r, "cancelled", "cancelled:moved_to_drafts_in_the_tool", event="cancelled in the tool")

    def _check_published(self, r, text):
        """F6: a post published with a text other than the approved one is checked again (E3)."""
        pack_dir = self.root / self.rel_social / "packs" / (r.get("pack_id") or "")
        try:
            pack = packmod.load(pack_dir)
        except (OSError, ValueError):
            return
        entry = packmod.post_meta(pack, r["post_id"])
        if not entry:
            return
        body, tags = text, []
        parts = text.rsplit("\n\n", 1)
        if len(parts) == 2 and all(w.startswith("#") for w in parts[1].split()):
            body, tags = parts[0], parts[1].split()
        tagged = re.search(r"https?://\S+utm_content=" + re.escape(r["post_id"]) + r"\S*", body)
        if tagged:
            body = body.replace(tagged.group(0), links.LINK)
        fields = dict(pack["posts"].get(r["post_id"]) or {}, text=body, hashtags=tags)
        results = [x for x in checks.check_post(pack, entry, fields, self.check_ctx(pack)) if x["check"] in RULE_CHECKS]
        failing = [x for x in results if not x["ok"]]
        self.audit(r, "published text checked", checks=results)
        if failing:
            self.mark(r, "published_breaks_a_rule")

    # 5: approvals from GitHub's record (boundary 3), fix PRs and their expiry
    def step_approvals(self):
        gh = self.env.gh
        if gh is None or not self.github_ok:
            return
        if not self.settings_accepted:                     # a post cannot be checked without settings
            self.banner("approval", "approvals wait: no settings accepted yet (settings.md counts only through "
                                    "a PR merged by someone with write access)")
            return
        try:
            closed = gh.pulls(state="closed", base="main", sort="updated", direction="desc", limit=2)
            opened = gh.pulls(state="open", base="main", sort="updated", direction="desc", limit=2)
        except github.GitHubError:
            self.github_ok = False
            self.banner("github", "GitHub could not be reached: no new hand-overs this hour")
            return
        news = []
        for simple in closed:
            m = BRANCH_RE.match((simple.get("head") or {}).get("ref") or "")
            if m and m["prefix"] == self.b["prefix"] and not self.db.pr_seen(simple["number"]):
                news.append((simple.get("closed_at") or "", simple, m))
        for _, simple, m in sorted(news, key=lambda x: (x[0], x[1]["number"])):
            try:
                pr = gh.pull(simple["number"])
                self._closed_pr(pr, m["pack"], int(m["fix"]) if m["fix"] else None)
            except github.GitHubError:
                self.github_ok = False
                return
            self.db.mark_pr(pr["number"], self.brand_key, pr["head"]["ref"], (pr.get("merged_by") or {}).get("login"),
                            pr.get("merged_at"), pr.get("merge_commit_sha"), pr.get("closed_at"))
        for pr in opened:
            m = BRANCH_RE.match((pr.get("head") or {}).get("ref") or "")
            if m and m["prefix"] == self.b["prefix"] and m["fix"]:
                self._open_fix_pr(pr, m["pack"], int(m["fix"]))

    def _pack_from(self, files):
        d = Path(tempfile.mkdtemp(prefix="px-pack-"))
        for rel, data in files.items():
            f = d / rel
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(data)
        return d, packmod.load(d)

    def _closed_pr(self, pr, pack_id, fix):
        rel = f"{self.rel_social}/packs/{pack_id}"
        merged = bool(pr.get("merged_at"))
        if not merged:
            raw = self.env.gh.file_at(f"{rel}/pack.json", pr["head"]["sha"])
            meta = json.loads(raw) if raw else {"posts": []}
            for p in meta.get("posts", []):
                if fix is not None and (p.get("fix") or {}).get("round") != fix:
                    continue
                rec = self.db.post(p["post_id"])
                if fix is not None:
                    if rec and rec["state"] not in FINAL:
                        self.set_state(rec, "cancelled", "cancelled:fix_pr_closed", event="fix PR closed",
                                       pr=pr["number"])
                elif rec is None:
                    rec = self._new_record(meta, p, None)
                    self.set_state(rec, "rejected", "", event="pack PR closed without merging", pr=pr["number"])
            return
        files = self.env.repo.files_at(pr["merge_commit_sha"], rel)
        if not files or "pack.json" not in files:
            self.db.audit(self.iso, self.brand_key, None, "merged PR without pack files", pr=pr["number"])
            return
        tmp, pack = self._pack_from(files)
        try:
            self._approve(pr, pack, tmp, fix)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def _approve(self, pr, pack, tmp, fix):
        merged_by = (pr.get("merged_by") or {}).get("login") or ""
        team_ok = self.team.has(merged_by)               # GitHubError: nothing changed, the PR is read again
        result = checks.run(pack, self.check_ctx(pack))
        deleted = set(packmod.deleted_posts(pack))
        for p in pack["meta"].get("posts", []):
            pid = p["post_id"]
            if pid in deleted or (fix is not None and (p.get("fix") or {}).get("round") != fix):
                continue
            rec = self.db.post(pid)
            if fix is not None and rec and rec["state"] in ("expired", "published", "rejected"):
                self.audit(rec, "fix PR merged after the post was final: ignored", pr=pr["number"])
                continue
            rec = self._new_record(pack["meta"], p, pack["posts"][pid], rec)
            rec["approval"] = {"pr": pr["number"], "merge_sha": pr["merge_commit_sha"], "merged_by": merged_by,
                               "merged_at": pr["merged_at"], "approved_files_sha256": handover.approval_hash(tmp, p)}
            rec["fix_pr"] = None
            if fix is not None:
                rec["retries"] = 0
            own = result["posts"].get(pid, [])
            failing = [x["check"] for x in own if not x["ok"]]
            data = {"pr": pr["number"], "merged_by": merged_by, "merged_at": pr["merged_at"],
                    "merge_sha": pr["merge_commit_sha"], "approved_text": rec["approved"]["text"], "checks": own}
            if not team_ok:
                self.set_state(rec, "needs_fix", "needs_fix:merged_by_other", event="merged by someone who cannot approve",
                               **data)
            elif failing:
                self.set_state(rec, "needs_fix", "needs_fix:check_failed", event="merged with a failing check",
                               detail=", ".join(failing), **data)
            else:
                self.set_state(rec, "waiting_for_article", "", event="approved", **data)

    def _new_record(self, meta, post, fields, rec=None):
        src = meta.get("source") or {}
        item = self._item(src.get("slug")) if src.get("slug") else None
        rec = rec or {"post_id": post["post_id"], "brand": self.brand_key, "markers": [], "retries": 0,
                      "created_utc": self.iso, "state": "in_review", "reason": ""}
        rec.update({
            "pack_id": meta.get("pack_id"), "account_id": post.get("account_id"), "network": post.get("network"),
            "role": post.get("role", "launch"), "format": post.get("format", "single"),
            "source": src.get("item_id") or src.get("request_id") or meta.get("pack_id"),
            "source_kind": src.get("kind"), "slug": src.get("slug"), "request_id": src.get("request_id"),
            "title": (item or {}).get("title") or meta.get("angle") or "",
            "sources": [s.get("line", "") for s in post.get("sources") or []],
            "pages": [rr["url"] for rr in src.get("records") or [] if rr.get("lines") and rr.get("kind", "page") == "page"],
            "outside_sources": any(rr.get("lines") and rr.get("kind", "page") != "page" for rr in src.get("records") or []),
            "earliest_utc": post.get("earliest_utc"),
        })
        if fields is not None:
            rec["approved"] = {"fields": fields, "text": packmod.publish_text(fields)}
            rec["matched_version"] = src.get("article_version")
        return rec

    def _open_fix_pr(self, pr, pack_id, fix):
        raw = self.env.gh.file_at(f"{self.rel_social}/packs/{pack_id}/pack.json", pr["head"]["sha"])
        try:
            meta = json.loads(raw) if raw else {}
        except ValueError:
            meta = {}
        opened = parse(pr.get("created_at")) or self.now
        expired = self.now - opened > FIX_PR_EXPIRY
        for p in meta.get("posts", []):
            if (p.get("fix") or {}).get("round") != fix:
                continue
            rec = self.db.post(p["post_id"])
            if rec is None or rec["state"] in FINAL or rec["state"] == "scheduled":
                continue
            if expired:
                self.set_state(rec, "expired", "expired:fix_pr_not_merged_in_30_days", event="fix PR expired",
                               pr=pr["number"])
                continue
            rec["fix_pr"] = {"number": pr["number"], "round": fix, "opened_utc": iso(opened)}
            if rec["state"] != "in_fix_pr":
                self.set_state(rec, "in_fix_pr", rec.get("reason", ""), event="in a fix PR", pr=pr["number"])
        if expired:
            p = board.packs_path(self.brand_key, self.root)
            text = board._read(p)
            row = next((r for r in board.parse_packs(text) if r.get("pack_id") == f"{pack_id}-fix-{fix}"), None)
            if row and row.get("status") == "open":
                p.write_text(board.upsert_pack(text, {"pack_id": row["pack_id"], "status": "expired",
                                                      "updated": self.iso[:10]}), encoding="utf-8")

    # 6: commands of the request list (F6)
    def step_commands(self):
        p = board.requests_path(self.brand_key, self.root)
        text = board._read(p)
        if not text:
            return
        _, cmds = board.parse_requests(text)
        changed = False
        for row in cmds:
            cid = row.get("id")
            if not cid or row.get("status") != "open" or self.db.command_seen(cid):
                continue
            cmd, why = board.parse_command(row)
            if cmd is None:
                text = board.set_command(text, cid, "ignored", why)
                self.db.mark_command(cid, self.brand_key, self.iso, "ignored")
                changed = True
                continue
            if cmd["kind"] in board.PACK_COMMANDS:            # at once, or at a chosen time: a post or a whole pack
                pack_id = cmd.get("pack_id") or (ids.parse_post_id(cmd["post_id"]) or {}).get("pack_id")
                recs = [self.db.post(cmd["post_id"])] if cmd.get("post_id") else \
                    [r for r in self.db.posts(self.brand_key) if r.get("pack_id") == pack_id]
                recs = [r for r in recs if r]
                if not recs and self._in_review(pack_id):
                    continue                                  # chosen before the merge: the line waits for it
                if not recs:
                    status, note = self._post_now(None, cid)
                else:
                    got = [self._post_now(r, cid) if cmd["kind"] == "post now" else
                           self._post_at(r, cid, self._local_start(cmd["date"])) for r in recs]
                    done = [n for s_, n in got if s_ == "done"]
                    status, note = ("done", done[0] + (f" ({len(done)} of {len(recs)} posts)" if len(recs) > 1 else "")) \
                        if done else got[0]
                text = board.set_command(text, cid, status, note)
                self.db.mark_command(cid, self.brand_key, self.iso, status)
                changed = True
                continue
            rec = self.db.post(cmd["post_id"])
            if cmd["kind"] == "fix":                        # the drafting run opens the fix PR (E7)
                if rec and rec["state"] not in ("published", "rejected", "cancelled", "expired", "not_from_pack"):
                    self.set_state(rec, "needs_fix", "needs_fix:fix_line", event="fix line", command=cid)
                self.db.mark_command(cid, self.brand_key, self.iso, "fix noted")
                continue
            status, note = "done", ""
            if rec is None:
                status, note = "ignored", "not approved yet: delete the post's file in its PR, or close the PR"
            elif rec["state"] in FINAL:
                status, note = "ignored", f"already {rec['state'].replace('_', ' ')}"
            elif rec["state"] == "scheduled":
                status, note = "ignored", "already in the publishing tool: cancel or move it there"
            elif cmd["kind"] == "cancel":
                self.set_state(rec, "cancelled", "cancelled:cancel_line", event="cancel line", command=cid)
            else:
                when = self._local_start(cmd["date"])
                rec["not_before_utc"] = iso(when)
                self.audit(rec, "not before", command=cid, not_before_utc=rec["not_before_utc"])
                self.db.save(rec)
                note = f"not before {cmd['date']}"
            text = board.set_command(text, cid, status, note)
            self.db.mark_command(cid, self.brand_key, self.iso, status)
            changed = True
        if changed:
            p.write_text(text, encoding="utf-8")

    def _post_now(self, rec, cid):
        """(status, note) of a 'post now' line. The post keeps every check: approval, rules, live
        page, pause; only the slot is skipped. A post already in the tool is pulled back and sent again."""
        if rec is None:
            return "ignored", "not approved yet: approve the pack first"
        if rec["state"] in FINAL:
            return "ignored", f"already {rec['state'].replace('_', ' ')}"
        if rec["state"] in ("needs_fix", "in_fix_pr", "article_changed"):
            return "ignored", f"it is {rec['state'].replace('_', ' ')}: it needs a fix PR first"
        rec["post_now"] = cid
        self.audit(rec, "post now", command=cid)
        self.db.save(rec)
        if rec["state"] == "scheduled":
            self._delete(rec, "post now")
            self.set_state(rec, "planned", "", event="pulled back to go out at once")
        return "done", "goes out at once" if rec["state"] in ("planned", "scheduled") else \
            "goes out at once when it can (it is " + rec["state"].replace("_", " ") + ")"

    def _post_at(self, rec, cid, when):
        """(status, note) of a 'post at' line: the post goes out at that time instead of at a slot, with
        every check kept. A post already in the tool is pulled back and handed over for the new time."""
        if rec["state"] in FINAL:
            return "ignored", f"already {rec['state'].replace('_', ' ')}"
        if rec["state"] in ("needs_fix", "in_fix_pr", "article_changed"):
            return "ignored", f"it is {rec['state'].replace('_', ' ')}: it needs a fix PR first"
        rec["at_utc"] = iso(max(when, self.now))
        rec.pop("post_now", None)
        self.audit(rec, "post at", command=cid, at_utc=rec["at_utc"])
        self.db.save(rec)
        if rec["state"] == "scheduled":
            self._delete(rec, "post at")
            self.set_state(rec, "planned", "", event="pulled back for its chosen time")
        import zoneinfo
        local = when.astimezone(zoneinfo.ZoneInfo(self.settings.brand["time_zone"])).strftime("%Y-%m-%d %H:%M")
        return "done", f"goes out at {local}"

    def _in_review(self, pack_id):
        """True while the pack's PR is open: a line chosen before the merge waits for it."""
        rows = board.parse_packs(board._read(board.packs_path(self.brand_key, self.root)))
        return any(r.get("pack_id") == pack_id and r.get("status") == "open" for r in rows)

    def _local_start(self, value):
        import zoneinfo
        tz = zoneinfo.ZoneInfo(self.settings.brand["time_zone"])
        t = value.replace("T", " ")
        dt = datetime.strptime(t, "%Y-%m-%d %H:%M") if " " in t else datetime.strptime(t, "%Y-%m-%d")
        return dt.replace(tzinfo=tz).astimezone(timezone.utc)

    # 7: go-live (F2)
    def step_golive(self):
        waiting = [r for r in self.db.posts(self.brand_key, sorted(RECOMPUTED)) if not r.get("went_live_utc")]
        by_slug = {}
        for r in waiting:
            if r.get("source_kind") == "page":                        # no article of its own to wait for
                r["went_live_utc"] = r.get("approval", {}).get("merged_at") or self.iso
                self.db.save(r)
                continue
            by_slug.setdefault(r.get("slug"), []).append(r)
        for slug, recs in by_slug.items():
            item = self._item(slug)
            if item is None:
                continue                                     # un-approved: step 8 holds them
            key = f"went_live:{self.brand_key}:{slug}"
            seen = self.db.get(key)
            live, address, why = (True, None, "") if seen else liveness.is_live(item, self.record or {}, self.settings.brand,
                                                                                self.brand_key, self.site)
            if not live:
                for r in recs:
                    if r["state"] == "waiting_for_article" and r.get("reason") != f"waiting:{why}":
                        r["reason"] = f"waiting:{why}"
                        self.db.save(r)
                continue
            if not seen:
                seen = self.iso
                self.db.set(key, seen)
                self.db.audit(self.iso, self.brand_key, None, "went live", item=item["id"], slug=slug, address=address)
            for r in recs:
                r["went_live_utc"] = seen
                r["article_url"] = address or liveness.live_address(item, self.record or {}, self.settings.brand,
                                                                    self.brand_key) or ""
                self.audit(r, "article live", went_live_utc=seen)
                self.db.save(r)

    # 8: article versions (A6, A9)
    def step_versions(self):
        for r in self.db.posts(self.brand_key):
            if r.get("source_kind") not in ("article", "intro") or r["state"] in FINAL - {"published"} or \
                    r["state"] in ("in_review",):
                continue
            item = self._item(r.get("slug"))
            if item is None or item.get("board_status") not in ("approved", "posted"):
                continue                                     # step 9 holds it: article un-approved
            if not r.get("matched_version") or item["article_version"] == r["matched_version"]:
                continue
            src_all = checks.source_text(item, self._articles.get(r["slug"], ""))
            missing = [ln for ln in r.get("sources") or [] if checks.md_plain(ln) not in src_all]
            if not missing:
                self.audit(r, "article version changed: every source line is still there",
                           from_version=r["matched_version"], to_version=item["article_version"])
                r["matched_version"] = item["article_version"]
                self.db.save(r)
            elif r["state"] == "published":
                if "article_changed_after_publishing" not in r.get("markers", []):
                    self.mark(r, "article_changed_after_publishing")
                    self.db.save(r)
            elif r["state"] not in ("article_changed", "in_fix_pr", "needs_fix"):
                self.set_state(r, "article_changed", "article_changed", event="article changed",
                               missing_lines=missing, to_version=item["article_version"])

    # 9: recompute the open posts, then pull back what may not stay in the tool (F7)
    def step_recompute(self):
        pause = self.paused()
        usable = {a["account_id"] for a in self.settings.usable_accounts()}
        for r in self.db.posts(self.brand_key, sorted(RECOMPUTED | {"scheduled"})):
            unapproved = r.get("source_kind") in ("article", "intro") and \
                (self._item(r.get("slug")) or {}).get("board_status") not in ("approved", "posted")
            login = parse(self.db.get(f"login_error:{self.brand_key}:{r.get('account_id')}"))
            acc = self.settings.account(r.get("account_id")) or {}
            ch = self.channels.get(acc.get("postiz_channel_id"))
            cause = None
            if pause:
                cause = "held:paused" if pause.startswith("paused") else "held:social_off"
            elif r.get("account_id") not in usable:
                cause = "held:account_off"
            elif (ch and ch.get("needs_reconnect")) or (login and self.now - login < LOGIN_HOLD):
                cause = "held:reconnect_account"
            elif ch and ch.get("disabled"):
                cause = "held:channel_disabled"
            elif unapproved:
                cause = "held:article_unapproved"
            if cause:
                if (r["state"], r.get("reason")) != ("held", cause):
                    self.set_state(r, "held", cause, event="held", detail=pause or "")
                continue
            if r["state"] == "scheduled":
                continue
            if not r.get("went_live_utc"):
                if r["state"] != "waiting_for_article":
                    self.set_state(r, "waiting_for_article", r.get("reason") if str(r.get("reason", "")).startswith("waiting:") else "")
                continue
            if r["state"] == "held" and r.get("reason") in HANDOVER_HOLDS and self.still_held(r):
                continue
            if r["state"] != "planned":
                self.set_state(r, "planned", "", event="released" if r["state"] == "held" else "planned")

    def still_held(self, r):
        """True while a hand-over hold still applies (each check looks again)."""
        if r["reason"] == "held:live_page_differs":
            missing, _ = self.live_page_missing(r, (r.get("approved") or {}).get("fields") or {})
            if missing and missing != r.get("missing_lines"):
                r["missing_lines"] = missing
                self.db.save(r)
            return bool(missing)
        if r["reason"] == "held:no_live_link":
            pack_dir = self.root / self.rel_social / "packs" / (r.get("pack_id") or "")
            try:
                entry = packmod.post_meta(packmod.load(pack_dir), r["post_id"]) or {}
            except (OSError, ValueError):
                return True
            address = self.link_address(r, entry)
            if not address or not links.allowed(address, self.brand_key, self.settings.brand, self.ops)[0]:
                return True
            return not self.site.fetch(address)["ok"]
        if r["reason"] == "held:no_visual":
            pack_dir = self.root / self.rel_social / "packs" / (r.get("pack_id") or "")
            try:
                entry = packmod.post_meta(packmod.load(pack_dir), r["post_id"]) or {}
            except (OSError, ValueError):
                return True
            files = [pack_dir / "visuals" / v["file"] for v in entry.get("visuals") or []]
            return not files or not all(f.exists() for f in files)
        return False

    def step_pullbacks(self):
        for r in self.db.posts(self.brand_key):
            h = r.get("handover") or {}
            if h.get("postiz_post_id") and r["state"] not in ("scheduled", "published"):
                self._delete(r, r.get("reason") or r["state"])

    # 10: planning (flow 5)
    def step_plan(self):
        recs = self.db.posts(self.brand_key)
        accounts = {a["account_id"]: {"slots": a["slots"], "max_per_day": a["max_per_day"]}
                    for a in self.settings.usable_accounts()}
        taken, known = [], {}
        for r in recs:
            when = parse(r.get("planned_slot_utc")) if r["state"] == "scheduled" else \
                parse(r.get("published_utc")) if r["state"] == "published" else \
                parse(r.get("published_utc") or r.get("planned_slot_utc")) if r["state"] == "not_from_pack" else None
            if when:
                taken.append({"account_id": r.get("account_id"), "slot": when})
                known[r["post_id"]] = when
        planned = [r for r in recs if r["state"] == "planned" and not (r.get("handover") or {}).get("intent_utc")]
        for r in [r for r in planned if r.get("post_now") or r.get("at_utc")]:   # at once, or at its post at time
            slot = self.now if r.get("post_now") else max(parse(r["at_utc"]) or self.now, self.now)
            r["planned_slot_utc"] = iso(slot)
            taken.append({"account_id": r.get("account_id"), "slot": slot})
            self.db.save(r)
        planned = [r for r in planned if not (r.get("post_now") or r.get("at_utc"))]
        waiting = []
        for r in planned:
            approval = r.get("approval") or {}
            kind = "follow-up" if r.get("role") == "follow-up" else "request" if r.get("request_id") or \
                r.get("role") == "request" else "launch"
            p = {"post_id": r["post_id"], "account_id": r["account_id"], "kind": kind,
                 "not_before": parse(r.get("not_before_utc")), "went_live": parse(r.get("went_live_utc"))}
            if kind == "request":
                p["eligible"] = max(x for x in (parse(approval.get("merged_at")), parse(r.get("earliest_utc")),
                                                parse(r.get("went_live_utc")), parse("2000-01-01")) if x)
                p["earliest"] = p["eligible"]
            elif kind == "follow-up":
                p["after"] = self._previous(r, recs)
                p["delay_days"] = (self.settings.account(r["account_id"]) or {}).get("followup_delay_days", 14)
            waiting.append(p)
        result, last = planner.plan(waiting, accounts, taken, self.now, self.settings.brand["time_zone"], known)
        for r in planned:
            got = result.get(r["post_id"]) or {}
            old = parse(r.get("planned_slot_utc"))
            if old and old < self.now + planner.LEAD:
                self.mark(r, "missed_window")
            slot = got.get("slot")
            r["planned_slot_utc"] = iso(slot)
            if got.get("earliest"):
                r["earliest_utc"] = iso(got["earliest"])
            if got.get("waited_14_days"):
                self.mark(r, "waited_14_days")
            self.db.save(r)
        for a in planner.schedule_full(last, self.now):
            self.banner("schedule", f"schedule full for {a}: add slots or lower posts per article")

    def _previous(self, r, recs):
        me = ids.parse_post_id(r["post_id"]) or {}
        prev = [x for x in recs if x.get("pack_id") == r.get("pack_id") and x.get("account_id") == r.get("account_id")
                and (ids.parse_post_id(x["post_id"]) or {}).get("k", 0) < me.get("k", 0)]
        return max(prev, key=lambda x: ids.parse_post_id(x["post_id"])["k"])["post_id"] if prev else None

    # 11: hand-over (flow 6)
    def step_handover(self):
        def due_now(r):
            slot = parse(r.get("planned_slot_utc"))
            if r.get("at_utc"):                       # its post at time: from 3 hours before, up to the time itself
                return slot is not None and slot - self.now <= timedelta(hours=3)
            return bool(r.get("post_now")) or planner.in_window(slot, self.now)
        due = [r for r in self.db.posts(self.brand_key, ["planned"]) if due_now(r) and not r.get("handover")]
        if not due:
            return
        why = list(self.no_handover) + ([] if self.github_ok else ["GitHub could not be reached"]) + \
            ([self.paused()] if self.paused() else [])
        if why:
            for r in due:
                self.audit(r, "hand-over waits", why="; ".join(why))
            return
        for r in sorted(due, key=lambda x: (x["planned_slot_utc"], x["post_id"])):
            if not self.github_ok:                    # GitHub stopped answering who may approve
                self.audit(r, "hand-over waits", why="GitHub could not be reached")
                continue
            handover.hand_over(self, r)

    def link_address(self, rec, entry):
        """The live address a post links to (flow 6 step 3)."""
        target = (entry.get("link") or {}).get("target")
        if target:
            return target
        item = self._item(rec.get("slug"))
        return liveness.live_address(item, self.record or {}, self.settings.brand, self.brand_key) if item else None

    def live_page_missing(self, rec, fields):
        """(missing lines, pages) of the live-page check (flow 6 step 4). Facts from a page or text a
        request named, or from another of our articles, were confirmed against it when drafting:
        such a post skips this step."""
        if rec.get("source_kind") == "page":
            if rec.get("outside_sources"):
                return [], rec.get("pages") or []
            pages = rec.get("pages") or []
        else:
            item = self._item(rec.get("slug"))
            address = liveness.live_address(item, self.record or {}, self.settings.brand, self.brand_key) if item else None
            pages = [address] if address else []
        if not pages or not rec.get("sources"):
            return [], pages                                 # an empty source record skips this step
        return handover.live_missing(self.site, pages, fields, self.settings.brand["allowed_number_names"]), pages

    # 12: expiry and markers
    def step_expiry(self):
        for r in self.db.posts(self.brand_key):
            if r["state"] in FINAL or r["state"] in ("scheduled", "in_review"):
                continue
            earliest = parse(r.get("earliest_utc"))
            if r.get("role") == "follow-up" and earliest and self.now - earliest > FOLLOWUP_EXPIRY:
                self.set_state(r, "expired", "expired:follow_up_60_days", event="follow-up expired")
                continue
            held = parse(r.get("held_since_utc"))
            if r["state"] == "held" and r.get("reason") == "held:live_page_differs" and held and self.now - held >= WAITING_LONG:
                self.mark(r, "waiting_long")
                self.db.save(r)
            merged = parse((r.get("approval") or {}).get("merged_at"))
            if r["state"] == "waiting_for_article" and merged and self.now - merged >= WAITING_LONG_FOR_ARTICLE:
                self.mark(r, "waiting_long_for_article")
                self.db.save(r)

    def standing_banners(self):
        recs = self.db.posts(self.brand_key)
        for ch in self.channels.values():
            acc = next((a for a in self.settings.accounts if a["postiz_channel_id"] == ch["id"]), None)
            if acc and acc["active"] and ch.get("needs_reconnect"):
                self.banner("reconnect", f"reconnect account {acc['account_id']}", "red")
        seen = {e["message"] for e in settingsmod.load(self.brand_key, self.root).errors}
        for e in self.settings.errors:
            if e["message"] not in seen:
                self.banner("settings", e["message"])
        for a in self.settings.accounts:
            if parse(self.db.get(f"login_error:{self.brand_key}:{a['account_id']}")) and \
                    self.now - parse(self.db.get(f"login_error:{self.brand_key}:{a['account_id']}")) < LOGIN_HOLD:
                self.banner("reconnect", f"reconnect account {a['account_id']}", "red")
        pause = self.paused()
        if pause and pause.startswith("paused"):
            self.banner("paused", f"{self.b['name']} is {pause}", "red")
            since = self.db.switches(self.brand_key)["since_utc"] or ""
            for ev in self.db.control_events(self.brand_key):
                if ev["command"] == "lift" and not ev["accepted"] and (ev["utc"] or "") >= since:
                    self.banner("paused", f"lift ignored: @{ev['author']} has no write access")
        others = {}
        for r in recs:
            if r.get("reason") == "needs_fix:merged_by_other" and r.get("approval"):
                others.setdefault((r["approval"]["pr"], r["approval"].get("merged_by")), []).append(r["post_id"])
        for (number, who), posts in sorted(others.items(), key=lambda x: x[0][0]):
            self.banner("approval", f"PR #{number} was merged by @{who}, who cannot approve (no write access, or a "
                                    f"bot): its posts are not approved ({', '.join(posts)})", "red")
        groups = {"article_changed": ("article", "articles changed after their pack was approved: "),
                  "held:live_page_differs": ("live page", "posts held because the live page differs: "),
                  "held:no_visual": ("visual", "posts held for no visual: ")}
        for key, (kind, text) in groups.items():
            hit = [r["post_id"] for r in recs if r.get("reason") == key or (key == "article_changed" and r["state"] == key)]
            if hit:
                self.banner(kind, text + ", ".join(hit[:8]) + (" …" if len(hit) > 8 else ""))
        changed = [r["post_id"] for r in recs if "changed_in_tool" in (r.get("markers") or []) and r["state"] != "published"]
        if changed:
            self.banner("tool", "posts changed in the tool: " + ", ".join(changed[:8]))
        foreign = [r["post_id"] for r in recs if r["state"] == "not_from_pack"]
        if foreign:
            self.banner("not from a pack", "posts not from a pack on a brand account: " + ", ".join(foreign[:8]), "red")
        broken = [r["post_id"] for r in recs if "published_breaks_a_rule" in (r.get("markers") or [])]
        if broken:
            self.banner("published", "published post breaks a rule: remove it on the network (" + ", ".join(broken) + ")", "red")
        if self.env.dry_run:
            self.banner("dry run", "dry run: hand-overs are planned and logged, nothing is sent to the networks", "info")

    def brand_state(self):
        sw = self.db.switches(self.brand_key)
        on = {"settings": bool(self.settings.brand["pause"]), "stop_now": sw["stop_now"], "tool": sw["tool_pause"]}
        names = {"settings": "Paused (settings)", "stop_now": "Paused (stop now)", "tool": "Paused (tool)"}
        return {"social": "on" if self.settings.social_on else "off", "paused": any(on.values()), "switches": on,
                "badges": [names[k] for k, v in on.items() if v], "since_utc": sw["since_utc"],
                "dry_run": bool(self.env.dry_run)}

    # 13: write SQLite, export, dashboard data, commit
    def step_write(self):
        self.standing_banners()
        self.db.commit()
        social = self.root / self.rel_social
        written, last_audit = ledgermod.export(self.db, self.brand_key, social, self.iso, self.banners,
                                               self.brand_state())
        review, schedule = dash.build(self.root, self.brand_key, self.now)
        dash.write(self.root, self.brand_key, review, schedule)
        self.db.commit()
        own = {k: v for k, v in self.env.own_secrets.items() if v}
        out = [social / "ledger.json", social / "audit", self.root / "docs" / "data" / "social",
               board.requests_path(self.brand_key, self.root), board.packs_path(self.brand_key, self.root)]
        leaks = secret_scan.scan_paths([p for p in out if p.exists()], own)
        if leaks:
            raise SystemExit("own secret found in the files to commit: nothing is committed ("
                             + ", ".join(sorted({x['kind'] for x in leaks})) + ")")
        ok = True
        if self.env.push:
            ok = self.github_ok and self.env.repo.commit_and_push(
                [p.relative_to(self.root) for p in out if p.exists()],
                f"social: publishing check {self.iso} ({self.brand_key})")
            if not ok:
                self.db.audit(self.iso, self.brand_key, None, "commit or push failed: the next check exports again")
        if ok and last_audit:
            self.db.set(f"audit_exported:{self.brand_key}", last_audit)
        self.db.commit()
        return written

    def go(self):
        run_id = self.db.run_start("check", self.iso)
        result = "ok"
        try:
            self.github_ok = self.env.repo.pull()
            if not self.github_ok:
                self.banner("github", "GitHub could not be reached: no new hand-overs this hour")
            self.step_keys()
            self.step_settings()
            self.record = None
            if self.env.publisher_record:
                try:
                    self.record = self.env.publisher_record(self.brand_key)
                except Exception:  # noqa: BLE001 - an unreachable record only means "use the board"
                    self.record = None
            if self.record is None:
                self.banner("record", "the publisher's record could not be read: go-live uses the board only", "info")
            self.step_sync()
            self.step_approvals()
            self.step_commands()
            self.step_golive()
            self.step_versions()
            self.step_recompute()
            self.step_pullbacks()
            self.step_plan()
            self.step_handover()
            self.step_expiry()
            self.step_write()
        except BaseException:
            result = "error"
            self.db.commit()
            raise
        finally:
            self.db.run_end(run_id, self.iso if self.env.fixed_clock else iso(datetime.now(timezone.utc)), result)
        return self.summary()

    def summary(self):
        counts = {}
        for r in self.db.posts(self.brand_key):
            counts[r["state"]] = counts.get(r["state"], 0) + 1
        return {"brand": self.brand_key, "utc": self.iso, "states": counts, "banners": self.banners,
                "github_ok": self.github_ok, "tool_ok": self.tool_ok}


# --- the guest --------------------------------------------------------------------------

def own_secrets_from_guest():
    """The guest's own secrets, for the key scan (flow 14): exact values never to be found in
    the repository. The App key counts by its longest base64 line."""
    out = {"postiz-key": os.environ.get("POSTIZ_API_KEY", ""),
           "webportals-token": os.environ.get("WEBPORTALS_READ_TOKEN", "")}
    key_file = os.environ.get("PX_SOCIAL_APP_KEY_FILE")
    if key_file and Path(key_file).exists():
        lines = [ln.strip() for ln in Path(key_file).read_text(encoding="utf-8").splitlines() if not ln.startswith("-----")]
        out["github-app-key"] = max(lines, key=len) if lines else ""
    return {k: v for k, v in out.items() if v}


def env_from_guest(a, now=None):
    from social import github_app
    root = Path(os.environ.get("PX_SOCIAL_DATA", "/var/lib/px-social/AIContent"))
    db = ledgermod.Ledger(os.environ.get("PX_SOCIAL_DB", "/var/lib/px-social/state.sqlite"))
    token = None
    if os.environ.get("PX_SOCIAL_APP_ID"):
        token, _ = github_app.installation_token(os.environ["PX_SOCIAL_APP_ID"], os.environ["PX_SOCIAL_INSTALLATION_ID"],
                                                 Path(os.environ["PX_SOCIAL_APP_KEY_FILE"]).read_text(encoding="utf-8"))
    gh = github.GitHub(token) if token else None
    if a.fake_postiz is not None:
        state = Path(a.fake_postiz) if a.fake_postiz else None
        client = postiz.FakePostiz.from_json(json.loads(state.read_text(encoding="utf-8"))) if state and state.exists() \
            else postiz.FakePostiz()
    else:
        client = postiz.Postiz(os.environ["POSTIZ_API_URL"], os.environ["POSTIZ_API_KEY"])
    if a.dry_run and a.fake_postiz is None:
        client = postiz.DryRun(client)
    portals = os.environ.get("WEBPORTALS_READ_TOKEN")

    def record(brand_key):
        if not portals:
            return None
        return github.GitHub(portals, PUBLISHER_REPO).contents_json(PUBLISHER_REPO, brands.brand(brand_key)["publisher_record"])

    return Env(root, db, client, gh, Repo(root, token), record, now=now,
               enabled_brands=[x.strip() for x in os.environ.get("PX_SOCIAL_ENABLED_BRANDS", "").split(",") if x.strip()],
               own_secrets=own_secrets_from_guest(), dry_run=a.dry_run,
               content_format=os.environ.get("POSTIZ_CONTENT_FORMAT", "html"), push=not a.no_push)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--brand", action="append")
    ap.add_argument("--dry-run", action="store_true", default=os.environ.get("DRY_RUN") == "1")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--fake-postiz", nargs="?", const="", default=None,
                    help="use an in-memory Postiz (kept in this JSON file between runs, if given)")
    ap.add_argument("--replay", help="replay a recorded day (vk-0300) without any network call")
    a = ap.parse_args(argv)
    if a.replay:
        from social import replay
        return replay.main(a.replay)
    env = env_from_guest(a)
    rc = 0
    for brand_key in a.brand or [b for b in env.enabled_brands] or ["vsichkikazina"]:
        out = Run(env, brand_key).go()
        print(json.dumps(out, ensure_ascii=False))
    if a.fake_postiz:
        Path(a.fake_postiz).write_text(json.dumps(env.postiz.to_json(), ensure_ascii=False, indent=2), encoding="utf-8")
    env.db.close()
    return rc


if __name__ == "__main__":
    sys.exit(main())
