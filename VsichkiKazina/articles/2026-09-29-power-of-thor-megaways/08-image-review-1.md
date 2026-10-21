# 08 — IMAGE REVIEW (Step 8), pass 1 · Power of Thor Megaways (Pragmatic Play)

IMAGES CREATED: 1 hand-authored SVG data infographic — images/power-of-thor-megaways-rtp-volatilnost-infografika.svg
AI HERO: SKIPPED — gemini_image_gen.py depends on the same Gemini API (HTTP 402). Logged
`image gen: skipped (Gemini unavailable)`. Infographic ships alone (never blocks the PR).

GEMINI VISUAL REVIEW:
COMMAND: python3 scripts/gemini_image_review.py articles/2026-09-29-power-of-thor-megaways/05b-final-draft.md images/power-of-thor-megaways-rtp-volatilnost-infografika.svg
RESULT: SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). Logged `image review: skipped (Gemini unavailable)`.
Per rules: keep the image, do NOT halt.

MANUAL INTEGRITY CHECK (orchestrator, since automated review is offline): PASS.
- Every number in the SVG (visible text + aria-label) is copied verbatim from 05b — verified
  programmatically (6 барабана + горен ред, до 117 649 начина, множител само в FS старт 1x, максимум
  5000x, FS от 4+ THOR = 10/+4/до 30, buy 100x RTP 96,97%, честота ~1/510 и ~1/860 000, RTP 96,55%
  default + 95,81%/94,77%, волатилност 5/5 — all ⊂ body). ✓
- No operator logos/names, no fake screenshots. ✓
- No invented bonus/RTP/licence numbers (all figures trace to sourced 05b; the reviewer-estimate
  frequencies and configurable-RTP uncertainty carry in-text [VERIFY] cautions + caption). ✓
- No people/faces; no glamorised winning (honest framing: множителят носи стойност само при дълга
  каскада; бонусът е рядък; „без таван" опира до 5000x; buy feature не мени предимството). ✓
- Descriptive lowercase-hyphenated filename; specific Bulgarian ALT + caption referenced from 05b. ✓
- Layout: viewBox 720×512, rounded card 704×496 with ≥16px inner padding; left labels start
  x=32/48; longest lines estimated (chars × font × 0.62) end ≥16px before the card's right edge;
  rows spaced ≥18–20px (no overlap); no em-dash in the SVG. ✓

images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS).
