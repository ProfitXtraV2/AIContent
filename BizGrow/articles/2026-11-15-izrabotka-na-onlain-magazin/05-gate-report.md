# 05-gate-report: /izrabotka-na-onlain-magazin/ (bg)

Input: 04-seo.md (PHASE 2: OPTIMISED PAGE). Rules read: pipeline/agents/brand-gate-bizgrow.md, pipeline/prompts/step-5-brand-gate.md, pipeline/markets/bg/author.md (BIZGROW CANON, voice, DE-AI, dictionary), pipeline/reference/site-rules.md, pipeline/reference/verification-policy.md, conversion-links.md, keyword-map.md (own row + siblings), 00-current.md, 00-inventory.md. Run-brief canon changes 2026-11-15 applied („оферта“ never „доклад“; no delivery periods; only the 30-minute call carries a duration; shop capabilities only in canon words; no platforms, payment/courier integrations, delivery times or prices).

## PHASE 1: SCORECARD (input = 04-seo.md)

```
BRAND COMPLIANCE SCORECARD — /izrabotka-na-onlain-magazin/ (bg)
Verdict: PASS WITH FIXES
Total: 89/100 (input) → 93/100 (after fixes)
Voice 18/20 | Language 14/15 | Trust & claims 16/20 | Usefulness 13/15 | Anti-AI 14/15 | SEO 14/15   (input)
Voice 19/20 | Language 15/15 | Trust & claims 18/20 | Usefulness 13/15 | Anti-AI 14/15 | SEO 14/15   (output)
```

### BLOCKING CHECKS

| # | Check | Result | Note |
|---|---|---|---|
| 1 | Nothing lost (I1–I16) | PASS | New page; all 16 required carriers present (table below). |
| 2 | Facts allowed list | FAIL → fixed | (a) FAQ 3 answer „Платформата и начинът на изграждане са описани в офертата…“ states a new fact about BizGrow (that the offer specifies a platform and build method). It is not canon and not current-page copy; an OWNER CONFIRM marker does not license new copy. Rewritten to canon wording (what will be built is clarified in the diagnosis and described in the offer with a one-off price); marker kept. (b) #izostaveni-kolichki „…според правила, договорени предварително с Вас.“ describes how the abandoned-cart service works beyond the canon words („automatic messages for abandoned carts“), against the run brief. Deleted. |
| 3 | Banned claims | PASS | No гарант*, №1, лидер, hype, prices, offers, testimonials. „безплатн*“ 6× all about the diagnosis. „не обещаваме“ (Google positions) is not a banned term and is the honest no-guarantee line. |
| 4 | Numbers | PASS | Visible figures: „30-минутен“ (canon call), step numbers 1–4, „четири стъпки“ (canon process). No delivery period, no hours, no percentages. Other digits only inside OWNER CONFIRM markers (O-refs). Checker hours referred to only as „ориентировъчно … на база типични случаи“, no figure. |
| 5 | Hypothetical label | N/A | No example scenarios or before/after rows on the page. |
| 6 | GDPR wording | PASS | „Работим по GDPR.“ verbatim, once (#cena). |
| 7 | Register | PASS | 0 „ти“ forms (the only „те“ is the plural pronoun „they“ in FAQ 5); 0 lowercase courtesy forms in direct address; 11 capitalised forms. FAQ questions in the buyer's 1st person („магазинът ми“, „Обвързвам ли се“) are correct. |
| 8 | CTA rules | PASS | 2 booking CTAs in different sections (#kak-rabotim „Запазете безплатна диагностика“, #cena „Запазете час“), both `{{BOOKING_URL}}`, approved wording; `{{EMAIL}}` once; no hard-coded URL/address; no urgency. |
| 9 | One term per page | PASS | „изработка на онлайн магазин“ once each in title, H1, lead sentence 1, H2 #kakvo-vklyuchva (+ meta). No sibling main term in title/H1/H2. „AI асистент“ (/ai-asistent/) 2× in body (explanation + link anchor), „автоматизация на бизнес процеси“ 1× as link anchor: passing mentions with links, allowed. |
| 10 | Links & anchors | PASS | /diagnostika/, /ai-asistent/, /seo-statii/, /avtomatizacii/ (body), /seo-optimizacia/ (FAQ 5): all in conversion-links.md. New page, new section ids; no EN pair. |
| 11 | BizGrow voice | PASS (moderate fixes) | No exclamation marks, no rhetorical questions, no slang, no hype; jargon explained (SEO, AI асистент/чат, интеграция, дашборд). Two moderate voice items fixed (see MODERATE). |

Criticals from 2(a) and 2(b) are mechanically fixable (rewrite within canon / delete non-canon detail), so the verdict is PASS WITH FIXES, not FAIL.

### CRITICAL (blocks until fixed)

1. FAQ 3 a: „Платформата и начинът на изграждане са описани в офертата, след като обсъдим нуждите на магазина в диагностиката.“ → check 2 (new BizGrow fact outside canon) → „Какво ще бъде изградено за Вашия магазин, уточняваме в безплатната диагностика и го описваме в офертата с ясна еднократна цена.“ OWNER CONFIRM marker (O1) kept verbatim.
2. #izostaveni-kolichki: „Настройваме автоматични съобщения, които напомнят на клиента за изоставената количка според правила, договорени предварително с Вас.“ → check 2 + run brief (shop capabilities only in canon words) → „Настройваме автоматични съобщения, които напомнят на клиента за изоставената количка.“ Channel marker kept.

### MODERATE

1. summary „…и добавяме към тях отговори за пратки…“ implies these solutions are always included, while the body says „когато има нужда“ → „…и можем да добавим към тях…“ (151 chars, one sentence). Label and eyebrow PASS („Онлайн магазин“, „Магазин и автоматизации“: no sibling main term, no number, no hype).
2. #za-kogo: two consecutive sentences opening on „има смисъл“ („Създаване на онлайн магазин има смисъл, когато… Има смисъл и когато…“) read as a repetitive advisory pattern → merged into one sentence with „или“; secondary term kept.
3. #kak-rabotim intro „…четири стъпки, които са едни и същи за магазина и за решенията към него.“ asserts more about the shop-build process than the canon says (service 6: nothing specific, no design process) → „Работата по магазина и по решенията към него преминава през четири стъпки.“ (raised as owner item G2).
4. meta description: comma before „с AI отговори“ breaks the phrase („за малкия бизнес, с AI отговори“) → comma removed; 154 chars, main term kept, no em-dash.
5. Not changed, noted: body links 4 vs the generic 1–3 guideline (owner required 3 + the inventory /diagnostika/ link; kept). „Повече подробности ще намерите…“ / „Подробности за тези решения ще намерите…“ repeat a pattern in two sections; acceptable, not rewritten.
6. Not changed, noted: „по всяко време на денонощието“ (#pratki) is the canon wording „around the clock“ describing what the assistant does, not a response-time guarantee; kept. Data-driven campaigns sentence in #izostaveni-kolichki and the document automation / dashboard sentence in #poruchki-i-schetovodstvo are canon (checker „Кампании на база данни“; service 1) but lie outside the four shop capabilities the run brief lists → kept, raised as owner item G1.

### VERIFIED CLEAN (input)

Em-dashes/en-dashes 0; „доклад“ 0; delivery periods 0; prices / price ranges 0; platforms, payment methods, courier names, hosting/domain claims 0 in visible text (only inside OWNER CONFIRM markers); signposting, „не A, а B“ endings, „освен това“/„в заключение“/„именно“/„точно“ 0; boilerplate 0; title 53 chars incl. „ | BizGrow“; meta 155 → 154.

### INVENTORY CHECK (after fixes)

| Item | Status | Where |
|---|---|---|
| I1 booking CTA | PRESENT | #kak-rabotim „Запазете безплатна диагностика“; #cena „Запазете час“ |
| I2 `{{EMAIL}}` | PRESENT | #cena |
| I3 /diagnostika/ | PRESENT | #za-kogo |
| I4 builds online shops, nothing specific | PRESENT | lead, #kakvo-vklyuchva, meta, summary |
| I5 courier-connected assistant + /ai-asistent/ | PRESENT | #kakvo-vklyuchva bullet, #pratki, FAQ 4 |
| I6 SEO descriptions for collections, own tool, approval + /seo-statii/ | PRESENT | #opisania-na-produkti |
| I7 automatic abandoned-cart messages | PRESENT (detail trimmed to canon) | #izostaveni-kolichki |
| I8 connected systems + /avtomatizacii/ | PRESENT | #poruchki-i-schetovodstvo |
| I9 free diagnosis + 30-minute call | PRESENT | step 1 |
| I10 оферта, prioritised, one-off prices | PRESENT | step 2 |
| I11 build, no duration, canon timing line | PRESENT | step 3; FAQ 2 |
| I12 monthly support + short report | PRESENT | step 4; FAQ 6 |
| I13 price formation, no number | PRESENT | #cena; FAQ 1 |
| I14 no long-term contracts, transparent prices | PRESENT | #cena; FAQ 7 |
| I15 diagnosis commits to nothing | PRESENT | #kak-rabotim; FAQ 7 |
| I16 „Работим по GDPR“ | PRESENT | #cena |

### OWNER ITEMS TO RAISE (for Step 6)

Carried from the inline markers (14 markers, 12 items; none removed or resolved):
- O1 Platform for the shops (ready platform or own build), and whether chosen with the client (#kakvo-vklyuchva; FAQ 3).
- O2 Payment methods set up in the shop (card, cash on delivery, bank transfer).
- O3 Courier connections beyond the parcel-status answer (shipping calculation, waybills) and which couriers.
- O4 Domain, hosting, SSL: who provides them and in whose name the shop and accounts stay.
- O5 Design, mobile view, number of revisions, migrating products from an existing shop.
- O6/O7 Whether the client can add/edit products alone and whether training is given (FAQ 6).
- O8 Whether automations are added to a shop built by someone else, and on which platforms (#za-kogo; FAQ 8).
- O9 Which couriers the assistant connects to, and whether it also answers in the shop's own site chat (#pratki).
- O10 Channel of abandoned-cart reminders (email, SMS, Messenger) (#izostaveni-kolichki).
- O11 Which accounting programs and spreadsheets can be connected (#poruchki-i-schetovodstvo).
- O12 Whether monthly support covers maintaining the shop itself (updates, fixes) and what the shop report contains (#kak-rabotim).
- Price expectation: buyers expect a starting price; canon forbids any number or range; owner decision only, no text change (#cena).

Added by the gate (report only, no inline marker added):
- G1 Confirm that the shop page may mention data-driven campaigns („кампании според това кой какво купува и кога се връща“), document automation and a dashboard: canon capabilities, but outside the four shop capabilities named in the 2026-11-15 run brief.
- G2 Confirm that the four-step process (diagnosis → offer → build → support with a monthly report) applies to building the shop itself, not only to the automations (canon service 6 says nothing about the shop-build process).

Total owner items: 14 (12 carried + 2 gate).

### VOICE NOTES (protect in Step 6)

- Calm explanatory pattern per section: the owner's task first, then what BizGrow sets up, then the plain-word explanation of the term (SEO, асистент в чата, интеграция, дашборд). Keep the explanations.
- The honest no-ranking line („не обещаваме конкретно място в резултатите“, FAQ 5) is the page's guarantee-safe position; keep its wording, never turn it into a positive promise.
- „Срокът зависи от решението и го посочваме в офертата.“ is verbatim canon; never replace with a period.
- Owner word „асистент в чата“ over „AI асистент“ (sibling main term) is intentional SEO; keep.

## PHASE 2: FIXED PAGE

title = "Изработка на онлайн магазин с автоматизации | BizGrow"  (53 chars incl. " | BizGrow")
meta_description = "Изработка на онлайн магазин за малкия бизнес с AI отговори за пратки, SEO описания на продукти и напомняния за колички. Започнете с безплатна диагностика."  (154 chars)
label = "Онлайн магазин"
summary = "Изграждаме онлайн магазини за малки бизнеси и можем да добавим към тях отговори за пратки, SEO описания на продукти и напомняния за изоставени колички."
eyebrow = "Магазин и автоматизации"
primary_keyword = "изработка на онлайн магазин"
secondary_keywords = ["създаване на онлайн магазин", "изработка на онлайн магазин цена", "изработване на онлайн магазин", "платформа за онлайн магазин"]

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

Работим с малки бизнеси, които продават стоки: онлайн магазини, както и магазини и шоуруми, които искат да продават и през интернет. Създаване на онлайн магазин има смисъл, когато клиентите Ви вече търсят продуктите Ви онлайн или когато поръчките по телефон и в съобщения отнемат твърде много време.

Ако вече имате онлайн магазин, трудността често е в повтарящата се работа около поръчките. В [безплатната диагностика](/diagnostika/) изберете „Онлайн магазин“ и отбележете проблемите, които познавате. Ще видите ориентировъчно колко часа седмично отиват за тях, изчислени на база типични случаи. След това можете да запазите разговор. [OWNER CONFIRM: дали автоматизациите се добавят и към магазин, изработен от друг, и на кои платформи]

## Автоматични отговори на въпроса „Къде ми е поръчката?“ {#pratki}

В онлайн магазина едни и същи въпроси за пратките идват всеки ден и отнемат време на човека, който проверява и отговаря. Свързваме асистент в чата с куриера и той отговаря автоматично на клиента със статуса на пратката.

Асистентът в чата (AI асистент) е автоматичен помощник, който отговаря на клиентите в Messenger, Instagram или WhatsApp по всяко време на денонощието. Когато не може да помогне, той записва контакта на клиента, за да можете да се свържете с него. Повече подробности ще намерите на страницата за [AI асистента](/ai-asistent/). [OWNER CONFIRM: с кои куриери се свързва асистентът и дали отговаря и в чат на самия магазин]

## SEO описания на продукти за цели колекции {#opisania-na-produkti}

Когато в магазина влизат много нови продукти, описанията им често остават за по-късно или се пишат ръчно едно по едно. Нашият собствен инструмент за съдържание пише SEO описания за цели колекции. SEO описанието е текст, подготвен така, че търсачки като Google по-лесно да разберат какво продавате.

Вие преглеждате и одобрявате всяко описание, преди да бъде публикувано. Позицията на магазина в Google зависи от много фактори, затова не обещаваме конкретно място в резултатите. Как работи инструментът, можете да видите на страницата за [SEO статии и описания](/seo-statii/).

## Напомняния за изоставени колички {#izostaveni-kolichki}

Част от клиентите добавят продукти в количката и затварят страницата, без да завършат поръчката. Ако никой не им напомни, тези поръчки обикновено остават незавършени.

Настройваме автоматични съобщения, които напомнят на клиента за изоставената количка. [OWNER CONFIRM: по какъв канал се изпращат напомнянията (имейл, SMS, Messenger)] Със същите данни за покупките могат да се подготвят и кампании според това кой какво купува и кога се връща.

## Поръчки, таблици и счетоводство без ръчно копиране {#poruchki-i-schetovodstvo}

В много магазини едни и същи данни се прехвърлят ръчно от поръчките в таблица и след това в счетоводството. Свързваме програмите, които вече използвате (това се нарича интеграция), и данните се попълват сами, без копиране.

Към това можем да добавим автоматизация на документите и табло (дашборд) с основните показатели на едно място. Подробности за тези решения ще намерите на страницата за [автоматизация на бизнес процеси](/avtomatizacii/). [OWNER CONFIRM: кои счетоводни програми и таблици могат да се свържат]

## Как протича работата {#kak-rabotim}

Работата по магазина и по решенията към него преминава през четири стъпки.

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
a = "Какво ще бъде изградено за Вашия магазин, уточняваме в безплатната диагностика и го описваме в офертата с ясна еднократна цена. [OWNER CONFIRM: answer depends on O1 (platforms used, who chooses); keep or rewrite after the owner's reply]"

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

## FIXES APPLIED (6)

1. FAQ 3 answer rewritten to canon wording (critical, check 2); O1 marker kept verbatim.
2. #izostaveni-kolichki: non-canon detail „според правила, договорени предварително с Вас“ deleted (critical, check 2 / run brief).
3. summary: „добавяме към тях“ → „можем да добавим към тях“ (accuracy; matches body „когато има нужда“).
4. #za-kogo: two „има смисъл“ sentences merged into one (voice).
5. #kak-rabotim intro: „…четири стъпки, които са едни и същи за магазина и за решенията към него“ → „Работата по магазина и по решенията към него преминава през четири стъпки.“ (no process claim beyond canon; G2).
6. meta description: comma before „с AI отговори“ removed (155 → 154 chars).

Nothing added: no new fact, number, link, CTA or flag text. Nothing removed from the inventory; no marker removed or resolved; all anchors, tokens, CTAs and links unchanged.

## FLAGS (after gate)

- OWNER CONFIRM: 14 inline markers (unchanged count and wording): #kakvo-vklyuchva 5, #za-kogo 1, #pratki 1, #izostaveni-kolichki 1, #poruchki-i-schetovodstvo 1, #kak-rabotim 1, #cena 1, FAQ 3, FAQ 6, FAQ 8.
- VERIFY 0 | DATA NEEDED 0 | LINK NEEDED 0 | new external facts 0.
- Gate owner items (report only): G1, G2.
- CANON ADDITIONS: none.
