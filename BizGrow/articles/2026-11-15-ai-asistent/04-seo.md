# 04-seo: /ai-asistent/ (bg, new-page, LOOP 1 re-run)

Input: 03-humanised.md (LOOP 1 structure: in every section paragraphs first, then at most one unordered list, nothing after the list). Reference reused from loop0/04-seo.md: title, meta description, label, summary, eyebrow and the FAQ decisions, all of which still fit the new structure.

## PHASE 1: AUDIT

```
SEO AUDIT: /ai-asistent/ (bg)
Main term: ai асистент | Intent: commercial + informational (service page; the „чатбот“ SERP is informational and reserved for a /saveti/ article)
Placement (03-humanised): title Y, H1 Y, first 100 words Y (lead sentence 1, word 3), H2 Y (#kakvo-pravi, „AI асистентът“)
Relevance score: 88/100 (alignment 24/25 | entities 30/35 | questions 21/25 | on-page 13/15)
```

QUERY ALIGNMENT
- Main term once in each required slot (python count of the body: 3 uses = H1, lead sentence 1, H2 #kakvo-pravi; plus title and meta outside the body). No exact-match use in any other H2, paragraph or list item.
- Outside the slots: FAQ q5 „Колко струва AI асистент?“ is the buyer's own phrasing of the price question and stays (same decision as loop0); `label` „AI асистент“ is navigation, not body copy. No de-flooding needed: loop0's extra use in FAQ q1 is already gone in this version.
- One term per page: no sibling main term targeted. Checked: „ai автоматизация“ (/) absent; „автоматизация на бизнес процеси“ (/avtomatizacii/) absent, link anchor „автоматизациите за бизнеса“; „безплатна диагностика за бизнеса“ (/diagnostika/) absent as an exact phrase; „маркетинг в социалните мрежи“ absent („пишат в социалните мрежи“ is a passing phrase); „seo копирайтинг“, „реклама в гугъл“, „seo оптимизация“ absent.
- „чатбот“: H1 and the defining sentence in #kakvo-pravi (2 uses in the body). Natural, not targeted; no use added.

ENTITY COVERAGE
- PRESENT: Messenger, Instagram, WhatsApp; денонощно; collecting the contact; training on the business's own information; repeated questions (цени, работно време, доставка, наличности); hotel guest assistant in any language with live availability and prices; courier-connected parcel status; real-estate enquiry qualification and viewing slots; process (безплатна диагностика, 30-минутен разговор, доклад до 48 часа, изграждане обикновено до 2 седмици, поддръжка с кратък месечен отчет); the diagnosis commits to nothing; price formation without a number; no long-term contracts; transparent prices; „Работим по GDPR“; human control („под Ваш контрол“); nine canon audience groups incl. B2B; chatbot explained on first use.
- Secondary „виртуален асистент“ (30, KD 0) is already present in #kakvo-pravi P1 („Изграждаме такъв виртуален асистент за чата“); nothing to add.
- MISSING (not canon, NOT added): assistant on the client's website („чатбот за сайт“), handoff to a person beyond collecting the contact, languages for non-hotel assistants, AI model/platform, data location. They remain owner items.
- ORPHANED: none.

UNANSWERED BUYER QUESTIONS
- „Отговаря ли на английски и други езици?“: answered in the body for hotels only (#za-kogo list, #primeri); no FAQ. The FAQ list is at the 8-item ceiling and a general answer needs the owner. Candidate logged, not added.
- „Кой AI модел / платформа?“: Tier 3, correctly unanswered. „Готова платформа или изграден асистент?“: vendor comparison not allowed, correctly skipped.
- All other brief questions are answered in body + FAQ (channels, денонощно, unknown answer, own information, price, build time, staff replacement, GDPR).

SYNONYM FIELD
- Owner words present: „съобщения“, „чат“, „запитване“, „контакт“, „отговор“, „свързване на програмите, които вече ползвате“ (instead of „интеграция“). No „лийд“, no unexplained jargon. Good.

ON-PAGE / DEFECTS
- Title 55 characters incl. „ | BizGrow“ (python), unique, no em-dash. OK.
- Meta description 143 characters (python), contains the main term in its first words, no em-dash, „безплатна“ only for the diagnosis, no price digit. OK.
- One H1; 8 H2 (within 6–8); no H3. OK.
- Template constraint verified with python per section: #kakvo-pravi, #usloviya, #sledvashta-stapka paragraphs only; #zadachi, #za-kogo, #proces, #kakvo-poluchavate, #primeri paragraphs then one unordered list, nothing after the list. The booking CTA and email line in #sledvashta-stapka are the marked template-rendered block, not port strings. OK.
- Links only from conversion-links.md: /diagnostika/ (#proces), /avtomatizacii/ (#zadachi); tokens {{BOOKING_URL}} and {{EMAIL}} only in the template-rendered block. 2 body links, within the 1–3 rule. OK.
- FAQ: 8 entries, 2–3 complete formal sentences each (python sentence count 2,2,2,2,3,2,2,2), none repeats a body heading word for word. OK.
- Em-dashes 0 (python). „ти“ forms 0. No banned, hype, offer or testimonial terms.
- Defects: none found in this version.

LINKS TO ADD
- None. `related` = /diagnostika/, /avtomatizacii/, /socialni-mrezhi/ (3 sibling paths from conversion-links.md).

FAQ CANDIDATES
- Kept: all 8 from Step 3 unchanged.
- Candidate not added (ceiling + owner dependency): „Отговаря ли асистентът на английски и други езици?“.

---

## PHASE 2: OPTIMISED PAGE

Page: /ai-asistent/ | Locale: bg | Type: new-page | Main term: ai асистент

No body edit was needed: the main term already sits once in each slot, the secondary „виртуален асистент“ is present, no sibling term is targeted and the template constraint holds. The body below is 03-humanised.md verbatim.

META
- title: „AI асистент за бизнеса в Messenger и WhatsApp | BizGrow“ (55 characters, python)
- meta_description: „AI асистент, който отговаря на клиентите Ви в Messenger, Instagram и WhatsApp денонощно. Безплатна диагностика и доклад с ясни цени до 48 часа.“ (143 characters, python)

CONTENTPAGE FIELDS
- label: „AI асистент“ (11 characters; breadcrumb/card name)
- summary: „Асистент в Messenger, Instagram и WhatsApp, който отговаря на клиентите Ви денонощно с информацията на Вашия бизнес.“ (116 characters; one sentence, canon only, deliberately without the exact main term so cards on other pages do not repeat it)
- eyebrow: „Messenger, Instagram и WhatsApp“ (31 characters; kicker above the H1, avoids „AI автоматизации“, which is too close to the home page's main term)
- service (schema name, from brief): „AI асистент и чатбот“
- related: /diagnostika/, /avtomatizacii/, /socialni-mrezhi/

secondary_keywords used:
- „ai асистент за бизнеса“ (title)
- „виртуален асистент“ (#kakvo-pravi P1)
- „чатбот за бизнес“ (natural variant in H1 „чатбот за Вашия бизнес“; not targeted)
- „чатбот messenger“ / „whatsapp чатбот“ (semantic: chatbot defined and the channels named in the same #kakvo-pravi paragraph; no forced exact phrases)
- Not used: „ai чатбот“, „чатбот за фейсбук“ (would push the page toward targeting „чатбот“; Facebook not named in canon), „чатбот за сайт“ (website assistant not in canon, owner item)

H1: AI асистент и чатбот за Вашия бизнес [OWNER CONFIRM: H1 of the new page]

LEAD:
BizGrow изгражда AI асистент, който отговаря на клиентите Ви в Messenger, Instagram и WhatsApp денонощно и събира контакта им, когато не може да помогне. Асистентът е обучен на собствената информация на Вашия бизнес и поема повтарящите се въпроси за цени, работно време, доставка и наличности.

(Template-rendered under the lead, not in port strings: button „Запазете час“ → {{BOOKING_URL}}; button „Безплатна диагностика“ → /diagnostika/.)

## Какво прави AI асистентът за Вашия бизнес {#kakvo-pravi}

Чатботът е програма, която отговаря автоматично на съобщенията, които клиентите пишат в чата. Изграждаме такъв виртуален асистент за чата, който отговаря на въпросите на клиентите Ви в Messenger, Instagram и WhatsApp с информацията на Вашия бизнес.

Асистентът работи денонощно, затова съобщение, изпратено вечер или в почивен ден, може да получи отговор и извън работно време. Така клиентът може да научи това, което търси, без да чака началото на работния ден.

Когато въпросът излиза извън информацията, с която асистентът разполага, той събира контакта на клиента. Запитването остава при Вас и Вие решавате кой от екипа и кога да се свърже с човека.

## Кои въпроси и задачи поема асистентът {#zadachi}

Асистентът е обучен на собствената информация на Вашия бизнес. Той поема въпросите, на които иначе Вие или служителите Ви отговаряте по няколко пъти всеки ден.

Ако освен отговорите в чата търсите и онлайн записване с напомняния, автоматични оферти или свързване на програмите, които вече ползвате, разгледайте [автоматизациите за бизнеса](/avtomatizacii/). В чата асистентът поема следните въпроси и задачи.

- Цени на продуктите и услугите Ви.
- Работно време и почивни дни.
- Условия и срокове за доставка.
- Наличност на стоки, стаи или свободни часове.
- Събиране на контакта на клиента, когато асистентът не може да помогне.

## За кои бизнеси е подходящ асистентът {#za-kogo}

Работим с малки бизнеси, чиито клиенти пишат в социалните мрежи и в WhatsApp и често задават едни и същи въпроси.

Сред тях са ресторанти и кафенета, хотели и къщи за гости, салони, онлайн магазини, търговски обекти и шоуруми, клиники и практики. Работим и с автосервизи и майстори, агенции за недвижими имоти и фирми, които работят с други фирми (B2B).

В някои отрасли асистентът поема и по-специфични задачи.

- **Хотели и къщи за гости.** Асистентът за гости отговаря на всеки език, денонощно, с актуалната наличност и цените на стаите.
- **Онлайн магазини.** Асистентът е свързан с куриера и сам отговаря на въпроса „Къде ми е поръчката?“ със статуса на пратката.
- **Недвижими имоти.** Асистентът отделя сериозните запитвания от останалите и предлага на тези клиенти свободни часове за оглед.

## Как протича работата {#proces}

Работата започва с [безплатната диагностика](/diagnostika/). На страницата за диагностика избирате вида на бизнеса си, отбелязвате проблемите, които познавате, виждате ориентировъчно колко часа седмично Ви отнемат и запазвате разговор.

Диагностиката не Ви задължава с нищо. Вие решавате дали и кои от предложените в доклада решения да изградим.

- **Безплатна диагностика и 30-минутен разговор.** Разглеждаме къде бизнесът Ви губи време, включително съобщенията, които остават без отговор.
- **Доклад до 48 часа.** Получавате доклад с приоритизирани решения и ясни еднократни цени за всяко от тях.
- **Изграждане.** Изграждаме и настройваме асистента, обикновено до 2 седмици.
- **Поддръжка.** След старта поддържаме асистента и Ви изпращаме кратък месечен отчет.

## Какво получавате {#kakvo-poluchavate}

Асистентът е инструмент, който Вашият бизнес използва под Ваш контрол. Запитванията, които изискват преценка, остават за Вас и Вашия екип.

- **Асистент в Messenger, Instagram и WhatsApp**, обучен на информацията на Вашия бизнес и настроен да отговаря денонощно.
- **Контактите на клиентите**, на които асистентът не е могъл да помогне, за да продължите разговора лично.
- **Доклад с ясни еднократни цени**, който получавате преди началото на работата.
- **Поддръжка с кратък месечен отчет** след изграждането.

## Примерни сценарии {#primeri}

Примерни сценарии по нашия метод, не данни от конкретни клиенти. [OWNER CONFIRM: example scenarios adapted from the „Скрити проблеми“ checker pain lines, with their numbers]

- **Вечерно съобщение.** Клиент пише в 21:30 с въпрос за продукт. Ако чака отговор до сутринта, може вече да е купил от друго място. Асистентът му отговаря още същата вечер или записва контакта му.
- **Хотел.** Турист пише на английски в 23:00 и пита за свободни стаи. Асистентът за гости му отговаря на английски с актуалната наличност и цените, без запитването да чака до сутринта.
- **Онлайн магазин.** Въпросът „Къде ми е поръчката?“ идва по двадесет пъти на ден. Асистентът, свързан с куриера, отговаря на всеки клиент със статуса на неговата пратка.
- **Недвижими имоти.** Запитване за оглед пристига в полунощ от сайт за имоти и се вижда чак на обяд, заедно с още 40. Асистентът отделя сериозните запитвания и предлага на тези клиенти свободни часове за оглед още през нощта.

## Цена, договори и данни {#usloviya}

Цената за изграждането на асистента е еднократна и зависи от това какво точно се изгражда за Вашия бизнес. Посочваме я в доклада след безплатната диагностика, преди да започне каквато и да е работа.

Цените ни са прозрачни и не изискваме дългосрочни договори. Работим по GDPR.

## Следваща стъпка {#sledvashta-stapka}

Ако клиентите Ви пишат в Messenger, Instagram или WhatsApp и отговорите често закъсняват, започнете с безплатната диагностика. В 30-минутния разговор ще прегледаме кои въпроси може да поеме асистентът и къде още бизнесът Ви губи време.

<!-- template-rendered CTA, not in port strings: the porter maps the booking CTA to the button under the lead and the CTA band „Първата стъпка е безплатна“ after the FAQ, and the email line to the footer {{EMAIL}}. Do not copy into paragraphs[]. -->
**Template-rendered CTA, not in port strings:**

[Запазете безплатна диагностика]({{BOOKING_URL}})

Ако предпочитате да пишете, изпратете ни имейл на {{EMAIL}}.

---

## FAQ

[[faq]]
q = "В кои канали работи асистентът?"
a = "Асистентът отговаря на клиентите Ви в Messenger, Instagram и WhatsApp. Кои от тези канали са подходящи за Вашия бизнес, уточняваме по време на безплатната диагностика."

[[faq]]
q = "Отговаря ли асистентът извън работно време?"
a = "Да, асистентът е настроен да отговаря денонощно, включително вечер и в почивни дни. Така съобщенията могат да получат отговор и когато никой от екипа Ви не е на линия."

[[faq]]
q = "Какво става, ако асистентът не знае отговора?"
a = "Когато не може да помогне, асистентът събира контакта на клиента. Запитването остава при Вас и Вие решавате кой да продължи разговора."

[[faq]]
q = "Откъде асистентът знае цените, работното време и условията на моя бизнес?"
a = "Асистентът е обучен на собствената информация на Вашия бизнес. С нея той отговаря на въпросите за цени, работно време, доставка и наличности."

[[faq]]
q = "Колко струва AI асистент?"
a = "Цената е еднократна и зависи от това какво се изгражда за Вашия бизнес. Посочваме я в доклада, който получавате до 48 часа след безплатната диагностика. Не изискваме дългосрочни договори."

[[faq]]
q = "Колко време отнема изграждането на асистента?"
a = "Изграждането отнема обикновено до 2 седмици. Преди него са безплатната диагностика с 30-минутен разговор и докладът, който получавате до 48 часа."

[[faq]]
q = "Ще замени ли асистентът служител?"
a = "Асистентът е инструмент, който поема повтарящите се въпроси в чата. Вие и екипът Ви продължавате да отговаряте на запитванията, които изискват преценка."

[[faq]]
q = "Как се отнасяте към данните на клиентите ми?"
a = "Работим по GDPR. Конкретните въпроси за данните на Вашия бизнес можете да обсъдите в 30-минутния разговор по време на диагностиката."

(After the FAQ the template renders the CTA band „Първата стъпка е безплатна“ → {{BOOKING_URL}}.)
---

## RELATED
- /diagnostika/
- /avtomatizacii/
- /socialni-mrezhi/

---

## MAIN-TERM PLACEMENT CHECK (after optimisation)

| slot | text | count |
|---|---|---|
| title | „AI асистент за бизнеса в Messenger и WhatsApp \| BizGrow“ | 1 |
| H1 | „AI асистент и чатбот за Вашия бизнес“ | 1 |
| first 100 words | lead sentence 1, „BizGrow изгражда AI асистент…“ | 1 |
| H2 | #kakvo-pravi „Какво прави AI асистентът за Вашия бизнес“ | 1 (only H2 with the term) |
| meta description | opening words | 1 |
| FAQ | q5 „Колко струва AI асистент?“ (buyer phrasing) | 1 |
| label | „AI асистент“ (navigation, not body copy) | 1 |

Body paragraphs, lists and the other 7 H2s use „асистентът“ / „асистента“ only. „чатбот“: H1 + one defining sentence.

## INVENTORY CHECK (00-inventory.md, all items present, none weakened)

1–2. Booking CTA `[Запазете безплатна диагностика]({{BOOKING_URL}})` and the {{EMAIL}} line: #sledvashta-stapka template-rendered block (button under the lead + CTA band after the FAQ on the site). Unchanged.
3–4. /diagnostika/ in #proces P1; /avtomatizacii/ in #zadachi P2. Unchanged.
5–9. Canon capabilities (channels, денонощно, contact, own information, hotel, courier, real estate): lead, #kakvo-pravi, #zadachi, #za-kogo, #kakvo-poluchavate, #primeri, FAQ 1–4. Unchanged.
10. Process with „30-минутен разговор“, „до 48 часа“, „обикновено до 2 седмици“, „кратък месечен отчет“: #proces list, #kakvo-poluchavate, FAQ 6. Unchanged.
11–12. Price formation without a number, no long-term contracts, transparent prices, „Работим по GDPR“: #usloviya, FAQ 5, FAQ 8. Unchanged.
- Example label alone in #primeri P1, same section as the examples. Unchanged.

## FLAGS

- [OWNER CONFIRM: H1 of the new page] (H1 line). Carried.
- [OWNER CONFIRM: example scenarios adapted from the „Скрити проблеми“ checker pain lines, with their numbers] (#primeri). Carried.
- For `[[owner_items]]` at Step 6 (carried, not in text): [OWNER CONFIRM: label „AI асистент“, summary and eyebrow „Messenger, Instagram и WhatsApp“ for the ContentPage card/breadcrumb]; [OWNER CONFIRM: assistant on the client's website]; [OWNER CONFIRM: languages for non-hotel assistants]; [OWNER CONFIRM: handoff and contact delivery]; [OWNER CONFIRM: model/platform and data location, only if the owner wants them on the page]; [DATA NEEDED: support pricing model, if the owner wants it explained].
- SEO note for owner: if the website assistant is confirmed, „чатбот за сайт“ becomes usable, and the language FAQ („Отговаря ли асистентът на английски и други езици?“) can replace one entry (stay within 8).
- Claim watch for Step 5: „може да получи отговор и извън работно време“ (#kakvo-pravi P2) and „могат да получат отговор“ (FAQ 2) are hedged with „може/могат“; keep the hedge, it is not a response-time promise.
- Porter note (not an owner item): booking CTA and email line in #sledvashta-stapka are template-rendered, not paragraphs[].
- [VERIFY]: none. [LINK NEEDED]: none. New external facts: none.

## CHANGE SUMMARY

1. Main term verified once each in title, H1, lead sentence 1 and the #kakvo-pravi H2 (python: 3 body uses); FAQ q5 kept as buyer phrasing; no de-flooding needed.
2. „виртуален асистент“ already present in #kakvo-pravi; „чатбот“ left at H1 + definition, not targeted; no sibling main term targeted.
3. Title (55) and meta description (143) reused from loop0 after python count; label (11), summary (116, one sentence), eyebrow (31) reused, no new facts.
4. Template constraint re-verified per section with python (paragraphs, then at most one list, nothing after); 8 H2, 8 FAQ of 2–3 sentences, 0 em-dashes.
5. Body, FAQ, links, tokens, example label, inventory items and every flag preserved verbatim from 03-humanised.md; no new links, facts, numbers or FAQs.
