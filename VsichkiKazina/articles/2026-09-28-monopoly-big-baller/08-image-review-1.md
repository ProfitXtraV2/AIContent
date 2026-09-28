# 08 — IMAGE REVIEW (Step 8), pass 1 · Monopoly Big Baller (Evolution)

IMAGES CREATED: 1 hand-authored SVG data infographic — images/monopoly-big-baller-bingo-mnozhiteli-rtp-infografika.svg
AI HERO: SKIPPED — gemini_image_gen.py depends on the same Gemini API (HTTP 402). Logged
`image gen: skipped (Gemini unavailable)`. Infographic ships alone (never blocks the PR).

GEMINI VISUAL REVIEW:
COMMAND: python3 scripts/gemini_image_review.py articles/2026-09-28-monopoly-big-baller/05b-final-draft.md images/monopoly-big-baller-bingo-mnozhiteli-rtp-infografika.svg
RESULT: SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). Logged `image review: skipped (Gemini unavailable)`.
Per rules: keep the image, do NOT halt.

MANUAL INTEGRITY CHECK (orchestrator): PASS.
- Every number in the SVG (text + aria-label) copied verbatim from 05b — verified programmatically
  (20 топки от 60 / 5x5 / 96,10% / висока / €500 000 / 10x–20x / 20x–50x / 2x–3x / 199:1 / 39:1 /
  −10–20% / GO all ⊂ body). ✓
- Bonus-card RTPs (96,58% / 95,83%) deliberately NOT put in the graphic (they carry an in-text
  [VERIFY]); only the solid standard-card 96,10% is shown. ✓
- No operator logos/names, no fake screenshots (MONOPOLY board/Mr Monopoly not depicted). ✓
- No invented RTP/max/licence numbers (all trace to sourced 05b). ✓
- No people/faces; no glamorised winning (honest framing: множителите се плащат от базовия RTP;
  повече карти = по-голям залог, не по-добро предимство). ✓
- Descriptive lowercase-hyphenated filename; specific Bulgarian ALT + caption referenced from 05b. ✓
- Layout: viewBox 720×552, two-column panels, ≥16px padding; end-anchored values; SVG well-formed
  (xml parse OK); no overlap/clipping. ✓

images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS).
