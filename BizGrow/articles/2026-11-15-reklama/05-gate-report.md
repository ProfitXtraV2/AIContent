# 05-gate-report: /reklama/ (bg, new-page) · fix loop 1 (gate on 04-seo r2, after the Step 4 F1 re-run)

Inputs read: 00-current.md, 00-inventory.md, 00-brief.md (owner instructions), 04-seo.md (r2), keyword-map.md (row /reklama/ + siblings), conversion-links.md, pipeline/markets/bg/author.md (canon, voice, de-AI rules), pipeline/reference/site-rules.md, pipeline/reference/verification-policy.md; 05-gate-report.r1.md for continuity (owner items carried; its two check-2 defects recur in 04-seo r2 and get the same fixes). The current text was judged on its own.

## PHASE 1: EVALUATION

```
BRAND COMPLIANCE SCORECARD — /reklama/ (bg)
Verdict: PASS WITH FIXES
Total (before fixes): 89/100  |  Total (after fixes): 94/100
Before: Voice 18/20 | Language 14/15 | Trust & claims 16/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 13/15
After:  Voice 18/20 | Language 14/15 | Trust & claims 20/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 14/15
```

Trust & claims after fixes is higher than in r1 (19 → 20): the F1 sentences now match what the source supports (the CPC condition), so no sourced statement claims more than Google says.

### BLOCKING CHECKS

| # | check | result | note |
|---|---|---|---|
| 1 | NOTHING LOST (new page, every 00-inventory item) | PASS | I1–I18 present with the same meaning; I19 n/a (diff below). |
| 2 | FACTS ALLOWED LIST | FAIL → fixed (mechanical) | Same two non-canon statements as r1, still present in 04-seo r2: (a) #facebook-instagram „При планирането **заедно с Вас** се решава…“ (client co-decision not in canon; canon: the specialist plans); (b) #diagnostika „…къде губите време **или пари**“ (canon: the diagnosis finds where the business loses time). Both deleted, nothing added. |
| 3 | BANNED CLAIMS | PASS | 0 „гарант*“, „№1“, „лидер“, „най-добр*“, „промоц*“, „отстъп*“; „безплатн*“ 11×, all about the diagnosis; no price, testimonial or hype word. „най-горното място“ only in FAQ 2 as the sourced statement that a higher amount does not assure it. |
| 4 | NUMBERS | PASS | Only canon figures: 30 минути, 48 часа, „обикновено до 2 седмици“, „четири стъпки“ (canon 4-step process). „CPC“ adds no figure. |
| 5 | HYPOTHETICAL LABEL | N/A | No example scenario. |
| 6 | GDPR WORDING | PASS | „Работим по GDPR.“ only (#cena). |
| 7 | REGISTER | PASS | Scripted scan: 0 „ти“ forms (no -иш/-еш/-аш 2nd-sg verbs, no твой*/теб/те/ти), 0 lowercase ви/вас/ваш/вие. FAQ questions in the owner's 1st person are correct. |
| 8 | CTA RULES | PASS | `{{BOOKING_URL}}` ×2, one per section (#proces „Запазете безплатна диагностика“, #diagnostika „Запазете час“); `{{EMAIL}}` ×1; no hard-coded URL/address; no urgency. |
| 9 | ONE TERM PER PAGE | PASS | „реклама в гугъл“: title (exact), H1 (keyword-map H1, „Google“ variant), lead sentence 1 (exact), one H2 (#kak-raboti). No sibling main term in title/H1/H2; sibling page names appear only as link anchors. |
| 10 | LINKS & ANCHORS | PASS | /seo-optimizacia/, /socialni-mrezhi/ (×2), /diagnostika/, all in conversion-links.md. 8 new section ids; no EN pair. |
| 11 | BIZGROW VOICE | PASS | No fragments as style, no rhetorical questions in body (all 8 „?“ are FAQ questions; 2 more sit inside OWNER CONFIRM markers), no verdict lines, slang, hype or exclamation marks. Jargon glossed: Google Ads, кампания, CPC („цена на кликване“), PPC, ключови думи, рекламен ранг, SEO, B2B. |

**F1 / CPC check (task-specific): PASS.** Every sentence stating that Google charges only on a click carries the CPC condition:
- #kak-raboti: „При оферирането за цена на кликване (CPC) Google таксува рекламодателя само когато някой кликне върху рекламата.“
- #cena: „…, а при оферирането за цена на кликване (CPC) Google таксува само при клик върху рекламата.“
- FAQ 1: „…, а при оферирането за цена на кликване (CPC) Google таксува само при клик върху рекламата.“
- FAQ 3: „При оферирането за цена на кликване (CPC) в Google Ads рекламодателят плаща само когато някой кликне върху рекламата.“
Other click mentions are not F1 claims: the PPC gloss („плащане на клик“, #kak-raboti and FAQ 3) is a term definition, and „неплатените резултати… не се плаща на клик“ (#kak-raboti) is about SEO. Title, meta, label, summary, eyebrow, H1, H2s and lead contain no F1 statement. Each F1 VERIFY marker names the CPC condition. No sentence claims CPC is the only payment model.

Deliverable constraints: H2 8 (6–8 ✓) | FAQ 8 (6–8 ✓) | title 59 chars incl. „ | BizGrow“ (≤ 60 ✓, python-counted, no em-dash) | meta 148 chars (120–160 ✓, main term at start) | each section: paragraphs first, then at most one list ✓ (#proces: paragraph + CTA line + one numbered list) | inline syntax only `**bold**`, `[label](path)`, `[label]({{BOOKING_URL}})`, `{{EMAIL}}` ✓ | em-dashes in copy 0 (the only „—“ sit inside `[VERIFY: … — URL]` markers, which Step 6 removes).

### CRITICAL (blocks until fixed)
1. „При планирането заедно с Вас се решава дали да използвате само един от тези канали или комбинация от тях.“ → check 2 (client co-decision not in canon) → „При планирането се решава дали да използвате само един от тези канали или комбинация от тях.“ (owner item 9).
2. „…какво Ви носи рекламата и къде губите време или пари.“ → check 2 (canon: where the business loses time) → „…какво Ви носи рекламата и къде губите време.“ (owner item 10).

### MODERATE (not changed; noted)
- „оферирането“ is Google Ads' own term (the source's wording); it is readable in context because CPC is glossed as „цена на кликване“. No gloss added to avoid growing the „тоест“ chain.
- „Затова този вид Гугъл реклама често се нарича PPC реклама“ now follows the CPC sentence, so it refers to CPC bidding; coherent, kept.
- „какво връща всяко вложено евро“ appears in lead, #specialist, #otchet, FAQ 4 and summary. Canon I6 wording; acceptable on a service page, should not grow.
- #cena: two consecutive sentences start with „Работим“; kept so the GDPR wording stays verbatim as its own sentence.
- H1 „Google“ vs title „Гугъл“: keyword-map H1 kept; owner item 6.

### OWNER ITEMS TO RAISE (for Step 6)
Carried (from 04-seo r2 and gate r1):
1. `[VERIFY]` F1, now qualified: with cost-per-click (CPC) bidding, Google Ads charges only when someone clicks (https://support.google.com/google-ads/answer/6227565?hl=bg). #kak-raboti, #cena, FAQ 1, FAQ 3.
2. `[VERIFY]` F2: the advertiser decides the average daily amount (same URL). #kak-raboti, #cena, FAQ 1.
3. `[VERIFY]` F3: placement depends on competition and ad rank; a higher amount does not assure placement (https://support.google.com/google-ads/answer/2472742?hl=bg). #kak-raboti, FAQ 2.
4. `[OWNER CONFIRM]` Pricing model of the specialist's ongoing work vs canon „еднократна цена за всяко решение“. #cena.
5. `[OWNER CONFIRM]` Is the ad budget paid to Google/Meta separate from BizGrow's fee? #cena, FAQ 1 (no claim in text).
6. `[OWNER CONFIRM]` Title uses Cyrillic „Гугъл“ (exact search term) while the H1 keeps the keyword-map „Google“; label „Реклама в Google и Facebook“, summary and eyebrow „Маркетинг специалист“.
7. `[DATA NEEDED]` Whose ad account is used (the client's own Google Ads / Meta account or BizGrow's).
8. `[DATA NEEDED]` Minimum ad budget; tools used for tracking; time to first results.
9. `[OWNER CONFIRM]` Does the client take part in choosing the channels (Google, Facebook, Instagram) at the planning stage? „заедно с Вас“ removed as non-canon; it can return if confirmed.
10. `[OWNER CONFIRM]` Scope of the free diagnosis for this service: the page says the call covers „как рекламирате сега, какво Ви носи рекламата и къде губите време“ and „досегашната Ви реклама“; canon says only „безплатна диагностика и 30-минутен разговор“ that finds where the business loses time. Confirm the ads-specific scope wording.
New from this run: none.

### VOICE NOTES (protect during later edits)
- Lead sentence 1 states the offer with the exact main term; keep it first.
- Keep the CPC condition on every F1 sentence; never shorten back to „Google таксува само при клик“.
- Glosses „тоест …“ explain each term once; do not add more.
- FAQ 8 answers "how fast are results" without a promise; keep it free of any time figure.
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
| I7 takes over planning/execution; report, not tasks | PASS | #specialist |
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

**INVENTORY DIFF: PASS (18/18 applicable, I19 n/a).** Flags: 5 inline markers (F1 ×4 locations, F2, F3, 2 OWNER CONFIRM) + 2 DATA NEEDED carried unchanged; owner items 9–10 carried from r1. No flag removed, no fact or number added.

## PHASE 2: FIXES APPLIED

1. #facebook-instagram: „При планирането заедно с Вас се решава…“ → „При планирането се решава…“ (owner item 9).
2. #diagnostika: „…и къде губите време или пари.“ → „…и къде губите време.“ (owner item 10).

No other change. Title, meta, label, summary, eyebrow, H1, H2s, lead, the four CPC-qualified F1 sentences, FAQ, CTAs, tokens, links, section ids and all flags are exactly as in 04-seo.md r2.

---

## FULL ARTICLE AFTER FIXES

Page: /reklama/ | Locale: bg | Type: new-page | Main term: реклама в гугъл

META
- title: „Реклама в Гугъл и Facebook с маркетинг специалист | BizGrow“ (59 characters incl. „ | BizGrow“; exact main term; no em-dash)
- meta_description: „Реклама в Гугъл, Facebook и Instagram, която маркетинг специалист планира, пуска, следи и отчита с числа. Безплатна диагностика и доклад до 48 часа.“ (148 characters; main term at the start; „безплатна“ only for the diagnosis; numbers 48 canon)

CONTENTPAGE FIELDS
- label: „Реклама в Google и Facebook“ (27 characters; same name as the page in conversion-links.md, so menu, breadcrumb and link tables match)
- summary: „Кампании в Google Ads, Facebook и Instagram, които маркетинг специалист планира, пуска и следи, като Ви показва какво връща всяко вложено евро.“ (143 characters; one sentence; canon facts I4/I6/I9 only; deliberately without the exact main term so cards on other pages do not repeat it)
- eyebrow: „Маркетинг специалист“ (20 characters; secondary term, the service's own name in the canon)
- service (schema name, from brief): „Реклама в Google и Facebook“
- related: /socialni-mrezhi/, /seo-optimizacia/, /diagnostika/

secondary_keywords used
- гугъл реклама: #kak-raboti „този вид Гугъл реклама“ (kept)
- google реклама / реклама в google: H1 „Реклама в Google“ (variant of main term)
- google ads реклама: #kak-raboti „Google Ads е рекламната платформа…“; FAQ 1 „рекламата в Google Ads“
- реклама в гугъл цена: covered by intent in #cena and FAQ 1 (no extra exact-match)
- ppc реклама: #kak-raboti, FAQ 3 (kept)
- онлайн реклама: #za-kogo (added, one use)
- фейсбук реклама / реклама в инстаграм: Latin-script variants in title, meta, lead, H2 #facebook-instagram, FAQ 6
- маркетинг специалист: title, meta, H1, eyebrow, #specialist, #otchet
- Not used: „реклама в интернет“ (would be a second near-synonym of „онлайн реклама“ in a short page; skipped to avoid stuffing)

---

# Реклама в Google и Facebook с маркетинг специалист

Предлагаме реклама в Гугъл, Facebook и Instagram, която жив маркетинг специалист планира, пуска и следи вместо Вас. Той отговаря пред Вас с числа и Ви показва какво връща всяко вложено евро. Първата стъпка е безплатна диагностика, която не Ви обвързва с нищо.

## Какво прави маркетинг специалистът {#specialist}

Маркетинг специалистът на BizGrow е реален човек, който поема рекламата на Вашия бизнес от планирането до отчета. Той работи с кампании, като кампания означава една реклама или група реклами с обща цел и бюджет. Специалистът поема планирането и изпълнението, а при Вас остава отчетът с резултатите.

- **Планиране.** Специалистът планира в кои канали да се показва рекламата: Google, Facebook, Instagram или няколко от тях.
- **Настройка и пускане.** Подготвя и пуска кампаниите, без да Ви прехвърля задачи по тях.
- **Проследяване.** Следи резултатите на кампаниите и Ви показва какво връща всяко вложено евро.
- **Кампании на база данни.** Насочва кампаниите според това кой какво купува, кога се връща и какво е подходящо да му предложите.

## Как работи рекламата в Гугъл за малък бизнес {#kak-raboti}

Google Ads е рекламната платформа на Google, чрез която бизнесите пускат платени реклами. При оферирането за цена на кликване (CPC) Google таксува рекламодателя само когато някой кликне върху рекламата. [VERIFY: при офериране за цена на кликване (CPC) Google Ads таксува рекламодателя само при клик върху рекламата — https://support.google.com/google-ads/answer/6227565?hl=bg] Затова този вид Гугъл реклама често се нарича PPC реклама, от английското „pay per click“, тоест плащане на клик.

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

От страна на Google Вие решавате средната дневна сума за рекламата, а при оферирането за цена на кликване (CPC) Google таксува само при клик върху рекламата. [VERIFY: рекламодателят решава средната дневна сума; при офериране за цена на кликване (CPC) таксуване само при клик — https://support.google.com/google-ads/answer/6227565?hl=bg] [OWNER CONFIRM: is the ad budget paid to Google/Meta separate from BizGrow's fee? owner item only, no claim in text]

## Запазете безплатна диагностика {#diagnostika}

На безплатната диагностика ще разгледаме как рекламирате сега, какво Ви носи рекламата и къде губите време. Можете да запазите час директно или да ни пишете на {{EMAIL}}.

[Запазете час]({{BOOKING_URL}})

---

## FAQ

1. **q:** Колко струва рекламата в Google Ads?
   **a:** В Google Ads Вие решавате средната дневна сума, а при оферирането за цена на кликване (CPC) Google таксува само при клик върху рекламата. [VERIFY: F1 (при офериране за цена на кликване, CPC, таксуване само при клик) / F2 — https://support.google.com/google-ads/answer/6227565?hl=bg] Цената на нашата работа получавате в доклада след безплатната диагностика и тя зависи от това какво ще изградим. [OWNER CONFIRM: is the ad budget paid to Google/Meta separate from BizGrow's fee? owner item only, no claim in text]

2. **q:** Ако платя повече, ще се показва ли рекламата ми най-отгоре?
   **a:** По-високата сума сама по себе си не осигурява най-горното място. Според Google мястото на рекламата зависи от конкуренцията с други рекламодатели и от рекламния ранг. [VERIFY: F3 — https://support.google.com/google-ads/answer/2472742?hl=bg]

3. **q:** Какво е PPC реклама?
   **a:** PPC идва от английското „pay per click“, тоест плащане на клик. При оферирането за цена на кликване (CPC) в Google Ads рекламодателят плаща само когато някой кликне върху рекламата. [VERIFY: F1 (при офериране за цена на кликване, CPC, таксуване само при клик) — https://support.google.com/google-ads/answer/6227565?hl=bg]

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

## FLAGS (all carried unchanged)

Inline:
- `[VERIFY]` F1 (charge only on click, qualified with the CPC-bidding condition): #kak-raboti, #cena, FAQ 1, FAQ 3.
- `[VERIFY]` F2 (advertiser decides average daily amount): #kak-raboti, #cena, FAQ 1.
- `[VERIFY]` F3 (placement depends on competition and ad rank; higher amount does not assure placement): #kak-raboti, FAQ 2.
- `[OWNER CONFIRM]` Pricing model of the specialist's ongoing work vs canon „еднократна цена за всяко решение“: #cena.
- `[OWNER CONFIRM]` Ad budget paid to Google/Meta separate from BizGrow's fee: #cena, FAQ 1.

Owner items, not in the text:
- `[DATA NEEDED]` Whose ad account is used (client's own Google Ads / Meta account or BizGrow's).
- `[DATA NEEDED]` Minimum ad budget; tools used for tracking; time to first results.
- `[OWNER CONFIRM]` Title „Гугъл“ vs H1 „Google“; label, summary, eyebrow.
- `[OWNER CONFIRM]` Client's part in choosing channels at planning („заедно с Вас“ removed).
- `[OWNER CONFIRM]` Ads-specific scope wording of the free diagnosis (#diagnostika, #proces step 1).
