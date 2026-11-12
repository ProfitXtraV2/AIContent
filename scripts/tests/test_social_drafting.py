import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_library as bl  # noqa: E402
from social import (checks, make_pack, mdtable, pack as packmod, pagetext, review_view, secret_scan,  # noqa: E402
                    settings as st, source_record, worklist)
from test_build_library import make_repo  # noqa: E402

ON = """## Brand
| key | value |
|---|---|
| social | on |
| compliance_long | 18+ Хазартът може да пристрасти. Играйте отговорно. |
| compliance_short | 18+ Играйте отговорно. |
| eligible_types | guide, comparison, review, news |
| allowed_link_areas | /blog/ |
| address_pattern | https://vsichkikazina.bg/blog/{slug}/ |
| identities_verified | 2026-11-01 |
| offer_words | бонус, оферта |
| register_words | регистрирайте се |
| packs_per_run | 2 |

## Accounts
| account_id | network | postiz_channel_id | active | posts_per_article | followup_delay_days | format | max_hashtags | link | slots | max_per_day | emoji | tone_override | test_post_seen | profile_link_set |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fb-vsichkikazina | facebook | ch-fb | on | 1 | 14 | auto | 3 | in post | daily 12:30, 19:30 | 2 | light |  | 2026-11-02 Ana | |
| ig-vsichkikazina | instagram | ch-ig | on | 1 | 14 | auto | 5 | profile | daily 12:30, 19:30 | 2 | light |  | 2026-11-02 Ana | 2026-11-03 |
| x-vsichkikazina | x | ch-x | on | 1 | 14 | single | 2 | in post | daily 12:30, 19:30 | 2 | light |  | 2026-11-02 Ana | |
| li-vsichkikazina | linkedin-page | ch-li | off | 1 | 14 | auto | 5 | in post | daily 12:30, 19:30 | 2 | none |  | | |
"""
LINE = "Банко 1:1 минус 5% комисиона."
DRAFT = {
    "brand": "vsichkikazina", "source": {"kind": "article", "item_id": "vk-0002"}, "request_id": None,
    "angle": "key takeaway", "posts": [
        {"account_id": "fb-vsichkikazina", "role": "launch", "angle": "one number",
         "text": "Разиграването x40 на бонуса е условие, не подарък.\n\nПрочетете: [[LINK]]\n\n"
                 "18+ Хазартът може да пристрасти. Играйте отговорно.",
         "hashtags": ["#разиграване"], "image_text": ["Какво значи x40"], "alt_text": "Катинар върху чипове",
         "english": {"text": "Wagering x40 on the bonus is a condition, not a gift.", "image_text": ["What x40 means"]},
         "art_idea": "a padlock on a stack of chips with looping arrows",
         "sources": [{"line": "x40 на бонуса.", "where": "Разиграване"}]},
        {"account_id": "ig-vsichkikazina", "role": "launch", "text": "Какво значи x40? Линкът е в профила ни.\n\n"
                                                                    "18+ Хазартът може да пристрасти. Играйте отговорно.",
         "hashtags": ["#разиграване", "#казино", "#правила"], "image_text": ["Какво значи x40"],
         "english": {"text": "What does x40 mean? The link is in our profile.", "image_text": ["What x40 means"]},
         "alt_text": "Катинар", "art_idea": "padlock", "sources": [{"line": "x40 на бонуса.", "where": "Разиграване"}]},
        {"account_id": "li-vsichkikazina", "role": "launch", "text": "inactive", "hashtags": [], "image_text": ["x"],
         "alt_text": "", "sources": []},
    ]}


def offline(url, **kwargs):
    """Tests never reach the live site."""
    raise OSError("offline in tests")


def repo_on(tmp):
    root = make_repo(tmp)
    (root / "VsichkiKazina" / "social" / "settings.md").write_text(ON, encoding="utf-8")
    for name in ("packs.md", "requests.md", "image-spend.json"):
        src = Path(__file__).resolve().parent / "fixtures" / "social" / name          # as shipped, not live
        (root / "VsichkiKazina" / "social" / name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    prompts = root / "VsichkiKazina" / "social" / "prompts"
    prompts.mkdir()
    for name in ("visual-art.md", "visual-review.md"):
        (prompts / name).write_text((Path(__file__).resolve().parents[2] / "VsichkiKazina" / "social" / "prompts" / name)
                                    .read_text(encoding="utf-8"), encoding="utf-8")
    items, missing = bl.build(root)
    bl.write(root / "library" / "vsichkikazina", items, missing, "vsichkikazina")
    return root


# --- page text and source records ---------------------------------------------------------

PAGE = """<html><head><script>var x = "Банко 1:1";</script></head><body><nav>Меню</nav>
<article><h1>Бакара</h1><p>Банко&nbsp;1:1 минус 5%
комисиона.</p><footer>18+</footer></article></body></html>"""


def test_visible_text_and_records():
    text = pagetext.visible_text(PAGE)
    assert text == "Бакара\nБанко 1:1 минус 5%\nкомисиона."
    assert pagetext.contains(text, LINE)
    s = st.parse(ON)
    rec = source_record.record("https://vsichkikazina.bg/blog/bakara-pravila/", [LINE, "Равенство 9:1."], "vsichkikazina",
                               s.brand, fetch=lambda url: PAGE)
    assert (rec["lines"], rec["missing"]) == ([LINE], ["Равенство 9:1."])
    bad = source_record.record("https://vsichkikazina.bg/casino/betano/", [LINE], "vsichkikazina", s.brand, fetch=lambda u: PAGE)
    assert bad["lines"] == [] and bad["error"].startswith("not an allowed page")


# --- the work list --------------------------------------------------------------------------

def test_work_list(tmp_path):
    root = repo_on(tmp_path)
    s = st.load("vsichkikazina", root)
    index = bl.load_index(root, "vsichkikazina")
    items = {e["slug"]: bl.load_item(root, "vsichkikazina", e["slug"])[0] for e in index["items"]}
    merged = {2: "2026-11-02T10:00:00Z", 5: "2026-11-02T09:00:00Z"}
    requests = [{"id": "vk-req-001", "kind": "article", "target": "vk-0001", "status": "open", "angle": "второ"},
                {"id": "vk-req-002", "kind": "article", "target": "nope", "status": "open"},
                {"id": "vk-req-003", "kind": "keyword", "target": "бакара стратегия", "status": "open"},
                {"id": "vk-req-004", "kind": "intro", "target": "hub-intro-casino-payments", "status": "open"}]
    w = worklist.work_list(s, index, items, [], requests, ["NV Casino"], "2026-11-01T00:00:00Z", merged.get)
    assert w["brand_off"] == ""
    assert [n["item_id"] for n in w["new"]] == ["vk-0002"]                  # vk-0005 is an operator article
    assert w["skipped"] == [{"item_id": "vk-0005", "slug": "nv-casino-bonus",
                             "reason": "operator or bonus article (names the operator NV Casino)"}]
    assert [r["request_id"] for r in w["requests"]] == ["vk-req-001"]        # cap 2: one article, one request
    assert w["waiting"] == 2
    assert w["failed_requests"] == [{"id": "vk-req-002", "reason": "not in the approved feed"}]
    # approved before social was switched on: never automatic (A4, A5)
    w = worklist.work_list(s, index, items, [], [], ["NV Casino"], "2026-11-05T00:00:00Z", merged.get)
    assert w["new"] == []
    # already has a pack (A3)
    w = worklist.work_list(s, index, items, [{"pack_id": "vk-0002-p1", "source": "vk-0002", "status": "merged"}], [],
                         ["NV Casino"], "2026-11-01T00:00:00Z", merged.get)
    assert w["new"] == []
    # social off: nothing new, but fixes still listed
    off = st.parse(ON.replace("| social | on |", "| social | off |"))
    w = worklist.work_list(off, index, items, [], [], [], None, merged.get,
                         ledger_posts=[{"post_id": "vk-0002-p1-fb-1", "pack_id": "vk-0002-p1", "state": "needs_fix",
                                        "reason": "text differs from approved"}],
                         commands=[{"id": "vk-cmd-001", "kind": "fix", "post_id": "vk-0002-p1-x-1"}])
    assert w["brand_off"] == "social is off" and w["new"] == []
    assert w["fixes"] == [{"pack_id": "vk-0002-p1", "posts": [
        {"post_id": "vk-0002-p1-fb-1", "why": "text differs from approved"},
        {"post_id": "vk-0002-p1-x-1", "why": "fix line vk-cmd-001"}]}]


def test_redo_notes_and_redrafts(tmp_path):
    root = repo_on(tmp_path)
    s = st.load("vsichkikazina", root)
    index = bl.load_index(root, "vsichkikazina")
    items = {e["slug"]: bl.load_item(root, "vsichkikazina", e["slug"])[0] for e in index["items"]}
    prs = [{"pack_id": "vk-0002-p1", "number": 410, "handled": [11],
            "comments": [{"id": 11, "body": "/redo vk-0002-p1-fb-1 по-кратко"},
                         {"id": 12, "body": "/redo vk-0002-p1-fb-1, vk-0002-p1-ig-1 без въпрос в началото"},
                         {"id": 13, "body": "Хубаво!"}],
            "images_out_of_date": ["vk-0002-p1-ig-1"],
            "source": {"item_id": "vk-0002", "article_version": "old"}}]
    w = worklist.work_list(s, index, items, [], [], [], None, lambda n: None, open_prs=prs)
    assert w["redo"] == [{"pack_id": "vk-0002-p1", "pr": 410, "comment_id": 12,
                          "post_ids": ["vk-0002-p1-fb-1", "vk-0002-p1-ig-1"], "note": "без въпрос в началото"}]
    assert w["redraw"] == [{"pack_id": "vk-0002-p1", "pr": 410, "post_ids": ["vk-0002-p1-ig-1"]}]
    assert w["redraft"][0]["item_id"] == "vk-0002" and w["redraft"][0]["from_version"] == "old"
    assert worklist.parse_redo("/redo vk-0300-p1-x-2 fix it") == (["vk-0300-p1-x-2"], "fix it")
    assert worklist.parse_redo("please /redo") is None


# --- building a pack ------------------------------------------------------------------------

def test_build_a_pack(tmp_path):
    root = repo_on(tmp_path)
    d, summary = make_pack.build(DRAFT, "vsichkikazina", root, gemini=None, fetch=offline, now="2026-11-03T09:40:00Z")
    assert summary["pack_id"] == "vk-0002-p1" and summary["branch"] == "social/vk/vk-0002-p1"
    assert summary["title"] == "Social: Разиграване (Всички Казина) — 2 posts"
    assert summary["posts"] == ["vk-0002-p1-fb-1", "vk-0002-p1-ig-1"]
    assert summary["notes"] == ["li-vsichkikazina: not an active account without errors; post dropped"]
    p = packmod.load(d)
    fb, ig = p["meta"]["posts"]
    assert fb["link"] == {"mode": "placeholder", "campaign": "razigravane", "content": "vk-0002-p1-fb-1"}
    assert ig["link"] == {"mode": "none", "reason": "link in profile"}
    assert fb["numbers"] == [{"value": "x40", "source_index": 0}]
    assert [(v["kind"], v["fallback_case"]) for v in fb["visuals"]] == [("text-card", "images: fallback (generation unavailable)")]
    assert (d / "visuals" / "vk-0002-p1-fb-1-1.jpg").exists()
    assert p["meta"]["source"]["article_version"] == bl.load_item(root, "vsichkikazina", "razigravane")[0]["article_version"]
    # every check passes: the English reference came with the draft, and it is no check anyway
    assert summary["failing"] == [] and summary["checks_ok"] is True
    assert "| `vk-0002-p1-fb-1` | fb-vsichkikazina | Facebook | single |" in summary["pr_body"]
    # a second pack of the same article (a request) gets number 2, never reusing IDs
    d2, s2 = make_pack.build(dict(DRAFT, request_id="vk-req-001"), "vsichkikazina", root, gemini=None, fetch=offline)
    assert s2["pack_id"] == "vk-0002-p2" and s2["posts"][0] == "vk-0002-p2-fb-1"


def test_build_from_page_records(tmp_path):
    root = repo_on(tmp_path)
    draft = {"brand": "vsichkikazina", "request_id": "vk-req-003", "angle": "бакара",
             "source": {"kind": "page", "request_id": "vk-req-003",
                        "pages": [{"url": "https://vsichkikazina.bg/blog/bakara-pravila/", "lines": [LINE]}]},
             "posts": [{"account_id": "x-vsichkikazina", "role": "request", "text": "Бакара: " + LINE + " [[LINK]] 18+ Играйте отговорно.",
                        "hashtags": ["#бакара"], "image_text": ["Бакара"], "alt_text": "Бакара",
                        "target_page": "https://vsichkikazina.bg/blog/bakara-pravila/",
                        "sources": [{"line": LINE, "where": "https://vsichkikazina.bg/blog/bakara-pravila/"},
                                    {"line": "Равенство 9:1.", "where": "https://vsichkikazina.bg/blog/bakara-pravila/"}]}]}
    d, summary = make_pack.build(draft, "vsichkikazina", root, gemini=None, fetch=lambda url, **k: PAGE)
    assert summary["pack_id"] == "vk-req-003-p1"
    p = packmod.load(d)
    post = p["meta"]["posts"][0]
    assert post["post_id"] == "vk-req-003-p1-x-1"
    assert post["link"] == {"mode": "placeholder", "campaign": "vk-req-003", "content": "vk-req-003-p1-x-1",
                            "target": "https://vsichkikazina.bg/blog/bakara-pravila/"}
    assert "[VERIFY: not found in the recorded source: Равенство 9:1.]" in p["posts"][post["post_id"]]["text"]
    assert ("vk-req-003-p1-x-1", "verify") in summary["failing"] and ("vk-req-003-p1-x-1", "sources") in summary["failing"]


def add_request(root, **row):
    req = root / "VsichkiKazina" / "social" / "requests.md"
    text = req.read_text(encoding="utf-8")
    t = mdtable.find(text, "kind", "target")
    req.write_text(mdtable.replace(text, t, t["rows"] + [row]), encoding="utf-8")


def test_work_list_topics_and_bad_requests(tmp_path):
    root = repo_on(tmp_path)
    s = st.load("vsichkikazina", root)
    index = bl.load_index(root, "vsichkikazina")
    requests = [{"id": "vk-req-005", "kind": "topic", "target": "Три залога в бакара", "status": "open",
                 "format": "carousel", "slides": "4", "sources": "https://example.org/bakara, sources/bakara-notes.md"},
                {"id": "vk-req-006", "kind": "topic", "target": "x", "status": "open", "slides": "15"}]
    w = worklist.work_list(s, index, {}, [], requests, [], None, lambda n: None)
    assert w["requests"] == [{"kind": "request", "request_id": "vk-req-005", "request_kind": "topic",
                              "topic": "Три залога в бакара", "angle": "", "target_page": "", "accounts": "",
                              "earliest": "", "format": "carousel", "slides": "4",
                              "sources": ["https://example.org/bakara", "sources/bakara-notes.md"]}]
    assert w["failed_requests"] == [{"id": "vk-req-006", "reason": "slides must be 3–10 (or empty for the account's), not '15'"}]


def test_build_a_topic_pack_from_named_sources(tmp_path):
    """A free topic: facts from a page and a text the request names, and from one of our articles;
    a carousel of the request's slides, made without generated art (no image key)."""
    root = repo_on(tmp_path)
    add_request(root, id="vk-req-005", kind="topic", target="Три залога в бакара", format="carousel", slides="4",
                sources="https://example.org/bakara, sources/bakara-notes.md")
    notes = root / "VsichkiKazina" / "social" / "sources"
    notes.mkdir()
    (notes / "bakara-notes.md").write_text("# Бележки\n\nРавенство 8:1 се плаща **рядко**.\n", encoding="utf-8")
    (notes / "other.md").write_text("Равенство 8:1 се плаща рядко.\n", encoding="utf-8")
    outside = "<html><body><p>Пунто плаща 1:1.</p></body></html>"
    lines = ["Пунто плаща 1:1.", "Равенство 8:1 се плаща рядко.", LINE]
    draft = {"brand": "vsichkikazina", "request_id": "vk-req-005", "angle": "три залога",
             "source": {"kind": "page", "request_id": "vk-req-005",
                        "pages": [{"url": "https://example.org/bakara", "lines": [lines[0]]}],
                        "texts": [{"ref": "sources/bakara-notes.md", "lines": [lines[1]]},
                                  {"ref": "vk-0001", "lines": [lines[2]]},
                                  {"ref": "sources/other.md", "lines": [lines[1]]}]},
             "posts": [{"account_id": "ig-vsichkikazina", "role": "request",
                        "text": "Бакара има три залога. Пунто плаща 1:1, равенство 8:1.\n\n"
                                "18+ Хазартът може да пристрасти. Играйте отговорно.",
                        "hashtags": ["#бакара", "#казиноигри"],
                        "image_text": ["Три залога в бакара", "Пунто плаща 1:1", "Равенство 8:1", "Запазете поста"],
                        "alt_text": "Три залога в бакара",
                        "sources": [{"line": ln, "where": w} for ln, w in zip(lines, ["https://example.org/bakara",
                                                                                     "sources/bakara-notes.md", "vk-0001"])]}]}
    d, summary = make_pack.build(draft, "vsichkikazina", root, gemini=None, fetch=lambda url, **k: outside)
    p = packmod.load(d)
    post = p["meta"]["posts"][0]
    recs = p["meta"]["source"]["records"]
    assert [(r["kind"], r.get("url") or r.get("file") or r.get("item_id"), r["lines"]) for r in recs] == [
        ("outside", "https://example.org/bakara", [lines[0]]), ("text", "sources/bakara-notes.md", [lines[1]]),
        ("text", "vk-0001", [lines[2]]), ("text", "sources/other.md", [])]
    assert recs[3]["error"] == "the request does not name this file"
    assert (post["format"], post["slides"]) == ("carousel", 4)                 # the request's, not the account's auto
    assert [(v["role"], v["kind"]) for v in post["visuals"]] == [("cover", "text-card"), ("point", "text-card"),
                                                                  ("point", "text-card"), ("closing", "text-card")]
    assert "[VERIFY" not in p["posts"][post["post_id"]]["text"]
    assert summary["failing"] == []
    assert "- https://example.org/bakara (a page the request named, read " in summary["pr_body"]


# --- the review view, the English reference, the key scan ----------------------------------

def test_review_view_english_reference_and_marker(tmp_path):
    root = repo_on(tmp_path)
    d, summary = make_pack.build(DRAFT, "vsichkikazina", root, gemini=None, fetch=offline)
    p = packmod.load(d)
    fb = p["posts"]["vk-0002-p1-fb-1"]
    assert fb["english"] == "Text:\nWagering x40 on the bonus is a condition, not a gift.\n\nImage text:\n- What x40 means"
    assert packmod.english_current(p["meta"]["posts"][0], fb) and summary["failing"] == []
    s = st.load("vsichkikazina", root)
    result = checks.run(p, checks.context_for(p, "vsichkikazina", root))
    body = review_view.render(p, result, s, "vsichkikazina", commit_sha="abc123")
    assert ("raw.githubusercontent.com/ProfitXtraV2/AIContent/abc123/VsichkiKazina/social/packs/vk-0002-p1/visuals/"
            "vk-0002-p1-fb-1-1.jpg") in body
    assert "https://vsichkikazina.bg/blog/razigravane/?utm_source=facebook&utm_medium=social&utm_campaign=razigravane" \
           "&utm_content=vk-0002-p1-fb-1" in body
    assert "- `x40` — „x40 на бонуса.“ (Разиграване)" in body
    assert "Wagering x40 on the bonus" in body and "Written before the last edit" not in body
    r = checks.run(p, checks.context_for(p, "vsichkikazina", root, pr_body=body))
    assert r["ok"] is True                                                  # every check, the review view included
    # a person edits the text in the PR: the English is out of date, which the view says; nothing waits for it
    edit = d / "posts" / "vk-0002-p1-fb-1.md"
    edit.write_text(edit.read_text(encoding="utf-8").replace("не подарък", "а не подарък"), encoding="utf-8")
    p = packmod.load(d)
    r = checks.run(p, checks.context_for(p, "vsichkikazina", root, pr_body=body))
    assert not [x["check"] for rs in r["posts"].values() for x in rs if not x["ok"]]
    assert [x["check"] for x in r["pack"] if not x["ok"]] == ["review-view"]          # only: the view is older than the files
    body = review_view.render(p, r, s, "vsichkikazina", commit_sha="abc124")
    stale = body.split("### `vk-0002-p1-fb-1`")[1].split("### ")[0]
    assert "⚠️ Written before the last edit of the text or the image text" in stale
    assert "Written before the last edit" not in body.split("### `vk-0002-p1-ig-1`")[1]
    # the agent rewrites a post (a redo): it writes the English again with `make_pack.py english`
    assert make_pack.english(d, {"vk-0002-p1-fb-1": {"text": "Wagering x40 is a condition and not a gift."}}) == ["vk-0002-p1-fb-1"]
    p = packmod.load(d)
    assert packmod.english_current(p["meta"]["posts"][0], p["posts"]["vk-0002-p1-fb-1"])
    assert p["posts"]["vk-0002-p1-fb-1"]["english"] == "Text:\nWagering x40 is a condition and not a gift."
    # a draft without English: a note, no failing check, and the view says there is none
    bare = dict(DRAFT, request_id="vk-req-001", posts=[{k: v for k, v in dp.items() if k != "english"} for dp in DRAFT["posts"]])
    d2, summary2 = make_pack.build(bare, "vsichkikazina", root, gemini=None, fetch=offline)
    assert "vk-0002-p2-fb-1: no English reference in the draft" in summary2["notes"] and summary2["failing"] == []
    assert "(none: the AI did not write one)" in summary2["pr_body"]


def test_secret_scan(tmp_path):
    key = "AIza" + "B" * 35
    header = "-----BEGIN OPENSSH " + "PRIVATE KEY-----"        # built here, so this file holds no key header
    found = secret_scan.scan_text(f"line\nGEMINI={key}\n{header}\n", "x.md")
    assert found == [{"kind": "google-api-key", "where": "x.md", "line": 2},
                     {"kind": "private-key", "where": "x.md", "line": 3}]
    assert secret_scan.scan_text("token ghp_" + "a" * 36) [0]["kind"] == "github-token"
    assert secret_scan.scan_text("postiz: s3cr3t-value-123", own_secrets={"postiz-key": "s3cr3t-value-123"}) == \
        [{"kind": "postiz-key", "where": "text", "line": 1}]
    assert secret_scan.scan_text("nothing here, AIza short") == []
    (tmp_path / "a.md").write_text(f"x {key}", encoding="utf-8")
    assert secret_scan.main([str(tmp_path)]) == 1
