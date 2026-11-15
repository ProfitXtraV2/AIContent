# 05-gate-report · /saveti/klyuchovi-dumi/ (Step 5, Brand Gate)

Page: /saveti/klyuchovi-dumi/ | Locale: bg | Type: new-page (advice article) | Main term: ключови думи
Inputs read: 04-seo.md, 00-brief.md, 00-inventory.md, 00-current.md, pipeline/markets/bg/author.md (BIZGROW CANON, DE-AI RULES, AI-TELL DICTIONARY), pipeline/reference/site-rules.md, pipeline/reference/verification-policy.md, keyword-map.md, conversion-links.md.
Mechanical checks: _tmp/gate5.py (lengths, word count, H2/FAQ counts, banned terms, „ти“ forms, digits, main-term hits).

```
BRAND COMPLIANCE SCORECARD — /saveti/klyuchovi-dumi/ (bg)
Verdict: PASS
Total: 92/100
Voice 18/20 | Language 13/15 | Trust & claims 19/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 14/15

BLOCKING CHECKS
1. NOTHING LOST — PASS. New page; every 00-inventory.md item present: L1 /seo-statii/ („статии и текстове за Вашия бранш и град“), L2 /seo-optimizacia/ („оптимизацията на отделните страници“), L3 /diagnostika/ („безплатната диагностика“), C1 one booking CTA in #pomosht, C2 {{EMAIL}} optional/unused, canon closing facts, example label in #primer.
2. FACTS ALLOWED LIST — PASS. BizGrow statements: own content tool writes articles for the client's industry and city; publication only after approval; free diagnosis shows where the business loses time; 30-minute call; „оферта с приоритизирани решения и ясни еднократни цени“; diagnosis commits to nothing. All canon. No vendor, team, years, clients, price, phone or address.
3. BANNED CLAIMS — PASS. 0 guarantee/гарант*, 0 №1/лидер/най-добр*, 0 hype words, 0 prices/promo/testimonials; „безплатн*“ 2× and both about the diagnosis.
4. NUMBERS — PASS. Figures: step numbers 1–3; „30-минутен разговор“ (canon, the only duration); „последните три месеца“ (Search Console default window, external fact under [VERIFY] src 2, not a delivery period). Delivery periods („48 часа“, „до 2 седмици“, „за дни“): 0. „доклад“: 0; „оферта“ used. Sourced facts: 3 ([VERIFY] autocomplete, Performance report, spam policies) = cap; FAQ 4 reuses src 3.
5. HYPOTHETICAL LABEL — PASS. #primer P1: „Примерът е хипотетичен, не е от конкретен клиент и в него няма брой търсения.“ + [OWNER CONFIRM] kept. Other examples (clinic wording, „фризьор за къдрава коса в Пловдив“, „химическо чистене Варна“) are generic search-phrase illustrations, not business scenarios or results.
6. GDPR WORDING — N/A (GDPR not mentioned).
7. REGISTER — PASS. 0 „ти“ forms (only hits for „те“ are the 3rd-person plural „they“: „обикновено те знаят“, „те често са“); 0 lowercase вие/ви/вас/ваш in direct address; formal imperatives throughout (Записвайте, Започнете, Изберете, Пишете, Избягвайте, Запазете).
8. CTA RULES — PASS. 1× [Запазете безплатна диагностика]({{BOOKING_URL}}) (approved wording) in #pomosht; no hard-coded URL/email; no urgency.
9. ONE TERM PER PAGE — PASS. Main term = keyword-map row „ключови думи“. Placement: title 1, H1 1, first 100 words 1 (lead S1), H2 1 (#kakvo-sa-klyuchovi-dumi); the other 7 H2s use „основна дума“. Sibling main terms „seo копирайтинг“ 0, „seo оптимизация“ 0 (not targeted, not anchors), „копирайтър“ 0, „бизнес профил в гугъл“ 0, „изработка на сайт“ 0, „реклама в гугъл“ 0.
10. LINKS & ANCHORS — PASS. Body links /seo-statii/, /seo-optimizacia/, /diagnostika/ all in conversion-links.md; related = exactly those 3 paths; no EN pair.
11. BIZGROW VOICE — PASS. No fragment paragraphs, no rhetorical questions in body (question H2s are allowed by the article format), no exclamation marks, no slang or hype; jargon explained on first use (title, H1, meta description, Search Console, keyword stuffing).

RUN-SPECIFIC CHECKS
- Advice article: 8 question-led H2s (6–8) ✓ | body 947 words (900–1,400; H2s, flags, page fields and FAQ excluded) ✓ | FAQ 6 (4–6) ✓ | one soft closing section #pomosht ✓ | max one booking CTA (1) ✓ | eyebrow „Съвети“ ✓ | label „Ключови думи“ (short) ✓ | summary 124 chars (≤160) ✓ | no service key ✓ | related = /seo-statii/, /seo-optimizacia/, /diagnostika/ (3, from conversion-links.md) ✓
- title 53 chars incl. " | BizGrow" (≤60), no em-dash ✓ | meta description 145 chars (120–160), contains main term ✓
- Canon 2026-11-15: „оферта“ ✓, „доклад“ 0 ✓, delivery periods 0 ✓, only the 30-minute call carries a duration ✓
- Port shape: #kakvo-sa P | #kak-da-otkriete P → steps(3) → closing | #edna-osnovna-duma P(2) → bullets(3) | #namerenie P(3) | #primer P → bullets(4) → closing | #kade-v-teksta P → bullets(5) → closing | #greshki P(3) → bullets(5) | #pomosht P(2) → closing(CTA). Max one steps list and one bullets list per section ✓. Inline only **bold** and [label](path) ✓ (flags are pipeline markers, stripped at port). No tables/H3/images/quotes ✓
- No tool vendors named as recommendations (Ahrefs/Semrush/Ranktracker/Keyword Planner 0; only Google's own autocomplete and Search Console as sourced general facts) ✓
- Em-dashes 0, en-dashes 0 ✓

CRITICAL (blocks): none.

MODERATE (non-blocking; page left as is, optional for the human at port):
- #kak-da-otkriete P1 „Много собственици питат как се откриват ключови думи без платени програми.“ is a soft unsourced observation (it carries the secondary term „как се откриват ключови думи“). Optional rewording that keeps the term: „Ако се питате как се откриват ключови думи без платени програми, започнете от източниците, които вече имате…“.
- FAQ 2 S2 „Основната дума на всяка страница е различна от думите на останалите страници на сайта.“ reads as a description; clearer as advice: „Основната дума на всяка страница трябва да е различна от основните думи на останалите страници.“
- #namerenie P3 „Намерението се проверява лесно:“ leans toward a signpost lead-in; acceptable, could be „За да проверите намерението, потърсете думата в Google…“.
- FAQ 3 restates the Search Console fact without its own [VERIFY] marker; covered by src 2 in #kak-da-otkriete (same fact, no new claim).

OWNER ITEMS TO RAISE (for Step 6):
1. [OWNER CONFIRM] new hypothetical example in #primer (fictional pastry shop in Plovdiv, keywords per page, no numbers): keep?
2. [VERIFY] ×3 external Google facts to confirm and move to [[sources]]: autocomplete reflects real searches (support.google.com/websearch/answer/7368877); Search Console Performance report metrics, query grouping, default 3-month window (support.google.com/webmasters/answer/7576553); keyword stuffing definition and examples (developers.google.com/search/docs/essentials/spam-policies).
3. Coverage gap by design: the meta keywords question (buyer question) and Keyword Planner were left out under the 3-source cap; owner may approve a 4th source in a later run (SEO Starter Guide: "Google Search doesn't use the keywords meta tag").
4. Pipeline housekeeping (not a page defect): pipeline/markets/bg/author.md BIZGROW CANON › PRICES still says the one-off price is „given in the report after the free diagnosis“; it should read „offer“ to match the 2026-11-15 canon change. Shared file, not edited by this stage.

VOICE NOTES (protect during port):
- Formal, calm, practical tone; short concrete examples in owners' words („зъбен имплант“ vs „дентална имплантология“).
- Keep „основна дума“ in the non-main H2s (main-term de-flooding from Step 4).
- Keep the closing exactly as canon: free diagnosis → 30-минутен разговор → оферта с ясни еднократни цени → no obligation.
```

Fixes applied in this stage: none (verdict PASS, zero criticals). The page below is 04-seo.md's page verbatim.

---

# PAGE (gate-approved draft, owner approval pending)

## PAGE FIELDS

- meta.title: Ключови думи: как да ги откриете и изберете | BizGrow
- meta.description: Какво са ключови думи, как да откриете думите, с които клиентите Ви търсят, и как да ги използвате естествено в текста. С пример за малък бизнес.
- eyebrow: Съвети
- label: Ключови думи
- summary: Как да откриете думите, с които клиентите Ви търсят, да изберете една основна дума за страница и да я използвате естествено.
- h1: Ключови думи: как да ги изберете за сайта си
- lead: Ключови думи са думите и фразите, които хората пишат в Google, когато търсят продукт, услуга или отговор. Тук обясняваме как да ги откриете, как да изберете една основна дума за всяка страница и как да я използвате естествено в текста.
- primaryKeyword: ключови думи
- related: /seo-statii/, /seo-optimizacia/, /diagnostika/
- service: none (no key)

---

## Какво са ключови думи и защо са важни за сайта Ви? {#kakvo-sa-klyuchovi-dumi}

Всяко търсене в Google започва с няколко думи, написани от човек, който има конкретна нужда. За Вашия бизнес това са изразите, с които клиентите описват това, което продавате или правите.

Собствениците на бизнес често мислят с професионални термини, а клиентите търсят с по-обикновени думи. Например на сайта на една клиника може да пише „дентална имплантология“, докато пациентите търсят „зъбен имплант“. Когато знаете как говорят клиентите, можете да пишете текстовете на сайта със същите думи и посетителят веднага вижда, че е на правилното място.

## Как да откриете думите, с които клиентите Ви търсят? {#kak-da-otkriete}

Много собственици питат как се откриват ключови думи без платени програми. За малък бизнес е разумно да започнете от източниците, които вече имате, защото в тях личат реалните думи на клиентите.

1. **Въпросите на клиентите.** Записвайте как клиентите питат по телефона, в имейлите и в съобщенията. Думите, които се повтарят, обикновено са същите, с които хората търсят в Google.
2. **Подсказките на Google.** Започнете да пишете основната дума в полето за търсене и разгледайте предложенията, които се появяват под него. Според Google тези предложения отразяват реални търсения, направени в Google. [VERIFY: "Once you start to type, autocomplete predictions reflect real searches that have been done on Google." | https://support.google.com/websearch/answer/7368877]
3. **Google Search Console.** Това е инструмент на Google, с който собствениците следят как сайтът им се показва в търсенето. Отчетът за ефективността (Performance) показва кликванията, показванията, процента кликвания и средната позиция, а данните могат да се групират по заявките, които хората са написали. По подразбиране отчетът показва последните три месеца. [VERIFY: Performance report metrics; "groups your data by the search query users typed"; default "the past three months" | https://support.google.com/webmasters/answer/7576553]

Съберете намерените думи в един списък и до всяка отбележете за коя страница от сайта е подходяща. Така ще видите кои теми вече имат страница и за кои все още няма.

## Защо всяка страница има нужда от една основна дума? {#edna-osnovna-duma}

Определянето на ключови думи започва с правилото, че всяка страница отговаря на едно основно търсене. Изберете за нея една основна дума и няколко близки фрази, които я допълват. Когато две страници на сайта говорят за едно и също, посетителят трудно разбира коя от тях е основната.

Наред с кратките думи съществуват и по-дълги фрази, например „фризьор за къдрава коса в Пловдив“. По тях търсят по-малко хора, но обикновено те знаят по-точно какво искат. За малък бизнес с местни клиенти такива фрази често са добро начало.

Когато избирате основната дума за страница, проверете дали:

- думата описва точно съдържанието на страницата;
- клиентите наистина я използват, защото сте я видели във въпросите им, в подсказките или в Search Console;
- това, което човекът иска да получи с търсенето, съвпада с целта на страницата.

## Какво е намерение на търсенето и защо има значение? {#namerenie}

Зад всяко търсене стои намерение, тоест това, което човекът иска да получи. Едни хора търсят информация, например „как се почиства кожено яке“. Други искат да поръчат услуга или да запазят час, например „химическо чистене Варна“.

Страницата за услуга трябва да отговаря на думите, с които хората искат да поръчат или да се запишат. Статия като тази отговаря на въпроси. Ако смесите двете цели на една страница, тя трудно ще обслужи добре и двете групи посетители.

Намерението се проверява лесно: потърсете думата в Google и разгледайте първите резултати. Ако там са предимно статии, думата е подходяща за статия. Ако са сайтове на фирми и магазини, по-подходяща е страница за услуга или продукт.

## Как изглежда такъв списък за един малък бизнес? {#primer}

Следващият пример за ключови думи е за измислена сладкарница в Пловдив. Примерът е хипотетичен, не е от конкретен клиент и в него няма брой търсения. [OWNER CONFIRM: new hypothetical example (fictional pastry shop in Plovdiv, keywords per page, no numbers): keep?]

- **Начална страница:** „сладкарница Пловдив“.
- **Страница за торти:** „торти по поръчка Пловдив“, с близки фрази като „торта за рожден ден“ и „детска торта“.
- **Страница за събития:** „сладкиши за сватба“ и „сладък бар за сватба“.
- **Статия в блога:** „как да изберем торта за кръщене“.

Всяка страница има своя основна дума и не повтаря думата на друга страница. Статията отговаря на въпрос, докато страниците за торти и за събития са за хора, които вече искат да поръчат.

## Къде в текста да поставите основната дума? {#kade-v-teksta}

Когато подреждате ключови думи в текст, поставете основната дума на местата, които посетителят вижда и чете първи. Използвайте я естествено, така както бихте я казали на клиент в разговор.

- **Заглавието на страницата (title).** Краткото заглавие, с което страницата се показва в резултатите от търсенето и в раздела на браузъра.
- **Основното заглавие (H1).** Голямото заглавие в началото на страницата.
- **Първият абзац.** Още в първите изречения посетителят трябва да разбере, че е намерил това, което търси.
- **Едно от подзаглавията.** Близките фрази могат да стоят в останалите подзаглавия.
- **Краткото описание (meta description).** Едно-две изречения, които описват страницата в резултатите от търсенето.

Тези места са част от [оптимизацията на отделните страници](/seo-optimizacia/), която върви заедно с техническата настройка на сайта. Подредете текста така, че посетителят да намира отговора си още в първите абзаци.

## Колко пъти да повторите основната дума и кои грешки да избегнете? {#greshki}

Няма точен брой повторения, който да е правилен за всяка страница. Пишете за хората и прочетете текста на глас: ако едно изречение звучи неестествено, думата вероятно е повторена твърде често.

Google описва прекаленото повтаряне в правилата си срещу спам (на английски keyword stuffing). Според тях това е пълнене на страница с ключови думи или числа с цел да се повлияе на класирането в резултатите от търсенето. Сред примерите на Google са блокове текст, които изброяват градове и региони, и повтаряне на едни и същи думи толкова често, че звучи неестествено. [VERIFY: keyword stuffing definition + examples "Blocks of text that list cities and regions…", "Repeating the same words or phrases so often that it sounds unnatural" | https://developers.google.com/search/docs/essentials/spam-policies]

Избягвайте следните грешки:

- една и съща основна дума на няколко страници;
- списък с градове в края на страницата без реална информация за тях;
- професионален термин, с който клиентите не търсят;
- дума, която не отговаря на съдържанието на страницата;
- текст, писан за търсачката, който посетителят трудно чете.

## Кога има смисъл да потърсите помощ? {#pomosht}

Първите стъпки можете да направите сами, като изберете по една основна дума за всяка страница на сайта. Когато са нужни повече текстове, BizGrow подготвя [статии и текстове за Вашия бранш и град](/seo-statii/) със собствения си инструмент за съдържание. Всяка статия се публикува едва след Вашето одобрение.

Ако не сте сигурни откъде да започнете, [безплатната диагностика](/diagnostika/) показва къде бизнесът Ви губи време. След 30-минутен разговор подготвяме оферта с приоритизирани решения и ясни еднократни цени. Диагностиката не Ви задължава с нищо.

[Запазете безплатна диагностика]({{BOOKING_URL}})

---

## FAQ (6)

**В: Какво е ключова дума с прости думи?**
О: Това е думата или фразата, която човек пише в Google, когато търси нещо. За един бизнес това са изразите, с които клиентите назовават неговите продукти и услуги.

**В: Колко ключови думи трябва да има една страница?**
О: Препоръчително е една страница да има една основна ключова дума и няколко близки фрази към нея. Основната дума на всяка страница е различна от думите на останалите страници на сайта.

**В: Нужни ли са платени инструменти, за да откриете ключови думи?**
О: За начало не са задължителни. Реални думи, с които хората търсят, ще намерите във въпросите на клиентите, в подсказките, които Google показва при писане, и в отчета за ефективността в Google Search Console.

**В: Има ли значение колко пъти се повтаря ключовата дума?**
О: Правилен брой повторения няма. Прекаленото повтаряне на думи попада в правилата на Google срещу спам, затова думата трябва да стои в текста естествено. [VERIFY: same source as #greshki | https://developers.google.com/search/docs/essentials/spam-policies]

**В: Как да разбера дали дадена дума е за статия или за страница на услуга?**
О: Въведете думата в Google и вижте какви страници се показват най-отгоре. Когато преобладават статии, подходяща е статия, а когато преобладават сайтове на фирми и магазини, по-подходяща е страница за услуга или продукт.

**В: Какво е дълга ключова фраза?**
О: Това е по-дълго търсене от няколко думи, например „фризьор за къдрава коса в Пловдив“. По такива фрази търсят по-малко хора, но обикновено те знаят по-точно какво искат, затова за малък бизнес с местни клиенти те често са добро начало.

---

