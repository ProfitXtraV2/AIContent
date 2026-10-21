# 08 — Gemini image review, pass 1 — Sizzling Hot

Model: gemini-3.1-pro-preview · script: scripts/gemini_image_review.py
Images reviewed: images/sizzling-hot-rtp.svg + images/sizzling-hot-hero.webp (3-reel hero)

**Score: 65/100 · NEEDS WORK.**

## Gemini verbatim
Overall, both the hero image and the infographic are of high quality, clean, and highly relevant to the article. They avoid all critical failures (no fake UI, no real logos, no faces, neutral tone).

**Image 1: sizzling-hot-rtp.svg**
- Problems: None. The math, figures, and claims perfectly match the article text. Layout is clean, margins are respected, and no text overlaps or clips. Tone is neutral and responsible.
- Fixes: N/A. Ready to publish.

**Image 2: sizzling-hot-hero.webp**
- Problems: Accuracy failure. The image depicts symbols arranged in 3 columns, and the ALT text explicitly says "подредени в три барабана" (arranged in three reels). However, the article text explicitly states the game features "Пет барабана" (Five reels).
- Fixes: Adjust the AI generation prompt to specify "5 columns of retro slot symbols" to match the game's actual grid. Update the ALT text from "три барабана" to "пет барабана".

## Decision
Infographic: PASS, no fixes. Hero: accuracy mismatch (3 vs 5 reels) → regenerate with five symbols in a row + fix ALT to "пет барабана" (image fix pass 2). No integrity failure. Re-review after regen.
