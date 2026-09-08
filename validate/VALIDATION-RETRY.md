# Step-8 Image Generation — Retry Validation (2026-09-08)

## LIVE-READY STATUS: YES ✅

Image generation now produces a **real WebP file under 100 KB**.  
The Pillow/WebP fix is working correctly in the live environment.

---

## Test A — Generation Results

| Field | Value |
|---|---|
| Script | `scripts/gemini_image_gen.py` |
| Output file | `validate/hero-retry.webp` |
| File type | RIFF WebP (VP8, 1024×1024, YUV) — confirmed real WebP |
| Size | **24.3 KB** (24,864 bytes) — well under 100 KB limit |
| Exit code | 0 |
| WARN line appeared? | **No** — Pillow auto-install ran silently (pip venv advisory only, not the script's WARN) |

The script auto-installed Pillow (pip ran at invocation), converted the API
response to WebP, and enforced the size cap without errors.  
Previous run produced `hero-test.png` at ~972 KB — that regression is resolved.

---

## Test C — Image Review

| Field | Value |
|---|---|
| Script | `scripts/gemini_image_review.py` |
| Article | `validate/article.md` |
| Image | `validate/hero-retry.webp` |
| Exit code | 0 |
| Score | **65 / 100** |
| Verdict | **NEEDS WORK** |

### Review problems noted

- **Relevance:** Generic slot reels don't illustrate the article's core topic
  (wagering requirements, multipliers, locked balances).
- **SEO:** `hero-retry.webp` is a non-descriptive filename; no ALT text passed.

### Recommended fixes for production runs

1. Use a concept-specific prompt: progress bar unlocking a padlock, "x30"
   multiplier graphic, or balance scale (bonus vs. required turnover).
2. Rename output to something descriptive, e.g. `wagering-requirements-slots.webp`.
3. Pass article-specific Bulgarian ALT text in the pipeline.

> The review score reflects the image's conceptual mismatch with the article,
> **not** a technical failure of the generation or format pipeline.  
> The infrastructure (API call → WebP → < 100 KB) is confirmed working.

---

## Summary

The Pillow/WebP fix is successful. Step-8 is **live-ready**: the script
generates compliant WebP images under the size cap with exit 0. The 65/NEEDS
WORK review verdict is a prompt-quality signal — production runs should use
article-matched prompts rather than the generic test prompt used here.
