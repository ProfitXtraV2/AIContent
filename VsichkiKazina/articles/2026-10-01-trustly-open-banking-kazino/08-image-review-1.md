# Image Review Pass 1 — 2026-10-01-trustly-open-banking-kazino

## Images reviewed
- images/trustly-open-banking.svg (hand-authored infographic)

## Verdict
GEMINI_UNAVAILABLE — HTTP 402; image review skipped. Manual integrity check: PASS — every claim traces to 05b; no operator logos/names; no people/faces; no glamorised winning; no fabricated figures.

## Manual integrity detail
- Claims vs 05b (each traces):
  - „Trustly / open banking · мигновено в двете посоки" ← 05b „при Trustly парите се движат мигновено в двете посоки". ✓
  - „тегленето често за минути в същата сесия" ← 05b „парите често се получават за минути, понякога в рамките на същата сесия". ✓
  - „Класически банков превод · няколко работни дни · ръчно нареждане по IBAN" ← 05b „класическия банков превод … няколко работни дни обиколка" + „При Trustly няма преписване на IBAN … няма ръчно нареждане" (contrast). ✓
  - „Казиното не вижда картови данни, вход или реквизити на сметката" ← 05b „Казиното в нито един момент не вижда номера на картата ти, данните за вход или пълните реквизити на сметката". ✓
  - „верификацията често е вградена (KYC остава)" ← 05b „Верификацията често е вградена … Това не отменя KYC". ✓
  - „Наличността зависи от банката и казиното; в България е ограничена" ← 05b „твоята банка трябва да е свързана с Trustly и конкретното казино трябва … да предлага метода … В България наличността е ограничена". ✓
  - „Trustly е удобство, лицензът от НАП е защитата" ← 05b „Trustly е удобство, лицензът е защитата". ✓
- Deliberately NOT placed on the graphic: the „над 3 000 банки" scale figure (it carries a [VERIFY] caveat for the BG market in 05b) — kept in prose only, not emphasised in the image.
- Layout (Step-8 width formula, Cyrillic × 0.62): viewBox 0 0 720 372; every `<text>` inside ≥16px padding (all left ≥ 49, all right ≤ 642 within the 704 safe edge); two contrast cards do not overlap (left ends x=340, right starts x=380); two info bars + footer stacked with clear gaps; no clip/overlap/edge-touch.
- Hygiene: Trustly appears only as the plain-text method/provider name (no logo/UI/screenshot); IBAN/KYC/НАП are generic terms; no operator brand; no people/faces; no glamorised winning; carries „18+ Играйте отговорно".
- Well-formed XML (parsed OK); 0 em-dashes; `<title>` + aria-label with a specific Bulgarian description.

## Decision — KEEP (manual PASS, Gemini review skipped 402)
No integrity failures, no layout defects. Ship in the content PR. images: 1 (infographic, manual integrity PASS).
