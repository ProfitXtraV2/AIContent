# 06-VERIFICATION — Всички Казина · 2026-10-01-bankov-prevod-kazino
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Банков превод в онлайн казино: срокове, лимити и такси** · type: guide (метод-ниво, evergreen) · byline: persona (Георги Тодоров) · gate: PASS WITH FIXES 93/100 (criticals 0) · humanisation: HUMAN-LIKE · Gemini Step-7: SKIPPED (HTTP 402) · images: 1 (infographic, manual integrity PASS) · run date: 01.10.2026 (2nd fire)

## Surviving [VERIFY] flags (still in the text)
**1** in-text [VERIFY] — точната такса за изходящ превод зависи от тарифния план на конкретната банка → играчът/редакторът да потвърди в тарифата на банката. Не [CONFLICT], не [DATA NEEDED].

## Time-sensitive / general claims to confirm at publish (source URLs)
| Claim | Source to confirm | Note |
|---|---|---|
| SEPA превод в евро обикновено **~1 работен ден**; **SEPA Instant** за секунди 24/7 | skydo.com (SEPA explainer) | Web-verified, метод-ниво; срок хеджиран („обикновено"). |
| SEPA покрива **над 40 държави**, само в **евро** | skydo.com | Web-verified (~41 държави). |
| **Цялата обиколка** (одобрение на казиното + превод + осчетоводяване) = **няколко работни дни** в двете посоки | tothebrain.com (withdrawal times) | Web-verified, метод-ниво; примерен сбор, хеджиран. |
| Казиното обикновено **не таксува** банков превод; **банката** може да начисли за изходящ превод | tothebrain.com; general SEPA pricing | Web-verified; конкретиката план-специфична → [VERIFY]. |
| **Високи лимити** (до десетки хиляди €, примерни); **по-висок минимум** (примерно €20 срещу €5/€10) | tothebrain.com | Web-verified посока; точните прагове са оператор/банка-специфични → маркирани примерни. |
| **Правило за същата сметка** (AML); допълнителна проверка на произхода при големи/презгранични суми | AML general practice | Общо правило, метод-ниво. |
| KYC при първо теглене | метод-ниво (AML) | Общо правило. |

### Sources (cited in 00-brief; web-verified 01.10.2026)
1. skydo.com — SEPA credit transfer (standard ~1 banking business day; SEPA Instant within ~10s 24/7; euro-only; ~41 countries; priced like a domestic transfer, often free): https://www.skydo.com/blog/what-is-sepa-payment
2. tothebrain.com — Casino withdrawal times by method (bank transfer: high limits, higher minimums, 1–3 business days after approval, AML checks on large/cross-border sums): https://tothebrain.com/casino-withdrawal-times/

## Illustrative numbers used (labelled примерни / hedged)
| Where | Figure | Note |
|---|---|---|
| Самият превод | ≈ 1 работен ден | web-verified (SEPA standard); „обикновено" |
| Цялата обиколка | няколко работни дни | примерен сбор, зависи от казино/банка |
| Лимити | до десетки хиляди евро на превод | изрично „примерни суми" в текста |
| Минимален депозит | примерно €20 срещу €5 или €10 | изрично „примерни прагове" в текста |
| Такси на банката | зависят от тарифния план | примерни → [VERIFY] |

## Recalculation shown (per Step-6 requirement)
- Няма деривирани изчисления (качествен метод-guide; без превъртане/бонус-математика). Нищо за
  преизчисляване. Единствената числова конкретика (срокове/прагове) е или web-verified, или изрично
  примерна, или [VERIFY] (банкова тарифа).

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-body + footer). ✓ (2×)
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 август 2026 / ДВ бр. 69), pending-application, БЕЗ issued-licence claim, БЕЗ измислен №. ✓
- Internal links: само verified-live (/blog/casino-payments/, /blog/evro-hazart-depoziti/, /depoziti-i-teglenia/, /otgovorna-igra/), 4 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" коректно. ✓
- Метод-guide, без конкретен оператор → без Протокол, без НАП №, без афилиейт линк. ✓
- Zero em-dashes (вкл. meta и SVG). En-dash само в „10:00–17:00". Без промис/хайп. Данъчна тема не се засяга. ✓

## SVG number-diff (05b ↔ инфографика)
- „≈ 1 работен ден" (самият превод) — 05b ✓ / SVG ✓
- „няколко работни дни · в двете посоки" — 05b ✓ / SVG ✓
- „секунди само при SEPA Instant (24/7)" — 05b ✓ / SVG ✓
- „казиното обикновено не начислява · банката може да вземе такса по тарифата си" — 05b ✓ / SVG ✓
- „до десетки хиляди евро на превод (примерни)" — 05b ✓ / SVG ✓
- „примерно €20 вместо €5 или €10 при картите (примерни)" — 05b ✓ / SVG ✓
- „Тегленето се връща по сметката, от която е дошъл депозитът" — 05b ✓ / SVG ✓
Всяко твърдение/число в инфографиката се проследява до 05b. Без операторски лога/имена, без хора/лица, без глорификация на печалба.

## External check (Step 7 — Gemini cross-model)
external check: skipped (Gemini unavailable, HTTP 402)
images: 1 (infographic, manual integrity PASS; Gemini review skipped 402)

## Human-action list (owned by you, Step 6 / publish)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve/keep the in-text [VERIFY]: точната такса за изходящ превод (тарифен план на банката) — потвърди при публикуване.
3. Confirm the site's affiliate-licence status at publish (footer казва подадено/очаква — никога „издаден").
