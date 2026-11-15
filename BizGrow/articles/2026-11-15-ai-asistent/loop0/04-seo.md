# 04-seo: /ai-asistent/ (bg, new-page)

## PHASE 1: AUDIT

```
SEO AUDIT: /ai-asistent/ (bg)
Main term: ai асистент | Intent: commercial + informational (service page; "чатбот" SERP is informational and reserved for a /saveti/ article)
Placement (03-humanised): title Y, H1 Y, first 100 words Y (lead, sentence 1), H2 Y (#kakvo-pravi, „AI асистентът“)
Relevance score: 86/100 (alignment 23/25 | entities 30/35 | questions 21/25 | on-page 12/15)
```

QUERY ALIGNMENT
- Main term appears exactly once in each required slot: title („AI асистент за бизнеса…“), H1 („AI асистент и чатбот за Вашия бизнес“), lead sentence 1 („BizGrow изгражда AI асистент…“, word 3), H2 #kakvo-pravi („Какво прави AI асистентът за Вашия бизнес“, grammatical variant).
- Extra exact-match uses outside the slots: FAQ q1 („AI асистентът“) and FAQ q5 („AI асистент“). Two FAQ uses read as light stuffing; q1 trimmed to „асистентът“, q5 kept because „колко струва ai асистент“ is the buyer's own phrasing of the price question.
- One term per page: no other address's main term is targeted. Checked: „ai автоматизация“ (/) absent; „автоматизация на бизнес процеси“ (/avtomatizacii/) absent, the link anchor is „автоматизациите за бизнеса“; „безплатна диагностика за бизнеса“ (/diagnostika/) absent as exact phrase (only „безплатната диагностика“ and the approved CTA); „маркетинг в социалните мрежи“ absent („пишат в социалните мрежи“ is a passing phrase); „seo копирайтинг“, „реклама в гугъл“, „seo оптимизация“ absent.
- „чатбот“: H1 and one defining sentence in #kakvo-pravi. Natural, not targeted, no extra use added.

ENTITY COVERAGE
- PRESENT: Messenger, Instagram, WhatsApp; денонощно; collecting the contact; training on the business's own information; repeated questions (цени, работно време, доставка, наличности); hotel guest assistant in any language with live availability and prices; courier-connected parcel status; real-estate enquiry qualification and viewing slots; process (безплатна диагностика, 30-минутен разговор, доклад до 48 часа, изграждане обикновено до 2 седмици, поддръжка с кратък месечен отчет); price formation without a number; no long-term contracts; transparent prices; „Работим по GDPR“; human control; nine canon audience groups; chatbot explained on first use.
- MISSING (canon-supported): secondary synonym „виртуален асистент“ (30 searches, KD 0) is absent; it can be added in one honest sentence in #kakvo-pravi. „AI асистент за бизнеса“ sits in the title only, which is enough.
- MISSING (not canon, NOT added): assistant on the client's website („чатбот за сайт“), handoff to a person beyond collecting the contact, languages for non-hotel assistants, AI model/platform, data location. These remain owner items.
- ORPHANED: none.

UNANSWERED BUYER QUESTIONS
- „Отговаря ли на английски и други езици?“: answered in the body for hotels only (#za-kogo, #primeri); no FAQ. A canon-only FAQ is possible for the hotel guest assistant, but the FAQ list is already at the 8-item ceiling and the non-hotel answer needs the owner. Logged as a candidate (FLAGS), not added.
- „Кой AI модел / платформа?“: Tier 3, not answered (correct).
- „Готова платформа или изграден асистент?“: vendor comparison not allowed, skipped (correct).
- All other brief questions are answered in body + FAQ.

SYNONYM FIELD
- Owner words present: „асистент в чата“ (implied), „отговор“, „запитване“, „контакт“, „свързване на програмите, които вече ползвате“. No „лийд“, no unexplained „интеграция“. Good.

ON-PAGE / DEFECTS
- Title 55 characters incl. „ | BizGrow“ (python count), unique, no em-dash. OK.
- Meta description 143 characters (python count), contains the main term, no em-dash, „безплатна“ only for the diagnosis. OK.
- One H1; 8 H2 (within 6–8); no H3 needed. OK.
- Internal links only from conversion-links.md: /avtomatizacii/, /diagnostika/; tokens {{BOOKING_URL}} ×2 (one per section), {{EMAIL}} ×1. OK.
- FAQ: 8 entries (within 6–8), 1–3 sentences each, none repeats a body heading word for word. OK.
- Defect 1 (minor): FAQ q1 carries an extra exact-match main term. Fixed.
- Defect 2 (minor): ContentPage `label`, `summary`, `eyebrow` not yet proposed. Added below.

LINKS TO ADD
- None required. Body has 2 contextual links (/diagnostika/, /avtomatizacii/), within the 1–3 rule. `related` = /diagnostika/, /avtomatizacii/, /socialni-mrezhi/.

FAQ CANDIDATES
- Kept: all 8 from Step 3 (q1 reworded to drop the extra main term).
- Candidate not added (ceiling + owner dependency): „Отговаря ли асистентът на английски и други езици?“.

---

## PHASE 2: OPTIMISED PAGE

Page: /ai-asistent/ | Locale: bg | Type: new-page | Main term: ai асистент

META
- title: „AI асистент за бизнеса в Messenger и WhatsApp | BizGrow“ (55 characters)
- meta_description: „AI асистент, който отговаря на клиентите Ви в Messenger, Instagram и WhatsApp денонощно. Безплатна диагностика и доклад с ясни цени до 48 часа.“ (143 characters)

CONTENTPAGE FIELDS
- label: „AI асистент“ (11 characters; breadcrumb/menu name)
- summary: „Асистент в Messenger, Instagram и WhatsApp, който отговаря на клиентите Ви денонощно с информацията на Вашия бизнес.“ (116 characters; one sentence for cards, deliberately without the exact main term so cards on other pages do not repeat it)
- eyebrow: „Messenger, Instagram и WhatsApp“ (short kicker above the H1; avoids „AI автоматизации“, which is too close to the home page's main term)
- service (schema name, from brief): „AI асистент и чатбот“
- related: /diagnostika/, /avtomatizacii/, /socialni-mrezhi/

secondary_keywords used:
- „ai асистент за бизнеса“ (title)
- „виртуален асистент“ (#kakvo-pravi, added)
- „чатбот за бизнес“ (natural variant in H1: „чатбот за Вашия бизнес“; not targeted)
- „чатбот messenger“ / „whatsapp чатбот“ (covered semantically: chatbot defined + channels named in the same section; no forced exact phrases)
- Not used: „ai чатбот“, „чатбот за фейсбук“ (would push „чатбот“ toward targeting; Facebook not named in canon), „чатбот за сайт“ (website assistant not in canon, owner item)

H1: AI асистент и чатбот за Вашия бизнес [OWNER CONFIRM: H1 of the new page]

LEAD (the `lead` field under the H1, no heading):
BizGrow изгражда AI асистент, който отговаря на клиентите Ви в Messenger, Instagram и WhatsApp денонощно и събира контакта им, когато не може да помогне. Асистентът е обучен на собствената информация на Вашия бизнес и поема повтарящите се въпроси за цени, работно време, доставка и наличности.

## Какво прави AI асистентът за Вашия бизнес {#kakvo-pravi}

Чатботът е програма, която отговаря автоматично на съобщенията, които клиентите пишат в чата. Асистентът, който изграждаме, работи като виртуален асистент в чата и отговаря на въпросите на клиентите Ви в Messenger, Instagram и WhatsApp с информацията на Вашия бизнес.

Асистентът работи денонощно, затова съобщение, изпратено вечер или в почивен ден, може да получи отговор веднага. Така клиентът може да научи това, което търси, без да чака началото на работния ден.

Когато въпросът излиза извън информацията, с която асистентът разполага, той събира контакта на клиента. Запитването остава при Вас и Вие решавате кой от екипа и кога да се свърже с човека.

## Кои въпроси и задачи поема асистентът {#zadachi}

Асистентът е обучен на собствената информация на Вашия бизнес. Той поема въпросите, на които иначе Вие или служителите Ви отговаряте по няколко пъти всеки ден.

- Цени на продуктите и услугите Ви.
- Работно време и почивни дни.
- Условия и срокове за доставка.
- Наличност на стоки, стаи или свободни часове.
- Името и контакта на клиента, когато асистентът не може да помогне.

Ако освен отговорите в чата търсите и онлайн записване с напомняния, автоматични оферти или свързване на програмите, които вече ползвате, разгледайте [автоматизациите за бизнеса](/avtomatizacii/).

## За кои бизнеси е подходящ асистентът {#za-kogo}

Работим с малки бизнеси, чиито клиенти пишат в социалните мрежи и в WhatsApp и често задават едни и същи въпроси. Сред тях са:

- ресторанти и кафенета;
- хотели и къщи за гости;
- салони;
- онлайн магазини;
- търговски обекти и шоуруми;
- клиники и практики;
- автосервизи и майстори;
- агенции за недвижими имоти;
- фирми, които работят с други фирми (B2B).

В някои отрасли асистентът поема и по-специфични задачи:

- **Хотели и къщи за гости.** Асистентът за гости отговаря на всеки език, денонощно, с актуалната наличност и цените на стаите.
- **Онлайн магазини.** Асистентът е свързан с куриера и сам отговаря на въпроса „Къде ми е поръчката?“ със статуса на пратката.
- **Недвижими имоти.** Асистентът отделя сериозните запитвания от останалите и предлага на тези клиенти свободни часове за оглед.

## Как протича работата {#proces}

Работата започва с [безплатната диагностика](/diagnostika/). На страницата избирате вида на бизнеса си, отбелязвате проблемите, които познавате, виждате ориентировъчно колко часа седмично Ви отнемат и запазвате разговор.

1. **Безплатна диагностика и 30-минутен разговор.** Разглеждаме къде бизнесът Ви губи време, включително съобщенията, които остават без отговор.
2. **Доклад до 48 часа.** Получавате доклад с приоритизирани решения и ясни еднократни цени за всяко от тях.
3. **Изграждане.** Изграждаме и настройваме асистента, обикновено до 2 седмици.
4. **Поддръжка.** След старта поддържаме асистента и Ви изпращаме кратък месечен отчет.

Диагностиката не Ви задължава с нищо. Вие решавате дали и кои от предложените в доклада решения да изградим.

[Запазете безплатна диагностика]({{BOOKING_URL}})

## Какво получавате {#kakvo-poluchavate}

- **Асистент в Messenger, Instagram и WhatsApp**, обучен на информацията на Вашия бизнес и настроен да отговаря денонощно.
- **Контактите на клиентите**, на които асистентът не е могъл да помогне, за да продължите разговора лично.
- **Доклад с ясни еднократни цени**, който получавате преди началото на работата.
- **Поддръжка с кратък месечен отчет** след изграждането.

Асистентът е инструмент, който Вашият бизнес използва под Ваш контрол. Запитванията, които изискват преценка, остават за Вас и Вашия екип.

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
a = "Асистентът е инструмент, който поема повтарящите се въпроси в чата. Запитванията, които изискват преценка, остават за Вас и Вашия екип."

[[faq]]
q = "Как се отнасяте към данните на клиентите ми?"
a = "Работим по GDPR. Конкретните въпроси за данните на Вашия бизнес можете да обсъдите в 30-минутния разговор по време на диагностиката."

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
| label | „AI асистент“ (navigation/breadcrumb, not body copy) | 1 |

Body paragraphs and the other 7 H2s use „асистентът“ / „асистента“ only. „чатбот“: H1 + one defining sentence.

## INVENTORY CHECK (00-inventory.md, all items present, none weakened)

1–2. {{BOOKING_URL}} CTA in #proces and #sledvashta-stapka (one per section); {{EMAIL}} in #sledvashta-stapka. Unchanged.
3–4. /diagnostika/ in #proces; /avtomatizacii/ in #zadachi. Unchanged.
5–9. Canon capabilities (channels, денонощно, contact, own information, hotel, courier, real estate): lead, #kakvo-pravi, #zadachi, #za-kogo, #kakvo-poluchavate, #primeri, FAQ 1–4. Unchanged; one sentence in #kakvo-pravi gained „работи като виртуален асистент в чата“ with no new fact.
10. Process with „30-минутен разговор“, „до 48 часа“, „обикновено до 2 седмици“, „кратък месечен отчет“: #proces, FAQ 6. Unchanged.
11–12. Price formation without a number, no long-term contracts, transparent prices, „Работим по GDPR“: #usloviya, FAQ 5, FAQ 8. Unchanged.
- Example label in #primeri, same section. Unchanged.

## FLAGS

- [OWNER CONFIRM: H1 of the new page] (H1 line). Carried.
- [OWNER CONFIRM: example scenarios adapted from the „Скрити проблеми“ checker pain lines, with their numbers] (#primeri). Carried.
- For `[[owner_items]]` at Step 6 (carried, not in text): [OWNER CONFIRM: assistant on the client's website]; [OWNER CONFIRM: languages for non-hotel assistants]; [OWNER CONFIRM: handoff and contact delivery]; [OWNER CONFIRM: model/platform and data location, only if the owner wants them on the page]; [DATA NEEDED: support pricing model, if the owner wants it explained].
- New, for `[[owner_items]]`: [OWNER CONFIRM: label „AI асистент“, summary and eyebrow „Messenger, Instagram и WhatsApp“ for the ContentPage card/breadcrumb].
- SEO note for owner: if the website assistant is confirmed, „чатбот за сайт“ becomes usable and the language FAQ („Отговаря ли асистентът на английски и други езици?“) can replace or join the list (stay within 8).
- Claim watch for Step 5: „може да получи отговор веднага“ (#kakvo-pravi) is hedged with „може“; keep the hedge, it is not a response-time promise.
- [VERIFY]: none. [LINK NEEDED]: none. New external facts: none.

## CHANGE SUMMARY

1. Main term confirmed once each in title, H1, lead sentence 1 and the #kakvo-pravi H2; extra exact-match removed from FAQ q1 („AI асистентът“ → „асистентът“), FAQ q5 kept as buyer phrasing.
2. Added secondary „виртуален асистент“ in one canon-safe sentence in #kakvo-pravi; „чатбот“ left at H1 + definition, not targeted (reserved for /saveti/).
3. Title (55 chars) and meta description (143 chars) kept from Step 3 after python count; both within limits, no em-dash, no banned or price terms.
4. Proposed ContentPage fields: label „AI асистент“, summary (116 chars, one sentence, no new fact), eyebrow „Messenger, Instagram и WhatsApp“, related /diagnostika/, /avtomatizacii/, /socialni-mrezhi/.
5. No sibling main term targeted, no new links, facts, numbers or FAQs; 8 H2, 8 FAQ, all inventory items, the example label and every flag preserved.
