# 07 — Gemini Step-7 check — pass 2 (after humaniser pass 1)

Normalized human-likeness: **25** (verdict "Shows AI patterns, 75% confidence" → 100 − 75).
Result: still below 80. Noisy/adversarial detector — it now flags passages it praised in pass 1
and admits several flags are "borderline" / "effective copywriting". Same relocating-flags pattern
seen on sibling card-game guides (santase, kanasta). Will apply the legitimate recs in humaniser
pass 2, then keep-best.

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 75% confidence.**

This article is highly polished, factually dense, and avoids the most egregious AI clichés (like "В днешния дигитален свят" or "Нека се потопим"). The Bulgarian is grammatically excellent. However, it exhibits several structural and tonal hallmarks of an LLM—specifically, the tendency to end paragraphs with dramatic, philosophical summaries, the use of formulaic signposting, and a slightly preachy, didactic tone when discussing strategy and budgeting.

### 1. The "AI Bow" (Philosophical/Dramatic Summarization)
- Flagged: "Тук се изчерпва цялата ви свобода на действие." (opening the fold/call section).
- Flagged: "Същественото е, че стратегията ограничава щетата, но не сменя посоката." (after optimal strategy).
- Recommendation: Delete these sentences; move straight to the next point.

### 2. Formulaic Signposting ("It is worth noting" translation)
- Flagged: "Струва си да се каже направо: карибският покер не е източник на доход..."
- Recommendation: Cut the filler; start directly with the factual statement.

### 3. The "Variance Disclaimer" Template
- Flagged: "Една вечер може да свърши на плюс, друга на минус, но колкото повече ръце играете, толкова по-близо реалният резултат клони към тази загуба."
- Recommendation: Reads like a textbook house-edge explainer; make it more conversational / practical.

### 4. Unprompted Moralizing / Embedded RG Language (Process Issue)
- Flagged: "...по-близо до лотариен билет... когато си правите бюджета." and "Разумното правило... не след третата ръка."
- Recommendation / Process Note: Per your hard rules, DO NOT remove this language (RG markers). Process note only: RG advice leaked into gameplay sections.

### 5. Staccato Rhythm in Introductions (Rule of Three)
- Flagged: "Няма наддаване помежду играчите, няма карти на масата, които всички да ползват, и няма начин да изблъфирате по-силна ръка."
- Recommendation: Borderline (effective copywriting). Vary so it doesn't rely on three consecutive "няма" clauses.
