# 05-GATE-REPORT — vk-0240 (Brand Gate: agents/brand-gate-vsichkikazina.md)

BRAND COMPLIANCE SCORECARD — Странични залози в казино игрите: струват ли си математически
Verdict: PASS WITH FIXES → fixes applied in 05b → PASS
Total (post-fix): 92/100
Personality 18/20 | Tone 14/15 | E-E-A-T 18/20 | Trust signals 15/15 | Language&Style 14/15 | RG 13/15  (sum 92)

CRITICAL (blocks publish): none.
 - Em-dashes in body/title/meta: 0 (grep clean). Promise/hype words: none. FOMO: none. Fabricated anecdote: none. Tax claim: none (nothing on winnings tax). Site-licence claim: only the verbatim "заявление подадено, очаква издаването" footer.
 - [DATA NEEDED]: none. Version A/B structure: none (task-brief range "2-11%" was resolved at synthesis into exact table+deck pairs).

MODERATE (fixed in 05b):
 1. „средното показва цената, не изхода" — paragraph-ending „не A, а B" antithesis (author.md confirmed-BG-finding #1) → removed; paragraph now stops on the fact.
 2. „Лично за мен: …" — unsupported first-person opinion (Pillar 5, pronoun audit) → rewritten as an objective statement („Ниска цена на масата имат само…").
 3. RG: budget not stated as „money you can lose entirely" → added „Парите за него трябва да са такива, които можете да загубите изцяло" (Pillar 6).
 4. SEO-stage artefact „(пише се и 21 плюс 3)" read as filler → removed.
 5. Meta description said „от 2,74% до 14,36%" while the table reaches 22,33% (Перфектна двойка, 2 тестета) → corrected to „от 2,74% до 22,33%".
 6. Earlier „звучат прилично, докато не видите…" shape (debunk template, humaniser stage) → already replaced by a plain statement before gate; confirmed absent.

TABLE CHECK (Pillar 5 over-polished tables): the 14-row table does genuine comparative work (3 games × deck counts × paytables), every row carries a stated paytable/deck assumption and a verified source → KEEP.
LIST CHECK: no bullet lists.
SHAPE CHECK: sections differ in shape (flowing analytical paragraphs / table+source note / short two-paragraph / worked-€ figures ending on a number / opinionated verdict). No signposting lead-ins, no „Именно/Точно" amplifiers, no counted prose („първо/второ"), no rhetorical-question openers, no „Звучи като… Само че". Ending is asymmetric (stance on what is cheap vs. what is a paid thrill).

MATH RECALC (every claim re-derived; Python exact enumeration in session, results match Wizard of Odds to 0.01 pp)
 - Перфектна двойка 25/12/6: n=52d cards; first card fixed, same rank other cards = 4d-1 → perfect d-1, coloured d, mixed 2d (over n-1). 6 decks: P=(5,6,12)/311; EV=(5×25+6×12+12×6)/311 − (1−23/311)=269/311−288/311=−19/311=−6.11%. ✓ 4 decks −10.14, 8 decks −4.10, 2 decks −22.33 ✓. Hit frequency 23/311=7.40% ✓; perfect pair 5/311=1.61% ✓.
 - 21+3 (всички печеливши ръце 9:1) exact 3-card enumeration: 1d −13.30, 2d −7.26, 6d −3.24, 8d −2.74 ✓ (4d 4,24 not used in text).
 - Бакара двойка: p=31/415=7.47%; EV=11p−(1−p)=−10.36% ✓; fair odds (1−p)/p=12.39 → „около 12,4" ✓. Tie: 8:1 with edge 14.36% → 9p−1=−0.1436 → p=9.52%; fair (1−p)/p=9.51 → „около 9,5" ✓. „над 90% от ръцете" (92.53% / 90.48%) ✓.
 - Worked €: 100×€10=€1 000 × 0.5% = €5.00 ✓; 100×€1=€100 ×6.11% = €6.11 ✓; ×10.14% = €10.14 ✓; 5.00+6.11 = €11.11 ✓; 6.11/11.11 = 55%(not stated); €100 / €1 100 = 9.09% → „около 9%" ✓. Banker 100×€10=€1 000 × 1.06% = €10.60 ✓; Tie 100×€1=€100 × 14.36% = €14.36 ✓.
 - „около дванайсет пъти": 6.11/0.5 = 12.2 ✓. „над пет пъти" : 2.74/0.5 = 5.48 ✓. „Стотината евро излизат по-скъпо от хилядата": €6.11 > €5.00 ✓.

NUMBER DIFF (across editing stages, logged): 02→03 only ADDED 1,61% / 5 от 311 (own-calc hit freq., verified) and „пет пъти"; 03→04 added meta-only numbers; 04→05b dropped only the temporarily removed image ALT numbers (restored in Step 8 from the same 05b figures). No changed or dropped figure.

VERIFY QUEUE (route to human): none surviving in text. Residual caveats (stated as plain caveats in text, not flags): paytables on any given operator table differ; blackjack ≈0.5% is rule-dependent (0.28-0.43% examples quoted).

VOICE NOTES (protected): dry, numbers-first; no anecdotes; no first-person claims.
Mandatory elements verified present: byline Георги Тодоров; brand „Всички Казина" exact; published + last-edited 02.10.2026; About slot; verbatim 18+ line (twice: pre-byline and in RG block); /otgovorna-igra/ + НАП регистър + „Солидарност" line; affiliate-disclosure footer verbatim (no affiliate links in body); internal links /kazino-igri/, /kak-ocenyavame/, /otgovorna-igra/ (3, all in approved set).
