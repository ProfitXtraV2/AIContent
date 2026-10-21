# 08 — IMAGE REVIEW (Step 8), pass 1 · Gonzo's Quest Megaways (Red Tiger)

IMAGES CREATED: 1 hand-authored SVG data infographic — images/gonzos-quest-megaways-rtp-mnozhiteli-infografika.svg
AI HERO: SKIPPED — gemini_image_gen.py depends on the same Gemini API (HTTP 402). Logged
`image gen: skipped (Gemini unavailable)`. Infographic ships alone (never blocks the PR).

GEMINI VISUAL REVIEW:
COMMAND: python3 scripts/gemini_image_review.py articles/2026-09-29-gonzos-quest-megaways/05b-final-draft.md images/gonzos-quest-megaways-rtp-mnozhiteli-infografika.svg
RESULT: SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). Logged `image review: skipped (Gemini unavailable)`.
Per rules: keep the image, do NOT halt.

MANUAL INTEGRITY CHECK (orchestrator, since automated review is offline): PASS.
- Every number in the SVG (visible text + aria-label) is copied verbatim from 05b — verified
  programmatically (6 барабана / 2–7 реда, до 117 649 начина, множители 1x→2x→3x→5x и 3x→6x→9x→15x,
  ≥3 Free Fall / старт 9, RTP 95,77% под кръглите 96%, конфигурируем към ~90%, висока волатилност,
  максимум ≈20 972x — all ⊂ body). ✓
- No operator logos/names, no fake screenshots. ✓
- No invented bonus/RTP/licence numbers (all figures trace to sourced 05b; the configurable-RTP and
  free-spins-count uncertainties carry in-text [VERIFY] cautions + caption). ✓
- No people/faces; no glamorised winning (honest framing: множителите носят стойност само при серия;
  RTP е конфигурируем и е дългосрочна средна; 20 972x е рядък твърд таван). ✓
- Descriptive lowercase-hyphenated filename; specific Bulgarian ALT + caption referenced from 05b. ✓
- Layout: viewBox 720×512, rounded card 704×496 with ≥16px inner padding; left labels start
  x=32/48; longest lines estimated (chars × font × 0.62) end ≥16px before the card's right edge;
  rows spaced ≥18–20px (no overlap); ladder arrows „→" used (not em-dashes); no em-dash in the SVG. ✓

images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS).
