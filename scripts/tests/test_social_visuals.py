import json
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import settings as st, spend as spendmod, visuals  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
SETTINGS = st.parse((Path(__file__).resolve().parent / "fixtures" / "social" / "settings.md").read_text(encoding="utf-8"))
TEMPLATE = (REPO / "VsichkiKazina" / "social" / "prompts" / "visual-art.md").read_text(encoding="utf-8")
PASS = "SCORE: 91\nVERDICT: PASS\nINTEGRITY: OK\nLAYOUT: OK\n"
WORK = "SCORE: 64\nVERDICT: NEEDS WORK\nINTEGRITY: OK\nLAYOUT: OK\nThe metaphor is generic."


class FakeGemini:
    def __init__(self, verdicts=(PASS,), fail_generate="", fail_review="", fail_from=None):
        self.verdicts, self.fail_generate, self.fail_review = list(verdicts), fail_generate, fail_review
        self.fail_from = fail_from                      # the call number from which generation fails
        self.prompts, self.reviews, self.refs, self.inputs = [], [], [], []

    def generate(self, prompt, out_png, aspect, size="2K", refs=()):
        self.prompts.append((prompt, aspect))
        self.refs.append([Path(r).name for r in refs])
        if self.fail_generate or (self.fail_from and len(self.prompts) >= self.fail_from):
            return False, self.fail_generate or "GEMINI_ERROR: HTTP 500"
        a, b = (int(x) for x in aspect.split(":"))
        colour = (20, 90, 70) if len(self.prompts) == 1 else (200, 60, 30)      # the cover, then the points
        Image.new("RGB", (1600, round(1600 * b / a)), colour).save(out_png)
        return True, ""

    def review(self, article_file, images, usage_out):
        self.reviews.append([Path(i).name for i in images])
        self.inputs.append(Path(article_file).read_text(encoding="utf-8"))
        if self.fail_review:
            return False, "", self.fail_review
        Path(usage_out).write_text(json.dumps({"usageMetadata": {"promptTokenCount": 4000, "candidatesTokenCount": 300}}))
        return True, self.verdicts.pop(0) if len(self.verdicts) > 1 else self.verdicts[0], ""


POST = {"post_id": "vk-0001-p1-fb-1", "network": "facebook", "art_idea": "two cards on a balance scale",
        "sources": [{"line": "Банко 1:1 минус 5% комисиона."}]}
FIELDS = {"text": "x", "image_text": ["Три залога в бакара"], "alt_text": "", "hashtags": []}
ITEM = {"kind": "article", "slug": "bakara-pravila", "images": [
    {"name": "bakara-hero.webp", "path": "hero.webp", "alt": "Две карти на везни",
     "review": {"score": 95, "integrity_ok": True, "source": "08-image-review-2.md"}}]}


def ctx(tmp, gemini, budget=60.0, item=None, fetch=None, page_url=None, ops=("Betano",), settings=SETTINGS, styled=False):
    (tmp / "pack" / "visuals").mkdir(parents=True, exist_ok=True)
    if item:
        Image.new("RGB", (1200, 400), (10, 20, 60)).save(tmp / "hero.webp")
    s = spendmod.Spend(tmp / "spend.json", "vsichkikazina", budget)
    style, refs = visuals.load_style("vsichkikazina", REPO) if styled else ("", [])
    return visuals.Ctx("vsichkikazina", tmp / "pack", settings, s, gemini, item, tmp, list(ops), TEMPLATE,
                       fetch=fetch, page_url=page_url, style=style, refs=refs)


def test_a_passing_first_attempt(tmp_path):
    g = FakeGemini()
    c = ctx(tmp_path, g)
    vis, notes, fmt = visuals.make(POST, FIELDS, c)
    assert (fmt, notes) == ("single", [])
    assert [(v["file"], v["kind"], v["role"], v["score"]) for v in vis] == [("vk-0001-p1-fb-1-1.jpg", "generated", "single", 91)]
    assert Image.open(tmp_path / "pack" / "visuals" / "vk-0001-p1-fb-1-1.jpg").size == (1080, 1350)
    assert g.prompts[0][1] == "4:5" and "two cards on a balance scale" in g.prompts[0][0]
    assert "NO text, NO numbers" in g.prompts[0][0]
    spent = json.loads((tmp_path / "spend.json").read_text())["months"]
    entry = next(iter(spent.values()))["vsichkikazina"]
    assert (entry["images"], entry["reviews"]) == (1, 1) and entry["usd"] > 0.134


def test_three_failing_attempts_use_the_articles_own_image(tmp_path):
    g = FakeGemini([WORK, WORK, WORK])
    vis, notes, fmt = visuals.make(POST, FIELDS, ctx(tmp_path, g, item=ITEM))
    assert len(g.prompts) == 3 and "Avoid the problems" in g.prompts[1][0]
    assert notes == ["visual needs attention"]
    assert [(v["kind"], v["fallback_case"], v["score"]) for v in vis] == [("article-image", "visual needs attention", 95)]


def test_no_social_key_falls_back_without_using_any_key(tmp_path):
    item = dict(ITEM, images=[dict(ITEM["images"][0], alt="Betano лого")])     # alt names an operator: skipped
    page = ('<html><head><meta property="og:image" content="https://vsichkikazina.bg/assets/img/og/bakara.webp">'
            '<meta property="og:title" content="Бакара: правила"></head></html>')
    card = Image.new("RGB", (1200, 630), (200, 200, 200))
    import io
    buf = io.BytesIO()
    card.save(buf, "PNG")

    def fetch(url, binary=False):
        return buf.getvalue() if binary else page
    vis, notes, _ = visuals.make(POST, FIELDS, ctx(tmp_path, None, item=item, fetch=fetch,
                                                   page_url="https://vsichkikazina.bg/blog/bakara-pravila/"))
    assert notes == ["images: fallback (generation unavailable)"]
    assert [(v["kind"], v["role"]) for v in vis] == [("social-card", "single")]


def test_budget_reached_gives_a_text_card(tmp_path):
    g = FakeGemini()
    vis, notes, _ = visuals.make(POST, FIELDS, ctx(tmp_path, g, budget=0.05))
    assert g.prompts == []                                                  # nothing generated
    assert notes == ["images: fallback (budget reached)"]
    assert [(v["kind"], v["image_text_hash"] is not None) for v in vis] == [("text-card", True)]


def test_credits_exhausted_is_noted(tmp_path):
    g = FakeGemini(fail_generate="GEMINI_ERROR: HTTP 429 b'RESOURCE_EXHAUSTED: prepayment credits are depleted'")
    c = ctx(tmp_path, g)
    vis, notes, _ = visuals.make(POST, FIELDS, c)
    assert notes == ["images: fallback (budget reached)"] and vis[0]["kind"] == "text-card"
    assert c.spend.entry["credits_exhausted"] is True
    assert c.spend.can_spend(0.1) == (False, "credits exhausted")


def test_review_unavailable_never_ships_a_generated_image(tmp_path):
    g = FakeGemini(fail_review="GEMINI_ERROR: HTTP 503")
    vis, notes, _ = visuals.make(POST, FIELDS, ctx(tmp_path, g))
    assert notes == ["images: fallback (review unavailable)"] and vis[0]["kind"] == "text-card"


def test_carousels(tmp_path):
    g = FakeGemini()
    post = dict(POST, post_id="vk-0001-p1-ig-1", network="instagram")
    fields = dict(FIELDS, image_text=["Бакара накратко", "Банко 1:1", "Пунто", "Равенство", "Прочетете ръководството"])
    vis, notes, fmt = visuals.make(post, fields, ctx(tmp_path, g), account_format="auto")
    assert fmt == "carousel" and [v["role"] for v in vis] == ["cover", "point", "point", "point", "closing"]
    assert g.reviews == [[f"try-1-{i}.jpg" for i in range(1, 6)]]          # all slides in one review
    assert {Image.open(tmp_path / "pack" / "visuals" / v["file"]).size for v in vis} == {(1080, 1350)}
    post_x = dict(POST, post_id="vk-0001-p1-x-1", network="x")
    vis, notes, fmt = visuals.make(post_x, fields, ctx(tmp_path, FakeGemini()), account_format="carousel")
    assert (fmt, notes) == ("single", ["carousel not offered on x: single image"])
    assert Image.open(tmp_path / "pack" / "visuals" / vis[0]["file"]).size == (1600, 900)


def test_no_image_title_holds_the_post(tmp_path):
    vis, notes, _ = visuals.make(POST, dict(FIELDS, image_text=[]), ctx(tmp_path, FakeGemini()))
    assert vis == [] and notes == ["Held: no visual (no image title)"]


def test_verdicts():
    assert visuals.parse_verdict(PASS) == {"score": 91, "integrity_ok": True, "layout_ok": True, "passed": True}
    assert visuals.parse_verdict("SCORE: 95\nINTEGRITY FAILURE: a fake slot screen")["passed"] is False
    assert visuals.parse_verdict("SCORE: 90\nLAYOUT DEFECT: „комисиона“ is clipped")["passed"] is False
    assert visuals.parse_verdict("**Score: 85/100** · PASS. No integrity failure, nothing clipped.")["passed"] is True
    assert visuals.parse_verdict("SCORE: 88 — the word „залога“ is clipped at the right edge")["passed"] is False
    assert visuals.parse_verdict("Score: 79/100")["passed"] is False
    assert visuals.plan_format("auto", "instagram", ["a", "b", "c"]) == ("single", "")
    assert visuals.plan_format("auto", "instagram", list("abcd")) == ("carousel", "")
    assert visuals.plan_format("carousel", "facebook", list("abc")) == ("carousel", "")
    assert visuals.plan_format("carousel", "facebook", list("abcdefghij")) == ("carousel", "")
    assert visuals.plan_format("carousel", "facebook", list("abcdefghijk")) == \
        ("single", "a carousel needs 3–10 image text lines: single image")
    assert visuals.plan_format("carousel", "instagram", ["a", "b"]) == \
        ("single", "a carousel needs 3–10 image text lines: single image")


def test_a_carousel_without_generated_art_keeps_its_slides(tmp_path):
    post = dict(POST, post_id="vk-0001-p1-ig-1", network="instagram")
    fields = dict(FIELDS, image_text=["Бакара накратко", "Банко 1:1", "Пунто", "Прочетете ръководството"])
    vis, notes, fmt = visuals.make(post, fields, ctx(tmp_path, None, item=ITEM), account_format="carousel")
    assert fmt == "carousel" and notes == ["images: fallback (generation unavailable)"]
    assert [(v["role"], v["kind"], v["score"]) for v in vis] == [("cover", "article-image", 95), ("point", "text-card", None),
                                                                  ("point", "text-card", None), ("closing", "text-card", None)]
    assert {Image.open(tmp_path / "pack" / "visuals" / v["file"]).size for v in vis} == {(1080, 1350)}
    vis, _, fmt = visuals.make(post, fields, ctx(tmp_path, None), account_format="carousel")   # no article image
    assert fmt == "carousel" and [v["kind"] for v in vis] == ["text-card"] * 4


def test_an_article_image_cover_is_reviewed_against_its_own_line(tmp_path):
    post = dict(POST, post_id="vk-0001-p1-ig-1", network="instagram")
    fields = dict(FIELDS, image_text=["Бакара накратко", "Банко 1:1", "Прочетете ръководството"])
    item = dict(ITEM, images=[dict(ITEM["images"][0], review={})])          # no recorded review: Gemini reviews it
    g = FakeGemini([WORK, WORK, WORK, PASS])
    vis, notes, fmt = visuals.make(post, fields, ctx(tmp_path, g, item=item), account_format="carousel")
    assert len(g.reviews) == 4 and g.reviews[3] == ["fallback-review.jpg"]
    assert "IMAGE TEXT\nБакара накратко\n\n" in g.inputs[3]                  # only the line that image shows
    assert [v["kind"] for v in vis] == ["article-image", "text-card", "text-card"]


CAROUSEL = dict(POST, post_id="vk-0001-p1-ig-1", network="instagram",
                art_idea="the fox in a lab coat weighs tokens on a balance scale",
                slide_ideas=["a gold coin with 1:1 on a badge", "the fox points at a card", "a tied ribbon"])
SLIDES = dict(FIELDS, image_text=["Бакара накратко", "Банко 1:1", "Пунто", "Равенство", "Прочетете ръководството"])


def test_every_slide_has_its_picture_in_the_house_style(tmp_path):
    g = FakeGemini()
    c = ctx(tmp_path, g, styled=True)
    vis, notes, fmt = visuals.make(CAROUSEL, SLIDES, c, account_format="carousel")
    assert fmt == "carousel" and notes == [] and [v["role"] for v in vis] == ["cover", "point", "point", "point", "closing"]
    assert len(g.prompts) == 4                                             # the cover and 3 points, no closing picture
    cover, point = g.prompts[0][0], g.prompts[1][0]
    assert "STYLE: Flat vector editorial illustration" in cover and "the brand's fox" in cover
    assert "THE PICTURE: the fox in a lab coat weighs tokens on a balance scale." in cover
    assert "top third" in cover and "lower half of a slide" in point and "a gold coin with 1:1 on a badge" in point
    assert g.refs[0] == ["fox-lab-coat.png", "fox-suit.png"]               # the mascot as references
    assert g.refs[1] == ["cover-ref-1.jpg"] and visuals.NO_FOX in point    # a point without the fox: the cover only
    assert g.refs[2] == ["fox-lab-coat.png", "fox-suit.png", "cover-ref-1.jpg"]   # with the fox: the mascot too
    assert visuals.NO_FOX not in g.prompts[2][0]
    assert g.prompts[1][1] == visuals.aspect_for(visuals.compose.art_box((1080, 1350))) == "3:2"
    assert "STYLE GUIDE" in g.inputs[0] and "the brand's fox" in g.inputs[0]   # the review checks the style
    assert "SET BY OUR OWN LAYOUT TOOL" in g.inputs[0]                     # and is told what our layout adds
    slide = Image.open(tmp_path / "pack" / "visuals" / vis[1]["file"]).convert("RGB")
    box = visuals.compose.art_box((1080, 1350))
    mid = slide.getpixel(((box[0] + box[2]) // 2, (box[1] + box[3]) // 2))
    assert all(abs(a - b) < 25 for a, b in zip(mid, (200, 60, 30)))       # the point's own picture, below its text
    entry = c.spend.entry
    assert entry["images"] == 4 and entry["reviews"] == 1


def test_the_points_stay_text_slides_without_ideas_or_with_art_cover(tmp_path):
    g = FakeGemini()
    visuals.make(dict(CAROUSEL, slide_ideas=[]), SLIDES, ctx(tmp_path, g, styled=True), account_format="carousel")
    assert len(g.prompts) == 1
    g = FakeGemini()
    cover_only = st.parse((Path(__file__).resolve().parent / "fixtures" / "social" / "settings.md").read_text(encoding="utf-8")
                          .replace("| art | every slide |", "| art | cover |"))
    assert cover_only.brand["art"] == "cover"
    vis, _, _ = visuals.make(CAROUSEL, SLIDES, ctx(tmp_path, g, settings=cover_only), account_format="carousel")
    assert len(g.prompts) == 1 and len(vis) == 5
    assert "STYLE: Flat vector" in g.prompts[0][0]                          # no guide: the plain flat style


def test_a_point_picture_that_fails_leaves_text_slides(tmp_path):
    g = FakeGemini(fail_from=3)                                             # the cover and one point, then an error
    vis, notes, fmt = visuals.make(CAROUSEL, SLIDES, ctx(tmp_path, g, styled=True), account_format="carousel")
    assert fmt == "carousel" and notes == ["a point picture failed: text slides"]
    assert [v["kind"] for v in vis] == ["generated"] * 5
    slide = Image.open(tmp_path / "pack" / "visuals" / vis[1]["file"]).convert("RGB")
    box = visuals.compose.art_box((1080, 1350))
    assert slide.getpixel(((box[0] + box[2]) // 2, (box[1] + box[3]) // 2)) != (200, 60, 30)


def test_reference_pictures_go_before_the_prompt(tmp_path):
    import importlib
    sys.path.insert(0, str(REPO / "scripts"))
    gen = importlib.import_module("gemini_image_gen")
    ref = tmp_path / "fox.png"
    Image.new("RGB", (4, 4), (238, 106, 36)).save(ref)
    parts = gen.parts_for("draw the fox", [ref])
    assert parts[0]["inlineData"]["mimeType"] == "image/png" and parts[0]["inlineData"]["data"]
    assert parts[-1] == {"text": "draw the fox"} and gen.parts_for("x") == [{"text": "x"}]
