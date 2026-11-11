# ELLE Dental — site rules the pipeline must satisfy (reference, binding)

These rules are copied from the ELLE Dental publisher in the WebPortals repo
(`ProfitXtraV2/WebPortals`, folder `ElleDental/_publisher/`, branch `feature/elledental-site`
until it is merged to `main`) and from the site spec
`docs/superpowers/specs/2026-11-08-elledental-rebuild-design.md` (sections "SEO requirements"
and "Medical content"). They were read on 2026-11-11. **If the publisher's own files differ
from this copy, the publisher wins**: re-read `banned-terms.json`, `claim-exceptions.json`,
`keyword-map.md`, `clinic.json`, `check_site.py` and `tests/test_content.py` at the start of
every run and log any difference in `log.md`.

The pipeline never writes to WebPortals. It produces a content file; a human copies it there
and runs the site's own gate (`check_site.py`) and build.

---

## 1. The site is medical (YMYL). These rules override SEO goals.

- AI text is a **draft** until a doctor has reviewed it. Medical reviewer: Д-р Елена Манолова.
  A page counts as reviewed only when `reviewed_by` and `reviewed_on` are set by the human
  after a real review. **The pipeline never sets `reviewed_by`, `reviewed_on` or
  `also_reviewed_by`**, never writes a "Медицински преглед" line, and never claims a review.
- **Never remove** a warning, risk, contraindication, number, link, `{{TOKEN}}`, `[[sources]]`
  entry, existing `[[clinical_items]]` entry, FAQ answer's medical content, or the urgent-care
  block. Rewording is allowed; deletion is not. A merged duplicate must keep the stricter wording.
- **Every new medical fact** needs (a) an authoritative source (NHS, Mayo Clinic, Cleveland
  Clinic, ADA, Cochrane, a European specialist society guideline such as ESE/EFP, a national
  regulator, or a peer-reviewed paper) whose URL returns HTTP 200, added to `[[sources]]` with
  empty `checked_by` / `checked_on`; and (b) one `[[clinical_items]]` entry describing the new
  fact, with `decision = ""`, `decided_by = ""`, `decided_on = ""`. **At most 3 new medical
  facts per page per run.** Never add a medical claim without a source.
- No invented patient stories, patients, testimonials, experience, years, case counts,
  equipment, brands of materials, visit durations, numbers of visits, or credentials. Where a
  page needs a real duration or visit count, write what is known and add a
  `[[clinical_items]]` entry asking the doctors for it.
- **Emergency wording is never downgraded.** Use the strictest rule found anywhere on the site:
  high fever with a tooth/gum infection or after treatment → 112 or emergency care; swelling of
  lips or tongue, or trouble breathing soon after anaesthetic → always 112; facial or throat
  swelling that grows or affects breathing or swallowing → 112. Every emergency wording change
  gets a `[[clinical_items]]` entry quoting the old and the new wording.

## 2. Banned terms (`_publisher/banned-terms.json`, 2026-11-11 copy)

Matched case-insensitively on visible text, titles, descriptions, ALT text and JSON-LD.
`*` = any ending. "negation excuses" = allowed only when „не“, „няма“ or „нито“ is among
the three words before the term in the same clause (the site gate's rule). Approved
sentence-level exceptions live in `claim-exceptions.json` (empty on 2026-11-11).

| term | scope | negation excuses |
|---|---|---|
| гарантир*, гаранци* | all | yes |
| перфект* | all | yes |
| безболезнен* | all | **no** (never, even negated) |
| без болка, пълно обезболяване | all | yes |
| напълно безопасн*, абсолютно безопасн* | all | yes |
| напълно обратим*, напълно ефективн* | all | yes |
| пълно възстановяване, възстановят напълно | all | yes |
| безкомпромисн*, най-ефективн* | all | yes |
| връща времето назад, възстанов* младостта | all | yes |
| ботокс*, botox* | all | **no** |
| dysport*, диспорт*, azzalure*, азалур*, азалюр*, аззалур* | all | **no** |
| bocouture*, бокутюр*, xeomin*, ксеомин*, vistabel*, вистабел* | all | **no** |
| opalescence*, опалесценс* | all | **no** |
| мигрена, изпотяване, бруксизъм | `/botulinov-toksin/` only | yes |

Pipeline stance: even where negation is technically excused, prefer to avoid the term.

## 3. No prices, offers or testimonials (site tests)

- PRICE: a digit followed by лв / лева / евро / € / EUR / BGN → forbidden on every page.
- OFFER: цена/цената/цени/цените, промоци*, отстъпк*, оферт*, ваучер* → forbidden in body copy
  (the spec: "Prices anywhere on the site, and sections explaining what affects the price" are
  out of scope).
- TESTIMONIAL: отзив*, „мнения на пациенти“, „доволни пациенти“ → forbidden. Superdoc reviews
  may be linked (doctor pages only), never quoted.

## 4. `/botulinov-toksin/`

Neutral medical information page. No booking wording (`запази час`, `запазете час`, `zapazi`),
no `superdoc`, no doctor names or tokens, no prices, offers, testimonials, no brand names, no
„ботокс“, no medical-use claims (мигрена, изпотяване, бруксизъм). It must keep naming the risks
(птоза/клепач, асиметри*, синин*/кръвонасяд*, инфекци*, алерг*) and the contraindications
(противопоказ*, бременн*, кърм*, невромускул*, лекарств*/медикамент*). A lawyer's answer on
promoting it is pending; the page changes only within these limits.

## 5. Treatment-page structure (`tests/test_content.py`)

Treatment pages (`type = "treatment"`) must keep one H2 matching each pattern
(case-insensitive) and the urgent heading exactly:

| part | H2 must match |
|---|---|
| who it suits | `подходящ\|за кого\|кога се (прави\|поставя\|препоръчва\|налага)` |
| risks | `риск\|усложнени\|странични` |
| alternatives | `алтернатив\|вместо\|друг[аио]? (вариант\|възможност\|решени)` |
| time and visits | `колко (време\|продължава\|посещени\|трае)\|посещения` |
| aftercare | `след \|грижа\|възстановяване` |
| urgent | exactly `## Кога да се обадите веднага`, followed (at the end of that section) by `{{URGENT_CARE}}` |

Each page words its own headings for its treatment; the same wording on every page is a
defect. Target about 6–9 H2s. A clear, predictable order is wanted (ELLE VOICE in
`markets/bg/author.md`); question headings are allowed. Secondary questions go to `[[faq]]` or H3s.

The shared urgent-care block (`shared/urgent-care.md`), inserted by `{{URGENT_CARE}}`, reads:
„В работно време се обадете на {{PHONE}}. Извън работно време, или ако не се свържете с нас,
потърсете дежурен лекар или спешна помощ. При затруднено дишане, подуване на лицето или
гърлото, промяна в зрението или силна болка с побеляване на кожата веднага се обадете на 112.“
The clinic has **no emergency service** and no out-of-hours number. Never imply otherwise.

## 6. SEO limits (`kw-brief.md`, `keyword-map.md`)

- `title` ≤ 60 characters **including** ` | ELLE Dental Clinic`, unique across the site,
  contains „София“.
- `meta_description` ≤ 155 characters (spec floor: aim for 120+), hand-written for that page,
  contains the main term, no skeleton repeated across pages.
- One main search term per address (`keyword-map.md`). Place it **once each** in the title,
  the H1 (as the map proposes), the first 100 words and one H2. Never stuff; use the
  variants patients use elsewhere.
- Keep the H1 unless it is wrong. A medical page's H1 is part of its reviewed text, so a
  changed H1 gets a `[[clinical_items]]` entry.
- The first sentence answers what the treatment is. The clinic name does not go inside the
  definition.
- FAQ: `[[faq]]` entries (`q`, `a`), answers of 1–3 sentences that stand alone and are
  supported by the page or its sources; never a body heading word for word.

## 7. Language and voice

- Bulgarian, formal „Вие“ with the site's capitalised forms (Вие, Ви, Вас, Ваш, Вашия).
- No em-dashes (—) anywhere. Use a comma, colon, full stop, or the hyphen in ranges.
- Correct Bulgarian first: native word order, clitic doubling, agreement, commas. A native
  editor still proofreads every page before launch (spec open item 6).
- ELLE VOICE (owner decision 2026-11-11, full text in `markets/bg/author.md`): professional
  patient information from a modern clinic, comparable to a good national health service
  leaflet. Complete sentences, mostly 12–25 words; paragraphs of 2–4 sentences; lists for steps,
  symptoms and risks; third-person clinic voice („в клиниката“, „лекарят“) or a sparing neutral
  „ние“. No fragments, asides, opinions, colloquial wording or deliberate imperfection.

## 8. Doctors

- Д-р Елена Манолова (`/d-r-elena-manolova/`) and Д-р Теодора Янчева
  (`/d-r-teodora-yancheva/`). Facts only from `clinic.json` and the doctors' own public
  Superdoc profiles (read 2026-11-10, copied into `ElleDental/pipeline/markets/bg/author.md`).
- „има обучение по“ for a course; never say a doctor performs a treatment unless her profile
  lists it. Each page that uses a profile fact adds a `[[clinical_items]]` entry asking that
  doctor to confirm it. Never mention „off label“. Never put a doctor on `/botulinov-toksin/`.

## 9. Content file format (the pipeline's final output)

TOML front matter between `+++` lines, then the Markdown body. Field order as the site uses:

```
+++
title = "… | ELLE Dental Clinic"
meta_description = "…"
h1 = "…"
slug = "…"                     # never changes
type = "treatment"             # treatment | home | info | doctor; never changes
group = "…"                    # treatment pages only; never changes
status = "draft"               # never changes
last_updated = "YYYY-MM-DD"    # the run date
related = ["…", "…"]           # keep existing slugs
written_by = "…"               # keep the existing value
performed_by = []              # only if the page already has it; keep as is
# reviewed_by / reviewed_on / also_reviewed_by: NEVER set by the pipeline

[[faq]]
q = "…"
a = "…"

[[sources]]
title = "…"
url = "…"
checked_by = ""
checked_on = ""

[[clinical_items]]
item = "…"                     # Bulgarian: what changed or what the doctor must confirm
decision = ""
decided_by = ""
decided_on = ""
+++

Body in Markdown, H2 = `## `, links `[текст](/address/)`, tokens `{{TOKEN}}` kept verbatim.
```

Tokens in use on the site (keep verbatim, never expand): `{{CLINIC_NAME}}`, `{{LOGO_LINE}}`,
`{{ADDRESS_FULL}}`, `{{PHONE}}`, `{{PHONE_TEL}}`, `{{EMAIL}}`, `{{HOURS_REGULAR}}`,
`{{HOURS_CLOSED}}`, `{{HOURS_NOTE}}`, `{{LEGAL_DETAILS}}`, `{{DOCTOR_ONE_NAME}}`,
`{{DOCTOR_ONE_SLUG}}`, `{{DOCTOR_ONE_SUPERDOC}}`, `{{DOCTOR_TWO_NAME}}`, `{{DOCTOR_TWO_SLUG}}`,
`{{DOCTOR_TWO_SUPERDOC}}`, `{{URGENT_CARE}}`.

The final content file contains **no** `[VERIFY]`, `[DATA NEEDED]`, `[CONFLICT]` or
`[LINK NEEDED]` markers: the site gate rejects any bracketed placeholder in visible text.
Every open question becomes a `[[clinical_items]]` entry (medical) or a line in
`06-verification.md` under REMAINING FOR HUMAN (non-medical).
