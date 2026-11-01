import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from social import checks, pack as packmod  # noqa: E402
from social_fixtures import edit_meta, edit_post, make_pack  # noqa: E402

FB, IG, X = "vk-0001-p1-fb-1", "vk-0001-p1-ig-1", "vk-0001-p1-x-1"


def run(root, d, pr_body=None):
    p = packmod.load(d)
    return checks.run(p, checks.context_for(p, "vsichkikazina", root, pr_body))


def failing(result):
    return sorted((pid, r["check"]) for pid, rs in result["posts"].items() for r in rs if not r["ok"]) + \
        sorted(("pack", r["check"]) for r in result["pack"] if not r["ok"])


def detail(result, pid, check):
    return next(r["detail"] for r in result["posts"][pid] if r["check"] == check)


def test_a_good_pack_passes_every_check(tmp_path):
    root, d = make_pack(tmp_path)
    r = run(root, d)
    assert failing(r) == [], r
    assert r["ok"] and sorted(r["posts"]) == [FB, IG, X]
    assert detail(r, FB, "link") == "https://vsichkikazina.bg/blog/bakara-pravila/ (filled in when live)"
    assert detail(r, IG, "carousel") == "4 slides"


def test_advertising_and_numbers(tmp_path):
    root, d = make_pack(tmp_path)
    edit_post(d, FB, text=packmod.parse_post_md((d / "posts" / f"{FB}.md").read_text(encoding="utf-8"))["text"]
              + "\nВ NV Casino бонус 100% до €200. Регистрирайте се сега!")
    edit_post(d, X, image_text=["Предимство 1,25%"])
    r = run(root, d)
    assert ("vk-0001-p1-fb-1", "advertising") in failing(r)
    adv = detail(r, FB, "advertising")
    assert "text names NV Casino" in adv and "text states an offer amount (100%" in adv \
        and "invites to register or deposit ('регистрирайте се')" in adv
    assert detail(r, FB, "numbers") == "100% is not in a source line; €200 is not in a source line"
    assert detail(r, X, "numbers") == "1,25% is not in a source line"
    assert (X, "images-fresh") in failing(r) and not [c for _p, c in failing(r) if c == "english-reference"]


def test_compliance_hashtags_verify_and_instagram_address(tmp_path):
    root, d = make_pack(tmp_path)
    edit_post(d, FB, text="Бакара [[LINK]]", hashtags=["#a", "#b", "#c", "#d"])
    edit_post(d, IG, text="Вижте vsichkikazina.bg/blog/ [VERIFY: проверка]\n\n18+ Хазартът може да пристрасти. Играйте отговорно.")
    r = run(root, d)
    f = failing(r)
    assert (FB, "compliance") in f and (FB, "hashtags") in f
    assert detail(r, FB, "hashtags").startswith("4 (account max 3")
    assert (IG, "instagram-url") in f and (IG, "verify") in f
    assert detail(r, IG, "verify") == "[VERIFY: проверка]"


def test_x_uses_the_short_compliance_line_and_its_weighted_length(tmp_path):
    root, d = make_pack(tmp_path)
    r = run(root, d)
    assert detail(r, X, "length").startswith("8") or int(detail(r, X, "length").split()[0]) < 280
    edit_post(d, X, text="Бакара " * 40 + "[[LINK]] 18+ Играйте отговорно.")
    r = run(root, d)
    assert (X, "length") in failing(r)


def test_links(tmp_path):
    root, d = make_pack(tmp_path)

    def bad_links(meta):
        meta["posts"][0]["link"]["campaign"] = "other"
        meta["posts"][1]["link"] = {"mode": "placeholder", "campaign": "bakara-pravila", "content": IG}
        meta["posts"][2]["link"] = {"mode": "none", "reason": "because"}
    edit_meta(d, bad_links)
    r = run(root, d)
    assert detail(r, FB, "link") == "utm_campaign 'other' should be 'bakara-pravila'"
    assert "Instagram posts carry no link (link in profile)" in detail(r, IG, "link")
    assert "no allowed reason" in detail(r, X, "link") and "holds [[LINK]]" in detail(r, X, "link")


def test_sources_and_article_changes(tmp_path):
    root, d = make_pack(tmp_path)
    edit_meta(d, lambda m: m["posts"][0]["sources"].append({"line": "Равенство плаща 9:1.", "where": "x"}))
    r = run(root, d)
    assert detail(r, FB, "sources") == "not in the article: Равенство плаща 9:1."
    edit_meta(d, lambda m: m["source"].update(article_version="0" * 64))
    r = run(root, d)
    assert "article changed since drafting" in detail(r, X, "sources")


def test_carousel_and_visuals(tmp_path):
    root, d = make_pack(tmp_path)
    (d / "visuals" / f"{IG}-3.jpg").unlink()                       # a person deleted a slide
    (d / "visuals" / f"{X}-1.jpg").unlink()
    r = run(root, d)
    assert detail(r, IG, "carousel") == "4 image text lines for 3 slides"
    assert (X, "visual") in failing(r)


def test_carousel_slides_as_set(tmp_path):
    root, d = make_pack(tmp_path)
    edit_meta(d, lambda m: m["posts"][1].update(slides=5))           # 4 slides when 5 are set: fewer points
    assert detail(run(root, d), IG, "carousel") == "4 slides (5 set: the source has fewer points)"
    edit_meta(d, lambda m: m["posts"][1].update(slides=3))
    assert detail(run(root, d), IG, "carousel") == "4 slides, more than the 3 set"


def test_deleted_posts_leave_the_pack_and_the_review_view(tmp_path):
    root, d = make_pack(tmp_path)
    (d / "posts" / f"{X}.md").unlink()
    r = run(root, d, pr_body="no marker")
    assert r["deleted"] == [X] and X not in r["posts"]
    assert failing(r) == [("pack", "review-view")]
    marker = f"<!-- view:{packmod.files_hash(d)} -->"
    r = run(root, d, pr_body="Review view\n" + marker)
    assert failing(r) == []
    md = checks.markdown(r, "vk-0001-p1")
    assert "all passing" in md and f"`{X}`" in md.split("Deleted in this PR")[1]


def test_cli(tmp_path):
    root, d = make_pack(tmp_path)
    out = tmp_path / "result.json"
    assert checks.main([str(d), "--root", str(root), "--json", str(out), "--markdown", str(tmp_path / "c.md")]) == 0
    assert out.exists() and (tmp_path / "c.md").read_text(encoding="utf-8").startswith("### Social checks — vk-0001-p1")

