# 06-verification, / (home), 2026-11-11

Deliverable: `content/home.md` (front matter byte-identical to 00-current.md, which already has
`last_updated = "2026-11-11"`; body from 05b-final-draft.md, unchanged).

## RESOLVED-TO-CLINICAL-ITEMS
- None. 05b-final-draft.md contains no `[VERIFY]`, `[DATA NEEDED]`, `[CONFLICT]` or
  `[LINK NEEDED]` markers. No new medical facts, no emergency-wording change (FAQ Q4 verbatim),
  no H1 change, no doctor-profile fact newly used (the bio facts were removed; CI1 still covers
  the profile data), and the Brand Gate raised no clinical items. No sources fetched.

## REMAINING FOR HUMAN
1. Intentional removals (REMOVE-BY-BRIEF, owner brief 2026-11-11), not defects:
   - The treatment list with 19 internal links: /profilaktichni-pregledi/, /lechenie-na-karies/,
     /diagnostika-i-lechenie-na-gingivit-i-parodontit/, /zabni-koroni/, /zabni-mostove/,
     /protezi/, /pochistvane-na-zaben-kamak-i-polirane/, /silanti/, /lechenie-na-pulpiti/,
     /lechenie-na-peridontiti/, /dalboko-pochistvane-zakrit-i-otkrit-kjuretazh/,
     /poddarzhashta-terapija/, /bonding/, /faseti/, /izbelvane-na-zabi/,
     /ortodontsko-lechenie-s-alajneri/, /precizni-intervencii-s-minimalen-diskomfort/,
     /dermalni-filari/, /mezoterapija-i-biorevitalizacija/. The treatment cards in
     `_publisher/templates/home.html` link all 19 (orchestrator check after step 1). Confirm
     after the build that the rendered home page still shows those cards.
   - Doctor bio paragraphs: graduation MU Sofia 2020, specialty „Протетична дентална медицина“
     2024 (MU Plovdiv), focus on crowns/bridges/dentures, courses and interests of both doctors,
     5 years in a comprehensive-treatment clinic, „над 5 години опит“, БЗС membership. Still
     covered by CI1 and the doctor pages / template doctor cards.
   - H2 „Езици“ and H2 „Дентална клиника в София за цялото семейство“ merged into the Part 1
     quick facts (content kept).
2. Title is 50 chars with no ` | ELLE Dental Clinic` suffix (would be 70 with it). Step 4
   confirmed build_site.py renders `title` verbatim and home/za-nas/kontakti use this pattern;
   title kept unchanged per brief. Owner may confirm.
3. Copy `content/home.md` into `WebPortals/ElleDental/_publisher/content/home.md` and run the
   site's own gate (`check_site.py`) and build. Native-editor proofread still pending
   (spec open item 6). CI1 still awaits the doctors' decision.

## SELF-CHECK
| check | result |
|---|---|
| TOML front matter parses (Python 3.14 tomllib) | PASS |
| Field order/fields as current file; no reviewed_by/reviewed_on/also_reviewed_by; no added fields | PASS (byte-identical) |
| last_updated = 2026-11-11 | PASS |
| Title ≤ 60 incl. suffix, contains „София“ | „София“ PASS; 50 chars, no suffix (see REMAINING 2) |
| meta_description ≤ 155 | PASS (154) |
| `—` count | PASS (0) |
| Bracketed markers | PASS (0) |
| Banned terms (site-rules §2) | PASS (0) |
| PRICE / OFFER / TESTIMONIAL | PASS (0 / 0 / 0) |
| Six treatment H2s + urgent heading + {{URGENT_CARE}} | N/A (type = home) |
| Botulinum rules | N/A |
| `<!-- more -->` exactly once, alone on its line | PASS |
| Tokens from current page (13) | PASS (13/13) |
| Links all in conversion-links.md or token links | PASS (9 links, 0 off-list) |
| Must-survive inventory items: W1-W3 + N1 (FAQ Q4 verbatim, „112“), W4 „Лекарят преценява след преглед кое лечение е подходящо във Вашия случай“, W5 „какви са рисковете и какви алтернативи съществуват. Решението за лечението вземате Вие“, W6 „с локална упойка, когато тя е необходима“, W7 „целта е естествен вид“, W8 „посочете това при записването на час“, F1-F5, L1-L9, CI1 verbatim, Q1-Q4 | PASS |
| Body word count (whitespace split, after front matter) | 266 |

## COUNTS
new facts: 0 · clinical items added: 0 · existing kept: 1 · sources added: 0
