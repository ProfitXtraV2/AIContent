# 05-gate-report — /saveti/google-biznes-profil/ (Step 5, Brand Gate)

Inputs read: 00-current.md, 00-inventory.md, 00-brief.md, 04-seo.md, keyword-map.md (row + all sibling primaries), conversion-links.md, site-rules.md, verification-policy.md, markets/bg/author.md (canon + voice), brand-gate-bizgrow.md, step-5-brand-gate.md.

```
BRAND COMPLIANCE SCORECARD — /saveti/google-biznes-profil/ (bg)
Verdict: PASS (moderate language fixes applied, no criticals)
Total: 91/100 → 93/100 after fixes
Voice 18/20 | Language 13/15 → 14/15 | Trust & claims 18/20 → 19/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 14/15
```

## ARTICLE RULE CHECKS (python, _tmp/gate_check.py)

| rule | result |
|---|---|
| question-led H2s 6–8 | PASS: 8, all questions |
| body 900–1,400 words excl. lead + FAQ + flag markers | PASS: 920 (gate count; Step 4 reported 934 with a different tokenisation; both in range) |
| FAQ 4–6 | PASS: 6, each 1–2 sentences, none repeats a heading verbatim |
| exactly one booking CTA on the page | PASS: 1 („Запазете безплатна диагностика“ → `{{BOOKING_URL}}`, #bizgrow) |
| eyebrow „Съвети“ | PASS |
| summary ≤160 | PASS: 148 |
| no `service` key | PASS |
| related = 3 sibling paths from conversion-links.md | PASS: /socialni-mrezhi/, /ai-asistent/, /seo-optimizacia/ |
| title ≤60 incl. „ | BizGrow“ | PASS: 54 |
| meta 120–160 | PASS: 140, contains the main term |
| max 3 sourced facts | PASS (see MODERATE 1): F1, F2, F3 per the brief's grouping |
| UI labels only verbatim from 00-brief passages | PASS: „Добавете бизнеса си в Google“, „Заявяване на този бизнес“ (both verbatim in S1); „Google Карти“, „Търсене“ are product names |
| no delivery periods | PASS: only „30-минутен разговор“; „до 5 работни дни“ is Google's sourced review time, not a BizGrow delivery period; „Срокът зависи от решението и го посочваме в офертата.“ verbatim |
| „оферта“, never „доклад“ | PASS: „доклад“ 0 |
| em-dashes / exclamation marks | PASS: 0 / 0 |

## BLOCKING CHECKS

1. NOTHING LOST (new page, inventory carriers): PASS. I1 single CTA in #bizgrow; I2 /diagnostika/ (#bizgrow); I3 /socialni-mrezhi/ („поддържа профила жив“, #bizgrow); I4 /ai-asistent/ (#ocenki); optional `{{EMAIL}}` present once; I5 monthly upkeep with posts, photos, information; I6 ratings/comments watched, reply prepared for approval; I7 free diagnosis + 30-minute call → оферта with prioritised fixes and clear one-off prices, timing line verbatim; I8 „Диагностиката не Ви обвързва с нищо. Работим без дългосрочни договори.“
2. FACTS ALLOWED LIST: PASS. Every BizGrow statement is canon (profile upkeep monthly; replies prepared for approval; AI assistant answering in Messenger/Instagram/WhatsApp outside working hours and taking the contact when it cannot help; process; no long-term contracts). No vendor, team, price, client or count.
3. BANNED CLAIMS: PASS. „безплатн*“ 2× (both the diagnosis); no „отзив*“ in visible copy; no guarantee words; ranking explicitly not promised („никой не може да обещае конкретно място в Картите“); no hype, price, offer or urgency.
4. NUMBERS: PASS. 30 (canon, call), 5 (Tier B, `[VERIFY]` S2, body + FAQ 2). No other figures.
5. HYPOTHETICAL LABEL: N/A (no example scenarios).
6. GDPR WORDING: N/A (GDPR not mentioned; the „лични данни“ line in #ocenki is reply etiquette, not a compliance claim).
7. REGISTER: PASS. Zero „ти“ forms (regex hits were word endings such as „Карти“). Courtesy forms capitalised. FAQ questions use the reader's first person („ми“, „мен“), which is correct.
8. CTA RULES: PASS. One booking CTA, approved wording, token only; email only as `{{EMAIL}}`; no urgency.
9. ONE TERM PER PAGE: PASS. „бизнес профил в гугъл“ once each in title, lead (first 100 words), one H2 (#syzdavane), plus meta; H1 is the keyword-map H1. No sibling primary (ai автоматизация, ai асистент as heading target, автоматизация на бизнес процеси, seo копирайтинг, маркетинг в социалните мрежи, реклама в гугъл, seo оптимизация, локално seo, копирайтър, ключови думи, безплатна диагностика за бизнеса) in title, H1 or any H2. „AI асистент“ appears only as body link text to its own page.
10. LINKS & ANCHORS: PASS. /ai-asistent/, /socialni-mrezhi/, /diagnostika/ (3 contextual, within 1–3), all in conversion-links.md; no external body links (business.google.com/add deliberately not shown, flagged).
11. BIZGROW VOICE: PASS. No fragment paragraphs, rhetorical questions, verdict lines, slang or hype; jargon („AI асистент“) explained on first use.

CRITICAL (blocks): none.

## MODERATE (fixed or noted)

1. Sourced-fact count (noted, not changed): F1 bundles two statements from S1 (found in Search and Maps after adding and verifying; adding/claiming without monetary payment) and F2 two from S2 (ownership; options depend on business type). Counted as 3 facts per the brief's suggested grouping. The claim steps and the ownership-request sentence in #zayavyavane are procedural paraphrase of S1; Step 6 should cite S1 for them. Added as a FLAGS note and an owner item.
2. Language, lead (fixed): „Google бизнес профил е информацията …“ → „Google бизнес профилът е информацията …“ (subject needs the full article).
3. Language + scope, #bizgrow (fixed): „Нищо не се публикува, преди да го одобрите.“ (clitic „го“ does not agree with „нищо“) → „Нищо не се публикува без Вашето одобрение.“ Meaning of inventory I6 kept. The sentence also covers profile posts and photos, while canon states approval explicitly for replies and for the content tool → owner item.
4. Language, #danni (fixed): „дали сте отворени“ next to „отварят профила“ (repetition) → „дали работите в момента“.
5. SEO voice, lead (noted, not changed): „В търсачката хората го търсят и като „бизнес профил в гугъл“ или „гугъл бизнес профил“.“ reads slightly like a keyword note but is accurate and carries the main term in the first 100 words; left for the owner's colloquial-spelling decision (existing flag).
6. Repetition (noted): the no-ranking-promise idea appears in #kakvo-e and FAQ 4; acceptable because FAQ answers must stand alone.

## VOICE NOTES (protect in Step 6)
- Keep the calm advisory tone, the step lists, the no-ranking-promise sentence and the closing order: upkeep → diagnosis → оферта → timing line → no commitment → CTA → email.
- Keep „оценки и коментари“ throughout until the owner decides item 7.

---

## FIXED ARTICLE (post-gate)

# Как да създадете и поддържате Google бизнес профил

- title: Бизнес профил в гугъл: създаване и поддръжка | BizGrow
- meta_description: Създаване на бизнес профил в гугъл стъпка по стъпка: добавяне, заявяване и потвърждаване, месечна проверка и отговори на оценки и коментари.
- eyebrow: Съвети
- label: Google бизнес профил
- summary: Как да създадете, заявите и потвърдите Google бизнес профил и какво да проверявате в него всеки месец, включително отговорите на оценки и коментари.

**Lead:** Google бизнес профилът е информацията за бизнеса Ви, която клиентите виждат в Google Търсене и Google Карти: име, адрес, работно време, телефон, снимки, оценки и коментари. В търсачката хората го търсят и като „бизнес профил в гугъл“ или „гугъл бизнес профил“. Създаването, заявяването и потвърждаването му следват ясни стъпки, а поддръжката изисква редовна проверка на данните и отговори на клиентите.

## Какво е Google бизнес профил и защо е полезен? {#kakvo-e}

Профилът събира на едно място данните, които клиентите проверяват, преди да се обадят или да дойдат: къде се намирате, кога работите и как да се свържат с Вас. Той се показва в Google Търсене и Google Карти, когато някой потърси бизнеса Ви.

Според Google, когато добавите и потвърдите бизнес профила си, клиентите могат да намират бизнеса Ви в Търсене и Карти. Добавянето или заявяването на бизнес става без парично заплащане. [VERIFY: added and verified profile → customers can find the business in Search and Maps; adding/claiming without monetary payment: https://support.google.com/business/answer/2911778?hl=bg]

Профилът е полезен за всеки бизнес, при който клиентите идват на място или търсят телефон и работно време: ресторант, хотел, салон, автосервиз, клиника или магазин. Подредбата в резултатите се определя от Google и никой не може да обещае конкретно място в Картите. Пълният и актуален профил помага на клиентите да решат дали да дойдат при Вас, когато вече са Ви открили.

## Как се създава бизнес профил в гугъл? {#syzdavane}

[OWNER CONFIRM: main term „бизнес профил в гугъл“ placed verbatim in this H2, in the lead (first 100 words), in the title and in the meta description; SEO stage (Step 4) kept the colloquial form in this H2. Alternative if the owner prefers standard spelling in headings: „Как се създава бизнес профил в Google?“, with the colloquial form kept in title, meta and lead.]

Преди да създадете нов профил, проверете дали бизнесът Ви вече се показва в Google Карти, като потърсите името му и града. Ако го има, заявете съществуващия профил, за да не се появят два профила на едно място. Прочетете и условията на Google за това кои бизнеси могат да имат профил.

Ако бизнесът Ви още няма профил, създайте го така:

1. Отворете страницата на Google за добавяне на бизнес и изберете „Добавете бизнеса си в Google“. [OWNER CONFIRM: show the address business.google.com/add as plain text? External links are not allowed in the body; it is quoted in S1.]
2. Въведете данните на бизнеса, като следвате инструкциите на екрана.
3. Изберете начин за потвърждаване и изпълнете стъпките, които Google Ви показва.

Използвайте точното име на бизнеса, същото като на табелата и на сайта Ви. Така клиентите разпознават от пръв поглед, че профилът е Вашият.

## Какво да направите, ако бизнесът Ви вече е в Google Карти? {#zayavyavane}

Ако при търсенето бизнесът Ви вече се показва в Google Карти, не е нужно да създавате нов профил. Можете да заявите съществуващия по следния начин:

1. Отворете Google Карти от компютър.
2. Потърсете името на бизнеса и града си.
3. Изберете „Заявяване на този бизнес“ и продължете към потвърждаването.

Ако профилът вече е потвърден от друг човек, а Вие сте упълномощени да го управлявате, можете да подадете заявка за собственост до настоящия му собственик. [OWNER CONFIRM: the synthesis sentence „Това често се случва, когато профилът е създаден от бивш служител или от външна фирма.“ is an unsourced generalisation and was dropped per the outline; restore only if the owner agrees.]

## Как се потвърждава профилът и колко време отнема? {#potvarzhdavane}

Потвърждаването на бизнес профила доказва пред Google, че Вие управлявате бизнеса. Когато потвърдите бизнеса си, придобивате собствеността върху бизнес профила, а наличните начини за потвърждаване зависят от типа на бизнеса Ви. [VERIFY: verification gives ownership of the profile; available options depend on the business type: https://support.google.com/business/answer/7107242?hl=bg]

Google показва възможните начини по време на процеса, затова изберете този, който можете да изпълните веднага. Според Google прегледите за потвърждаване отнемат до 5 работни дни, а в редки случаи и повече. [VERIFY: verification reviews take up to 5 working days; rarely longer: https://support.google.com/business/answer/7107242?hl=bg]

Докато чакате, подгответе снимките и текстовете, които ще добавите след потвърждаването. Проверете и дали името, адресът и телефонът съвпадат с тези на сайта Ви и в профилите Ви в социалните мрежи.

## Какво да попълните в профила? {#danni}

Клиентите обикновено отварят профила, за да разберат дали работите в момента, как да стигнат до Вас и как да се свържат с Вас. Затова започнете с основните данни:

- Точното име на бизнеса.
- Адрес или местоположение, така че клиентите да Ви намерят на картата.
- Телефонен номер, на който някой отговаря в работно време.
- Уебсайт, ако имате такъв.
- Работно време, включително промените през празниците или през сезона.
- Снимки и видеоклипове на обекта, продуктите и услугите.

Добавяйте реални снимки на мястото и на това, което продавате. Те дават на клиента представа какво го очаква, преди да дойде.

## Какво да проверявате в профила всеки месец? {#poddrazhka}

Профилът е полезен, докато информацията в него е вярна. Ако работното време или менюто са остарели, клиентите може да намерят затворена врата или да очакват друга цена.

Веднъж месечно проверявайте следното:

- Работното време, особено преди празници и при смяна на сезона.
- Менюто, цените и услугите, така че да съвпадат със сайта и социалните мрежи.
- Снимките, като добавяте нови, когато обновите обекта, продуктите или услугите.
- Оценките и коментарите, на които още не сте отговорили.

Ако менюто или цените Ви се сменят често, удобно е да ги обновявате от едно място. Така в Google, в сайта и във Facebook не остава стара информация, която да обърква клиентите.

## Как да отговаряте на оценки и коментари в Google? {#ocenki}

Оценките и коментарите в Google се виждат от всеки, който отвори профила. Новите клиенти четат и самите коментари, и начина, по който бизнесът отговаря на тях.

Няколко правила помагат отговорите да звучат професионално:

- Отговаряйте и на положителните, и на критичните коментари.
- Благодарете конкретно, като споменете услугата или продукта, за който пише клиентът.
- При оплакване отговорете спокойно, признайте проблема и предложете да го решите извън профила.
- Не публикувайте лични данни на клиента и подробности за поръчката му.

Част от въпросите, които клиентите задават в коментарите, идват и като съобщения. Ако тези въпроси се повтарят в Messenger, Instagram или WhatsApp, на тях може да отговаря [AI асистент](/ai-asistent/), включително извън работно време. AI асистентът е програма, която отговаря автоматично по информацията на бизнеса Ви. Когато не може да помогне, асистентът записва контакта на клиента, за да се свържете с него.

[OWNER CONFIRM: the house term „оценки и коментари в Google“ is used throughout instead of Google's own „отзиви“ (site-rules §3; /diagnostika/ item 21 still open).]

## Как BizGrow може да поддържа профила вместо Вас? {#bizgrow}

Ако нямате време да следите профила редовно, BizGrow може да [поддържа профила жив](/socialni-mrezhi/) с публикации, снимки и актуална информация всеки месец. Следим оценките и коментарите, които клиентите оставят в Google, и подготвяме отговор за Вашето одобрение. Нищо не се публикува без Вашето одобрение.

Първата стъпка е [безплатната диагностика](/diagnostika/) и 30-минутен разговор, в който разглеждаме къде бизнесът Ви губи време. След него получавате оферта с приоритизирани решения и ясни еднократни цени. Срокът зависи от решението и го посочваме в офертата. Диагностиката не Ви обвързва с нищо. Работим без дългосрочни договори.

[Запазете безплатна диагностика]({{BOOKING_URL}})

Ако предпочитате да пишете, изпратете ни съобщение на {{EMAIL}}.

## FAQ

q: Плаща ли се за Google бизнес профил?
a: Google посочва, че можете да добавите или заявите бизнеса си без парично заплащане. [VERIFY: adding/claiming without monetary payment: https://support.google.com/business/answer/2911778?hl=bg]

q: Колко дни отнема потвърждаването на профила?
a: Според Google прегледите за потвърждаване на бизнес профила отнемат до 5 работни дни. В редки случаи може да отнемат повече време. [VERIFY: up to 5 working days, rarely longer: https://support.google.com/business/answer/7107242?hl=bg]

q: Мога ли да заявя профил, който Google Карти вече показва?
a: Да. Потърсете името на бизнеса и града си в Google Карти от компютър, изберете „Заявяване на този бизнес“ и изпълнете стъпките за потвърждаване.

q: Ще се класира ли бизнесът ми по-напред в Google Карти?
a: Подредбата в Карти и Търсене се определя от Google и никой не може да обещае конкретна позиция. Пълният и актуален профил помага на клиентите да изберат Вас, когато Ви открият.

q: Колко често да обновявам профила?
a: Обновявайте го веднага, щом се промени работното време, менюто, цените или контактите. Веднъж месечно проверявайте също снимките, както и оценките и коментарите, на които още няма отговор.

q: Може ли BizGrow да отговаря на оценките и коментарите вместо мен?
a: BizGrow следи оценките и коментарите в Google и подготвя отговор за Вашето одобрение. Отговорът се публикува едва след като го одобрите.

- related: /socialni-mrezhi/, /ai-asistent/, /seo-optimizacia/

## FLAGS

- [VERIFY] F1 (S1/S3, found in Search and Maps after adding and verifying; adding/claiming without monetary payment) → #kakvo-e, FAQ 1
- [VERIFY] F2 (S2, verification gives ownership; options depend on business type) → #potvarzhdavane
- [VERIFY] F3 (S2, up to 5 working days, rarely longer) → #potvarzhdavane, FAQ 2
- [OWNER CONFIRM] main-term H2 placement („Как се създава бизнес профил в гугъл?“); Step 4 kept it, alternative noted inline → #syzdavane
- [OWNER CONFIRM] show business.google.com/add as plain text → #syzdavane step 1
- [OWNER CONFIRM] „бивш служител / външна фирма“ sentence dropped per outline → #zayavyavane
- [OWNER CONFIRM] house wording „оценки и коментари“ vs Google's „отзиви“ (/diagnostika/ item 21) → #ocenki (applies also to #poddrazhka, #bizgrow, FAQ 5-6)
- [OWNER CONFIRM] FAQ 1 „например реклама“ sentence dropped per outline (not inline; listed here only)
- NOTE (gate) FAQ 4 reworded to „по-напред“ (no „първо място“)
- NOTE posts kept out of #poddrazhka as a Google feature (synthesis exclusion 4); posts appear only as BizGrow canon in #bizgrow
- NOTE (Step 4) „гугъл май бизнес“ not placed: needs a source for the former-name fact
- NOTE (Step 4) no-address / service-area question left unanswered (no source)
- [OWNER CONFIRM] (gate) „Нищо не се публикува без Вашето одобрение.“ in #bizgrow covers profile posts and photos as well as replies; canon states approval for replies and for the content tool → #bizgrow (owner items list only, not inline)
- NOTE (gate) sourced-fact count: F1 and F2 each bundle two statements from one passage (brief's suggested grouping, counted as 3 facts); claim steps and the ownership-request sentence in #zayavyavane are procedural paraphrase of S1, not a 4th fact; Step 6 cites S1 for them
- Inline markers in body/FAQ: 5 [VERIFY] + 4 [OWNER CONFIRM] (unchanged by the gate)

## CANON ADDITIONS

none

---

## OWNER ITEMS (for Step 6 → [[owner_items]]; decision fields stay empty)

1. [VERIFY] F1: adding and verifying the profile lets customers find the business in Search and Maps; adding or claiming is without monetary payment (S1 https://support.google.com/business/answer/2911778?hl=bg) → #kakvo-e, FAQ 1.
2. [VERIFY] F2: verification gives ownership of the profile; available options depend on the business type (S2 https://support.google.com/business/answer/7107242?hl=bg) → #potvarzhdavane.
3. [VERIFY] F3: verification reviews take up to 5 working days, rarely longer (S2) → #potvarzhdavane, FAQ 2.
4. [OWNER CONFIRM] Colloquial main term „бизнес профил в гугъл“ in the #syzdavane H2 (alternative „Как се създава бизнес профил в Google?“).
5. [OWNER CONFIRM] Show business.google.com/add as plain text in #syzdavane step 1, or keep the generic wording.
6. [OWNER CONFIRM] Dropped sentence „Това често се случва, когато профилът е създаден от бивш служител или от външна фирма.“ (#zayavyavane); restore only on approval.
7. [OWNER CONFIRM] House wording „оценки и коментари“ instead of Google's „отзиви“ (site-rules §3; /diagnostika/ item 21 still open).
8. [OWNER CONFIRM] FAQ 1 sentence „например реклама“ dropped per outline.
9. [OWNER CONFIRM] related #3: /seo-optimizacia/ (current) or /diagnostika/.
10. [OWNER CONFIRM] (gate) „Нищо не се публикува без Вашето одобрение.“ also covers profile posts and photos, not only replies; confirm that approval applies to all profile updates or narrow the sentence to replies.
11. [VERIFY] (gate) Step 6 to confirm the fact-count grouping (F1 and F2 as one fact each) and cite S1 for the claim steps and the ownership-request sentence in #zayavyavane.

Owner items: 11 (3 VERIFY facts, 1 VERIFY count/citation check, 7 OWNER CONFIRM).
