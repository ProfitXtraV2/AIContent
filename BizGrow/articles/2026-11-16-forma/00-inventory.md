# 00-inventory — consultation form (every item must survive, same meaning, same order)

## Structure (ids from sync-consultation-form.mjs)
- title (form title „Безплатна консултация“ / "Free consultation")
- Intro paragraph under the title in the .md (not rendered; editorial note for the owner). Keep its meaning.
- s1 (no heading) fields: s1.f1 Име и фамилия (text, required) · s1.f2 Имейл (email, required; was „Служебен имейл“, CHANGE-BY-BRIEF) · s1.f3 Телефон (tel) · s1.f4 Уебсайт на компанията (url) · s1.f5 Ниша / сектор на дейност (text, placeholder „онлайн търговия, недвижими имоти, счетоводство“ = s1.f5.placeholder) · s1.f6 Удобен ден и час за 30-минутен разговор (text) · s1.f7 Предпочитам (radio: s1.f7.o1 видеоразговор, s1.f7.o2 телефон)
- s2 team size, radio, help; o1 Само аз (соло предприемач) · o2 2–5 души · o3 6–20 души · o4 Над 20 души
- s3 most manual work, check max 2, help „Изберете до 2 основни приоритета.“; o1 customer service/enquiries (имейли, чат, телефон) · o2 sales, leads, follow-up (JARGON: „лийдове“, „follow-up“) · o3 marketing and content (социални мрежи, бюлетини, реклами) · o4 admin, invoicing, data entry · o5 orders, stock, logistics · o6 Друго + o6.detail text · s3.extra optional one sentence on the most repeated task
- s4 tools, check (title starts „Кои“), help; o1 Google Workspace (Gmail, Sheets, Drive) / Microsoft 365 · o2 CRM (HubSpot, Pipedrive, Salesforce, Zoho) (JARGON: CRM unexplained) · o3 online shop platform (Shopify, WooCommerce, CloudCart) · o4 communication/task tools (Slack, Viber, Trello, Notion, Asana) · o5 accounting / ERP (JARGON: ERP) · o6 still mostly spreadsheets (Excel) and manual records
- s5 hours/week lost, radio, help („възвръщаемост на инвестицията“); o1 Под 5 · o2 5–15 · o3 15–30 · o4 Над 30 часа седмично (цял работен щат)
- s6 main goal, radio, help „следващите 3 месеца“; o1 save time · o2 serve more customers without hiring · o3 fewer human errors in data/orders · o4 more sales via faster response to enquiries · o5 still exploring
- s7 budget, radio, help (JARGON: „no-code“); OWNER CONTENT, amounts locked: o1 под 1 000 лв. / €500 · o2 1 000–3 000 лв. / €500–€1 500 · o3 над 3 000 лв. / €1 500+ · o4 no budget yet, see benefits first
- s8 capacity for 30% more customers, radio, help; o1 not ready, barely coping · o2 a bit more, quality would drop · o3 ready if routine work is automated · o4 already have capacity for ~30% more
- consent (NEW-BY-BRIEF, required checkbox, last step)
- note (Под бутона): sending does not commit; on the call we say what can be fixed and what it would cost
- submit: Изпратете / Submit
- „## Попълнен пример“: invented example (label „Примерът е измислен…“ must stay), answers 1–8 mirroring option wording

## Numbers present (all keep)
30-минутен разговор (canon) · 2–5 / 6–20 / 20 души · до 2 приоритета · 5 / 5–15 / 15–30 / 30 часа · 3 месеца · budget amounts (owner, locked) · 30% (owner question) · „около три минути“ (contact.writtenBody, existing copy) · example data in Попълнен пример (labelled invented).

## contact keys (bg + en), all must be returned
title, writtenTitle, writtenBody, writtenButton, bookTitle, book, emailTitle, copyEmail, emailCopied, close, stepProgress ({current}/{total} placeholders literal), back, next, contactLead.
Register issues seen: bg writtenBody „не ви обвързва“ (lowercase), contactLead „с вас“ (lowercase). EN: "Submit written request" (missing article), "Email was copied".
NEW-BY-BRIEF contact keys (bg + en): sending, sentTitle, sentBody, sendError, mailSubject (19 keys per locale in total).
