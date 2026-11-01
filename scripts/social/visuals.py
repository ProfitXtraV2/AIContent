"""The visuals of a post (product spec C1–C7; tech spec flow 11).

    make(post, fields, ctx) → (visuals, notes, format)

1. Budget first (spend.py). Generation needs the social key; the article key is never used.
2. Generated art at the network's aspect ratio (2K), cover-cropped to the exact pixels, the image
   text and the brand frame laid on with Pillow (compose.py). Every picture follows the brand's
   house style (<brand>/social/style/style.md, its STYLE block in the prompt and in the review;
   the mascot pictures in style/mascot/ sent as references). Carousels: a generated cover, then
   the points, then the closing slide. With the brand's `art` setting `every slide` and the post's
   `slide_ideas`, each point gets its own picture below its text (the cover sent as a reference too,
   so the slides look alike); else the points are text slides.
3. Review (PASS at 80 or more, no integrity failure, no clipped or overlapping text), up to 2
   redos, keeping the best passing version.
4. Otherwise the fallback, in order: the item's own image (hero, else first image) when it
   qualifies; the live page's social card; a brand text card. A carousel keeps its slides in a
   fallback: the cover is the item's own image when it qualifies, else a text card, and the other
   slides are text slides. With none possible (no image title), the post gets no visual
   ("Held: no visual").

No generated visual is ever used unreviewed.
"""
import hashlib
import io
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

from PIL import Image

from social import brands, compose, links, operators, pack as packmod, spend as spendmod
from social import postnumbers as numbers

ROOT = brands.ROOT
CASES = {"generation": "images: fallback (generation unavailable)",
         "review": "images: fallback (review unavailable)",
         "budget": "images: fallback (budget reached)",
         "attention": "visual needs attention"}
SCORE_RE = re.compile(r"\bSCORE\b[^0-9\n]{0,10}(\d{1,3})|(\d{1,3})\s*/\s*100", re.I)


def _negated(text, pos):
    """True when the words just before `pos` deny it: „no …“, „nothing …“, „without …“."""
    return bool(re.search(r"\b(no|not|nothing|none|never|without|няма|без)\b[\w\s,-]{0,24}$",
                          text[max(0, pos - 40):pos], re.I))


def parse_verdict(text):
    """{score, integrity_ok, layout_ok, passed} from a review answer."""
    t = str(text or "")
    m = SCORE_RE.search(t)
    score = int(m.group(1) or m.group(2)) if m else None
    if re.search(r"INTEGRITY\s*:\s*OK", t, re.I):
        integrity_ok = True
    elif re.search(r"INTEGRITY FAILURE", t, re.I) and not re.search(r"\bno integrity failure", t, re.I):
        integrity_ok = False
    else:
        integrity_ok = not re.search(r"(?<!no )integrity failure", t, re.I)
    if re.search(r"LAYOUT\s*:\s*OK", t, re.I):
        layout_ok = True
    elif re.search(r"LAYOUT DEFECT", t, re.I):
        layout_ok = False
    else:
        layout_ok = not any(not _negated(t, m.start())
                            for m in re.finditer(r"\b(clipped|clips|overlapp?ing|overlaps|cut off)\b", t, re.I))
    passed = score is not None and score >= 80 and integrity_ok and layout_ok
    return {"score": score, "integrity_ok": integrity_ok, "layout_ok": layout_ok, "passed": passed}


class Gemini:
    """Runs the article scripts in a child process with GEMINI_API_KEY set to the social key,
    only for that process (C7: the article key is never used for social work)."""

    def __init__(self, social_key, root=ROOT, review_prompt=None):
        self.key, self.root = social_key, Path(root)
        self.review_prompt = review_prompt

    def _env(self):
        env = dict(os.environ)
        env["GEMINI_API_KEY"] = self.key
        env["PYTHONIOENCODING"] = "utf-8"          # the tools' output is read as UTF-8 (not the Windows code page)
        return env

    def generate(self, prompt, out_png, aspect, size="2K", refs=()):
        """(ok, error text). Writes a PNG at out_png. refs: reference pictures sent with the prompt."""
        cmd = [sys.executable, str(self.root / "scripts" / "gemini_image_gen.py"), prompt, str(out_png), "20000",
               "--aspect", aspect, "--size", size]
        for r in refs:
            cmd += ["--ref", str(r)]
        try:
            r = subprocess.run(cmd, env=self._env(), capture_output=True, encoding="utf-8", errors="replace", timeout=360)
        except (OSError, subprocess.SubprocessError) as e:
            return False, str(e)
        return (r.returncode == 0 and Path(out_png).exists()), (r.stderr or r.stdout)[-600:]

    def review(self, article_file, images, usage_out):
        """(ok, verdict text, error text)."""
        cmd = [sys.executable, str(self.root / "scripts" / "gemini_image_review.py"), str(article_file),
               *[str(i) for i in images], "--prompt", str(self.review_prompt), "--usage-out", str(usage_out)]
        try:
            r = subprocess.run(cmd, env=self._env(), capture_output=True, encoding="utf-8", errors="replace", timeout=360)
        except (OSError, subprocess.SubprocessError) as e:
            return False, "", str(e)
        return r.returncode == 0, r.stdout, r.stderr[-600:]


class Ctx:
    """What making a post's visuals needs. gemini=None means generation is unavailable."""

    def __init__(self, brand_key, pack_dir, settings, spend, gemini=None, item=None, item_root=ROOT,
                 operator_names=(), art_template="", fetch=None, page_url=None, style="", refs=()):
        self.brand_key, self.pack_dir, self.settings = brand_key, Path(pack_dir), settings
        self.spend, self.gemini, self.item, self.item_root = spend, gemini, item, Path(item_root)
        self.ops, self.art_template = operator_names, art_template
        self.fetch = fetch or _fetch
        self.page_url = page_url
        self.style, self.refs = style, list(refs)              # load_style(): the house style and the mascot
        self.art_mode = settings.brand.get("art", "every slide")


STYLE_RE = re.compile(r"^## STYLE\s*$(.*?)(?=^## |\Z)", re.M | re.S)
# What compose.py lays over and around the art: the review must not count it as added text or a style break
SET_BY_TOOL = ("SET BY OUR OWN LAYOUT TOOL, NOT BY THE ARTIST (expected: never count these as added text, as a gradient "
               "in the art or as a style break; only check that they are legible and do not collide)\n"
               "- every image: the brand band at the bottom with the name, the domain and the 18+ mark;\n"
               "- a cover or a single image: a dark shade from the top edge behind the title, so the white title reads;\n"
               "- a point slide: the counter (e.g. 2/3), a short accent bar, and the picture in a rounded panel;\n"
               "- the closing slide: no picture, deep green, the domain in large letters and the 18+ badge.")
NO_FOX = "; no fox and no animal in this picture, only the object"
DEFAULT_STYLE = "Flat vector editorial illustration in the brand palette, soft shadows, generous negative space."
COMPOSITIONS = {
    "cover": "Keep the top third of the picture calm and simple, with no detail behind where a title will be "
             "laid over it; place the main subject in the middle and lower part.",
    "point": "One subject in the centre, whole and uncropped, on a plain flat light background.",
}
GEMINI_ASPECTS = {"1:1": 1.0, "5:4": 1.25, "4:3": 4 / 3, "3:2": 1.5, "16:9": 16 / 9, "21:9": 21 / 9}


def load_style(brand_key, root=ROOT):
    """(the STYLE block of <brand>/social/style/style.md, [mascot pictures]); ("", []) without a guide."""
    d = brands.social_dir(brand_key, root) / "style"
    guide = d / "style.md"
    m = STYLE_RE.search(guide.read_text(encoding="utf-8")) if guide.exists() else None
    style = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    refs = sorted(p for p in (d / "mascot").glob("*") if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")) \
        if (d / "mascot").is_dir() else []
    return style, refs


def aspect_for(box):
    """The Gemini aspect ratio nearest to a box (left, top, right, bottom)."""
    r = (box[2] - box[0]) / (box[3] - box[1])
    return min(GEMINI_ASPECTS, key=lambda k: abs(GEMINI_ASPECTS[k] - r))


def _fetch(url, binary=False, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": operators.USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    return data if binary else data.decode("utf-8", "replace")


def art_prompt(template, idea, fixes="", style="", kind="cover"):
    """The PROMPT block of visual-art.md filled in: the house style, the idea and the composition
    for kind (cover, point; a single image is composed as a cover) from its Compositions list."""
    head, _, block = template.partition("## PROMPT") if "## PROMPT" in template else ("", "", template)
    comps = dict(COMPOSITIONS, **{k.lower(): v.strip() for k, v in re.findall(r"^- \*\*(\w+)\*\*: (.+)$", head, re.M)})
    p = block.strip().replace("{style}", style or DEFAULT_STYLE).replace("{idea}", idea.strip().rstrip("."))
    p = p.replace("{composition}", comps.get("point" if kind == "point" else "cover", ""))
    if fixes:
        p += "\nAvoid the problems a reviewer found in the last attempt: " + re.sub(r"\s+", " ", fixes)[:500]
    return p


def plan_format(account_format, network, lines):
    """("single" | "carousel", note) for the wanted format (the account's, or the request's) and the
    post's image text. A carousel has 3 slides up to the network's most (cover, points, closing);
    `auto` makes one from 4 image text lines (two points or more)."""
    net = brands.NETWORKS[network]
    want = account_format == "carousel" or (account_format == "auto" and len(lines) >= 4)
    if want and not net["carousel"]:
        return "single", f"carousel not offered on {network}: single image"
    if want and 3 <= len(lines) <= net["max_slides"]:
        return "carousel", ""
    if want:
        return "single", f"a carousel needs 3–{net['max_slides']} image text lines: single image"
    return "single", ""


def _passes_b5(text, ctx):
    b = ctx.settings.brand
    if operators.named(text, ctx.ops) or operators.offer_amount(text, b.get("offer_words") or []):
        return False
    low = text.lower()
    return not any(re.search(r"(?<![\w])" + re.escape(w) + r"(?![\w])", low) for w in b.get("register_words") or [])


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _compose_generated(art, lines, fmt, size, brand_key, point_arts=()):
    """[(role, image, frame)] for generated art: one image, or cover + points + closing. point_arts:
    the points' own pictures, in order (a point without one is a text slide)."""
    if fmt == "single":
        img, frame = compose.single(art, lines, size, brand_key)
        return [("single", img, frame)]
    out, total = [], len(lines)
    for i, line in enumerate(lines, 1):
        kind = "cover" if i == 1 else "closing" if i == total else "point"
        pic = art if kind == "cover" else (point_arts[i - 2] if kind == "point" and i - 2 < len(point_arts) else None)
        img, frame = compose.slide(kind, line, size, brand_key, art=pic, index=i, total=total)
        out.append((kind, img, frame))
    return out


def slide_ideas(post, lines, fmt, ctx):
    """The ideas of the point slides' own pictures, or [] when the points stay text slides: a carousel,
    the brand's art setting `every slide`, and one idea per point from the drafting routine."""
    points = lines[1:-1]
    ideas = [str(x).strip() for x in post.get("slide_ideas") or []][:len(points)]
    if fmt != "carousel" or ctx.art_mode != "every slide" or not points or len(ideas) < len(points) or not all(ideas):
        return []
    return ideas


def _review(ctx, post, fields, files, work):
    """(verdict dict or None, error)."""
    article = work / "review-input.md"
    article.write_text("SOURCE LINES\n" + "\n".join(s.get("line", "") for s in post.get("sources") or [])
                       + "\n\nIMAGE TEXT\n" + "\n".join(fields.get("image_text") or [])
                       + "\n\n" + SET_BY_TOOL
                       + (f"\n\nSTYLE GUIDE (every picture follows it)\n{ctx.style}" if ctx.style else ""), encoding="utf-8")
    usage = work / "usage.json"
    ok, text, err = ctx.gemini.review(article, files, usage)
    if not ok:
        ctx.spend.note_error(err)
        return None, err
    try:
        import json
        ctx.spend.add_review(json.loads(usage.read_text(encoding="utf-8")) if usage.exists() else None)
    except ValueError:
        ctx.spend.add_review(None)
    v = parse_verdict(text)
    v["text"] = text
    return v, ""


def _write(ctx, post_id, composed, kind, fields, fallback_case=None, score=None):
    visuals = []
    vdir = ctx.pack_dir / "visuals"
    for n, (role, img, frame) in enumerate(composed, 1):
        f = vdir / f"{post_id}-{n}.jpg"
        compose.save_jpeg(img, f)
        visuals.append({"file": f.name, "kind": kind, "role": role, "fallback_case": fallback_case,
                        "score": score, "image_text_hash": packmod.image_text_hash(fields),
                        "sha256": _sha(f), "frame": frame})
    return visuals


def _generated(post, fields, ctx, fmt, size, work):
    """(composed list or None, score, case or None, notes)."""
    if ctx.gemini is None:
        return None, None, "generation", []
    lines = fields.get("image_text") or []
    ideas = slide_ideas(post, lines, fmt, ctx)
    best, notes, fixes = None, [], ""
    for attempt in range(1, 4):
        ok, why = ctx.spend.can_spend(spendmod.estimate_attempt(1 + len(ideas)))
        if not ok:
            return (best[1], best[0], None, notes) if best else (None, None, "budget", notes)
        png = work / f"art-{attempt}.png"
        ok, err = ctx.gemini.generate(art_prompt(ctx.art_template, post.get("art_idea") or fields.get("alt_text", ""), fixes,
                                                 ctx.style, "cover"),
                                      png, brands.ASPECTS.get(size, "4:5"), refs=ctx.refs)
        if not ok:
            ctx.spend.note_error(err)
            if best:
                return best[1], best[0], None, notes
            return None, None, ("budget" if ctx.spend.entry.get("credits_exhausted") else "generation"), notes
        ctx.spend.add_image()
        point_arts = _point_arts(ctx, ideas, png, size, fixes, work, attempt)
        if len(point_arts) < len(ideas) and "a point picture failed: text slides" not in notes:
            notes.append("a point picture failed: text slides")
        try:
            composed = _compose_generated(Image.open(png), lines, fmt, size, ctx.brand_key,
                                          [Image.open(a) for a in point_arts] if len(point_arts) == len(ideas) else [])
        except compose.TextDoesNotFit:
            notes.append("image text does not fit the image")
            return None, None, "attention", notes
        files = []
        for i, (_role, img, _frame) in enumerate(composed, 1):
            files.append(compose.save_jpeg(img, work / f"try-{attempt}-{i}.jpg"))
        verdict, err = _review(ctx, post, fields, files, work)
        if verdict is None:
            if best:
                return best[1], best[0], None, notes
            return None, None, ("budget" if ctx.spend.entry.get("credits_exhausted") else "review"), notes
        if verdict["passed"] and (best is None or verdict["score"] > best[0]):
            best = (verdict["score"], composed)
        if verdict["passed"]:
            break
        fixes = verdict["text"]
    if best:
        return best[1], best[0], None, notes
    return None, None, "attention", notes


def _point_arts(ctx, ideas, cover_png, size, fixes, work, attempt):
    """The point slides' pictures ([png paths], all or as many as were made), each drawn with the
    cover (made small) as a reference, and with the mascot only when its idea has the fox."""
    if not ideas:
        return []
    ref = work / f"cover-ref-{attempt}.jpg"
    with Image.open(cover_png) as c:
        small = c.convert("RGB")
        small.thumbnail((768, 768))
        small.save(ref, "JPEG", quality=85)
    aspect = aspect_for(compose.art_box(size))
    out = []
    for j, idea in enumerate(ideas, 2):
        png = work / f"art-{attempt}-slide-{j}.png"
        fox = re.search(r"\bfox\b", idea, re.I)
        ok, err = ctx.gemini.generate(art_prompt(ctx.art_template, idea if fox else idea.rstrip(". ") + NO_FOX, fixes,
                                                 ctx.style, "point"),
                                      png, aspect, size="1K", refs=[*ctx.refs, ref] if fox else [ref])
        if not ok:
            ctx.spend.note_error(err)
            break
        ctx.spend.add_image()
        out.append(png)
    return out


def _article_image(post, fields, ctx, size, work):
    """Fallback 1: the item's hero, or else its first image, when it qualifies. (composed, score) or None."""
    item = ctx.item
    if not item or not item.get("images"):
        return None
    images = item["images"]
    heroes = [i for i in images if "hero" in i["name"].lower() and not i["name"].lower().endswith(".svg")]
    candidate = heroes[0] if heroes else images[0]
    alt = candidate.get("alt", "")
    sources = [s.get("line", "") for s in post.get("sources") or []]
    if not alt or not _passes_b5(alt, ctx) or numbers.unmatched(alt, sources, "text",
                                                                 ctx.settings.brand.get("allowed_number_names") or []):
        return None
    path = ctx.item_root / candidate["path"]
    if not path.exists():
        return None
    if path.suffix.lower() == ".svg":
        pic = compose.rasterize_svg(path, size[0])
        if pic is None:
            return None
    else:
        pic = Image.open(path)
    review = candidate.get("review") or {}
    score = review.get("score")
    title = (fields.get("image_text") or [""])[:1]
    crop = "hero" in candidate["name"].lower() and path.suffix.lower() != ".svg"
    try:
        img, frame = compose.placed(pic, title, size, ctx.brand_key, crop=crop)
    except compose.TextDoesNotFit:
        return None
    recorded_ok = isinstance(score, int) and score >= 80 and review.get("integrity_ok") is True
    if not recorded_ok:
        if ctx.gemini is None or not ctx.spend.can_spend(spendmod.prices()["review"]["estimate_usd"])[0]:
            return None
        f = compose.save_jpeg(img, work / "fallback-review.jpg")
        verdict, _err = _review(ctx, post, dict(fields, image_text=title), [f], work)   # the one line it shows
        if not verdict or not verdict["passed"]:
            return None
        score = verdict["score"]
    return [("single", img, frame)], score


def _fallback_carousel(post, fields, ctx, size, work):
    """A carousel without generated art: the item's own image as the cover when it qualifies (else a
    text card), then text slides for the points and the closing slide. (composed, kind, score) or None."""
    lines = fields.get("image_text") or []
    total = len(lines)
    try:
        got = _article_image(post, fields, ctx, size, work)
        if got:
            (_role, img, frame), = got[0]
            composed, kind, score = [("cover", img, frame)], "article-image", got[1]
        else:
            img, frame = compose.slide("cover", lines[0], size, ctx.brand_key)
            composed, kind, score = [("cover", img, frame)], "text-card", None
        for i, line in enumerate(lines[1:], 2):
            role = "closing" if i == total else "point"
            img, frame = compose.slide(role, line, size, ctx.brand_key, index=i, total=total)
            composed.append((role, img, frame))
    except compose.TextDoesNotFit:
        return None
    return composed, kind, score


def _social_card(post, fields, ctx, size):
    """Fallback 2: the live page's social card (/assets/img/og/, not the site default), when it
    exists at drafting time and the page title passes B5. Never cropped, never reviewed again."""
    url = ctx.page_url
    if not url:
        return None
    try:
        html = ctx.fetch(url)
    except Exception:  # noqa: BLE001
        return None
    m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I) or \
        re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
    if not m:
        return None
    img_url = m.group(1)
    if "/assets/img/og/" not in img_url or img_url.rstrip("/").endswith("home.webp"):
        return None
    t = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']*)["\']', html, re.I) or \
        re.search(r"<title>([^<]*)</title>", html, re.I)
    if not t or not _passes_b5(t.group(1), ctx):
        return None
    try:
        pic = Image.open(io.BytesIO(ctx.fetch(img_url, binary=True)))
        img, frame = compose.placed(pic, (fields.get("image_text") or [""])[:1], size, ctx.brand_key, crop=False)
    except Exception:  # noqa: BLE001
        return None
    return [("single", img, frame)]


def make(post, fields, ctx, account_format="auto"):
    """(visuals, notes, format) for one post; visuals are written to <pack>/visuals/."""
    network = post["network"]
    lines = fields.get("image_text") or []
    if not lines or not lines[0].strip():
        return [], ["Held: no visual (no image title)"], "single"
    fmt, note = plan_format(account_format, network, lines)
    notes = [note] if note else []
    size = brands.SIZES[network]["slide" if fmt == "carousel" else "single"]
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        composed, score, case, more = _generated(post, fields, ctx, fmt, size, work)
        notes += more
        if composed:
            ctx.spend.save()
            return _write(ctx, post["post_id"], composed, "generated", fields, None, score), notes, fmt
        notes.append(CASES[case])
        if fmt == "carousel":
            got = _fallback_carousel(post, fields, ctx, size, work)
            ctx.spend.save()
            if got:
                composed, kind, score = got
                vis = _write(ctx, post["post_id"], composed, kind, fields, CASES[case], score)
                for v in vis[1:]:                                    # after the cover: text slides
                    v.update(kind="text-card", score=None)
                return vis, notes, fmt
        single = brands.SIZES[network]["single"]
        got = _article_image(post, fields, ctx, single, work)
        ctx.spend.save()
        if got:
            return _write(ctx, post["post_id"], got[0], "article-image", fields, CASES[case], got[1]), notes, "single"
        card = _social_card(post, fields, ctx, single)
        if card:
            return _write(ctx, post["post_id"], card, "social-card", fields, CASES[case], None), notes, "single"
        try:
            img, frame = compose.text_card(lines[:1], single, ctx.brand_key)
        except compose.TextDoesNotFit:
            return [], notes + ["Held: no visual (the image title does not fit)"], "single"
        return _write(ctx, post["post_id"], [("single", img, frame)], "text-card", fields, CASES[case], None), notes, "single"


def page_url_for(item, settings_brand, brand_key):
    """The live address whose social card fallback 2 may use."""
    if not item:
        return None
    if item.get("kind") == "hub-intro":
        return f"{brands.brand(brand_key)['site']}/blog/{item['slug'].replace('hub-intro-', '', 1)}/"
    return links.address_for(item["slug"], settings_brand)
