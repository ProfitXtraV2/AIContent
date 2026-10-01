# LOG — vk-0230 · Trustly / open banking в онлайн казино (2026-10-01, 2nd fire)

slug: 2026-10-01-trustly-open-banking-kazino · brand: vsichkikazina · market: bg · content type: guide (метод-ниво, evergreen) · byline: persona (Георги Тодоров)

- brief   — 00-brief.md попълнен. Метод-ниво guide (open banking / pay-by-bank), БЕЗ конкретен оператор/НАП №/Протокол. Trustly = име на метода/доставчика (plain text). 3 web източника (trustly.com/gaming, casinobeats open banking, wizardofodds/casino.guru Pay N Play). Линкове: /blog/casino-payments/, /blog/evro-hazart-depoziti/, /depoziti-i-teglenia/, /otgovorna-igra/.
- research — WebSearch/WebFetch: open banking = плащане от сметката през банкова автентикация, казиното не вижда картови данни; мигновено в двете посоки, теглене често за минути; Pay N Play без отделна регистрация/портфейл, вградена верификация (KYC остава); Trustly свързан с над 3000 банки в Европа; такси обикновено за оператора/доставчика.
- 1       — 01-synthesis.md: теза (open banking = скоростта на моментален превод от сметка към сметка + без споделяне на картови данни; голямата разлика спрямо бавния класически превод); constants + 3 [VERIFY] (BG банки / BG казина / такси).
- 1.5     — 01.5-outline.md: H1 + 7 секции; hero ПРОПУСНАТ (API 402); SVG контраст Trustly vs класически превод + какво не вижда казиното + наличност.
- 2       — 02-draft.md: persona проза ~1025 думи; PRE-humanized; 4 линка; без Протокол; изрично разграничение от vk-0229.
- 3       — 03-humanised.md: HUMAN-LIKE; асиметричен край (силата конкретна / ограничението конкретно); NUMBER DIFF 02→03 identical.
- 4       — 04-seo.md: title 46 знака / meta 149 знака, 0 em-dash; 4 whitelisted линка; NUMBER DIFF 03→04 identical.
- 5       — 05-gate-report.md: PASS 93/100, criticals 0; Trust 15/15, RG 15/15; NUMBER DIFF 04→05→05b identical.
- 5b      — 05b-final-draft.md: ~1025 думи; 0 em-dash; 0 таблици/булети; SVG референция + caption; 4 whitelisted линка.

## Step 6/7/8
- Step 6: 06-verification.md (3 in-text [VERIFY] BG-наличност/такси; general-claim confirm-list със source URLs; untouchables spot-check; SVG claim-diff 05b↔инфографика). external check: skipped (Gemini unavailable, HTTP 402). images: 1 (infographic, manual integrity PASS; Gemini review skipped 402).
- Step 7 (Gemini): GEMINI_UNAVAILABLE — HTTP 402 (re-probed live 2nd fire). Step-7 skipped; single draft kept; gemini=skipped. 07-gemini-check-1.md persisted.
- Step 8 (images): 1 SVG инфографика (trustly-open-banking.svg) — hand-authored; всяко твърдение трасира до 05b (3000-банки числото НЕ е сложено заради [VERIFY] caveat); well-formed XML, width-checked (0 overlaps/clips); без лога/UI/хора/глориф.; 18+/RG note. Gemini image review skipped (402); manual integrity PASS. 08-image-review-1.md persisted.
- Status → drafted. drafted_date 01.10.2026. Human owns Step 6/publish.

FINAL GREP-VERIFICATION (05b + SVG)
- em-dashes (—): 0 в 05b и в SVG. En-dash „–": footer „10:00–17:00".
- верб. „18+ Хазартът може да пристрасти. Играйте отговорно." body RG touch + footer RG блок + /otgovorna-igra/ + регистър на уязвимите лица + „Солидарност" 0888 99 18 66: да.
- affiliate disclosure (1 август 2026 / ДВ бр. 69): верб. present. Нула site-licence „issued"; нула измислен №.
- byline Георги Тодоров + Публикувано 01.10.2026; brand „Всички Казина" коректно.
- internal links (4, whitelisted): /blog/casino-payments/ · /blog/evro-hazart-depoziti/ · /depoziti-i-teglenia/ · /otgovorna-igra/. Trustly=метод (plain text) → без афилиейт линк.
- flags in text: 3 [VERIFY] (BG банки / BG казина / такси); 0 CONFLICT/DATA NEEDED.
- key claims: мигновено в двете посоки; теглене за минути/същата сесия; vs няколко работни дни при обикновения превод; казиното не вижда картови данни; вградена верификация (KYC остава). RG доктрина присъства.
- Протокол на тегленето: правилно ОТСЪСТВА.
