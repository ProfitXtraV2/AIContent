# LOG — vk-0228 · Revolut в онлайн казино (2026-10-01)

slug: 2026-10-01-revolut-kazino · brand: vsichkikazina · market: bg · content type: guide (метод-ниво, evergreen) · byline: persona (Георги Тодоров)

- brief   — 00-brief.md попълнен. Метод-ниво guide, БЕЗ конкретен оператор/НАП №/Протокол. 3 web източника (help.revolut.com, casinos.org, revolut.com well-being). Линкове: /blog/casino-payments/, /mobilni-kazina/, /depoziti-i-teglenia/, /otgovorna-igra/.
- research — WebSearch: блокировка на хазарта (включване веднага; изключване до 48ч cooling-off; поддръжката не го заобикаля; MCC-базирано; не блокира банкови преводи / скрит MCC); депозит моментален; повечето тегления до 24ч; 0% такси от Revolut при казино плащания; конвертиране извън лимити/уикенд; възможно BIN блокиране.
- 1       — 01-synthesis.md: теза (платежен метод + уникален RG инструмент; контролът > скоростта) + constants; 0 blocking, 1 [VERIFY] (такси конвертиране план/ден-специфични).
- 1.5     — 01.5-outline.md: H1 + 7 секции; hero ПРОПУСНАТ (API 402); SVG за блокировката (веднага/48ч).
- 2       — 02-draft.md: persona проза ~1056 думи; PRE-humanized; 4 линка; без Протокол; блокировката = положителен инструмент (без насърчаване за изключване).
- 3       — 03-humanised.md: HUMAN-LIKE; solidarity RG тон; асиметричен край; NUMBER DIFF 02→03 identical.
- 4       — 04-seo.md: title ~48/meta <160, 0 em-dash; 4 whitelisted линка; NUMBER DIFF 03→04 identical.
- 5       — 05-gate-report.md: PASS WITH FIXES 95/100, criticals 0; RG 15/15; няма деривирани изчисления; NUMBER DIFF 04→05→05b identical.
- 5b      — 05b-final-draft.md: ~1056 думи; 0 em-dash; 0 таблици/булети; SVG референция + caption; 4 whitelisted линка.

## Step 6/7/8
- Step 6: 06-verification.md (1 in-text [VERIFY] такси конвертиране; general-claim confirm-list със source URLs; untouchables spot-check; SVG claim-diff 05b↔инфографика). external check: skipped (Gemini unavailable, HTTP 402). images: 1 (infographic, manual integrity PASS; Gemini review skipped 402).
- Step 7 (Gemini): GEMINI_UNAVAILABLE — HTTP 402 (re-probed live). Step-7 skipped; single draft kept; gemini=skipped. 07-gemini-check-1.md persisted.
- Step 8 (images): 1 SVG инфографика (revolut-blokirovka-hazart.svg) — hand-authored; всяко твърдение трасира до 05b; well-formed, no overlaps/clipping; title em-dash fixed; без лога/UI/хора/глориф. печалба; 18+/RG note. Gemini image review skipped (402); manual integrity PASS. 08-image-review-1.md persisted.
- Status → drafted. drafted_date 01.10.2026. Human owns Step 6/publish.

FINAL GREP-VERIFICATION (05b + SVG)
- em-dashes (—): 0 в 05b и в SVG (title поправен). En-dash „–": footer „10:00–17:00".
- верб. „18+ Хазартът може да пристрасти. Играйте отговорно." body RG touch + footer RG блок + /otgovorna-igra/ + регистър на уязвимите лица + „Солидарност" 0888 99 18 66: да.
- affiliate disclosure (1 август 2026 / ДВ бр. 69): верб. present. Нула site-licence „issued"; нула измислен №.
- byline Георги Тодоров + Публикувано 01.10.2026; brand „Всички Казина" коректно.
- internal links (4, whitelisted): /blog/casino-payments/ · /mobilni-kazina/ · /depoziti-i-teglenia/ · /otgovorna-igra/. Без конкретен оператор → без афилиейт линк.
- flags in text: 1 [VERIFY] (такси конвертиране); 0 CONFLICT/DATA NEEDED.
- key numbers: до 24 часа (теглене); до 48 часа (cooling-off). RG доктрина силно присъства.
- Протокол на тегленето: правилно ОТСЪСТВА.
