# 04-seo, / (home), 2026-11-11

```
SEO AUDIT — / (home)
Main term: дентална клиника софия + зъболекар софия | Intent: local + commercial (navigational for the brand)
Placement: title Y, H1 Y, first 100 words Y (sentence 1: „дентална клиника в София“, „зъболекарите“), H2 Y („Адрес на денталната клиника в София, работно време и записване на час“)
Relevance score: 88/100 (alignment 24/25 | entities 30/35 | questions 21/25 | on-page 13/15)

TITLE CHECK (publisher checked before judging length):
- build_site.py renders `title` verbatim into <title>, og:title and twitter:title (fill_template only; no suffix appended; layout.html `<title>{{TITLE}}</title>`). Brand is carried by og:site_name ({{CLINIC_NAME}}).
- Treatment/doctor pages write „… | ELLE Dental Clinic“ inside their own title; home, /za-nas/ and /kontakti/ use a sentence title without the suffix (/za-nas/ and /kontakti/ name the brand inline). Home title = 50 chars, contains „София“ and „Света Троица“, unique across the 28 content files. Adding „ | ELLE Dental Clinic“ would make it 70 chars (> 60), so no change. Not a defect.
- meta_description = 154 chars (≤ 155, ≥ 120), contains „Зъболекар“ and „дентална клиника в София“, page-specific, call to action, no prices/offers. Keep.
- H1 = keyword-map proposal verbatim, one H1. Keep (no clinical item needed).

ENTITY COVERAGE (home page scope)
PRESENT: clinic + location (София, ж.к. Света Троица), adults and children, two doctors (tokens), languages, consultation before treatment, risks/alternatives explained, patient decides, dental anxiety, local anaesthesia when needed, natural-looking result, address/hours/phone/Superdoc booking, map/directions (/kontakti/), no emergency line + 112.
MISSING (honestly coverable): none; treatment groups and doctor bios live in the template's treatment and doctor cards by brief (cards link all 19 treatment pages, per step-1 orchestrator check).
ORPHANED: none.

UNANSWERED QUESTIONS: prices (banned), НЗОК / health fund (not in canon → not answerable; no DATA NEEDED flag, out of scope for this run). All other patient questions answered (FAQ Q1-Q4, body).
SYNONYM FIELD: „зъболекар“ (2, incl. „зъболекарите“), „дентална клиника“ (2 incl. H2 variant), „Света Троица“ (2), „София“ (3); natural, no exact-match flooding. „дентален кабинет“ not needed.
DEFECTS: none. 1 H1, H2 hierarchy clean (2 H2, both in Part 2); `<!-- more -->` once, alone on its line; 0 em-dashes; 0 banned terms.
LINKS TO ADD: none. Contextual internal links already present: doctor tokens (Part 1), /za-nas/, /kontakti/, FAQ Q1 /lechenie-na-karies-pri-deca/ + /profilaktika-i-obuchenie/, all from conversion-links.md. Adding more would only repeat the treatment cards.
FAQ CANDIDATES: none new; 4 existing FAQs kept (1-3 formal sentences each, none copies a body heading or sentence word for word).
```

## CHANGE SUMMARY
1. Title, meta_description and H1 kept: no defect (title rendered verbatim, 50 chars, same pattern as /za-nas/ and /kontakti/; meta 154 chars with the main term).
2. Main term once each in title, H1, first 100 words and one H2 (variant); no de-flooding needed.
3. No text edits to body or FAQ: page is identical to 03-humanised.md.
4. No links added (existing 1-3 contextual links from conversion-links.md already in place); no new facts, no flags.
5. Checks: body 266 words (whitespace count incl. headings and tokens), Part 1 = 2 sentences + 5 quick facts, 13/13 tokens, 4 FAQs, CI1 verbatim, `<!-- more -->` once.

## OPTIMISED PAGE

+++
title = "Зъболекар и дентална клиника в София, Света Троица"
meta_description = "Зъболекар и дентална клиника в София, Света Троица, за деца и възрастни: профилактика, кариес, венци, коронки, протези и естетична медицина. Запазете час."
h1 = "Зъболекар и дентална клиника в София, Света Троица"
slug = "home"
type = "home"
status = "draft"
last_updated = "2026-11-11"
related = []

[[clinical_items]]
item = "Страницата използва данни от профилите на д-р Елена Манолова и д-р Теодора Янчева в Superdoc (прочетени на 10 ноември 2026 г.): образование и години, специалност на д-р Манолова (2024 г., Медицински университет – Пловдив), 5 години в клиника за комплексни дентални лечения на д-р Янчева, членство в Български зъболекарски съюз, преглед на възрастни и деца и езици (английски и испански; английски и френски). Двете лекарки да потвърдят данните, както и групите лечения, изброени на страницата."
decision = ""
decided_by = ""
decided_on = ""

[[faq]]
q = "Приемате ли деца?"
a = "Да, {{DOCTOR_ONE_NAME}} и {{DOCTOR_TWO_NAME}} преглеждат както възрастни пациенти, така и деца. Информация за детските зъби ще намерите на страниците за [кариес при деца](/lechenie-na-karies-pri-deca/) и [детска профилактика](/profilaktika-i-obuchenie/)."

[[faq]]
q = "На какви езици може да се проведе прегледът?"
a = "{{DOCTOR_ONE_NAME}} владее английски и испански, а {{DOCTOR_TWO_NAME}} владее английски и френски. Моля, посочете предпочитания език при записването на час."

[[faq]]
q = "Как да запазя час?"
a = "Час се запазва на телефон {{PHONE}} или чрез профила на лекаря в Superdoc: [{{DOCTOR_ONE_NAME}}]({{DOCTOR_ONE_SUPERDOC}}) или [{{DOCTOR_TWO_NAME}}]({{DOCTOR_TWO_SUPERDOC}})."

[[faq]]
q = "Има ли спешен телефон извън работното време?"
a = "Не, клиниката няма спешен номер и извън работното време телефонът ѝ не се обслужва. В такъв случай потърсете дежурен лекар или спешна помощ, а при затруднено дишане или подуване на лицето или гърлото незабавно се обадете на 112."
+++

{{CLINIC_NAME}} е дентална клиника в София, в ж.к. Света Троица, където зъболекарите преглеждат и лекуват както възрастни пациенти, така и деца. В клиниката се извършват профилактика, лечение на зъбите и венците, възстановяване и естетика на зъбите, както и процедури по естетична медицина, представени по-долу на страницата.

- Пациенти: възрастни и деца, като родителят и детето могат да се лекуват при един и същ лекар.
- Лекари: [{{DOCTOR_ONE_NAME}}](/{{DOCTOR_ONE_SLUG}}/) и [{{DOCTOR_TWO_NAME}}](/{{DOCTOR_TWO_SLUG}}/).
- Езици: двете лекарки говорят английски, {{DOCTOR_ONE_NAME}} владее и испански, а {{DOCTOR_TWO_NAME}} владее и френски.
- Местоположение: ж.к. Света Троица, София.
- Записване: по телефона или чрез профила на всяка от лекарките в Superdoc.

<!-- more -->

## Какво да очаквате при посещение

Лекарят преценява след преглед кое лечение е подходящо във Вашия случай. Преди всяка процедура той обяснява какво предстои, какви са рисковете и какви алтернативи съществуват. Решението за лечението вземате Вие след този разговор.

Ако изпитвате притеснение от посещението при зъболекар, моля, споделете това с лекаря. В клиниката се работи спокойно и без бързане, с локална упойка, когато тя е необходима. При денталните и естетичните процедури целта е естествен вид. Повече за начина на работа в клиниката можете да прочетете на страницата [За нас](/za-nas/).

## Адрес на денталната клиника в София, работно време и записване на час

Клиниката се намира на адрес {{ADDRESS_FULL}}. {{HOURS_REGULAR}}. {{HOURS_CLOSED}}. {{HOURS_NOTE}}

Можете да запазите час на телефон [{{PHONE}}](tel:{{PHONE_TEL}}) или чрез профила на лекаря в Superdoc: [{{DOCTOR_ONE_NAME}}]({{DOCTOR_ONE_SUPERDOC}}) или [{{DOCTOR_TWO_NAME}}]({{DOCTOR_TWO_SUPERDOC}}). Ако желаете прегледът да се проведе на английски, испански или френски, моля, посочете това при записването на час.

Карта, упътване и форма за писмено запитване до клиниката ще намерите на страницата [Контакти](/kontakti/).
