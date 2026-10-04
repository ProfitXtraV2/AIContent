# 08 — Gemini image review, pass 1 (Plinko)

Command: `python3 scripts/gemini_image_review.py .../05b-final-draft.md images/plinko-rtp.svg images/plinko-hero.webp`
Model: gemini-3.1-pro-preview · Exit 0

## Verbatim verdict
**Score: 60/100 — NEEDS WORK.** No integrity failure (no fabricated operator logo/name/screenshot, no invented bonus/RTP number, no people/faces, no glamorised winning).

- **plinko-hero.webp (raster):** logic/AI artifact — the glowing ball path branches to two bottom slots at once (physically impossible vs the single-path mechanic in the text); geometric mismatch (14 peg rows but only 9 slots shown); the trail connects pegs like a constellation instead of showing the ball falling between them. (Decorative image; flagged as quality, not integrity.)
- **plinko-rtp.svg (infographic):** "всичко останало е отлично: текстът отговаря на статията, няма припокриващи се шрифтове, числата са точни, метаданните са перфектни." Only micro-defect: rounded blue-bar corner leaves a tiny grey notch where the red house-edge bar starts.

## Fix decision (pass 1)
- SVG: extend blue RTP bars so the red house-edge bar overdraws the rounded corner (width 495→500 and 485→490). Numbers unchanged, still trace to 05b.
- Hero: regenerate with a prompt that removes the trajectory entirely (pegs + bins + single resting ball, no path/trail/connecting lines). Then re-review (pass 2).
