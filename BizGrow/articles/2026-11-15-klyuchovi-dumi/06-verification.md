# 06-VERIFICATION — /saveti/klyuchovi-dumi/ (Step 6, orchestrator, 2026-11-15)

Input: 05b-final-draft.md (Brand Gate PASS 92/100). Built by `_tmp/build.py` from one data structure into
`content/klyuchovi-dumi.md` and `content/klyuchovi-dumi.port.json`; checked by `_tmp/check.py` (python3.14, tomllib).

## RESOLVED-TO-OWNER-ITEMS (all URLs HTTP 200 via curl -L on 2026-11-15, re-fetched by Step 1)
1. Autocomplete reflects real searches — https://support.google.com/websearch/answer/7368877 — "Once you start to type, autocomplete predictions reflect real searches that have been done on Google." → kept (#kak-da-otkriete step 2), marker removed, [[sources]] + owner item.
2. Search Console Performance report — https://support.google.com/webmasters/answer/7576553 — Clicks: "The number of times a user clicked your site from Google Search results."; Impressions: "How many times your site appeared in Search results."; CTR: "The click count divided by the impression count."; Average position: "The average position of the topmost result from your site."; Queries tab groups data by search terms; default view = past three months. → kept (#kak-da-otkriete step 3), [[sources]] + owner item (also asks to confirm the Bulgarian UI label).
3. Keyword stuffing — https://developers.google.com/search/docs/essentials/spam-policies — "Keyword stuffing refers to the practice of filling a web page with keywords or numbers in an attempt to manipulate rankings in Google Search results."; examples "Blocks of text that list cities and regions that a web page is trying to rank for", "Repeating the same words or phrases so often that it sounds unnatural." → kept (#greshki P2, FAQ 4), [[sources]] + owner item.
4. [OWNER CONFIRM] hypothetical pastry-shop example (#primer) → marker removed, label kept in text, owner item.

## REMAINING FOR HUMAN
- Shared canon file `pipeline/markets/bg/author.md` PRICES paragraph still says "given in the report after the free diagnosis"; PROCESS says „оферта“. Not edited (shared file, parallel runs). Fix once in the pipeline.
- Optional wording notes from Steps 3/5 not applied (no stage was asked to rewrite): „Много собственици питат…“ (owner item 6).
- [LINK NEEDED]: none.

## PORTING NOTES
- New file `site/src/content/pages/bg/klyuchovi-dumi.ts` exporting a `ContentPage` = `content/klyuchovi-dumi.port.json` (no `service`, `eyebrow` „Съвети“). Register it wherever `getPages` collects pages (`site/src/content/index.ts`).
- Nested path `/saveti/klyuchovi-dumi/`: confirm the route (`app/(bg)/saveti/[slug]` or similar) and that `depthOf` resolves relative links at depth 2; the /saveti/ hub page (card = label + summary) is a separate page.
- `related` pages /seo-statii/, /seo-optimizacia/, /diagnostika/ must be published for the cards to render (ContentPageView filters unknown paths).
- `[[sources]]`: the human decides whether/how to show them (not rendered by ContentPage).
- No `Dictionary` type change needed.

## SELF-CHECK
| check | result |
|---|---|
| TOML parses | PASS |
| title ≤ 60 incl. " \| BizGrow", no em-dash | PASS (53) |
| meta 120–160, contains main term | PASS (145, „ключови думи“) |
| primary_keyword = keyword-map term | PASS („ключови думи“) |
| main term in title, H1, first 100 words (lead), one H2 | PASS (H2 #kakvo-sa-klyuchovi-dumi only) |
| [[sections]] ids = body blocks, same order | PASS |
| port strings verbatim in 05b (markers stripped) and in content md | PASS (0 mismatches) |
| em-dash / en-dash | PASS (0 / 0) |
| bracketed markers | PASS (0) |
| „ти“ forms; lowercase ви/вас/ваш | PASS (0; 0) |
| „доклад“; delivery periods | PASS (0; 0). Only duration: 30-минутен разговор |
| banned claims / hype / prices / testimonials | PASS (Gate 11/11; no numbers except the canon 30 min and the sourced "three months") |
| example label | PASS (#primer label present) |
| inventory L1 /seo-statii/, L2 /seo-optimizacia/, L3 /diagnostika/ | PASS |
| booking CTA max 1 | PASS (1, #pomosht) |
| links only from conversion-links.md | PASS |
| sibling main terms not targeted/anchored („seo копирайтинг“, „seo оптимизация“) | PASS (0 occurrences) |
| article rules: 8 question H2s, 6 FAQ, soft closing, summary ≤160, no service, related 3 | PASS (summary 124) |
| body words | 937 in sections (977 with lead), within 900–1,400 |

new facts: 3
owner items added: 7
