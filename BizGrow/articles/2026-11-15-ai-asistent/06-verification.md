# 06-verification — /ai-asistent/ (2026-11-15)

Run by the orchestrator (Step 6). Built from 05b-final-draft.md (loop 1) with a generator script so the content file and the port JSON share the exact same strings.

## RESOLVED-TO-OWNER-ITEMS
- No [VERIFY] markers (no external facts; new facts: 0).
- [OWNER CONFIRM: H1] → owner item 1.
- [OWNER CONFIRM: example scenarios … with their numbers] → owner item 2.
- Gate/flag list items (label/summary/eyebrow; website chat; languages outside hotels; contact handoff; model/platform + data location; support pricing [DATA NEEDED]) → owner items 3–8.
- Added at Step 6: owner item 9 (two inferences from canon: channels settled during the diagnosis in FAQ 1; the business decides who follows up in #kakvo-pravi).
- „ти“ → „Вие“ conversions: no existing headings or CTAs on this new page; the checker pain lines used in #primeri were rewritten from „ти“ (noted inside owner item 2).

## REMAINING FOR HUMAN
- none ([LINK NEEDED]: none).

## PORTING NOTES
- Target: a new `ContentPage` (site/src/content/types.ts), e.g. `site/src/content/pages/bg/ai-asistent.ts`; paste `content/ai-asistent.port.json` as the object. No dictionary keys change (all `dictionary_key = ""`).
- `hero` block → `h1` + `lead`. The booking CTA under the lead in the .md is the template's header button („Запазете час“ → {{BOOKING_URL}}) and is not a port string.
- `#proces` → `steps` (numbered; ContentPageView renders paragraphs → steps → bullets).
- `#sledvashta-stapka` keeps `[Запазете безплатна диагностика]({{BOOKING_URL}})` and the `{{EMAIL}}` line as paragraph strings (supported by the updated renderer per the coordinator, 2026-11-15). Note: the template also renders the header booking button and the CTA band after the FAQ, so the page shows several booking buttons in total; at most one per section is respected.
- `related`: /diagnostika/, /avtomatizacii/, /socialni-mrezhi/ (3 sibling paths from conversion-links.md). `service`: „AI асистент и чатбот“.
- After porting run `npm run lint`, `npx tsc --noEmit`, `npm run build` in the site repo. `steps` must exist on `PageSection` in the target branch (present in the working tree checked on 2026-11-15, uncommitted at 528ad25).

## SELF-CHECK
| check | result |
|---|---|
| TOML parses (python 3.14 tomllib) | PASS: 9 sections, 8 faq, 9 owner items |
| title ≤ 60 incl. „ | BizGrow“, no em-dash | PASS: 55 |
| meta_description 120–160, contains main term | PASS: 143, „AI асистент“ |
| primary_keyword = keyword-map term „ai асистент“ | PASS |
| main term in title / H1 / first 100 words / one H2 | PASS (H2 #kakvo-pravi „Какво прави AI асистентът…“) |
| section ids ↔ body blocks, same order and headings | PASS |
| em-dashes / en-dashes | PASS: 0 / 0 (md and port) |
| bracketed markers | PASS: 0 |
| „ти“ forms; lowercase formal pronouns | PASS: 0; 0 |
| banned claims / hype / prices / testimonials / „!“ | PASS: 0 hits |
| numbers | PASS: 30, 48, 2 (canon, „обикновено“ kept); 21:30, 23:00, 40, двадесет (labelled examples, owner item 2) |
| example label | PASS: first paragraph of #primeri |
| inventory items 1–12 | PASS: booking CTA (hero + #sledvashta-stapka), {{EMAIL}} (#sledvashta-stapka), /diagnostika/ (#proces), /avtomatizacii/ (#zadachi), денонощно + contact (lead, #kakvo-pravi), own information (lead, #zadachi), hotel any language (#za-kogo), courier (#za-kogo), real-estate qualification (#za-kogo), process 4 steps (#proces), price formation (#usloviya, FAQ 5), policies + „Работим по GDPR“ (#usloviya) |
| links only from conversion-links.md; tokens | PASS: /avtomatizacii/, /diagnostika/, {{BOOKING_URL}}, {{EMAIL}} |
| port: every string present verbatim in the .md | PASS |
| port: related = 3 siblings, not home, not itself | PASS |
| H2 count / FAQ count | 8 / 8 |

## COUNTS
- new facts: 0
- owner items added: 9
- body words (H1 to end, excl. FAQ): 807; FAQ words: 243
