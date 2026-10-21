# Image Review Pass 1 — 2026-10-01-revolut-kazino

## Images reviewed
- images/revolut-blokirovka-hazart.svg (hand-authored infographic)

## Verdict
GEMINI_UNAVAILABLE — HTTP 402; image review skipped. Manual integrity check: PASS — every claim/number traces to 05b; no operator logos/names; no people/faces; no glamorised winning; no fabricated figures.

## Manual integrity detail
- Claims vs 05b: „включване веднага" ✓; „изключване до 48 часа (период на изчакване; поддръжката не го заобикаля)" ✓; „спира картови плащания към хазартни търговци (по MCC); не блокира банкови преводи" ✓; „18+ Играйте отговорно · ... включи блокировката" ✓. All trace to 05b.
- viewBox 0 0 720 352; ≥16px inner padding all sides; title/subtitle + two cards + MCC bar + footer — no text touches an edge, no overlaps, no clipping. Longest footer line est. ≈ 72 chars × 11 × 0.62 ≈ 491px, centered in 720px → fits with slack.
- Revolut appears only as plain-text method name (the article's subject), NOT as a brand logo, UI, or fake screenshot. No people/faces; no glamorised winning. Neutral, RG-appropriate (the graphic is itself an RG self-control tool); carries „18+ Играйте отговорно".
- Well-formed XML (parsed OK); 0 em-dashes (title em-dash fixed to comma); <title> + aria-label with a specific Bulgarian description.

## Decision — KEEP (manual PASS, Gemini review skipped 402)
No integrity failures. Ship in the content PR. images: 1 (infographic, manual integrity PASS).
