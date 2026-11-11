# Conversion Links — ELLE Dental (elledental.bg)

Single source of truth for **internal links and the booking target** used in every ELLE
Dental page the pipeline drafts. Taken from the site's 28 live addresses (WordPress
`page-sitemap.xml`, kept 1:1 by the static rebuild; see the WebPortals spec
`docs/superpowers/specs/2026-11-08-elledental-rebuild-design.md`) on **2026-11-11**.

ELLE Dental is a clinic, not an affiliate site: there are **no affiliate links**, no
partner offers and no prices. Every link in this file points to a page on `elledental.bg`
itself.

**The 28 addresses never change.** No slug is renamed, shortened or "fixed", including the
misspelled ones (`/lechenie-na-peridontiti/`, `/precizni-intervencii-s-minimalen-diskomfort/`).
Only headings and visible text may change. A link to any address not in this file is a
defect: write `[LINK NEEDED: <topic>]` in a draft instead, and never let it reach the final
content file (the owner decides on new pages).

---

## Approved internal links (the 28 site addresses + the booking anchor)

| path | page (H1 per `_publisher/keyword-map.md`) | type | use when |
|---|---|---|---|
| / | Зъболекар и дентална клиника в София, Света Троица | home | orientation; "the clinic" in general |
| /za-nas/ | За ELLE Dental Clinic | info | who the clinic is; team and approach as stated on the site |
| /kontakti/ | Контакти на дентална клиника в София, Света Троица | info | address, phone, hours, directions |
| /kontakti/#zapazi | Запази час (booking block on the contacts page) | booking | the single booking link of a page (never on `/botulinov-toksin/`) |
| /d-r-elena-manolova/ | Д-р Елена Манолова, зъболекар в София | doctor | the page names Д-р Манолова (normally via `{{DOCTOR_ONE_NAME}}` / `{{DOCTOR_ONE_SLUG}}`) |
| /d-r-teodora-yancheva/ | Д-р Теодора Янчева, лекар по дентална медицина в София | doctor | the page names Д-р Янчева (normally via `{{DOCTOR_TWO_NAME}}` / `{{DOCTOR_TWO_SLUG}}`) |
| /privacy/ | Политика за поверителност | legal | forms, data; never as an editorial link |
| /profilaktichni-pregledi/ | Профилактичен преглед при зъболекар | treatment | check-ups, X-rays, prevention |
| /profilaktika-i-obuchenie/ | Детска дентална профилактика и обучение за миене на зъбите | treatment | children's prevention, brushing |
| /pochistvane-na-zaben-kamak-i-polirane/ | Почистване на зъбен камък и полиране | treatment | tartar, cleaning, polishing |
| /silanti/ | Силанти за зъби при деца | treatment | fissure sealants |
| /lechenie-na-karies/ | Лечение на кариес и пломби | treatment | caries, fillings |
| /lechenie-na-karies-pri-deca/ | Кариес при деца: лечение на детски зъби | treatment | children's caries, milk teeth |
| /lechenie-na-pulpiti/ | Лечение на пулпит и кореново лечение | treatment | pulpitis, root canal treatment |
| /lechenie-na-peridontiti/ | Лечение на периодонтит: възпаление около корена на зъба | treatment | periodontitis (root apex), granuloma |
| /diagnostika-i-lechenie-na-gingivit-i-parodontit/ | Лечение на пародонтоза, пародонтит и гингивит | treatment | gum disease (gingivitis, пародонтит, пародонтоза) |
| /dalboko-pochistvane-zakrit-i-otkrit-kjuretazh/ | Кюретаж на венци: дълбоко почистване при пародонтит | treatment | deep cleaning, curettage |
| /poddarzhashta-terapija/ | Поддържаща пародонтална терапия след лечение на венците | treatment | maintenance after gum treatment |
| /precizni-intervencii-s-minimalen-diskomfort/ | Вадене на зъб и мъдрец и дентална хирургия | treatment | extraction, wisdom teeth, oral surgery |
| /izbelvane-na-zabi/ | Избелване на зъби | treatment | whitening |
| /bonding/ | Бондинг на зъби | treatment | composite bonding |
| /faseti/ | Фасети за зъби | treatment | veneers |
| /zabni-koroni/ | Зъбни коронки | treatment | crowns |
| /zabni-mostove/ | Зъбни мостове | treatment | bridges |
| /protezi/ | Зъбни протези | treatment | dentures |
| /ortodontsko-lechenie-s-alajneri/ | Алайнери за зъби: изправяне с прозрачни шини | treatment | aligners, orthodontics |
| /botulinov-toksin/ | Ботулинов токсин | treatment (neutral info) | link label is always exactly „Ботулинов токсин“; see the special rules below |
| /dermalni-filari/ | Дермални филъри | treatment | dermal fillers |
| /mezoterapija-i-biorevitalizacija/ | Мезотерапия и биоревитализация | treatment | mesotherapy, skin boosters, biorevitalisation |

Note: периодонтит vs пародонтит is a known trap. `/lechenie-na-peridontiti/`
is inflammation around the tooth ROOT (периодонтит); the gum-disease page is
`/diagnostika-i-lechenie-na-gingivit-i-parodontit/` (пародонтит). Never swap them.

---

## Link rules

1. **Only addresses from the table.** Never invent a path, never add a trailing-slash-less
   variant, never link a WordPress system path (`/wp-content/`, `/?p=`).
2. **Body links:** 1–3 contextual links per page to related treatment pages, in addition to
   whatever the page already has. Every link the current page has is kept (removal = defect).
   Anchors are plain Bulgarian words a patient would use, never exact-match stuffing.
3. **`related`** in the front matter keeps its existing slugs. Adding a slug is allowed only
   when the body really links that page; removing one is not.
4. **Doctors** are linked through the existing tokens
   (`[{{DOCTOR_ONE_NAME}}](/{{DOCTOR_ONE_SLUG}}/)`, `[{{DOCTOR_TWO_NAME}}](/{{DOCTOR_TWO_SLUG}}/)`),
   never by hard-coded names or slugs in the body. Superdoc links only through
   `{{DOCTOR_ONE_SUPERDOC}}` / `{{DOCTOR_TWO_SUPERDOC}}` and only where the page already uses them.
5. **Booking:** the page template already carries the „Запази час“ button and sticky bar. The
   body may add at most one plain link to `/kontakti/#zapazi`. No urgency wording
   („запазете сега“, „само днес“, „последни часове“), ever.
6. **No external links in the body** except the page's own `[[sources]]` (rendered by the
   template) and the doctors' Superdoc tokens. No competitor clinics, directories or portals.

## `/botulinov-toksin/` special rules (binding)

- Neutral medical information only. No booking wording („запази час“, „запазете час“), no
  `/kontakti/#zapazi` link, no doctor names or tokens, no Superdoc, no testimonials, no
  prices or offers.
- Always „ботулинов токсин“: never „ботокс“, never a brand name (Botox, Dysport, Azzalure,
  Bocouture, Xeomin, Vistabel, in any script).
- No medical-use claims (мигрена, изпотяване, бруксизъм are banned on this page).
- Other pages that link here use the label „Ботулинов токсин“ exactly.
