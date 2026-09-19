# Gemini Step-8 image review — pass 1

Model: gemini-3.1-pro-preview · Date: 2026-09-19
Images: le-pharaoh-rtp.svg (infographic), le-pharaoh-hero.webp (decorative hero)

**SCORE: 70 · VERDICT: NEEDS WORK** · No integrity failure (no fabricated logos/numbers/screenshots, no faces, no glamorised winning; every SVG number traces to 05b).

Verbatim problems:
1. SVG layout: the two bottom summary boxes had tight bottom margins (box `y=211 height=74` ends at 285 with a 1.5px stroke; the descenders on the caption line at `y=280` left <2px margin).
2. SVG rendering: the player bar (`rx=8`) and house bar (`rx=4`) met flush at `x=530` with clashing corner radii, leaving a visible background-colour gap at the seam.
3. Hero raster: clean, relevant, correctly formatted, no prohibited elements — passes all checks.

Fixes applied (pass 1):
- Wrapped both bar segments in a `<g clip-path>` bound to one rounded container rect (rx=8) and used square-cornered rects → flush seam, no gap.
- Increased both summary boxes to `height=86` and nudged text baselines, giving comfortable bottom margin; widened the viewBox to `0 0 600 340`.
- Hero: no change needed (passed).
