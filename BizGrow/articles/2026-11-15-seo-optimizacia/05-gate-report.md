# 05 — Brand Gate report — /seo-optimizacia/ (bg)

Stage 5, fresh context, 2026-11-15. Inputs: 04-seo.md, 00-brief.md, 00-inventory.md, 00-current.md;
rules: agents/brand-gate-bizgrow.md, prompts/step-5-brand-gate.md, markets/bg/author.md (canon),
reference/site-rules.md, reference/verification-policy.md, keyword-map.md, conversion-links.md.
Mode for this run (orchestrator instruction): EVALUATE ONLY. The page is not edited here; the page of
record for Step 5b is the OPTIMISED PAGE BODY + title/meta/FAQ in `04-seo.md`, unchanged.

```
BRAND COMPLIANCE SCORECARD — /seo-optimizacia/ (bg)
Verdict: PASS
Total: 88/100
Voice 18/20 | Language 14/15 | Trust & claims 16/20 | Usefulness 14/15 | Anti-AI 13/15 | SEO 13/15
```

## BLOCKING CHECKS

| # | check | result | notes |
|---|---|---|---|
| 1 | Nothing lost (inventory R1–R8) | PASS | New page, no current copy. R1 lead + #kakvo-e + 3 H2s + FAQ 1; R2 /seo-statii/ in #on-page + FAQ 6; R3 `[Запазете безплатна диагностика]({{BOOKING_URL}})` in #cena + /diagnostika/ in #kak-rabotim; R4 all four canon steps, „обикновено“ kept; R5 #cena + FAQ 4, no number; R6 „Цените са прозрачни и не изискваме дългосрочни договори … Работим по GDPR.“; R7 #ochakvania + FAQ 2 + FAQ 3; R8 8 H2 + 8 FAQ. |
| 2 | Facts allowed list | PASS (with flags) | Service = canon item 5 (техническо SEO, on-page, връзки); content tool, client approval, product-collection descriptions, sectors, process, policies all canon. Every statement of BizGrow practice beyond canon carries an inline `[OWNER CONFIRM]` (O1 technical tasks, O2 on-page tasks, O3 link practice, O4 2-week build for SEO, O5 diagnosis covers SEO, O7 support pricing). No tool, vendor, team, years, count, office, phone, legal data or price. See M1 for the Step 6 consequence. |
| 3 | Banned claims | PASS | grep: 0 гарантир*/гаранци*, 0 първо място/топ позиции/№1/лидер/най-добр*, 0 hype words, 0 prices/offers/testimonials, 0 urgency. „безплатн*“ 8x, all „(безплатна/безплатната) диагностика“. „най-горното място“ appears only inside the no-promise statement and Google's sourced advice (required by R7). |
| 4 | Numbers | PASS | Only canon figures: 30-минутен, 48 часа, обикновено до 2 седмици; „четири стъпки“ / „три части“ count canon items. New sourced facts: 3 (F1 Google's list of SEO tasks, F2 avoid an SEO promising first place [used twice], F3 bought/sold links = link spam), each `[VERIFY: … — URL]`; max 3 respected. |
| 5 | Hypothetical label | N/A | No example scenarios or before/after rows. |
| 6 | GDPR wording | PASS | „Работим по GDPR.“ only. |
| 7 | Register | PASS | 0 „ти“ forms (body, headings, FAQ, title, meta, CTA); 0 lowercase вие/ви/вас/ваш in direct address. |
| 8 | CTA rules | PASS | One booking CTA (#cena), approved wording, `{{BOOKING_URL}}`; email only `{{EMAIL}}`; no hard-coded URL/address; no urgency. Template's own „Запазете час“ / „Безплатна диагностика“ buttons sit under the lead, not in a section. |
| 9 | One term per page | PASS | „seo оптимизация“ once each in title, H1 („SEO оптимизация на сайтове“), lead sentence 1, one H2 (#kakvo-e). No sibling main term in title/H1/H2. „SEO статии“ / „описания на продукти“ (/seo-statii/ terms) and „реклама в Google“ (/reklama/ term) occur only as passing mentions next to the link to the owning page. „локално SEO“ / „SEO одит“: 0. |
| 10 | Links & anchors | PASS | /seo-statii/ (x2), /diagnostika/, /reklama/: all in conversion-links.md. No parked addresses. 8 new section ids, short latin kebab-case. No EN pair. |
| 11 | BizGrow voice | PASS | No exclamation marks, no rhetorical questions in body, no slang, no hype. Minor voice items under MODERATE (not blocking). |

Brief-specific checks: 6–8 H2 (8) + 6–8 FAQ (8) PASS · link to /seo-statii/ PASS · no ranking
guarantee PASS · canon item 5 only, nothing more specific stated as unflagged BizGrow fact PASS (see M1/M2) ·
max 3 new sourced facts PASS (3) · no prices/numbers beyond canon PASS · no sibling or parked-page
term targeted PASS. Title 53 chars, meta 156 chars (python3 len), no em-dash, main term once each. Em-dashes
in page text: 0 (the only „—“ are inside `[VERIFY: … — URL]` markers, removed at Step 6).

## CRITICAL (blocks)

None.

## MODERATE (non-blocking; fix before the content file)

| id | quote | rule | fix | stage |
|---|---|---|---|---|
| M1 | #vrazki „Работата по връзките се води според правилата на Google.“; #on-page „Всяка страница се подрежда около изразите, с които клиентите търсят…“; #kak-rabotim step 1 „…и сайта Ви.“ | Check 2 / verification-policy: in the final file „the text says only what is known“. These are BizGrow-practice claims beyond canon item 5, held only by O2/O3/O5. | Step 6 must write each [[owner_items]] entry AND, unless the owner has confirmed, reduce the sentence to canon/general wording (e.g. describe Google's rule as a fact about Google, not as BizGrow's practice). Never ship them as confirmed fact. | Step 6 |
| M2 | #za-kogo „При SEO оптимизацията на онлайн магазин основната работа е по продуктовите страници и категориите.“ | Check 2 (soft): reads as BizGrow method, not flagged. | Either frame as general („обикновено основната работа е…“) or add to O2 as an owner item. Fact wording, so not 5b. | Step 6 (owner item) / orchestrator |
| M3 | #ochakvania „Ако имате нужда от посещения още сега, повече ще намерите на страницата за реклама…“ | Check 3 spirit (implied traffic outcome of a sibling service). | Neutral wording, e.g. „Ако искате сайтът да се показва и чрез платени обяви, повече за това ще намерите на страницата за [реклама в Google и Facebook](/reklama/).“ | Step 5b (wording; link/anchor unchanged) |
| M4 | FAQ 3 „Сроковете, които спазваме, са за самата работа…“ | Check 4 / canon (response-time promise beyond canon; canon says „обикновено“). | „Сроковете, които посочваме, са за самата работа…“. | Step 5b |
| M5 | #kakvo-e „технически съвети за хостинг … използване на JavaScript“ | Voice: unexplained jargon. | Brief gloss inside the sourced sentence, e.g. „хостинг (сървърът, на който е сайтът)“; do not change the sourced meaning. | Step 5b |
| M6 | #ochakvania „Можете да използвате този съвет при избора на SEO експерт или SEO агенция.“ | Pillar 6 / voice: inserted-keyword feel. | Keep the secondaries only if the sentence reads naturally, e.g. „Този съвет е полезен при избора на SEO експерт или агенция.“ | Step 5b |
| M7 | #tehnichesko-seo „Когато собственик пита защо сайтът му не излиза в Google, една от честите причини е техническа.“ | Voice/logic (cause tied to the asking; „честите“ is an unsourced generalisation). | „Ако сайтът не се показва в Google, една от възможните причини е техническа.“ | Step 5b |
| M8 | #kakvo-e „Целта е сайтът да отговаря ясно на въпросите…“ + #za-kogo „Работата цели сайтът да отговаря ясно на тези търсения…“; „Самият Google“ x2 (#ochakvania, FAQ 2) | Anti-AI: repeated sentence frame; emphasis crutch. | Vary one of the two „отговаря ясно“ sentences; drop „Самият“ in one place. | Step 5b |
| M9 | Lead „on-page оптимизация на страниците“ before #on-page explains it | Jargon on first use. | Optional: „on-page оптимизация (работа по текста и заглавията на самите страници)“ in the lead, or accept since #on-page explains it two sections later. | Step 5b (optional) |
| M10 | Step 5b input | Pipeline note | This gate did not produce a corrected article; Step 5b must take the OPTIMISED PAGE BODY + title/meta/FAQ from `04-seo.md`. | Orchestrator |

## OWNER ITEMS TO RAISE (for Step 6)

1. O1 — Which technical SEO tasks BizGrow performs (#tehnichesko-seo list describes the field in general; canon says only „техническо SEO“).
2. O2 — Which on-page tasks BizGrow performs (titles, meta descriptions, headings, keyword research, internal links); include M2 (online shop: product and category pages).
3. O3 — How BizGrow works on links (which sources; confirmation that no links are bought).
4. O4 — Whether „обикновено до 2 седмици“ applies to SEO fixes, including link work (#kak-rabotim step 3, FAQ 3).
5. O5 — Whether the free diagnosis and the 30-minute call cover the website's SEO state (the /diagnostika/ checker is about hours lost per week).
6. O6 — Access and ownership after the work (site, Google accounts, data access); buyer question left open on the page.
7. O7 — How monthly support is priced and contracted (FAQ 8).
8. F1–F3 — Three Google Search Central facts (do-i-need-seo x2 uses, spam-policies) to be fetched, quoted and listed in [[sources]] at Step 6; owner confirms by reading.
9. New page as a whole: canon item 5 was added on 2026-11-15 („full SEO too“); the owner approves the page, title „SEO оптимизация на сайтове за малки бизнеси | BizGrow“, H1, label/summary/eyebrow and `service` „SEO оптимизация“.
10. Home services card: the current card „SEO копирайтинг“ belongs to /seo-statii/; a home-page rewrite should add a card for /seo-optimizacia/ (site-rules §5).

## VOICE NOTES (protect during fixes)

- Keep the calm no-promise block in #ochakvania and FAQ 2–3; it is the page's main trust asset and satisfies R7.
- Keep the plain-word glosses (обхождане/индексиране, пренасочвания (redirects), връзките (линковете), ключови думи, B2B).
- Keep „Подредбата на резултатите я определя Google.“ (correct clitic doubling) and the formal „Вие“ capitalisation.
- Do not add tools, timelines, link counts or examples while fixing.
