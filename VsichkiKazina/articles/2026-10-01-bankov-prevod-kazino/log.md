# LOG — vk-0229 · Банков превод в онлайн казино (2026-10-01, 2nd fire)

slug: 2026-10-01-bankov-prevod-kazino · brand: vsichkikazina · market: bg · content type: guide (метод-ниво, evergreen) · byline: persona (Георги Тодоров)

- brief   — 00-brief.md попълнен. Метод-ниво guide, БЕЗ конкретен оператор/НАП №/Протокол. 2 web източника (skydo.com SEPA, tothebrain.com withdrawal times). Линкове: /blog/casino-payments/, /blog/evro-hazart-depoziti/, /depoziti-i-teglenia/, /otgovorna-igra/.
- research — WebSearch/WebFetch: SEPA превод в евро ~1 работен ден, SEPA Instant секунди 24/7, само евро, над 40 държави; казиното обикновено не таксува, банката може за изходящ превод; високи лимити / по-висок минимум; теглене по същата сметка (AML); KYC при първо теглене.
- 1       — 01-synthesis.md: теза (най-бавният разпространен метод, но високи лимити + чиста банкова следа; скоростта е цената); constants + 1 [VERIFY] (банкова тарифа).
- 1.5     — 01.5-outline.md: H1 + 7 секции; hero ПРОПУСНАТ (API 402); SVG за сроковете/таксите/лимитите.
- 2       — 02-draft.md: persona проза ~1047 думи; PRE-humanized; 4 линка; без Протокол.
- 3       — 03-humanised.md: HUMAN-LIKE; сведен повтарящ се „не след него" до единична употреба; асиметричен край; NUMBER DIFF 02→03 identical.
- 4       — 04-seo.md: title 46 знака / meta 159 знака, 0 em-dash; 4 whitelisted линка; NUMBER DIFF 03→04 identical.
- 5       — 05-gate-report.md: PASS WITH FIXES 93/100, criticals 0; няма деривирани изчисления; NUMBER DIFF 04→05→05b identical.
- 5b      — 05b-final-draft.md: ~1047 думи; 0 em-dash; 0 таблици/булети; SVG референция + caption; 4 whitelisted линка.

## Step 6/7/8
- Step 6: 06-verification.md (1 in-text [VERIFY] банкова тарифа; general-claim confirm-list със source URLs; untouchables spot-check; SVG claim-diff 05b↔инфографика). external check: skipped (Gemini unavailable, HTTP 402). images: 1 (infographic, manual integrity PASS; Gemini review skipped 402).
- Step 7 (Gemini): GEMINI_UNAVAILABLE — HTTP 402 (re-probed live 2nd fire). Step-7 skipped; single draft kept; gemini=skipped. 07-gemini-check-1.md persisted.
- Step 8 (images): 1 SVG инфографика (bankov-prevod-srokove.svg) — hand-authored; всяко твърдение трасира до 05b; well-formed XML, width-checked (0 overlaps/clips); без лога/UI/хора/глориф. печалба; 18+/RG note. Gemini image review skipped (402); manual integrity PASS. 08-image-review-1.md persisted.
- Status → drafted. drafted_date 01.10.2026. Human owns Step 6/publish.

FINAL GREP-VERIFICATION (05b + SVG)
- em-dashes (—): 0 в 05b и в SVG. En-dash „–": footer „10:00–17:00".
- верб. „18+ Хазартът може да пристрасти. Играйте отговорно." body RG touch + footer RG блок + /otgovorna-igra/ + регистър на уязвимите лица + „Солидарност" 0888 99 18 66: да.
- affiliate disclosure (1 август 2026 / ДВ бр. 69): верб. present. Нула site-licence „issued"; нула измислен №.
- byline Георги Тодоров + Публикувано 01.10.2026; brand „Всички Казина" коректно.
- internal links (4, whitelisted): /blog/casino-payments/ · /blog/evro-hazart-depoziti/ · /depoziti-i-teglenia/ · /otgovorna-igra/. Без конкретен оператор → без афилиейт линк.
- flags in text: 1 [VERIFY] (банкова тарифа); 0 CONFLICT/DATA NEEDED.
- key numbers: ≈1 работен ден (превод); няколко работни дни (обиколка); €20/€5/€10 (примерни); десетки хиляди евро (примерни). RG доктрина присъства.
- Протокол на тегленето: правилно ОТСЪСТВА.
