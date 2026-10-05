# 06-VERIFICATION — Всички Казина · 2026-09-30-depozit-s-bankova-karta
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Депозит с банкова карта (Visa/Mastercard) в онлайн казино: такси, срокове и сигурност** · type: guide (метод-ниво, evergreen) · byline: persona (Георги Тодоров) · gate: PASS WITH FIXES 92/100 (criticals 0) · humanisation: HUMAN-LIKE · Gemini Step-7: SKIPPED (HTTP 402) · images: 1 (infographic, manual integrity PASS) · run date: 30.09.2026

## Surviving [VERIFY] flags (still in the text)
**1** in-text [VERIFY] — кредитна карта cash advance: точното третиране на депозита като „теглене на пари в брой" и тарифата (порядък 3–5% + лихва от първия ден) зависят от конкретната банка и карта. Не може да се потвърди генерично за всяка българска банка/издател → играчът да провери в тарифата или при издателя. Не [CONFLICT], не [DATA NEEDED]. Общо потвърждение за практиката: CFPB (издателите третират хазартни транзакции като cash advance), но конкретните % са банко-специфични и затова маркирани ПРИМЕРНИ + [VERIFY].

## Time-sensitive / general claims to confirm at publish (source URLs)
| Claim | Source to confirm | Note |
|---|---|---|
| Visa/Mastercard най-разпространен метод; **депозит моментален** | Gambling Insider (mastercard-casinos); VegasSlotsOnline (visa) | Web-verified, метод-ниво. |
| **3-D Secure** = Verified by Visa / Mastercard Identity Check (код в приложение/SMS) | марките на 3DS (Visa/Mastercard); Gambling Insider (3-D Secure при депозит) | Общо познание за 3DS марките. |
| Теглене по карта **1–5 работни дни**, зависи от банка/казино | Gambling Insider (Mastercard 3–7 раб. дни); rotowire/sportsline (Visa 24–72 ч) | Обобщено като „обикновено 1–5 работни дни" (примерни срокове); варира. |
| Първото теглене → **KYC**: лична карта/паспорт, адрес (≤ ~90 дни), снимка на картата с последни 4 цифри | CasinoBeats (KYC casino requirements); next.io (KYC & document verification) | Web-verified; законово изискване (AML). |
| Правило **„до размера на депозита"** по карта; печалбата отгоре по друг метод | Gambling Insider (withdraw up to deposit) | Web-verified, метод-ниво. |
| Кредитна карта → **cash advance** (такса + лихва от първия ден) | CFPB Data Spotlight (gambling → cash advance); WalletHub (cash advance ~3–5% + immediate interest) | Практиката потвърдена; конкретни % банко-специфични → [VERIFY]. |
| Оператор пази данните по **PCI DSS / токенизация** | Wikipedia PCI DSS | Web-verified, метод-ниво. |

### Sources (cited in 00-brief; web-verified 30.09.2026)
1. CFPB — Data Spotlight: cash advance fees spike after legalization of sports gambling: https://www.consumerfinance.gov/data-research/research-reports/data-spotlight-credit-card-cash-advance-fees-spike-after-legalization-of-sports-gambling/
2. CasinoBeats — Guide to KYC casino requirements: https://casinobeats.com/features/guide-to-kyc-casino-requirements/
3. Gambling Insider — Mastercard casinos (instant deposit, withdrawal times, up-to-deposit rule): https://www.gamblinginsider.com/us/mastercard-casinos
4. Wikipedia — Payment Card Industry Data Security Standard: https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard

## Illustrative numbers used (all labelled „примерен" in text)
| Where | Figure | Note |
|---|---|---|
| Валутно конвертиране | €200 × 2% = €4 | примерна такса от банка при карта в друга валута/презгранично |
| „Същата карта" | €200 депозит / €500 теглене → ~€200 обратно / ~€300 по втори метод | примерен, за илюстрация на правилото |
| Cash advance | 3–5% + лихва от първия ден | примерен, зависи от банката/картата → [VERIFY] |
| Срок теглене | 1–5 работни дни | примерни срокове, зависят от банка/казино |

## Recalculation shown (per Step-6 requirement)
- Валутно конвертиране: 0,02 × €200 = **€4**. ✓ съвпада с текста (изрично примерно). Работа: 2/100 × 200 = 4.
- „Същата карта": депозит €200, теглене €500 → до размера на депозита по карта = **€200**; остатък €500 − €200 = **€300** по втори метод. ✓ съвпада с текста (примерно).

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-body + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 август 2026 / ДВ бр. 69), pending-application, БЕЗ issued-licence claim, БЕЗ измислен №. ✓
- Internal links: само verified-live набора (/blog/casino-payments/, /depoziti-i-teglenia/, /blog/evro-hazart-depoziti/, /otgovorna-igra/), 4 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" коректно. ✓
- Метод-guide, без конкретен оператор → без Протокол (няма разписки), без НАП №, без афилиейт линк. ✓
- Zero em-dashes (вкл. meta). En-dash само в числови диапазони и верб. footer „10:00–17:00". Без промис/хайп. Tax не се засяга. ✓

## SVG number-diff (05b ↔ инфографика)
- „моментален" (депозит) — 05b ✓ / SVG ✓
- „1–5 работни дни" — 05b ✓ / SVG ✓
- „Първото теглене изисква KYC верификация" — 05b ✓ / SVG ✓
- „примерни срокове" — 05b caption ✓ / SVG ✓
- „18+ Играйте отговорно" — SVG ✓
Всяко число/твърдение в инфографиката се проследява до 05b. Без операторски лога/имена, без хора/лица, без глорификация на печалба.

## External check (Step 7 — Gemini cross-model)
external check: skipped (Gemini unavailable, HTTP 402)
images: 1 (infographic, manual integrity PASS; Gemini review skipped 402)

## Human-action list (owned by you, Step 6 / publish)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve/keep the in-text [VERIFY]: cash advance третиране + тарифа при кредитна карта (банко/карта-специфично) — потвърди генеричната формулировка или добави конкретика при публикуване.
3. Confirm current typical card-withdrawal windows at publish (варира по банка/казино; текстът е хеджиран „обикновено 1–5 работни дни").
4. Confirm the site's affiliate-licence status at publish (footer казва подадено/очаква — никога „издаден").
