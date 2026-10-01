# Image Review Pass 1 — 2026-10-01-e-portfeili-skrill-neteller

## Images reviewed
- images/e-portfeil-skorost-bonus.svg (hand-authored infographic)

## Verdict
GEMINI_UNAVAILABLE — HTTP 402; image review skipped. Manual integrity check: PASS — every number/claim traces to 05b; no operator logos/names; no people/faces; no glamorised winning; no fabricated figures.

## Manual integrity detail
- Numbers/claims vs 05b: „моментален" (депозит) ✓; „до 24 часа" (теглене след одобрение) ✓; „много казина изключват Skrill/Neteller от бонуса" ✓; „примерни срокове, зависят от казиното" ✓; „18+ Играйте отговорно" ✓. All trace to 05b.
- viewBox 0 0 720 352; ≥16px inner padding all sides; title/subtitle + two cards + bonus-catch bar + footer — no text touches an edge, no overlaps, no clipping. Longest line („депозит през портфейл често не активира бонуса за добре дошли") est. width ≈ 60 chars × 11 × 0.62 ≈ 409px, centered in 640px card → fits with slack.
- No operator logos or brand names (Skrill/Neteller are the payment-method names the article is about, used as plain text, not logos/UI); no people/faces; no photoreal or glamorised winning imagery. Neutral, RG-appropriate; carries „18+ Играйте отговорно".
- Well-formed XML (parsed OK); has <title> + aria-label with a specific Bulgarian description.

## Decision — KEEP (manual PASS, Gemini review skipped 402)
No integrity failures. Ship in the content PR. images: 1 (infographic, manual integrity PASS).
