# Step 8 — Gemini image review, pass 2 (hero regeneration)

Model: gemini-3.1-pro-preview (multimodal). Only the hero was iterated (infographic already PASS 100 in pass 1).

## Hero regeneration attempt (v2)
Prompt hardened to force exactly 5 reel columns.
**Score: 75/100 · NEEDS WORK.** Improved over v1 (60 → 75). Gemini now counts 6 columns (the abstract dividers read as 6 rather than 5). No integrity failure (no fake UI, faces, operator logos, or glamorised winning; the fruit + red-7 shapes are generic game symbols, not fabricated bonus/RTP numbers).

## Decision — keep-best (MAX_IMAGE_PASSES=2 reached)
Both hero attempts have a minor AI reel-count artifact (v1: 3 reels, score 60; v2: reads as 6, score 75). Neither is an integrity failure. Per keep-best, **kept v2 (score 75)** — the highest-scoring version seen (already on disk). The reel count is cosmetic on a purely decorative banner; the article's data is carried entirely by the infographic (PASS 100), the primary illustration for this slot guide.

## Final image set
- `images/burning-hot-rtp.svg` — infographic, **100/100 PASS** (all figures trace to 05b).
- `images/burning-hot-hero.webp` — decorative hero, **75/100** (kept-best; no integrity issue).
images: 2 · best review score 100.
