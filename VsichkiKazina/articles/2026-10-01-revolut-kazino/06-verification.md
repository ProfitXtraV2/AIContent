# 06-VERIFICATION — Всички Казина · 2026-10-01-revolut-kazino
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Revolut в онлайн казино: депозити, тегления и контрол на хазартните разходи** · type: guide (метод-ниво, evergreen) · byline: persona (Георги Тодоров) · gate: PASS WITH FIXES 95/100 (criticals 0) · humanisation: HUMAN-LIKE · Gemini Step-7: SKIPPED (HTTP 402) · images: 1 (infographic, manual integrity PASS) · run date: 01.10.2026

## Surviving [VERIFY] flags (still in the text)
**1** in-text [VERIFY] — точните такси за валутно конвертиране и безплатните лимити на Revolut са план/ден (делник-уикенд)-специфични и се менят → играчът/редакторът да потвърди в приложението/плана на Revolut. Не [CONFLICT], не [DATA NEEDED].

## Time-sensitive / general claims to confirm at publish (source URLs)
| Claim | Source to confirm | Note |
|---|---|---|
| Депозит **моментален**; повечето тегления **до 24 часа** | casinos.org (Revolut casinos) | Web-verified, метод-ниво; срок хеджиран. |
| При казино плащания Revolut обикновено **не таксува** (0%); **конвертиране** може да се начисли извън лимити/в уикенда | casinos.org; Revolut help | Web-verified; конкретика план/ден-специфична → [VERIFY]. |
| **Блокировка на хазарта:** включване веднага; **изключване до 48 часа** cooling-off; поддръжката не го заобикаля | help.revolut.com (gambling block) | Web-verified; централна RG функция. |
| Блокировката работи по **MCC**; спира казина/букмейкъри/бетинг приложения; **не** блокира банкови преводи / друг MCC | help.revolut.com | Web-verified; границите казани честно. |
| Възможно конкретно казино да **блокира Revolut BIN-ове** | casinos.org | Web-verified; „провери с поддръжката на казиното". |
| KYC при първо теглене | метод-ниво (AML) | Общо правило. |

### Sources (cited in 00-brief; web-verified 01.10.2026)
1. help.revolut.com — How does the gambling block work (enable instant; disable up to 48h cooling-off; support cannot bypass; MCC-based; doesn't block bank transfers / non-gambling MCC): https://help.revolut.com/en-US/help/profile-and-plan/security-and-personal-data/gambling-block/what-is-gambling-block/
2. casinos.org — Revolut casinos (0% Revolut fees on casino payments typically; conversion fee may apply; instant deposits; most cashouts within 24h; possible BIN block): https://casinos.org/payments/revolut/
3. revolut.com — Customer vulnerability / well-being (spending controls, freeze card, gambling block): https://www.revolut.com/en-US/customer-vulnerability/

## Illustrative numbers used (labelled примерни / hedged)
| Where | Figure | Note |
|---|---|---|
| Теглене | до 24 часа (повечето) | примерен, зависи от казино/метод |
| Блокировка cooling-off | до 48 часа | web-verified от Revolut help; „до" = горна граница |
| Такси конвертиране | зависят от плана/деня | примерни → [VERIFY] |

## Recalculation shown (per Step-6 requirement)
- Няма деривирани изчисления (качествен метод-guide). Нищо за преизчисляване; таксите се потвърждават
  срещу приложението на Revolut (виж [VERIFY]).

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-body + footer). ✓ (2×)
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Блокировката е представена като положителен инструмент; БЕЗ насърчаване за изключване; БЕЗ „как да се заобиколи". ✓
- Affiliate footer (1 август 2026 / ДВ бр. 69), pending-application, БЕЗ issued-licence claim, БЕЗ измислен №. ✓
- Internal links: само verified-live (/blog/casino-payments/, /mobilni-kazina/, /depoziti-i-teglenia/, /otgovorna-igra/), 4 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" коректно. ✓
- Метод-guide, без конкретен оператор → без Протокол, без НАП №, без афилиейт линк. ✓
- Zero em-dashes (вкл. meta и SVG). En-dash само в „10:00–17:00". Без промис/хайп. Данъчна тема не се засяга. ✓

## SVG number-diff (05b ↔ инфографика)
- „Включване веднага" — 05b ✓ / SVG ✓
- „Изключване до 48 часа (период на изчакване; поддръжката не го заобикаля)" — 05b ✓ / SVG ✓
- „Спира картови плащания към хазартни търговци (по MCC); не блокира банкови преводи" — 05b ✓ / SVG ✓
- „18+ Играйте отговорно · ... включи блокировката" — 05b ✓ / SVG ✓
Всяко твърдение/число в инфографиката се проследява до 05b. Без операторски лога/имена, без хора/лица, без глорификация на печалба. (Revolut е името на платежния метод, използвано като текст.)

## External check (Step 7 — Gemini cross-model)
external check: skipped (Gemini unavailable, HTTP 402)
images: 1 (infographic, manual integrity PASS; Gemini review skipped 402)

## Human-action list (owned by you, Step 6 / publish)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve/keep the in-text [VERIFY]: точните такси за конвертиране + безплатни лимити на Revolut (план/ден-специфични) — потвърди в приложението при публикуване.
3. Confirm the gambling-block cooling-off window at publish (текстът казва „до 48 часа" по Revolut help).
4. Confirm the site's affiliate-licence status at publish (footer казва подадено/очаква — никога „издаден").
