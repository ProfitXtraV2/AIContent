# 06-VERIFICATION — Всички Казина · 2026-09-24-teglene-pechalba-kyc-verifikaciya
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Как да изтеглиш печалба от онлайн казино: верификация (KYC), лимити и срокове** · type: guide · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 90/100 · humanisation (Gemini): best human-likeness 25 (kept, cap reached) · run date: 24.09.2026

## Surviving flags (2)
**1. [VERIFY] TAX — данъчно третиране на печалбите от хазарт.** Located in the „Данъци върху изтеглената печалба" section. The article states NO rate, NO threshold and NO assertion that winnings are or are not taxed. It explicitly points the reader to a счетоводител/НАП and to the internal tax guide. This is the mandatory brand tax discipline: the claim is flagged, never asserted. Primary source for the human: НАП (nra.bg) and a licensed счетоводител for the reader's specific case. DO NOT resolve into a figure in the text.
**2. [VERIFY] TIMELINES — реалните срокове са оператор-зависими.** Located in the „Колко време отнема" section. All срокове are labelled „примерни" (in the H2, the SVG caption/ALT, and the flag itself). No operator is named, so nothing points at a specific T&C page. Primary source when applied to a real operator: that operator's published „Депозити и тегления"/T&C page. Kept illustrative; not a claim about any real casino.

[CONFLICT]: 0 · [DATA NEEDED]: 0.

## Time-sensitive claims needing a primary-source check
**None specific to an operator.** No operator terms, no live offers, no НАП licence numbers, no odds, no tax thresholds. Dated strings:
- Publication / last-updated **24.09.2026** (run date; factual, not a claim).
- No affiliate-licensing footer in this article (guide carries no operator/affiliate links). If an operator link is ever added, the verbatim 1-Aug-2026 pending-licence footer must be inserted; do not claim an issued site licence or invent a number.

## Illustrative numbers used (all hypothetical / примерни, none sourced)
| Where | Figure | Note |
|---|---|---|
| Срокове e-wallet | до 24 часа | примерен, оператор-зависим |
| Срокове карта | 1 до 3 работни дни | примерен |
| Срокове банков превод | между 1 и 5 работни дни | примерен |
| Първо теглене + KYC | 24 до 72 часа | примерен |
| Worked example | €200 → около 3 дни KYC + до 24 часа превод; второ теглене под ден | примерен |
| Лимит теглене | напр. €2,000 на седмица | примерен |
| Печалба на траншове | €5,000 при €2,000/седмица | примерен |
| Минимум теглене | около €10 или €20 | примерен |

## Recalculation shown (per Step-6 requirement)
Withdrawal-cap example, recomputed from scratch:
- Cap €2,000/седмица срещу печалба €5,000: 2,000 + 2,000 + 1,000 = **€5,000** → излиза на **3 транша** = „на няколко транша". ✓ matches text.
- „последният транш идва седмици след първата заявка": at €2,000/седмица the third tranche falls in седмица 3 → weeks after the first request. ✓ internally consistent.
- €200 first-withdrawal example: около 3 дни (KYC, within the 24–72 часа band = 1–3 дни) + до 24 часа превод. Band-consistent. ✓
No превъртане multiplier is quoted (withdrawal guide, not a bonus guide); no maths error found.

## Compliance spot-check (verbatim untouchables present)
- RG marker line „18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline close + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + Солидарност 0888 99 18 66 (делнични дни 10:00–17:00). ✓
- Byline Георги Тодоров + author-bio slot + pub/updated dates 24.09.2026. ✓ Brand written exactly „Всички Казина". ✓
- Internal links: only the approved/live set (/blog/evro-hazart-depoziti/, /blog/proverka-licenz-kazino/, /blog/danaci-pechalbi-onlajn-kazino/, /otgovorna-igra/), 4 total, no operator domains. ✓
- Zero em-dashes. ✓ No operator named, no sports, no promise/hype words, no tax figure, no invented licence №. ✓ Jurisdiction България named on the AML/legal claim. ✓

## Images
- images/pat-na-teglene-kyc-stapki.svg (5-step flow + примерни срокове; every number traces to 05b) and images/teglene-kyc-verifikaciya-hero.webp (decorative, no people/text/logos). Gemini image review: **100/100 PASS**, no integrity failure (08-image-review-1.md).

## External check
- Gemini Step-7 (gemini-3.1-pro-preview): 3 checks. Human-likeness 25 → 15 → 25. Cap (2 Humaniser passes) reached; kept best (25). Below the 80 target; logged for the human — detector scores on BG casino copy run low (market baseline ~25). No compliance defect; every untouchable intact. Verdicts: 07-gemini-check-1..3.md.

## Human-action list (owned by you, Step 6 / publish)
1. Fill the „[About Всички Казина boilerplate]" slot with the standard About block.
2. Resolve the two [VERIFY] flags: tax → счетоводител/НАП (never a figure in text); timelines stay примерни unless tied to a named operator's T&C.
3. Confirm no duplicate withdrawal/KYC guide exists on the live site before publish.
