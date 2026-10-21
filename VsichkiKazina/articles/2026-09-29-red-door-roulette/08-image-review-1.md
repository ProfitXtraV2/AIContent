# 08 — IMAGE REVIEW (Step 8), pass 1 · Red Door Roulette (Evolution)

IMAGES CREATED: 1 hand-authored SVG data infographic — images/red-door-roulette-kljuchove-mnozhiteli-rtp-infografika.svg
AI HERO: SKIPPED — gemini_image_gen.py depends on the same Gemini API (HTTP 402). Logged
`image gen: skipped (Gemini unavailable)`. Infographic ships alone (never blocks the PR).

GEMINI VISUAL REVIEW:
COMMAND: python3 scripts/gemini_image_review.py articles/2026-09-29-red-door-roulette/05b-final-draft.md images/red-door-roulette-kljuchove-mnozhiteli-rtp-infografika.svg
RESULT: SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). Logged `image review: skipped (Gemini unavailable)`.
Per rules: keep the image, do NOT halt.

MANUAL INTEGRITY CHECK (orchestrator, since automated review is offline): PASS.
- Every number in the SVG (visible text + aria-label) is copied verbatim from 05b — verified
  programmatically (37 джоба/една нула, стрейт-ъп 19:1 vs 35:1, сплит 17:1, ред/черно 1:1, 3–15
  бонус числа, ключове 2x–20x, 64 сегмента, Double, 4000x, €500 000, RTP 97,09%/97,30%,
  предимство ≈2,9%/≈2,7% — all ⊂ body). ✓
- No operator logos/names, no fake screenshots. ✓
- No invented bonus/RTP/licence numbers (all figures trace to sourced 05b; the version-dependent
  segment/4000x detail carries the in-text „примерни стойности" caution). ✓
- No people/faces; no glamorised winning (honest framing: множителите платени от орязания
  стрейт-ъп; предимството остава ≈2,7–2,9%; 4000x/€500 000 са редки). ✓
- Descriptive lowercase-hyphenated filename; specific Bulgarian ALT + caption referenced from 05b. ✓
- Layout: viewBox 720×512, rounded card 704×496 with ≥16px inner padding; left labels start
  x=32/48; longest lines estimated (chars × font × 0.62) end ≥16px before the card's right edge;
  text rows spaced ≥18–20px (y-values checked, no overlap); no em-dash in the SVG. ✓

images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS).
