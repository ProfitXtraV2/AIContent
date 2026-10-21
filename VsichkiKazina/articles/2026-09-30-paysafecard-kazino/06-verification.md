# 06-VERIFICATION — Всички Казина · 2026-09-30-paysafecard-kazino
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **PaySafeCard в онлайн казино: как работи, лимити и предимства** · type: guide (payment-method, evergreen) · byline: persona (Георги Тодоров) · gate: PASS 94/100 (criticals=0) · humanisation: HUMAN-LIKE · images: 1 (infographic, manual integrity PASS) · run date: 30.09.2026

## Surviving [VERIFY] flags (4 — country-variable / time-sensitive; confirm at publish)
| # | Flag (in-text) | What / why | Primary source to confirm |
|---|---|---|---|
| 1 | Транзакционен таван на класически ваучер ~€250 | Exact per-transaction cap varies by country and was changed over time (reduced 2016 per Wikipedia); do not assert one number as universal | https://en.wikipedia.org/wiki/PaysafeCard · https://www.paysafecard.com/en-us/fees-limits/ |
| 2 | my paysafecard лимит до ~€1 000 (транзакция/месец) | Registered-account limits differ by country/status; US page shows $1,000 monthly for the branded tier | https://www.paysafecard.com/en-us/fees-limits/ |
| 3 | Малка такса от разпространителя при покупка на каса | Distributor may add a purchase fee; varies by outlet/country (US retail fees $1.49–$3.49 cited) | https://www.paysafecard.com/en-us/fees-limits/ |
| 4 | Такса за неактивност + валутно конвертиране | Inactivity fee amount and timing vary by country/registration (US: $2/month after 24 months; some EU sources cite €2–€3/month with different windows); FX conversion fee provider-dependent | https://www.paysafecard.com/en-us/fees-limits/ · https://en.wikipedia.org/wiki/PaysafeCard |

## Time-sensitive / general method claims to confirm at publish (source URLs)
| Claim | Source | Note |
|---|---|---|
| PaySafeCard стартиран **2000 г.** (Австрия); **16-цифрен PIN**; купува се в брой без банкова сметка | https://en.wikipedia.org/wiki/PaysafeCard | Web-verified, evergreen. |
| Депозит **моментален**; **депозит-само** (няма теглене обратно); нужен алтернативен метод за изход | https://wizardofodds.com/banking/paysafecard/ | Web-verified. Core claim of the article. |
| Анонимност спрямо оператора (не спрямо закона); KYC на казино акаунта остава | https://wizardofodds.com/banking/paysafecard/ · https://en.wikipedia.org/wiki/PaysafeCard | Framed as „анонимен спрямо казиното в тесен смисъл". |
| Номинали **€10–€100** (типично €10/€25/€50/€100), варират по държава | https://en.wikipedia.org/wiki/PaysafeCard · https://www.paysafecard.com/en-us/fees-limits/ | Range web-verified; exact set country-variable. |
| **my paysafecard** акаунт комбинира ваучери / вдига лимити | https://www.paysafecard.com/en-us/fees-limits/ | Web-verified. |
| Вграден таван на харчене = сумата на ваучера (spending control) | https://wizardofodds.com/banking/paysafecard/ | „players cannot spend funds they don't have". |

## Illustrative numbers used (labelled „примерни", none operator-sourced)
| Where | Figure | Note |
|---|---|---|
| §3 / §7 | Ваучер €50 → баланс €50; таван за сесията = €50 | illustrative |
| §5 | 3 × €50 = €150 | illustrative, labelled примерни |
| §5 / SVG | Номинали €10 – €100 | примерни, варират по държава |

## Recalculation shown (per Step-6 requirement)
- Комбиниране на ваучери: 3 × €50 = **€150**. ✓ matches text + SVG range note.
- Ваучер €50 → баланс €50 → сесиен таван €50 (еднопосочен метод, няма свързан източник за догонване). ✓
- Няма превъртане/RTP/score аритметика (payment-method guide, не review). N/A.

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (§7 body + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), application-pending wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the verified-live set for vk-0225 (/blog/casino-payments/, /depoziti-i-teglenia/, /blog/evro-hazart-depoziti/, /otgovorna-igra/), 4 distinct. ✓ No other internal URL.
- Byline Георги Тодоров; brand „Всички Казина" correct. ✓
- Zero em-dashes (incl. title/meta). En-dash only in numeric range „€10 – €100" and verbatim footer „10:00–17:00". ✓
- No operator named → no affiliate link, no НАП licence № needed (payment-method guide). ✓
- No „Протокол на тегленето:" (no real receipts supplied) — correctly omitted, none invented. ✓

## External check (Step 7 — Gemini cross-model)
external check: skipped (Gemini unavailable, HTTP 402)
Single draft kept; no cross-model humanness pass available. Manual anti-AI self-check (Step 5 + author self-check) passed: 0 em-dashes, no banned connectives, no „не X, а Y" ender habit, no signposting, varied rhythm, asymmetric ending.

## Images (Step 8)
images: 1 (infographic, manual integrity PASS; Gemini review skipped 402)
- `images/paysafecard-depozit-teglene.svg` — hand-authored infographic; every number/word traces to 05b (16-цифрен PIN, „Купи ваучер", „Въведи 16-цифрен PIN", „Депозитът е моментален", „Депозит: ДА (моментален)", „Теглене: НЕ (нужен друг метод)", „Заредиш ли €50, това е таванът", „€10 – €100", „примерни, варират по държава", „18+ Играйте отговорно"); no operator logos/names; no people/faces; no glamorised winning. Rendered to PNG at 720px and eyeballed: no overlap, no clipping, ≥16px padding. Well-formed XML with <title>.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve/confirm the 4 [VERIFY] flags against paysafecard.com for the Bulgarian/EUR market at publish (limits + fees change and are country-specific).
3. Confirm PaySafeCard is currently offered by the casinos you list elsewhere (method availability changes); this guide names no operator by design.
4. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
