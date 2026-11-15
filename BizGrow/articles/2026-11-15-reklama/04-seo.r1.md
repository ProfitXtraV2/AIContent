# 04-seo: /reklama/ (bg, new-page)

## PHASE 1: AUDIT

```
SEO AUDIT: /reklama/ (bg)
Main term: реклама в гугъл | Intent: commercial + informational (SERP mixes Google help, Wikipedia, "how-to/steps" articles and agency service pages with price in the title)
Placement (03-humanised): title N (no title yet), H1 Y (variant „Реклама в Google“), first 100 words Y (lead sentence 1), H2 Y (#kak-raboti „Как работи рекламата в гугъл…“)
Relevance score: 82/100 (alignment 20/25 | entities 30/35 | questions 22/25 | on-page 10/15)
After optimisation: 90/100 (alignment 24/25 | entities 32/35 | questions 22/25 | on-page 12/15)
```

QUERY ALIGNMENT
- Main term slots in 03: H1 („Реклама в Google и Facebook…“, Latin-script variant, kept as the keyword-map H1), lead sentence 1 („Предлагаме реклама в гугъл…“), H2 #kak-raboti. Title missing (written below).
- Extra main-term use: FAQ q1 „Колко струва реклама в Google?“ is a fifth exact-variant occurrence. De-flooded to „Колко струва рекламата в Google Ads?“ (keeps the price intent of „реклама в гугъл цена“, adds the „Google Ads“ entity).
- Orthography defect: „гугъл“ written lowercase in body copy. Bulgarian transliterated proper names are capitalised („Гугъл“); search matching is case-insensitive, so this costs nothing in SEO. Fixed in lead, H2 #kak-raboti and the PPC sentence.
- One term per page: checked against every row. „ai автоматизация“, „ai асистент“, „автоматизация на бизнес процеси“, „seo копирайтинг“, „маркетинг в социалните мрежи“, „seo оптимизация“, „безплатна диагностика за бизнеса“: none targeted. „SEO оптимизация на сайтове“ appears only as the link anchor to /seo-optimizacia/ (passing mention with link, allowed). „поддръжка на социални мрежи и криейтиви“ appears only as the link anchor to /socialni-mrezhi/ (body + FAQ 5, required by inventory I10; passing mention with link, allowed). Sibling secondaries „реклама в социалните мрежи“, „социални мрежи реклама“, „рекламни визии“ are absent; nothing new added toward them.

ENTITY COVERAGE
- PRESENT: Google Ads (defined), Facebook, Instagram, кампания (defined), PPC / плащане на клик (defined), ключови думи (defined), търсачка, рекламен ранг (defined), конкуренция с други рекламодатели, средна дневна сума, неплатени резултати vs платени (SEO link), визии и текстове за рекламите, кампании на база данни, отчет с числа, „какво връща всяко вложено евро“, месечен отчет, process (диагностика, 30-минутен разговор, доклад до 48 часа, изграждане обикновено до 2 седмици, поддръжка), price formation without a number, no long-term contracts, „Работим по GDPR“, audience (6 canon groups).
- MISSING (honestly coverable): „бюджет“ / „дневен бюджет“, the word owners actually use, is absent; added as a gloss of the already-sourced F2 sentence (no new fact). „онлайн реклама“ (150, KD 2) absent; added once in #za-kogo where it reads naturally.
- MISSING (not coverable, NOT added): quality score (same Google source, but would be a 4th sourced fact; ceiling is 3), minimum budget, whose ad account, tracking tools, time to results, Meta auction facts (source unreadable). Remain owner items / DATA NEEDED.
- ORPHANED: none.

BUYER QUESTIONS (brief)
- Какво е реклама в Google и как работи: answered (#kak-raboti, FAQ 3).
- Колко струва / „реклама в гугъл цена“: answered without numbers (#cena, FAQ 1).
- Как се прави (стъпки): answered via #specialist bullets + #proces.
- Предимства и недостатъци: partly (ads shown to people searching via ключови думи; cost tied to clicks). No opinion added; correct.
- По-висока сума = първо място: answered (#kak-raboti, FAQ 2), no guarantee wording.
- Google или Facebook/Instagram: answered (#facebook-instagram, FAQ 6), no performance claims.
- Как разбирам какво ми носи: answered (#otchet, FAQ 4).
- Договор / обвързване: answered (#cena, FAQ 7).
- Кой прави визиите: answered (FAQ 5, link).
- Колко бързо има резултат: answered around it without a promise (FAQ 8).
- Unanswered: none worth a new FAQ; list already at the 8-item ceiling.

SYNONYM FIELD
- Owner words present: реклама, клиенти, оферти, отчет, евро, „да видим дали ще стане“, сума, кликне. Added: „бюджет“. No unexplained jargon (кампания, PPC, ключови думи, рекламен ранг, SEO all glossed on first use).

ON-PAGE / DEFECTS
- D1 (major): no title / meta description. Written below (python-counted).
- D2 (minor): extra main-term variant in FAQ q1. Fixed.
- D3 (minor): lowercase „гугъл“ in copy. Fixed („Гугъл“).
- D4 (minor): „бюджет“ and „онлайн реклама“ missing. Added, one use each.
- D5 (minor): ContentPage `label`, `summary`, `eyebrow` not proposed. Added.
- One H1; 8 H2 (within 6–8); no H3. FAQ 8 (within 6–8), each 1–3 complete sentences.
- Links: /seo-optimizacia/, /socialni-mrezhi/ (×2, body + FAQ 5), /diagnostika/; all in conversion-links.md. Tokens {{BOOKING_URL}} ×2 (one per section), {{EMAIL}} ×1.

LINKS TO ADD
- None. Body already carries 3 contextual links (rule 1–3). `related` suggestion: /socialni-mrezhi/, /seo-optimizacia/, /diagnostika/.

FAQ CANDIDATES
- Kept all 8; q1 reworded (de-flood). No new FAQ (ceiling).

---

## PHASE 2: OPTIMISED PAGE

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

Google Ads е рекламната платформа на Google, чрез която бизнесите пускат платени реклами. Google таксува рекламодателя само когато някой кликне върху рекламата. [VERIFY: Google Ads таксува рекламодателя само при клик върху рекламата — https://support.google.com/google-ads/answer/6227565?hl=bg] Затова този вид Гугъл реклама често се нарича PPC реклама, от английското „pay per click“, тоест плащане на клик.

Вие решавате каква средна сума да се изразходва за рекламата всеки ден, тоест какъв да бъде дневният бюджет. [VERIFY: рекламодателят решава средната дневна сума — https://support.google.com/google-ads/answer/6227565?hl=bg] При настройката на кампанията се избират ключови думи, тоест думите, които хората пишат в търсачката, когато търсят дадена услуга или продукт.

Мястото, на което се показва рекламата, не зависи само от сумата. Според Google то зависи от конкуренцията с други рекламодатели и от рекламния ранг, тоест оценката, която Google дава на всяка реклама при показването ѝ. По-високата сума сама по себе си не осигурява определено място. [VERIFY: мястото зависи от конкуренцията и рекламния ранг; по-високата сума не осигурява място — https://support.google.com/google-ads/answer/2472742?hl=bg]

Позициите в неплатените резултати на Google са отделна работа, която не се плаща на клик. С тях се занимава услугата [SEO оптимизация на сайтове](/seo-optimizacia/), тоест подобряване на сайта, така че търсачката да го показва в обикновените резултати.

## Реклама във Facebook и Instagram {#facebook-instagram}

Освен в Google, маркетинг специалистът планира и пуска реклама във Facebook и Instagram. При планирането заедно с Вас се решава дали да използвате само един от тези канали или комбинация от тях.

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

На безплатната диагностика ще разгледаме как рекламирате сега, какво Ви носи рекламата и къде губите време или пари. Можете да запазите час директно или да ни пишете на {{EMAIL}}.

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

## MAIN-TERM PLACEMENT CHECK (after optimisation)

| slot | text | count |
|---|---|---|
| title | „Реклама в Гугъл и Facebook с маркетинг специалист \| BizGrow“ | 1 (exact) |
| H1 | „Реклама в Google и Facebook с маркетинг специалист“ | 1 (Latin variant, keyword-map H1) |
| first 100 words | lead sentence 1, „Предлагаме реклама в Гугъл…“ | 1 (exact) |
| H2 | #kak-raboti „Как работи рекламата в Гугъл за малък бизнес“ | 1 (only H2 with the term) |
| meta description | opening words | 1 |
| FAQ | none (q1 de-flooded to „Google Ads“) | 0 |

„Гугъл реклама“ (secondary, reversed word order) once in #kak-raboti. No other exact or variant uses in body paragraphs.

## FLAGS (all carried unchanged)

Inline:
- `[VERIFY]` F1 (charge on click): #kak-raboti, #cena, FAQ 1, FAQ 3.
- `[VERIFY]` F2 (advertiser decides average daily amount): #kak-raboti, #cena, FAQ 1. The added gloss „тоест какъв да бъде дневният бюджет“ restates F2 in owner words; no new fact.
- `[VERIFY]` F3 (placement depends on competition and ad rank; higher amount does not assure placement): #kak-raboti, FAQ 2.
- `[OWNER CONFIRM]` Pricing model of the specialist's ongoing work vs canon „еднократна цена за всяко решение“: #cena.
- `[OWNER CONFIRM]` Ad budget paid to Google/Meta separate from BizGrow's fee: #cena, FAQ 1.

Owner items, not in the text (carried):
- `[DATA NEEDED]` Whose ad account is used (client's own Google Ads / Meta account or BizGrow's).
- `[DATA NEEDED]` Minimum ad budget; tools used for tracking; time to first results.

New, for `[[owner_items]]`:
- `[OWNER CONFIRM: title uses Cyrillic „Гугъл“ (exact search term, 400/mo) while the H1 keeps the keyword-map „Google“; label „Реклама в Google и Facebook“, summary and eyebrow „Маркетинг специалист“ for the ContentPage card/breadcrumb]`
- SEO note: if the owner confirms the ad-budget question, FAQ 1 can state it in one sentence and better match „реклама в гугъл цена“ without a number.
- New external facts this step: none (sourced facts stay at 3). [LINK NEEDED]: none.

## INVENTORY DIFF (00-inventory.md vs optimised page)

| item | status | where |
|---|---|---|
| I1 booking CTA, formal imperative, max one per section | PASS | #proces „Запазете безплатна диагностика“; #diagnostika „Запазете час“ |
| I2 `{{EMAIL}}` | PASS | #diagnostika |
| I3 link /diagnostika/ | PASS | #proces step 1 |
| I4 real specialist plans, runs, tracks | PASS | lead, #specialist, FAQ 5, summary |
| I5 reports with numbers | PASS | lead, #otchet, FAQ 4, meta |
| I6 what each invested euro returns | PASS | lead, #specialist, #otchet, FAQ 4, summary |
| I7 takes over planning/execution, report not tasks | PASS | #specialist |
| I8 data-driven campaigns | PASS | #specialist bullet 4 |
| I9 Google Ads + Facebook/Instagram | PASS | lead, #kak-raboti, #facebook-instagram, FAQ 1/3/6 |
| I10 creatives every month → /socialni-mrezhi/ | PASS | #facebook-instagram, FAQ 5 |
| I11 free diagnosis + 30-minute call | PASS | #proces step 1, FAQ 8 |
| I12 report within 48 h, one-off prices, no number | PASS | #proces step 2, #cena, FAQ 8, meta |
| I13 build „обикновено до 2 седмици“ | PASS | #proces step 3, FAQ 8 |
| I14 monthly support + short monthly report | PASS | #proces step 4, #otchet, FAQ 4 |
| I15 no long-term contracts | PASS | #cena, FAQ 7 |
| I16 transparent prices, formation, no number | PASS | #cena, FAQ 1 |
| I17 „Работим по GDPR“ only wording | PASS | #cena |
| I18 diagnosis commits to nothing | PASS | lead, #cena, FAQ 7 |
| I19 example label | PASS (n/a) | no example scenario |

Counts: CTAs 2 | tokens 2 | body links 3 (+1 repeat in FAQ 5) | numbers 30, 48, 2 only | section ids 8 unchanged | FAQs 8 | flags 5 inline + 2 owner items unchanged. Em-dashes in copy: 0 (only inside `[VERIFY: … — URL]` markers). „ти“ forms 0; banned/price/offer terms 0.

**INVENTORY DIFF: PASS (19/19 present, same meaning).**

## CHANGE SUMMARY

1. Title written with the exact main term (59 chars, „Реклама в Гугъл и Facebook с маркетинг специалист | BizGrow“) and meta description (148 chars) opening with the main term; H1 keeps the keyword-map „Google“ variant.
2. De-flooded FAQ q1 („Колко струва реклама в Google?“ → „Колко струва рекламата в Google Ads?“) so the main term sits once each in title, H1, lead and H2 #kak-raboti.
3. Capitalised „Гугъл“ (correct Bulgarian for a transliterated proper name) in lead, H2 and the PPC sentence.
4. Added secondaries naturally, one use each: „онлайн реклама“ (#za-kogo) and „дневният бюджет“ as an owner-word gloss of the sourced F2 sentence; no new fact, number or link.
5. Proposed label „Реклама в Google и Facebook“, summary (143 chars), eyebrow „Маркетинг специалист“, related paths; every fact, flag, CTA, token, link, section id and the 8 FAQs preserved; no sibling main or secondary term targeted.
