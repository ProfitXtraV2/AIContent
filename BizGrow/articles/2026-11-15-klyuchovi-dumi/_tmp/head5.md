# 05-gate-report · /saveti/klyuchovi-dumi/ (Step 5, Brand Gate)

Page: /saveti/klyuchovi-dumi/ | Locale: bg | Type: new-page (advice article) | Main term: ключови думи
Inputs read: 04-seo.md, 00-brief.md, 00-inventory.md, 00-current.md, pipeline/markets/bg/author.md (BIZGROW CANON, DE-AI RULES, AI-TELL DICTIONARY), pipeline/reference/site-rules.md, pipeline/reference/verification-policy.md, keyword-map.md, conversion-links.md.
Mechanical checks: _tmp/gate5.py (lengths, word count, H2/FAQ counts, banned terms, „ти“ forms, digits, main-term hits).

```
BRAND COMPLIANCE SCORECARD — /saveti/klyuchovi-dumi/ (bg)
Verdict: PASS
Total: 92/100
Voice 18/20 | Language 13/15 | Trust & claims 19/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 14/15

BLOCKING CHECKS
1. NOTHING LOST — PASS. New page; every 00-inventory.md item present: L1 /seo-statii/ („статии и текстове за Вашия бранш и град“), L2 /seo-optimizacia/ („оптимизацията на отделните страници“), L3 /diagnostika/ („безплатната диагностика“), C1 one booking CTA in #pomosht, C2 {{EMAIL}} optional/unused, canon closing facts, example label in #primer.
2. FACTS ALLOWED LIST — PASS. BizGrow statements: own content tool writes articles for the client's industry and city; publication only after approval; free diagnosis shows where the business loses time; 30-minute call; „оферта с приоритизирани решения и ясни еднократни цени“; diagnosis commits to nothing. All canon. No vendor, team, years, clients, price, phone or address.
3. BANNED CLAIMS — PASS. 0 guarantee/гарант*, 0 №1/лидер/най-добр*, 0 hype words, 0 prices/promo/testimonials; „безплатн*“ 2× and both about the diagnosis.
4. NUMBERS — PASS. Figures: step numbers 1–3; „30-минутен разговор“ (canon, the only duration); „последните три месеца“ (Search Console default window, external fact under [VERIFY] src 2, not a delivery period). Delivery periods („48 часа“, „до 2 седмици“, „за дни“): 0. „доклад“: 0; „оферта“ used. Sourced facts: 3 ([VERIFY] autocomplete, Performance report, spam policies) = cap; FAQ 4 reuses src 3.
5. HYPOTHETICAL LABEL — PASS. #primer P1: „Примерът е хипотетичен, не е от конкретен клиент и в него няма брой търсения.“ + [OWNER CONFIRM] kept. Other examples (clinic wording, „фризьор за къдрава коса в Пловдив“, „химическо чистене Варна“) are generic search-phrase illustrations, not business scenarios or results.
6. GDPR WORDING — N/A (GDPR not mentioned).
7. REGISTER — PASS. 0 „ти“ forms (only hits for „те“ are the 3rd-person plural „they“: „обикновено те знаят“, „те често са“); 0 lowercase вие/ви/вас/ваш in direct address; formal imperatives throughout (Записвайте, Започнете, Изберете, Пишете, Избягвайте, Запазете).
8. CTA RULES — PASS. 1× [Запазете безплатна диагностика]({{BOOKING_URL}}) (approved wording) in #pomosht; no hard-coded URL/email; no urgency.
9. ONE TERM PER PAGE — PASS. Main term = keyword-map row „ключови думи“. Placement: title 1, H1 1, first 100 words 1 (lead S1), H2 1 (#kakvo-sa-klyuchovi-dumi); the other 7 H2s use „основна дума“. Sibling main terms „seo копирайтинг“ 0, „seo оптимизация“ 0 (not targeted, not anchors), „копирайтър“ 0, „бизнес профил в гугъл“ 0, „изработка на сайт“ 0, „реклама в гугъл“ 0.
10. LINKS & ANCHORS — PASS. Body links /seo-statii/, /seo-optimizacia/, /diagnostika/ all in conversion-links.md; related = exactly those 3 paths; no EN pair.
11. BIZGROW VOICE — PASS. No fragment paragraphs, no rhetorical questions in body (question H2s are allowed by the article format), no exclamation marks, no slang or hype; jargon explained on first use (title, H1, meta description, Search Console, keyword stuffing).

RUN-SPECIFIC CHECKS
- Advice article: 8 question-led H2s (6–8) ✓ | body 947 words (900–1,400; H2s, flags, page fields and FAQ excluded) ✓ | FAQ 6 (4–6) ✓ | one soft closing section #pomosht ✓ | max one booking CTA (1) ✓ | eyebrow „Съвети“ ✓ | label „Ключови думи“ (short) ✓ | summary 124 chars (≤160) ✓ | no service key ✓ | related = /seo-statii/, /seo-optimizacia/, /diagnostika/ (3, from conversion-links.md) ✓
- title 53 chars incl. " | BizGrow" (≤60), no em-dash ✓ | meta description 145 chars (120–160), contains main term ✓
- Canon 2026-11-15: „оферта“ ✓, „доклад“ 0 ✓, delivery periods 0 ✓, only the 30-minute call carries a duration ✓
- Port shape: #kakvo-sa P | #kak-da-otkriete P → steps(3) → closing | #edna-osnovna-duma P(2) → bullets(3) | #namerenie P(3) | #primer P → bullets(4) → closing | #kade-v-teksta P → bullets(5) → closing | #greshki P(3) → bullets(5) | #pomosht P(2) → closing(CTA). Max one steps list and one bullets list per section ✓. Inline only **bold** and [label](path) ✓ (flags are pipeline markers, stripped at port). No tables/H3/images/quotes ✓
- No tool vendors named as recommendations (Ahrefs/Semrush/Ranktracker/Keyword Planner 0; only Google's own autocomplete and Search Console as sourced general facts) ✓
- Em-dashes 0, en-dashes 0 ✓

CRITICAL (blocks): none.

MODERATE (non-blocking; page left as is, optional for the human at port):
- #kak-da-otkriete P1 „Много собственици питат как се откриват ключови думи без платени програми.“ is a soft unsourced observation (it carries the secondary term „как се откриват ключови думи“). Optional rewording that keeps the term: „Ако се питате как се откриват ключови думи без платени програми, започнете от източниците, които вече имате…“.
- FAQ 2 S2 „Основната дума на всяка страница е различна от думите на останалите страници на сайта.“ reads as a description; clearer as advice: „Основната дума на всяка страница трябва да е различна от основните думи на останалите страници.“
- #namerenie P3 „Намерението се проверява лесно:“ leans toward a signpost lead-in; acceptable, could be „За да проверите намерението, потърсете думата в Google…“.
- FAQ 3 restates the Search Console fact without its own [VERIFY] marker; covered by src 2 in #kak-da-otkriete (same fact, no new claim).

OWNER ITEMS TO RAISE (for Step 6):
1. [OWNER CONFIRM] new hypothetical example in #primer (fictional pastry shop in Plovdiv, keywords per page, no numbers): keep?
2. [VERIFY] ×3 external Google facts to confirm and move to [[sources]]: autocomplete reflects real searches (support.google.com/websearch/answer/7368877); Search Console Performance report metrics, query grouping, default 3-month window (support.google.com/webmasters/answer/7576553); keyword stuffing definition and examples (developers.google.com/search/docs/essentials/spam-policies).
3. Coverage gap by design: the meta keywords question (buyer question) and Keyword Planner were left out under the 3-source cap; owner may approve a 4th source in a later run (SEO Starter Guide: "Google Search doesn't use the keywords meta tag").
4. Pipeline housekeeping (not a page defect): pipeline/markets/bg/author.md BIZGROW CANON › PRICES still says the one-off price is „given in the report after the free diagnosis“; it should read „offer“ to match the 2026-11-15 canon change. Shared file, not edited by this stage.

VOICE NOTES (protect during port):
- Formal, calm, practical tone; short concrete examples in owners' words („зъбен имплант“ vs „дентална имплантология“).
- Keep „основна дума“ in the non-main H2s (main-term de-flooding from Step 4).
- Keep the closing exactly as canon: free diagnosis → 30-минутен разговор → оферта с ясни еднократни цени → no obligation.
```

Fixes applied in this stage: none (verdict PASS, zero criticals). The page below is 04-seo.md's page verbatim.

---

# PAGE (gate-approved draft, owner approval pending)

