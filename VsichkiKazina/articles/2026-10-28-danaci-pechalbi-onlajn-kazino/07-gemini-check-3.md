# Step 7 — Gemini check, pass 3 (after humaniser pass 2) — danaci-pechalbi-onlajn-kazino

Run: 2026-10-28 · model gemini-3.1-pro-preview · file 05b-final-draft.md (after humaniser pass 2)
Normalized human-likeness = 100 − 75 = **25**.

KEEP-BEST DECISION (MAX_GEMINI_PASSES=2 reached): HL by version — initial 15, pass 1 15, **pass 2 = 25 (highest)**. Final 05b = humaniser pass 2, kept. Below the 80 target; detector runs noisy on BG YMYL legal/tax copy (documented pattern across this repo), facts locked to the ЗДДФЛ source pack, gate PASS 92/100, 3 [VERIFY] flags preserved. gemini column = `ai 75`. Logged for human review.

---
## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 75% confidence.**

While the article is grammatically flawless and adheres well to the YMYL (Your Money or Your Life) neutral editorial brief, it suffers from classic LLM structural tells. The text relies heavily on "concept looping" (repeating the same premise in slightly different words to pad the word count), formulaic transition sentences, and algorithmic over-hedging. 

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations.

### 1. Pattern: Concept Looping / Redundancy
AI models often struggle to state a simple fact once and move on. Instead, they rephrase the core premise multiple times across consecutive paragraphs. 

*   **Flagged Passages:**
    *   *(Intro)* "...не са облагаем доход за физическото лице..."
    *   *(Intro)* "Данък печалба от хазарт на практика зависи само от едно: от лиценза..."
    *   *(Intro)* "Спечелите ли от казино с редовен лиценз, върху печалбата не дължите данък..."
    *   *(H2)* "Освобождаването... стъпва изцяло на едно условие: организаторът да държи лиценз..."
    *   *(H2)* "Има ли такъв лиценз, печалбата на играча е необлагаема..."
*   **Recommendation:** Consolidate the introduction and the first H2 ("Защо данъкът върху печалба от хазарт зависи от лиценза"). State the legal rule (чл. 13, ал. 1, т. 20 ЗДДФЛ) and its implication once, clearly and concisely. Use the saved space to move directly into the practical advice (how to check the license) rather than hammering the same point five times.

### 2. Pattern: Formulaic Signposting / Artificial Transitions
LLMs frequently use standalone, highly mechanical sentences to bridge the gap between the introduction and the body paragraphs. 

*   **Flagged Passage:** 
    *   "Извън този масов случай има положения, в които отговорът вече е за счетоводител или за НАП."
*   **Recommendation:** Remove this sentence entirely. It adds no informational value and reads like a generated structural bridge. Let your subheadings (H2s) do the work of introducing the edge cases naturally.

### 3. Pattern: Algorithmic Over-Hedging
Because this is a YMYL topic (taxes), the AI has gone into overdrive with safety guardrails. It mechanically inserts a "consult a professional" disclaimer at the end of almost every single section.

*   **Flagged Passages:**
    *   "...се преценява със счетоводител."
    *   "Това е разговор със счетоводител за конкретната ви дейност."
    *   "Как се третира такава печалба, се изяснява с НАП."
    *   "За конкретна декларация потвърдете с НАП или със счетоводител."
*   **Recommendation:** You already have a strong, legally sound boilerplate disclaimer at the bottom of the article (*"Това не е данъчна консултация. За обвързващ отговор..."*). Rely on that. Strip out the repetitive inline referrals to accountants and NAP in the body text. It will make the text read much more like a confident editorial guide and less like a nervous AI.

### 4. Pattern: Process Issue (Prompt Leakage)
Internal editorial instructions and generation parameters have survived into the final text. 

*   **Flagged Passages:**
    *   `` `[VERIFY: конкретни AML прагове/задължения при входящ превод — извън source pack; дръж общо/хеджирано или насочи към банката]` ``
    *   `` `[VERIFY: третиране на хазартни загуби по ЗДДФЛ — извън source pack; дръж хеджирано или пропусни]` ``
    *   `` `[VERIFY: данъчно третиране на печалба от нелицензиран / извън-ЕС/ЕИП организатор — извън source pack; НИКОГА ставка/праг; насочи към НАП]` ``
    *   `` `[About boilerplate slot - Всички Казина]` ``
*   **Recommendation:** Per my instructions, I am not telling you to delete these. However, I must flag this as a critical workflow failure. These tags indicate that the writer/editor did not resolve the data gaps required by the brief before marking the article as "finished." The editorial team needs to address the specific queries inside these brackets and clear the tags before publication.
