#!/usr/bin/env python3
"""One-off: Gemini image generation guided by reference photos (image-to-image style transfer).

Usage: ASPECT=4:5 python3 WeddingSite/oneoff/gen_from_ref.py "<prompt>" <out.webp> <ref1.jpg> [ref2.jpg ...]
"""
import base64, io, json, os, sys, urllib.error, urllib.request
from pathlib import Path

MODELS = [os.environ.get("GEMINI_IMAGE_MODEL", "gemini-3-pro-image"), "gemini-2.5-flash-image"]
API = "https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent"


def main():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("GEMINI_UNAVAILABLE", file=sys.stderr); return 2
    prompt, out, refs = sys.argv[1], Path(sys.argv[2]), sys.argv[3:]
    parts = [{"inline_data": {"mime_type": "image/jpeg", "data": base64.b64encode(Path(r).read_bytes()).decode()}} for r in refs]
    parts.append({"text": prompt})
    raw, errs = None, []
    for m in MODELS:
        for ic in (True, False):
            cfg = {"responseModalities": ["TEXT", "IMAGE"]}
            if ic:
                cfg["imageConfig"] = {"aspectRatio": os.environ.get("ASPECT", "4:5")}
            body = {"contents": [{"parts": parts}], "generationConfig": cfg}
            req = urllib.request.Request(API.format(m=m), data=json.dumps(body).encode(),
                                         headers={"Content-Type": "application/json", "x-goog-api-key": key})
            try:
                with urllib.request.urlopen(req, timeout=300) as r:
                    data = json.load(r)
            except urllib.error.HTTPError as e:
                errs.append(f"{m} ic={ic}: HTTP {e.code} {e.read()[:200]!r}"); continue
            except Exception as e:  # noqa: BLE001
                errs.append(f"{m} ic={ic}: {e}"); continue
            for c in data.get("candidates", []):
                for p in c.get("content", {}).get("parts", []):
                    i = p.get("inlineData") or p.get("inline_data")
                    if i and i.get("data"):
                        raw = base64.b64decode(i["data"])
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
    out.parent.mkdir(parents=True, exist_ok=True)
    for q in (86, 80, 72, 64):
        img.save(out, "WEBP", quality=q, method=6)
        if out.stat().st_size <= 520 * 1024:
            break
    print(f"{out} {img.size} {out.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
