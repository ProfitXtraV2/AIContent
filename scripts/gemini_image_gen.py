#!/usr/bin/env python3
"""Generate a decorative article image via the Gemini image API.

Reads GEMINI_API_KEY (and optional GEMINI_IMAGE_MODEL) from the environment. Sends a text
prompt to a Gemini image model, extracts the returned inline image (base64), writes it to
<out>, and — if Pillow is available — converts to a web-optimised WebP under the size cap.

Usage:  python3 scripts/gemini_image_gen.py "<prompt>" <out_path> [max_kb]
        <out_path> should end .webp (preferred) or .png. Default max_kb = 100.
Exit:   0 = ok (wrote the file; prints the final path) · 2 = unavailable/error (caller skips)

Image hygiene is the CALLER'S responsibility via the prompt (no operator logos/names, no
people/faces, no fake bonus numbers, no promotional text, decorative only). This script just
renders whatever prompt it is given.

stdlib-only for the API call (urllib). Pillow is used only if present (WebP conversion);
without it the raw PNG is kept.
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

# Image model confirmed working by the image test run (see scripts/GEMINI_ENDPOINT.md).
DEFAULT_MODEL = os.environ.get("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image")
API_TMPL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"


def _find_inline_image(data):
    """Return (mime, raw_bytes) of the first inline image part, or None. Tolerates both
    camelCase (inlineData/mimeType) and snake_case (inline_data/mime_type) response shapes."""
    for cand in data.get("candidates", []):
        parts = cand.get("content", {}).get("parts", [])
        for p in parts:
            inline = p.get("inlineData") or p.get("inline_data")
            if inline and (inline.get("data")):
                mime = inline.get("mimeType") or inline.get("mime_type") or "image/png"
                return mime, base64.b64decode(inline["data"])
    return None


def _request(url, key, prompt, with_modalities):
    body = {"contents": [{"parts": [{"text": prompt}]}]}
    if with_modalities:
        body["generationConfig"] = {"responseModalities": ["TEXT", "IMAGE"]}
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.load(resp)


def _ensure_pil():
    """Return PIL.Image, importing it — and pip-installing Pillow if the cloud image
    doesn't ship it (the validation run showed Pillow may be absent). None if unavailable."""
    try:
        from PIL import Image
        return Image
    except Exception:
        pass
    try:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "--quiet",
                        "--disable-pip-version-check", "Pillow"],
                       check=True, timeout=240)
        from PIL import Image
        return Image
    except Exception as e:  # noqa: BLE001
        print(f"WARN: Pillow unavailable ({e}); cannot convert/compress to WebP",
              file=sys.stderr)
        return None


def _to_webp(png_bytes, out_path, max_kb):
    """Convert PNG bytes to a WebP <= max_kb using Pillow (auto-installed if missing).
    Returns True if a WebP was written, False if Pillow is unavailable (caller keeps PNG)."""
    Image = _ensure_pil()
    if Image is None:
        return False
    import io
    img = Image.open(io.BytesIO(png_bytes)).convert("RGB")
    if max(img.size) > 1024:                      # keep heroes reasonable
        img.thumbnail((1024, 1024))
    for q in (82, 72, 62, 52, 42, 32):
        img.save(out_path, "WEBP", quality=q, method=6)
        if out_path.stat().st_size <= max_kb * 1024:
            return True
    return True                                   # kept best effort even if slightly over


def main():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("GEMINI_UNAVAILABLE: GEMINI_API_KEY not set", file=sys.stderr)
        return 2
    if len(sys.argv) < 3:
        print("usage: gemini_image_gen.py \"<prompt>\" <out_path> [max_kb]", file=sys.stderr)
        return 2
    prompt = sys.argv[1]
    out = Path(sys.argv[2])
    max_kb = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    url = API_TMPL.format(model=DEFAULT_MODEL)

    data = None
    try:
        data = _request(url, key, prompt, with_modalities=True)
    except urllib.error.HTTPError as e:
        # Some models reject responseModalities; retry once without it before giving up.
        if e.code == 400:
            try:
                data = _request(url, key, prompt, with_modalities=False)
            except Exception as e2:  # noqa: BLE001
                print(f"GEMINI_ERROR: HTTP retry failed {e2}", file=sys.stderr)
                return 2
        else:
            print(f"GEMINI_ERROR: HTTP {e.code} {e.read()[:300]!r}", file=sys.stderr)
            return 2
    except Exception as e:  # noqa: BLE001
        print(f"GEMINI_ERROR: {e}", file=sys.stderr)
        return 2

    found = _find_inline_image(data)
    if not found:
        print("GEMINI_ERROR: no inline image in response (model returned text only)",
              file=sys.stderr)
        return 2
    _mime, raw = found

    out.parent.mkdir(parents=True, exist_ok=True)
    if out.suffix.lower() == ".webp" and _to_webp(raw, out, max_kb):
        pass
    else:                                         # keep PNG (no Pillow or non-webp target)
        png = out.with_suffix(".png")
        png.write_bytes(raw)
        out = png
    kb = out.stat().st_size / 1024
    if kb > max_kb:
        print(f"WARN: {out.name} is {kb:.0f} KB (> {max_kb} KB cap) — Pillow/WebP conversion "
              f"failed; prefer the SVG infographic or re-run once Pillow is available.",
              file=sys.stderr)
    print(f"{out}  ({kb:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
