# LOG — vk-0224 · Депозит с банкова карта (Visa/Mastercard) в онлайн казино (2026-09-30)

slug: 2026-09-30-depozit-s-bankova-karta · brand: vsichkikazina · market: bg · content type: guide (метод-ниво, evergreen) · byline: persona (Георги Тодоров)

- brief   — 00-brief.md попълнен. Метод-ниво guide, БЕЗ конкретен оператор/НАП №/Протокол. 4 web источника (CFPB, CasinoBeats, Gambling Insider, Wikipedia PCI DSS). Планирани линкове: /blog/casino-payments/, /depoziti-i-teglenia/, /blog/evro-hazart-depoziti/, /otgovorna-igra/.
- research — WebSearch: депозит с карта моментален; 3-D Secure (Verified by Visa / Mastercard Identity Check); теглене 1–5 раб. дни; KYC при първо теглене (лична карта/адрес/снимка на карта); правило „до размера на депозита"; казиното не таксува, банката таксува (конвертиране/презгранично/cash advance); PCI DSS/токенизация.
- 1       — 01-synthesis.md: seed теза + verified constants; 0 blocking, 1 [VERIFY] (cash advance банко-специфично).
- 1.5     — 01.5-outline.md: H1 + 8 секции, варирани форми; hero ПРОПУСНАТ (API офлайн), SVG при сроковете; anti-tell watch.
- 2       — 02-draft.md: persona проза ~1050 думи; PRE-humanized; number set locked; no CANON ADDITIONS; без Протокол.
- 3       — 03-humanised.md: MIXED→HUMAN-LIKE; намален „…, не Y" ender; NUMBER DIFF 02→03 identical.
- 4       — 04-seo.md: title 51/meta <160, 0 em-dash; keywords естествено; 4 whitelisted линка; NUMBER DIFF 03→04 identical.
- 5       — 05-gate-report.md: PASS WITH FIXES 92/100, criticals 0; maths recalc OK (€200×2%=€4; €200/€500→€200/€300); NUMBER DIFF 04→05→05b identical.
- 5b      — 05b-final-draft.md: ~1047 думи; 0 em-dash в прозата; 0 таблици/булети; SVG референция + caption.

## Step 6/7/8
- Step 6: 06-verification.md (1 in-text [VERIFY] cash advance; general-claim confirm-list с source URLs; illustrative-number table; recalcs показани; untouchables spot-check; SVG number-diff 05b↔инфографика). external check: skipped (Gemini unavailable, HTTP 402). images: 1 (infographic, manual integrity PASS; Gemini review skipped 402).
- Step 7 (Gemini): GEMINI_UNAVAILABLE — HTTP 402. Step-7 skipped; single draft kept; gemini=skipped. 07-gemini-check-1.md persisted.
- Step 8 (images): 1 SVG инфографика (depozit-karta-srokove.svg) — hand-authored; всяко число трасира до 05b; well-formed, rendered-checked, без overlaps/clipping; без лога/имена/хора/глориф. печалба; 18+/RG note. Gemini image review skipped (402); manual integrity PASS. 08-image-review-1.md persisted.
- Status → drafted. drafted_date 30.09.2026. Human owns Step 6/publish (About slot, [VERIFY] cash advance, теглене-срокове refresh, affiliate-licence status).

FINAL GREP-VERIFICATION (05b)
- em-dashes (—): 0 в прозата и meta. En-dash „–": числови диапазони (1–5, 3–5%), footer „10:00–17:00".
- верб. „18+ Хазартът може да пристрасти. Играйте отговорно." body RG touch + footer RG блок + /otgovorna-igra/ + регистър на уязвимите лица + „Солидарност" 0888 99 18 66: да.
- affiliate disclosure (1 август 2026 / ДВ бр. 69): верб. present. Нула site-licence „issued"; нула измислен №.
- byline Георги Тодоров + Публикувано 30.09.2026; brand „Всички Казина" коректно.
- internal links (4, whitelisted за тази статия): /blog/casino-payments/ · /depoziti-i-teglenia/ · /blog/evro-hazart-depoziti/ · /otgovorna-igra/. Без конкретен оператор → без афилиейт линк.
- flags in text: 1 [VERIFY] (cash advance третиране/тарифа); 0 CONFLICT/DATA NEEDED.
- key numbers: 1–5 работни дни; €200×2%=€4; €200/€500→€200/€300; 3–5% cash advance (примерни). Всички примерни маркирани.
- Протокол на тегленето: правилно ОТСЪСТВА (няма разписки).
