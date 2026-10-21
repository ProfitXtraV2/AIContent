# Image Review Pass 1 — 2026-10-01-bankov-prevod-kazino

## Images reviewed
- images/bankov-prevod-srokove.svg (hand-authored infographic)

## Verdict
GEMINI_UNAVAILABLE — HTTP 402; image review skipped. Manual integrity check: PASS — every claim/number traces to 05b; no operator logos/names; no people/faces; no glamorised winning; no fabricated figures.

## Manual integrity detail
- Claims/numbers vs 05b (each traces):
  - „≈ 1 работен ден" (самият превод) ← 05b „самият превод обикновено стига до банката получател за един работен ден". ✓
  - „секунди само при SEPA Instant (24/7)" ← 05b „SEPA Instant, който движи парите за секунди в режим 24/7". ✓
  - „няколко работни дни · в двете посоки" ← 05b „цялата обиколка излиза няколко работни дни, и то в двете посоки". ✓
  - „Такси: казиното обикновено не начислява · банката може да вземе такса за изходящ превод по тарифата си" ← 05b „Казиното обикновено не начислява собствена такса … тарифата на твоята банка, която за изходящ превод понякога взема такса според плана ти". ✓
  - „до десетки хиляди евро на превод (примерни)" ← 05b „до десетки хиляди евро на превод (примерни суми)". ✓
  - „примерно €20 вместо €5 или €10 при картите (примерни)" ← 05b „примерно €20 вместо €5 или €10 при картите (примерни прагове)". ✓ (number formatting €20/€5/€10 matches 05b exactly)
  - „Тегленето се връща по сметката, от която е дошъл депозитът" ← 05b verbatim. ✓
  - „лицензът от НАП е защитата, методът е удобство" ← 05b „методът на плащане е удобство, лицензът е защитата". ✓
- Layout (per Step-8 width formula, Cyrillic × 0.62): viewBox 0 0 720 400; every `<text>` sits inside a ≥16px inner padding (all left ≥ 118, all right ≤ 648 within the 704 safe edge); two timeline cards do not overlap (left ends x=340, right starts x=380); two info bars and two footer lines stacked with clear vertical gaps; no character clips or touches an edge.
- Hygiene: no operator logos/names/UI, no fake screenshot; no people/faces; no glamorised winning; carries „18+ Играйте отговорно". „SEPA" / „НАП" / „Revolut"-style brand terms: only SEPA (a payment scheme) and НАП (the regulator) appear as plain text, no operator brand.
- Well-formed XML (parsed OK); 0 em-dashes; `<title>` + aria-label with a specific Bulgarian description.

## Decision — KEEP (manual PASS, Gemini review skipped 402)
No integrity failures, no layout defects. Ship in the content PR. images: 1 (infographic, manual integrity PASS).
