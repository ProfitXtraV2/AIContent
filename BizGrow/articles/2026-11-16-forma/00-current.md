# 00-current — consultation form copy (verbatim)

Source: biz-grow repo, branch main, HEAD f49f083 (working tree has the consent plumbing in sync-consultation-form.mjs / consultation-form.ts / Contact.tsx, uncommitted). Read 2026-11-16.

## A. docs/forma-bezplatna-konsultacia.md

````markdown
# Безплатна консултация

Оставени са въпросите, които подготвят разговора: кой е бизнесът, къде отива ръчното време, с какви инструменти работи, колко време се губи, каква е целта, какъв бюджет е реалистичен и дали има капацитет за повече клиенти. Повтарящите се въпроси за канал на клиентите, общ списък „какво вече имате“ и отделно свободно поле за една задача са махнати, защото се покриват от сектора, инструментите и приоритетите по-долу.

## 1.

- Име и фамилия: [текстово поле]
- Служебен имейл: [имейл поле]
- Телефон: [телефонно поле]
- Уебсайт на компанията: [URL поле]
- Ниша / сектор на дейност: [текстово поле, напр. онлайн търговия, недвижими имоти, счетоводство]
- Удобен ден и час за 30-минутен разговор: [текстово поле]
- Предпочитам: [ ] видеоразговор [ ] телефон

## 2. Какъв е размерът на вашия екип в момента?

Помага ни да преценим мащаба на процесите и нужната инфраструктура.

- [ ] Само аз (соло предприемач)
- [ ] 2–5 души
- [ ] 6–20 души
- [ ] Над 20 души

## 3. Коя сфера от бизнеса ви отнема най-много ръчен труд и време в момента?

Изберете до 2 основни приоритета.

- [ ] Обслужване на клиенти и отговаряне на запитвания (имейли, чат, телефон)
- [ ] Продажби, генериране на лийдове и последваща комуникация (follow-up)
- [ ] Маркетинг и създаване на съдържание (социални мрежи, бюлетини, реклами)
- [ ] Административни задачи, фактуриране и въвеждане на данни
- [ ] Управление на поръчки, складови наличности и логистика
- [ ] Друго: [текстово поле]

По желание, едно изречение коя задача се повтаря най-често: [текстово поле]

## 4. Кои софтуерни инструменти използвате ежедневно в работата си?

За да проверим възможностите за директна интеграция.

- [ ] Google Workspace (Gmail, Sheets, Drive) / Microsoft 365
- [ ] CRM система (напр. HubSpot, Pipedrive, Salesforce, Zoho)
- [ ] Платформа за онлайн магазин (напр. Shopify, WooCommerce, CloudCart)
- [ ] Инструменти за комуникация и задачи (напр. Slack, Viber, Trello, Notion, Asana)
- [ ] Счетоводен / ERP софтуер
- [ ] Все още работим предимно с таблици (Excel) и ръчни записи

## 5. Колко часа седмично приблизително губите в повтарящи се, рутинни задачи?

Помага ни да изчислим потенциалната възвръщаемост на инвестицията.

- [ ] Под 5 часа седмично
- [ ] 5–15 часа седмично
- [ ] 15–30 часа седмично
- [ ] Над 30 часа седмично (цял работен щат)

## 6. Каква е основната ви цел с внедряването на AI и автоматизации?

Изберете най-важното за вас в следващите 3 месеца.

- [ ] Да спестя време на себе си и екипа си
- [ ] Да обслужвам повече клиенти, без да наемам нови хора
- [ ] Да намаля човешките грешки при обработка на данни и поръчки
- [ ] Да увелича продажбите чрез по-бърза реакция към запитванията
- [ ] Все още проучвам какви са възможностите за моя бизнес

## 7. Имате ли предвиден ориентировъчен бюджет за внедряване на решението?

Помага ни да предложим реалистични инструменти, от готови no-code решения до разработка по поръчка.

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

Под бутона: „Изпращането не ви обвързва. На разговора ще кажем какво може да се оправи и какво би струвало.“

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

## B. site/src/content/consultation-form.en.ts

````ts
/** English labels for the consultation form. Keys match ids from `npm run sync:form`. */
export const consultationFormEn: Record<string, string> = {
  title: "Free consultation",
  note: "Sending this does not commit you to anything. On the call we will say what can be fixed and what it would cost.",
  submit: "Submit",
  "s1.f1": "First and last name",
  "s1.f2": "Work email",
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
  "s3.o2": "Sales, lead generation and follow-up",
  "s3.o3": "Marketing and creating content (social networks, newsletters, ads)",
  "s3.o4": "Admin, invoicing and data entry",
  "s3.o5": "Orders, stock and logistics",
  "s3.o6": "Other",
  "s3.o6.detail": "Other",
  "s3.extra": "Optional: one sentence on the task that repeats most often",
  s4: "Which software tools do you use every day?",
  "s4.help": "So we can see what can be connected directly.",
  "s4.o1": "Google Workspace (Gmail, Sheets, Drive) / Microsoft 365",
  "s4.o2": "A CRM (for example HubSpot, Pipedrive, Salesforce, Zoho)",
  "s4.o3": "An online shop platform (for example Shopify, WooCommerce, CloudCart)",
  "s4.o4": "Communication and task tools (for example Slack, Viber, Trello, Notion, Asana)",
  "s4.o5": "Accounting / ERP software",
  "s4.o6": "We still work mostly with spreadsheets (Excel) and handwritten notes",
  s5: "About how many hours a week do you lose to repeated, routine tasks?",
  "s5.help": "This helps us estimate the return on the time you would get back.",
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
  "s7.help": "This helps us suggest realistic tools, from ready-made no-code setups to a custom build.",
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

## C. contact keys — site/src/i18n/dictionaries/bg.ts

````json
  "contact": {
    "title": "Свържете се с нас",
    "writtenTitle": "Изпратете писмено запитване",
    "writtenBody": "Опишете бизнеса и къде отива времето. Формата отнема около три минути и не ви обвързва с нищо.",
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
    "contactLead": "Как да се свържем с вас?"
  },
````

## D. contact keys — site/src/i18n/dictionaries/en.ts

````json
  "contact": {
    "title": "Contact us",
    "writtenTitle": "Submit written request",
    "writtenBody": "Tell us about the business and where the time goes. The form takes about three minutes and does not commit you to anything.",
    "writtenButton": "Submit written request",
    "bookTitle": "Book a video call",
    "book": "Book a video call now",
    "emailTitle": "Send us an email",
    "copyEmail": "Copy email",
    "emailCopied": "Email was copied",
    "close": "Close",
    "stepProgress": "Question {current} of {total}",
    "back": "Back",
    "next": "Next",
    "contactLead": "How should we contact you?"
  },
````

## E. How the site renders the consent line

Contact.tsx renders on the last wizard step a REQUIRED checkbox: `{form.consent}` then, only if site.privacyHref is set, a space and a link whose text is t.footer.privacy (currently bg „Поверителност“, en "Privacy"; the launching session says the link text will be „Политика за поверителност“ / "Privacy policy"). So the consent sentence must be a complete sentence ending in a full stop that reads well alone AND followed by that link text.

contact.contactLead is used as the title of wizard step 1 (section `## 1.` has an empty heading). contact.stepProgress keeps the placeholders {current} and {total} literally.
