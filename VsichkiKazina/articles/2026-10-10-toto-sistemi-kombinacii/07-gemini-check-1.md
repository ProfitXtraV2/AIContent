# Step 7 — Gemini cross-model check — PASS 1 (initial 05b)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-10 (cloud reconcile of HANDOFF row)

## Verdict (verbatim)

→ Normalized HUMAN-LIKENESS = **90**  (PASS threshold = 80) — PASS

---

Here is my evaluation of the article from the perspective of a senior copywriter and AI-text detection specialist.

### **Verdict: Likely human-written (or heavily, expertly human-edited), 90% confidence.**

This is an exceptionally strong piece of copy. It avoids almost all the classic LLM traps: there is no fluffy introduction ("В днешно време лотарията..."), no generic conclusion ("В заключение..."), and no moralizing filler. 

The strongest indicators of human authorship are the punchy, non-standard syntax and conversational logic. Phrases like **"На фиш, да. На евро, не."** and **"Коя е най-добрата система за Тото 2? Няма такава."** are highly uncharacteristic of AI, which typically hedges its answers with "Въпреки че..." (Although...) or "Зависи от..." (It depends...). Furthermore, explaining the math via human intuition (*"Да изберете 6 от 8 е същото като да решите кои 2 остават извън шестицата"*) is a classic human copywriting technique that AI rarely executes unprompted.

However, because the text is highly structured and mathematically dense, there are a few specific passages that might trigger false positives in AI detectors or read slightly like a textbook. 

Here are the specific patterns flagged and how to smooth them out.

---

### **Flagged Passages, Patterns, and Recommendations**

#### **1. Pattern: The "Wall of Math" (Dense Statistical Block)**
> **Flagged text:** *"В 6/49 се печели с 6, 5, 4 или 3 познати числа. За една комбинация шестицата е 1 към 13 983 816. Пет познати числа дават 258 комбинации, ≈ 1 към 54 201, четири числа 13 545 комбинации (≈ 1 към 1 032), а три числа 246 820 комбинации, или ≈ 1 към 57. Поне 3 числа излизат с шанс ≈ 1 към 54."*

*   **Why it triggers AI detection:** LLMs love to output dense, unbroken paragraphs of statistics when asked to explain probabilities. Visually and rhythmically, this reads like a machine-generated data dump. It lacks breathing room.
*   **Recommendation:** Break this paragraph into a bulleted list. Keep the exact numbers and odds, but format them so the reader's eye can scan them. For example, introduce the concept ("В 6/49 се печели с 6, 5, 4 или 3 познати числа, като шансовете за една комбинация са:"), and then list the odds for 6, 5, 4, and 3 numbers as separate bullet points. 

#### **2. Pattern: Didactic / Textbook Transitions**
> **Flagged text:** *"Очакваната стойност следва същата логика. В даден тираж всички комбинации имат еднаква очаквана стойност, а системата е пакет от такива комбинации, затова и очакваната стойност на евро остава непроменена."*

*   **Why it triggers AI detection:** "X follows the same logic" is a very common LLM transitional phrase used to bridge two technical concepts. It sounds slightly academic and robotic compared to the punchy tone established earlier in the article.
*   **Recommendation:** Soften the transition to make it more conversational. Instead of stating that it "follows the same logic," suggest rephrasing to directly connect the mathematical concept of expected value to the player's wallet (e.g., framing it around the idea that buying in bulk doesn't change the mathematical return on investment). 

#### **3. Pattern: Academic Summary / Over-formal Conclusion**
> **Flagged text:** *"Средният резултат е същият, разпределението около него е различно, и това е дисперсията."*

*   **Why it triggers AI detection:** AI often ends explanatory paragraphs by summarizing the preceding sentences with a formal academic term (in this case, defining "variance" / "дисперсия"). It feels a bit like a Wikipedia entry suddenly dropped into a consumer guide.
*   **Recommendation:** You can keep the word "дисперсията", but suggest blending it more naturally into the sentence rather than using it as a definitive concluding clause. For example, frame it as the reason *why* players experience the game differently (the "boom or bust" nature of systems), rather than just stating "and this is variance."

---

### **Process Note on Editorial Flags**
I noted several `[VERIFY: ...]` tags remaining in the text (e.g., `[VERIFY: текущи цени за една комбинация...]`, `[VERIFY: максимален размер на система...]`). 

As per your hard rules, **I have not touched or removed these, nor have I altered any of the responsible gambling language or 18+ markers.** However, from a purely operational standpoint, the presence of bracketed editorial tags in a "finished" article indicates a gap in the final pre-publishing review process. These should be resolved by your fact-checking team before the piece goes live.
