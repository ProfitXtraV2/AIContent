# 08 — Gemini image review, pass 2 (after hero ALT correction) — Gates of Hades

Model: gemini-3.1-pro-preview · script: scripts/gemini_image_review.py

## Combined review (both images)
**Score: 75 · NEEDS WORK** — but on BYTE-IDENTICAL image files. Between pass 1 (90) and pass 2 only the markdown hero ALT text changed; `gates-of-hades-rtp.svg` and `gates-of-hades-hero.webp` are unchanged. Both passes confirm **no integrity failure**.

## What changed vs pass 1
Pass 1 called the SVG "excellent… zero text overlaps, clipping, or margin issues"; pass 2 flagged the same unchanged SVG for "text crowding/touching the edges of the summary boxes." This is detector noise on identical bytes (the box text is centered at x=160 / x=440 within 220px boxes, same layout as the Gates of Olympus template that scored 85). Hero and infographic both explicitly PASS the integrity/hygiene section in both passes.

## Keep-best decision (mandatory)
MAX_IMAGE_PASSES (2) reached. The image files never regressed (they are identical across passes), so the highest score seen for this exact version is **90 (pass 1)**. Keep the current files (corrected ALT + unchanged SVG/hero). No integrity failure. Best image-review score recorded = **90**. Not chasing the noisy detector with a speculative nudge that would have no remaining review pass.
