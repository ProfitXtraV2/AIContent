# Step 7 — Gemini external check · pass 2

Model: gemini-3.1-pro-preview · Date: 2026-09-13
Verdict: Shows AI patterns, 65% confidence → human-likeness = 35
Result: improved from HL 25 (initial) → HL 35 (pass 1). Still < 80 → one more Humaniser pass (pass 2, the cap).

## Gemini verbatim verdict + recommendations

Here is my assessment of the article based on LLM writing patterns and AI text detection.

### **Verdict**
**Shows AI patterns (Hybrid/Heavily Edited), 65% confidence.** 
The article is actually quite good and avoids the most egregious AI tropes (there is no "В днешния дигитален свят" or "В заключение"). The mathematical explanations regarding RTP and volatility are highly accurate and read like expert human input. However, the structural "glue" holding the paragraphs together, the way lists are formatted, and certain repetitive phrasing strongly indicate an AI base draft that has been polished by a human, or a very strictly prompted LLM output.

---

### **Flagged Passages and AI Patterns**

**1. Circular Repetition / Stalling (The "Echo" Effect)**
*   **The Pattern:** AI often struggles to advance the narrative immediately after the introduction, opting instead to rephrase the intro's core premise and reuse the exact same examples in the first H2.
*   **The Quote:** 
    *   *In the Intro:* "При печалба от €0.20 и множител x100 на екрана излизат €20 (числата са примерни)."
    *   *In the first H2:* "...печалба от €0.20 става €0.40 при x2 и €20 при x100 (примерни), а разликата между двете е само коефициентът..."

**2. The "Squashed List" (Formulaic Enumeration)**
*   **The Pattern:** When asked to describe types or categories, AI often takes what should be a bulleted list and squashes it into a single, dense paragraph. To make it flow, it uses highly mechanical, robotic transitional glue to chain the items together.
*   **The Quote:** "Най-прекият коефициент умножава... **До него върви** символ-множителят... Прогресивният вариант не стои фиксиран... **докато** случайният пада без правило... **Остава** множителят в бонуса..."

**3. Translation Artifact / Awkward Collocation**
*   **The Pattern:** LLMs often translate English idioms or sentence structures directly into Bulgarian, resulting in grammatically correct but logically awkward phrasing where inanimate concepts perform actions they shouldn't.
*   **The Quote:** "Случайният множител носи серия популярни заглавия на Pragmatic Play." *(Literal translation artifact, likely from "The random multiplier drives/carries a series of popular titles..." Multipliers don't "carry" games in natural Bulgarian).*

**4. The "Tied-with-a-Bow" Summary**
*   **The Pattern:** Even when instructed not to use "In conclusion," AI models have a compulsive need to summarize the entire thesis of the article in the final paragraph before delivering the final warning or call to action.
*   **The Quote:** "x500 на банера обещава по-голямо число, но зад него стои същото предимство за казиното, само разлято в по-редки и по-едри попадения." *(This is a poetic but unnecessary recap of the entire "Голям таван" section).*

---

### **Concrete Recommendations**

*   **Fix the Echo:** Do not repeat the €0.20 / €20 example in the first H2 ("Върху какво пада коефициентът"). Since the intro already explains the math perfectly, use the first H2 to explain *why* this matters (e.g., how it impacts bankroll) or use a completely different scenario to illustrate the difference between multiplying the bet vs. multiplying the win.
*   **Unpack the Squashed List:** In the "Видовете, които ще срещнеш" section, break that dense paragraph into actual bullet points. Remove the artificial transitions ("До него върви", "Остава"). Let each multiplier type stand on its own as a clear, scannable item. 
*   **Correct the Collocation:** Rephrase the opening sentence of the Pragmatic Play section so the subject and verb make logical sense. Instead of the multiplier "carrying" the titles, state that a series of popular Pragmatic Play titles *use* or *rely on* the random multiplier.
*   **Cut the Summary:** Delete the sentence starting with "x500 на банера обещава по-голямо число..." Let the article transition naturally from the bonus wagering rules directly into the practical advice ("Ако това темпо ти допада...") and the responsible gambling warnings. 

*(Note: The responsible gambling language, 18+ markers, and affiliate disclosures at the bottom are perfectly formatted and compliant. Do not alter or remove them during your revisions).*
