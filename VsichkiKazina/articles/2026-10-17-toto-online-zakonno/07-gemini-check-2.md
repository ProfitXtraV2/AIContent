# Step 7 — Gemini cross-model check · PASS 2 (after humaniser pass 1 applying check-1 recs)

**Script:** `python3 scripts/gemini_check.py 05b-final-draft.md`
**Input version:** 05b after humaniser pass 1 (check-1 recs: removed summary/Накратко, signposting, filler transition, truism opener)

## Verdict (verbatim, normalized)
**"Likely AI-generated but heavily human-edited (or prompted with extreme specificity), 70% confidence."**
→ AI-patterns-type verdict at 70% → human-likeness = 100 − 70 = **30**

"This text is actually of very high quality. It features excellent, natural Bulgarian idioms ('няма да опрете до затворена врата', 'утре може да осъмне блокиран', 'сядате да играете')… However, the underlying structural scaffolding, the specific rhetorical devices used for emphasis, and the punctuation habits strongly point to an LLM given a highly detailed prompt, or a human relying on AI outlines."

## Flagged patterns + recs
1. „Не просто X, а Y" contrast — „Нелицензираните сайтове не са просто по-лошият вариант; играта там е нарушение…" → state the fact directly (this is confirmed BG tell #1).
2. „Цената е…" dramatic conclusion — „…цената е вашата защита и глоба от 500 до 2000 лв." → soften, advise directly (NOTE: this is the very sentence check-1 told us to MOVE here — whack-a-mole detector).
3. Colon-gluing of clauses — several („Разликата е изцяло правна:", „проверката отнема около минута:", „недостъпен за играчи:", „не е закана на хартия:") → replace ~half with full stops / conjunctions.
4. Robotic internal-link signposting — „Кои числови формати стоят зад отделните игри разглеждаме в материалите за…" → weave links into narrative.

## Keep-best ledger
- pass 0 (baseline post-5b): HL **35**
- pass 1 applied → pass 2 check: HL **30** (LOWER — noisy/adversarial detector relocated flags)
- Current best = pass 0 (HL 35).

## Decision
Score dropped despite legit edits (classic noisy-detector whack-a-mole on dry legal/procedural content, as documented on vk-0063/0264/0279/0282). Recs #1 (contrast) and #3 (colons) are genuine brand-dictionary de-AI improvements → apply a 2nd (final, MAX_GEMINI_PASSES=2) humaniser pass, then re-check and KEEP THE BEST version seen.
