#!/usr/bin/env python3
"""External visual review of an article's image(s) via the Gemini API.

Reads GEMINI_API_KEY (and optional GEMINI_VISION_MODEL). Sends the article text plus one or
more images to a multimodal Gemini model with the Step-8 image-review prompt, and prints
Gemini's verdict (a 0-100 SEO/quality/accuracy score + PASS/iterate + concrete fixes). The
caller (daily-run.md Step 8) reads the verdict, decides whether to regenerate/fix the image,
and re-checks — mirroring the Step-7 text loop (keep-best, commit trail).

- RASTER images (.webp/.png/.jpg/.jpeg) are sent as inline image parts (Gemini "sees" them).
- SVG infographics are sent as their SOURCE TEXT (Gemini reads the markup, so it can verify
  the labels/numbers match the article) — no local SVG rasteriser is required in the cloud.

Usage:  python3 scripts/gemini_image_review.py <article_file> <image1> [image2 ...]
Exit:   0 = ok (verdict on stdout) · 2 = unavailable/error (caller falls back to skip)

stdlib-only (urllib).
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_MODEL = os.environ.get("GEMINI_VISION_MODEL", "gemini-3.1-pro-preview")
API_TMPL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

PROMPT_FILE = Path(__file__).resolve().parents[1] / \
    "VsichkiKazina/pipeline/prompts/step-8-image-review.md"

RASTER = {".webp": "image/webp", ".png": "image/png",
          ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}


def _prompt():
    """Extract the verbatim PROMPT block from the Step-8 image-review prompt file."""
    try:
        text = PROMPT_FILE.read_text(encoding="utf-8")
        marker = "## PROMPT (verbatim"
        if marker in text:
            body = text.split(marker, 1)[1].split("\n", 1)[1]
            return body.split("## Accept / iterate", 1)[0].strip()
    except Exception:  # noqa: BLE001
        pass
    return ("Act as an SEO + editorial image reviewer. Judge whether each image is accurate "
            "to the article, on-topic, free of fabricated operator logos/names/bonus numbers, "
            "responsible-gambling appropriate, and technically sound (clear, legible, correct "
            "aspect). Give a 0-100 score, a PASS/NEEDS-WORK verdict, and concrete fixes. Do "
            "not invent facts; flag any number in an infographic that is not supported by the "
            "article text.")


def main():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("GEMINI_UNAVAILABLE: GEMINI_API_KEY not set", file=sys.stderr)
        return 2
    if len(sys.argv) < 3:
        print("usage: gemini_image_review.py <article_file> <image1> [image2 ...]",
              file=sys.stderr)
        return 2

    article = Path(sys.argv[1]).read_text(encoding="utf-8")
    parts = [{"text": _prompt() + "\n\n---ARTICLE TEXT---\n\n" + article}]

    for img_arg in sys.argv[2:]:
        p = Path(img_arg)
        if not p.exists():
            print(f"GEMINI_ERROR: image not found: {p}", file=sys.stderr)
            return 2
        ext = p.suffix.lower()
        if ext == ".svg":
            parts.append({"text": f"\n\n---IMAGE (SVG SOURCE) {p.name}---\n\n"
                                  + p.read_text(encoding="utf-8")})
        elif ext in RASTER:
            parts.append({"text": f"\n\n---IMAGE {p.name}---"})
            parts.append({"inline_data": {"mime_type": RASTER[ext],
                                          "data": base64.b64encode(p.read_bytes()).decode()}})
        else:
            print(f"GEMINI_ERROR: unsupported image type: {p.name}", file=sys.stderr)
            return 2

    url = API_TMPL.format(model=DEFAULT_MODEL)
    payload = json.dumps({
        "contents": [{"parts": parts}],
        "generationConfig": {"temperature": 0.2},
    }).encode("utf-8")
    req = urllib.request.Request(
        url, data=payload,
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.load(resp)
        print(data["candidates"][0]["content"]["parts"][0]["text"])
        return 0
    except urllib.error.HTTPError as e:
        print(f"GEMINI_ERROR: HTTP {e.code} {e.read()[:300]!r}", file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001
        print(f"GEMINI_ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
