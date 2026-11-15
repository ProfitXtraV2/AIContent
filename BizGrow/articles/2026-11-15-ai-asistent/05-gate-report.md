# 05-gate-report: /ai-asistent/ (bg, new-page, LOOP 1 re-run)

Input: 04-seo.md (LOOP 1 structure). Checked against 00-current.md, 00-inventory.md, 00-brief.md, keyword-map.md (row /ai-asistent/ + siblings), conversion-links.md, markets/bg/author.md (canon), reference/site-rules.md, reference/verification-policy.md. Structural constraint verified and preserved: in every section, paragraphs first, then at most one list, nothing after the list.

## PHASE 1: EVALUATION

```
BRAND COMPLIANCE SCORECARD — /ai-asistent/ (bg)
Verdict: PASS
Total: 91/100
Voice 18/20 | Language 13/15 | Trust & claims 19/20 | Usefulness 14/15 | Anti-AI 13/15 | SEO 14/15
```

Score above is for 04-seo.md as received. After the moderate fixes below: Voice 19 | Language 14 | Trust & claims 19 | Usefulness 14 | Anti-AI 14 | SEO 14 = 94/100.

### BLOCKING CHECKS

1. NOTHING LOST: PASS. New page; every 00-inventory.md item present. (1) Booking CTA „Запазете безплатна диагностика“ → {{BOOKING_URL}}: #sledvashta-stapka closing block (template-rendered; the template also renders „Запазете час“ under the lead and the CTA band after the FAQ). (2) {{EMAIL}} line: #sledvashta-stapka closing block. (3) /diagnostika/: #proces P1. (4) /avtomatizacii/: #zadachi P2. (5) Messenger/Instagram/WhatsApp, денонощно, collects the contact: lead, #kakvo-pravi, #zadachi list, FAQ 1–3. (6) Own information, repeated questions (цени, работно време, доставка, наличности): lead, #zadachi, FAQ 4. (7) Hotel guest assistant, any language, live availability and prices: #za-kogo list, #primeri. (8) Courier parcel status: #za-kogo list, #primeri. (9) Real-estate qualification + viewing slots: #za-kogo list, #primeri. (10) Process with 30-минутен разговор / до 48 часа / обикновено до 2 седмици / кратък месечен отчет: #proces list, #kakvo-poluchavate, FAQ 6. (11) Price formation without a number: #usloviya, FAQ 5. (12) No long-term contracts, transparent prices, „Работим по GDPR“: #usloviya, FAQ 5, FAQ 8. Example label: #primeri P1. Loop-1 note: the booking CTA no longer sits in #proces (loop 0 had it there); the inventory requires it at least once, so this is not a loss.
2. FACTS ALLOWED LIST: PASS. Every BizGrow statement maps to the canon (checker capabilities, process, price formation, policies, audience, „Диагностиката не Ви задължава с нищо“, the /diagnostika/ checker description). No vendor, model, platform, team, price, office, phone, data location or website-assistant claim. „Наличност на … свободни часове“ (#zadachi) is read as answering about availability (canon „наличности“, viewing slots); no booking-system claim is made on this page.
3. BANNED CLAIMS: PASS. Scan: 0 гарант*/гаранци*, 0 hype words, 0 №1/лидер/най-добр*, 0 currency or price digits, 0 промоци*/отстъпк*/отзив*, 0 „100%“, 0 сертиф*. All 9 occurrences of „безплатн*“ refer to the diagnosis (incl. the template CTA band „Първата стъпка е безплатна“). The only „!“ is inside the HTML comment marker.
4. NUMBERS: PASS. Canon: 30 (минути), 48 (часа), 2 (седмици, with „обикновено“). #primeri: 21:30, 23:00, „двадесет пъти“, „още 40“, „в полунощ“ come from the owner's „Скрити проблеми“ pain lines (00-current.md), inside the labelled example section, carrying [OWNER CONFIRM]. No other figures.
5. HYPOTHETICAL LABEL: PASS. „Примерни сценарии по нашия метод, не данни от конкретни клиенти.“ is P1 of #primeri, same section as the examples. The #za-kogo industry bullets are canon capabilities, not scenarios.
6. GDPR WORDING: PASS. „Работим по GDPR.“ only (#usloviya, FAQ 8). No data-location, certification or compliance claim.
7. REGISTER: PASS. Scan: 0 „ти“ forms, 0 lowercase вие/ви/вас/ваш* in direct address. FAQ questions in the buyer's first person („моя бизнес“, „клиентите ми“) are correct.
8. CTA RULES: PASS. One booking CTA in the body (#sledvashta-stapka), approved wording, token {{BOOKING_URL}}; email only as {{EMAIL}}; no hard-coded URL or address; no urgency wording.
9. ONE TERM PER PAGE: PASS. „ai асистент“ once each in title (55 chars), H1, lead sentence 1, one H2 (#kakvo-pravi); extra uses in meta, FAQ q5 (buyer phrasing) and label are not stuffing. No sibling main term targeted („ai автоматизация“, „автоматизация на бизнес процеси“, „безплатна диагностика за бизнеса“, „seo копирайтинг“, „маркетинг в социалните мрежи“, „реклама в гугъл“, „seo оптимизация“ absent as exact phrases). „чатбот“ only in the H1 and the defining sentence.
10. LINKS & ANCHORS: PASS. Body links /diagnostika/, /avtomatizacii/; related /diagnostika/, /avtomatizacii/, /socialni-mrezhi/; all in conversion-links.md. New section ids; no EN pair.
11. BIZGROW VOICE: PASS. 0 exclamation marks in copy, 0 rhetorical questions („Къде ми е поръчката?“ is a quoted customer question), no slang, no hype, no fragment paragraphs, „чатбот“ and „B2B“ explained on first use.

STRUCTURE CHECK (template): PASS. #kakvo-pravi, #usloviya, #sledvashta-stapka: paragraphs only. #zadachi, #za-kogo, #proces, #kakvo-poluchavate, #primeri: paragraphs, then one unordered list, nothing after it. Preserved after the fixes.

### CRITICAL (blocks)
None.

### MODERATE (fixed surgically in Phase 2)
1. „Изграждаме такъв виртуален асистент за чата, който отговаря…“ (#kakvo-pravi P1) → Language: „който“ can attach to „чата“ → „Изграждаме такъв виртуален асистент, който отговаря…“ (secondary term „виртуален асистент“ kept).
2. „…изпратено вечер или в почивен ден, може да получи отговор и извън работно време. Така клиентът може да научи това, което търси, без да чака началото на работния ден.“ (#kakvo-pravi P2) → Language/Anti-AI: „вечер или в почивен ден“ already is „извън работно време“ (redundant), and „Така“ is a connective crutch (also opens FAQ 2 sentence 2) → „…изпратено вечер или в почивен ден, също може да получи отговор. Клиентът може да научи това, което търси, без да чака началото на работния ден.“ Both hedges („може“) kept; no response-time promise.
3. #za-kogo P1 is a one-sentence paragraph, and P1–P2 repeat „работ*“ three times („Работим с…“, „Работим и с…“, „фирми, които работят с други фирми“) → Voice (paragraphs of 2–4 sentences) / Language → P1 and P2 merged into one 3-sentence paragraph; „Работим и с автосервизи…“ → „Към тях спадат и автосервизи…“; „фирми, които работят с други фирми (B2B)“ → „фирми, които продават на други фирми (B2B)“. Same nine canon audience groups, same B2B explanation.
4. „**Template-rendered CTA, not in port strings:**“ (#sledvashta-stapka) → Voice/porting risk: an English porter note written as visible bold body text could be ported as a paragraph → removed; the HTML porter comment directly above it (kept verbatim) carries the same instruction. CTA line and {{EMAIL}} line unchanged.

Not changed (noted): „В чата асистентът поема следните въпроси и задачи.“ (#zadachi) is a functional list lead-in required by the paragraphs-then-list template, not a revealing signpost. FAQ 2 „Така съобщенията могат…“ kept (one „Така“ on the page after fix 2). „по няколко пъти всеки ден“ (#zadachi) is a frequency description, not a figure.

### OWNER ITEMS TO RAISE (for Step 6)
- [OWNER CONFIRM: H1 of the new page] („AI асистент и чатбот за Вашия бизнес“, keyword-map proposal).
- [OWNER CONFIRM: example scenarios adapted from the „Скрити проблеми“ checker pain lines, with their numbers] (#primeri).
- [OWNER CONFIRM: label „AI асистент“, summary and eyebrow „Messenger, Instagram и WhatsApp“ for the ContentPage card/breadcrumb].
- [OWNER CONFIRM: assistant on the client's website] (would unlock „чатбот за сайт“).
- [OWNER CONFIRM: languages for non-hotel assistants] (would unlock a language FAQ).
- [OWNER CONFIRM: handoff and contact delivery] (how collected contacts reach the business).
- [OWNER CONFIRM: model/platform and data location, only if the owner wants them on the page].
- [DATA NEEDED: support pricing model, if the owner wants it explained].

### PORTER NOTE FOR STEP 6 (not an owner item)
- The closing CTA and {{EMAIL}} line in #sledvashta-stapka are marked as template-rendered by Step 4. Step 6 confirms against the current `ContentPageView` whether they map to the template's buttons/CTA band and footer or to `paragraphs[]` strings (`[label]({{BOOKING_URL}})`, bare `{{EMAIL}}`); the wording is identical either way and the CTA must survive in one of the two.
- #proces list maps to `bullets` as written; if the template's numbered `steps` field is used, the four strings stay the same.

### VOICE NOTES (protect during later steps)
- Keep the hedges „може да получи отговор“, „може да научи“, „могат да получат отговор“, „обикновено до 2 седмици“, „ориентировъчно“.
- Keep the human-control sentences (#kakvo-pravi P3, #kakvo-poluchavate P1, FAQ 3, FAQ 7): they carry claim rule 7.
- Keep „чатбот“ at H1 + one definition; do not add more.
- Keep the example label as P1 of #primeri, verbatim.
- Keep the paragraphs-then-one-list order in every section.

---

## PHASE 2: CORRECTED PAGE

Page: /ai-asistent/ | Locale: bg | Type: new-page | Main term: ai асистент

META
- title: „AI асистент за бизнеса в Messenger и WhatsApp | BizGrow“ (55 characters)
- meta_description: „AI асистент, който отговаря на клиентите Ви в Messenger, Instagram и WhatsApp денонощно. Безплатна диагностика и доклад с ясни цени до 48 часа.“ (143 characters)

CONTENTPAGE FIELDS
- label: „AI асистент“
- summary: „Асистент в Messenger, Instagram и WhatsApp, който отговаря на клиентите Ви денонощно с информацията на Вашия бизнес.“
- eyebrow: „Messenger, Instagram и WhatsApp“
- service (schema name): „AI асистент и чатбот“
- related: /diagnostika/, /avtomatizacii/, /socialni-mrezhi/

H1: AI асистент и чатбот за Вашия бизнес [OWNER CONFIRM: H1 of the new page]

LEAD:
BizGrow изгражда AI асистент, който отговаря на клиентите Ви в Messenger, Instagram и WhatsApp денонощно и събира контакта им, когато не може да помогне. Асистентът е обучен на собствената информация на Вашия бизнес и поема повтарящите се въпроси за цени, работно време, доставка и наличности.

(Template-rendered under the lead, not in port strings: button „Запазете час“ → {{BOOKING_URL}}; button „Безплатна диагностика“ → /diagnostika/.)

## Какво прави AI асистентът за Вашия бизнес {#kakvo-pravi}

Чатботът е програма, която отговаря автоматично на съобщенията, които клиентите пишат в чата. Изграждаме такъв виртуален асистент, който отговаря на въпросите на клиентите Ви в Messenger, Instagram и WhatsApp с информацията на Вашия бизнес.

Асистентът работи денонощно, затова съобщение, изпратено вечер или в почивен ден, също може да получи отговор. Клиентът може да научи това, което търси, без да чака началото на работния ден.

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

Работим с малки бизнеси, чиито клиенти пишат в социалните мрежи и в WhatsApp и често задават едни и същи въпроси. Сред тях са ресторанти и кафенета, хотели и къщи за гости, салони, онлайн магазини, търговски обекти и шоуруми, клиники и практики. Към тях спадат и автосервизи и майстори, агенции за недвижими имоти и фирми, които продават на други фирми (B2B).

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

## MAIN-TERM PLACEMENT (unchanged by the fixes)

| slot | text |
|---|---|
| title | „AI асистент за бизнеса в Messenger и WhatsApp \| BizGrow“ |
| H1 | „AI асистент и чатбот за Вашия бизнес“ |
| first 100 words | lead sentence 1, „BizGrow изгражда AI асистент…“ |
| H2 | #kakvo-pravi „Какво прави AI асистентът за Вашия бизнес“ |
| meta description | opening words |
| FAQ | q5 „Колко струва AI асистент?“ (buyer phrasing) |

## INVENTORY CHECK (after fixes, all present, none weakened)

1–2. Booking CTA `[Запазете безплатна диагностика]({{BOOKING_URL}})` and the {{EMAIL}} line: #sledvashta-stapka closing block. Unchanged.
3–4. /diagnostika/ in #proces P1; /avtomatizacii/ in #zadachi P2. Unchanged.
5–9. Canon capabilities: lead, #kakvo-pravi, #zadachi, #za-kogo, #kakvo-poluchavate, #primeri, FAQ 1–4. Unchanged in meaning (fixes 1–2 reword #kakvo-pravi P1–P2 only).
10. Process with 30 минути, 48 часа, „обикновено до 2 седмици“, кратък месечен отчет: #proces list, #kakvo-poluchavate, FAQ 6. Unchanged.
11–12. Price formation without a number, no long-term contracts, transparent prices, „Работим по GDPR“: #usloviya, FAQ 5, FAQ 8. Unchanged.
- Example label: #primeri P1, verbatim. Unchanged.
- Audience: nine canon groups incl. B2B with explanation, #za-kogo P1 (fix 3 merged paragraphs only).

## FLAGS (carried, none resolved)

- [OWNER CONFIRM: H1 of the new page] (H1 line).
- [OWNER CONFIRM: example scenarios adapted from the „Скрити проблеми“ checker pain lines, with their numbers] (#primeri).
- For `[[owner_items]]` at Step 6 (not in text): [OWNER CONFIRM: label „AI асистент“, summary and eyebrow „Messenger, Instagram и WhatsApp“ for the ContentPage card/breadcrumb]; [OWNER CONFIRM: assistant on the client's website]; [OWNER CONFIRM: languages for non-hotel assistants]; [OWNER CONFIRM: handoff and contact delivery]; [OWNER CONFIRM: model/platform and data location, only if the owner wants them on the page]; [DATA NEEDED: support pricing model, if the owner wants it explained].
- SEO note for owner: if the website assistant is confirmed, „чатбот за сайт“ becomes usable, and the language FAQ („Отговаря ли асистентът на английски и други езици?“) can replace one entry (stay within 8).
- [VERIFY]: none. [LINK NEEDED]: none. New external facts: none.

## OWNER ITEMS (for Step 6)

1. H1 „AI асистент и чатбот за Вашия бизнес“ (new page, keyword-map proposal).
2. Example scenarios in #primeri adapted from the „Скрити проблеми“ pain lines, with their numbers (21:30, 23:00, двадесет пъти, полунощ, още 40).
3. ContentPage label „AI асистент“, summary and eyebrow „Messenger, Instagram и WhatsApp“.
4. Whether BizGrow also builds the assistant for the client's website.
5. Languages for assistants outside hotels.
6. How collected contacts reach the business (handoff).
7. AI model/platform and data location, only if the owner wants them on the page.
8. Support pricing model, if the owner wants it explained.

## CHANGE SUMMARY

1. #kakvo-pravi P1: removed „за чата“ before „който“ (ambiguous antecedent).
2. #kakvo-pravi P2: removed the redundant „и извън работно време“ and the „Така“ opener; hedges kept.
3. #za-kogo: P1 + P2 merged into one 3-sentence paragraph; repeated „работ*“ reworded; audience list and B2B explanation unchanged; still paragraphs then one list.
4. #sledvashta-stapka: removed the English bold porter line from the visible body; HTML porter comment, CTA and {{EMAIL}} line kept verbatim.
5. No fact, number, link, token, CTA, label, FAQ or flag added or removed. Title, meta, label, summary, eyebrow, FAQ and related unchanged. 0 em-dashes, 0 „ти“ forms.
