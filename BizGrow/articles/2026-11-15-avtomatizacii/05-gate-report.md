# 05-GATE-REPORT | /avtomatizacii/ (BizGrow, new-page, bg), run 2026-11-15

## PHASE 1 — EVALUATION (on 04-seo.md as received)

```
BRAND COMPLIANCE SCORECARD — /avtomatizacii/ (bg)
Verdict: PASS WITH FIXES
Total: 86/100 (before fixes) → 93/100 (after Phase 2)
Voice 18/20 | Language 14/15 | Trust & claims 15/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 11/15 → 14/15
```

BLOCKING CHECKS
1. NOTHING LOST (new page: required items in 00-inventory.md): PASS. 19/19 present (see INVENTORY DIFF).
2. FACTS ALLOWED LIST: FAIL, mechanically fixable. Two unflagged statements went beyond the canon:
   - `kak-rabotim` intro „а след доклада Вие избирате кои решения да изградим“, bullet „Изграждаме избраните решения“ and FAQ 4 „След като изберете решенията от доклада“. The canon says: report with prioritised fixes and one-off prices per fix; the diagnosis commits to nothing. It does not say the client picks a subset of fixes. → reworded to canon wording; owner item added (see below).
   - `klienti-i-zapisvania` „а пропуснатите обаждания често означават пропуснати клиенти“: an unsourced outcome claim („често“) not in the canon or in the owner's fix lines. → cut; the sentence now states only that someone from the team must be available.
   - `dokumenti` listing bullet „публикува на няколко портала, обновява я и я сваля от тях“ (carried `[VERIFY]`): matches the owner line in 00-current.md („Публикуване веднъж: системата качва, обновява и сваля навсякъде.“), which the canon allows to be stated as written. → wording kept; the inline `[VERIFY]` marker is cleared on this documented owner evidence and recorded under FLAGS (not silently dropped).
   - `kakvo-e` ¶2 „Правилата определяме заедно с Вас, а Вие решавате кои задачи остават в ръцете на Вашите хора.“ already carries `[OWNER CONFIRM]`; passed through unchanged. Step 6 must turn it into an `[[owner_items]]` entry and keep the sentence out of the content file unless the owner confirms it.
3. BANNED CLAIMS: PASS. No guarantee, price, offer, testimonial, hype word; „безплатн*“ only for the diagnosis.
4. NUMBERS: PASS. Only 30 минути, 48 часа, „обикновено до 2 седмици“. No owner hours used.
5. HYPOTHETICAL LABEL: N/A (no example scenario on the page).
6. GDPR WORDING: PASS on wording („Работим по GDPR“ only). MODERATE: FAQ 7 asked „Как се отнасяте към данните на моите клиенти?“ and answered only „Работим по GDPR.“, which reads as evasive. → question reworded to match the only canon answer („Работите ли по GDPR?“ / „Да, работим по GDPR.“); `[DATA NEEDED]` kept.
7. REGISTER: PASS. Zero „ти“ forms (scripted scan of body, FAQ, title, meta; the one hit „те“ in `kakvo-e` ¶2 is the 3rd-person plural pronoun). Formal pronouns capitalised.
8. CTA RULES: PASS. One `[Запазете безплатна диагностика]({{BOOKING_URL}})` (#tsena, standalone paragraph), `{{EMAIL}}` once (#tsena, standalone paragraph). No hard-coded URL or address, no urgency.
9. ONE TERM PER PAGE: PASS. Main term „автоматизация на бизнес процеси“ (keyword-map row for /avtomatizacii/) in title, H1, lead (first 100 words), H2 #kakvo-e, and meta. No sibling main term (ai автоматизация, ai асистент, seo копирайтинг, маркетинг в социалните мрежи, реклама в гугъл, seo оптимизация, безплатна диагностика за бизнеса) in title, H1 or any H2.
10. LINKS & ANCHORS: PASS. Body links /ai-asistent/ and /diagnostika/ (both in conversion-links.md); section ids unchanged; no `#anchor` links.
11. BIZGROW VOICE: PASS with one moderate: „B2B фирми“ used without explanation (jargon rule). → explained on first use in #oferti.

CRITICAL (mechanically fixable, fixed in Phase 2)
- „Вие избирате кои решения да изградим“ / „избраните решения“ / „След като изберете решенията от доклада“ → check 2 → reworded to canon (diagnosis commits to nothing; report; build usually up to 2 weeks); owner item.
- „пропуснатите обаждания често означават пропуснати клиенти“ → check 2 / no-outcome-claims → cut.

MODERATE
- FAQ 7 question/answer mismatch → question reworded to fit the owner's wording.
- „B2B“ unexplained → „(фирми, които продават на други фирми)“ on first use.
- `[VERIFY]` on the listing bullet: owner source line confirms „качва, обновява и сваля навсякъде“ → marker cleared with evidence, logged below.

SEO LIMITS (python len)
- Title „Автоматизация на бизнес процеси: записване, оферти | BizGrow“ = 60 chars incl. suffix, no em-dash. PASS (at the limit; do not lengthen).
- Meta = 151 chars, contains the main term, no em-dash. PASS.
- Summary 122 chars, one sentence. Label „Автоматизации“. Eyebrow omitted.
- Em-dashes in page copy: 0. En-dashes as dashes: 0. Exclamation marks: 0.

OWNER ITEMS TO RAISE (for Step 6)
1. [OWNER CONFIRM] `kakvo-e`: „Правилата определяме заедно с Вас, а Вие решавате кои задачи остават в ръцете на Вашите хора.“ (carried from Step 2).
2. [OWNER CONFIRM, new at Step 5] Can the client choose only some of the fixes in the report (per-fix one-off prices suggest it)? If yes, `kak-rabotim` and FAQ 4 may say „Вие избирате кои решения да изградим“ / „Изграждаме избраните решения“ again.
3. [OWNER CONFIRM] `za-kogo`: hotels and guest houses mapping (checker maps no booking/reminder automation to hotels).
4. [OWNER CONFIRM] FAQ 5: whether replacing a program is ever part of a fix.
5. [DATA NEEDED] `klienti-i-zapisvania`: reminder channel (SMS / имейл / съобщение); blocks secondary „sms напомняне“.
6. [DATA NEEDED] FAQ 7: data handling beyond „Работим по GDPR“ (where data is stored, who has access are Tier 3).
7. [OWNER ITEM, optional] FAQ candidates not added: „Замества ли автоматизацията служителите?“, „Какъв софтуер използвате?“, „Трябва ли да знам програмиране?“.
8. [INFO, cleared at Step 5] Listing bullet „обновява я и я сваля“: matches the owner's checker fix line (00-current.md, estate). Step 6 may list it as a confirm-by-reading owner item if it wants a sign-off; no inline marker remains.

VOICE NOTES (protect during later steps)
- Problem → what is built → for whom → process → price/terms order; paragraphs then one list per section (renderer shows paragraphs before bullets).
- Business types attached to each capability come from the checker `t` field; keep them as they are.
- „помага за по-малко неявявания“ is the softened form of the owner's „намаляват неявяванията“; do not strengthen it.
- Keep „обикновено“ in every build-time mention.

## PHASE 2 — FIXED PAGE

Page: /avtomatizacii/ | Locale: bg | Type: new-page | Main term: автоматизация на бизнес процеси

TITLE (60 chars incl. " | BizGrow"): Автоматизация на бизнес процеси: записване, оферти | BizGrow

META_DESCRIPTION (151 chars): Автоматизация на бизнес процеси за малки бизнеси: онлайн записване с напомняния, автоматични оферти в PDF, фактури и табло с показатели в реално време.

LABEL: Автоматизации

SUMMARY (122 chars, one sentence): Изграждаме онлайн записване с напомняния, автоматични оферти, документи и фактури, свързани програми и табло с показатели.

EYEBROW: omitted (optional; if the template needs one: „Услуги“).

SERVICE (schema): Автоматизация на бизнес процеси

H1: Автоматизация на бизнес процеси

LEAD (ContentPage `lead`, no heading):
BizGrow изгражда автоматизация на бизнес процеси за малки бизнеси в България, от онлайн записването и офертите до документите и таблото с показатели. Първо откриваме къде Вашият бизнес губи време, след това изграждаме решенията, които поемат повтарящата се ръчна работа.

## Какво е автоматизация на бизнес процеси {#kakvo-e}

Във всеки бизнес има задачи, които се повтарят всеки ден и следват едни и същи правила. Такива са записването на час, напомнянето към клиента, писането на оферта, издаването на фактура и пренасянето на данни от една програма в друга.

Софтуерът за автоматизация изпълнява тези задачи по зададени правила, така че те не зависят от това дали някой от екипа е свободен в момента. Правилата определяме заедно с Вас, а Вие решавате кои задачи остават в ръцете на Вашите хора. [OWNER CONFIRM: "rules agreed with the client" and "the client decides what stays manual" describe how the work goes; canon rule 7 frames automation as a tool under the client's control, but the canon does not describe this step]

Отговорите на съобщенията в Messenger, Instagram и WhatsApp се поемат от AI асистент, програма, която отговаря на клиентите в чата. На него е посветена отделна страница: [AI асистент и чатбот за бизнеса](/ai-asistent/). Автоматизациите на тази страница са подредени по области на работа: записвания, оферти, документи и данни.

## Онлайн записване, напомняния и резервации {#klienti-i-zapisvania}

Когато всеки час се записва по телефона, някой от екипа трябва да е на разположение, за да вдигне. Онлайн записването позволява на клиентите сами да изберат свободен час или маса. Резервациите се синхронизират с календара, така че целият график е на едно място.

Тези решения се използват най-вече в ресторанти и заведения, салони, клиники и кабинети, както и в автосервизи.

- **Онлайн записване и онлайн резервации.** Клиентът избира свободен час или маса, а записването влиза директно в календара.
- **Автоматични потвърждения и напомняния.** Клиентът получава потвърждение при записването и напомняне преди часа си, което помага за по-малко неявявания. [DATA NEEDED: reminder channel (SMS, имейл, съобщение); canon says only „напомняния“; keyword-map secondary „sms напомняне“ depends on this]
- **Списък с чакащи.** Когато някой откаже, освободеният час се предлага на клиентите от списъка с чакащи.
- **Съобщения за статуса на ремонта.** Клиентът на автосервиза получава автоматично съобщение докъде е стигнал ремонтът, без да се налага да звъни.

## Автоматични оферти: от запитване до готов PDF {#oferti}

Когато всяка оферта се пише на ръка, клиентът чака отговор, а запитванията се трупат. Автоматичните оферти съкращават пътя от запитването до готовото предложение.

Офертите от формуляр са подходящи за B2B фирми (фирми, които продават на други фирми), магазини и шоуруми, автосервизи и агенции за недвижими имоти. Офертата от снимки е подходяща за автосервизи и B2B фирми.

- **Оферта от формуляр.** Клиентът попълва кратък формуляр, а системата подготвя оферта в PDF и я изпраща на имейла му.
- **Оферта от снимки.** Клиентът изпраща снимки и попълва кратък формуляр, а от тях се подготвя оферта.

## Документи, фактури и свързани програми {#dokumenti}

В много малки бизнеси едни и същи данни се пренаписват ръчно във фактури, договори, таблици и няколко програми. Автоматизацията на документи поема тази работа, като фактурите, отчетите и таблиците се създават и подреждат сами по зададени правила. Автоматичното фактуриране намалява ръчното въвеждане на едни и същи данни.

Свързваме и програмите, които вече използвате, така че данните да се попълват сами. Това свързване се нарича интеграция.

Документите се автоматизират във всеки вид бизнес. Шаблоните за договори са подходящи най-вече за B2B фирми и агенции за недвижими имоти. Свързаните програми са полезни за онлайн магазини, магазини и шоуруми и B2B фирми, а публикуването на обяви е предназначено за агенциите за недвижими имоти.

- **Фактури, отчети и таблици.** Създават се и се подреждат автоматично, без ръчно копиране между файлове.
- **Шаблони за договори с автоматично попълване.** Данните на клиента и на сделката се попълват в шаблона, което предпазва от грешки при ръчно копиране.
- **Свързани програми.** Данните, въведени в една програма, се появяват автоматично и в останалите.
- **Обява, публикувана веднъж.** Обявата се въвежда на едно място, а системата я публикува на няколко портала, обновява я и я сваля от тях.

## Табло с показатели и резюме след среща {#danni}

Таблото с показатели (дашборд) събира основните числа на бизнеса на едно място и ги показва в реално време. Така не се налага да ги търсите в различни програми и таблици, за да видите как върви работата. Таблото е полезно за всеки вид бизнес.

AI резюмето след среща подрежда изводите, задачите и следващите стъпки от разговора в кратък текст. Това решение е предназначено най-вече за B2B фирми.

## За кои бизнеси е подходяща автоматизацията {#za-kogo}

Различните бизнеси губят време на различни места, затова и полезните автоматизации се различават. Кои решения имат смисъл за Вашия бизнес, показва [безплатната диагностика](/diagnostika/).

- **Ресторанти и заведения:** онлайн резервации на маси, напомняния и списък с чакащи.
- **Хотели и къщи за гости:** автоматизация на документи и табло с показатели, а на въпросите на гостите за свободни места и цени отговаря AI асистентът. [OWNER CONFIRM: the checker maps no booking/reminder automation to hotels; confirm whether online reservations for hotels belong on this page]
- **Салони:** онлайн записване, напомняния и списък с чакащи.
- **Онлайн магазини:** свързани програми, автоматични документи и табло с показатели.
- **Магазини и шоуруми:** автоматични оферти и свързани програми.
- **Клиники и кабинети:** онлайн записване, напомняния и списък с чакащи.
- **Автосервизи и майстори:** онлайн записване, съобщения за статуса на ремонта и оферти от снимки.
- **Недвижими имоти:** автоматични оферти, шаблони за договори и обяви, публикувани веднъж.
- **B2B фирми:** оферти, шаблони за договори, свързани програми и AI резюме след среща.

## Как протича работата {#kak-rabotim}

Работата започва с безплатна диагностика, която не Ви обвързва с нищо, и продължава с доклад, изграждане и поддръжка.

- **Безплатна диагностика и 30-минутен разговор.** Разговаряме за това къде Вашият бизнес губи време и кои задачи се повтарят.
- **Доклад до 48 часа.** Получавате доклад с приоритизирани решения и ясни еднократни цени.
- **Изграждане.** Изграждаме решенията от доклада, обикновено до 2 седмици.
- **Поддръжка.** След внедряването предлагаме поддръжка с кратък месечен отчет.

## Цена и условия {#tsena}

Цената е еднократна за всяко решение и зависи от това какво се изгражда. Посочваме я в доклада след безплатната диагностика, така че я знаете, преди да решите дали да продължите.

Не работим с дългосрочни договори и цените ни са прозрачни. Диагностиката не Ви обвързва с нищо. Работим по GDPR.

Първата стъпка е безплатната диагностика, в която заедно преглеждаме кои автоматизации имат смисъл за Вашия бизнес.

[Запазете безплатна диагностика]({{BOOKING_URL}})

Ако предпочитате да пишете, изпратете ни имейл на {{EMAIL}}.

---

## FAQ

1. **q:** Кои задачи в малкия бизнес могат да се автоматизират?
   **a:** Подходящи са повтарящите се задачи с ясни правила: онлайн записване и напомняния, оферти, фактури и други документи, договори по шаблон, пренасяне на данни между програми и табло с показатели. Кои от тях имат смисъл за Вас, се вижда при безплатната диагностика.

2. **q:** Откъде да започна, ако не знам какво да автоматизирам?
   **a:** Започнете с безплатната диагностика и 30-минутния разговор. До 48 часа получавате доклад с приоритизирани решения, от който се вижда какво да се направи първо.

3. **q:** Колко струва автоматизацията?
   **a:** Цената е еднократна за всяко решение и зависи от това какво се изгражда. Посочваме я в доклада след безплатната диагностика и не работим с дългосрочни договори.

4. **q:** Колко време отнема изграждането?
   **a:** След доклада с решенията изграждането обикновено отнема до 2 седмици.

5. **q:** Трябва ли да сменя програмите, които използвам?
   **a:** Целта е да свържем програмите, които вече използвате, така че данните да се попълват сами. [OWNER CONFIRM: canon says only "connecting the systems a business already uses"; confirm whether replacing a program is ever part of a fix]

6. **q:** Какво се случва, след като автоматизацията заработи?
   **a:** След внедряването предлагаме поддръжка с кратък месечен отчет за работата на решенията.

7. **q:** Работите ли по GDPR?
   **a:** Да, работим по GDPR. [DATA NEEDED: anything more specific (where data is stored, who has access) is Tier 3 and needs the owner]

8. **q:** Обвързва ли ме диагностиката с договор?
   **a:** Не. Диагностиката не Ви обвързва с нищо, а ако решите да продължите, работим без дългосрочни договори.

---

## RELATED (3 sibling paths, all in conversion-links.md)

- /ai-asistent/
- /diagnostika/
- /seo-statii/

## SECONDARY KEYWORDS USED

софтуер за автоматизация; онлайн записване; онлайн резервации; автоматични оферти; автоматизация на документи; автоматично фактуриране; табло с показатели. Not used: sms напомняне (blocked by `[DATA NEEDED]`), софтуерна автоматизация (would be stuffing).

## CHANGES MADE AT STEP 5 (surgical; everything else byte-identical to 04-seo.md)

1. `klienti-i-zapisvania` ¶1, sentence 1: „…трябва да е на разположение, а пропуснатите обаждания често означават пропуснати клиенти.“ → „…трябва да е на разположение, за да вдигне.“ (unsourced outcome claim removed).
2. `kak-rabotim` intro: „Работата започва с безплатна диагностика, а след доклада Вие избирате кои решения да изградим.“ → „Работата започва с безплатна диагностика, която не Ви обвързва с нищо, и продължава с доклад, изграждане и поддръжка.“ (canon wording).
3. `kak-rabotim` bullet 3: „Изграждаме избраните решения, обикновено до 2 седмици.“ → „Изграждаме решенията от доклада, обикновено до 2 седмици.“
4. FAQ 4: „След като изберете решенията от доклада, изграждането обикновено отнема до 2 седмици.“ → „След доклада с решенията изграждането обикновено отнема до 2 седмици.“
5. FAQ 7: q „Как се отнасяте към данните на моите клиенти?“ → „Работите ли по GDPR?“; a „Работим по GDPR.“ → „Да, работим по GDPR.“ (owner wording kept); `[DATA NEEDED]` kept, its "Step 4/5 may drop this FAQ" note removed because the FAQ now answers its own question.
6. `oferti` ¶2: „B2B фирми“ → „B2B фирми (фирми, които продават на други фирми)“ on first use.
7. `dokumenti` listing bullet: inline `[VERIFY]` marker cleared; wording unchanged; evidence = owner line „Публикуване веднъж: системата качва, обновява и сваля навсякъде.“ (00-current.md).

Unchanged: title, meta, label, summary, H1, lead, all section ids and headings, paragraphs-then-one-list structure, inline syntax (`**bold**`, `[label](/path/)` only), standalone CTA and `{{EMAIL}}` paragraphs, related, all other flags.

## INVENTORY DIFF (00-inventory.md vs fixed page)

1. Booking CTA → `{{BOOKING_URL}}`: #tsena, standalone, once. OK
2. `{{EMAIL}}`: #tsena, final standalone paragraph. OK
3. /diagnostika/: #za-kogo. OK
4. /ai-asistent/: #kakvo-e. OK
5. Booking + calendar + reminders + waitlist: #klienti-i-zapisvania. OK
6. Offers form → PDF; offer from photos: #oferti. OK
7. Document and invoice automation: #dokumenti. OK
8. Contract templates with auto-fill: #dokumenti. OK
9. Connecting existing systems: #dokumenti + FAQ 5. OK
10. Listing once to several portals: #dokumenti. OK
11. Real-time dashboard: #danni. OK
12. AI meeting summary: #danni. OK
13. Process, 4 canon steps: #kak-rabotim. OK
14. Policies (no long-term contracts, transparent prices, „Работим по GDPR“, diagnosis commits to nothing): #tsena (+ #kak-rabotim intro, FAQ 7, FAQ 8). OK
15. Price formation, no number: #tsena + FAQ 3. OK
16. Audience, 9 canon types: #za-kogo. OK
17. 30 минути / 48 часа / „обикновено до 2 седмици“: #kak-rabotim, FAQ 2, FAQ 4. OK
18. Example label: not triggered. N/A
19. FAQ: 8 entries. OK
Result: 19/19 (18 present + 1 N/A).

## FLAGS (pass-through)

- [OWNER CONFIRM] `kakvo-e`: rules agreed with the client / the client decides what stays with their people. (Step 6: owner item; keep the sentence out of the content file unless confirmed.)
- [OWNER CONFIRM, new at Step 5, no inline marker; text already reworded to canon] client choosing a subset of the report's fixes (`kak-rabotim`, FAQ 4).
- [OWNER CONFIRM] `za-kogo`: hotels and guest houses mapping.
- [OWNER CONFIRM] FAQ 5: whether replacing a program is ever part of a fix.
- [DATA NEEDED] `klienti-i-zapisvania`: reminder channel (SMS / имейл / съобщение); blocks „sms напомняне“.
- [DATA NEEDED] FAQ 7: data handling beyond „Работим по GDPR“.
- [VERIFY → cleared at Step 5] `dokumenti` listing bullet „обновява я и я сваля“: matches the owner checker line in 00-current.md; optional confirm-by-reading owner item.
- [OWNER ITEM, optional] FAQ candidates „Замества ли автоматизацията служителите?“, „Какъв софтуер използвате?“, „Трябва ли да знам програмиране?“ not included.
- [PORT NOTE] `{{BOOKING_URL}}` / `{{EMAIL}}` paragraphs in `tsena` are standalone so the port JSON can omit them (the template supplies the booking button, CtaBand and footer email).

## UPDATED SCORECARD (after Phase 2)

```
Verdict: PASS WITH FIXES (fixes applied; ready for Step 6)
Total: 93/100
Voice 19/20 | Language 14/15 | Trust & claims 18/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 14/15
Blocking checks 1–11: all PASS / N/A. Remaining: owner items above (flagged, not resolved).
```

## CANON ADDITIONS

none
