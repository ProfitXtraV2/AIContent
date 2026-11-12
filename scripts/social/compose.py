"""Image composition with Pillow (product spec C1–C5; tech spec flow 11).

Every visual gets the brand frame: a band with the brand name and the domain, and „18+“ for
Всички Казина (C3). The image text is laid over generated art exactly as written, in the
brand fonts, shrunk within set bounds to fit; when it still does not fit, composition fails
(TextDoesNotFit) instead of clipping. Fallback images (article images, social cards) are
placed whole on a brand-colour background, with the text and the band beside them, never over
them (C5).

    single(art, lines, size, brand_key)          generated art + image title (art cover-cropped)
    text_card(lines, size, brand_key)             brand text card (fallback step 3)
    placed(image, lines, size, brand_key, crop)   an article image or social card, whole
    slide(kind, text, size, brand_key, ...)       carousel slides: cover, point (art below the text
                                                  when given, art_box), closing
    save_jpeg(img, path)                          JPEG, quality 90, sRGB, under 8 MB
"""
import io
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from social import brands

FONT_DIR = Path(__file__).resolve().parent / "fonts"
FONT_FILES = {"Onest": "Onest-Variable.ttf", "Literata": "Literata-Variable.ttf",
              "Noto Sans": "NotoSans-Variable.ttf"}
WHITE = (255, 255, 255)
MAX_BYTES = 8 * 1024 * 1024


class TextDoesNotFit(Exception):
    """The image text does not fit the space even at the smallest allowed size (C3)."""


def rgb(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def font(family, size, weight="Regular"):
    path = FONT_DIR / FONT_FILES.get(family, FONT_FILES["Onest"])
    if not path.exists():
        path = FONT_DIR / FONT_FILES["Onest"]
    f = ImageFont.truetype(str(path), int(size))
    try:
        names = f.get_variation_names()
        want = weight.encode() if isinstance(names[0], bytes) else weight
        if want in names:
            f.set_variation_by_name(want)
    except (OSError, IndexError, AttributeError):
        pass
    return f


def text_width(draw, text, f):
    left, _top, right, _bottom = draw.textbbox((0, 0), text, font=f)
    return right - left


def wrap(draw, text, f, max_width):
    """Lines broken only at spaces, words never split or changed. None when one word alone is
    wider than the space."""
    lines, current = [], ""
    for word in text.split(" "):
        trial = word if not current else current + " " + word
        if text_width(draw, trial, f) <= max_width:
            current = trial
            continue
        if not current or text_width(draw, word, f) > max_width:
            return None
        lines.append(current)
        current = word
    if current:
        lines.append(current)
    return lines


def fit(draw, paragraphs, family, weight, box_w, box_h, max_size, min_size, spacing=1.18):
    """(font, [lines], line height) for the largest size from max_size down to min_size at
    which every paragraph fits the box. Raises TextDoesNotFit."""
    size = int(max_size)
    while size >= int(min_size):
        f = font(family, size, weight)
        lines = []
        for p in paragraphs:
            w = wrap(draw, p, f, box_w)
            if w is None:
                lines = None
                break
            lines += w
        if lines is not None:
            line_h = int(size * spacing)
            if len(lines) * line_h <= box_h:
                return f, lines, line_h
        size -= 2
    raise TextDoesNotFit(" / ".join(paragraphs)[:120])


def cover_crop(img, size):
    """Scaled to cover the size, then centre-cropped to the exact pixels."""
    w, h = size
    img = img.convert("RGB")
    scale = max(w / img.width, h / img.height)
    resized = img.resize((max(w, round(img.width * scale)), max(h, round(img.height * scale))), Image.LANCZOS)
    left = (resized.width - w) // 2
    top = (resized.height - h) // 2
    return resized.crop((left, top, left + w, top + h))


def contain(img, box):
    """Scaled to fit inside the box whole, aspect kept."""
    bw, bh = box
    scale = min(bw / img.width, bh / img.height)
    return img.convert("RGB").resize((max(1, round(img.width * scale)), max(1, round(img.height * scale))), Image.LANCZOS)


def band_height(size):
    return max(72, round(size[1] * (0.085 if size[0] <= size[1] else 0.11)))


def draw_frame(img, brand_key):
    """The brand band at the bottom: name left; domain and „18+“ right. Returns the frame facts
    recorded in the manifest."""
    b = brands.brand(brand_key)
    pal = b["palette"]
    w, h = img.size
    bh = band_height(img.size)
    d = ImageDraw.Draw(img)
    d.rectangle((0, h - bh, w, h), fill=rgb(pal["green"]))
    d.rectangle((0, h - bh, w, h - bh + max(4, bh // 18)), fill=rgb(pal["gold"]))
    margin = round(w * 0.055)
    f_name = font(b["fonts"]["title"], bh * 0.34, "SemiBold")
    f_dom = font(b["fonts"]["body"], bh * 0.28, "Medium")
    cy = h - bh // 2 + max(2, bh // 36)
    d.text((margin, cy), b["name"], font=f_name, fill=WHITE, anchor="lm")
    x = w - margin
    if b["mark_18"]:
        r = round(bh * 0.30)
        d.ellipse((x - 2 * r, cy - r, x, cy + r), outline=rgb(pal["gold"]), width=max(3, r // 7))
        d.text((x - r, cy), "18+", font=font(b["fonts"]["title"], r * 0.82, "Bold"), fill=WHITE, anchor="mm")
        x -= 2 * r + round(bh * 0.25)
    d.text((x, cy), b["domain"], font=f_dom, fill=WHITE, anchor="rm")
    return {"domain": True, "mark_18": bool(b["mark_18"]), "name": True}


def _scrim(img, top_fraction):
    """A dark gradient from the top, so white text reads on any art."""
    w, h = img.size
    grad = Image.new("L", (1, h))
    stop = max(1, int(h * top_fraction))
    for y in range(h):
        grad.putpixel((0, y), int(185 * max(0.0, 1 - y / stop)))
    alpha = grad.resize((w, h))
    black = Image.new("RGB", (w, h), (10, 12, 14))
    return Image.composite(black, img, alpha)


def single(art, lines, size, brand_key):
    """Generated art cover-cropped to the size, the image title over a scrim at the top, the
    brand band below. (image, frame)."""
    b = brands.brand(brand_key)
    img = cover_crop(art, size)
    w, h = size
    img = _scrim(img, 0.46 if w <= h else 0.62)
    d = ImageDraw.Draw(img)
    margin = round(w * 0.07)
    box_w = w - 2 * margin
    box_h = round(h * (0.30 if w <= h else 0.42))
    f, wrapped, lh = fit(d, [ln for ln in lines if ln], b["fonts"]["title"], "Bold", box_w, box_h,
                         max_size=w * (0.078 if w <= h else 0.05), min_size=w * (0.042 if w <= h else 0.028))
    y = round(h * 0.06)
    for ln in wrapped:
        d.text((margin, y), ln, font=f, fill=WHITE)
        y += lh
    frame = draw_frame(img, brand_key)
    return img, frame


def text_card(lines, size, brand_key):
    """Brand text card (C5 fallback 3): brand colour, the image title, the brand band."""
    b = brands.brand(brand_key)
    pal = b["palette"]
    w, h = size
    img = Image.new("RGB", size, rgb(pal["green"]))
    d = ImageDraw.Draw(img)
    margin = round(w * 0.09)
    bh = band_height(size)
    d.rectangle((margin, round(h * 0.12), margin + round(w * 0.12), round(h * 0.12) + max(6, h // 120)),
                fill=rgb(pal["gold"]))
    box_h = h - bh - round(h * 0.30)
    f, wrapped, lh = fit(d, [ln for ln in lines if ln], b["fonts"]["title"], "Bold", w - 2 * margin, box_h,
                         max_size=w * 0.085, min_size=w * 0.045)
    top = round(h * 0.12) + round(h * 0.06)
    y = top + max(0, (h - bh - top - round(h * 0.06) - len(wrapped) * lh) // 2)
    for ln in wrapped:
        d.text((margin, y), ln, font=f, fill=WHITE)
        y += lh
    d.rectangle((0, h - bh, w, h), fill=rgb(pal["ink"]))
    frame = draw_frame(img, brand_key)
    return img, frame


def placed(image, lines, size, brand_key, crop=False):
    """An article image or a social card, whole on the brand background (C5): the image title in
    a strip above it, the brand band below, nothing over the image. crop=True (a hero with no
    text) fills the space instead. (image, frame)."""
    b = brands.brand(brand_key)
    pal = b["palette"]
    w, h = size
    img = Image.new("RGB", size, rgb(pal["paper"]))
    d = ImageDraw.Draw(img)
    bh = band_height(size)
    margin = round(w * 0.06)
    title_h = 0
    if any(lines):
        box_h = round(h * 0.17)
        f, wrapped, lh = fit(d, [ln for ln in lines if ln], b["fonts"]["title"], "Bold", w - 2 * margin, box_h,
                             max_size=w * 0.06, min_size=w * 0.034)
        y = round(h * 0.045)
        for ln in wrapped:
            d.text((margin, y), ln, font=f, fill=rgb(pal["ink"]))
            y += lh
        title_h = y + round(h * 0.02)
    area = (w - 2 * margin, h - bh - title_h - margin)
    top = title_h or margin
    if crop:
        pic = cover_crop(image, (w, h - bh - title_h))
        img.paste(pic, (0, title_h))
    else:
        pic = contain(image, area)
        img.paste(pic, ((w - pic.width) // 2, top + (area[1] - pic.height) // 2))
    frame = draw_frame(img, brand_key)
    return img, frame


def art_box(size):
    """(left, top, right, bottom) of a point slide's picture: the lower half, above the band."""
    w, h = size
    margin = round(w * 0.08)
    return margin, round(h * 0.47), w - margin, h - band_height(size) - round(h * 0.03)


def _rounded(img, radius):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img.width - 1, img.height - 1), radius=radius, fill=255)
    return mask


def slide(kind, text, size, brand_key, art=None, index=1, total=1):
    """A carousel slide (C4). kind: cover (generated art + title), point (the point, with its
    picture in art_box when art is given, else a text slide), closing (the call to read, the domain
    and „18+“). The counter „index/total“ is drawn on inner slides."""
    b = brands.brand(brand_key)
    pal = b["palette"]
    w, h = size
    if kind == "cover":
        if art is None:
            return text_card([text], size, brand_key)
        return single(art, [text], size, brand_key)
    bh = band_height(size)
    margin = round(w * 0.08)
    if kind == "point":
        img = Image.new("RGB", size, rgb(pal["paper"]))
        d = ImageDraw.Draw(img)
        d.text((w - margin, round(h * 0.07)), f"{index}/{total}", font=font(b["fonts"]["title"], w * 0.04, "SemiBold"),
               fill=rgb(pal["gold"]), anchor="ra")
        d.rectangle((margin, round(h * 0.16), margin + round(w * 0.1), round(h * 0.16) + max(6, h // 140)),
                    fill=rgb(pal["green"]))
        if art is not None:                                  # the point above, its picture below
            box = art_box(size)
            top = round(h * 0.21)
            f, wrapped, lh = fit(d, [text], b["fonts"]["title"], "SemiBold", w - 2 * margin, box[1] - top - round(h * 0.03),
                                 max_size=w * 0.068, min_size=w * 0.04)
            y = top + max(0, (box[1] - top - round(h * 0.03) - len(wrapped) * lh) // 2)
            for ln in wrapped:
                d.text((margin, y), ln, font=f, fill=rgb(pal["ink"]))
                y += lh
            pic = cover_crop(art, (box[2] - box[0], box[3] - box[1]))
            img.paste(pic, box[:2], _rounded(pic, round(w * 0.03)))
            return img, draw_frame(img, brand_key)
        f, wrapped, lh = fit(d, [text], b["fonts"]["title"], "SemiBold", w - 2 * margin, h - bh - round(h * 0.34),
                             max_size=w * 0.075, min_size=w * 0.04)
        top = round(h * 0.22)
        y = top + max(0, (h - bh - top - round(h * 0.12) - len(wrapped) * lh) // 2)
        for ln in wrapped:
            d.text((margin, y), ln, font=f, fill=rgb(pal["ink"]))
            y += lh
        return img, draw_frame(img, brand_key)
    if kind == "closing":
        img = Image.new("RGB", size, rgb(pal["green"]))
        d = ImageDraw.Draw(img)
        badge = (2 * round(w * 0.075) + round(w * 0.04)) if b["mark_18"] else 0
        f, wrapped, lh = fit(d, [text], b["fonts"]["title"], "Bold", w - 2 * margin - badge, round(h * 0.34),
                             max_size=w * 0.07, min_size=w * 0.04)
        y = round(h * 0.2)
        for ln in wrapped:
            d.text((margin, y), ln, font=f, fill=WHITE)
            y += lh
        d.text((margin, y + round(h * 0.05)), b["domain"], font=font(b["fonts"]["title"], w * 0.075, "Bold"),
               fill=rgb(pal["gold"]))
        if b["mark_18"]:
            r = round(w * 0.075)
            cx, cy = w - margin - r, round(h * 0.2) + r
            d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=rgb(pal["gold"]), width=max(4, r // 8))
            d.text((cx, cy), "18+", font=font(b["fonts"]["title"], r * 0.8, "Bold"), fill=WHITE, anchor="mm")
        d.rectangle((0, h - bh, w, h), fill=rgb(pal["ink"]))
        return img, draw_frame(img, brand_key)
    raise ValueError(f"unknown slide kind {kind!r}")


def save_jpeg(img, path):
    """JPEG at quality 90 (lower only if the file would pass 8 MB), sRGB, no metadata."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    rgb_img = img.convert("RGB")
    for q in (90, 85, 80, 75, 70):
        buf = io.BytesIO()
        rgb_img.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
        if buf.tell() <= MAX_BYTES:
            path.write_bytes(buf.getvalue())
            return path
    path.write_bytes(buf.getvalue())
    return path


def rasterize_svg(svg_path, width):
    """An SVG infographic as an image at the given width (CairoSVG), or None when CairoSVG is
    not installed (the next fallback is used then)."""
    try:
        import cairosvg
    except Exception:  # noqa: BLE001
        return None
    png = cairosvg.svg2png(url=str(svg_path), output_width=int(width))
    return Image.open(io.BytesIO(png))
