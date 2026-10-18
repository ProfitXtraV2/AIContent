#!/usr/bin/env python3
"""One-off: generate a full-resolution image (default 9:16, override with ASPECT=4:5 etc.) via Gemini (imageConfig aspect ratio).

Usage: python3 WeddingSite/oneoff/gen_hero.py "<prompt>" <out.webp> [max_kb]
Reuses the request helpers from scripts/gemini_image_gen.py; differs only in asking for a
9:16 image and keeping it up to 1600px tall (the article helper caps at 1024).
"""
import base64, json, os, sys, urllib.error, urllib.request, io
from pathlib import Path

MODELS = [os.environ.get("GEMINI_IMAGE_MODEL", "gemini-3-pro-image"), "gemini-2.5-flash-image"]
API = "https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent"


def call(model, key, prompt, image_config=True):
    cfg = {"responseModalities": ["TEXT", "IMAGE"]}
    if image_config:
        cfg["imageConfig"] = {"aspectRatio": os.environ.get("ASPECT", "9:16")}
    body = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": cfg}
    req = urllib.request.Request(API.format(m=model), data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": key})
    with urllib.request.urlopen(req, timeout=240) as r:
        return json.load(r)


def find_image(data):
    for c in data.get("candidates", []):
        for p in c.get("content", {}).get("parts", []):
            i = p.get("inlineData") or p.get("inline_data")
            if i and i.get("data"):
                return base64.b64decode(i["data"])
    return None


def main():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("GEMINI_UNAVAILABLE", file=sys.stderr); return 2
    prompt, out = sys.argv[1], Path(sys.argv[2])
    max_kb = int(sys.argv[3]) if len(sys.argv) > 3 else 700
    raw, errs = None, []
    for m in MODELS:
        for ic in (True, False):
            try:
                raw = find_image(call(m, key, prompt, ic))
            except urllib.error.HTTPError as e:
                errs.append(f"{m} ic={ic}: HTTP {e.code} {e.read()[:200]!r}"); continue
            except Exception as e:  # noqa: BLE001
                errs.append(f"{m} ic={ic}: {e}"); continue
            if raw:
                print(f"model={m} imageConfig={ic}"); break
            errs.append(f"{m} ic={ic}: no image")
        if raw:
            break
    if not raw:
        print("GEMINI_ERROR: " + " | ".join(errs), file=sys.stderr); return 2
    try:
        from PIL import Image
    except ImportError:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "Pillow"], check=True)
        from PIL import Image
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    print("native size", img.size)
    if img.height > 1600:
        img.thumbnail((1600, 1600))
    out.parent.mkdir(parents=True, exist_ok=True)
    for q in (86, 80, 74, 68, 60):
        img.save(out, "WEBP", quality=q, method=6)
        if out.stat().st_size <= max_kb * 1024:
            break
    out.with_suffix(".png").write_bytes(raw)   # keep the original too
    print(f"{out} {img.size} {out.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
