# 01-synthesis — / (home), 2026-11-11

## SYNTHESIS REPORT

Page: / (slug `home`) | Type: page-rewrite (owner UX-restructure brief) | Main term: дентална клиника софия + зъболекар софия | Intent: local / commercial-navigational (a patient in София looking for a clinic near Света Троица: who, where, which patients, how to book)
Current facts kept: 13 (W1-W8, N1, N2, F1-F5; F6 as a one-line general mention) | New sourced facts: 0 | Excluded weak claims: 0 | CONFLICT: 0 | DATA NEEDED: 0
Removed by brief (intentional, not defects): treatment list + 19 treatment links (incl. the intro sentence's 6 links); doctors' bio paragraphs (N3 2020, N4 2024, N5 „над 5 години“, БЗС membership, courses, interests). These facts remain in CI1 (verbatim) and on the doctor pages / doctor cards.

Patient questions answerable: children and adults (FAQ Q1 + quick facts); languages (FAQ Q2 + quick facts + booking block); how to book (FAQ Q3 + booking block); emergency / out of hours (FAQ Q4); what happens at a visit, risks and alternatives explained (Part 2).
Not answerable (need doctors/owner): prices (banned on the site); НЗОК contract (UNKNOWN in canon, never stated); doctor qualifications (doctor pages, not the home body per brief).
Excluded claims (with why): Superdoc rating (not on the current page; brief makes it conditional; canon says rating counts are not used). „над 5 години опит“ (canon: Superdoc experience figure not used; also bio removed by brief).

Intent notes: the top of the page must answer "what / where / for whom / which doctors" in seconds, because the treatment cards and doctor cards follow directly. Part 2 serves the patient who has scrolled through cards and now wants reassurance (what to expect) and the practical block (address, hours, booking).

Localisation: patient words used: „зъболекар“, „дентална клиника“, „упойка“ (as „локална упойка“), „венци“. No foreign-source facts on this page.

Structure (brief): Part 1 = 3 sentences + 5 quick-fact lines; `<!-- more -->` exactly once, alone on its line; Part 2 = H2 „what to expect“ (W4-W7) + one H2 block for address, hours, booking (all existing tokens, W8, /kontakti/). Home page: the six treatment-page H2s and the urgent heading do not apply (type = home); emergency facts W1-W3 + N1 stay in FAQ Q4 verbatim.

Main-term placement: „дентална клиника в София“ + „зъболекар“ in sentence 1 (first 100 words); variant „денталната клиника в София“ in one H2. Title / meta / H1 unchanged (no defect found).

## FLAGS FOR LATER STAGES (non-medical)
- [VERIFY: the template's treatment cards link all 19 treatment pages removed from the body; owner/Step 6 to confirm in build_site.py output, otherwise home loses internal links]
- CI1 still names facts (2020, 2024, 5 години, БЗС, курсове) that are no longer in the body. Kept verbatim per brief and site rules (never drop a clinical item); they are still shown in the doctor cards. Step 6 may note this; no new clinical item needed (no medical or emergency wording changed).
- Doctor names in the languages line use tokens (`{{DOCTOR_ONE_NAME}}`, `{{DOCTOR_TWO_NAME}}`) instead of the current page's hard-coded „д-р Манолова“ / „д-р Янчева“; plain text, not links.

---

## THE DRAFT (body)

{{CLINIC_NAME}} е дентална клиника в София, в ж.к. Света Троица, където зъболекар преглежда както възрастни пациенти, така и деца. В клиниката се извършват профилактика, лечение на зъбите и венците, възстановяване и естетика на зъбите, а също и процедури по естетична медицина. Лечебните области и лекарите са представени по-долу на страницата.

- Пациенти: възрастни и деца, като родителят и детето могат да се лекуват при един и същ лекар.
- Лекари: [{{DOCTOR_ONE_NAME}}](/{{DOCTOR_ONE_SLUG}}/) и [{{DOCTOR_TWO_NAME}}](/{{DOCTOR_TWO_SLUG}}/).
- Езици: двете лекарки говорят английски, {{DOCTOR_ONE_NAME}} владее и испански, а {{DOCTOR_TWO_NAME}} владее и френски.
- Местоположение: ж.к. Света Троица, София.
- Записване: по телефона или чрез профила на лекаря в Superdoc.

<!-- more -->

## Какво да очаквате при посещение

Кое лечение е подходящо във Вашия случай, лекарят преценява след преглед. Преди всяка процедура лекарят обяснява какво предстои, какви са рисковете и какви алтернативи съществуват, а решението за лечението се взема от Вас след този разговор.

Ако изпитвате притеснение от посещението при зъболекар, моля, споделете това с лекаря. В клиниката се работи спокойно и без бързане, с локална упойка, когато тя е необходима, а при денталните и естетичните процедури целта е естествен вид. Повече за начина на работа можете да прочетете на страницата [За нас](/za-nas/).

## Адрес на денталната клиника в София, работно време и записване на час

Клиниката се намира на адрес {{ADDRESS_FULL}}. {{HOURS_REGULAR}}. {{HOURS_CLOSED}}. {{HOURS_NOTE}}

Можете да запазите час на телефон [{{PHONE}}](tel:{{PHONE_TEL}}) или чрез профила на лекаря в Superdoc: [{{DOCTOR_ONE_NAME}}]({{DOCTOR_ONE_SUPERDOC}}) или [{{DOCTOR_TWO_NAME}}]({{DOCTOR_TWO_SUPERDOC}}). Ако предпочитате прегледът да се проведе на английски, испански или френски, моля, посочете това при записването на час.

Карта, упътване и форма за писмено запитване до клиниката ще намерите на страницата [Контакти](/kontakti/).

---

## PROPOSED FAQ

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

(All four FAQs kept verbatim: wording already formal and complete; Q4 emergency wording untouched.)

---

## INVENTORY MAP (draft position)
- W1, W2, W3, N1: FAQ Q4 (verbatim).
- W4: Part 2, „Какво да очаквате“, sentence 1 („лекарят преценява след преглед“).
- W5: Part 2, same paragraph („какви са рисковете и какви алтернативи… решението… от Вас“).
- W6, W7: Part 2, paragraph 2 („споделете това с лекаря“, „локална упойка, когато тя е необходима“, „целта е естествен вид“).
- W8: Part 2 booking block („посочете това при записването на час“) + FAQ Q2.
- N2: CI1 verbatim (front matter). N3-N5: REMOVE-BY-BRIEF (remain in CI1).
- Tokens (13/13): CLINIC_NAME (P1), DOCTOR_ONE/TWO_NAME (P1, P2, FAQ), DOCTOR_ONE/TWO_SLUG (P1), DOCTOR_ONE/TWO_SUPERDOC (P2, FAQ), PHONE, PHONE_TEL, ADDRESS_FULL, HOURS_REGULAR, HOURS_CLOSED, HOURS_NOTE (P2).
- Links L1, L2 (P1); L3, L4, L5, L6, L7 (P2); L4, L5, L8, L9 (FAQ). 19 treatment links: REMOVE-BY-BRIEF.
- F1 (P1 sentence 1 + quick fact), F2 (P1 + FAQ Q1), F3 (P1 + P2 + FAQ Q2), F4 (P1 + P2 + FAQ Q3), F5 (P2), F6 (P1 sentence 2, general mention).
- CI1: kept verbatim in front matter. Front matter (title, meta, h1, slug, type, status, related): unchanged; last_updated 2026-11-11.
