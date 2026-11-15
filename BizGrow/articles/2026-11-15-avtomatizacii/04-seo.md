# 04-SEO | /avtomatizacii/ (BizGrow, new-page, bg), run 2026-11-15

## PHASE 1 — AUDIT

```
SEO AUDIT — /avtomatizacii/ (bg)
Main term: автоматизация на бизнес процеси | Intent: commercial + informational (service page; SERP for the head term „автоматизация“ is informational)
Placement: title Y | H1 Y | first 100 words Y (lead, word 3) | H2 Y (#kakvo-e)
Exact-match count in page copy (H1 + lead + sections + FAQ): 3 (H1, lead, one H2) + title 1 + meta 1. No flooding.
Relevance score: 86/100 (alignment 24/25 | entities 30/35 | questions 20/25 | on-page 12/15 → 14/15 after Phase 2)
```

ONE TERM PER PAGE (sibling main terms, counted in page copy, title, meta, FAQ):
- ai автоматизация 0 | ai асистент: 3 passing mentions (kakvo-e ¶3 with link to /ai-asistent/, za-kogo hotels bullet), not targeted, no heading → OK
- seo копирайтинг 0 | маркетинг в социалните мрежи 0 | реклама в гугъл 0 | seo оптимизация 0 | безплатна диагностика за бизнеса 0 (only „безплатна(та) диагностика“, linked once to /diagnostika/) → OK
- „автоматизация“ alone (home secondary) is used only as a common noun, never as a heading target → OK

SECONDARY TERMS (keyword-map row), used naturally:
- софтуер за автоматизация: present („Софтуерът за автоматизация“, kakvo-e ¶2)
- онлайн записване / онлайн резервации: present (H2 + bullet „Онлайн записване и онлайн резервации“)
- автоматични оферти: present (H2 #oferti + ¶1)
- автоматизация на документи: present (dokumenti ¶1)
- автоматично фактуриране: present (dokumenti ¶1)
- табло с показатели: present (H2 #danni, lead, za-kogo)
- sms напомняне: NOT used, blocked by `[DATA NEEDED: reminder channel]`; canon says only „напомняния“. Not added.
- софтуерна автоматизация: not used; it would be a near-duplicate of „софтуер за автоматизация“ in the same paragraph (stuffing). Left out.

ENTITY COVERAGE
- PRESENT: online booking + calendar sync, reminders, waitlist, repair-status messages, offers form → PDF, offer from photos, documents, invoices, contract templates with auto-fill, connected programs („интеграция“ explained), listing once to several portals, real-time dashboard („дашборд“ explained), AI meeting summary, 9 canon business types, 4-step canon process (30 минути, 48 часа, обикновено до 2 седмици), price formation without a number, no long-term contracts, transparent prices, „Работим по GDPR“, client control (flagged).
- MISSING (coverable honestly): none. Reminder channel and tools/vendors are Tier 3 → stay flagged / owner items.
- ORPHANED: none.

BUYER QUESTIONS (brief) → coverage
- Какво е автоматизация на бизнес процеси? → H2 #kakvo-e. OK
- Кои процеси да автоматизирам първо? → FAQ 2 (diagnosis + report with prioritised fixes; no universal "first"). OK
- Подходяща ли е за моя тип бизнес? → H2 #za-kogo + FAQ 1. OK
- Трябва ли да сменя програмите? → FAQ 5 (flagged). OK
- Колко струва? → FAQ 3 + #tsena, canon level, no number. OK
- Колко време отнема? → FAQ 4 (обикновено до 2 седмици). OK
- Поддръжка след внедряването? → FAQ 6. OK
- GDPR / данни? → FAQ 7 („Работим по GDPR“, flagged). OK
- Замества ли автоматизацията служителите? → UNANSWERED as FAQ. The only answer available is the flagged #kakvo-e ¶2 wording (client decides what stays with their people, `[OWNER CONFIRM]`); adding it would make 9 FAQ (over 6–8) and repeat an unconfirmed claim → owner item, not added.
- Какъв софтуер използвате? → Tier 3 (vendors) → owner item, not added.
- Колко време се спестява? → only the owner's hours with the „на база типични случаи“ label; brief prefers no numbers → not added.

DEFECTS
- None blocking. Title, meta and card fields did not exist yet (written below). Section ids, paragraphs-then-one-list structure and inline syntax (`**bold**`, `[label](/path/)` only) are valid.
- Note: the lead precedes the #kakvo-e H2, so that H2 falls inside the first ~100 words of rendered text. Body copy carries the term once (lead); the H2 is the intended one-H2 placement, not flooding.

LINKS
- Body links: 2, `/ai-asistent/` (kakvo-e) and `/diagnostika/` (za-kogo). Both in conversion-links.md; within 1–3. Anchors are plain words („AI асистент и чатбот за бизнеса“, „безплатната диагностика“). No link added (a third would be decoration).
- CTA: `[Запазете безплатна диагностика]({{BOOKING_URL}})` once (#tsena, standalone). `{{EMAIL}}` once (#tsena, standalone). Tokens verbatim.
- No external links, no `[LINK NEEDED]`.

FAQ REVIEW (8 entries; target 6–8)
- All answers 1–3 complete formal sentences; none repeats a body heading word for word (H2s: „Какво е…“, „Онлайн записване…“, „Автоматични оферти…“, „Документи…“, „Табло…“, „За кои бизнеси…“, „Как протича работата“, „Цена и условия“).
- FAQ 3 (price): canon wording, no number. OK
- FAQ 7: one sentence („Работим по GDPR.“) + `[DATA NEEDED]`. Kept: a real buyer question answered in the owner's wording; Step 5 may drop it if the owner adds nothing (the page then has 7, still in range).
- FAQ 5: kept with `[OWNER CONFIRM]`.
- No changes to FAQ text.

FAQ CANDIDATES not added: „Замества ли автоматизацията служителите?“, „Какъв софтуер използвате?“, „Трябва ли да знам програмиране?“ (all need the owner).

## PHASE 2 — OPTIMISED PAGE

Page: /avtomatizacii/ | Locale: bg | Type: new-page | Main term: автоматизация на бизнес процеси

TITLE (60 chars incl. " | BizGrow", python len): Автоматизация на бизнес процеси: записване, оферти | BizGrow

META_DESCRIPTION (151 chars, python len; contains the main term): Автоматизация на бизнес процеси за малки бизнеси: онлайн записване с напомняния, автоматични оферти в PDF, фактури и табло с показатели в реално време.

LABEL: Автоматизации

SUMMARY (122 chars, one sentence): Изграждаме онлайн записване с напомняния, автоматични оферти, документи и фактури, свързани програми и табло с показатели.

EYEBROW: omitted (optional; outline default. If the template needs one: „Услуги“).

SERVICE (schema): Автоматизация на бизнес процеси

H1: Автоматизация на бизнес процеси

LEAD (ContentPage `lead`, no heading):
BizGrow изгражда автоматизация на бизнес процеси за малки бизнеси в България, от онлайн записването и офертите до документите и таблото с показатели. Първо откриваме къде Вашият бизнес губи време, след това изграждаме решенията, които поемат повтарящата се ръчна работа.

## Какво е автоматизация на бизнес процеси {#kakvo-e}

Във всеки бизнес има задачи, които се повтарят всеки ден и следват едни и същи правила. Такива са записването на час, напомнянето към клиента, писането на оферта, издаването на фактура и пренасянето на данни от една програма в друга.

Софтуерът за автоматизация изпълнява тези задачи по зададени правила, така че те не зависят от това дали някой от екипа е свободен в момента. Правилата определяме заедно с Вас, а Вие решавате кои задачи остават в ръцете на Вашите хора. [OWNER CONFIRM: "rules agreed with the client" and "the client decides what stays manual" describe how the work goes; canon rule 7 frames automation as a tool under the client's control, but the canon does not describe this step]

Отговорите на съобщенията в Messenger, Instagram и WhatsApp се поемат от AI асистент, програма, която отговаря на клиентите в чата. На него е посветена отделна страница: [AI асистент и чатбот за бизнеса](/ai-asistent/). Автоматизациите на тази страница са подредени по области на работа: записвания, оферти, документи и данни.

## Онлайн записване, напомняния и резервации {#klienti-i-zapisvania}

Когато всеки час се записва по телефона, някой от екипа трябва да е на разположение, а пропуснатите обаждания често означават пропуснати клиенти. Онлайн записването позволява на клиентите сами да изберат свободен час или маса. Резервациите се синхронизират с календара, така че целият график е на едно място.

Тези решения се използват най-вече в ресторанти и заведения, салони, клиники и кабинети, както и в автосервизи.

- **Онлайн записване и онлайн резервации.** Клиентът избира свободен час или маса, а записването влиза директно в календара.
- **Автоматични потвърждения и напомняния.** Клиентът получава потвърждение при записването и напомняне преди часа си, което помага за по-малко неявявания. [DATA NEEDED: reminder channel (SMS, имейл, съобщение); canon says only „напомняния“; keyword-map secondary „sms напомняне“ depends on this]
- **Списък с чакащи.** Когато някой откаже, освободеният час се предлага на клиентите от списъка с чакащи.
- **Съобщения за статуса на ремонта.** Клиентът на автосервиза получава автоматично съобщение докъде е стигнал ремонтът, без да се налага да звъни.

## Автоматични оферти: от запитване до готов PDF {#oferti}

Когато всяка оферта се пише на ръка, клиентът чака отговор, а запитванията се трупат. Автоматичните оферти съкращават пътя от запитването до готовото предложение.

Офертите от формуляр са подходящи за B2B фирми, магазини и шоуруми, автосервизи и агенции за недвижими имоти. Офертата от снимки е подходяща за автосервизи и B2B фирми.

- **Оферта от формуляр.** Клиентът попълва кратък формуляр, а системата подготвя оферта в PDF и я изпраща на имейла му.
- **Оферта от снимки.** Клиентът изпраща снимки и попълва кратък формуляр, а от тях се подготвя оферта.

## Документи, фактури и свързани програми {#dokumenti}

В много малки бизнеси едни и същи данни се пренаписват ръчно във фактури, договори, таблици и няколко програми. Автоматизацията на документи поема тази работа, като фактурите, отчетите и таблиците се създават и подреждат сами по зададени правила. Автоматичното фактуриране намалява ръчното въвеждане на едни и същи данни.

Свързваме и програмите, които вече използвате, така че данните да се попълват сами. Това свързване се нарича интеграция.

Документите се автоматизират във всеки вид бизнес. Шаблоните за договори са подходящи най-вече за B2B фирми и агенции за недвижими имоти. Свързаните програми са полезни за онлайн магазини, магазини и шоуруми и B2B фирми, а публикуването на обяви е предназначено за агенциите за недвижими имоти.

- **Фактури, отчети и таблици.** Създават се и се подреждат автоматично, без ръчно копиране между файлове.
- **Шаблони за договори с автоматично попълване.** Данните на клиента и на сделката се попълват в шаблона, което предпазва от грешки при ръчно копиране.
- **Свързани програми.** Данните, въведени в една програма, се появяват автоматично и в останалите.
- **Обява, публикувана веднъж.** Обявата се въвежда на едно място, а системата я публикува на няколко портала, обновява я и я сваля от тях. [VERIFY: canon says only "publishing a listing once to several portals"; „обновява я и я сваля“ goes beyond the canon wording, carried from the draft; owner to confirm or Step 5 to trim]

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

Работата започва с безплатна диагностика, а след доклада Вие избирате кои решения да изградим.

- **Безплатна диагностика и 30-минутен разговор.** Разговаряме за това къде Вашият бизнес губи време и кои задачи се повтарят.
- **Доклад до 48 часа.** Получавате доклад с приоритизирани решения и ясни еднократни цени.
- **Изграждане.** Изграждаме избраните решения, обикновено до 2 седмици.
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
   **a:** След като изберете решенията от доклада, изграждането обикновено отнема до 2 седмици.

5. **q:** Трябва ли да сменя програмите, които използвам?
   **a:** Целта е да свържем програмите, които вече използвате, така че данните да се попълват сами. [OWNER CONFIRM: canon says only "connecting the systems a business already uses"; confirm whether replacing a program is ever part of a fix]

6. **q:** Какво се случва, след като автоматизацията заработи?
   **a:** След внедряването предлагаме поддръжка с кратък месечен отчет за работата на решенията.

7. **q:** Как се отнасяте към данните на моите клиенти?
   **a:** Работим по GDPR. [DATA NEEDED: anything more specific (where data is stored, who has access) is Tier 3 and needs the owner; if nothing is added, Step 4/5 may drop this FAQ]

8. **q:** Обвързва ли ме диагностиката с договор?
   **a:** Не. Диагностиката не Ви обвързва с нищо, а ако решите да продължите, работим без дългосрочни договори.

---

## RELATED (3 sibling paths, all in conversion-links.md)

- /ai-asistent/
- /diagnostika/
- /seo-statii/

## SECONDARY KEYWORDS USED

софтуер за автоматизация; онлайн записване; онлайн резервации; автоматични оферти; автоматизация на документи; автоматично фактуриране; табло с показатели. Not used: sms напомняне (blocked by `[DATA NEEDED]`), софтуерна автоматизация (would be stuffing).

## CHANGE SUMMARY (5 lines)

1. Wrote title (≤ 60 incl. suffix, no em-dash) and meta description (120–160, main term first) for this page only.
2. Added card fields: label „Автоматизации“, one-sentence summary, eyebrow omitted, related = /ai-asistent/, /diagnostika/, /seo-statii/.
3. Main term confirmed once each in title, H1, lead (first 100 words) and H2 #kakvo-e; zero sibling main terms targeted.
4. Body, FAQ (8) and links (2 body + CTA + email) unchanged: coverage already complete within canon; no stuffing of „sms напомняне“ / „софтуерна автоматизация“.
5. All flags carried through unchanged; no new facts, numbers, prices or links.

## INVENTORY DIFF (00-inventory.md vs this page)

Body copy, lead, FAQ, links and tokens are byte-identical to 03-humanised.md (no body edit at this step), so every item keeps its Step 3 position:
1. Booking CTA → `{{BOOKING_URL}}`: #tsena, standalone, once. OK
2. `{{EMAIL}}`: #tsena, final standalone paragraph. OK
3. /diagnostika/: #za-kogo. OK
4. /ai-asistent/: #kakvo-e. OK
5–12. Canon capabilities (booking + calendar + reminders + waitlist; offers form → PDF and from photos; documents and invoices; contract templates; connected programs; listing once; real-time dashboard; AI meeting summary): present, unchanged. OK
13. Process, 4 canon steps: #kak-rabotim. OK
14. Policies: #tsena. OK
15. Price formation, no number: #tsena + FAQ 3. OK
16. Audience, 9 canon types: #za-kogo. OK
17. 30 минути / 48 часа / „обикновено до 2 седмици“: present, „обикновено“ kept. OK
18. Example label: not triggered (no example scenario). OK
19. FAQ: 8 entries. OK

New strings (title, meta, summary, label) checked: no number, price, guarantee, hype, banned word, „ти“ form or em-dash. Result: 19/19.

## FLAGS

- [OWNER CONFIRM] `kakvo-e`: rules agreed with the client / the client decides what stays with their people.
- [OWNER CONFIRM] `za-kogo`: hotels and guest houses mapping (no booking/reminder automation mapped to hotels in the checker).
- [OWNER CONFIRM] FAQ 5: whether replacing a program is ever part of a fix.
- [DATA NEEDED] `klienti-i-zapisvania`: reminder channel (SMS / имейл / съобщение); blocks „sms напомняне“.
- [DATA NEEDED] FAQ 7: data handling beyond „Работим по GDPR“.
- [VERIFY] `dokumenti` listing bullet: „обновява я и я сваля“ beyond canon wording (new at Step 3).
- [OWNER ITEM, optional] FAQ „Трябва ли да знам програмиране?“ not included.
- Carried from Step 2 for Step 5 attention (no marker): `kak-rabotim` intro and FAQ 4 client-choice wording; `klienti-i-zapisvania` „пропуснатите обаждания често означават пропуснати клиенти“.
- [PORT NOTE] `{{BOOKING_URL}}` / `{{EMAIL}}` paragraphs in `tsena` are standalone so the port JSON can omit them.
- [OWNER ITEM, optional] FAQ candidates „Замества ли автоматизацията служителите?“ and „Какъв софтуер използвате?“ not added (need owner input).

## CANON ADDITIONS

none
