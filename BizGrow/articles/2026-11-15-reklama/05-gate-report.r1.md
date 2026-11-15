# 05-gate-report: /reklama/ (bg, new-page)

Inputs read: 00-current.md, 00-inventory.md, 00-brief.md (owner instructions), 04-seo.md, keyword-map.md (row /reklama/ + siblings), conversion-links.md, pipeline/markets/bg/author.md (canon, voice, de-AI rules), pipeline/reference/site-rules.md, pipeline/reference/verification-policy.md.

## PHASE 1: EVALUATION

```
BRAND COMPLIANCE SCORECARD — /reklama/ (bg)
Verdict: PASS WITH FIXES
Total (before fixes): 89/100  |  Total (after fixes): 93/100
Before: Voice 18/20 | Language 14/15 | Trust & claims 16/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 13/15
After:  Voice 18/20 | Language 14/15 | Trust & claims 19/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 14/15
```

### BLOCKING CHECKS

| # | check | result | note |
|---|---|---|---|
| 1 | NOTHING LOST (new page: every 00-inventory item present) | PASS | I1–I19 all present with the same meaning (table below). |
| 2 | FACTS ALLOWED LIST | FAIL → fixed (mechanical) | Two statements about how BizGrow works that are not in the canon: (a) #facebook-instagram „При планирането **заедно с Вас** се решава…“ (claims the client co-decides the channels); (b) #diagnostika „…и къде губите време **или пари**“ (canon: the diagnosis finds where the business loses time). Both deleted, nothing added; (a) raised as an owner item. |
| 3 | BANNED CLAIMS | PASS | No „гарантир*/гаранци*“, „№1“, „лидер“, „най-добрите“; „безплатн*“ only for the diagnosis (8 uses, all diagnosis); no price, offer („отстъпки“ from the owner copy was correctly rendered as „оферти“), testimonial or hype word. „най-горното място“ appears only in FAQ 2 as the sourced statement that a higher amount does not assure it (Google's own wording, not a BizGrow claim). |
| 4 | NUMBERS | PASS | Only canon figures: 30 минути, 48 часа, „обикновено до 2 седмици“, plus „четири стъпки“ (the canon's 4-step process). No digit before лв/евро/€. |
| 5 | HYPOTHETICAL LABEL | N/A | No example scenario on the page. The #za-kogo situations are the owner's own pain wording, not example results. |
| 6 | GDPR WORDING | PASS | „Работим по GDPR.“ only (#cena). |
| 7 | REGISTER | PASS | 0 „ти“ forms (scripted scan: no 2nd-sg -иш/-еш verbs, no твой*/теб/те/ти, no singular imperatives); 0 lowercase ви/вас/ваш/вие. FAQ questions use the owner's own 1st person („Ако платя повече…“), which is correct. |
| 8 | CTA RULES | PASS | 2 booking CTAs, one per section (#proces „Запазете безплатна диагностика“, #diagnostika „Запазете час“), both `{{BOOKING_URL}}`; `{{EMAIL}}` token once; no hard-coded URL/address; no urgency. |
| 9 | ONE TERM PER PAGE | PASS | Main term „реклама в гугъл“ (keyword-map): title (exact, „Гугъл“), H1 (keyword-map H1, Latin variant „Google“), lead sentence 1 (exact), H2 #kak-raboti (exact). No sibling main term in title/H1/H2. „SEO оптимизация на сайтове“ and „поддръжка на социални мрежи и криейтиви“ appear only as link anchors (the pages' names in conversion-links.md). Sibling secondaries „реклама в социалните мрежи“, „рекламни визии“ absent. |
| 10 | LINKS & ANCHORS | PASS | /seo-optimizacia/, /socialni-mrezhi/ (×2), /diagnostika/: all in conversion-links.md. 8 new section ids, no EN pair. |
| 11 | BIZGROW VOICE | PASS | No fragments as style, no rhetorical questions in body, no verdict lines, no slang, no hype, no exclamation marks. Jargon glossed on first use: Google Ads, кампания, PPC, ключови думи, рекламен ранг, SEO, B2B. |

Deliverable constraints (task): H2 sections 8 (6–8 ✓) | FAQ 8 (6–8 ✓) | title 59 chars incl. „ | BizGrow“ (≤ 60 ✓, no em-dash) | meta 148 chars (120–160 ✓, main term at start, no em-dash) | per-section structure: paragraphs first, then at most one list ✓ (#proces: paragraph + CTA line + one numbered list; CTA is a paragraph-level link) | inline syntax only `**bold**` and `[label](path)` ✓ (CTAs use `[label]({{BOOKING_URL}})` per site-rules §8). Em-dashes in copy: 0; the only „—“ characters sit inside `[VERIFY: … — URL]` markers, which Step 6 removes.

### CRITICAL (blocks until fixed)
1. „При планирането заедно с Вас се решава дали да използвате само един от тези канали или комбинация от тях.“ → check 2 (client co-decision is not in the canon; canon: the specialist plans) → delete „заедно с Вас“ → „При планирането се решава дали да използвате само един от тези канали или комбинация от тях.“ + owner item.
2. „…какво Ви носи рекламата и къде губите време или пари.“ → check 2 (canon: the diagnosis finds where the business loses time) → delete „или пари“.

### MODERATE (not changed; noted)
- „какво връща всяко вложено евро“ appears in lead, #specialist, #otchet, FAQ 4 and summary. Canon I6 wording, so kept; the repetition is acceptable on a service page but should not grow in later edits.
- #cena: two consecutive sentences start with „Работим“. Minor rhythm point; left as is to keep the owner's exact GDPR wording as its own sentence.
- H1 uses „Google“ while the title uses „Гугъл“. Keyword-map H1 kept; already an owner item from Step 4.
- #proces renders the 4 steps as a numbered Markdown list; the porter maps it to `bullets[]` of the ContentPage section.

### OWNER ITEMS TO RAISE (for Step 6)
Carried unchanged from earlier stages:
1. `[VERIFY]` F1: Google Ads charges the advertiser only when someone clicks (https://support.google.com/google-ads/answer/6227565?hl=bg). #kak-raboti, #cena, FAQ 1, FAQ 3.
2. `[VERIFY]` F2: the advertiser decides the average daily amount (same URL). #kak-raboti, #cena, FAQ 1.
3. `[VERIFY]` F3: placement depends on competition and ad rank; a higher amount does not assure placement (https://support.google.com/google-ads/answer/2472742?hl=bg). #kak-raboti, FAQ 2.
4. `[OWNER CONFIRM]` Pricing model of the specialist's ongoing work vs canon „еднократна цена за всяко решение“. #cena.
5. `[OWNER CONFIRM]` Is the ad budget paid to Google/Meta separate from BizGrow's fee? #cena, FAQ 1 (no claim in text).
6. `[OWNER CONFIRM]` Title uses Cyrillic „Гугъл“ (exact search term) while the H1 keeps the keyword-map „Google“; label „Реклама в Google и Facebook“, summary and eyebrow „Маркетинг специалист“.
7. `[DATA NEEDED]` Whose ad account is used (the client's own Google Ads / Meta account or BizGrow's).
8. `[DATA NEEDED]` Minimum ad budget; tools used for tracking; time to first results.
New from this gate:
9. `[OWNER CONFIRM]` Does the client take part in choosing the channels (Google, Facebook, Instagram) at the planning stage? The phrase „заедно с Вас“ was removed as non-canon; it can return if the owner confirms.
10. `[OWNER CONFIRM]` Scope of the free diagnosis for this service: the page says the call covers „как рекламирате сега, какво Ви носи рекламата и къде губите време“ and the business's „досегашната Ви реклама“. Canon says only „безплатна диагностика и 30-минутен разговор“ that finds where the business loses time; confirm the ads-specific scope wording.

### VOICE NOTES (protect during later edits)
- Lead sentence 1 states the offer with the exact main term; keep it first.
- Glosses „тоест …“ explain each term once; do not add more.
- FAQ 8 answers the "how fast are results" question without a promise („срок за резултати от самите реклами не обещаваме предварително“); keep it free of any time figure.
- „оферти“ (not „отстъпки“) in #za-kogo is deliberate: „отстъпк*“ is a banned OFFER term.

### INVENTORY DIFF (00-inventory.md vs page after fixes)

| item | status | where |
|---|---|---|
| I1 booking CTA, formal imperative, max one per section | PASS | #proces „Запазете безплатна диагностика“; #diagnostika „Запазете час“ |
| I2 `{{EMAIL}}` | PASS | #diagnostika |
| I3 link /diagnostika/ | PASS | #proces step 1 |
| I4 real specialist plans, runs, tracks | PASS | lead, #specialist, FAQ 5, summary |
| I5 reports with numbers | PASS | lead, #otchet, FAQ 4, meta |
| I6 what each invested euro returns | PASS | lead, #specialist, #otchet, FAQ 4, summary |
| I7 takes over planning/execution; report, not tasks | PASS | #specialist („поема планирането и изпълнението, а при Вас остава отчетът“; „без да Ви прехвърля задачи“) |
| I8 data-driven campaigns | PASS | #specialist bullet 4 |
| I9 Google Ads + Facebook/Instagram | PASS | lead, #kak-raboti, #facebook-instagram, FAQ 1/3/6 |
| I10 creatives every month → /socialni-mrezhi/ | PASS | #facebook-instagram, FAQ 5 |
| I11 free diagnosis + 30-minute call | PASS | #proces step 1, FAQ 8 |
| I12 report within 48 h, one-off prices, no number | PASS | #proces step 2, #cena, FAQ 8, meta |
| I13 build „обикновено до 2 седмици“ | PASS | #proces step 3, FAQ 8 |
| I14 monthly support + short monthly report | PASS | #proces step 4, #otchet, FAQ 4 |
| I15 no long-term contracts | PASS | #cena, FAQ 7 |
| I16 transparent prices, formation, no number | PASS | #cena, FAQ 1 |
| I17 „Работим по GDPR“ | PASS | #cena |
| I18 diagnosis commits to nothing | PASS | lead, #cena, FAQ 7 |
| I19 example label | N/A | no example scenario |

**INVENTORY DIFF: PASS (18/18 applicable present, I19 n/a).** Flags: 5 inline markers + 2 DATA NEEDED carried unchanged; 2 new owner items added. No flag removed, no fact or number added.

## PHASE 2: FIXES APPLIED

1. #facebook-instagram: „При планирането заедно с Вас се решава…“ → „При планирането се решава…“ (non-canon co-decision removed; owner item 9).
2. #diagnostika: „…и къде губите време или пари.“ → „…и къде губите време.“ (aligned to canon wording; owner item 10).

No other change. Title, meta, label, summary, eyebrow, FAQ, CTAs, tokens, links, section ids and flags are as in 04-seo.md.

---

## FULL ARTICLE AFTER FIXES

Page: /reklama/ | Locale: bg | Type: new-page | Main term: реклама в гугъл

META
- title: „Реклама в Гугъл и Facebook с маркетинг специалист | BizGrow“ (59 characters)
- meta_description: „Реклама в Гугъл, Facebook и Instagram, която маркетинг специалист планира, пуска, следи и отчита с числа. Безплатна диагностика и доклад до 48 часа.“ (148 characters)

CONTENTPAGE FIELDS
- label: „Реклама в Google и Facebook“
- summary: „Кампании в Google Ads, Facebook и Instagram, които маркетинг специалист планира, пуска и следи, като Ви показва какво връща всяко вложено евро.“
- eyebrow: „Маркетинг специалист“
- service (schema name): „Реклама в Google и Facebook“
- related: /socialni-mrezhi/, /seo-optimizacia/, /diagnostika/

# Реклама в Google и Facebook с маркетинг специалист

Предлагаме реклама в Гугъл, Facebook и Instagram, която жив маркетинг специалист планира, пуска и следи вместо Вас. Той отговаря пред Вас с числа и Ви показва какво връща всяко вложено евро. Първата стъпка е безплатна диагностика, която не Ви обвързва с нищо.

## Какво прави маркетинг специалистът {#specialist}

Маркетинг специалистът на BizGrow е реален човек, който поема рекламата на Вашия бизнес от планирането до отчета. Той работи с кампании, като кампания означава една реклама или група реклами с обща цел и бюджет. Специалистът поема планирането и изпълнението, а при Вас остава отчетът с резултатите.

- **Планиране.** Специалистът планира в кои канали да се показва рекламата: Google, Facebook, Instagram или няколко от тях.
- **Настройка и пускане.** Подготвя и пуска кампаниите, без да Ви прехвърля задачи по тях.
- **Проследяване.** Следи резултатите на кампаниите и Ви показва какво връща всяко вложено евро.
- **Кампании на база данни.** Насочва кампаниите според това кой какво купува, кога се връща и какво е подходящо да му предложите.

## Как работи рекламата в Гугъл за малък бизнес {#kak-raboti}

Google Ads е рекламната платформа на Google, чрез която бизнесите пускат платени реклами. Google таксува рекламодателя само когато някой кликне върху рекламата. [VERIFY: Google Ads таксува рекламодателя само при клик върху рекламата — https://support.google.com/google-ads/answer/6227565?hl=bg] Затова този вид Гугъл реклама често се нарича PPC реклама, от английското „pay per click“, тоест плащане на клик.

Вие решавате каква средна сума да се изразходва за рекламата всеки ден, тоест какъв да бъде дневният бюджет. [VERIFY: рекламодателят решава средната дневна сума — https://support.google.com/google-ads/answer/6227565?hl=bg] При настройката на кампанията се избират ключови думи, тоест думите, които хората пишат в търсачката, когато търсят дадена услуга или продукт.

Мястото, на което се показва рекламата, не зависи само от сумата. Според Google то зависи от конкуренцията с други рекламодатели и от рекламния ранг, тоест оценката, която Google дава на всяка реклама при показването ѝ. По-високата сума сама по себе си не осигурява определено място. [VERIFY: мястото зависи от конкуренцията и рекламния ранг; по-високата сума не осигурява място — https://support.google.com/google-ads/answer/2472742?hl=bg]

Позициите в неплатените резултати на Google са отделна работа, която не се плаща на клик. С тях се занимава услугата [SEO оптимизация на сайтове](/seo-optimizacia/), тоест подобряване на сайта, така че търсачката да го показва в обикновените резултати.

## Реклама във Facebook и Instagram {#facebook-instagram}

Освен в Google, маркетинг специалистът планира и пуска реклама във Facebook и Instagram. При планирането се решава дали да използвате само един от тези канали или комбинация от тях.

Рекламите имат нужда от визии и текстове. Брандирани визии, публикации и рекламни материали можем да подготвяме всеки месец, без да Ви е нужен дизайнер на щат. Повече за това ще намерите на страницата [поддръжка на социални мрежи и криейтиви](/socialni-mrezhi/).

## За кои бизнеси е подходящо {#za-kogo}

Услугата е подходяща, ако сте пускали онлайн реклама „да видим дали ще стане“ и все още не знаете какво Ви е донесла. Подходяща е и когато пускате оферти към клиентите без ясен план и не знаете кои от тях ги връщат при Вас. Ако нямате време да планирате маркетинга, специалистът поема тази работа. Услугата е предназначена за малки бизнеси като:

- онлайн магазини;
- търговски обекти и шоуруми;
- B2B компании, които продават на други фирми;
- салони за красота;
- агенции за недвижими имоти;
- ресторанти и кафенета.

## Как разбирате какво Ви носи рекламата {#otchet}

Маркетинг специалистът отговаря пред Вас с числа. Той настройва кампаниите и Ви показва какво връща всяко вложено евро, така че да виждате кои кампании си струва да продължат и кои е по-добре да се променят.

След изграждането следва месечна поддръжка, за която получавате кратък месечен отчет. Така знаете какво е свършено през месеца, без да следите сами всяка реклама.

## Как започва работата {#proces}

Работата започва с безплатна диагностика и минава през четири стъпки. Цените научавате още в доклада, преди да решите дали да продължите.

[Запазете безплатна диагностика]({{BOOKING_URL}})

1. **Безплатна диагностика.** Започваме с безплатна диагностика и 30-минутен разговор за Вашия бизнес и досегашната Ви реклама. Можете да започнете и от страницата [безплатна диагностика](/diagnostika/).
2. **Доклад до 48 часа.** До 48 часа получавате доклад с приоритизирани решения и ясни еднократни цени.
3. **Изграждане.** Изграждаме и настройваме решенията от доклада, обикновено до 2 седмици.
4. **Поддръжка.** Следва поддръжка, за която всеки месец получавате кратък отчет.

## Как се формира цената {#cena}

Цените ни са прозрачни: получавате ги в доклада след безплатната диагностика, като ясна еднократна цена за всяко решение. Цената зависи от това какво ще изградим за Вашия бизнес. [OWNER CONFIRM: pricing model of the specialist's ongoing work vs canon „еднократна цена за всяко решение“] Работим без дългосрочни договори, а самата диагностика не Ви обвързва с нищо. Работим по GDPR.

От страна на Google Вие решавате средната дневна сума за рекламата, а Google таксува при клик върху рекламата. [VERIFY: рекламодателят решава средната дневна сума; таксуване само при клик — https://support.google.com/google-ads/answer/6227565?hl=bg] [OWNER CONFIRM: is the ad budget paid to Google/Meta separate from BizGrow's fee? owner item only, no claim in text]

## Запазете безплатна диагностика {#diagnostika}

На безплатната диагностика ще разгледаме как рекламирате сега, какво Ви носи рекламата и къде губите време. Можете да запазите час директно или да ни пишете на {{EMAIL}}.

[Запазете час]({{BOOKING_URL}})

---

## FAQ

1. **q:** Колко струва рекламата в Google Ads?
   **a:** В Google Ads Вие решавате средната дневна сума, а Google таксува само при клик върху рекламата. [VERIFY: F1/F2 — https://support.google.com/google-ads/answer/6227565?hl=bg] Цената на нашата работа получавате в доклада след безплатната диагностика и тя зависи от това какво ще изградим. [OWNER CONFIRM: is the ad budget paid to Google/Meta separate from BizGrow's fee? owner item only, no claim in text]

2. **q:** Ако платя повече, ще се показва ли рекламата ми най-отгоре?
   **a:** По-високата сума сама по себе си не осигурява най-горното място. Според Google мястото на рекламата зависи от конкуренцията с други рекламодатели и от рекламния ранг. [VERIFY: F3 — https://support.google.com/google-ads/answer/2472742?hl=bg]

3. **q:** Какво е PPC реклама?
   **a:** PPC идва от английското „pay per click“, тоест плащане на клик. При Google Ads рекламодателят плаща само когато някой кликне върху рекламата. [VERIFY: F1 — https://support.google.com/google-ads/answer/6227565?hl=bg]

4. **q:** Как ще видя дали рекламата ми носи клиенти?
   **a:** Маркетинг специалистът отговаря пред Вас с числа и Ви показва какво връща всяко вложено евро. По време на поддръжката получавате и кратък месечен отчет.

5. **q:** Кой подготвя визиите за рекламите?
   **a:** Брандирани визии и рекламни материали можем да подготвяме всеки месец. Повече за това ще намерите на страницата [поддръжка на социални мрежи и криейтиви](/socialni-mrezhi/). Самите кампании планира, пуска и следи жив маркетинг специалист.

6. **q:** По-добре ли е да рекламирам в Google или във Facebook и Instagram?
   **a:** Това се решава при планирането, след като специалистът разгледа Вашия бизнес. Той планира и пуска реклами и в Google, и във Facebook и Instagram, така че можете да използвате един канал или няколко.

7. **q:** Трябва ли да подпиша дългосрочен договор?
   **a:** Не, работим без дългосрочни договори, а безплатната диагностика не Ви обвързва с нищо.

8. **q:** Колко време отнема, докато започнем?
   **a:** Започваме с безплатна диагностика и 30-минутен разговор, след което до 48 часа получавате доклад с приоритизирани решения и цени. Изграждането обикновено отнема до 2 седмици, а срок за резултати от самите реклами не обещаваме предварително.

---

## FLAGS (all carried; none resolved)

Inline:
- `[VERIFY]` F1 (charge on click): #kak-raboti, #cena, FAQ 1, FAQ 3.
- `[VERIFY]` F2 (advertiser decides the average daily amount): #kak-raboti, #cena, FAQ 1.
- `[VERIFY]` F3 (placement depends on competition and ad rank; a higher amount does not assure placement): #kak-raboti, FAQ 2.
- `[OWNER CONFIRM]` Pricing model of the specialist's ongoing work vs canon „еднократна цена за всяко решение“: #cena.
- `[OWNER CONFIRM]` Ad budget paid to Google/Meta separate from BizGrow's fee: #cena, FAQ 1.

Owner items, not in the text:
- `[OWNER CONFIRM]` Title „Гугъл“ vs H1 „Google“; label, summary, eyebrow.
- `[DATA NEEDED]` Whose ad account is used (client's own Google Ads / Meta account or BizGrow's).
- `[DATA NEEDED]` Minimum ad budget; tools used for tracking; time to first results.
- `[OWNER CONFIRM]` (new, Step 5) Does the client take part in choosing the channels at planning? („заедно с Вас“ removed as non-canon.)
- `[OWNER CONFIRM]` (new, Step 5) Ads-specific scope of the free diagnosis („как рекламирате сега, какво Ви носи рекламата“, „досегашната Ви реклама“) vs canon „безплатна диагностика и 30-минутен разговор“.

New external facts this step: none (sourced facts stay at 3). Canon additions: none.
