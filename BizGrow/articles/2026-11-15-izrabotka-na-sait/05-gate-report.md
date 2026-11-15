# 05-gate-report: /izrabotka-na-sait/ (bg)

Input: 04-seo.md (PHASE 2 optimised page). Rules read: pipeline/agents/brand-gate-bizgrow.md, pipeline/prompts/step-5-brand-gate.md, markets/bg/author.md (BIZGROW CANON, VOICE, DE-AI, dictionary), reference/site-rules.md, reference/verification-policy.md, keyword-map.md (row /izrabotka-na-sait/, main term „изработка на сайт“, plus sibling main terms), conversion-links.md, 00-current.md (new page, no current copy), 00-inventory.md (R1–R10), 00-brief.md.
Canon decisions of 2026-11-15 applied over older wording (author.md PRICES „report“): the document after the diagnosis is „оферта“, never „доклад“; no delivery periods anywhere; only the 30-minute call carries a duration; timing line „Срокът зависи от решението и го посочваме в офертата.“ Service 6 canon only. Brief-approved exception: 4 required body links.
Mechanical checks (python3 on the page, flags stripped): em-dashes 0, en-dashes 0; „доклад“ 0; гарант*/гаранц* 0; „безплатн*“ 7, all about the diagnosis; lowercase courtesy forms 0; „ти“ forms 0 („те“ ×2 = 3rd-person plural pronoun); digits in visible copy only „30-минутен“ ×3, „B2B“, step numbers; currency 0; exclamation marks 0; title 56 chars, meta 147 chars.

## PHASE 1: EVALUATION

```
BRAND COMPLIANCE SCORECARD — /izrabotka-na-sait/ (bg)
Verdict: PASS WITH FIXES
Total: 88/100
Voice 18/20 | Language 13/15 | Trust & claims 16/20 | Usefulness 13/15 | Anti-AI 14/15 | SEO 14/15
```

### BLOCKING CHECKS

1. NOTHING LOST: PASS. New page, 0 current-page items. Required items R1–R10 all present (see INVENTORY CHECK below). REMOVE-BY-BRIEF: none.
2. FACTS ALLOWED LIST: FAIL, mechanically fixable.
   - #cena „Сами решавате кои решения да изпълним **и в какъв ред**.“ → the client setting the order of work is a term not in the canon (canon: the offer carries *prioritised* fixes; the diagnosis commits to nothing) → delete „и в какъв ред“. FIXED.
   - All other BizGrow statements are canon (service 6 build + поддръжка на сайт; services list subset; audience; four process steps; one-off price per fix in the offer; no long-term contracts; transparent prices; „Работим по GDPR“; diagnosis commits to nothing; menu/prices from one place; online booking synced with a calendar with reminders; SEO = technical, on-page, links) or carry an inline `[OWNER CONFIRM]` (build scope, maintenance tasks, diagnosis scope/redesign, price factors, SEO basics in a build).
   - No platform, vendor, team, years, client count, office, phone, legal data or price.
3. BANNED CLAIMS: PASS. No guarantee words; no №1/лидер/най-добрите; no hype words; no price, offer, promo, testimonial; „безплатн*“ only for the diagnosis. Outcome talk is explicitly non-promissory („Не обещаваме конкретни позиции в Google, брой посетители, запитвания или продажби…“; FAQ 7), wording without banned terms.
4. NUMBERS: PASS. Only „30-минутен“ (canon, diagnosis call) ×3. No delivery period („48 часа“, „до 2 седмици“, „за дни“) anywhere; timing only via the canon line (step 3, FAQ 2). „четири стъпки“ counts the canon steps. „всеки месец“ = canon monthly support. No other figure.
5. HYPOTHETICAL LABEL: N/A. No example scenario or before/after row. The #cena comparison („Сайт, който представя няколко услуги … е различна задача от сайт със записване на час…“) is an illustration of price factors, carries O4, no figures.
6. GDPR WORDING: PASS. „Работим по GDPR.“ (#cena) only.
7. REGISTER: PASS. Zero „ти“ forms in title, meta, H1, H2, body, lists, CTA, FAQ. Imperatives formal („Запазете“, „разгледайте“, „изпратете“). Courtesy forms capitalised (Вие, Ви, Вас, Вашия, Ваш). FAQ questions in the buyer's own 1st person („ме“, „ми“) are correct.
8. CTA RULES: PASS. One booking CTA „[Запазете безплатна диагностика]({{BOOKING_URL}})“ in #zapochnete (approved wording); email only as bare `{{EMAIL}}`; no hard-coded URL/address; no urgency wording. Template buttons/CTA band are site components, not copy.
9. ONE TERM PER PAGE: PASS. „изработка на сайт“ exactly once each in title, H1, lead sentence 1 (first 100 words) and H2 #cena; meta also carries it (required by §6). Other addresses' main terms not in title/H1/H2: „SEO оптимизация“ ×2 (canon service list + link anchor), „автоматизация на бизнес процеси“ ×1 (link anchor), „AI автоматизация“ ×1 (service list), „изработка на онлайн магазин“ 0, „seo копирайтинг“ 0, „безплатна диагностика за бизнеса“ 0 (only „безплатна диагностика“). FAQ 1/2/5 articled variants are buyer-query carriers (accepted, not placements). Breadcrumb label = main term: not a check-9 placement (see MODERATE M5).
10. LINKS & ANCHORS: PASS. Body links /avtomatizacii/, /seo-optimizacia/, /seo-statii/, /izrabotka-na-onlain-magazin/, all in conversion-links.md; 4 vs the generic 1–3 is the brief-approved exception. Section ids new (kakvo-predlagame, kakvo-tryabva, telefon-i-google, za-kogo, kak-rabotim, poddrazhka, cena, zapochnete), no existing anchor changed. No EN pair.
11. BIZGROW VOICE: PASS after fix. One verdict/fragment-style line: #telefon-i-google „Новият сайт поставя основата.“ (4-word aphorism opener) → „Новият сайт е основата за видимостта в Google. Самата видимост обикновено се изгражда с отделна работа: …“ FIXED. No rhetorical questions (the three questions in #telefon-i-google are Google's quoted self-check questions, introduced as such), no slang, no hype, no exclamation marks; jargon explained on first use (SEO, индексиране, класиране, Core Web Vitals).

### CRITICAL (blocks)
- „…кои решения да изпълним и в какъв ред.“ (#cena) → check 2, BizGrow term outside canon → deleted „и в какъв ред“. Mechanically fixed; no fact added.

### MODERATE
Applied here (allowed by Phase 2):
- A1 (check 11) #telefon-i-google verdict line „Новият сайт поставя основата.“ → complete sentence (above). Meaning, links and „обикновено“ qualifier unchanged.
- A2 (check 2 / verification policy) #zapochnete „Предварително можем да опишем какво ще прави сайтът: кои услуги представя, как клиентът се свързва с Вас и дали може да запази час онлайн.“ is a BizGrow statement about the offer's content that depends on the unconfirmed build scope → flag added, no text changed: `[OWNER CONFIRM: that the offer describes in advance what the site will do (services shown, contact path, online booking); same item as the build-scope flag in #kakvo-predlagame]`.

Routed to Step 5b (language polish; do not change meaning, flags, links or keywords):
- M1 #za-kogo „Тук описваме изработка на уебсайт за бизнеси, които…“: page-referential signpost carrying the secondary „изработка на уебсайт“. Rephrase so the sentence states the scope directly; keep the exact phrase „изработка на уебсайт“.
- M2 #kakvo-tryabva „Актуална информация.“ bullet: „навсякъде“ twice in two sentences („…верни навсякъде, където клиентите ги виждат. Менюто и цените могат да се обновяват навсякъде от едно място.“). Remove the repetition; keep the canon capability „обновяване от едно място“.
- M3 #za-kogo „B2B фирми“: the only audience item in jargon; explain in plain words on first use (e.g. „фирми, които продават на други фирми (B2B)“).
- M4 #cena ¶2–¶3 and #kak-rabotim step 2: „решения“ / „решавате“ / „решенията“ cluster („Сами решавате кои решения…“); vary one verb, keep „оферта с приоритизирани решения и ясни еднократни цени“ verbatim.

Routed to Step 6 (report-only, no text change):
- M5 `label = "Изработка на сайт"` equals the main term (breadcrumb/schema name from the brief). Not a check-9 placement; human may switch to „Сайтове“ if breadcrumbs are counted.
- M6 Four process steps here (canon) vs the home page's „три стъпки“ lead (bg.ts `process.lead`): cross-page consistency note for the human/owner.
- M7 Body links 4 (> generic 1–3): brief-approved exception; record in 06-verification.md.
- M8 Buyer question „Мога ли да си направя сайт сам с конструктор?“ unanswered (FAQ cap 8 reached; no canon answer); REMAINING FOR HUMAN.

### OWNER ITEMS TO RAISE (for Step 6)
1. O1 (#kakvo-predlagame, + A2 pointer in #zapochnete): what a BizGrow website build includes (design, texts, mobile version, contact form, basic SEO setup, connecting booking or other systems) and whether the offer describes in advance what the site will do.
2. O2 (#poddrazhka + FAQ 3): which maintenance tasks BizGrow performs (content changes, software and security updates, backups, speed checks) and whether it maintains sites it did not build; that the tasks are described in the offer.
3. O3 (#kak-rabotim step 1): whether the free diagnosis and 30-minute call cover website needs and an existing site (redesign); the /diagnostika/ checker is about hours lost per week.
4. O4 (#cena): the price factors named as illustration (what the site must do, pages and functions, connected booking or systems); canon says only „depends on what is built“.
5. O5 (FAQ 5): which SEO basics are included in a build versus the separate SEO service.
6. Domain, hosting and access (from Step 4, no text written): who provides the domain and hosting and in whose name the site, domain and access stay.
7. Home services list has no website-building card: whether to add a card linking /izrabotka-na-sait/ (site-rules §5, record as [[owner_items]]).
8. F1 (Tier B, #telefon-i-google): Google mobile-first indexing, https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing → Step 6 fetch, quote, [[sources]] + owner item.
9. F2 (Tier B, #telefon-i-google): page experience + self-assessment questions, https://developers.google.com/search/docs/appearance/page-experience → Step 6 fetch, quote, [[sources]] + owner item.

### VOICE NOTES (protect during fixes)
- Calm, specific B2B register works: concrete jobs of the site (services, contact, booking, current info), plain explanations of SEO / indexing / Core Web Vitals, honest non-promise in #zapochnete and FAQ 7. Keep the „обикновено“ qualifier.
- Keep verbatim: the four canon step titles, „Срокът зависи от решението и го посочваме в офертата.“, „Цените са прозрачни и работим без дългосрочни договори. Диагностиката не Ви задължава с нищо. Работим по GDPR.“, the CTA line and the {{EMAIL}} line.
- Do not add a price, platform, maintenance task, page count or any duration other than the 30-minute call.

### INVENTORY CHECK (after Phase 2)
| Item | Status | Where |
|---|---|---|
| R1 service 6 canon only | KEPT | lead; #kakvo-predlagame ¶1–2 + O1; meta/summary canon-only |
| R2 contact, booking → /avtomatizacii/, SEO → /seo-optimizacia/ + /seo-statii/ | KEPT | #kakvo-tryabva bullets 2–3; #telefon-i-google last ¶ (rewritten opener, links unchanged) |
| R3 /izrabotka-na-onlain-magazin/ link, term not targeted | KEPT | #za-kogo; FAQ 6 |
| R4 canon process, „оферта“, no delivery period | KEPT | #kak-rabotim 1–4; FAQ 2 |
| R5 price formation without numbers | KEPT | #cena ¶1–2 (only „и в какъв ред“ removed); FAQ 1; meta |
| R6 policies | KEPT | #cena ¶3; #poddrazhka; FAQ 4, 8 |
| R7 maintenance section + flag | KEPT | #poddrazhka + O2; FAQ 3 |
| R8 booking CTA {{BOOKING_URL}}; bare {{EMAIL}} | KEPT | #zapochnete |
| R9 7–8 H2, 6–8 FAQ | KEPT | 8 H2, 8 FAQ |
| R10 no guarantees | KEPT | #telefon-i-google „обикновено“; #zapochnete; FAQ 7 |
Flags: VERIFY 2 (F1, F2) unchanged; OWNER CONFIRM 6 unchanged + 1 added (A2 pointer to O1). None removed or resolved.

## PHASE 2: APPLICATION (PASS WITH FIXES)

Changes applied (3): (1) #cena „…кои решения да изпълним и в какъв ред.“ → „…кои решения да изпълним.“; (2) #telefon-i-google „Новият сайт поставя основата. Видимостта в Google обикновено се изгражда с отделна работа:“ → „Новият сайт е основата за видимостта в Google. Самата видимост обикновено се изгражда с отделна работа:“; (3) #zapochnete OWNER CONFIRM pointer added after „…дали може да запази час онлайн.“ No fact, number, link, token, anchor or flag removed; no fact or number added.

```
UPDATED SCORECARD — /izrabotka-na-sait/ (bg)
Verdict: PASS WITH FIXES (fixes applied; ready for Step 5b)
Total: 91/100
Voice 19/20 | Language 13/15 | Trust & claims 18/20 | Usefulness 13/15 | Anti-AI 14/15 | SEO 14/15
BLOCKING CHECKS: 1 PASS | 2 PASS (fixed) | 3 PASS | 4 PASS | 5 N/A | 6 PASS | 7 PASS | 8 PASS | 9 PASS | 10 PASS | 11 PASS (fixed)
Criticals remaining: 0 | Moderate for 5b: 4 (M1–M4) | Report-only for Step 6: 4 (M5–M8) | Owner items: 9
```

## ARTICLE FOR STEP 5b

title = "Изработка на сайт и поддръжка за малки бизнеси | BizGrow"  (56 chars incl. " | BizGrow")
meta_description = "Изработка на сайт за малки бизнеси в България и месечна поддръжка с кратък отчет. Цената е в офертата, която получавате след безплатна диагностика."  (147 chars)
label = "Изработка на сайт"
summary = "Изграждаме сайтове за малки бизнеси и ги поддържаме след пускането, с кратък месечен отчет."
eyebrow = "Сайт и поддръжка"
primary_keyword = "изработка на сайт"
secondary_keywords = ["изработка на уебсайт", "изработка на сайтове", "изработка на сайт цена", "поддръжка на сайт", "поддръжка на уебсайт"]
service = "Изработка на сайт"

H1: Изработка на сайт за малкия бизнес

BizGrow предлага изработка на сайт за малки бизнеси в България, както и поддръжка на сайта, след като той започне да работи. Сайтът помага на клиентите Ви да разберат какво предлагате и да се свържат с Вас, без да търсят дълго.

## Какво предлагаме: изработка и поддръжка на сайта {#kakvo-predlagame}

Изработката на сайтове е една от услугите на BizGrow, заедно с AI автоматизациите, собствения ни инструмент за съдържание и SEO оптимизацията. SEO е работата по сайта, която помага на Google да го разбере и да го показва в търсенето.

Ако бизнесът Ви има нужда, сайтът може да работи заедно с другите ни услуги, например със записването на час или със статиите за Google. След като сайтът заработи, поемаме и поддръжката му, ако решите. [OWNER CONFIRM: what a BizGrow website build includes (design, texts, mobile version, contact form, basic SEO setup, connecting booking or other systems); canon says only „изработка на сайтове“ and „поддръжка на сайт“]

## Какво трябва да прави сайтът на малкия бизнес {#kakvo-tryabva}

Сайтът на малкия бизнес има няколко практични задачи. Посетителят трябва бързо да разбере какво предлагате и как може да се свърже с Вас.

- **Ясно описани услуги или продукти.** Всяка основна услуга има свое място на сайта и е описана с думите, с които клиентите я търсят.
- **Лесен начин за контакт.** Телефонът, имейлът или формата за запитване трябва да се виждат от всяка страница на сайта.
- **Записване на час.** За салон, клиника, автосервиз или ресторант възможността клиентът сам да запази час през сайта може да замени част от обажданията. Онлайн записването, синхронизирано с календара и с напомняния, е част от [автоматизацията на бизнес процеси](/avtomatizacii/).
- **Актуална информация.** Работното време, менюто и цените трябва да са верни навсякъде, където клиентите ги виждат. Менюто и цените могат да се обновяват навсякъде от едно място.

## Сайт, който се отваря добре на телефон и се вижда в Google {#telefon-i-google}

В документацията си Google посочва, че използва мобилната версия на съдържанието на сайта за индексиране и класиране. Индексирането означава включване на страниците в търсачката, а класирането е подреждането им в резултатите. [VERIFY: Google uses the mobile version of a site's content for indexing and ranking (mobile-first indexing) — https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing]

Google посочва също, че основните му системи за класиране се стремят да отличават съдържание с добро „преживяване на страницата“. Google предлага на собствениците на сайтове въпроси за самопроверка, например:

- Имат ли страниците добри Core Web Vitals (показатели на Google за скоростта и стабилността при зареждане)?
- Зареждат ли се страниците по защитена връзка?
- Показват ли се страниците добре на мобилни устройства?

[VERIFY: Google's core ranking systems look to reward good page experience; self-assessment asks about Core Web Vitals, secure serving and mobile display — https://developers.google.com/search/docs/appearance/page-experience]

Новият сайт е основата за видимостта в Google. Самата видимост обикновено се изгражда с отделна работа: [SEO оптимизацията](/seo-optimizacia/) на сайта и [SEO статиите](/seo-statii/), които Вие одобрявате преди публикуване.

## За кои бизнеси правим сайтове {#za-kogo}

Работим с малки бизнеси, за които сайтът е мястото, където клиентът проверява услугите, цените и начина за връзка:

- ресторанти и кафенета;
- хотели и къщи за гости;
- салони;
- търговски обекти и шоуруми;
- клиники и практики;
- автосервизи и майстори;
- недвижими имоти;
- B2B фирми.

Ако искате да продавате онлайн, разгледайте [страницата за онлайн магазини](/izrabotka-na-onlain-magazin/). Тук описваме изработка на уебсайт за бизнеси, които представят услугите си и приемат запитвания или записвания на час.

## Как протича работата по сайта {#kak-rabotim}

Работата по сайта минава през четири стъпки, от първия разговор до поддръжката след пускането.

1. **Безплатна диагностика и 30-минутен разговор.** В разговора обсъждаме какво трябва да прави сайтът за Вашия бизнес и кои задачи са най-важни. [OWNER CONFIRM: whether the free diagnosis and the 30-minute call cover the client's website needs and an existing site (redesign); the /diagnostika/ checker is about hours lost per week]
2. **Оферта с приоритизирани решения и ясни еднократни цени.** В офертата всяко решение е описано отделно, с цената си, и Вие избирате кои да изпълним.
3. **Изграждане.** Изграждаме решенията, които сте избрали. Срокът зависи от решението и го посочваме в офертата.
4. **Поддръжка с кратък месечен отчет.** След пускането поддържаме сайта и всеки месец получавате кратък отчет за свършената работа.

## Поддръжка на сайт след пускането {#poddrazhka}

Сайтът има нужда от грижа и след като бъде пуснат, защото информацията за бизнеса се променя и техническата му основа трябва да остане изправна. Поддръжката на сайт при BizGrow е месечна и всеки месец получавате кратък отчет за нея.

Конкретните задачи в поддръжката описваме в офертата според сайта и нуждите Ви. [OWNER CONFIRM: which maintenance tasks BizGrow performs (content changes, software and security updates, backups, speed checks) and whether it maintains sites it did not build; canon says only „поддръжка с кратък месечен отчет“] Поддръжката не Ви обвързва с дългосрочен договор.

## Как се формира цената за изработка на сайт {#cena}

Цената не е една и съща за всички бизнеси, защото зависи от това какво се изгражда. Сайт, който представя няколко услуги и начин за контакт, е различна задача от сайт със записване на час, свързано с календара. [OWNER CONFIRM: the price factors named here as illustration (what the site must do, pages and functions, connected booking or systems); canon says only „depends on what is built“]

След безплатната диагностика получавате оферта с приоритизирани решения и ясна еднократна цена за всяко от тях. Сами решавате кои решения да изпълним.

Цените са прозрачни и работим без дългосрочни договори. Диагностиката не Ви задължава с нищо. Работим по GDPR.

## Какво да очаквате и как да започнете {#zapochnete}

Сайтът помага на клиентите да Ви открият и да се свържат с Вас. Не обещаваме конкретни позиции в Google, брой посетители, запитвания или продажби, защото те зависят и от фактори извън сайта, като конкуренцията във Вашия бранш.

Предварително можем да опишем какво ще прави сайтът: кои услуги представя, как клиентът се свързва с Вас и дали може да запази час онлайн. [OWNER CONFIRM: that the offer describes in advance what the site will do (services shown, contact path, online booking); same item as the build-scope flag in #kakvo-predlagame] Първата стъпка е безплатна диагностика с 30-минутен разговор, в който обсъждаме Вашия бизнес.

[Запазете безплатна диагностика]({{BOOKING_URL}})

Ако предпочитате първо да ни пишете, изпратете имейл на {{EMAIL}}.

## FAQ

[[faq]]
q = "Колко струва изработката на сайт?"
a = "Цената зависи от това какво трябва да прави сайтът, затова не даваме една обща цена предварително. След безплатната диагностика получавате оферта с ясна еднократна цена за всяко решение."

[[faq]]
q = "Колко време отнема изработката на сайта?"
a = "Срокът зависи от решението и го посочваме в офертата. Първата стъпка е безплатна диагностика с 30-минутен разговор."

[[faq]]
q = "Какво включва поддръжката на сайт?"
a = "Поддръжката е месечна и всеки месец получавате кратък отчет за нея. Конкретните задачи описваме в офертата според сайта и нуждите Ви. [OWNER CONFIRM: maintenance task list, same item as in #poddrazhka]"

[[faq]]
q = "Трябва ли да подпиша дългосрочен договор за поддръжка на уебсайта?"
a = "Не. Работим без дългосрочни договори, а цените в офертата са прозрачни."

[[faq]]
q = "Включено ли е SEO в изработката на сайта?"
a = "Сайтът трябва да е изграден така, че Google да може да го прочете и да се показва добре на телефон. Цялостното SEO, с техническа работа, оптимизация на страниците и връзки от други сайтове, е отделна услуга на BizGrow. [OWNER CONFIRM: which SEO basics are included in a BizGrow build versus the separate SEO service]"

[[faq]]
q = "Правите ли и онлайн магазини?"
a = "Да, изработваме и онлайн магазини. На сайта ни те са описани на отделна страница."

[[faq]]
q = "Ще ми донесе ли новият сайт повече клиенти?"
a = "Не обещаваме брой клиенти, запитвания или позиции в Google. Сайтът улеснява клиентите да разберат какво предлагате и да се свържат с Вас. Резултатът зависи и от фактори извън сайта."

[[faq]]
q = "Задължава ли ме безплатната диагностика с нещо?"
a = "Не. След диагностиката и офертата сами решавате дали и кои решения да изпълним."
