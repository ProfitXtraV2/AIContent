# log.md · vk-0016 · Кено: правила, изплащания и реални шансове

- Brief (00): built from 00-brief-template. Guide, editorial voice, signature Георги Тодоров. Web research done: Wizard of Odds, Wikipedia, Techopedia (game-education). House-edge ranges + odds captured; anti-cannibalization confirmed (no keno page in sitemap). No number changes.
- Stage 1 Synthesis (01): report + original BG draft + suggested persona (Editorial). Ranges/odds set as facts; 1 [VERIFY] (pick-6 range), small-catch odds flagged approximate. No [CONFLICT].
- Stage 1.5 Outline (01.5): H1 + 6 sections, deliberately varied shapes (narrative build / short blunt / worked-numeric / analytical / opinionated close). Editorial mode = no signature slots. 3 approved links assigned. 2 [VERIFY] flags carried forward.
- Stage 2 Author (02): editorial prose, 1021 words (in 1000–1500 range after one expansion pass; first pass 736 → expanded with real substance, not padding). Zero em-dashes in body. Both [VERIFY] flags in text. NUMBER DIFF vs brief: consistent.
- Stage 3 Humaniser (03): Phase 1 verdict HUMAN-LIKE 50/60 (≥48) → no rewrite; article carried forward verbatim. NUMBER DIFF 02→03: identical (verified programmatically, multiset match).
- Stage 4 SEO (04): audit 92/100. De-flooded one H2 (кено in 4 headings → 3). Added title (42 chars) + meta (142 chars), both zero em-dashes, „кено" front-loaded. 3 approved links kept, none added/invented. NUMBER DIFF 03→04: identical.
- Stage 5 Brand Gate (05): PASS WITH FIXES → PASS, 95/100 (Personality 19 | Tone 14 | E-E-A-T 18 | Trust 15 | Language&Style 14 | RG 15). Fix applied: filled 3 trust-slot placeholders with byline+dates, About boilerplate, verbatim RG footer, verbatim affiliate-licensing footer. Recalcs checked. Flags left in text. NUMBER DIFF 04→05 body: identical.
- Stage 5b Humaniser light (05b): scanned em-dashes / signposting / banned connectives / over-polished tables / excessive bullets — none present. Article unchanged from gate output. Final file in required Title/Meta/H1/body/footer format. NUMBER DIFF 05→05b article: identical.
- Verification (06): 2 surviving [VERIFY] flags; claims-to-confirm + illustrative-numbers tables; pick-10 recalculation shown; compliance spot-check (zero em-dashes); anti-cannibalization note; human-action list.

═══════════════════════════════════════════
## FINAL GREP-VERIFICATION BLOCK
═══════════════════════════════════════════
- Em-dashes (—) in 05b (whole file incl. title/meta/footers): 0 ✓
- Number multisets identical across 02 / 03 / 04 / 05 / 05b bodies: TRUE ✓
- Preserved figures (all stages): ranges 4% / 35% / 50% / 80% / 20% / 40% / 84% / 95% / 96% / 5% / 60%–95%; odds 1 на 8,9 милиона, 1 на 3,5 квинтилиона, 1 на 80, 20 от 80; small-catch 1 на 4 / 17 / 73; € examples €1, €100, €96; множители 1 000 / 2 000; picks 4/5/6/8/10/15/20 ✓
- Recalculation: C(20,10)/C(80,10) = 1 / 8,911,711 → „около 1 на 8,9 милиона" ✓
- Byline „Георги Тодоров": present ✓ · Brand „Всички Казина": exact, no transliteration ✓
- Dates 08.09.2026 (публикувано + последна редакция): present ✓
- Verbatim 18+ line inline in body AND in RG footer: present ✓
- RG signposting /otgovorna-igra/ + регистър на уязвимите лица (НАП): present ✓
- Verbatim affiliate-licensing footer (1 Aug 2026, ДВ бр. 69 от 31.07.2026): present, „подало заявление … очаква издаването му" (no issued-licence claim) ✓
- Internal links (approved set): /kazino-igri/, /kak-ocenyavame/, /otgovorna-igra/ = 3 distinct in body ✓
- кено in headings: 3 (H1 + „Как се играе кено" + „Струва ли си да играеш кено") ✓
- Banned AI connectives / promise / hype words: 0 ✓
- Surviving in-text flags: 2 [VERIFY] (left in text, not resolved) ✓
- Body word count: 1021 (target 1000–1500) ✓
- Anti-cannibalization: no keno page in sitemap ✓

## Step 6/7 (orchestrator, post-writer)
- Post-writer cleanup: removed a stray Stage-5b process note that had leaked as line 1 of 05b (file now starts with `Title tag:`); reverted the writer-filled About block back to the literal `[About Всички Казина boilerplate]` placeholder (human owns the boilerplate at Step 8).
- Step 6 prep: 06-verification.md updated (2 in-text [VERIFY] flags; odds/house-edge confirm-list with source URLs; illustrative-numbers table; pick-10 catch-all recalc = 1/8,911,711 → „около 1 на 8,9 милиона"; untouchables spot-check; anti-cannibalization; Step-7 result; human-action list).
- Step 7 (Gemini, gemini-3.1-pro-preview): check 1 initial "Likely AI-written 85%" → hl 15; Humaniser pass 1 (fixed „casino floor" calque „на пода/целия под" → native BG, removed 2 signposting lead-ins, de-dramatized 2 wrap-ups, broke the seesaw conclusion) → check 2 "Shows AI patterns 80%" → hl 20; Humaniser pass 2 (broke „Улучиш три/пет/осемте" rule-of-three + „и двата…и двата" repetition, fixed meta anglicism „Кено на прости думи", deleted „За перспектива", cut fluff transition) → check 3 "Shows AI patterns 85%" → hl 15. MAX_GEMINI_PASSES=2 reached; kept HIGHEST hl = pass 1 (20); 05b reverted to the pass-1 commit. content-queue gemini = ai 80. Rejected Gemini's request to remove the RG doctrine „Хазартът не е финансова стратегия" (untouchable); kept both [VERIFY] flags. All numbers/links/RG/18+/dates/byline/brand preserved; no flag resolved; not posted, not merged. 07-gemini-check-1/-2/-3.md persisted.
- Status → drafted. drafted_date 08.09.2026. Human owns Step 6 (resolve the 2 [VERIFY] odds/paytable figures) + publish.
