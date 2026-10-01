# 06-VERIFICATION — Всички Казина · 2026-10-01-trustly-open-banking-kazino
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Trustly и мигновените банкови плащания (open banking) в онлайн казино** · type: guide (метод-ниво, evergreen) · byline: persona (Георги Тодоров) · gate: PASS 93/100 (criticals 0) · humanisation: HUMAN-LIKE · Gemini Step-7: SKIPPED (HTTP 402) · images: 1 (infographic, manual integrity PASS) · run date: 01.10.2026 (2nd fire)

## Surviving [VERIFY] flags (still in the text)
**3** in-text [VERIFY] — всички свързани с BG-пазарна наличност/такси, които се менят и са оператор/доставчик-специфични (НЕ fabrication, НЕ [CONFLICT], НЕ [DATA NEEDED]):
1. [VERIFY: кои банки в България са свързани с Trustly]
2. [VERIFY: кои лицензирани в България казина предлагат Trustly]
3. [VERIFY: конкретните такси при плащане с Trustly зависят от оператора и доставчика]

## Time-sensitive / general claims to confirm at publish (source URLs)
| Claim | Source to confirm | Note |
|---|---|---|
| Open banking / pay-by-bank: плащане директно от сметката през силна банкова автентикация, казиното не вижда картови/вход данни | trustly.com (gaming); casinobeats (open banking) | Web-verified, метод-ниво. |
| **Мигновено в двете посоки**; тегленето често за минути / същата сесия | trustly.com; casino.guru / wizardofodds (Pay N Play) | Web-verified; „често" хеджирано. |
| **Pay N Play** = без отделна регистрация/портфейл; разпознаване по сметката; вградена верификация (KYC остава) | wizardofodds / casino.guru (Pay N Play) | Web-verified. |
| Trustly свързан с **над 3 000 банки в Европа** | trustly.com | Web-verified, консервативна долна граница („над"); BG-наличността е [VERIFY]. |
| Такси обикновено на страната на оператора/доставчика, не на играча | casinobeats; general open-banking pricing | Web-verified; конкретика → [VERIFY]. |
| KYC при първо теглене; вътрешна проверка на изходящите суми | метод-ниво (AML) | Общо правило. |

### Sources (cited in 00-brief; web-verified 01.10.2026)
1. trustly.com/us/gaming — Trustly Pay N Play / open banking for gaming (instant deposits and withdrawals; no card details shared; connects to thousands of European banks; built-in verification): https://www.trustly.com/us/gaming
2. casinobeats.com — open banking / pay-by-bank in iGaming (bank-authenticated, no card data to the operator, fees typically borne by the operator): https://www.casinobeats.com/
3. wizardofodds.com / casino.guru — Pay N Play mechanics (no separate registration; account-recognised; KYC pulled from the bank): https://wizardofodds.com/

## Illustrative / hedged figures used
| Where | Figure | Note |
|---|---|---|
| Теглене | често за минути / същата сесия | хеджирано „често"; web-verified посока |
| Мрежа | над 3 000 банки в Европа | консервативна долна граница; BG-наличност [VERIFY] |
| Такси за играча | обикновено няма | web-verified посока; конкретика [VERIFY] |

## Recalculation shown (per Step-6 requirement)
- Няма деривирани изчисления (качествен метод-guide; без превъртане/бонус-математика). Единствената
  числова конкретика („над 3 000 банки") е консервативна долна граница от доставчика, а BG-наличността
  е изрично [VERIFY].

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-body + footer). ✓ (2×)
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 август 2026 / ДВ бр. 69), pending-application, БЕЗ issued-licence claim, БЕЗ измислен №. ✓
- Internal links: само verified-live (/blog/casino-payments/, /blog/evro-hazart-depoziti/, /depoziti-i-teglenia/, /otgovorna-igra/), 4 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" коректно. Trustly = име на метода/доставчика (plain text), не оператор → без афилиейт линк, без НАП №, без Протокол. ✓
- Zero em-dashes (вкл. meta и SVG). En-dash само в „10:00–17:00". Без промис/хайп/FOMO. Данъчна тема не се засяга. ✓
- Ясно разграничение от класическия банков превод (vk-0229): open banking = мигновено, без IBAN/основание, банкова автентикация. ✓

## SVG number-diff (05b ↔ инфографика)
- „мигновено в двете посоки" / „тегленето често за минути в същата сесия" — 05b ✓ / SVG ✓
- „класически банков превод · няколко работни дни · ръчно нареждане по IBAN" — 05b ✓ / SVG ✓
- „казиното не вижда картови данни, вход или реквизити на сметката" — 05b ✓ / SVG ✓
- „верификацията често е вградена (KYC остава)" — 05b ✓ / SVG ✓
- „наличността зависи от банката и казиното; в България е ограничена" — 05b ✓ / SVG ✓
Всяко твърдение в инфографиката се проследява до 05b. „над 3 000 банки" НЕ е сложено на графиката (има [VERIFY] caveat). Без операторски лога/имена, без хора/лица, без глорификация.

## External check (Step 7 — Gemini cross-model)
external check: skipped (Gemini unavailable, HTTP 402)
images: 1 (infographic, manual integrity PASS; Gemini review skipped 402)

## Human-action list (owned by you, Step 6 / publish)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve/keep the 3 in-text [VERIFY]: кои BG банки са свързани с Trustly, кои BG казина го предлагат, конкретните такси — потвърди в касата при публикуване.
3. Confirm the „над 3 000 банки" scale figure against trustly.com at publish (консервативна долна граница).
4. Confirm the site's affiliate-licence status at publish (footer казва подадено/очаква — никога „издаден").
