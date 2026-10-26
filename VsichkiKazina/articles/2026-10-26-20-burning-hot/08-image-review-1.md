# 08 — Gemini image review · pass 1

Script: `python3 scripts/gemini_image_review.py 05b-final-draft.md images/20-burning-hot-rtp.svg images/20-burning-hot-hero.webp`
Run: 2026-10-26

**Score: 60/100 — NEEDS WORK** (no integrity failure: numbers trace to 05b, no operator logos/names, no fabricated bonus/RTP, no people/faces, no glamorised winning). → iterate (pass 2, within MAX_IMAGE_PASSES=2).

## Gemini verbatim

### 1. SVG Infographic — Layout Integrity Failure (Text Collision)
- The text label `4.12%` (x=539 y=82) collides with and overlaps the column header `Домашно предимство` (x=550 y=80); they share the same vertical space and horizontal alignment area, rendering on top of each other.
- Fix: move `4.12%` into the red bar (y=120, white fill) like the player RTP %, or move it significantly higher/lower to clear the header's bounding box.

### 2. Raster hero — Technical Quality & AI Hallucinations
- Hallucinated diagonal lines forming an "X" inside every cell across the 5x3 board → looks like a wire fence / crossed-out boxes, not reels/paylines.
- The red "7" on reel 1 is misshapen and structurally different from the "7" on reel 2.
- Fix: regenerate with a modified prompt; remove the diagonal "payline path" instruction, simpler grid (vertical lines between reels, horizontal between rows, no diagonal lines inside cells).

### 3. SEO Metadata — PASS
- Both filenames hyphenated/descriptive; Bulgarian ALT texts specific and accurate, no keyword stuffing.
