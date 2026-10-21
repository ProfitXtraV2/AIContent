# Image Review Pass 1 — 2026-10-01-apple-pay-google-pay

## Images reviewed
- images/apple-google-pay-tokenizaciya.svg (hand-authored infographic)

## Verdict
GEMINI_UNAVAILABLE — HTTP 402; image review skipped. Manual integrity check: PASS — every claim traces to 05b; no operator logos/names; no people/faces; no glamorised winning; no fabricated figures.

## Manual integrity detail
- Claims vs 05b: „депозит моментален" ✓; „картовите данни не стигат до казиното (токенизация + биометрия)" ✓; „теглене по свързаната карта, не към портфейла" ✓; „нужни са казино + банка + устройство" ✓; „срокове за теглене по карта са примерни" ✓; „18+ Играйте отговорно" ✓. All trace to 05b.
- viewBox 0 0 720 352; ≥16px inner padding all sides; title/subtitle + two cards + compatibility bar + footer — no text touches an edge, no overlaps, no clipping. Longest footer line est. ≈ 70 chars × 11 × 0.62 ≈ 477px, centered in 720px → fits with slack.
- Apple Pay/Google Pay appear only as plain-text method names (the article's subject), NOT as brand logos, UI, or fake screenshots. No people/faces; no glamorised winning. Neutral, RG-appropriate; carries „18+ Играйте отговорно".
- Well-formed XML (parsed OK); <title> + aria-label with a specific Bulgarian description.

## Decision — KEEP (manual PASS, Gemini review skipped 402)
No integrity failures. Ship in the content PR. images: 1 (infographic, manual integrity PASS).
