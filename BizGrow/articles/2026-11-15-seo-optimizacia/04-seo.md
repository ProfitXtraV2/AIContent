# 04-seo — /seo-optimizacia/ (Step 4, SEO copywriter)

## PHASE 1 — AUDIT

```
SEO AUDIT — /seo-optimizacia/ (bg)
Main term: seo оптимизация | Intent: commercial + informational (service page; SERP = "какво е + как работи + цена + FAQ")
Placement (03-humanised): title N (none yet), H1 Y („SEO оптимизация на сайтове“), first 100 words Y (lead, sentence 1), H2 Y (#kakvo-e „Какво е SEO оптимизация на сайт“)
Relevance score: 84/100 (alignment 19/25 | entities 31/35 | questions 23/25 | on-page 11/15)

MISSING ENTITIES (canon/sources can cover honestly):
- none required. Present: техническо SEO (обхождане, индексиране, скорост, телефон, redirects, грешки,
  вътрешни връзки), on-page (заглавия, описания, подзаглавия, текст, ключови думи), връзки + Google spam
  policy, content tool → /seo-statii/ with client approval, online shops / product collections, nine
  canon sectors, 4-step canon process, price formation, policies (GDPR owner wording, без дългосрочни
  договори, прозрачни цени), no-guarantee stance + Google's own advice, ads vs SEO → /reklama/.
- Not added (no canon/source): tools (Search Console etc.), audit length, link counts, timelines for
  rankings, access/ownership policy (stays [OWNER CONFIRM] O6).
ORPHANED: none.

UNANSWERED QUESTIONS:
- „Защо сайтът ми не се показва в Google?“ answered in body (#tehnichesko-seo, „една от честите
  причини е техническа“); no FAQ slot left (8/8), so no new FAQ.
- „Кой притежава достъпите?“ left open by design ([OWNER CONFIRM] O6), not answered.

DEFECTS:
- D1 No title / meta description yet → written below.
- D2 Main-term flooding: exact/inflected „SEO оптимизация(та)“ appeared 6x in body copy beyond the
  lead + H1 + H2 (#kakvo-e p1, #vrazki, #za-kogo x2, #cena) and 4x in FAQ questions (1, 3, 4, 5).
  Rule: once each in title, H1, first 100 words, one H2; extra exact-match uses de-flooded.
- D3 FAQ 7 question „…SEO или реклама в Google?“ puts a /reklama/ term („реклама в google“, a
  secondary of the sibling's main term „реклама в гугъл“) into a question heading → reads as
  targeting. Reworded to „платена реклама“; the body keeps the passing mention + link to /reklama/.
- Sibling terms check: „SEO статии“ appears only as a passing description of the content tool next
  to the /seo-statii/ link (#on-page, FAQ 6) → OK. „seo копирайтинг“, „локално seo“, „seo одит“,
  „реклама в гугъл“: 0 occurrences. Banned claims/prices/offers/testimonials: 0. Em-dashes outside
  flag markers: 0.

LINKS TO ADD: none. Body links 3 (/seo-statii/, /diagnostika/, /reklama/) + FAQ 6 /seo-statii/, all
in conversion-links.md. R2 /seo-statii/ kept.

FAQ CANDIDATES: the 8 existing FAQ already cover the brief's buyer questions (what it includes,
guarantee, time to results, price, online shop, texts, SEO vs ads, contract). Count stays 8.
```

## PHASE 2 — OUTPUT

**title** (53 characters, python3 len): `SEO оптимизация на сайтове за малки бизнеси | BizGrow`

**meta_description** (156 characters, python3 len): `SEO оптимизация на сайтове за малки бизнеси: техническо SEO, on-page оптимизация и връзки. Безплатна диагностика и доклад с ясни еднократни цени до 48 часа.`

Checks: no em-dash; main term once in each; no guarantee/ranking wording; „безплатна“ only for the diagnosis; „48 часа“ and „ясни еднократни цени“ are canon (R4).

**Main-term placement after edits:** title ✓ (1) · H1 ✓ „SEO оптимизация на сайтове“ · first 100 words ✓ (lead sentence 1) · one H2 ✓ (#kakvo-e). Remaining inflected body uses: 2 (#za-kogo „При SEO оптимизацията на онлайн магазин“ = secondary „seo оптимизация на онлайн магазин“; #cena „Цената на SEO оптимизацията“ = secondary „seo оптимизация цена“). FAQ questions: 2 (FAQ 1, FAQ 4).

**secondary_keywords used** (naturally, once or twice each): seo оптимизация на сайтове (H1), seo оптимизация на сайт (H2 #kakvo-e, FAQ 1), техническо seo (H2 #tehnichesko-seo), seo услуги (H2 #za-kogo „SEO услугата“, H2 #cena „SEO услугите“, FAQ 8), seo експерт + seo агенция (#ochakvania), seo оптимизация на онлайн магазин (#za-kogo), seo за онлайн магазин (FAQ 5), seo оптимизация цена / seo цена (#cena, FAQ 4; answered without numbers). Not forced: seo фирма, seo компания (no natural slot without stuffing).

**Proposed for the ContentPage port** (formal „Вие“, no em-dashes):
- `label`: „SEO оптимизация“
- `summary`: „Техническо SEO, on-page оптимизация и работа по връзките, с ясни еднократни цени в доклада след безплатната диагностика.“ (120 characters)
- `eyebrow`: „SEO за малки бизнеси“
- `service`: „SEO оптимизация“ (from brief)

---

## OPTIMISED PAGE BODY

Page: /seo-optimizacia/ | Locale: bg | Type: new-page | Main term: seo оптимизация

# SEO оптимизация на сайтове

<!-- LEAD (kind: hero; rendered under the H1, not an H2; the template adds the „Запазете час“ and „Безплатна диагностика“ buttons below it) -->

BizGrow предлага SEO оптимизация на сайтове за малки бизнеси в България, която включва техническо SEO, on-page оптимизация на страниците и работа по връзките от други сайтове. SEO (оптимизация за търсачки) е работата, с която сайтът става по-лесен за откриване и разбиране както от Google, така и от хората, които търсят Вашите услуги.

## Какво е SEO оптимизация на сайт {#kakvo-e}

Тази работа обхваща всичко, което помага на Google да открие страниците Ви, да разбере какво предлагате и да ги покаже на хората, които търсят точно това. Ключовите думи са изразите, които клиентите пишат в Google, когато търсят дадена услуга или продукт.

В собствените си насоки Google посочва с какво може да помогне специалист по SEO. Сред задачите са преглед на съдържанието и структурата на сайта, технически съвети за хостинг, пренасочвания, страници за грешки и използване на JavaScript, както и проучване на ключовите думи. [VERIFY: Google lists content/structure review, technical advice (hosting, redirects, error pages, JavaScript) and keyword research as SEO work — https://developers.google.com/search/docs/fundamentals/do-i-need-seo]

Целта е сайтът да отговаря ясно на въпросите на Вашите клиенти, а Google да може да го прочете и да го показва при подходящите търсения. При BizGrow тази работа има три части: техническо SEO, on-page оптимизация на страниците и връзки от други сайтове.

## Техническо SEO: сайтът да може да бъде открит и прочетен {#tehnichesko-seo}

Техническото SEO се занимава с основата на сайта и с това дали Google може да обходи и индексира страниците му. Обхождането означава, че Google открива страниците, а индексирането, че ги включва в базата, от която подбира резултатите от търсенето.

Когато собственик пита защо сайтът му не излиза в Google, една от честите причини е техническа. Страница, която не е индексирана, не се показва в резултатите, колкото и полезен да е текстът ѝ. Тази част на SEO обикновено обхваща:

- достъпа на Google до страниците и тяхното индексиране;
- скоростта на зареждане и работата на сайта на телефон;
- пренасочванията (redirects) от стари адреси към нови, така че посетителят да не попада на липсваща страница;
- страниците, които връщат грешка, и счупените връзки вътре в сайта;
- подредбата на адресите и вътрешните връзки между страниците.

[OWNER CONFIRM: which technical SEO tasks BizGrow performs; the list above describes the field in general, canon says only „техническо SEO“]

## On-page оптимизация на страниците {#on-page}

On-page оптимизацията е работата по самите страници на сайта: заглавията, описанията, които Google показва в резултатите, подзаглавията и текста. Всяка страница се подрежда около изразите, с които клиентите търсят съответната услуга или продукт, и казва ясно какво предлага. [OWNER CONFIRM: which on-page tasks BizGrow performs (titles, meta descriptions, headings, keyword research, internal links)]

Някои страници имат нужда от нови или по-пълни текстове. Подготвяме ги с [инструмента ни за съдържание](/seo-statii/), който пише SEO статии и описания на продукти. Всеки текст се публикува едва след като го одобрите.

## Връзки от други сайтове {#vrazki}

Връзките (линковете) от други сайтове към Вашия са третата част от работата. Това са споменавания на сайта Ви в други сайтове, които водят посетители и показват на Google, че други се позовават на Вас.

Работата по връзките се води според правилата на Google. В тях купуването и продаването на връзки с цел по-добро класиране е определено като спам на връзки. [VERIFY: buying or selling links for ranking purposes is link spam under Google's spam policies — https://developers.google.com/search/docs/essentials/spam-policies] [OWNER CONFIRM: how BizGrow works on links (which sources, confirmation that no links are bought); canon says only „връзки“]

## За кои бизнеси е подходяща SEO услугата {#za-kogo}

SEO е полезно за всеки бизнес, чиито клиенти търсят в Google, преди да се обадят, да запазят час или да поръчат. Работата цели сайтът да отговаря ясно на тези търсения, за да могат клиентите да го открият.

При SEO оптимизацията на онлайн магазин основната работа е по продуктовите страници и категориите. Инструментът ни за съдържание може да подготви SEO описания за цели колекции от продукти, които Вие одобрявате преди публикуване.

Работим с малки бизнеси от следните сектори:

- ресторанти и кафенета;
- хотели и къщи за гости;
- салони;
- онлайн магазини;
- търговски обекти и шоуруми;
- клиники и практики;
- автосервизи и майстори;
- недвижими имоти;
- фирми, които работят с други фирми (B2B).

## Как протича работата {#kak-rabotim}

Работата минава през четири стъпки и не изисква дългосрочен ангажимент от Ваша страна.

1. **Безплатна диагностика и 30-минутен разговор.** В разговора обсъждаме Вашия бизнес и сайта Ви. Можете да започнете от [безплатната диагностика](/diagnostika/). [OWNER CONFIRM: whether the diagnosis and the 30-minute call cover the website's SEO state; the /diagnostika/ checker is about hours lost per week]
2. **Доклад до 48 часа.** Получавате доклад с приоритизирани решения и ясни еднократни цени.
3. **Изграждане, обикновено до 2 седмици.** Изпълняваме решенията, които изберете от доклада. [OWNER CONFIRM: whether „обикновено до 2 седмици“ applies to SEO fixes, including link work]
4. **Поддръжка с кратък месечен отчет.** След изграждането продължаваме с поддръжка и всеки месец Ви изпращаме кратък отчет.

## Какво можете да очаквате и какво не обещаваме {#ochakvania}

BizGrow не обещава конкретни позиции в Google, трафик, запитвания или срокове за класиране. Подредбата на резултатите я определя Google. Тя зависи и от сайтовете, с които се състезавате. Самият Google съветва собствениците на сайтове да потърсят друг изпълнител, ако някой им обещава най-горното място в резултатите. [VERIFY: Google advises against an SEO who promises first place in search results — https://developers.google.com/search/docs/fundamentals/do-i-need-seo] Можете да използвате този съвет при избора на SEO експерт или SEO агенция.

От нас получавате ясно описание на работата в доклада и сами избирате кои решения да изпълним. Одобрявате всеки текст преди публикуване, а напредъкът се вижда в краткия месечен отчет.

Рекламата в Google работи по друг начин: тя се показва срещу заплащане, докато кампанията е активна. Ако имате нужда от посещения още сега, повече ще намерите на страницата за [реклама в Google и Facebook](/reklama/).

[OWNER CONFIRM: access and ownership policy (who keeps the site, Google accounts and data access after the work); not stated on the page, buyer question left open]

## Как се формира цената на SEO услугите {#cena}

Цената на SEO оптимизацията зависи от това какво трябва да се направи по конкретния сайт. След безплатната диагностика получавате доклад с еднократна цена за всяко отделно решение и сами избирате кои да изпълним.

Цените са прозрачни и не изискваме дългосрочни договори. Диагностиката не Ви задължава с нищо. Работим по GDPR.

Ако имате въпрос преди разговора, можете да ни пишете на {{EMAIL}}.

[Запазете безплатна диагностика]({{BOOKING_URL}})

---

## FAQ

1. **q:** Какво включва SEO оптимизацията на сайт?
   **a:** Тя включва техническо SEO, on-page оптимизация на страниците и работа по връзките от други сайтове. Кои решения са нужни за Вашия сайт, се вижда в доклада след безплатната диагностика.

2. **q:** Можете ли да обещаете най-горното място в резултатите на Google?
   **a:** Не. Подредбата на резултатите я определя Google, затова BizGrow не обещава позиции, трафик или срокове. Самият Google съветва да се избягва изпълнител, който обещава най-горното място. [VERIFY: Google advises against an SEO who promises first place in search results — https://developers.google.com/search/docs/fundamentals/do-i-need-seo]

3. **q:** Кога ще видя резултат от SEO работата?
   **a:** Не даваме срок за позиции в Google, защото той не зависи само от нас. Сроковете, които спазваме, са за самата работа: доклад до 48 часа след диагностиката и изграждане, обикновено до 2 седмици. [OWNER CONFIRM: whether „обикновено до 2 седмици“ applies to SEO fixes, including link work]

4. **q:** Колко струва SEO оптимизацията?
   **a:** Цената зависи от това какво трябва да се направи по сайта. След безплатната диагностика получавате доклад с ясна еднократна цена за всяко решение, без дългосрочен договор.

5. **q:** Подходящо ли е SEO за онлайн магазин?
   **a:** Да, онлайн магазините са сред бизнесите, с които работим. Освен техническата и on-page работа можем да подготвим SEO описания за цели колекции от продукти, които Вие одобрявате преди публикуване.

6. **q:** Пишете ли текстовете и статиите за сайта?
   **a:** Да, с нашия инструмент за съдържание, който пише SEO статии и описания на продукти. Вие одобрявате всеки текст преди публикуване, а повече подробности ще намерите на страницата за [инструмента за съдържание](/seo-statii/).

7. **q:** Кое е по-подходящо за мен, SEO или платена реклама?
   **a:** SEO подобрява самия сайт, за да може да се показва в обикновените резултати на Google, а рекламата се показва срещу заплащане само докато кампанията е активна. Кое да е първо за Вашия бизнес, можем да го обсъдим в безплатната диагностика.

8. **q:** Трябва ли да подпиша дългосрочен договор за SEO услуги?
   **a:** Не, работим без дългосрочни договори. Плащате еднократно за решенията, които изберете, а поддръжката с кратък месечен отчет е отделна стъпка. [OWNER CONFIRM: how monthly support is priced/contracted; canon says only „поддръжка с кратък месечен отчет“ and „без дългосрочни договори“]

---

## LINKS

| link | where | in conversion-links.md |
|---|---|---|
| /seo-statii/ (R2) | #on-page; FAQ 6 | yes |
| /diagnostika/ | #kak-rabotim step 1 | yes |
| /reklama/ | #ochakvania | yes |
| {{BOOKING_URL}} (R3) | #cena closing CTA „Запазете безплатна диагностика“ | token |
| {{EMAIL}} | #cena | token |

## FLAGS (carried unchanged)

| flag | where |
|---|---|
| [VERIFY] F1 Google's list of SEO work (do-i-need-seo) | #kakvo-e |
| [VERIFY] F2 Google: avoid an SEO who promises first place (do-i-need-seo) | #ochakvania; FAQ 2 |
| [VERIFY] F3 buying/selling links = link spam (spam-policies) | #vrazki |
| [OWNER CONFIRM] O1 technical SEO tasks | #tehnichesko-seo |
| [OWNER CONFIRM] O2 on-page tasks | #on-page |
| [OWNER CONFIRM] O3 link work (sources, no bought links) | #vrazki |
| [OWNER CONFIRM] O4 „обикновено до 2 седмици“ for SEO fixes incl. links | #kak-rabotim step 3; FAQ 3 |
| [OWNER CONFIRM] O5 diagnosis/call covers the site's SEO state | #kak-rabotim step 1 |
| [OWNER CONFIRM] O6 access and ownership after the work | #ochakvania |
| [OWNER CONFIRM] O7 monthly support pricing/contract | FAQ 8 |
| [DATA NEEDED] / [LINK NEEDED] | none |

## CHANGE SUMMARY (5 lines)

1. Wrote title (53 chars) and meta description (156 chars), each with the main term once, no em-dash, no ranking promise; proposed label / summary / eyebrow for the ContentPage port.
2. De-flooded the main term in body: #kakvo-e p1 „SEO оптимизацията на сайт обхваща“ → „Тази работа обхваща“; #vrazki „третата част от SEO оптимизацията“ → „третата част от работата“; #za-kogo „SEO оптимизацията е полезна…“ → „SEO е полезно…“ and „SEO работата цели“ → „Работата цели“ (avoids two „SEO работа“ in a row).
3. De-flooded FAQ questions: FAQ 3 „…от SEO оптимизацията?“ → „…от SEO работата?“; FAQ 5 „Подходяща ли е SEO оптимизацията за онлайн магазин?“ → „Подходящо ли е SEO за онлайн магазин?“ (matches secondary „seo за онлайн магазин“).
4. Removed sibling-term targeting from FAQ 7 question („реклама в Google“ → „платена реклама“); body passing mention + /reklama/ link unchanged.
5. No new facts, numbers, links, sections or FAQ; headings, section ids, tokens, flags and all canon wording unchanged.

## INVENTORY DIFF vs 00-inventory.md (03-humanised → 04-seo)

| item | 03-humanised | 04-seo | result |
|---|---|---|---|
| R1 canon item 5 (техническо SEO, on-page, връзки) | lead, #kakvo-e, 3 H2s, FAQ 1 | lead and #kakvo-e three-part sentence unchanged; 3 H2s unchanged; FAQ 1 unchanged | OK |
| R2 body link /seo-statii/ | #on-page, FAQ 6 | unchanged | OK |
| R3 {{BOOKING_URL}} CTA + /diagnostika/ | #cena CTA; #kak-rabotim step 1 | unchanged | OK |
| R4 canon process (30-минутен разговор, 48 часа, „обикновено до 2 седмици“, кратък месечен отчет) | #kak-rabotim, FAQ 3 | unchanged; also echoed in meta („доклад с ясни еднократни цени до 48 часа“) | OK |
| R5 price formation, no numbers | #cena, FAQ 4 | unchanged | OK |
| R6 policies (без дългосрочни договори, прозрачни цени, „Работим по GDPR“) | #cena, FAQ 8 | unchanged | OK |
| R7 no-guarantee statement | #ochakvania, FAQ 2, FAQ 3 | unchanged (FAQ 3 answer unchanged; only its question reworded) | OK |
| R8 6–8 H2 + 6–8 FAQ | 8 H2 + 8 FAQ | 8 H2 + 8 FAQ | OK |

Mechanical counts (identical in 03 and 04): section ids 8 (kakvo-e, tehnichesko-seo, on-page, vrazki, za-kogo, kak-rabotim, ochakvania, cena); H2 headings word-for-word unchanged; links /seo-statii/ x2, /diagnostika/ x1, /reklama/ x1; tokens {{BOOKING_URL}} x1, {{EMAIL}} x1; [VERIFY] 4 occurrences, [OWNER CONFIRM] 8 occurrences; nine-sector list unchanged; em-dashes outside flag markers 0. Items lost: 0. Items weakened: 0. Items added: 0 (title, meta, label, summary, eyebrow are new metadata, not page facts).
