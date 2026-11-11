# log — / (home), 2026-11-11

## Authorisation
- The brand is PAUSED (SKILL.md banner, 2026-11-11). The owner asked on 2026-11-11 to restructure the ELLE home page and to have all site text go through ContentAI. This run is a **one-off manual run for `home` only**, relayed by the owner's session. The PAUSED banners, backlog statuses, dashboard config and routines were NOT edited. The brand stays paused for every other page.

## Step 0 — brief
- Deviation (owner instruction): 00-current.md is the newest home text, the UNCOMMITTED local file `WebPortals/ElleDental/_publisher/content/home.md` on branch feature/elledental-original-look (base commit 1737a44), not the committed file on feature/elledental-site/main. Used verbatim.
- Publisher rule files re-read from the same `_publisher/` folder. Difference vs reference/site-rules.md: local build_site.py adds the `<!-- more -->` body split. No other differences.
- Patient questions: one web search (standard). Ahrefs metrics from topic-backlog.md row 9.
- Superdoc rating: not on the current page → not used (brief makes it conditional).
- Principle 9: nothing written to WebPortals; the owner copies the deliverable.

## Step 1 — synthesis
- 01-synthesis.md written: two-part draft (3 sentences + 5 quick facts / `<!-- more -->` once / what-to-expect + address-hours-booking block), ≈270 body words incl. headings and tokens. 0 new medical facts, 0 CONFLICT, 0 DATA NEEDED; all 13 tokens, 9 must-survive links, W1-W8, N1 kept; 4 FAQs and CI1 verbatim; title/meta/h1 unchanged.
- Removed by brief: treatment list (19 links) and doctor bios. Flag: confirm the treatment cards link all 19 pages. Superdoc rating not used (not on the current page).

## Orchestrator check after step 1
- Inventory diff (mechanical script + read): clean. All 13 tokens, 9 must-survive links, 112 / no-emergency / duty-doctor wording, W4-W8, languages, location present; `<!-- more -->` once. Intentional removals: 19 treatment links + doctor bio facts (REMOVE-BY-BRIEF). CI1 referenced as kept (synthesis is a worksheet; verbatim check at step 6).
- Step-1 flag resolved: `_publisher/templates/home.html` treatment cards link all 19 removed treatment pages, so the home page loses no internal links.

## Step 1.5 — outline
- 01.5-outline.md written per owner brief (home type, §5 treatment H2s and urgent heading not applicable): Part 1 = opening paragraph (2-3 sentences) + 5 quick facts; `<!-- more -->` once; Part 2 = H2 „Какво да очаквате при посещение“ (W4-W7, /za-nas/) + H2 address/hours/booking (all tokens, W8, /kontakti/).
- Main term: first 100 words (P1a sentence 1) + H2-2 variant; title/H1/meta unchanged. 4 FAQs kept; every inventory item mapped, none homeless; no open flags.

## Step 2 — author (editorial)
- 02-draft.md written in ELLE VOICE: Part 1 = 2 sentences + 5 quick facts; `<!-- more -->` once, alone on its line; Part 2 = „Какво да очаквате при посещение“ (W4-W7, /za-nas/) + address/hours/booking block (all tokens, W8, /kontakti/). Body 269 words (wc, tokens as written).
- 13/13 tokens, 9 must-survive links, W1-W8, N1 kept; CI1 and title/meta/h1 verbatim; 4 FAQs kept (Q3 lightly reworded, Q4 emergency wording verbatim). 0 em-dashes, 0 banned terms, no open flags.

## Orchestrator inventory diff after step 2 (00-inventory vs 02-draft)
- Clean: 13/13 tokens, 9/9 must-survive links, W1-W8, N1 (112), CI1 verbatim, 4 FAQs, `<!-- more -->` once, 0 em-dashes in page text, 0 banned/offer terms. Intentional removals (REMOVE-BY-BRIEF): 19 treatment links, doctor bio facts N3-N5 and courses/interests/БЗС.

## Step 3 — professional-quality check
- Verdict NEEDS EDIT (Correctness 8, Clarity 7, Register 9, Readability 9, No AI tells 8); 03-humanised.md written. Edits are wording only: W6/W7 sentence split, native word order for W4, active form for W5, participle in Part 1 sentence 2, FAQ Q3 back to the current page's „Час се запазва…“ (it duplicated the booking sentence).
- Kept: 13/13 tokens, 9/9 links, W1-W8, N1, CI1 verbatim, Q4 verbatim, title/meta/h1, `<!-- more -->` once alone; Part 1 = 2 sentences + 5 quick facts; body 263 words; 0 em-dashes; no flags.

## Orchestrator inventory diff after step 3 (00-inventory vs 03-humanised)
- Clean: 13/13 tokens, 9/9 must-survive links, W1-W8 same meaning (W4/W5 reworded only), N1, CI1 verbatim, 4 FAQs, marker once, 0 em-dashes in page text (one in the report heading only), 0 banned terms. Intentional removals unchanged (19 treatment links, bio facts).

## Step 4 — SEO
- 04-seo.md written. Relevance 88/100; main term once each in title, H1, first 100 words and one H2 (variant). Title checked in the publisher: build_site.py renders `title` verbatim (no suffix); home follows the /za-nas/ and /kontakti/ pattern, 50 chars with „София“; meta 154 chars. Title/meta/H1 kept, no clinical item needed.
- No edits: page identical to 03-humanised (266 words, 13/13 tokens, 4 FAQs, CI1 verbatim, marker once, 0 em-dashes). No links or facts added; НЗОК question not answerable from canon (out of scope).

## Orchestrator inventory diff after step 4 (00-inventory vs 04-seo)
- Clean; body identical to 03 (no SEO text edits). Title/meta/h1 kept. Intentional removals unchanged.

## Step 5 — brand gate
- 05-gate-report.md written: PASS, 90/100 (voice 18, language 13, E-E-A-T 18, safety 15, anti-AI 13, SEO 13). Blocking checks 1, 4-7, 9-11 PASS; 2, 3, 8 N/A (home). 0 criticals; page not edited.
- Brief structure OK: marker once alone, Part 1 = 2 sentences + 5 quick facts, Part 2 = what-to-expect + one address/hours/booking block with /kontakti/, 264 body words. Only REMOVE-BY-BRIEF items removed; CI1 and front matter identical to current.
- Optional polish noted: „той обяснява“ (two female doctors) → repeat „лекарят“. No new clinical items.

## Step 5b — humaniser light re-check
- 05b-final-draft.md written from 04-seo.md (gate PASS). One edit: Part 2 „Преди всяка процедура той обяснява“ → „лекарят обяснява“ (gate's optional polish; both doctors are women). Nothing else applied: 0 em-dashes, no signposting, „не A, а B“ endings, register breaches or list issues found.
- Kept: title/meta/h1, CI1 verbatim, 13/13 tokens, all links, 4 FAQs (Q4 verbatim), `<!-- more -->` once alone; Part 1 = 2 sentences + 5 quick facts; body 267 words (wc after front matter). No flags.

## Orchestrator inventory diff after step 5b (00-inventory vs 05b-final-draft)
- Clean: one wording edit („той обяснява“ → „лекарят обяснява“); all must-survive items present; intentional removals unchanged.

## Step 6 — verification + content file
- content/home.md written: front matter byte-identical to 00-current.md (last_updated already 2026-11-11, CI1 verbatim, no review fields), body = 05b unchanged. No markers, so 0 new facts, 0 sources, 0 clinical items added.
- Self-check all PASS (TOML parsed with python3.14 tomllib; meta 154; 0 em-dashes/banned/price/offer/testimonial; 13/13 tokens; 9 links all approved; `<!-- more -->` once). Body 266 words. Title has no suffix (kept per step 4/brief). 06-verification.md lists the REMOVE-BY-BRIEF removals for the human.

## Orchestrator check after step 6 (00-inventory vs content/home.md)
- Inventory diff CLEAN. Front matter byte-identical to the current file (last_updated already 2026-11-11). 13/13 tokens, 9/9 must-survive links, W1-W8, 112, CI1 verbatim, 4 FAQs, `<!-- more -->` once, 0 em-dashes, 0 banned/offer terms. Body ≈ 263-267 words (counting method differs slightly by stage), inside the 250-400 target.
- Intentional removals (owner brief): 19 treatment links (/profilaktichni-pregledi/, /lechenie-na-karies/, /diagnostika-i-lechenie-na-gingivit-i-parodontit/, /zabni-koroni/, /zabni-mostove/, /protezi/, /pochistvane-na-zaben-kamak-i-polirane/, /silanti/, /lechenie-na-pulpiti/, /lechenie-na-peridontiti/, /dalboko-pochistvane-zakrit-i-otkrit-kjuretazh/, /poddarzhashta-terapija/, /bonding/, /faseti/, /izbelvane-na-zabi/, /ortodontsko-lechenie-s-alajneri/, /precizni-intervencii-s-minimalen-diskomfort/, /dermalni-filari/, /mezoterapija-i-biorevitalizacija/), all still linked from the home template's treatment cards; doctor bio paragraphs (2020, 2024 specialty, 5 years, БЗС, courses, interests), still in CI1 and on the doctor pages/cards.
- Attempted the publisher's test_content.py on a scratch copy (not WebPortals): could not run locally (tests deselected / `markdown` module not installed). The human runs check_site.py and the build in WebPortals as usual.

## Step 7 — Gemini check
- skipped: GEMINI_API_KEY exists only in the cloud environment.

## Step 8 — images
- none (page-rewrite).

## Process note
- Steps 1, 1.5, 2, 3, 4, 5, 5b, 6 each ran as a separate fresh-context subagent reading only its stage's agent file, prompt and inputs (principle 8). Gate: PASS (90/100) on the first run; no upstream fixes needed.
- STOP: the owner copies content/home.md into WebPortals (feature/elledental-original-look), runs check_site.py and the build; CI1 still needs both doctors' confirmation. Brand remains PAUSED.
