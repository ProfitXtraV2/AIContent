# 08 — Gemini image review — pass 1

Images reviewed: `images/liga-na-naciite-format.svg` (SVG source) + `images/liga-na-naciite-hero.webp` (raster).

**Score: 75/100 — Verdict: NEEDS WORK**

Integrity: PASS (0 fabrication). Infographic numbers match the article exactly; hero has no faces,
no real logos, no national flags, no glamorised gambling; SEO filenames + Bulgarian ALT accurate.

Gemini (verbatim, trimmed):
### 1. Layout Collision in SVG Infographic
- Labels `▲ промоция` (y=170) and `▼ изпадане` (y=340) both at x=548; the "Ключови числа" panel begins at x=560 → the left-aligned ~70px labels bleed over the panel border/background.
- At y=340 the League D rect ends at x=525, leaving only a 35px gutter; the "▼ изпадане" label cannot fit without overlapping the blue rect or the panel.
### 2. Hero Image & SEO Metadata — PASS
- The raster hero captures the stadium atmosphere in neutral flat-vector style, no faces/logos/glamorised gambling. SEO metadata descriptive and accurate.
### Actionable fixes
- Widen the gutter between the pyramid and the key-numbers panel; move the arrow elements so no characters touch the blue boxes or the right-side panel.

→ FIX APPLIED (image fix pass 1): narrowed the division rectangles (A/B/C/D now end at 400/420/440/460),
replaced the two overlapping word-labels with compact arrow GLYPHS (▲ green / ▼ red) at x=486 (26px clear
of the rects, 52px clear of the panel); the words „промоция/изпадане" moved into the bottom caption.
No number/fact changed. Re-run as review 2.
