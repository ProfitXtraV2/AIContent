# Step-8 Image Scripts — Live Gemini API Validation
**Date:** 2026-09-08  
**Branch:** validate/images-2026-09-08

## Overall Status: PARTIALLY LIVE-READY

Image review (Tests C & D) works correctly. Image generation (Test A) works — the Gemini API responds and produces an image — but the output is a **PNG fallback at ~972 KB, far exceeding the 100 KB target**. The generation script cannot currently deliver a lightweight WebP as intended. Fix required before Step 8 is production-ready.

---

## Pre-flight Checks

| Item | Status |
|---|---|
| `scripts/gemini_image_gen.py` | ✅ Found |
| `scripts/gemini_image_review.py` | ✅ Found |
| `VsichkiKazina/pipeline/prompts/step-8-images.md` | ✅ Found |
| `VsichkiKazina/pipeline/prompts/step-8-image-review.md` | ✅ Found |
| `GEMINI_API_KEY` set | ✅ YES |

---

## Test Results

| Test | Description | Model | Exit Code | Result | File Size | Score / Verdict |
|---|---|---|---|---|---|---|
| **A — Image Gen** | Slot-reel hero image via Gemini | imagen-3 / Gemini (inferred) | 0 | PNG fallback (not WebP) | **972 KB** (target: < 100 KB) | N/A — size FAIL |
| **C — Raster Review** | Review hero-test.png against article | Gemini (review model) | 0 | Returned verdict | 972 KB input | **55/100 — NEEDS WORK** |
| **D — SVG Review** | Review hand-authored SVG against article | Gemini (review model) | 0 | Returned verdict | 2.1 KB input | **90/100 — PASS** |

---

## Test A — Image Generation Detail

**Command:**
```
python3 scripts/gemini_image_gen.py "<slot reel prompt>" validate/hero-test.webp 100
```

**Outcome:**
- Exit code: **0** (no crash)
- Printed output path: `validate/hero-test.png` ← PNG fallback, not WebP
- File size: **971.7 KB (~972 KB)** — target is < 100 KB
- The script accepted the 100 KB limit argument but produced a PNG well above it

**Issue:** The script falls back from WebP to PNG and does not enforce the byte-size constraint. The Gemini Imagen API returns a PNG; the script renames output but does not convert or compress to meet the size budget.

**Suggested fix:** Add Pillow-based WebP conversion with quality tuning after download:
```python
from PIL import Image
img = Image.open(tmp_png)
img.save(output_path, "WEBP", quality=75, method=6)
# check size, reduce quality if still over max_kb
```

---

## Test C — Raster Review Detail

**Command:**
```
python3 scripts/gemini_image_review.py validate/article.md validate/hero-test.png
```

**Full verdict:**
> **Score:** 55/100  
> **Verdict:** NEEDS WORK  
>
> **Problems:**
> - Relevance & Value: The image is generic filler. While it depicts slot reels, it fails to illustrate the core topic: wagering requirements, multipliers, locked balances, or game contributions.
> - SEO Metadata: The filename `hero-test.png` is non-descriptive. No Bulgarian ALT text provided.
>
> **Actionable Fixes:**
> - Change generation prompt to focus on wagering mechanics (padlock on chips, prominent "x30" multiplier, visual scale slot 100% vs roulette 10%).
> - Rename file descriptively; add Bulgarian ALT text.

**Assessment:** The review script works correctly — it calls the API, receives a structured score, and provides actionable feedback. The low score reflects the generation prompt mismatch (generic slot image for a wagering-mechanics article), not a script defect.

---

## Test D — SVG Review Detail

**Command:**
```
python3 scripts/gemini_image_review.py validate/article.md validate/infographic-test.svg
```

**Full verdict (translated highlights):**
> **Score: 90/100**  
> **Verdict: PASS**
>
> **Issues noted (minor):**
> 1. Filename `infographic-test.svg` contains "test" — not production-descriptive.
> 2. No ALT text provided (expected at publish time).
> 3. Number format inconsistency: article uses `€3,000` (comma), SVG uses `€3 000` (space) — space is more correct in Bulgarian but inconsistent.
>
> **Positive note (reviewer):** "Инфографиката е отлична. Напълно точна спрямо математиката в текста, изчистен дизайн, без забранени елементи, ясно предупреждение за отговорна игра."

**Assessment:** SVG review works correctly and returns a high-quality structured verdict with nuanced feedback.

---

## Summary & Recommended Fixes

### What works ✅
- `gemini_image_review.py` is fully operational — it handles both PNG/raster and SVG inputs, calls the live API, returns scores 0–100 with PASS/NEEDS WORK, and provides actionable Bulgarian-language feedback.
- `gemini_image_gen.py` connects to the Gemini API successfully (exit 0, no auth errors).

### What needs fixing ⚠️
1. **PNG fallback / size**: `gemini_image_gen.py` cannot produce WebP within the KB budget. Add post-download Pillow conversion + quality loop to enforce the `max_kb` argument.
2. **Generation prompt quality**: The generic slot-reel prompt scores 55/100 on a wagering-mechanics article. Step 8's `step-8-images.md` prompts should be article-context-aware (inject the article topic/headline into the image prompt).
3. **SVG number formatting**: Minor — align `€3 000` vs `€3,000` convention across article and infographic templates.
