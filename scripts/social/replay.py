#!/usr/bin/env python3
"""A recorded day, replayed without any network call (tech spec, Environments: "One recorded day
is the vk-0300 timeline of flow 0, so the walk-through is also a test").

    python3 scripts/social/publishing_check.py --dry-run --fake-postiz --replay vk-0300

`World` is a brand with its repository, GitHub's record, the publisher's record, the live site
and Postiz, all fake and on a clock that the caller moves. The tests use it for every publishing
check scenario; `vk0300()` plays flow 0's example timeline and returns what each check saw.
"""
import json
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_library  # noqa: E402
from social import board, brands, ledger as ledgermod, make_pack, mdtable, postiz, publishing_check as pc  # noqa: E402

SETTINGS = """# Social settings — Всички Казина

## Brand
| key | value |
|---|---|
| social | on |
| time_zone | Europe/Sofia |
| compliance_long | 18+ Хазартът може да пристрасти. Играйте отговорно. |
| compliance_short | 18+ Играйте отговорно. |
| eligible_types | guide, comparison, review, news |
| allowed_link_areas | /blog/ |
| address_pattern | https://vsichkikazina.bg/blog/{slug}/ |
| identities_verified | 2026-11-01, SOCIAL-SETUP.md#identities |
| offer_words | бонус, оферта |
| register_words | регистрирайте се |

## Accounts
| account_id | network | postiz_channel_id | active | posts_per_article | followup_delay_days | format | max_hashtags | link | slots | max_per_day | emoji | tone_override | test_post_seen | profile_link_set |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fb-vsichkikazina | facebook | ch-fb | on | 1 | 14 | auto | 3 | in post | daily 12:30, 19:30 | 2 | light |  | 2026-11-02 Ana, phone | |
| ig-vsichkikazina | instagram | ch-ig | on | 1 | 14 | auto | 5 | profile | daily 12:30, 19:30 | 2 | light |  | 2026-11-02 Ana, phone | 2026-11-02 |
| x-vsichkikazina | x | ch-x | on | 1 | 14 | single | 2 | in post | daily 12:30, 19:30 | 2 | light |  | 2026-11-02 Ana, phone | |
| li-vsichkikazina | linkedin-page | ch-li | off | 1 | 14 | auto | 5 | in post | daily 12:30, 19:30 | 2 | none |  | | |
"""
CHANNELS = [{"id": "ch-fb", "name": "Всички Казина", "identifier": "facebook"},
            {"id": "ch-ig", "name": "vsichkikazina", "identifier": "instagram"},
            {"id": "ch-x", "name": "@vsichkikazina", "identifier": "x"},
            {"id": "ch-li", "name": "Всички Казина", "identifier": "linkedin-page"}]
QUEUE_HEAD = ("# Content Queue\n| id | status | type | query | keywords_or_terms | volume | kd | source | drafted_date | "
              "posted_date | folder | pr | gemini | notes |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
ROW = "| {id} | {status} | {type} | {query} | {kw} | 100 | 10 | research | 2026-11-01 | {posted} | {folder} | #{pr} | human 85 |  |\n"
LINE_ODDS = "Европейската рулетка има 37 полета, а предимството на казиното е 2,7%."
LINE_PAY = "Единичното число плаща 35:1."
ARTICLE = f"""Title tag: Рулетка: шансове и залози
Meta description: Какви са шансовете при рулетката и колко плаща всеки залог.

# Рулетка: шансове и залози

{LINE_PAY}

{LINE_ODDS}
"""
COMPLIANCE = "18+ Хазартът може да пристрасти. Играйте отговорно."
DRAFT_0300 = {
    "brand": "vsichkikazina", "source": {"kind": "article", "item_id": "vk-0300"}, "request_id": None,
    "angle": "key takeaway", "posts": [
        {"account_id": "fb-vsichkikazina", "role": "launch", "angle": "one number",
         "text": f"{LINE_ODDS}\n\nКакво значи това за всеки залог: [[LINK]]\n\n{COMPLIANCE}",
         "hashtags": ["#рулетка"], "image_text": ["37 полета, 2,7% предимство"], "alt_text": "Колело на рулетка",
         "art_idea": "a roulette wheel seen from above", "sources": [{"line": LINE_ODDS, "where": "Рулетка: шансове и залози"}]},
        {"account_id": "ig-vsichkikazina", "role": "launch", "angle": "one number",
         "text": f"{LINE_PAY} Ръководството е на линка в профила ни.\n\n{COMPLIANCE}",
         "hashtags": ["#рулетка", "#казино", "#шансове"], "image_text": ["Единичното число плаща 35:1"],
         "alt_text": "Чипове върху едно число", "art_idea": "chips on a single number",
         "sources": [{"line": LINE_PAY, "where": "Рулетка: шансове и залози"}]},
        {"account_id": "x-vsichkikazina", "role": "launch", "angle": "one number",
         "text": "Рулетка: 37 полета и 2,7% предимство за казиното. [[LINK]] 18+ Играйте отговорно.",
         "hashtags": ["#рулетка"], "image_text": ["37 полета"], "alt_text": "Колело на рулетка",
         "art_idea": "a roulette wheel", "sources": [{"line": LINE_ODDS, "where": "Рулетка: шансове и залози"}]},
    ]}
PAGE = """<html><head><title>Рулетка</title><script>var x = "99";</script></head><body><nav>Меню</nav>
<article><h1>Рулетка: шансове и залози</h1><p>{pay}</p><p>{odds}</p></article><footer>18+</footer></body></html>"""


def utc(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)


def offline(url, **kwargs):
    raise OSError("offline: the replay reaches no site")


def english(draft_post):
    """The English reference the drafting agent writes with a post."""
    return {"text": f"EN: {draft_post['text'][:60]}", "image_text": [f"EN: {t[:60]}" for t in draft_post.get("image_text") or []]}


class FakeGitHub:
    """GitHub's record: PRs, files at commits, commits per path, comments, permissions."""

    def __init__(self):
        self.prs, self.files, self.path_commits, self.commit_prs = {}, {}, {}, {}
        self.comments, self.down = [], False
        self.perms = {"AmigoNiko": "admin", "Ivana": "write"}       # the team; anyone else reads

    def _up(self):
        if self.down:
            raise pc.github.GitHubError("GitHub cannot be reached")

    def pulls(self, state="open", base="main", sort="updated", direction="desc", limit=3):
        self._up()
        return [dict(p) for p in self.prs.values() if p["state"] == state]

    def pull(self, number):
        self._up()
        return dict(self.prs[int(number)])

    def file_at(self, path, ref):
        self._up()
        return self.files.get((ref, path))

    def commits(self, path, since=None, sha="main"):
        self._up()
        return list(self.path_commits.get(path, []))

    def commit_pulls(self, sha):
        self._up()
        return [{k: v for k, v in p.items() if k != "merged_by"} for p in self.commit_prs.get(sha, [])]

    def issue_comments(self, number, since=None):
        self._up()
        return list(self.comments)

    def permission(self, user):
        self._up()
        return self.perms.get(user, "read")


class FakeRepo:
    """The data clone: the working tree is the world's folder; commits are snapshots."""

    def __init__(self, root):
        self.root, self.snapshots, self.ok, self.diff, self.sha, self.pushed = Path(root), {}, True, "", "c0", []

    def pull(self):
        return self.ok

    def head(self):
        return self.sha

    def files_at(self, sha, rel_dir):
        return self.snapshots.get((sha, rel_dir))

    def diff_since(self, sha):
        return self.diff

    def commit_and_push(self, paths, message):
        self.pushed.append(message)
        return True

    def snapshot(self, sha, rel_dir):
        d = self.root / rel_dir
        self.snapshots[(sha, rel_dir)] = {p.relative_to(d).as_posix(): p.read_bytes()
                                          for p in sorted(d.rglob("*")) if p.is_file()}
        return self.snapshots[(sha, rel_dir)]


# the boards as they ship, empty: a replay never starts from what the live boards hold
BOARDS = {
    "packs.md": "# Social pack registry\n\n" + mdtable.render(board.PACK_COLS, []) + "\n",
    "requests.md": ("# Social requests and commands\n\n## Requests\n\n" + mdtable.render(board.REQUEST_COLS, []) +
                    "\n\n## Commands\n\n" + mdtable.render(board.COMMAND_COLS, []) + "\n"),
    "image-spend.json": '{\n  "months": {}\n}\n',
}


class World:
    """Всички Казина on a clock: its repository, GitHub, the publisher, the site and Postiz."""

    brand = "vsichkikazina"

    def __init__(self, root, settings_text=SETTINGS, dry_run=False):
        self.root = Path(root)
        self.social = self.root / "VsichkiKazina" / "social"
        self.gh, self.repo = FakeGitHub(), FakeRepo(self.root)
        self.postiz = postiz.FakePostiz(CHANNELS)
        self.db = ledgermod.Ledger(":memory:")
        self.record, self.pages, self.fetched = {}, {}, []
        self.dry_run, self.n, self.queue = dry_run, 200, {}      # PR numbers given here start at 201
        self._setup(settings_text)

    # the repository
    def _setup(self, settings_text):
        (self.social / "prompts").mkdir(parents=True, exist_ok=True)
        for name, text in BOARDS.items():
            (self.social / name).write_bytes(text.encode("utf-8"))
        real = brands.ROOT / "VsichkiKazina" / "social"
        for name in ("visual-art.md", "visual-review.md"):
            shutil.copy(real / "prompts" / name, self.social / "prompts" / name)
        (self.root / "VsichkiKazina" / "affiliate-links.md").write_text(
            "| operator | affiliate_url |\n|---|---|\n| NV Casino | https://vsichkikazina.bg/go/nv/ |\n", encoding="utf-8")
        self.set_settings(settings_text, by="AmigoNiko", at="2026-11-01T10:00:00Z")

    def set_settings(self, text, by="AmigoNiko", at="2026-11-01T10:00:00Z", merged=True):
        """settings.md changes on main, through a PR merged by `by` (or by a direct push)."""
        rel = "VsichkiKazina/social/settings.md"
        (self.root / rel).write_bytes(text.encode("utf-8"))      # as git checks it out: LF, byte for byte
        if merged:
            self.n += 1
            sha = f"set{self.n}"
            pr = {"number": self.n, "state": "closed", "merged_at": at, "closed_at": at, "merge_commit_sha": sha,
                  "merged_by": {"login": by}, "base": {"ref": "main"}, "head": {"ref": f"settings-{self.n}", "sha": sha}}
            self.gh.prs[self.n] = pr
            self.gh.files[(sha, rel)] = text.encode("utf-8")
            self.gh.path_commits.setdefault(rel, []).insert(0, {"sha": sha})
            self.gh.commit_prs[sha] = [pr]
            return self.n
        return None

    def article(self, item_id, folder, text, status="approved", type_="guide", posted=""):
        d = self.root / "VsichkiKazina" / "articles" / folder
        (d / "images").mkdir(parents=True, exist_ok=True)
        (d / "05b-final-draft.md").write_text(text, encoding="utf-8")
        self.queue[item_id] = {"id": item_id, "status": status, "type": type_, "query": folder, "kw": folder,
                               "posted": posted, "folder": folder, "pr": item_id.split("-")[1]}
        self.rebuild()

    def set_status(self, item_id, status, posted=""):
        self.queue[item_id].update(status=status, posted=posted)
        self.rebuild()

    def rebuild(self):
        """The queue file and the article library, as approve-on-merge and social-board leave them."""
        text = QUEUE_HEAD + "".join(ROW.format(**r) for r in self.queue.values())
        (self.root / "VsichkiKazina" / "content-queue.md").write_text(text, encoding="utf-8")
        items, missing = build_library.build(self.root, self.brand, now="2026-11-01T00:00:00Z")
        build_library.write(self.root / "library" / self.brand, items, missing, self.brand)

    def draft(self, draft):
        draft = dict(draft, posts=[dict(dp, english=dp.get("english") or english(dp))   # the agent writes it with the post
                                   for dp in draft["posts"]])
        return make_pack.build(draft, self.brand, self.root, gemini=None, fetch=offline, now="2026-11-03T07:40:00Z")

    def edit_post(self, pack_id, post_id, **fields):
        from social import pack as packmod
        f = self.social / "packs" / pack_id / "posts" / f"{post_id}.md"
        got = packmod.parse_post_md(f.read_text(encoding="utf-8"))
        got.update(fields)
        f.write_text(packmod.render_post_md(post_id, got), encoding="utf-8")   # its English reference stays as it was

    def merge_pack(self, pack_id, at, by="AmigoNiko", fix=None, number=None, opened_by="px-drafting[bot]"):
        number = number or self._next()
        rel = f"VsichkiKazina/social/packs/{pack_id}"
        sha = f"m{number}"
        self.repo.snapshot(sha, rel)
        ref = f"social/vk/{pack_id}" + (f"-fix-{fix}" if fix else "")
        self.gh.prs[number] = {"number": number, "state": "closed", "merged_at": at, "closed_at": at,
                               "merge_commit_sha": sha, "merged_by": {"login": by}, "created_at": at,
                               "user": {"login": opened_by},
                               "base": {"ref": "main"}, "head": {"ref": ref, "sha": f"h{number}"}}
        return number

    def open_pack(self, pack_id, at, fix=None, number=None):
        number = number or self._next()
        ref = f"social/vk/{pack_id}" + (f"-fix-{fix}" if fix else "")
        raw = (self.social / "packs" / pack_id / "pack.json").read_bytes()
        self.gh.files[(f"h{number}", f"VsichkiKazina/social/packs/{pack_id}/pack.json")] = raw
        self.gh.prs[number] = {"number": number, "state": "open", "merged_at": None, "closed_at": None,
                               "merge_commit_sha": None, "merged_by": None, "created_at": at,
                               "base": {"ref": "main"}, "head": {"ref": ref, "sha": f"h{number}"}}
        return number

    def close_pack(self, number, at):
        self.gh.prs[number].update(state="closed", closed_at=at)

    def _next(self):
        self.n += 1
        return self.n

    # the publisher and the site
    def deploy(self, slug, path=None, html=None):
        self.record[slug] = {"path": path or f"blog/{slug}", "content_hash": "h", "deployed_utc": "t"}
        self.pages[f"https://vsichkikazina.bg/{(path or 'blog/' + slug).strip('/')}/"] = (200, html or "")

    def site_get(self, url):
        self.fetched.append(url)
        return self.pages.get(url, (404, ""))

    # the check
    def check(self, now, **env):
        client = postiz.DryRun(self.postiz) if self.dry_run else self.postiz
        e = pc.Env(self.root, self.db, client, self.gh, self.repo, lambda brand: dict(self.record),
                   site_get=self.site_get, now=now, enabled_brands={self.brand},
                   dry_run=self.dry_run, push=env.pop("push", True), **env)
        self.postiz.advance(now)
        return pc.Run(e, self.brand).go()

    def states(self):
        return {r["post_id"]: r["state"] for r in self.db.posts(self.brand)}

    def post(self, post_id):
        return self.db.post(post_id)

    def ledger(self):
        return json.loads((self.social / "ledger.json").read_text(encoding="utf-8"))


def vk0300(root):
    """Flow 0's example timeline, check by check. Returns (world, timeline)."""
    w = World(root)
    timeline = []

    def check(when, note):
        now = utc(when)
        w.check(now)
        rows = {r["post_id"]: (r["state"], r.get("planned_slot_utc") or r.get("published_utc") or "")
                for r in w.db.posts(w.brand)}
        timeline.append({"utc": when, "note": note, "posts": rows})

    # Mon 2 Nov 20:00 Sofia: Nikolay merges the article PR; approve-on-merge builds the library
    w.article("vk-0300", "2026-11-02-ruletka-shansove", ARTICLE)
    # Tue 3 Nov, about 09:40 Sofia: the drafting run opens the pack PR; social-pr adds the English
    w.draft(DRAFT_0300)
    # Tue 13:00 Sofia: one Bulgarian sentence of the Facebook post changed, then merged
    w.edit_post("vk-0300-p1", "vk-0300-p1-fb-1",
                text=f"{LINE_ODDS}\n\nКакво значи това за всеки ваш залог: [[LINK]]\n\n{COMPLIANCE}")
    w.merge_pack("vk-0300-p1", "2026-11-03T11:00:00Z", number=301)
    check("2026-11-03 12:10", "Tue 14:10 Sofia: the merge is confirmed; the article is not live yet")
    # Wed 4 Nov, about 08:45 Sofia: the publisher deploys vk-0300 and writes back posted
    w.deploy("ruletka-shansove", html=PAGE.format(pay=LINE_PAY, odds=LINE_ODDS))
    w.set_status("vk-0300", "posted", posted="2026-11-04")
    check("2026-11-04 07:10", "Wed 09:10 Sofia: go-live seen; each launch post planned for 12:30")
    check("2026-11-04 08:10", "Wed 10:10 Sofia: first check inside 09:30–12:00: handed over for 12:30")
    check("2026-11-04 09:10", "Wed 11:10 Sofia: nothing to do, the posts wait in the tool")
    check("2026-11-04 11:10", "Wed 13:10 Sofia: Published, with the network links")
    return w, timeline


def main(name):
    if name != "vk-0300":
        print(f"unknown recorded day {name!r} (vk-0300)")
        return 2
    tmp = Path(tempfile.mkdtemp(prefix="px-replay-"))
    try:
        w, timeline = vk0300(tmp)
        for step in timeline:
            print(f"{step['utc']} UTC  {step['note']}")
            for pid, (state, when) in sorted(step["posts"].items()):
                print(f"    {pid:<18} {state:<20} {when}")
        print("\nhanded to the tool (fake Postiz):")
        for p in w.postiz.items.values():
            print(f"    {p['channel_id']:<6} {p['date']}  {p['state']:<9} {postiz.normalize_content(p['content'])[:90]!r}")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "vk-0300"))
