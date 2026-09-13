# Step 7 — Gemini external check · pass 1

Model: gemini-3.1-pro-preview · Date: 2026-09-13
Verdict: Shows AI patterns, 75% confidence → human-likeness = 25
Result: needs changes (HL 25 < 80) → apply recs via fresh Humaniser pass

## Gemini verbatim verdict + recommendations

Here is my evaluation of the article based on LLM writing patterns and AI text detection.

### **Verdict**
**Shows AI patterns, 75% confidence.** 
While the article is highly informative, free of typical AI "fluff," and does an excellent job explaining the math without over-promising, its underlying skeleton is highly mechanical. It suffers from a staccato rhythm, disguised lists, and formulaic transitions that are classic hallmarks of a well-prompted Large Language Model (like GPT-4 or Claude) instructed to be concise. 

---

### **Specific Passages and Patterns Flagged**

**1. The "Disguised List" (Formulaic Paragraph Structure)**
> *"Коефициентите в ротативките идват в няколко форми. Най-прекият е множителят на печалбата: умножава резултата... Символ-множителят обикновено е wild... Нарастващият (прогресивен) множител не стои фиксиран... Случайният пада без правило... Има и множител в бонуса..."*
* **The Pattern:** AI models often struggle to write organic paragraphs when asked to explain multiple types of something. Instead, they write a bulleted list and just remove the bullet points, resulting in a robotic, repetitive cadence where every sentence introduces a new item with the exact same subject-verb structure. The opening sentence ("идват в няколко форми" / "comes in several forms") is also a classic AI introductory trope.

**2. Staccato Rhythm (Over-indexed Conciseness)**
> *"Коефициентът се начислява върху печалбата, не върху залога. Печалба от €0.20 при x2 става €0.40. Същата печалба при x100 излиза €20 (примерни). Между двете стои само коефициентът, докато базата остава дребната сума..."*
* **The Pattern:** In an attempt to be clear and avoid hallucination, the AI has generated a series of short, choppy sentences of almost identical length. This creates a "staccato" rhythm that feels unnatural to a human reader, who would typically use a mix of simple and complex sentences to explain math.

**3. Abrupt Fact Insertion (Context-Dropping)**
> *"В Sweet Bonanza коефициентите падат като бомби само в безплатните завъртания и се начисляват върху общата печалба от завъртането, в диапазон от 2x до 100x. Играта излиза през 2019 г. При Gates of Olympus кълбата стигат до 500x..."*
* **The Pattern:** AI models are often prompted to "include facts and data." To satisfy this, they will abruptly drop a raw fact (like a release year) right in the middle of a mechanical explanation, with zero transitional tissue connecting it to the sentences before or after it. 

**4. AI Signposting and Sweeping Summaries**
> *"За илюстрация: при €0.20 залог играта с нисък таван може да ти връща..."*
> *"Множителят е най-ефектната част от ротативката и най-често подвежда."*
* **The Pattern:** "За илюстрация" (For illustration) is a textbook AI signpost used to pivot into an example. Furthermore, the final paragraph begins with a sweeping, definitive summary statement—a structural habit ingrained in LLMs from being trained on standard essay formats (Introduction, Body, Conclusion).

---

### **Concrete Recommendations**

*   **Fix the Disguised List:** In the "Видовете, които ще срещнеш" section, either format the text as an actual bulleted list (which is better for UX anyway), or rewrite the paragraph to flow conversationally. Connect the ideas using transitional phrases rather than starting five consecutive sentences with the name of a new multiplier.
*   **Vary the Sentence Length:** In the "Върху какво пада коефициентът" section, combine the math examples into a single, flowing sentence. Use conjunctions or semicolons to break up the robotic subject-verb-object repetition. 
*   **Integrate Orphaned Facts:** Do not remove the 2019 release date for *Sweet Bonanza*, but weave it into the narrative. For example, connect the date to the mechanic itself (e.g., explaining that since its release in 2019, the game set a standard for how random multipliers work). 
*   **Remove Signposts and Soften the Conclusion:** Delete the phrase "За илюстрация:" and simply start the sentence with the example. For the final paragraph, drop the sweeping essay-style opening sentence. Start directly with the practical advice about how the x500 banner promises a big number but requires bankroll management. 

*(Note: The responsible gambling language, 18+ markers, and affiliate disclosures at the bottom are perfectly placed and formatted. They should remain exactly as they are.)*
