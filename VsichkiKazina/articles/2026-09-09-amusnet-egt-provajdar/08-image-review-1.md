# 08 — Gemini image review, pass 1 — Amusnet / EGT

Model: gemini-3.1-pro-preview · script: scripts/gemini_image_review.py

## Image 1 — images/amusnet-egt-rtp.svg (infographic)
**Score: 100/100 · PASS.** All numbers (96.37% / 95.81% / 95.79% / 95.53% / ~96% / ~90%) match the article verbatim; source (Wizard of Odds) cited; 18+/RG note present; ALT thorough; bar math against the 95.00–96.50% scale correct; green=above / amber=below hierarchy aids comprehension. No fixes needed.

## Image 2 — images/amusnet-egt-hero.webp (decorative AI hero, 19.9 KB)
**Score: 55/100 · NEEDS WORK.** No integrity failure (no operator logo/brand, no fabricated number, no person/face, no glamorised winning). Quality/aesthetic defect only: the 3D reel cylinders scatter symbols across the drum surface (physically impossible layout), and a seven on the leftmost reel is clipped. Reviewer recommends a flat 2D layout, not 3D reels.

## Decision
Infographic PASS (kept). Hero 55 < 80 → regenerate with a flat 2D prompt (no 3D reels), re-review (MAX_IMAGE_PASSES=2). Keep-best tracker: hero pass 1 = 55.
