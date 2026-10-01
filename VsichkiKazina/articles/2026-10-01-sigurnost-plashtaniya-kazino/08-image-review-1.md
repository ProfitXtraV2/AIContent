# Image Review Pass 1 — 2026-10-01-sigurnost-plashtaniya-kazino

## Images reviewed
- images/sigurnost-sloeve-plashtaniya.svg (hand-authored infographic — layered-security diagram)

## Verdict
GEMINI_UNAVAILABLE — HTTP 402; image review skipped. Manual integrity check: PASS — every claim traces to 05b; no operator logos/names; no people/faces; no glamorised winning; no fabricated figures.

## Manual integrity detail
- Claims vs 05b (each traces):
  - НАП banner „Лиценз от НАП: първата проверка, преди всичко останало · пази правата ти; техническите слоеве пазят само транзакцията" ← 05b „проверката на лиценза от НАП … стои преди всичко останало" + „Техническите слоеве пазят транзакцията; лицензът пази правата ти". ✓
  - Layer 1 „SSL/TLS: криптирана връзка (https) · пази данните по пътя, не гарантира честен оператор" ← 05b „връзката … криптирана по протокола TLS (наследник на по-стария SSL …)" + „То не гарантира, че от другата страна стои честен оператор". ✓
  - Layer 2 „PCI DSS: правила за картовите данни · по цялата верига: оператор плюс платежен доставчик" ← 05b „PCI DSS е стандартът, по който всеки, който … картови данни, е длъжен да работи" + „работи с платежен доставчик, който носи сертификацията". ✓
  - Layer 3 „3-D Secure / SCA: второ потвърждение от банката · поне два независими фактора от три категории" ← 05b „банката ти иска второ потвърждение" + „поне два независими фактора от три възможни категории" (verbatim). ✓
  - Layer 4 „Токенизация: казиното пази токен, не номера · истинският номер стои при платежния доставчик" ← 05b „казиното вижда и пази само токена" + „Истинският номер стои в защитено хранилище при платежния доставчик". ✓
  - Footer „сигурността пази транзакцията, лицензът пази правата ти" ← 05b verdict verbatim-equivalent. ✓
- Layout (Step-8 width formula, Cyrillic × 0.62): viewBox 0 0 720 438; every `<text>` inside ≥16px padding (all left ≥ 103, all right ≤ 617 within the 704 safe edge); НАП banner + 4 layer bars stacked vertically with 6px gaps, no overlap; no clip/edge-touch. НАП banner emphasised (2px emerald stroke) to signal „first/above"; layers tinted blue→violet downward.
- Hygiene: SSL/TLS/PCI DSS/3-D Secure/SCA/токенизация/НАП are generic standards/regulator in plain text; no operator brand/logo/UI/screenshot; no people/faces; no glamorised winning; carries „18+ Играйте отговорно".
- Well-formed XML (parsed OK); 0 em-dashes; `<title>` + aria-label with a specific Bulgarian description.

## Decision — KEEP (manual PASS, Gemini review skipped 402)
No integrity failures, no layout defects. Ship in the content PR. images: 1 (infographic, manual integrity PASS).
