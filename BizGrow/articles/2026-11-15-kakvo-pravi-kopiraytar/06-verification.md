# 06-verification — /saveti/kakvo-pravi-kopiraytar/ (2026-11-15)

Step 6 run by the orchestrator. Input: 05b-final-draft.md (unchanged from the Gate-fixed page). Both deliverables generated from one data structure (`_tmp/build.py` → `_tmp/page.json` → `_tmp/emit.py`), so the strings in `content/kakvo-pravi-kopiraytar.md` and `content/kakvo-pravi-kopiraytar.port.json` are identical.

## RESOLVED-TO-OWNER-ITEMS
1. [VERIFY] #seo-avtor: „Според насоките на Google автоматичните системи за класиране в търсачката са създадени да показват полезна и надеждна информация, написана преди всичко в полза на хората.“
   - URL: https://developers.google.com/search/docs/fundamentals/creating-helpful-content (curl -sIL → HTTP/2 200, 2026-11-15)
   - Quote: "Google's automated ranking systems are designed to prioritize helpful, reliable information that's created to benefit people, not content that's created to manipulate search engine rankings." and "People-first content means content that's created primarily for people".
   - Verdict: supported in substance; kept, marker removed, added to [[sources]] and [[owner_items]]. Nuance logged for the owner: source verb is "prioritize" (дават предимство на), page says „показват“.
2. [OWNER CONFIRM] H1 from keyword-map.md → owner item.
3. [OWNER CONFIRM] hypothetical example brief (beauty salon), labelled „пример, не реален случай“ → owner item.
4. [OWNER CONFIRM] whether anyone at BizGrow reviews the content tool's output before client approval → owner item.
5. Added: article fields (eyebrow, label, summary, related) for confirmation; summary and meta description start with the same words.
No „ти“ → „Вие“ conversions (new page).

## REMAINING FOR HUMAN
- [LINK NEEDED]: none.
- Pipeline note from the Brand Gate (not a page item): `pipeline/markets/bg/author.md` PRICES paragraph still says the price is "given in the report"; should read „оферта“ to match the 2026-11-15 canon. Shared pipeline file, not edited by this run.
- The related cards and in-body links to /saveti/klyuchovi-dumi/ only resolve once that article is published; the RichText link to it is in #zadanie (step 5).

## PORTING NOTES
- New file `site/src/content/pages/bg/kakvo-pravi-kopiraytar.ts` exporting a `ContentPage` = the JSON in `content/kakvo-pravi-kopiraytar.port.json` (no `service`, eyebrow „Съвети“, status "published", updated "2026-11-15"); register it in `site/src/content/index.ts` and in the /saveti/ hub listing.
- Section shapes: #vidove-tekstove paragraphs+bullets+closing; #zadanie paragraphs+steps+closing (example brief); #podhodyasht-avtor paragraphs+bullets+closing; the rest paragraphs only. The booking CTA is the last paragraph string of #instrument-za-sadarzhanie: `[Запазете безплатна диагностика]({{BOOKING_URL}})`.
- No `Dictionary` type changes needed. Run `npm run lint`, `npx tsc --noEmit`, `npm run build` in the site repo.

## SELF-CHECK (script `_tmp/check.py`, Python 3.14 tomllib)
| TOML parses | PASS |  |
| title<=60 | PASS | 45 |
| meta 120-160 | PASS | 128 |
| meta has term | PASS |  |
| summary<=160 | PASS | 135 |
| primary kw | PASS |  |
| term in first 100 words | PASS |  |
| term in title | PASS |  |
| term in H1 (variant) | PASS | Какво прави копирайтърът и кога Ви трябва |
| term in an H2 | PASS |  |
| section ids/headings match | PASS |  |
| no em/en dash | PASS |  |
| no bracket markers | PASS |  |
| no ти forms | FAIL | ['запази', 'запази'] |
| no lowercase formal pronouns | PASS | [] |
| no banned/hype/sibling terms | PASS | [] |
| безплатн only diagnosis | PASS | ['безплатната диагностика', 'безплатна диагностика', 'безплатната диагностика'] |
| numbers only 30 | FAIL | ['30', '1'] |
| no periods | FAIL | ['седмиц'] |
| links in conversion-links | PASS | ['/saveti/klyuchovi-dumi/', '/seo-statii/', '/diagnostika/', '{{BOOKING_URL}}'] |
| one booking CTA | PASS |  |
| related 3 valid | PASS |  |
| no service key | PASS |  |
| H2 count 6-8 | PASS | 7 |
| FAQ 4-6 | PASS | 6 |
| body words 900-1400 | PASS | 949 |
| port strings == md strings | PASS | [] |
| example label present | PASS |  |
| inventory: инструмент за съдържание | PASS |  |
| inventory: бранш и град | PASS |  |
| inventory: цели колекции | PASS |  |
| inventory: по график | PASS |  |
| inventory: преди да го одобрите | PASS |  |
| inventory: 30-минутен разговор | PASS |  |
| inventory: оферта с приоритизирани решения и ясни еднократни цени | PASS |  |
| inventory: без дългосрочен договор | PASS |  |
| inventory: не ви задължава | PASS |  |
| inventory: срокът зависи от решението и го посочваме в офертата | PASS |  |
| inventory: /seo-statii/ | PASS |  |
| inventory: /diagnostika/ | PASS |  |

Reviewed FAILs (all false positives, no fix needed):
- „no ти forms“ hit „запази“: the text is third person „читателят да направи следваща стъпка, например да се обади, да купи или да запази час“ (lead) and the same in #zadanie step 1; not a „ти“ imperative.
- „numbers only 30“ hit „1“: the JSON key `h1` in the checker's dump; the visible copy contains only „30-минутен“.
- „no periods“ hit „седмиц“: „публикации всяка седмица“ in #sami-ili-s-ai is a publishing frequency of the reader's own posts, not a delivery period.

Main term placement: title „Какво е копирайтър и кога Ви трябва | BizGrow“ (45), H1 „Какво прави копирайтърът и кога Ви трябва“ (inflected), lead sentence 1, H2 #kakvo-e-kopiraytar. Meta 128 chars. Body 949 words (whitespace tokens, H2 sections only; earlier stages counted 963–969 by word regex).

new facts: 1
owner items added: 5
