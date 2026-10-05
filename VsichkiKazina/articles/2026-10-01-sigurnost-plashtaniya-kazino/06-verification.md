# 06-VERIFICATION — Всички Казина · 2026-10-01-sigurnost-plashtaniya-kazino
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Сигурност на онлайн плащанията в казино: слоевете защита и защо лицензът е първи** · type: guide (concept/security pillar, informational, evergreen) · byline: persona (Георги Тодоров) · gate: PASS WITH FIXES 92/100 (criticals 0) · humanisation: HUMAN-LIKE · Gemini Step-7: SKIPPED (HTTP 402) · images: 1 (infographic, manual integrity PASS) · run date: 01.10.2026 (2nd fire)

## Surviving [VERIFY] flags (still in the text)
**0** in-text [VERIFY] — pure-concept pillar; всички стандарти/версии са описани качествено (без конкретни числа/версии, които да искат потвърждение). 0 [CONFLICT], 0 [DATA NEEDED].

## Time-sensitive / general claims to confirm at publish (source URLs)
| Claim | Source to confirm | Note |
|---|---|---|
| **SSL/TLS** = криптирана връзка (https); сертификат се издава лесно/безплатно → не доказва честен оператор | dnsfilter.com; certera.com (padlock limits) | Web-verified concept. |
| **PCI DSS** = стандарт за боравене с картови данни, съставен от картовите схеми, поддържан от независим съвет; потвърждава се периодично | pcisecuritystandards.org; cloudflare (PCI explainer) | Web-verified concept. |
| **3-D Secure / SCA** = второ потвърждение от банката; **поне два независими фактора от три категории** (знаеш/притежаваш/си); в ЕС задължително | emvco.com (3DS); checkout.com (SCA) | Web-verified concept. |
| **Токенизация** = реалният номер се заменя с токен без връзка с оригинала; номерът стои при доставчика; токенът е merchant-specific | worldpay.com; squareup.com (tokenization) | Web-verified concept. |
| **Лиценз от НАП = първата проверка** (пази правата ти); слоевете пазят само транзакцията | licence-first site doctrine; /zakonno-li-e/ | Brand doctrine; concept-level. |

### Sources (cited in 00-brief; web-verified 01.10.2026)
1. pcisecuritystandards.org — PCI DSS overview (standard for handling cardholder data, maintained by an independent council): https://www.pcisecuritystandards.org/
2. emvco.com — 3-D Secure / EMVCo 3DS knowledge hub (3-domain model; bank step-up authentication): https://www.emvco.com/knowledge-hub/
3. checkout.com — Strong Customer Authentication (two of three independent factors, EU requirement): https://www.checkout.com/
4. worldpay.com / squareup.com — payment tokenization (real PAN replaced by a token, stored by the provider; merchant-specific): https://www.worldpay.com/
5. dnsfilter.com / certera.com — the padlock/HTTPS does not prove a site is trustworthy: https://www.dnsfilter.com/

## Illustrative numbers used (labelled / hedged)
| Where | Figure | Note |
|---|---|---|
| SCA | поне два независими фактора от три категории | web-verified (EU SCA); не illustrative |
| (иначе) | няма числови конкретики | концептуален pillar, без измислени статистики |

## Recalculation shown (per Step-6 requirement)
- Няма деривирани изчисления (концептуален pillar; без превъртане/€-математика/RTP). Единствената
  числова конкретика („два от три фактора", SCA) е web-verified стандарт, не примерна и не [VERIFY].

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-body + footer). ✓ (2×)
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 август 2026 / ДВ бр. 69), pending-application, БЕЗ issued-licence claim, БЕЗ измислен №. ✓
- Internal links: само verified-live (/blog/casino-payments/, /depoziti-i-teglenia/, /zakonno-li-e/, /otgovorna-igra/), 4 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" коректно. ✓
- Concept pillar, без конкретен оператор/сертификат → без Протокол, без НАП №, без афилиейт линк, без измислен сертификатен №. SSL/TLS/PCI DSS/3-D Secure/SCA/токенизация = generic standards (plain text). ✓
- Zero em-dashes (вкл. meta и SVG). En-dash само в „10:00–17:00". Без промис/хайп/FOMO. Данъчна тема не се засяга. ✓
- Licence-first doctrine силно присъства (лицензът пред всичко; слоевете пазят транзакцията, не правата). ✓
- Anti-cannibal: altitude = „как да познаеш сигурна каса + защо лицензът е първи"; method-guide статиите (карта/портфейли/Revolut/банков превод/Trustly) реферират насам (fold-in), НЕ пренаписани. ✓

## SVG number/claim-diff (05b ↔ инфографика)
- НАП: „първата проверка, преди всичко останало · пази правата ти" — 05b ✓ / SVG ✓
- Layer 1 SSL/TLS „криптирана връзка (https), не гарантира честен оператор" — 05b ✓ / SVG ✓
- Layer 2 PCI DSS „правила за картовите данни, оператор + платежен доставчик" — 05b ✓ / SVG ✓
- Layer 3 3-D Secure/SCA „второ потвърждение, поне два от три фактора" — 05b ✓ / SVG ✓
- Layer 4 токенизация „казиното пази токен, не номера; номерът при доставчика" — 05b ✓ / SVG ✓
- Footer „сигурността пази транзакцията, лицензът пази правата ти" — 05b ✓ / SVG ✓
Всяко твърдение в инфографиката се проследява до 05b. Без операторски лога/имена, без хора/лица, без глорификация.

## External check (Step 7 — Gemini cross-model)
external check: skipped (Gemini unavailable, HTTP 402)
images: 1 (infographic, manual integrity PASS; Gemini review skipped 402)

## Human-action list (owned by you, Step 6 / publish)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. (No in-text [VERIFY] to resolve.) Confirm the generic security-standard descriptions at publish against the cited sources if desired.
3. Confirm the site's affiliate-licence status at publish (footer казва подадено/очаква — никога „издаден").
