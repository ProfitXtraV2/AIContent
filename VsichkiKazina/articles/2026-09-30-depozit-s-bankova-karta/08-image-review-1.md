# Image Review Pass 1 — 2026-09-30-depozit-s-bankova-karta

## Images reviewed
- images/depozit-karta-srokove.svg (hand-authored infographic)

## Verdict
GEMINI_UNAVAILABLE — HTTP 402; image review skipped. Manual integrity check: PASS — every number traces to 05b; no operator logos/names; no people/faces; no glamorised winning; no fabricated figures.

## Manual integrity detail
- Numbers vs 05b: „моментален" (депозит) ✓; „1–5 работни дни" ✓; „Първото теглене изисква KYC верификация" ✓; „примерни срокове" ✓; „18+ Играйте отговорно" ✓. All trace to 05b.
- viewBox 0 0 720 336; ≥16px inner padding on all sides; rendered to PNG at 720px — no text touches an edge, no overlaps, no clipping (title/subtitle, two cards, KYC bar, footer all clear).
- No operator logos or brand names; no people/faces; no photoreal or glamorised winning imagery. Neutral, RG-appropriate; carries „18+ Играйте отговорно".
- Well-formed XML (parsed OK); has <title> + aria-label with a specific Bulgarian description.

## Decision — KEEP (manual PASS, Gemini review skipped 402)
No integrity failures. Ship in the content PR. images: 1 (infographic, manual integrity PASS).
