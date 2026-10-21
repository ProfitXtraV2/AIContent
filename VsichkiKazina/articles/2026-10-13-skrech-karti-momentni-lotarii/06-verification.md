# 06 — Verification checklist (for the human, Step 6)

Article: **Скреч карти и моментни лотарии: как работят и могат ли да бъдат онлайн**
Slug: `2026-10-13-skrech-karti-momentni-lotarii` · Type: guide · vk-0279
Byline: Георги Тодоров · Brand: Всички Казина

> FLAGS STAY IN THE TEXT until the human resolves them against primary sources. Claude did
> not resolve any flag. This file only pre-assembles the sources so the human's review is fast.

---

## A. Surviving flags (1)

### [VERIFY] — odds / EV sentence (Section „Реалният шанс и защо билетът „губи" средно")
> „…В международните моментни игри делът за най-ниското ниво често е около 1 към 3 или 1 към 4…
> [VERIFY: точните шансове и награден фонд за конкретната българска игра идват само от официалните
> правила на серията; стойностите 1 към 3 / 1 към 4 са международни и примерни, не български.]"
- **What to confirm:** the overall odds-of-any-prize for the specific Bulgarian instant game being
  referenced (if the editor wants to name one), and that the „1 към 3 / 1 към 4" range is presented
  only as an international/illustrative figure, not a Bulgarian number.
- **Primary source:** the official series rules / back-of-ticket print for the specific БСТ/Национална
  лотария моментна игра. toto.bg game pages were **Radware/CAPTCHA-gated** at runtime (could not be
  fetched from the cloud env), so this needs a human with a BG browser, or leave the figure as the
  labelled international illustration it already is. Do NOT insert a BG-specific odds/price figure
  without the official series rules.

---

## B. Time-sensitive / citable claims with primary sources (not flagged, but confirm at review)

| Claim in article | Source to confirm against | Pack reference |
|---|---|---|
| Моментната лотария е вид лотарийна игра по ЗХ | ЗХ чл. 2–3 (видове игри); НАП „Видове хазартни игри" | nap-gambling-law-and-rg-2026-10-10.md §3 |
| Чл. 41, ал. 1 ЗХ — носителят не мени вида на играта | ЗХ чл. 41 ал. 1 (lex.bg / kik-info consolidated ЗХ) | nap pack §3 |
| Чл. 41, ал. 2 ЗХ — всички игри ОСВЕН томбола и моментна лотария може онлайн | ЗХ чл. 41 ал. 2 | nap pack §3 |
| От 01.08.2026 НАП спира достъпа до нелицензиран сайт до 24 ч (чл. 17, ал. 6 ЗХ) | ЗХ чл. 17 ал. 6 (ДВ бр. 69/31.07.2026) | nap pack §4 |
| Играч при нелицензиран организатор — глоба 500 до 2000 лв. (чл. 9, ал. 14 + чл. 97а, ал. 2 ЗХ) | ЗХ чл. 9 ал. 14 + чл. 97а ал. 2 (ДВ бр. 42/2024) | nap pack §4 |
| Сигнали: illegal_gambling@nra.bg | НАП страница „Нелицензирани сайтове" | nap pack §4 |
| НАП препоръчва бюджет ≤5% от нетния доход (RG) | НАП „Отговорна игра" страница | nap pack §5 (gate-flagged to confirm source) |
| Регистър на уязвимите лица (чл. 10г ЗХ) | ЗХ чл. 10г; НАП RG страница | nap pack §5 |
| Линия „Солидарност" 0888 99 18 66 | Национална инф. линия (наркотици/алкохол/хазарт) | nap pack §5 |
| БСТ/toto.bg физически моментни (скреч) игри: „Златният билет", „Големият удар", „Магичната 8" | toto.bg „Моментни игри" (CAPTCHA-gated at runtime — confirm live) | bst-toto-2026-10-10.md |

Note: the article names the БСТ products only as **physical state instant-lottery examples** (no prices,
no odds, no top prizes stated) — in line with the guides-only scope. No operator T&C or НАП-register
data was used.

---

## C. One recalculated figure (worked) — why „цената стои над средната печалба"

The article states the ticket price is always above the average expected payout, without giving a
Bulgarian number. The arithmetic behind that statement, as a **purely illustrative model (НЕ български
данни)**:

- Приемаме примерна серия: 1 000 000 билета по 2 €  →  оборот 2 000 000 €.
- Ако наградният фонд е примерно 50 % от оборота (типичен дял за лотарийни продукти) → 1 000 000 € раздадени награди.
- Средна очаквана печалба на билет = 1 000 000 € ÷ 1 000 000 билета = **1,00 €**, срещу цена **2,00 €**.
- Разликата (≈ 1,00 € на билет) покрива наградите вече са извадени от оборота; остатъкът финансира оператора и каузата/бюджета.

Изводът на механиката (цена > средна печалба) е верен за всяка моментна игра; точният дял на
наградния фонд за конкретна българска игра трябва да дойде от официалните правила (вж. флага в раздел A).
Числата по-горе са примерни и НЕ влизат в статията.

---

## D. External checks (recorded)

- **Step 7 (Gemini text):** gemini-3-pro-image family cross-model. Initial (pass 0) human-likeness **35**
  („Shows AI patterns, 65%"); Humaniser pass 1 → **20**; Humaniser pass 2 → **25**. MAX_GEMINI_PASSES (2)
  reached; both passes lowered the score (noisy detector, goalposts relocating). **KEEP-BEST → pass 0
  kept** (HL 35). `gemini` column = **ai 65**. Human editor attention advised on style; content is
  factually strong (Brand Gate 94/100). Trail: 07-gemini-check-1..3.md.
- **Step 8 (Gemini images):** **2 images, review score 100, PASS**, no integrity issues
  (infographic 100 + decorative hero 100). Trail: 08-image-review-1.md.
- **Brand Gate (Step 5):** 94/100 — PASS WITH FIXES (one em-dash → colon, applied in place).

## E. Status
Guides-only scope: NO operator T&C / НАП-register primary data used or needed. 1 surviving [VERIFY]
(flag A). Claude did NOT resolve flags, post, or merge — the human owns Step 6 and publishing.
