# 08 — Gemini image review, pass 1 — Wild Wild Riches

Model: gemini-3.1-pro-preview · script: scripts/gemini_image_review.py

## Combined review (both images)
**Score: 75 · NEEDS WORK.** No integrity failure (no fake UI/logos/numbers, no people/faces, no glamorised winning; every SVG figure traces to 05b).

## Image 1 — images/wild-wild-riches-rtp.svg (infographic)
Problem: layout/margin risk. The footer line at `y="312"` (~110 chars at font-size 11) renders ~590–600px wide on a 600px canvas → touches/clips left+right edges. Fix: split into two shorter `<text>` lines and adjust footer y-coordinates.

## Image 2 — images/wild-wild-riches-hero.webp (decorative AI hero, 37.5 KB)
"No changes needed. Highly relevant, technically clean, perfectly matches the Irish folklore theme… excellent descriptive Bulgarian ALT text." Effectively PASS.

## Decision
Hand-fix the SVG footer (split the long line, adjust y-coords; numbers unchanged, still trace to 05b), then re-run the review as pass 2. Hero kept as is.
