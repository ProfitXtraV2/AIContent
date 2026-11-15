# 03 · Step 3 professional-quality reports: follow-up 2026-11-15 (items A, B, C)

Checks run on all three drafts: em-dashes and en-dashes used as dashes (0), „ти“ forms (0), lowercase courtesy pronouns in direct address (0), exclamation marks (0), price patterns (0), „доклад“ (0), delivery periods (0), guarantee wording (0), „безплатн*“ only for the diagnosis. JSON keys, ids, hrefs, icons, paths, related and tool unchanged in all outputs (key structure compared programmatically for reklama).

---

## A. /saveti/ (new hub)

```
PROFESSIONAL-QUALITY REPORT: /saveti/ (bg)
Verdict: PUBLISH-READY
Correctness 9/10 | Clarity 9/10 | Register 9/10 | Readability 8/10 | No AI tells 9/10
CRITICAL (must fix): none
MODERATE:
- lead, sentence 1 (about 38 words): „Тук ще намерите практични съвети … и как да планирате
  съдържанието и рекламата си.“ → long, but it is a colon list lead-in with three real topic
  items, which the rules allow → left as written.
PRESERVE (already good):
- First sentence states what the page offers; AI and SEO explained on first use
  („изкуствен интелект (AI)“, „да се показва по-добре в Google (SEO)“).
- CTA link to /diagnostika/ worded without urgency; no promise beyond the hub's purpose.
- Title 52 chars incl. suffix; meta description 136 chars; label „Съвети“, path, tool "hub",
  sections [], faq [], 3 related service paths as the inventory requires.
```
Change log: no edits; 03-humanised/saveti.json is a copy of the draft.

---

## B. Home service cards + nav

Reviewed as new copy: cards izrabotka-na-sait, izrabotka-na-onlain-magazin, reklama-vav-facebook, the edited /reklama/ card and services_title. The five live owner-approved cards were checked for hard errors only (none found).

```
PROFESSIONAL-QUALITY REPORT: home #services cards and nav (bg)
Verdict: PUBLISH-READY
Correctness 9/10 | Clarity 9/10 | Register 9/10 | Readability 9/10 | No AI tells 9/10
CRITICAL (must fix): none
MODERATE: none
MINOR (no edit):
- Facebook card opens „Маркетинг специалистът …“ (definite form) and relies on the /reklama/
  card above for „Реален маркетинг специалист“. Reads correctly in the grid order; left as is.
- Both advertising cards use icon "chart" (not a copy issue; icons are out of scope).
PRESERVE (already good):
- Site card: build + maintenance + short monthly report, all canon, no platform or period.
- Online-shop card: only canon capabilities (product descriptions for whole collections,
  automatic messages for abandoned carts), framed as „можем да добавим“, no promise.
- /reklama/ card: Google only, specialist plans/runs/tracks, numbers, „какво връща всяко
  вложено евро“ (canon).
- services_title adds „сайтове“ cleanly; nav adds „Съвети“ → /saveti/, other links unchanged.
```
Change log: no edits; 03-humanised/home-cards.json is a copy of the draft.

---

## C. /reklama/ (minimal Google-only edit)

New copy reviewed = the strings that differ from `_tmp/reklama.current.json` (meta.title, meta.description, label, summary, eyebrow, h1, lead, specialist paragraph, „Планиране“ bullet, facebook-instagram title and paragraph, FAQ 6 answer, related[0], service). Unchanged owner-approved strings were left alone.

```
PROFESSIONAL-QUALITY REPORT: /reklama/ (bg)
Verdict: NEEDS EDIT
Correctness 7/10 | Clarity 8/10 | Register 9/10 | Readability 8/10 | No AI tells 8/10
CRITICAL (must fix):
- meta.description: „Реклама в Гугъл и Google Ads управление от маркетинг специалист“ →
  English word order (keyword calque) → „Реклама в Гугъл и управление на Google Ads от
  маркетинг специалист“.
- facebook-instagram paragraph: „… можем да подготвяме всеки месец, повече за това ще намерите
  на страницата […]“ → comma splice; also dropped „публикации“ from inventory item C12
  (branded visuals, posts, advertising materials) → „Брандирани визии, публикации и рекламни
  материали за кампаниите можем да подготвяме всеки месец в рамките на услугата
  [поддръжка на социални мрежи и криейтиви](/socialni-mrezhi/).“ (section stays at 3 sentences,
  per R2).
MODERATE:
- specialist paragraph: „поема управлението на Google Ads, от планирането до изпълнението“
  repeats „от планирането до …“ from the first sentence → „Специалистът управлява кампаниите
  в Google Ads, като поема планирането и изпълнението, а при Вас остава отчетът с резултатите.“
  (C10 meaning kept).
- FAQ 6 answer: „Можете да използвате един канал или няколко, а рекламата във Facebook и
  Instagram е описана …“ → „а“ joins two unrelated statements → split into two sentences.
PRESERVE (already good):
- Title 48 chars, Google-only label/h1/summary/service, eyebrow, lead with C7–C9 and C16.
- „Планиране“ bullet now Google-only and concrete.
- Section title „Кампании извън Google“ with the /reklama-vav-facebook/ pointer (R2).
- „Гугъл“ in title/meta/lead kept: it is the page's primary keyword from the baseline.
```

### Change log (reklama)
1. meta.description: „Google Ads управление“ → „управление на Google Ads“ (natural word order; 157 chars, still within 120–160; secondary term „google ads управление“ is now matched by phrase, not exact order).
2. sections[0].paragraphs[0], sentence 3: repetition removed, C10 meaning unchanged.
3. sections[2].paragraphs[0], sentence 3: comma splice fixed, „публикации“ restored (C12), /socialni-mrezhi/ link kept.
4. faq[5].answer: split into two sentences, /reklama-vav-facebook/ link kept.
Preserved: every CTA, token, link, id, related path, number (30-минутен), source-based fact. No flags in the text.

### Inventory diff (03-humanised/reklama.json)

| Item | Present | Where |
|---|---|---|
| C1 | yes | proces: „[Запазете безплатна диагностика]({{BOOKING_URL}})“ |
| C2 | yes | diagnostika: „[Запазете час]({{BOOKING_URL}})“ |
| C3 | yes | diagnostika: „… или да ни пишете на {{EMAIL}}.“ |
| C4 | yes | proces step 1: „[безплатна диагностика](/diagnostika/)“ |
| C5 | yes | kak-raboti para 4: „[SEO оптимизация на сайтове](/seo-optimizacia/)“ |
| C6 | yes | facebook-instagram para (edited) + FAQ „Кой подготвя визиите“ → /socialni-mrezhi/ |
| C7 | yes | lead: „жив маркетинг специалист планира, пуска и следи вместо Вас“ |
| C8 | yes | lead + otchet + FAQ 4: „отговаря пред Вас с числа“ |
| C9 | yes | lead, summary, „Проследяване“ bullet, otchet, FAQ 4 |
| C10 | yes | specialist para: „поема планирането и изпълнението, а при Вас остава отчетът“ |
| C11 | yes | „Кампании на база данни“ bullet |
| C12 | yes | facebook-instagram: „Брандирани визии, публикации и рекламни материали … всеки месец“ (restored „публикации“) + FAQ 5 |
| C13 | yes | za-kogo: three „подходящо, ако“ situations + 6 bullets |
| C14 | yes | proces steps 1–4 („оферта с приоритизирани решения и ясни еднократни цени“), no delivery period |
| C15 | yes | cena para 1 + FAQ 1 |
| C16 | yes | lead, cena, FAQ 7 |
| C17 | yes | cena: „Работим по GDPR.“ |
| C18 | yes | FAQ 8: „Срокът за изграждане зависи от решението и го посочваме в офертата …“ |
| C19 | yes | kak-raboti para 1, cena para 2, FAQ 1, FAQ 3 |
| C20 | yes | kak-raboti para 2, cena para 2, FAQ 1 |
| C21 | yes | kak-raboti para 3, FAQ 2 |
| C22 | yes | kak-raboti para 1 (PPC) and para 4 (SEO separate), FAQ 3 |
| Section ids | yes | specialist, kak-raboti, facebook-instagram, za-kogo, otchet, proces, cena, diagnostika |
| FAQ (8) | yes | all 8 questions present, wording unchanged |
| R1–R4 | applied | Google-only meta/label/summary/h1/lead/service/bullet; facebook section 3 sentences; FAQ 6 kept and repointed; related[0] = /reklama-vav-facebook/ |

Note: neither the baseline JSON nor the draft carries a sources array; S1/S2 are referenced through the „Според Google“ wording in kak-raboti and FAQ 2, unchanged.
