# 04-seo: /izrabotka-na-onlain-magazin/ (bg)

Input: 03-humanised.md (PHASE 2: EDITED PAGE). Rules read: pipeline/agents/seo-copywriter.md, pipeline/prompts/step-4-seo.md, pipeline/reference/site-rules.md, conversion-links.md, keyword-map.md (own row + siblings), pipeline/markets/bg/author.md (canon).

## PHASE 1: AUDIT

```
SEO AUDIT — /izrabotka-na-onlain-magazin/ (bg)
Main term: изработка на онлайн магазин | Intent: commercial + informational (service page; SERP = studios, a1.bg DR 71 #1)
Placement (input): title N (none yet) | H1 Y | first 100 words Y (lead, sentence 1) | H2 Y (#kakvo-vklyuchva)
Relevance score (input): 79/100 (alignment 21/25 | entities 27/35 | questions 20/25 | on-page 11/15)
Relevance score (output): 88/100 (alignment 24/25 | entities 27/35 | questions 22/25 | on-page 15/15)
```

QUERY ALIGNMENT
- Main term exact: H1, lead sentence 1, H2 #kakvo-vklyuchva, title (added). Body has no further exact uses. FAQ 1 uses the articled variant „изработката на онлайн магазин“ in the question; kept on purpose because it is the buyer's price query (secondary „изработка на онлайн магазин цена“), and FAQ questions are not body placements.
- Secondary terms in input: „създаване на онлайн магазин“ (#za-kogo), „създаването на онлайн магазин“ (FAQ 2), „изработването на онлайн магазин“ (#kak-rabotim); „платформа за онлайн магазин“ only inside an OWNER CONFIRM marker (not visible), price term only through FAQ 1.
- One term per page: no sibling main term targeted. „изработка на сайт“, „seo оптимизация“, „seo за онлайн магазин“, „seo копирайтинг“: 0. „автоматизация на бизнес процеси“: 1, as the link anchor to /avtomatizacii/ (passing mention with link, allowed). DEFECT: „AI асистент“ (main term of /ai-asistent/) appeared 5 times (bullet, #pratki x2, link anchor, FAQ 4); de-flooded to 2 (one explanation of the term, one link anchor) by using the owner word „асистент в чата“.

ENTITY COVERAGE
- PRESENT: the shop itself (where customers browse and order); courier-connected assistant with parcel status (Messenger, Instagram, WhatsApp, around the clock, collects contact); SEO product descriptions for whole collections with client approval; abandoned-cart reminders; data-driven campaigns; integration of orders, spreadsheets, accounting; document automation; dashboard; audience (online shops, retail, showrooms); process 4 steps; offer with one-off prices; monthly support + short report; no long-term contracts; transparent prices; GDPR in owner wording; diagnosis checker „Онлайн магазин“ with hours „ориентировъчно … на база типични случаи“.
- MISSING (buyers expect, canon cannot cover honestly): platform, payments, courier integrations beyond status, domain/hosting/SSL/ownership, design and mobile view, product migration, client editing products/training. All already carried as OWNER CONFIRM markers (O1–O8, O10, O11); nothing written around them.
- ORPHANED: none.

BUYER QUESTIONS
- Answered: price formation (FAQ 1, #cena), time (FAQ 2, step 3, canon line), courier „Къде ми е поръчката?“ (#pratki, FAQ 4), Google visibility without promises (#opisania-na-produkti, FAQ 5), many product descriptions (#opisania-na-produkti), abandoned carts (#izostaveni-kolichki), orders/accounting (#poruchki-i-schetovodstvo), support (FAQ 6), contract/commitment (FAQ 7), existing shop (FAQ 8).
- Partly / owner-dependent: platform (FAQ 3, now phrased with the secondary term „платформа за онлайн магазин“; answer still under OWNER CONFIRM O1); payments/couriers/hosting/ownership (markers only, Tier 3 / not canon, no text written).
- FAQ CANDIDATES beyond the 8 present: none that the canon can answer; the FAQ cap of 8 is reached.

ON-PAGE
- Title: missing in input → added, 53 chars, no em-dash, unique vs sibling /izrabotka-na-sait/ (H1 „Изработка на сайт за малкия бизнес“).
- Meta description: missing → added, 155 chars, contains the main term, no em-dash.
- One H1; 8 H2 (target 7–8); no H3; 8 FAQ (target 6–8); FAQ questions do not repeat any H2 word for word.
- Links: body 4 (/diagnostika/, /ai-asistent/, /seo-statii/, /avtomatizacii/) = owner-required 3 + /diagnostika/; FAQ 5 links /seo-optimizacia/. All in conversion-links.md. Kept at 4 (owner requirement outweighs the generic 1–3 guideline; no reason to change).
- CTAs: 2 booking CTAs in different sections (#kak-rabotim „Запазете безплатна диагностика“, #cena „Запазете час“), 1 `{{EMAIL}}`. Kept.
- Checks on output: em-dashes 0; „доклад“ 0; numbers visible: „30“ (call) and step numbers 1–4 only; no delivery periods; no prices; banned terms 0 („безплатн*“ only for the diagnosis); lowercase courtesy forms in direct address 0.

DEFECTS FIXED: no title/meta; secondary „платформа за онлайн магазин“ not visible on the page; sibling term „AI асистент“ flooded (5); #cena H2 did not carry the shop context of the price query.

## PHASE 2: OPTIMISED PAGE

title = "Изработка на онлайн магазин с автоматизации | BizGrow"  (53 chars incl. " | BizGrow")
meta_description = "Изработка на онлайн магазин за малкия бизнес, с AI отговори за пратки, SEO описания на продукти и напомняния за колички. Започнете с безплатна диагностика."  (155 chars)
label = "Онлайн магазин"
summary = "Изграждаме онлайн магазини за малки бизнеси и добавяме към тях отговори за пратки, SEO описания на продукти и напомняния за изоставени колички."
eyebrow = "Магазин и автоматизации"
primary_keyword = "изработка на онлайн магазин"
secondary_keywords = ["създаване на онлайн магазин", "изработка на онлайн магазин цена", "изработване на онлайн магазин", "платформа за онлайн магазин"]

Secondary keywords used (where):
- създаване на онлайн магазин: #za-kogo „Създаване на онлайн магазин има смисъл…“; FAQ 2 „създаването на онлайн магазин“
- изработка на онлайн магазин цена: FAQ 1 „Колко струва изработката на онлайн магазин?“ + H2 #cena „Как се формира цената на онлайн магазина“ (price intent, no number)
- изработване на онлайн магазин: #kak-rabotim „Изработването на онлайн магазин започва с този разговор.“
- платформа за онлайн магазин: FAQ 3 question „Коя платформа за онлайн магазин използвате?“ (answer pending OWNER CONFIRM O1)
- изработка онлайн магазин: not written (ungrammatical without „на“); covered by the main-term match.

# Изработка на онлайн магазин

<!-- lead (ContentPage `lead`, under the H1, no heading) -->
BizGrow предлага изработка на онлайн магазин за малки бизнеси в България. Към магазина можем да добавим решения, които намаляват ръчната работа около поръчките, пратките и продуктите.

## Изработка на онлайн магазин: какво включва {#kakvo-vklyuchva}

Изграждаме самия магазин и, когато има нужда, решенията около него, които поемат повтарящата се работа. Кои от тях да включим, избираме според това къде Вашият магазин губи време.

- Онлайн магазинът, в който клиентите Ви разглеждат продуктите и поръчват.
- Асистент в чата, който е свързан с куриера и отговаря на въпроси за пратките.
- Описания на продуктите за цели колекции, подготвени за търсачките (SEO).
- Автоматични напомняния за изоставени колички.
- Връзка между поръчките, таблиците и счетоводството без ръчно копиране.

Какво точно ще бъде изградено, определяме след безплатната диагностика и го описваме в офертата. Така знаете предварително какво включва работата и каква е еднократната цена.

[OWNER CONFIRM: на коя платформа за онлайн магазин изработвате магазините (готова платформа или собствено решение) и дали изборът се прави заедно с клиента; canon names no platform, buyers search „платформа за онлайн магазин“]
[OWNER CONFIRM: какви плащания се настройват в магазина (карта, наложен платеж, банков превод)]
[OWNER CONFIRM: какви връзки с куриери се настройват освен отговора за статус на пратката (изчисляване на доставка, товарителници) и с кои куриери]
[OWNER CONFIRM: домейн, хостинг и SSL сертификат: кой ги осигурява и на чие име остават магазинът и профилите]
[OWNER CONFIRM: дизайн, работа на телефон, брой корекции и прехвърляне на продукти от съществуващ магазин]

## За кои бизнеси е подходящо {#za-kogo}

Работим с малки бизнеси, които продават стоки: онлайн магазини, както и магазини и шоуруми, които искат да продават и през интернет. Създаване на онлайн магазин има смисъл, когато клиентите Ви вече търсят продуктите Ви онлайн. Има смисъл и когато поръчките по телефон и в съобщения отнемат твърде много време.

Ако вече имате онлайн магазин, трудността често е в повтарящата се работа около поръчките. В [безплатната диагностика](/diagnostika/) изберете „Онлайн магазин“ и отбележете проблемите, които познавате. Ще видите ориентировъчно колко часа седмично отиват за тях, изчислени на база типични случаи. След това можете да запазите разговор. [OWNER CONFIRM: дали автоматизациите се добавят и към магазин, изработен от друг, и на кои платформи]

## Автоматични отговори на въпроса „Къде ми е поръчката?“ {#pratki}

В онлайн магазина едни и същи въпроси за пратките идват всеки ден и отнемат време на човека, който проверява и отговаря. Свързваме асистент в чата с куриера и той отговаря автоматично на клиента със статуса на пратката.

Асистентът в чата (AI асистент) е автоматичен помощник, който отговаря на клиентите в Messenger, Instagram или WhatsApp по всяко време на денонощието. Когато не може да помогне, той записва контакта на клиента, за да можете да се свържете с него. Повече подробности ще намерите на страницата за [AI асистента](/ai-asistent/). [OWNER CONFIRM: с кои куриери се свързва асистентът и дали отговаря и в чат на самия магазин]

## SEO описания на продукти за цели колекции {#opisania-na-produkti}

Когато в магазина влизат много нови продукти, описанията им често остават за по-късно или се пишат ръчно едно по едно. Нашият собствен инструмент за съдържание пише SEO описания за цели колекции. SEO описанието е текст, подготвен така, че търсачки като Google по-лесно да разберат какво продавате.

Вие преглеждате и одобрявате всяко описание, преди да бъде публикувано. Позицията на магазина в Google зависи от много фактори, затова не обещаваме конкретно място в резултатите. Как работи инструментът, можете да видите на страницата за [SEO статии и описания](/seo-statii/).

## Напомняния за изоставени колички {#izostaveni-kolichki}

Част от клиентите добавят продукти в количката и затварят страницата, без да завършат поръчката. Ако никой не им напомни, тези поръчки обикновено остават незавършени.

Настройваме автоматични съобщения, които напомнят на клиента за изоставената количка според правила, договорени предварително с Вас. [OWNER CONFIRM: по какъв канал се изпращат напомнянията (имейл, SMS, Messenger)] Със същите данни за покупките могат да се подготвят и кампании според това кой какво купува и кога се връща.

## Поръчки, таблици и счетоводство без ръчно копиране {#poruchki-i-schetovodstvo}

В много магазини едни и същи данни се прехвърлят ръчно от поръчките в таблица и след това в счетоводството. Свързваме програмите, които вече използвате (това се нарича интеграция), и данните се попълват сами, без копиране.

Към това можем да добавим автоматизация на документите и табло (дашборд) с основните показатели на едно място. Подробности за тези решения ще намерите на страницата за [автоматизация на бизнес процеси](/avtomatizacii/). [OWNER CONFIRM: кои счетоводни програми и таблици могат да се свържат]

## Как протича работата {#kak-rabotim}

Работата преминава през четири стъпки, които са едни и същи за магазина и за решенията към него.

1. **Безплатна диагностика и 30-минутен разговор.** Разглеждаме как продавате сега и къде губите време.
2. **Оферта.** Получавате оферта с приоритизирани решения и ясни еднократни цени.
3. **Изграждане.** Изграждаме магазина и избраните решения. Срокът зависи от решението и го посочваме в офертата.
4. **Поддръжка.** След пускането поддържаме изграденото и Ви изпращаме кратък месечен отчет. [OWNER CONFIRM: дали месечната поддръжка обхваща и поддръжката на самия магазин (обновления, поправки) и какво съдържа отчетът за магазин]

Изработването на онлайн магазин започва с този разговор. Диагностиката не Ви задължава с нищо.

[Запазете безплатна диагностика]({{BOOKING_URL}})

## Как се формира цената на онлайн магазина {#cena}

Цената на магазина е еднократна и зависи от това какво ще бъде изградено: самият магазин и решенията, които изберете към него. Посочваме я в офертата след безплатната диагностика, затова на тази страница няма цени. [OWNER CONFIRM: buyers expect a starting price for a shop; canon forbids any number or range, owner item only, no text change]

Цените са прозрачни и не подписвате дългосрочен договор. Работим по GDPR.

Ако имате въпрос преди разговора, пишете ни на {{EMAIL}}.

[Запазете час]({{BOOKING_URL}})

---

## FAQ

[[faq]]
q = "Колко струва изработката на онлайн магазин?"
a = "Цената е еднократна и зависи от това какво ще бъде изградено: магазинът и решенията, които изберете към него. Посочваме я в офертата, която получавате след безплатната диагностика."

[[faq]]
q = "Колко време отнема създаването на онлайн магазин?"
a = "Срокът зависи от решението и го посочваме в офертата. Той се определя от това какво включва магазинът и какви автоматизации добавяме към него."

[[faq]]
q = "Коя платформа за онлайн магазин използвате?"
a = "Платформата и начинът на изграждане са описани в офертата, след като обсъдим нуждите на магазина в диагностиката. [OWNER CONFIRM: answer depends on O1 (platforms used, who chooses); keep or rewrite after the owner's reply]"

[[faq]]
q = "Може ли магазинът да отговаря сам на въпроси за пратки?"
a = "Да. Свързваме асистент в чата с куриера и той отговаря на клиентите със статуса на пратката им. Когато асистентът не може да помогне, записва контакта на клиента, за да се свържете с него."

[[faq]]
q = "Ще се показва ли магазинът ми в Google?"
a = "Не обещаваме позиции в Google, защото те зависят от много фактори. Можем да подготвим SEO описания на продуктите и да поемем [работата по видимостта на сайта в Google](/seo-optimizacia/)."

[[faq]]
q = "Има ли поддръжка след пускането на магазина?"
a = "Да. След пускането поддържаме изградените решения и Ви изпращаме кратък месечен отчет. [OWNER CONFIRM: дали клиентът може сам да добавя и редактира продукти и дали има обучение; O6/O7]"

[[faq]]
q = "Обвързвам ли се с договор, ако запазя диагностика?"
a = "Не. Диагностиката не Ви задължава с нищо. След нея работим без дългосрочни договори и с прозрачни цени."

[[faq]]
q = "Работите ли и с вече съществуващ онлайн магазин?"
a = "Да. Към съществуващ магазин можем да добавим отговори за пратки, описания на продукти, напомняния за изоставени колички и връзка със счетоводството. Какво е възможно за Вашия магазин, уточняваме в диагностиката. [OWNER CONFIRM: O8, platforms on which automations can be added to a third-party shop]"

## CHANGE SUMMARY (5 lines)

1. Added title „Изработка на онлайн магазин с автоматизации | BizGrow“ (53) and meta description (155) with the main term; main term now once each in title, H1, first 100 words, one H2.
2. FAQ 3 question rewritten to „Коя платформа за онлайн магазин използвате?“ so the secondary term „платформа за онлайн магазин“ is visible; answer and its OWNER CONFIRM unchanged.
3. H2 #cena „Как се формира цената“ → „Как се формира цената на онлайн магазина“ (price query alignment; anchor `cena` unchanged; no number).
4. Sibling term „AI асистент“ de-flooded from 5 to 2 (bullet, #pratki para 1 and FAQ 4 now say „асистент в чата“; the term is explained once and kept as link anchor to /ai-asistent/).
5. Proposed ContentPage label/summary/eyebrow; nothing else changed: all CTAs, tokens, 4 body links + FAQ link, anchors, canon facts, the „на база типични случаи“ label and all 14 OWNER CONFIRM markers kept.

## INVENTORY DIFF (I1–I16)

| Item | Status | Where after Step 4 |
|---|---|---|
| I1 Booking CTA → `{{BOOKING_URL}}` | PRESENT, unchanged | #kak-rabotim „[Запазете безплатна диагностика]({{BOOKING_URL}})“; #cena „[Запазете час]({{BOOKING_URL}})“ |
| I2 `{{EMAIL}}` | PRESENT, unchanged | #cena „пишете ни на {{EMAIL}}“ |
| I3 /diagnostika/ | PRESENT, unchanged | #za-kogo „В [безплатната диагностика](/diagnostika/) изберете „Онлайн магазин“…“ |
| I4 builds online shops, nothing more specific | PRESENT, unchanged | lead „BizGrow предлага изработка на онлайн магазин…“; #kakvo-vklyuchva „Изграждаме самия магазин“; meta, summary |
| I5 courier-status AI, link /ai-asistent/ | PRESENT, same meaning | #pratki „Свързваме асистент в чата с куриера и той отговаря автоматично на клиента със статуса на пратката.“ + „Асистентът в чата (AI асистент) е автоматичен помощник…“ + link; FAQ 4 |
| I6 SEO descriptions for collections, own tool, approval, /seo-statii/ | PRESENT, unchanged | #opisania-na-produkti „Нашият собствен инструмент за съдържание пише SEO описания за цели колекции“; „Вие преглеждате и одобрявате всяко описание…“ |
| I7 abandoned-cart messages | PRESENT, unchanged | #izostaveni-kolichki „Настройваме автоматични съобщения, които напомнят на клиента за изоставената количка…“ |
| I8 connected systems, /avtomatizacii/ | PRESENT, unchanged | #poruchki-i-schetovodstvo „Свързваме програмите, които вече използвате (това се нарича интеграция)…“ |
| I9 free diagnosis + 30-minute call | PRESENT, unchanged | #kak-rabotim step 1 |
| I10 оферта, prioritised, one-off prices | PRESENT, unchanged | #kak-rabotim step 2; „доклад“ 0 |
| I11 build, no duration | PRESENT, unchanged | step 3 „Срокът зависи от решението и го посочваме в офертата.“; FAQ 2 |
| I12 monthly support + short report | PRESENT, unchanged | step 4; FAQ 6 |
| I13 price formation, no number | PRESENT, unchanged | #cena (H2 reworded only); FAQ 1 |
| I14 no long-term contracts, transparent prices | PRESENT, unchanged | #cena; FAQ 7 |
| I15 diagnosis commits to nothing | PRESENT, unchanged | #kak-rabotim; FAQ 7 |
| I16 „Работим по GDPR“ | PRESENT, verbatim | #cena |

## FLAGS

- OWNER CONFIRM: 14 inline markers (O1–O12), all carried unchanged from 03-humanised.md (#kakvo-vklyuchva 5, #za-kogo 1, #pratki 1, #izostaveni-kolichki 1, #poruchki-i-schetovodstvo 1, #kak-rabotim 1, #cena 1, FAQ 3, FAQ 6, FAQ 8). FAQ 3 question text changed, its marker (O1) unchanged.
- VERIFY 0 | DATA NEEDED 0 | LINK NEEDED 0 | new external facts 0.
- SEO notes for Step 5: (a) body links 4 vs the generic 1–3 guideline, kept by owner requirement; (b) FAQ 1 articled main-term variant is the price-query carrier, intentional; (c) label/summary/eyebrow are proposals for the ContentPage object and contain no main term of another address.
