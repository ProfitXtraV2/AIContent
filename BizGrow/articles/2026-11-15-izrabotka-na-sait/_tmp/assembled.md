# 04-seo: /izrabotka-na-sait/ (bg)

Input: 03-humanised.md (EDITED PAGE). Rules read: pipeline/agents/seo-copywriter.md, pipeline/prompts/step-4-seo.md, pipeline/reference/site-rules.md, conversion-links.md, keyword-map.md (own row + sibling main terms), 00-brief.md, 00-inventory.md. Canon change 2026-11-15 applied over the agent file's older price wording: „оферта“ (never „доклад“), no delivery periods; price questions answered without numbers.

## PHASE 1: AUDIT

```
SEO AUDIT — /izrabotka-na-sait/ (bg)
Main term: изработка на сайт | Intent: commercial + informational (service page; SERP = studio service pages with price tables + „колко струва“ articles; local pack present)
Placement (input):  title N (none yet) | H1 Y | first 100 words Y (lead, sentence 1) | H2 Y (#cena „Как се формира цената за изработка на сайт“)
Placement (output): title Y | H1 Y | first 100 words Y | H2 Y (#cena), each exactly once in visible copy
Relevance score (input):  80/100 (alignment 20/25 | entities 28/35 | questions 22/25 | on-page 10/15)
Relevance score (output): 89/100 (alignment 24/25 | entities 28/35 | questions 23/25 | on-page 14/15)
```

QUERY ALIGNMENT
- Main term exact (visible copy): H1, lead sentence 1, H2 #cena, title (added) = once each. The articled body variant „Изработката на сайта поставя основата“ (#telefon-i-google) was a fifth near-exact use → rewritten to „Новият сайт поставя основата.“ FAQ questions 1, 2 and 5 keep the articled variant „изработката на сайт(а)“: they are the buyer's own queries (price, time, SEO) and FAQ items are not body placements (same handling as /izrabotka-na-onlain-magazin/).
- One term per page: „изработка на онлайн магазин“ 0 (only „онлайн магазини“ + link anchor „страницата за онлайн магазини“ → /izrabotka-na-onlain-magazin/); „seo копирайтинг“ 0; „автоматизация на бизнес процеси“ 1 = link anchor to /avtomatizacii/ (passing mention, allowed); „ai автоматизация“ 1 = canon service list, no target. DEFECT: „SEO оптимизация“ (main term of /seo-optimizacia/) appeared 4× (service list, definition sentence, link anchor, FAQ 5 question + answer counted once each in Q/A) → de-flooded to 2 (canon service list + link anchor). The SEO definition now reads „SEO е работата по сайта…“; FAQ 5 uses „SEO“ / „Цялостното SEO“.

ENTITY COVERAGE
- PRESENT: the site's jobs (services/products, contact, booking, current info incl. menu/prices from one place), mobile-first indexing and page experience (2 sourced facts, VERIFY F1/F2), SEO as separate work (/seo-optimizacia/, /seo-statii/ with client approval), audience (8 canon segments), shops routed to /izrabotka-na-onlain-magazin/, canon process (диагностика + 30-минутен разговор → оферта → изграждане → поддръжка с кратък месечен отчет), timing line, maintenance (поддръжка на сайт, monthly + short report), price formation without numbers, no long-term contracts, transparent prices, „Работим по GDPR“, no-promise statement.
- MISSING (buyers expect; canon cannot cover honestly): what a build includes (design, texts, mobile version, form, basic SEO), platform/CMS, domain/hosting/access ownership, redesign of an existing site, maintenance task list. All are already OWNER CONFIRM flags (O1–O5) or owner items; nothing written around them. Domain/hosting ownership has no flag in the copy: recorded below as an owner item for Step 5, no text added.
- ORPHANED: none.

BUYER QUESTIONS (brief list)
- Answered: price / what it depends on (FAQ 1, #cena), time (FAQ 2, step 3 canon line), what a small-business site needs (#kakvo-tryabva), phone/Google (#telefon-i-google), SEO included? (FAQ 5, partly + O5), maintenance (FAQ 3, #poddrazhka + O2), contract (FAQ 4), shops (FAQ 6 + body link), more clients? (FAQ 7, no guarantee), diagnosis commitment (FAQ 8).
- Not answered (owner-dependent, no text written): domain/hosting/access ownership; redesign (O3 covers the diagnosis side); DIY site builder vs studio (neutral answer possible but FAQ cap of 8 reached; not added).
- FAQ CANDIDATES beyond the 8 present: none that the canon can answer within the 6–8 cap.

SYNONYM FIELD: сайт / уебсайт / сайтове, поддръжка, оферта, записване на час, запитване, клиенти, търсене в Google: natural, owner vocabulary; no jargon left unexplained (SEO, индексиране, класиране, Core Web Vitals explained on first use).

ON-PAGE
- Title: missing → added, 56 chars incl. „ | BizGrow“, no em-dash, unique vs siblings (/izrabotka-na-onlain-magazin/ „Изработка на онлайн магазин с автоматизации | BizGrow“; / „AI автоматизация за малкия бизнес | BizGrow“).
- Meta description: missing → added, 147 chars (python3 len), contains the main term, canon-only claims, no em-dash, no number other than none.
- One H1; 8 H2 (target 7–8), no H3; 8 FAQ (target 6–8); no FAQ question repeats an H2 word for word.
- Links: body 4 (/avtomatizacii/, /seo-optimizacia/, /seo-statii/, /izrabotka-na-onlain-magazin/), all four required by the brief, all in conversion-links.md. Kept at 4 (brief requirement outweighs the generic 1–3 guideline). 1 booking CTA (#zapochnete) via {{BOOKING_URL}}, 1 bare {{EMAIL}}.
- Checks on output (python3 over the body): em-dashes 2, both inside the VERIFY F1/F2 flags (pass-through, never visible); „доклад“ 0; „гаранц*/гарантир*“ 0; visible digits only „30-минутен“ (×3), „B2B“ and list/step numbers; delivery periods 0; prices/currency 0; „безплатн*“ only for the diagnosis; lowercase courtesy forms in direct address 0.

DEFECTS FIXED: no title/meta; sibling main term „SEO оптимизация“ flooded (4 → 2); fifth near-exact main-term use in body; secondary „поддръжка на уебсайт“ absent.

## PHASE 2: OPTIMISED PAGE

title = "Изработка на сайт и поддръжка за малки бизнеси | BizGrow"  (56 chars incl. " | BizGrow")
meta_description = "Изработка на сайт за малки бизнеси в България и месечна поддръжка с кратък отчет. Цената е в офертата, която получавате след безплатна диагностика."  (147 chars)
label = "Изработка на сайт"
summary = "Изграждаме сайтове за малки бизнеси и ги поддържаме след пускането, с кратък месечен отчет."
eyebrow = "Сайт и поддръжка"
primary_keyword = "изработка на сайт"
secondary_keywords = ["изработка на уебсайт", "изработка на сайтове", "изработка на сайт цена", "поддръжка на сайт", "поддръжка на уебсайт"]
service = "Изработка на сайт"

Notes on the proposals: label = the breadcrumb/card name and the schema `service` name from the brief (same wording as the conversion-links.md page name); summary (91 chars) uses canon only (build + monthly support with a short report) and no other address's main term; eyebrow follows the sibling pattern („Магазин и автоматизации“).

Secondary keywords used (where):
- изработка на уебсайт: #za-kogo „Тук описваме изработка на уебсайт за бизнеси, които представят услугите си…“
- изработка на сайтове: #kakvo-predlagame „Изработката на сайтове е една от услугите на BizGrow…“
- изработка на сайт цена: H2 #cena „Как се формира цената за изработка на сайт“ + FAQ 1 „Колко струва изработката на сайт?“ (answered without a number)
- поддръжка на сайт: H2 #poddrazhka „Поддръжка на сайт след пускането“; #poddrazhka „Поддръжката на сайт при BizGrow е месечна…“; FAQ 3; lead „поддръжка на сайта“; meta
- поддръжка на уебсайт: FAQ 4 „…дългосрочен договор за поддръжка на уебсайта?“ (added this step)
- изработка на уеб сайт (700, KD 48): not written. It is a spelling variant of „уебсайт“ (covered at #za-kogo); writing the split spelling would read as a typo in a professional page, and KD 48 is out of reach for now.

Page: /izrabotka-na-sait/ | Locale: bg | Type: new-page | Main term: изработка на сайт

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

Новият сайт поставя основата. Видимостта в Google обикновено се изгражда с отделна работа: [SEO оптимизацията](/seo-optimizacia/) на сайта и [SEO статиите](/seo-statii/), които Вие одобрявате преди публикуване.

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

След безплатната диагностика получавате оферта с приоритизирани решения и ясна еднократна цена за всяко от тях. Сами решавате кои решения да изпълним и в какъв ред.

Цените са прозрачни и работим без дългосрочни договори. Диагностиката не Ви задължава с нищо. Работим по GDPR.

## Какво да очаквате и как да започнете {#zapochnete}

Сайтът помага на клиентите да Ви открият и да се свържат с Вас. Не обещаваме конкретни позиции в Google, брой посетители, запитвания или продажби, защото те зависят и от фактори извън сайта, като конкуренцията във Вашия бранш.

Предварително можем да опишем какво ще прави сайтът: кои услуги представя, как клиентът се свързва с Вас и дали може да запази час онлайн. Първата стъпка е безплатна диагностика с 30-минутен разговор, в който обсъждаме Вашия бизнес.

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
