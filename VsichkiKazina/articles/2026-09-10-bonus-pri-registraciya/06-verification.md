# 06-VERIFICATION — Всички Казина · 2026-09-10-bonus-pri-registraciya
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Бонус при регистрация: как работи и какви са условията** · type: guide (bonus-mechanics education) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 85 (HL 35→85, PASS pass 1) · images: 2 (best score 100) · run date: 10.09.2026

## Surviving flags
**1** in-text [VERIFY]: данъчен режим на печалбите от хазарт (насочено към счетоводител/НАП, НЕ твърдяно). No [CONFLICT]/[DATA NEEDED]. Няма конкретен оператор, няма licence №, няма конкретна оферта. Всяко € число е ИЛЮСТРАТИВНО (маркирано „примерни" в текста и в инфографиката).

## Nature of the content (why no operator/НАП source needed)
Общи механики на депозитен welcome бонус (индустриален стандарт), не оператор-специфични T&C и не конкретна оферта. Никакви реални бонус числа/лицензи/оператори не са твърдени. Затова темата е в guides-only scope и не опира до geo-blocked BG оператор/НАП източник.

## Illustrative numbers used (none operator-sourced; all marked примерни)
| Where | Figure | Note |
|---|---|---|
| Пример депозит | €100 + 100% бонус €100 = €200 баланс; таван на офертата €500 | илюстративно |
| Превъртане | 35x върху депозит+бонус (€200) = €7,000 оборот | илюстративно |
| Превъртане | 35x само върху бонуса (€100) = €3,500 оборот | илюстративно |
| Принос | 10% → €100 залог брои €10 към превъртането | илюстративно |
| Макс. залог | ~€5 при разиграване | типичен пример |

## Recalculation shown (per Step-6 requirement)
- 35 × €200 = **€7,000** ✓ (база депозит+бонус).
- 35 × €100 = **€3,500** ✓ (база само бонус). Един и същ множител, различна база → двойна разлика в оборота. ✓
- Принос 10%: 0,10 × €100 = **€10** към превъртането ✓.
- Core honesty claims: банерът („100% до €500") не е сумата на ръка (таванът е таван, €600 депозит → пак €500 бонус ✓); реалната цена = множител × база + срок + принос + таван на тегленето; базата „депозит+бонус" удвоява тежестта спрямо „само бонус"; макс. залог и таван на тегленето са скритите ограничения. Всички логически коректни. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline в закриващата секция + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Превъртане ВИНАГИ с база (депозит+бонус vs само бонус) — CRITICAL rule спазен. ✓
- Данъци = [VERIFY], не твърдяно. ✓
- Internal links: only approved set (/kak-ocenyavame/, /bonus-category/welcome-bonus/, /kazino-igri/, /depoziti-i-teglenia/, /otgovorna-igra/). ✓
- Byline Георги Тодоров; brand „Всички Казина". ✓
- Zero em-dashes (prose + SVG aria-label). En-dash only in verbatim footer „10:00–17:00". ✓ No promise/hype/FOMO. ✓ Bonus-механики guide, no operator → no affiliate link. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness by version: initial **35** ("Shows AI patterns 65%") → Humaniser pass 1 **85** ("Likely human-written 85%"). PASS in 1 pass; kept pass 1. content-queue gemini = `human 85`. Pass 1 fixed: signposting intro sentence removed, staccato parallelism merged, two dramatic subheadings made functional, "не е подарък и не е капан" antithesis close removed. All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand UNTOUCHED. 07-gemini-check-1/-2.md persist.

## Images (Step 8)
2 images, best score 100 (gemini-3.1-pro-preview):
- `images/bonus-pri-registraciya-prevurtane.svg` — hand-authored infographic; every figure traces to 05b (€100/€100/€200/35x/€7,000/€3,500); „18+ Играйте отговорно"; marked „числата са примерни". Review pass 1 = 90 (flagged title logic „една база"→„различна база"); fixed → pass 2 = 100.
- `images/bonus-pri-registraciya-hero.webp` — decorative AI hero (gemini-3-pro-image, 24.8 KB); gift + ribbon looping through a padlock = bonus locked until wagering; no fabricated UI/logos/numbers/people/winning.
08-image-review-1/-2.md persist.

## Anti-cannibalization note (Step-6 human check)
No „бонус при регистрация" educational page in the sitemap (checked 10.09.2026). Distinct from the no-deposit pillar vk-0004 (/blog/bonus-bez-depozit-2026/) — this is a DEPOSIT welcome bonus, no-deposit only marked as a separate category. Distinct from the navigational /bonus-category/welcome-bonus/ listing (linked prose-only, hub-and-spoke). Folds the „начален/депозитен бонус/бонус за първи депозит" synonym cluster. Does not duplicate wagering guide vk-0001 (/blog/kak-raboti-razigravaneto/) — превъртане is here one condition of the welcome bonus in context.

## Human-action list (owned by you, Step 6)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the tax treatment of gambling winnings with НАП/счетоводител, or drop the clause — never assert.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
