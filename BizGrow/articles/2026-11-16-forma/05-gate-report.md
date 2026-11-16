# 05-gate-report: consultation form copy (light path, Step 5 Brand Gate)

Page: consultation form (wizard) | Locale: bg + en | Type: page-rewrite (light path, UI copy) | Main term: n/a (Step 4 skipped)
Input: 03-humanised.md (parts A, B, C, flags in F) checked against 00-brief.md (owner instructions 2026-11-16 + parser constraints, binding), 00-current.md, 00-inventory.md, markets/bg/author.md and markets/en/author.md canon, reference/site-rules.md.

## SCORECARD

```
BRAND COMPLIANCE SCORECARD: consultation form (bg + en)
Verdict: PASS (one minor voice fix applied in EN; see D)
Total: 95/100 (81/85 on the five scored pillars, rescaled; Pillar 6 SEO N/A on the light path)
Voice 19/20 | Language 14/15 | Trust & claims 19/20 | Usefulness 14/15 | Anti-AI 15/15 | SEO N/A

BLOCKING CHECKS:
1. NOTHING LOST: PASS. Every 00-inventory.md item present, same order, same field kinds: title,
   intro paragraph, s1 f1–f7 (f2 „Имейл“ / "Email" CHANGE-BY-BRIEF, bracket `[имейл поле]`),
   s2–s8 with all options in order, s3 „до 2“ + Друго + extra line, s4 starts „Кои “, consent
   (NEW-BY-BRIEF), note, submit, „## Попълнен пример“ last with its label „Примерът е измислен…“.
   contact.json: 14 existing + 5 NEW-BY-BRIEF keys = 19 per locale; no `mailFallback`;
   `{current}` / `{total}` literal. All numbers in the inventory kept, none added.
2. FACTS ALLOWED LIST: PASS. BizGrow facts limited to: it contacts the visitor about the request,
   the 30-minute call, sending commits to nothing, the call says what can be fixed and what it
   would cost (current copy), custom development (canon service). Tool/vendor names in s4
   (HubSpot, Shopify, Slack …) describe the visitor's tools, not BizGrow's stack: not a claim.
3. BANNED CLAIMS: PASS with owner items. No guarantee, hype, urgency or testimonial. Prices: the
   s7 amounts („под 1 000 лв. / €500“, „1 000–3 000 лв. / €500–€1 500“, „над 3 000 лв. / €1 500+“
   and EN pairs) match the §3 price pattern but are owner content locked by brief instruction 4;
   verified byte-identical to 00-current.md in BG and EN; NOT deleted, recorded under OWNER ITEMS.
   „безплатн*“: „Безплатна консултация“ (title) and „безплатна консултация“ in mailSubject name
   the free first call, i.e. the canon free diagnosis + 30-minute call; existing owner title,
   kept by brief. Acceptable; terminology alignment with „безплатна диагностика“ raised as an
   owner item (not a blocker). mailSubject goes to BizGrow's own inbox, not to page visitors.
4. NUMBERS: PASS. 30-минутен / 30-минутния / 30-minute = canon (diagnosis call only duration).
   No delivery period or response time anywhere (sentBody: „Ще се свържем с Вас, за да уговорим
   30-минутния разговор.“ has no „до … часа“, „скоро“, „в рамките на“). Other figures are owner
   question/option content in the respondent's frame (2–5 / 6–20 / 20 души, до 2, 5 / 5–15 /
   15–30 / 30 часа, 3 месеца, 30%, s7 amounts) or existing copy („около три минути“ = form
   completion time in writtenBody, not a delivery period) or labelled invented example data.
   „оферта“/„доклад“: neither word appears; no breach.
5. HYPOTHETICAL LABEL: PASS. „Примерът е измислен, за да се види формата в действие.“ kept in
   the example section.
6. GDPR WORDING: PASS. Consent line BG „Давате съгласие BizGrow да използва данните от формата,
   за да се свърже с Вас по това запитване.“ / EN "You agree that BizGrow may use the data from
   this form to contact you about this request." states purpose only: no GDPR/compliance claim,
   no retention period, storage location, rights wording or third-party promise. Complete
   sentence ending in a full stop; reads correctly alone and followed by „Политика за
   поверителност“ / „Поверителност“ / "Privacy policy" / "Privacy".
7. REGISTER (BG): PASS. Zero „ти“ forms; zero lowercase ви/вас/ваш/вие (mechanical scan).
   Capitalised forms in all direct address (Вашия, Ви, Вашите, Вас). Options in the respondent's
   first person by design (owner instruction 1), not a breach.
8. CTA RULES: PASS. Submit „Изпратете“ / "Submit" from the approved set; no links, tokens or
   hard-coded contact data in the form (maria@example.com / example.com are labelled invented
   example answers). Existing keys „Запазете видеоразговор сега“ / "Book a video call now"
   unchanged from current copy; „сега“ is not scarcity wording, noted for the owner only.
9. ONE TERM PER PAGE: N/A (UI copy, no main term; Step 4 skipped by brief).
10. LINKS & ANCHORS: PASS / N/A. No links or anchors in the copy; ids/keys unchanged; EN keys
   equal the BG template's ids (s1.f1–s8.o4, consent, note, submit).
11. BIZGROW VOICE: PASS after one minor fix. No rhetorical questions in copy (section titles are
   form questions by function), no exclamation marks, no slang, no hype, no verdict lines; jargon
   removed or explained (лийдове, follow-up, no-code, интеграция, възвръщаемост на инвестицията
   gone; CRM and ERP explained on first use). One EN help line was a clause fragment:
   "So we can see which of your tools can be connected directly." → fixed (see D).

CRITICAL (blocks): none.

MODERATE: none.

MINOR:
- EN s4.help fragment (subordinate clause standing alone) → full sentence matching the other help
  lines' "This helps us …" pattern. Applied.
- s8.o1 „Не съм готов. И сега едва смогваме“ / "Not ready. We are only just keeping up": two
  fragments and an аз/ние mix, but it is an owner option in the respondent's voice and options
  keep their wording by brief instruction 5. Not changed; carried as owner item.
- BG s2/s5/s7 help lines open with a subjectless „Помага ни …“ (current-page pattern, short UI
  help text); acceptable on a form, not changed.

PARSER CONSTRAINTS (re-verified on the final A): title `# …`; 8 sections `## N.`; `## 1.`
untitled; brackets `[имейл поле]`, `[телефонно поле]`, `[URL поле]`; „Име и фамилия“ present;
inline radio `- Предпочитам: [ ] видеоразговор [ ] телефон`; „Друго: [текстово поле]“; „до
<digit>“ only in s3 help („Изберете до 2 основни приоритета.“); s4 title starts „Кои “; s3
after-line ends `: [текстово поле]`; `Съгласие:` directly before `Под бутона:`, then `Бутон:`;
„## Попълнен пример“ last. Em-dashes 0 (en-dash only in numeric ranges; „…“ in „Изпращане…“ is
an ellipsis).

OWNER ITEMS TO RAISE (for Step 6): see E.

VOICE NOTES (protect during later edits):
- Keep options in first person; keep capitalised Вие in questions, help lines, consent, note,
  contact keys.
- Keep sentBody free of any response time; keep sendError as one sentence.
- Keep s7 options and amounts byte-identical (owner content).
```

## A. forma-bezplatna-konsultacia.md

````markdown
# Безплатна консултация

Оставени са въпросите, които подготвят разговора: кой е бизнесът, къде отива ръчното време, с какви инструменти работи, колко време се губи, каква е целта, какъв бюджет е реалистичен и дали има капацитет за повече клиенти. Повтарящите се въпроси за канал на клиентите, общ списък „какво вече имате“ и отделно свободно поле за една задача са махнати, защото се покриват от сектора, инструментите и приоритетите по-долу.

## 1.

- Име и фамилия: [текстово поле]
- Имейл: [имейл поле]
- Телефон: [телефонно поле]
- Уебсайт на компанията: [URL поле]
- Ниша / сектор на дейност: [текстово поле, напр. онлайн търговия, недвижими имоти, счетоводство]
- Удобен ден и час за 30-минутен разговор: [текстово поле]
- Предпочитам: [ ] видеоразговор [ ] телефон

## 2. Какъв е размерът на Вашия екип в момента?

Помага ни да преценим мащаба на процесите и какво е нужно за тях.

- [ ] Само аз (соло предприемач)
- [ ] 2–5 души
- [ ] 6–20 души
- [ ] Над 20 души

## 3. Коя сфера от бизнеса Ви отнема най-много ръчен труд и време в момента?

Изберете до 2 основни приоритета.

- [ ] Обслужване на клиенти и отговаряне на запитвания (имейли, чат, телефон)
- [ ] Продажби, привличане на потенциални клиенти и последваща връзка с тях
- [ ] Маркетинг и създаване на съдържание (социални мрежи, бюлетини, реклами)
- [ ] Административни задачи, фактуриране и въвеждане на данни
- [ ] Управление на поръчки, складови наличности и логистика
- [ ] Друго: [текстово поле]

По желание, едно изречение коя задача се повтаря най-често: [текстово поле]

## 4. Кои софтуерни инструменти използвате ежедневно в работата си?

Така ще видим кои от Вашите програми могат да се свържат директно.

- [ ] Google Workspace (Gmail, Sheets, Drive) / Microsoft 365
- [ ] CRM система (програма за клиенти и продажби, напр. HubSpot, Pipedrive, Salesforce, Zoho)
- [ ] Платформа за онлайн магазин (напр. Shopify, WooCommerce, CloudCart)
- [ ] Инструменти за комуникация и задачи (напр. Slack, Viber, Trello, Notion, Asana)
- [ ] Счетоводен софтуер или ERP (система за управление на цялата фирма)
- [ ] Все още работим предимно с таблици (Excel) и ръчни записи

## 5. Колко часа седмично приблизително губите в повтарящи се, рутинни задачи?

Помага ни да преценим доколко автоматизацията би се изплатила за Вас.

- [ ] Под 5 часа седмично
- [ ] 5–15 часа седмично
- [ ] 15–30 часа седмично
- [ ] Над 30 часа седмично (цял работен щат)

## 6. Каква е основната Ви цел с внедряването на AI и автоматизации?

Изберете най-важното за Вас в следващите 3 месеца.

- [ ] Да спестя време на себе си и екипа си
- [ ] Да обслужвам повече клиенти, без да наемам нови хора
- [ ] Да намаля човешките грешки при обработка на данни и поръчки
- [ ] Да увелича продажбите чрез по-бърза реакция към запитванията
- [ ] Все още проучвам какви са възможностите за моя бизнес

## 7. Имате ли предвиден ориентировъчен бюджет за внедряване на решението?

Помага ни да предложим реалистични инструменти: от готови решения, които се настройват без програмиране, до разработка по поръчка.

- [ ] Търся максимално бюджетно решение (под 1 000 лв. / €500)
- [ ] Стандартен пакет за малък бизнес (1 000–3 000 лв. / €500–€1 500)
- [ ] По-мащабна автоматизация на няколко процеса (над 3 000 лв. / €1 500+)
- [ ] Все още не съм определил бюджет, искам първо да видя ползите

## 8. Доколко сте готови да поемете 30% повече клиенти в момента?

Показва дали растежът опира до капацитет, или бизнесът вече може да поеме повече работа.

- [ ] Не съм готов. И сега едва смогваме
- [ ] Мога да поема малко повече, но качеството ще падне
- [ ] Готов съм, ако рутинната работа се поеме автоматично
- [ ] Вече имам капацитет за около 30% повече клиенти

Съгласие: Давате съгласие BizGrow да използва данните от формата, за да се свърже с Вас по това запитване.

Под бутона: „Изпращането не Ви обвързва. На разговора ще кажем какво може да се оправи и какво би струвало.“

Бутон: **Изпратете**

## Попълнен пример

Примерът е измислен, за да се види формата в действие.

1. Мария Иванова. maria@example.com. 0888 000 000. https://example.com. Дентална клиника. Вторник след 14:00, видеоразговор.
2. 2–5 души.
3. Обслужване на клиенти и отговаряне на запитвания. Административни задачи, фактуриране и въвеждане на данни. „Сестрата потвърждава и мести часове по телефона по няколко часа на ден.“
4. Google Workspace. Счетоводен софтуер. Все още част от записите са в Excel.
5. 15–30 часа седмично.
6. Да обслужвам повече клиенти, без да наемам нови хора.
7. Все още не съм определил бюджет, искам първо да видя ползите.
8. Готов съм, ако рутинната работа се поеме автоматично.
````

## B. consultation-form.en.ts

````ts
/** English labels for the consultation form. Keys match ids from `npm run sync:form`. */
export const consultationFormEn: Record<string, string> = {
  title: "Free consultation",
  consent: "You agree that BizGrow may use the data from this form to contact you about this request.",
  note: "Sending this does not commit you to anything. On the call we will say what can be fixed and what it would cost.",
  submit: "Submit",
  "s1.f1": "First and last name",
  "s1.f2": "Email",
  "s1.f3": "Phone",
  "s1.f4": "Company website",
  "s1.f5": "Niche / line of business",
  "s1.f5.placeholder": "online retail, real estate, accounting",
  "s1.f6": "A convenient day and time for a 30-minute call",
  "s1.f7": "I prefer",
  "s1.f7.o1": "video call",
  "s1.f7.o2": "phone",
  s2: "What is the size of your team right now?",
  "s2.help": "This helps us judge the scale of the processes and the setup they need.",
  "s2.o1": "Just me (solo owner)",
  "s2.o2": "2–5 people",
  "s2.o3": "6–20 people",
  "s2.o4": "More than 20 people",
  s3: "Which part of the business takes the most manual work and time right now?",
  "s3.help": "Choose up to 2 main priorities.",
  "s3.o1": "Customer service and answering enquiries (email, chat, phone)",
  "s3.o2": "Sales, finding potential customers and following up with them",
  "s3.o3": "Marketing and creating content (social networks, newsletters, ads)",
  "s3.o4": "Admin, invoicing and data entry",
  "s3.o5": "Orders, stock and logistics",
  "s3.o6": "Other",
  "s3.o6.detail": "Other",
  "s3.extra": "Optional: one sentence on the task that repeats most often",
  s4: "Which software tools do you use every day?",
  "s4.help": "This helps us see which of your tools can be connected directly.",
  "s4.o1": "Google Workspace (Gmail, Sheets, Drive) / Microsoft 365",
  "s4.o2": "A CRM (software for customers and sales, for example HubSpot, Pipedrive, Salesforce, Zoho)",
  "s4.o3": "An online shop platform (for example Shopify, WooCommerce, CloudCart)",
  "s4.o4": "Communication and task tools (for example Slack, Viber, Trello, Notion, Asana)",
  "s4.o5": "Accounting software or ERP (a system for running the whole company)",
  "s4.o6": "We still work mostly with spreadsheets (Excel) and handwritten notes",
  s5: "About how many hours a week do you lose to repeated, routine tasks?",
  "s5.help": "This helps us estimate whether automation would pay off for you.",
  "s5.o1": "Under 5 hours a week",
  "s5.o2": "5–15 hours a week",
  "s5.o3": "15–30 hours a week",
  "s5.o4": "Over 30 hours a week (a full-time job)",
  s6: "What is your main goal for AI and automation?",
  "s6.help": "Choose what matters most over the next 3 months.",
  "s6.o1": "Save time for myself and my team",
  "s6.o2": "Serve more customers without hiring",
  "s6.o3": "Reduce human errors in data and orders",
  "s6.o4": "Increase sales by answering enquiries faster",
  "s6.o5": "I am still finding out what is possible for my business",
  s7: "Do you have a rough budget for putting the solution in place?",
  "s7.help": "This helps us suggest realistic tools, from ready-made setups that need no programming to a custom build.",
  "s7.o1": "I want the lowest budget (under 1,000 BGN / €500)",
  "s7.o2": "A standard package for a small business (1,000–3,000 BGN / €500–€1,500)",
  "s7.o3": "A larger automation of several processes (over 3,000 BGN / €1,500+)",
  "s7.o4": "I have not set a budget yet. I want to see the benefit first",
  s8: "How ready are you to take on 30% more customers right now?",
  "s8.help": "This shows whether growth is limited by capacity, or the business can already take on more work.",
  "s8.o1": "Not ready. We are only just keeping up",
  "s8.o2": "I could take a few more, but the quality would drop",
  "s8.o3": "Ready, if the routine work is handled automatically",
  "s8.o4": "I already have room for about 30% more customers",
};
````

## C. contact.json

````json
{
  "bg": {
    "title": "Свържете се с нас",
    "writtenTitle": "Изпратете писмено запитване",
    "writtenBody": "Опишете бизнеса и къде отива времето. Формата отнема около три минути и не Ви обвързва с нищо.",
    "writtenButton": "Изпратете писмено запитване",
    "bookTitle": "Запазете видеоразговор",
    "book": "Запазете видеоразговор сега",
    "emailTitle": "Изпратете ни имейл",
    "copyEmail": "Копирайте имейла",
    "emailCopied": "Имейлът е копиран",
    "close": "Затворете",
    "stepProgress": "Въпрос {current} от {total}",
    "back": "Назад",
    "next": "Напред",
    "contactLead": "Как да се свържем с Вас?",
    "sending": "Изпращане…",
    "sentTitle": "Благодарим Ви за запитването",
    "sentBody": "Запитването Ви е изпратено. Ще се свържем с Вас, за да уговорим 30-минутния разговор.",
    "sendError": "Изпращането не успя, затова Ви молим да ни пишете на имейл адреса по-долу, който можете да копирате.",
    "mailSubject": "Запитване за безплатна консултация от"
  },
  "en": {
    "title": "Contact us",
    "writtenTitle": "Submit a written request",
    "writtenBody": "Tell us about the business and where the time goes. The form takes about three minutes and does not commit you to anything.",
    "writtenButton": "Submit a written request",
    "bookTitle": "Book a video call",
    "book": "Book a video call now",
    "emailTitle": "Send us an email",
    "copyEmail": "Copy email",
    "emailCopied": "Email copied",
    "close": "Close",
    "stepProgress": "Question {current} of {total}",
    "back": "Back",
    "next": "Next",
    "contactLead": "How should we contact you?",
    "sending": "Sending…",
    "sentTitle": "Thank you for your request",
    "sentBody": "Your request has been sent. We will contact you to arrange the 30-minute call.",
    "sendError": "Sending failed, so please write to us at the email address shown below, which you can copy.",
    "mailSubject": "Free consultation request from"
  }
}
````


## D. FIXES APPLIED (before → after)

1. B (EN labels), `s4.help`, check 11 / Pillar 1 (clause fragment as a help line):
   - before: `"s4.help": "So we can see which of your tools can be connected directly.",`
   - after: `"s4.help": "This helps us see which of your tools can be connected directly.",`
   Meaning unchanged; key unchanged; matches the BG „Така ще видим кои от Вашите програми могат да се свържат директно.“ and the other EN help lines.

No other change. Part A (BG template) and part C (contact.json) are byte-identical to 03-humanised.md. Section 7 question, options and amounts are byte-identical to 00-current.md in BG and EN (help line de-jargoned by Step 2 as the brief allows).

## E. OWNER ITEMS

Carried over from 03-humanised.md part F (unchanged):

1. [OWNER CONFIRM] Budget amounts in s7 (BG and EN: под 1 000 лв. / €500 · 1 000–3 000 лв. / €500–€1 500 · над 3 000 лв. / €1 500+) are prices in page copy, which site-rules §3 and the canon forbid. Kept by brief instruction 4 as the owner's own form options, not deleted by the gate; owner to confirm they stay.
2. [OWNER CONFIRM] Consent wording is a plain-language draft, not legal advice. Owner (or whoever handles GDPR) to confirm it covers what the business needs. Optional: append the canon sentence „Работим по GDPR.“ / "We work under GDPR." after it; not added, to keep one consent sentence as the brief asks.
3. [LINK NEEDED] The consent sentence is written to be followed by the privacy link; the privacy page does not exist yet and the footer key currently reads „Поверителност“ / "Privacy" (brief says it will become „Политика за поверителност“ / "Privacy policy"). Both read correctly after the sentence. Until the page exists, a required consent checkbox points to no privacy policy; owner to decide whether the form goes live before the privacy page.
4. Note (not a blocker): the note keeps „какво може да се оправи“ (owner wording, plain spoken Bulgarian); a more formal alternative is „какво може да се подобри“, but that shifts the meaning slightly, so unchanged.
5. Note: s3.extra BG label „По желание, едно изречение коя задача се повтаря най-често“ is a label phrase, kept unchanged because the parser requires the `По желание, …: [текстово поле]` shape and the meaning is clear.
6. CANON ADDITIONS: none.
7. Note (not a blocker): s8.o1 „Не съм готов. И сега едва смогваме“ mixes „аз“ and „ние“ in one option; owner option wording, left unchanged. Owner may unify it (e.g. „Не съм готов, и сега едва смогваме“) if desired.

New from the gate:

8. Note (terminology, not a blocker): the form title „Безплатна консултация“ / "Free consultation" and mailSubject „Запитване за безплатна консултация от“ / "Free consultation request from" use „консултация“ for the free first call, while the canon and the approved CTAs call it „безплатна диагностика“ / "free diagnosis". Acceptable because it names the same canon free call (diagnosis + 30-minute call) and is the owner's existing title; owner may align to „Безплатна диагностика“ site-wide if preferred. mailSubject is only seen in BizGrow's own inbox.
9. Note (not a blocker): existing keys „Запазете видеоразговор сега“ / "Book a video call now" (unchanged current copy) add „сега“ / "now" to the approved CTA „Запазете видеоразговор“. Not scarcity wording; owner may drop „сега“ for full alignment with site-rules §4.
10. Note (not a blocker): writtenBody „Формата отнема около три минути“ / "about three minutes" is existing copy and describes the visitor's time to fill in the form, not a delivery period; kept. Owner to confirm the estimate still holds now that a consent step was added.
11. Note (not a blocker): sentBody promises contact („Ще се свържем с Вас, за да уговорим 30-минутния разговор.“) with no time frame, as the canon requires; the owner should make sure every request is actually answered, since the form now only sends automatically (no `mailFallback`).
