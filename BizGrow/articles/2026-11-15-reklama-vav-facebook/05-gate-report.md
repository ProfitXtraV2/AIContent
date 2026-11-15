# 05-GATE REPORT: /reklama-vav-facebook/ (bg, new-page, 2026-11-15)

Page: /reklama-vav-facebook/ | Locale: bg | Type: new-page | Main term: платена реклама във фейсбук
Inputs: 04-seo.md, 00-brief.md, 00-inventory.md; canon pipeline/markets/bg/author.md (BIZGROW CANON incl. 2026-11-15 changes); pipeline/reference/site-rules.md; verification-policy.md; keyword-map.md; conversion-links.md.

```
BRAND COMPLIANCE SCORECARD — /reklama-vav-facebook/ (bg)
Verdict: PASS WITH FIXES
Total: 90/100 before → 91/100 after
Before: Voice 18/20 | Language 13/15 | Trust & claims 19/20 | Usefulness 13/15 | Anti-AI 13/15 | SEO 14/15
After:  Voice 18/20 | Language 13/15 | Trust & claims 19/20 | Usefulness 13/15 | Anti-AI 14/15 | SEO 14/15
CRITICAL: 0
```

## BLOCKING CHECKS

| # | check | result | note |
|---|---|---|---|
| 1 | Nothing lost (inventory I1–I20) | PASS | 19/19 applicable items present (I20 n/a, no example scenario); diff below. REMOVE-BY-BRIEF: none. |
| 2 | Facts allowed list | PASS | Every BizGrow statement maps to canon: real specialist plans/runs/tracks (I5), report with numbers (I6), what each euro returns (I7), report not tasks (I8), data-driven campaigns (I9), FB + IG (I10, brief), monthly creatives (I11), audience = 9 canon types, process 4 steps, policies. No vendor, team, years, client counts, phone, address, price. „Специалистът ги използва в рекламите“ (`vizii`) is a direct reading of canon service 3 „advertising materials“ + service 4; accepted. |
| 3 | Banned claims | PASS | 0 guarantee/hype/№1/price/offer/testimonial terms; „безплатн*“ only for the diagnosis (6×); no „!“. „Не обещаваме … запитвания или продажби“ is a non-banned negation (no „гарант*“). |
| 4 | Numbers / delivery periods | PASS | Only digit in copy: „30-минутен/30-минутният“ (diagnosis call). No „до 48 часа“, „до 2 седмици“, „за дни“, no other period. „на ден“ in `kak-raboti` is Meta's daily-budget definition, not a delivery period. Timing line is the canon one („Срокът зависи от решението и го посочваме в офертата“). „доклад“: 0; „оферта“ used throughout. Sourced facts: 3 (S1–S3, one Meta page) = max. |
| 5 | Hypothetical label | N/A | No example scenario or before/after row. |
| 6 | GDPR wording | PASS | „Работим по GDPR.“ verbatim, nothing stronger. |
| 7 | Register „Вие“ | PASS | 0 „ти“ forms (only hit „те“ = 3rd-person plural „they“ in `razhodi`); all courtesy forms capitalised (Ви/Вас/Вашия/Вашата/Вашите/Вие, 14 hits); FAQ questions in the reader's first person („Мога ли“, „ми“, „ме“) are correct. |
| 8 | CTAs | PASS | 2 booking CTAs, one per section (`proces` „Запазете безплатна диагностика“, `cena` „Запазете час“), both `{{BOOKING_URL}}`; `{{EMAIL}}` bare token ×1; no urgency. |
| 9 | One term per page | PASS | Main term = keyword-map „платена реклама във фейсбук“; once each in title (exact), H1 (Latin variant „Платена реклама във Facebook“, flagged OC5), lead sentence 1 (exact), H2 `kak-raboti` (definite form). /reklama/ is treated as Google-only: its terms (реклама в гугъл, гугъл/google реклама, google ads реклама, онлайн реклама, реклама в интернет, ppc реклама) 0×; „маркетинг специалист“ 1× as the canon service name in body only (not title/H1/H2/meta/FAQ). /socialni-mrezhi/ terms 0× (link anchor „поддръжка на социални мрежи“ is a navigational anchor to that page, not targeting). /ai-asistent/ terms 0×. |
| 10 | Links & anchors | PASS | /reklama/ (anchor „Google Ads“, Google only), /socialni-mrezhi/ ×2, /diagnostika/, related /reklama/ /socialni-mrezhi/ /ai-asistent/: all in conversion-links.md. `#cena` is this page's own section id (site inline syntax `[label](#anchor)`); 8 section ids new, nothing renamed. No external body links. |
| 11 | BizGrow voice | PASS (after fix) | No rhetorical questions outside FAQ, no fragments as style (bullet labels are UI labels), no slang, no hype, no exclamation marks. Repetition FAQ 3 / FAQ 7 „Резултатът (…) зависи от много фактори“ fixed (see FIXES). |

Owner canon checks 2026-11-15 (requested as blocking): „оферта“ not „доклад“ PASS; no delivery periods PASS; only the 30-minute call carries a duration PASS; ad budget separate/included NOT stated PASS (OC1 open; see MODERATE M1); /reklama/ Google-only PASS.

## CRITICAL
None.

## MODERATE (not blocking; for Step 6 / owner)
- M1 (budget separation, implicit reading). The page never says whether the ad budget paid to Meta is separate from or included in BizGrow's fee. But FAQ 1 and `razhodi` place Meta's ad cost next to „Цената на работата на BizGrow“, so a reader may infer two separate costs. No wording change can remove this without stating one side; leave as is and re-word when OC1 is decided.
- M2 (Meta jargon). „стратегията за наддаване“ and „целта за представяне“ are framed as Meta's own parameter names but not explained. A gloss needs a readable Meta source (the „About Ad Auctions“ page is JS-rendered), so no gloss is added here. Step 6 may confirm Meta's Bulgarian interface terms; otherwise the owner can accept the framing.
- M3 (mixed script in title/meta). „фейсбук“ in Cyrillic beside „Instagram“ in Latin: an SEO choice to carry the exact main term; site rule 7 prefers Latin brand names. Accepted for title/meta/lead/H2; H1 uses „Facebook“.
- M4 (`razhodi`) „суми за клик или минимален бюджет … зависят от тези фактори“: a light reading of S2 for „минимален бюджет“; acceptable as a reason for not giving numbers, Step 6 may tighten if the owner prefers.
- M5 (cross-page) keyword-map's /reklama/ H1 proposal „Реклама в Google и Facebook с маркетинг специалист“ still names Facebook although /reklama/ is now Google-only; raise with the owner's session so the two pages do not compete on H1.
- M6 (style, left) „Като част от нашите услуги можем да изготвяме…“ (`vizii`) and FAQ 6 slightly generic; within voice, not changed.

## FIXES APPLIED (Phase 2)
1. FAQ 7 answer: „Резултатът зависи от много фактори, затова не посочваме срок за него.“ → „Не посочваме предварително кога рекламата ще донесе резултат.“ (repeated FAQ 3 wording and doubled „срок“; meaning unchanged, no fact added, no period added).

No flag resolved or removed; no source, CTA, token, anchor or link removed.

## INVENTORY DIFF (04-seo → 05-gate)
I1–I19 unchanged in place (see 04-seo.md table); I20 n/a. Mechanical counts: {{BOOKING_URL}} 2→2, {{EMAIL}} 1→1, [VERIFY] 5→5, [OWNER CONFIRM] 6→6 in body (+1 OC5 repeat in on-page fields), links /reklama/ 1, /socialni-mrezhi/ 2, /diagnostika/ 1, #cena 1, section ids 8→8, FAQ 8→8, em-dashes outside flags 0, „ти“ 0, „доклад“ 0, delivery periods 0, digits other than 30 and list numbering 0. Title 49 chars incl. „ | BizGrow“; meta 154 chars.

## OWNER ITEMS TO RAISE (for Step 6)
- OC1 Ad budget paid to Meta: separate from BizGrow's fee or included? (OPEN; page states neither.)
- OC2 Who decides the ad budget size (client, specialist, jointly)?
- OC3 Whose ad account / access (Business Manager, Pixel) — owner item only, not on the page.
- OC4 How ongoing ad management is priced alongside the canon one-off price + monthly support.
- OC5 H1 „Платена реклама във Facebook и Instagram“ vs keyword-map „Реклама във Facebook и Instagram“; placements beyond Facebook/Instagram (Messenger, Audience Network)?
- M5 /reklama/ keyword-map H1 still mentions Facebook.
- Sources S1–S3 (https://www.facebook.com/business/ads/pricing): re-check with WebFetch (curl returns 400).

## VOICE NOTES (protect in Step 6)
- Keep the lead's first sentence with the exact main term; keep „Специалистът … отчита се пред Вас с конкретни числа“ and „отчет вместо задачи“ (canon I8).
- Keep the canon timing line verbatim in `proces` step 3 and FAQ 7; add no period anywhere.
- Keep „Според Meta“ attribution at the start of `kak-raboti`, `razhodi`, FAQ 1 and FAQ 4 when the [VERIFY] markers are removed.

---

# GATED PAGE

Page: /reklama-vav-facebook/ | Locale: bg | Type: new-page | Main term: платена реклама във фейсбук

## ON-PAGE FIELDS

- title: Платена реклама във фейсбук и Instagram | BizGrow  (49 characters incl. suffix; no em-dash; main term exact)
- meta_description: Платена реклама във фейсбук и Instagram, водена от реален специалист: планиране, пускане, проследяване и отчет с числа. Започнете с безплатна диагностика.  (154 characters; main term exact; no period promised; no price; no em-dash)
- h1: Платена реклама във Facebook и Instagram [OWNER CONFIRM: H1 adds „Платена“ to the keyword-map proposal „Реклама във Facebook и Instagram“ so it carries the main term; fallback is the keyword-map H1 unchanged (OC5)]
- label: Реклама във Facebook и Instagram
- summary: Реален специалист планира, пуска и следи рекламите Ви във Facebook и Instagram и Ви отчита резултатите с конкретни числа.
- service (schema): Реклама във Facebook и Instagram
- eyebrow: Реклама и растеж
- primary_keyword: платена реклама във фейсбук
- secondary_keywords used: реклама във фейсбук (FAQ 1 q); колко струва реклама във фейсбук (FAQ 1 q); фейсбук реклама (`kakvo-pravim` „всяка фейсбук реклама“); реклама във facebook (`razhodi` H2 „рекламата във Facebook“, variant); платена реклама в инстаграм (FAQ 2 q „платена реклама в Instagram“, Latin script per site rule 7); реклама в инстаграм (`kakvo-pravim` „реклама в Instagram“, Latin script); успешна реклама във фейсбук (FAQ 3 q „успешната реклама във фейсбук“). Not used: реклама във фейсбук цени (covered by FAQ 1 intent; a forced phrase would read unnaturally).
- related (exactly 3, from conversion-links.md, not / and not itself): /reklama/, /socialni-mrezhi/, /ai-asistent/

---

## HERO

- eyebrow: Реклама и растеж
- h1: Платена реклама във Facebook и Instagram [OWNER CONFIRM: H1 adds „Платена“ to the keyword-map proposal „Реклама във Facebook и Instagram“ so it carries the main term; fallback is the keyword-map H1 unchanged (OC5)]
- lead: Предлагаме платена реклама във фейсбук, като кампаниите се планират, пускат и следят от реален специалист. По същия начин водим и рекламите Ви в Instagram. Резултатите Ви се отчитат с конкретни числа, включително какво връща всяко вложено евро.

---

## Какво поема специалистът по Вашата реклама {#kakvo-pravim}

Рекламите на Вашия бизнес във Facebook и Instagram се водят от реален маркетинг специалист. Той поема планирането и изпълнението, а Вие получавате отчет вместо задачи. Не е нужно сами да настройвате всяка фейсбук реклама или реклама в Instagram.

- **Планиране.** Специалистът планира кампаниите във Facebook и Instagram.
- **Настройка и пускане.** Той настройва рекламите и ги пуска.
- **Проследяване.** Следи как се представят кампаниите и какво връща всяко вложено евро.
- **Отчет.** Отчита се пред Вас с конкретни числа.

Рекламата в търсачката Google е описана на страницата за [Google Ads](/reklama/).

[OWNER CONFIRM: whether placements beyond Facebook and Instagram (Messenger, Audience Network) are run; the page names only Facebook and Instagram (OC5)]

## За кои бизнеси е подходяща {#za-kogo}

Рекламите във Facebook и Instagram водим за малки бизнеси, сред които:

- Ресторанти и кафенета
- Хотели и къщи за гости
- Салони
- Онлайн магазини
- Магазини и шоуруми
- Клиники и практики
- Автосервизи и майстори
- Недвижими имоти
- B2B фирми

## Как работи платената реклама във фейсбук {#kak-raboti}

Според Meta бюджетът е основният инструмент за контрол на разходите за реклама. Бюджетът може да бъде дневен или общ. Дневният бюджет е средната сума, която се харчи на ден за дадена кампания, а общият е сумата за целия период на кампанията. [VERIFY: Meta: budget is the most valuable cost control tool; daily budget = average amount per day per ad set or campaign; lifetime budget = amount over the entire run — https://www.facebook.com/business/ads/pricing] Рекламата може да бъде спряна временно или прекратена по всяко време. [VERIFY: „You can cancel or pause your ad at any time.“ — https://www.facebook.com/business/ads/pricing]

[OWNER CONFIRM: who decides the size of the ad budget (client, specialist, jointly); page states nothing until confirmed (OC2)]
[OWNER CONFIRM: whether the ad budget paid to Meta is separate from BizGrow's fee or included in it; OPEN, page states neither (OC1)]

## От какво зависи колко струва рекламата във Facebook {#razhodi}

Според Meta целта на кампанията играе голяма роля за цената на рекламите. Цената зависи и от параметрите на самата реклама, както Meta ги нарича: качеството на рекламата, стратегията за наддаване и целта за представяне, както и от вида на бюджета. [VERIFY: „Your ad campaign's objective plays a large role in impacting the cost of your ads.“ + factors: ad quality, bidding strategy, performance goal, type of budget — https://www.facebook.com/business/ads/pricing]

На тази страница не посочваме суми за клик или минимален бюджет, защото те зависят от тези фактори. Не обещаваме и определен брой запитвания или продажби. Как се формира цената на работата на BizGrow, е описано в раздела [Цена и условия](#cena).

## Кампании на база данни и отчет с числа {#otchet}

Когато реклама се пуска без ясен план, често не е ясно какво точно е донесла на бизнеса. Специалистът изгражда кампаниите на база данни: кой какво купува, кога се връща и какво е подходящо да му предложите. Решенията за следващата реклама се вземат по числата от предишните кампании.

Специалистът отговаря пред Вас с числа и показва какво връща всяко вложено евро. След пускането на кампаниите продължаваме с месечна поддръжка и Вие получавате кратък месечен отчет.

## Визиите за Вашите реклами {#vizii}

Като част от нашите услуги можем да изготвяме всеки месец брандирани визии, публикации и рекламни материали. Специалистът ги използва в рекламите във Facebook и Instagram. Повече за тази услуга ще намерите на страницата за [поддръжка на социални мрежи](/socialni-mrezhi/).

## Как протича работата {#proces}

1. **Безплатна диагностика и 30-минутен разговор.** На страницата за [безплатна диагностика](/diagnostika/) отбелязвате проблемите на Вашия бизнес и запазвате разговора. Диагностиката не Ви задължава с нищо.
2. **Оферта.** След разговора получавате оферта с приоритизирани решения и ясни еднократни цени.
3. **Настройка на кампаниите.** Специалистът подготвя и пуска рекламите. Срокът зависи от решението и го посочваме в офертата.
4. **Поддръжка.** Следим кампаниите и Ви изпращаме кратък месечен отчет.

[Запазете безплатна диагностика]({{BOOKING_URL}})

## Цена и условия {#cena}

Цената на работата на BizGrow е еднократна за всяко решение и зависи от това какво точно се изгражда. Посочваме я в офертата, която получавате след безплатната диагностика. [OWNER CONFIRM: how ongoing ad management is priced alongside the canon one-off price + monthly support; text repeats canon only (OC4)] [OWNER CONFIRM: ad budget paid to Meta separate from or included in BizGrow's fee; page states neither (OC1)]

Цените са прозрачни и работим без дългосрочни договори. Работим по GDPR.

Ако предпочитате да ни пишете, изпратете съобщение на {{EMAIL}}.

[Запазете час]({{BOOKING_URL}})

---

## [[faq]]

1. **q:** Колко струва реклама във фейсбук?
   **a:** Според Meta цената на рекламите зависи от целта на кампанията, качеството на рекламата, стратегията за наддаване, целта за представяне и вида на бюджета. [VERIFY: S2 — https://www.facebook.com/business/ads/pricing] Цената на работата на BizGrow е еднократна, зависи от това какво се изгражда и я посочваме в офертата след безплатната диагностика.

2. **q:** Правите ли и платена реклама в Instagram?
   **a:** Да, специалистът планира, пуска и следи кампаниите както във Facebook, така и в Instagram.

3. **q:** От какво зависи успешната реклама във фейсбук?
   **a:** Резултатът от рекламата зависи от много фактори и не обещаваме определен брой запитвания или продажби. Специалистът изгражда кампаниите на база данни и взема решенията за следващата реклама по числата от предишните.

4. **q:** Мога ли да спра рекламата, ако реша?
   **a:** Според Meta рекламата може да бъде спряна временно или прекратена по всяко време. [VERIFY: S3 — https://www.facebook.com/business/ads/pricing] Работим без дългосрочни договори.

5. **q:** Как ще разбера какво ми носи рекламата?
   **a:** Специалистът се отчита пред Вас с конкретни числа и показва какво връща всяко вложено евро. По време на месечната поддръжка получавате кратък месечен отчет.

6. **q:** Кой подготвя визиите за рекламите?
   **a:** Брандираните визии, публикации и рекламни материали могат да се изготвят всеки месец като част от нашите услуги. Подробности има на страницата за [поддръжка на социални мрежи](/socialni-mrezhi/).

7. **q:** Кога ще има резултат от рекламата?
   **a:** Не посочваме предварително кога рекламата ще донесе резултат. Срокът за настройката на кампаниите зависи от решението и го посочваме в офертата.

8. **q:** Задължава ли ме безплатната диагностика с нещо?
   **a:** Не, диагностиката и 30-минутният разговор не Ви задължават с нищо. След разговора получавате оферта с приоритизирани решения и ясни еднократни цени.

---

## FLAGS (passed through, none resolved)

- [VERIFY] S1 (`kak-raboti`), S2 (`razhodi` + FAQ 1), S3 (`kak-raboti` + FAQ 4); source https://www.facebook.com/business/ads/pricing (re-check with WebFetch; curl returns 400).
- [OWNER CONFIRM] OC1 ad budget paid to Meta separate from or included in BizGrow's fee (`kak-raboti` + `cena`), OPEN, page states neither.
- [OWNER CONFIRM] OC2 who decides the ad budget size (`kak-raboti`).
- [OWNER CONFIRM] OC3 whose ad account / access (owner item only, not on page).
- [OWNER CONFIRM] OC4 pricing of ongoing ad management (`cena`).
- [OWNER CONFIRM] OC5 H1 wording (hero) + placements beyond Facebook/Instagram (`kakvo-pravim`).
- [DATA NEEDED] / [LINK NEEDED]: none.

CANON ADDITIONS: none
