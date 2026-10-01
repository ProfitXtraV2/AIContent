# LOG — vk-0231 · Сигурност на онлайн плащанията в казино (2026-10-01, 2nd fire)

slug: 2026-10-01-sigurnost-plashtaniya-kazino · brand: vsichkikazina · market: bg · content type: guide (concept/security pillar, informational, evergreen) · byline: persona (Георги Тодоров)

- brief   — 00-brief.md попълнен. Концептуален/security pillar; БЕЗ конкретен оператор/сертификат/НАП №/Протокол. Стандартите (SSL/TLS, PCI DSS, 3-D Secure/SCA, токенизация) = generic (plain text). 5 web източника (pcisecuritystandards.org, emvco.com, checkout.com, worldpay/squareup, dnsfilter/certera). Линкове: /blog/casino-payments/, /depoziti-i-teglenia/, /zakonno-li-e/, /otgovorna-igra/.
- research — WebSearch/WebFetch: SSL/TLS = криптирана връзка, катинарчето не доказва честност; PCI DSS = стандарт за картови данни от схемите + независим съвет; 3-D Secure/SCA = второ потвърждение, 2 от 3 фактора, задължително в ЕС; токенизация = реален номер -> токен без връзка, merchant-specific, номерът при доставчика.
- 1       — 01-synthesis.md: теза (четири слоя пазят транзакцията, но лицензът от НАП пази правата; слоевете са хигиена, не гаранция за честна игра); 0 blocking, 0 [VERIFY] (всичко качествено).
- 1.5     — 01.5-outline.md: H1 + 7 секции (катинарче / PCI DSS / 3-D Secure / токенизация / хигиена-не-гаранция / как проверяваш сам / къде е истинската защита); hero ПРОПУСНАТ (API 402); 1 SVG layered-security диаграма (pure-concept pillar -> 1 explanatory diagram).
- 2       — 02-draft.md: persona проза ~1033 думи; PRE-humanized; 4 линка; без Протокол; licence-first силно.
- 3       — 03-humanised.md: HUMAN-LIKE; асиметричен verdict (сигурността хигиена / лицензът пази правата); NUMBER DIFF 02→03 identical.
- 4       — 04-seo.md: title 54 знака / meta 138 знака, 0 em-dash; 4 whitelisted линка; NUMBER DIFF 03→04 identical.
- 5       — 05-gate-report.md: PASS WITH FIXES 92/100, criticals 0 (RG 15/15); единствен mechanical fix = вмъкване на verbatim footer блокове; NUMBER DIFF 04→05→05b identical.
- 5b      — 05b-final-draft.md: ~1033 думи; 0 em-dash; 0 таблици/булети (слоевете в проза, не spec-таблица); SVG референция + caption; 4 whitelisted линка.

## Step 6/7/8
- Step 6: 06-verification.md (0 in-text [VERIFY]; general-claim confirm-list със source URLs; untouchables spot-check; SVG claim-diff 05b↔инфографика; anti-cannibal altitude note). external check: skipped (Gemini unavailable, HTTP 402). images: 1 (infographic, manual integrity PASS; Gemini review skipped 402).
- Step 7 (Gemini): GEMINI_UNAVAILABLE — HTTP 402 (re-probed live 2nd fire). Step-7 skipped; single draft kept; gemini=skipped. 07-gemini-check-1.md persisted.
- Step 8 (images): 1 SVG инфографика (sigurnost-sloeve-plashtaniya.svg) — hand-authored layered-security диаграма (НАП banner над 4 слоя); всяко твърдение трасира до 05b; well-formed XML, width-checked (0 overlaps/clips); без лога/UI/хора/глориф.; 18+/RG note. Gemini image review skipped (402); manual integrity PASS. 08-image-review-1.md persisted.
- Status → drafted. drafted_date 01.10.2026. Human owns Step 6/publish.

FINAL GREP-VERIFICATION (05b + SVG)
- em-dashes (—): 0 в 05b и в SVG. En-dash „–": footer „10:00–17:00".
- верб. „18+ Хазартът може да пристрасти. Играйте отговорно." body RG touch + footer RG блок + /otgovorna-igra/ + регистър на уязвимите лица + „Солидарност" 0888 99 18 66: да.
- affiliate disclosure (1 август 2026 / ДВ бр. 69): верб. present. Нула site-licence „issued"; нула измислен №/сертификат.
- byline Георги Тодоров + Публикувано 01.10.2026; brand „Всички Казина" коректно.
- internal links (4, whitelisted): /blog/casino-payments/ · /depoziti-i-teglenia/ · /zakonno-li-e/ · /otgovorna-igra/. Без конкретен оператор → без афилиейт линк.
- flags in text: 0 [VERIFY]; 0 CONFLICT/DATA NEEDED.
- key concepts: 4 слоя (SSL/TLS, PCI DSS, 3-D Secure/SCA 2-от-3, токенизация) + лиценз от НАП първи. Licence-first доктрина доминира. RG присъства.
- Протокол на тегленето: правилно ОТСЪСТВА.
