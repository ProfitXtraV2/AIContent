# 04-seo: /socialni-mrezhi/ (bg) · Step 4 SEO

## PHASE 1: AUDIT (of 03-humanised.md, edited page)

```
SEO AUDIT: /socialni-mrezhi/ (bg)
Main term: маркетинг в социалните мрежи | Intent: commercial + informational (SERP: academy/how-to articles + agency service pages, AI Overview present)
Placement (before): title N (none yet), H1 N (keyword-map H1, flag F6), first 100 words Y (lead, 1st sentence), H2 Y (#proces)
Relevance score (before): 78/100 (alignment 17/25 | entities 32/35 | questions 22/25 | on-page 7/15)
Relevance score (after):  93/100 (alignment 24/25 | entities 32/35 | questions 23/25 | on-page 14/15)

ONE TERM PER PAGE: no sibling main term targeted. „seo копирайтинг“ (/seo-statii/) not used; link anchor
„SEO статии и копирайтинг“ is a passing mention with a link (allowed). „реклама в гугъл“ (/reklama/) not used;
„Реклама в Google и Facebook“ appears only as the anchor of the /reklama/ link. /reklama/ secondaries
„фейсбук реклама“ and „реклама в инстаграм“ not targeted. „ai асистент“ appears only as „AI асистент“ in FAQ 8
pointing to /ai-asistent/ (passing mention + link).

ENTITIES PRESENT: content tool; posts with text + image; schedule; client approval before publication;
Instagram, Facebook; monthly branded creatives (визии, публикации, рекламни материали); криейтив explained;
AI images explained; Google Business профил (Search + Maps, V1); photos, working hours, current info;
Google ratings/comments with reply after approval (F4); marketing specialist for paid Facebook/Instagram ads,
reporting with numbers; audience list (8 business types, canon); process 30 min / 48 h / обикновено до 2
седмици / monthly short report; no long-term contracts; transparent prices; „Работим по GDPR“; diagnosis
commits to nothing.
MISSING ENTITIES (honest only): named networks beyond Instagram/Facebook (F2), cadence (F1),
community management (F3). Not fillable from canon; left as owner items. Nothing else missing that the
canon can cover.
ORPHANED: none.

UNANSWERED QUESTIONS: all brief buyer questions answered (body or FAQ). „Трябва ли да наемам дизайнер /
social media специалист на щат?“ deliberately not answered (comparative/savings claim excluded at Step 1).
„Какво е криейтив / рекламна визия?“ and „Защо Google Business профил?“ answered in body (#kreativi,
#google-profil); FAQ already at the brief's maximum of 8, so no FAQ added.

SYNONYM FIELD: публикации, профили, визии, рекламни материали, реклама, работно време, снимки,
одобрение: owner vocabulary, natural. „криейтив“ explained on first use. OK.

DEFECTS:
1. H1 lacks the main term (F6). → Resolved: H1 changed (see H1 DECISION).
2. No title / meta_description yet. → Added (below), counted with python3.
3. label/summary: summary omitted the Google profile (third pillar of the lead). → summary updated.
None else: 0 em-dashes, 0 en-dashes, 0 „ти“ forms, one H1, 8 H2 (no H3 needed), FAQ answers 1–3
sentences, price FAQ without a number, only canon digits (2, 30, 48), „евро“ only in the canon phrase
„какво връща всяко вложено в рекламата евро“ (no digit, not a price).

LINKS TO ADD: none. Body links /seo-statii/, /reklama/, /diagnostika/ (3 = rule maximum); FAQ links
/reklama/, /ai-asistent/; CTA {{BOOKING_URL}} (1, #kontakt); {{EMAIL}} (#kontakt). All from
conversion-links.md.

FAQ CANDIDATES: none new (8/8 used; all buyer questions covered).
```

## H1 DECISION (flag F6)

- Rule: site-rules §6 and step-4 require the main term once in the H1; the keyword-map proposal
  „Поддръжка на социални мрежи и криейтиви“ does not contain it.
- Decision: **H1 = „Маркетинг в социалните мрежи: поддръжка и криейтиви“** (51 chars). It keeps both
  elements of the keyword-map proposal (поддръжка, криейтиви; secondary „поддръжка на социални мрежи“
  stays recognisable) and adds the main term once.
- Unchanged: `service` (schema) „Поддръжка на социални мрежи и криейтиви“, the conversion-links.md page name,
  eyebrow and label.
- F6 stays open as `[OWNER CONFIRM F6]` (inline under the H1) → Step 6 must raise an `[[owner_items]]` entry:
  „H1 changed from keyword-map proposal to „Маркетинг в социалните мрежи: поддръжка и криейтиви“; approve
  (then update keyword-map.md h1 column) or revert (then the main term is missing from the H1).“

## META / HERO FIELDS (port values)

- title = „Маркетинг в социалните мрежи и криейтиви | BizGrow“ → **50 chars** (len, python3), incl. suffix, no em-dash, unique (no sibling uses it)
- meta_description = „Маркетинг в социалните мрежи за малкия бизнес: публикации по график след Вашето одобрение, брандирани криейтиви всеки месец и актуален Google профил.“ → **149 chars**, contains the main term, no em-dash, page-specific
- h1 = „Маркетинг в социалните мрежи: поддръжка и криейтиви“ → 51 chars
- eyebrow = „Социални мрежи и криейтиви“ (unchanged)
- label = „Социални мрежи и криейтиви“ → 26 chars (unchanged)
- summary = „Публикации по график след Вашето одобрение, брандирани криейтиви всеки месец и актуален Google профил.“ → 102 chars, one sentence (adds the Google profile)
- service = „Поддръжка на социални мрежи и криейтиви“ (unchanged, brief)
- related = /seo-statii/, /reklama/, /diagnostika/ → confirmed: exactly 3, all in conversion-links.md, not `/`, not itself
- primary_keyword = „маркетинг в социалните мрежи“
- Main term count in page copy (visible, flags excluded): 3 = H1, lead 1st sentence (first 100 words), H2 #proces; + title. None in FAQ or other body text.

## SECONDARY KEYWORDS USED

secondary_keywords = ["управление на социални мрежи", "реклама в социалните мрежи", "поддръжка на социални мрежи", "поддръжка на социални мрежи цена", "рекламни визии", "криейтиви"]

- управление на социални мрежи → FAQ 1 („управлението на социални мрежи“)
- реклама в социалните мрежи → H2 #platena-reklama
- поддръжка на социални мрежи → H1 („поддръжка“ with the main term), FAQ 2, `service`
- поддръжка на социални мрежи цена → FAQ 2 „Колко струва поддръжката на социални мрежи?“ (answered without a number)
- рекламни визии → H2 #kreativi
- криейтиви → H2 #kreativi, lead/summary/title/H1, FAQ 1/6
- социални мрежи реклама → not placed separately (word-order variant of „реклама в социалните мрежи“; adding it would read as stuffing)

---

# OPTIMISED PAGE

Page: /socialni-mrezhi/ | Locale: bg | Type: new-page | Main term: маркетинг в социалните мрежи

<!-- HERO (ContentPage fields outside sections[]) -->
- title: Маркетинг в социалните мрежи и криейтиви | BizGrow
- meta_description: Маркетинг в социалните мрежи за малкия бизнес: публикации по график след Вашето одобрение, брандирани криейтиви всеки месец и актуален Google профил.
- eyebrow: Социални мрежи и криейтиви
- label: Социални мрежи и криейтиви
- summary: Публикации по график след Вашето одобрение, брандирани криейтиви всеки месец и актуален Google профил.
- service: Поддръжка на социални мрежи и криейтиви
- related: /seo-statii/, /reklama/, /diagnostika/

# Маркетинг в социалните мрежи: поддръжка и криейтиви

[OWNER CONFIRM F6: Step 4 changed the H1 from the keyword-map proposal „Поддръжка на социални мрежи и криейтиви“ to „Маркетинг в социалните мрежи: поддръжка и криейтиви“ so that the main term appears once in the H1 (site-rules §6); owner approves or reverts; if approved, update the h1 column in keyword-map.md; the page name in conversion-links.md and the schema `service` stay unchanged]

BizGrow предлага маркетинг в социалните мрежи за малкия бизнес: публикации с текст и изображение по график, брандирани визии всеки месец и актуален профил в Google. Всяка публикация излиза едва след като Вие я одобрите.

## Публикации с текст и изображение по график {#publikacii}

Много собственици знаят, че профилите им в Instagram и Facebook трябва да са активни, но в натоварена седмица публикациите остават за по-късно. Така профилът често остава без нови публикации със седмици.

BizGrow използва собствен инструмент за съдържание. Той пише текста на публикацията, създава изображение към нея и я публикува в социалните мрежи по предварително зададен график.

Преди публикуване получавате всяка публикация за одобрение. В профилите Ви излиза само съдържание, което Вие сте одобрили.

Честотата на публикациите и мрежите, в които излизат, се уточняват в доклада след диагностиката според вида на Вашия бизнес. [OWNER CONFIRM F1: posting cadence and posts per month; the checker says „всяка седмица“, the canon text has no cadence] [OWNER CONFIRM F2: which social networks the tool publishes to; the canon says only „социалните мрежи“]

Същият инструмент пише и статии за Вашия сайт, подготвени за търсене в Google (SEO, оптимизация за търсачки). Те са описани на страницата [SEO статии и копирайтинг](/seo-statii/).

## Криейтиви и рекламни визии всеки месец {#kreativi}

Криейтив е готов визуален материал за публикация или реклама, например изображение, визия с текст или рекламен банер. Всеки месец подготвяме брандирани визии, публикации и рекламни материали, които следват стила на Вашата марка.

Изображенията се създават с помощта на AI, тоест с програма, която генерира изображение по описание. Подготвяме ги така, че да са подходящи както за публикуване в профилите, така и за реклама. Всяка нова публикация или кампания започва с готова визия.

## Актуален Google Business профил {#google-profil}

Google Business профилът е информацията за Вашия бизнес, която клиентите виждат в Google Търсене и Google Maps. [VERIFY V1: Google Business Profile is how a business appears on Google Search and Maps, https://www.google.com/business/]

Поддържаме профила актуален всеки месец: добавяме публикации, нови снимки и текуща информация, например променено работно време. Клиентите забелязват остарелите снимки и грешното работно време още преди да се свържат с Вас.

Можем също да следим оценките и коментарите, които клиентите оставят в Google, и да подготвяме отговор, който публикуваме след Вашето одобрение. [OWNER CONFIRM F4: are Google review replies part of this social media service, or of the AI assistant service (/ai-asistent/), as the checker tags them? If not this service, Step 4 removes this paragraph and FAQ 8 points to /ai-asistent/]

## Реклама в социалните мрежи с маркетинг специалист {#platena-reklama}

Платената реклама във Facebook и Instagram се води от маркетинг специалист. Той планира, пуска и следи кампаниите и Ви отчита резултатите с числа, така че да виждате какво връща всяко вложено в рекламата евро.

Месечните криейтиви се подготвят и за рекламните кампании, затова публикациите и рекламите Ви имат единен вид. Подробности за платената реклама ще намерите на страницата [Реклама в Google и Facebook](/reklama/).

## За кои бизнеси е подходящо {#za-kogo}

Услугата е подходяща за малки бизнеси, чиито клиенти търсят информация за тях в социалните мрежи и в Google.

- **Ресторанти и кафенета.** Публикации по график и актуално работно време в Google профила.
- **Хотели и къщи за гости.** Нови снимки в профила в Google и редовни публикации с визии на мястото.
- **Салони.** Брандирани визии за услугите и публикации след Вашето одобрение.
- **Онлайн магазини.** Визии за нови продукти, готови за публикации и за реклама.
- **Търговия и шоуруми.** Публикации за новите стоки и актуална информация в Google.
- **Клиники и практики.** Актуално работно време и информация в Google профила.
- **Автосервизи и майстори.** Профил в Google с текущи снимки, работно време и публикации.
- **Недвижими имоти.** Визии и публикации за имотите в социалните мрежи.

## Маркетинг в социалните мрежи стъпка по стъпка {#proces}

Преди изграждането провеждаме разговор и подготвяме доклад.

- **Безплатна диагностика.** Провеждаме 30-минутен разговор за Вашия бизнес и за това как поддържате профилите си в момента.
- **Доклад до 48 часа.** Получавате доклад с приоритизирани решения и ясни еднократни цени.
- **Изграждане.** Изграждаме избраното от Вас, обикновено до 2 седмици.
- **Поддръжка.** Поддържаме работата всеки месец и Ви изпращаме кратък месечен отчет.

Ако искате първо да прецените сами, [безплатната диагностика](/diagnostika/) показва ориентировъчно къде Вашият бизнес губи време всяка седмица.

## Цена и условия {#cena}

Цената зависи от това какво изграждаме за Вашия бизнес. Получавате я като ясна еднократна цена за всяко решение в доклада след безплатната диагностика. [OWNER CONFIRM F5: how ongoing monthly work (scheduled posts, monthly creatives, Google profile upkeep) is priced under the canon's "one-off price per fix" model; the page states only the canon wording]

- Работим без дългосрочни договори.
- Цените са прозрачни и ги виждате в доклада, преди да решите.
- Работим по GDPR.
- Диагностиката не Ви задължава с нищо.

## Започнете с безплатна диагностика {#kontakt}

На разговора ще разгледаме заедно какво може да поеме инструментът за съдържание и какви визии са нужни на Вашия бизнес.

Ако предпочитате да пишете, изпратете ни имейл на {{EMAIL}}.

[Запазете безплатна диагностика]({{BOOKING_URL}})

---

## FAQ

[[faq]]
q = "Какво включва управлението на социални мрежи при BizGrow?"
a = "Включва публикации с текст и изображение, които нашият инструмент за съдържание публикува по график след Вашето одобрение. Към тях всеки месец подготвяме брандирани визии и рекламни материали и поддържаме актуален Вашия Google Business профил."

[[faq]]
q = "Колко струва поддръжката на социални мрежи?"
a = "Цената зависи от това какво изграждаме за Вашия бизнес. Получавате ясна еднократна цена в доклада до 48 часа след безплатната диагностика, без дългосрочен договор."
# [OWNER CONFIRM F5: pricing of ongoing monthly work under the one-off price model]

[[faq]]
q = "Ще виждам ли публикациите, преди да бъдат публикувани?"
a = "Да. Всяка публикация първо идва при Вас за одобрение и в профилите излиза само съдържание, което сте одобрили."

[[faq]]
q = "Колко публикации на месец получавам?"
a = "Броят и честотата на публикациите се уточняват в доклада след диагностиката според Вашия бизнес и целите Ви."
# [OWNER CONFIRM F1: posting cadence / posts per month]

[[faq]]
q = "В кои социални мрежи публикувате?"
a = "Инструментът публикува в социалните мрежи, в които Вашият бизнес има профили. Конкретните мрежи се уточняват след диагностиката."
# [OWNER CONFIRM F2: the answer must name the networks or stay at this level]

[[faq]]
q = "Включена ли е платената реклама във Facebook и Instagram?"
a = "Платените кампании води маркетинг специалист, който планира, пуска и следи рекламата и Ви отчита резултатите с числа. Визиите за тези кампании са част от месечните криейтиви, а самата реклама е описана на страницата [Реклама в Google и Facebook](/reklama/)."

[[faq]]
q = "Трябва ли да подписвам дългосрочен договор?"
a = "Не. Работим без дългосрочни договори, а безплатната диагностика не Ви задължава с нищо."

[[faq]]
q = "Отговаряте ли на коментари и съобщения в профилите ми?"
a = "За съобщенията в Messenger, Instagram и WhatsApp BizGrow изгражда AI асистент, който отговаря на въпросите на клиентите и събира контакта им, когато не може да помогне. Повече ще намерите на страницата [AI асистент и чатбот](/ai-asistent/)."
# [OWNER CONFIRM F3: are replies to comments under posts (community management) part of this service? Not in canon, so not promised]

---

## 5-LINE CHANGE SUMMARY

1. H1 changed to „Маркетинг в социалните мрежи: поддръжка и криейтиви“ so the main term appears once in title, H1, first 100 words and one H2 (F6 kept open as an owner item).
2. Added title (50 chars) and meta_description (149 chars, main term included), both without em-dashes.
3. summary now covers all three pillars of the lead (posts, monthly creatives, Google profile); label, eyebrow, service, related unchanged; related confirmed.
4. Body, FAQ, links, CTA and tokens unchanged: placement and secondaries were already natural; no de-flooding needed (main term 3× in copy), no new facts, numbers or links.
5. Flags carried: V1, F1–F5 unchanged; F6 rewritten to record the Step 4 H1 decision for Step 6.

## INVENTORY DIFF (00-inventory.md vs optimised page)

17/17 items present, unchanged from 03-humanised.md:
- I1 booking CTA „Запазете безплатна диагностика“ → {{BOOKING_URL}} (#kontakt, only one); I2 {{EMAIL}} (#kontakt)
- I3 /reklama/ (#platena-reklama, FAQ 6, related); I4 /diagnostika/ (#proces, related); I5 /seo-statii/ (#publikacii, related)
- I6–I10 canon facts (lead, #publikacii, #kreativi, #google-profil, #platena-reklama, FAQ 1/3/6)
- I11 process 30 / 48 / „обикновено до 2 седмици“ / кратък месечен отчет (#proces); I12 policies incl. „Работим по GDPR“ (#cena, FAQ 7); I13 price without a number (#cena, FAQ 2)
- I14 digits only 2, 30, 48; I15 n/a (no example scenario); I16 8 FAQ, price FAQ without number
- I17 8 H2, service „Поддръжка на социални мрежи и криейтиви“; **H1 changed from the keyword-map proposal (F6, owner item)**: the only deviation, recorded.
Anchors unchanged: publikacii, kreativi, google-profil, platena-reklama, za-kogo, proces, cena, kontakt. Lost items: none.

## FLAGS

- [VERIFY V1] Google Business Profile definition (#google-profil), https://www.google.com/business/
- [OWNER CONFIRM F1] Posting cadence / posts per month (#publikacii, FAQ 4)
- [OWNER CONFIRM F2] Which social networks the tool publishes to (#publikacii, FAQ 5)
- [OWNER CONFIRM F3] Community management (replies to comments under posts) (FAQ 8)
- [OWNER CONFIRM F4] Google review replies: this service or /ai-asistent/? (#google-profil)
- [OWNER CONFIRM F5] Pricing of ongoing monthly work under the one-off price model (#cena, FAQ 2)
- [OWNER CONFIRM F6] H1 changed by Step 4 from the keyword-map proposal; owner approves (update keyword-map h1) or reverts → Step 6 [[owner_items]]

## CANON ADDITIONS

none
