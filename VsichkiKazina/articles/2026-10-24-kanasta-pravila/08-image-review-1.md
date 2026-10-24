# 08 — Gemini image review, pass 1

Run 24.10.2026 · scripts/gemini_image_review.py on 05b + 2 images (infographic SVG + hero WebP, first hero generation).

## Verdict (verbatim)
**Score: 65/100 — NEEDS WORK**

Overall, the SVG infographic is excellent and perfectly aligned with the article, but the raster hero image suffers from severe AI hallucinations on the core subject matter (the playing cards).

### 1. Raster hero (kanasta-karti-kosnica-hero.webp)
- AI hallucination: the cards' suits are inconsistent — the center card shows a large Club but its top-left corner index shows a Diamond; the far-right card shows a Heart at the bottom but a Diamond in the corner; other pips garbled. For a card-game guide the cards must be anatomically correct.
- SEO: filename good; add a Bulgarian ALT.
Fix: re-prompt so suits match, OR remove corner indices and show only large center suits.

### 2. SVG infographic (kanasta-stoynost-karti-bonusi.svg)
- FLAWLESS: strictly matches every number and rule in the article; layout mathematically sound, generous margins, no overlap/clip; RG/18+ placement correct; aria-label ALT highly specific and accurate.
- Minor copywriting nit: subtitle "точките по-долу са в точки" is redundant.

## Action taken (→ pass 2)
- SVG: subtitle changed to "стойностите по-долу са в точки" (redundancy removed).
- Hero: regenerated with corner indices removed (only large centered suit symbols) so suits cannot be misread; re-reviewed in pass 2.
- No integrity failure in either image (no operator logos/names, no invented numbers, no people/faces, no glamorised winning). Hero issue was anatomical/aesthetic, not integrity.
