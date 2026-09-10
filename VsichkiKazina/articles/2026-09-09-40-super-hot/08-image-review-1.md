# 08 — Gemini image review, pass 1 — 40 Super Hot

Model: gemini-3.1-pro-preview · script: scripts/gemini_image_review.py
**Overall score: 82/100 · PASS** (both images).

## Image 1 — images/40-super-hot-rtp.svg (infographic)
**PASS.** Math matches the article exactly (95.81% RTP, 4.19% edge, €958/€42 split); factual neutral tone; 18+/RG note; no fake UI; filename + ALT highly specific. Non-integrity code-hygiene note: player bar drawn as full-track + house overlay. **Applied fix:** player bar set to 479px (95.81% of 500px), house 21px — the two now tile the 500px track exactly. No number changed.

## Image 2 — images/40-super-hot-hero.webp (decorative AI hero, 10.7 KB, flat 2D)
**PASS.** Depicts the described fruit-slot symbols (cherry, lemon, grape, watermelon, 7, star); clean abstract vector; zero glamorisation, faces, or fake operator logos; filename hyphenated-lowercase; Bulgarian ALT accurate. Minor non-integrity note: omits the plum/orange (reviewer says "acceptable as-is") — kept.

## Result
Both images PASS on pass 1 (best 82). No integrity failures. Infographic hygiene fix applied (numbers untouched). Both ride the content PR. No regenerate needed.
