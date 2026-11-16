# Consultation form copy: report (2026-11-16)

Source: biz-grow `main` @ f49f083 (consent plumbing uncommitted in the working tree). Light path: Step 2 edit → Step 3 professional-quality edit → Step 5 Brand Gate → Step 5b light re-check, each a fresh-context subagent. Gemini skipped by instruction. Steps 1, 1.5, 4 skipped (form copy, no main term).

## Gate result

**PASS, 95/100** (Voice 19/20 · Language 14/15 · Trust & claims 19/20 · Usefulness 14/15 · Anti-AI 15/15; SEO and check 9 N/A). Blocking checks 1–8, 10, 11 PASS; no criticals. Gate fix: EN `s4.help` fragment. Step 5b fix: removed the comma before „или“ in the s8 help line.

Structure verified by running the site's real `sync-consultation-form.mjs` on the final template (copy in `_tmp/`): 8 sections, all 63 ids identical to the source; field kinds, required/optional, `max: 2` and option counts identical; `consent` parsed; s7 options byte-identical; EN keys = old keys + `consent`, every id has an EN string; contact.json 19 keys per locale, same set in bg and en; 0 em-dashes; no „доклад“.

## Changed strings: BG template (docs/forma-bezplatna-konsultacia.md)

| id | before | after |
|---|---|---|
| s1.f2 | Служебен имейл | Имейл (still `[имейл поле]`, required) |
| s2 | …размерът на вашия екип… | …размерът на Вашия екип… |
| s2.help | Помага ни да преценим мащаба на процесите и нужната инфраструктура. | Помага ни да преценим мащаба на процесите и какво е нужно за тях. |
| s3 | …от бизнеса ви отнема… | …от бизнеса Ви отнема… |
| s3.o2 | Продажби, генериране на лийдове и последваща комуникация (follow-up) | Продажби, привличане на потенциални клиенти и последваща връзка с тях |
| s4.help | За да проверим възможностите за директна интеграция. | Така ще видим кои от Вашите програми могат да се свържат директно. |
| s4.o2 | CRM система (напр. HubSpot, …) | CRM система (програма за клиенти и продажби, напр. HubSpot, …) |
| s4.o5 | Счетоводен / ERP софтуер | Счетоводен софтуер или ERP (система за управление на цялата фирма) |
| s5.help | Помага ни да изчислим потенциалната възвръщаемост на инвестицията. | Помага ни да преценим доколко автоматизацията би се изплатила за Вас. |
| s6 | …основната ви цел… | …основната Ви цел… |
| s6.help | …най-важното за вас… | …най-важното за Вас… |
| s7.help | …реалистични инструменти, от готови no-code решения до разработка по поръчка. | …реалистични инструменти: от готови решения, които се настройват без програмиране, до разработка по поръчка. |
| s8.help | …опира до капацитет, или бизнесът… | …опира до капацитет или бизнесът… |
| consent (NEW) | (none) | Съгласие: Давате съгласие BizGrow да използва данните от формата, за да се свърже с Вас по това запитване. |
| note | Изпращането не ви обвързва. … | Изпращането не Ви обвързва. … |

Unchanged: the s7 question, options and amounts; all other options; title; button; „Попълнен пример“ (still consistent: „Счетоводен софтуер“ still starts the new s4.o5).

## Changed strings: EN labels (site/src/content/consultation-form.en.ts)

| key | before | after |
|---|---|---|
| consent (NEW) | (none) | You agree that BizGrow may use the data from this form to contact you about this request. |
| s1.f2 | Work email | Email |
| s3.o2 | Sales, lead generation and follow-up | Sales, finding potential customers and following up with them |
| s4.help | So we can see what can be connected directly. | This helps us see which of your tools can be connected directly. |
| s4.o2 | A CRM (for example HubSpot, …) | A CRM (software for customers and sales, for example HubSpot, …) |
| s4.o5 | Accounting / ERP software | Accounting software or ERP (a system for running the whole company) |
| s5.help | This helps us estimate the return on the time you would get back. | This helps us estimate whether automation would pay off for you. |
| s7.help | …from ready-made no-code setups to a custom build. | …from ready-made setups that need no programming to a custom build. |

## Changed strings: contact (bg.ts / en.ts)

| key | before | after |
|---|---|---|
| bg.writtenBody | …и не ви обвързва с нищо. | …и не Ви обвързва с нищо. |
| bg.contactLead | Как да се свържем с вас? | Как да се свържем с Вас? |
| en.writtenTitle | Submit written request | Submit a written request |
| en.writtenButton | Submit written request | Submit a written request |
| en.emailCopied | Email was copied | Email copied |
| sending (NEW) | (none) | bg Изпращане… / en Sending… |
| sentTitle (NEW) | (none) | bg Благодарим Ви за запитването / en Thank you for your request |
| sentBody (NEW) | (none) | bg Запитването Ви е изпратено. Ще се свържем с Вас, за да уговорим 30-минутния разговор. / en Your request has been sent. We will contact you to arrange the 30-minute call. |
| sendError (NEW) | (none) | bg Изпращането не успя, затова Ви молим да ни пишете на имейл адреса по-долу, който можете да копирате. / en Sending failed, so please write to us at the email address shown below, which you can copy. |
| mailSubject (NEW) | (none) | bg Запитване за безплатна консултация от / en Free consultation request from |

`mailFallback` dropped per the owner's update (automatic sending only). All other contact keys unchanged.

## Owner items

1. s7 budget amounts are prices, which site rules and canon forbid in page copy. Kept as the owner's own form options (not removed by any stage); owner to confirm they stay.
2. Consent wording is a plain-language draft, not legal advice; owner (or whoever handles GDPR) to confirm. Optional: add the canon „Работим по GDPR.“ / "We work under GDPR." after it (left out to keep one sentence).
3. The privacy page does not exist yet, so the required consent checkbox has no policy to link to. Footer link text is still „Поверителност“ / "Privacy" (planned: „Политика за поверителност“ / "Privacy policy"); the sentence reads well either way. Owner to decide whether the form goes live before the privacy page.
4. The title „Безплатна консултация“ and mailSubject say „консултация“, while canon and CTAs say „безплатна диагностика“ for the same free call. Owner may align the term site-wide.
5. s8.o1 „Не съм готов. И сега едва смогваме“ mixes „аз“ and „ние“ (owner wording, unchanged).
6. The note keeps the owner's „какво може да се оправи“ (a more formal „подобри“ shifts the meaning slightly, unchanged).
7. The existing booking button „Запазете видеоразговор сега“ / "Book a video call now" adds „сега“ / "now" to the approved CTA. Not urgency wording; owner may drop it.
8. Confirm „около три минути“ still holds now that there is a consent step.
9. sentBody promises contact with no time frame. With automatic sending only, every incoming request must actually be answered.
10. For the porter: the sync script's printed id list does not include `consent` (the translate() in consultation-form.ts already handles it).
