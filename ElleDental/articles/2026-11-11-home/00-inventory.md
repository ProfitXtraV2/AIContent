# 00-inventory — / (home), from 00-current.md

Every item below must survive every editing stage with the same meaning, EXCEPT items marked
**[REMOVE-BY-BRIEF]**: the owner's brief for this run (00-brief.md) removes the long treatment
list and the doctors' biography paragraphs from the body, because the page template's own
treatment cards and doctor cards already show them. Those removals are intentional and are
reported as such in the inventory diffs; they are not defects.

## A. Warnings / safety / practical (MUST SURVIVE)
- W1 (FAQ) The clinic has no emergency number; outside working hours the phone is not answered.
- W2 (FAQ) Outside hours: look for a duty doctor (дежурен лекар) or emergency care (спешна помощ).
- W3 (FAQ) Trouble breathing or swelling of the face or throat → call 112 immediately.
- W4 (body) Which treatment suits the patient is decided by the doctor after an examination.
- W5 (body) Before every procedure the doctor explains what is planned, the risks and the alternatives; the decision is the patient's, after that conversation.
- W6 (body) If anxious about the visit, tell the doctor; calm, unhurried work; local anaesthetic when it is necessary.
- W7 (body) Aim of dental and aesthetic procedures: a natural look (practical/approach statement, keep).
- W8 (body) Tell the clinic your preferred language when booking.

## B. Risks / contraindications
- None on this page.

## C. Numbers
- N1 112 (FAQ) — MUST SURVIVE.
- N2 „10 ноември 2026 г.“ (existing clinical item) — MUST SURVIVE (clinical item kept verbatim).
- N3 2020 (graduation, both doctors) — body bio **[REMOVE-BY-BRIEF]** (remains in the clinical item and on the doctor pages).
- N4 2024 (Манолова specialty, Пловдив) — body bio **[REMOVE-BY-BRIEF]** (remains in clinical item).
- N5 „над 5 години опит“ / „5 години“ (Янчева) — body bio **[REMOVE-BY-BRIEF]** (remains in clinical item).

## D. Tokens (MUST SURVIVE, verbatim)
{{CLINIC_NAME}}, {{DOCTOR_ONE_NAME}}, {{DOCTOR_TWO_NAME}}, {{DOCTOR_ONE_SLUG}}, {{DOCTOR_TWO_SLUG}},
{{DOCTOR_ONE_SUPERDOC}}, {{DOCTOR_TWO_SUPERDOC}}, {{PHONE}}, {{PHONE_TEL}}, {{ADDRESS_FULL}},
{{HOURS_REGULAR}}, {{HOURS_CLOSED}}, {{HOURS_NOTE}}

## E. Links
MUST SURVIVE:
- L1 /{{DOCTOR_ONE_SLUG}}/ (body)
- L2 /{{DOCTOR_TWO_SLUG}}/ (body)
- L3 tel:{{PHONE_TEL}} (body)
- L4 {{DOCTOR_ONE_SUPERDOC}} (body + FAQ)
- L5 {{DOCTOR_TWO_SUPERDOC}} (body + FAQ)
- L6 /kontakti/ (body: map, directions, written enquiry form)
- L7 /za-nas/ (body: how the clinic works)
- L8 /lechenie-na-karies-pri-deca/ (body + FAQ; survives through the FAQ at minimum)
- L9 /profilaktika-i-obuchenie/ (body + FAQ; survives through the FAQ at minimum)

**[REMOVE-BY-BRIEF]** (treatment list / intro list of treatments; the template's treatment cards cover them):
/profilaktichni-pregledi/, /lechenie-na-karies/, /diagnostika-i-lechenie-na-gingivit-i-parodontit/,
/zabni-koroni/, /zabni-mostove/, /protezi/, /pochistvane-na-zaben-kamak-i-polirane/, /silanti/,
/lechenie-na-pulpiti/, /lechenie-na-peridontiti/, /dalboko-pochistvane-zakrit-i-otkrit-kjuretazh/,
/poddarzhashta-terapija/, /bonding/, /faseti/, /izbelvane-na-zabi/,
/ortodontsko-lechenie-s-alajneri/, /precizni-intervencii-s-minimalen-diskomfort/,
/dermalni-filari/, /mezoterapija-i-biorevitalizacija/
(Stages may keep a few of these if natural; none may be added that is not in conversion-links.md.)

## F. Facts (non-medical, from canon)
MUST SURVIVE:
- F1 Dental clinic in София, ж.к. Света Троица.
- F2 Both doctors see adults and children (parent and child can be treated by the same doctor).
- F3 Languages: both English; Манолова also Spanish; Янчева also French.
- F4 Booking by phone or via the doctor's Superdoc profile.
- F5 Address and hours via tokens; /kontakti/ has map, directions and a written-enquiry form.
- F6 Treatment groups exist in the clinic (prevention, caries/root canal, gums, restoration and aesthetics, aligners, surgery, aesthetic medicine) — the detailed list is **[REMOVE-BY-BRIEF]**; a one-line general mention may stay.
**[REMOVE-BY-BRIEF]** (bio paragraphs): MU Sofia 2020; specialty „Протетична дентална медицина“ 2024 MU Plovdiv; focus on crowns, bridges, dentures; courses (aesthetic restorations, endodontics, preparation for crowns and veneers, dermal fillers); Янчева 5 years in a comprehensive-treatment clinic; interests (biomimetic conservative dentistry, high-aesthetic restorations, digital dentistry); courses (direct and ceramic restorations, dental photography, aligners); BZS membership; „над 5 години опит“.
- Note: no Superdoc rating appears on the current page, so the brief's optional rating fact is NOT used.

## G. Sources
- None ([[sources]] absent).

## H. Existing clinical items (MUST SURVIVE verbatim)
- CI1 Superdoc profile data (read 10 Nov 2026) for both doctors: education and years, specialty, 5 years, BZS, adults and children, languages; doctors to confirm, and the treatment groups listed on the page.

## I. FAQ (MUST SURVIVE; wording may improve)
- Q1 Приемате ли деца? (links L8, L9)
- Q2 На какви езици може да се проведе прегледът?
- Q3 Как да запазя час? (L4, L5, {{PHONE}})
- Q4 Има ли спешен телефон извън работното време? (W1-W3, N1)

## J. Front matter
title, meta_description, h1, slug="home", type="home", status="draft", related=[] — keep
(title/meta/h1 change only if the SEO step finds a defect). No written_by / group fields on the current file: do not add.

Counts: 8 warnings/practical, 0 risks, 0 contraindications, 5 numbers (2 must-survive), 28 links (9 must-survive, 19 remove-by-brief), 13 tokens, 0 sources, 1 clinical item, 4 FAQs.
