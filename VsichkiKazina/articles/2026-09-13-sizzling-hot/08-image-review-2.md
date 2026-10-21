# 08 — Gemini image review, pass 2 — Sizzling Hot

Model: gemini-3.1-pro-preview · script: scripts/gemini_image_review.py
Images reviewed: images/sizzling-hot-rtp.svg + images/sizzling-hot-hero.webp (5-symbol hero)

**Score: 92/100 · PASS.** No integrity failures (no fake UI, no real logos, no faces, neutral tone).

## Gemini verbatim
Overall, both the hero image and the infographic are of high quality, clean, and highly relevant to the article. They avoid all critical failures (no fake UI, no real logos, no faces, neutral tone). However, there are two minor issues regarding strict layout margins in the SVG and a slight symbol inaccuracy in the raster image.

**1. SVG Layout: Extremely Tight Bottom Margins (Minor Defect)**
- Problem: the bottom labels „(средно, дългосрочно)" and „(домашно предимство ~4.34%)" at y="276" sit very close to the box bottom (y="281"); gap < 2px. Doesn't clip, but tight.
- Fix: shift the three text elements in both boxes up 7px (y 233→226, 261→254, 276→269).

**2. WebP Accuracy: Combined Symbols (Minor Defect)**
- Problem: the fiery 7 and the star are drawn as one combined symbol, while the article treats them as separate entities (седмица = top regular symbol; звезда = scatter). Matches the ALT verbatim but slightly contradicts the body.
- Fix (optional): regenerate separating the symbols, or omit the star from the prompt.

## Decision
PASS at 92 (up from 65 on pass 1). KEEP-BEST hero = pass-2 (5-symbol) version. Applied the trivial, strictly-safer SVG margin fix (y-shift 7px, re-rendered and eyeballed — text now comfortably centered, still no clip/overlap). Left the hero as-is: minor star-attached-to-7 note is cosmetic, no integrity failure, and a third regen risks a lower score (iteration cap reached at 2 passes). Both images ship. Best image-review score = 92.
