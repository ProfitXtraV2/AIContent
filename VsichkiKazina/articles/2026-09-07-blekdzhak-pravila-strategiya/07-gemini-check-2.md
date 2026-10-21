# Step 7 — Gemini check, pass 2 (after Humaniser pass 1)

Model: gemini-3.1-pro-preview · verbatim output below.
Normalized: **"Shows AI patterns, 75%"** → human-likeness = **25** (tied with initial; one more pass allowed).

---

**Verdict: Shows AI patterns, 75% confidence.**

While this article is highly informative, factually dense, and avoids the worst AI hallucinations, its underlying skeleton gives it away. It reads like a very well-prompted Large Language Model (likely GPT-4) that was instructed to be objective and include specific internal links. The primary giveaways are the formulaic transitions (signposting exactly what the next paragraph will be about), the didactic "teacher" voice that over-explains *why* a mechanic matters, and the tendency to wrap up paragraphs with neat, philosophical punchlines. 

Here is the breakdown of the specific patterns and how to fix them.

### 1. Formulaic Transitions & Signposting
AI models love to end a paragraph by explicitly pointing to the next one, treating the reader like they need to be led by the hand. 

*   **Flagged text:** *"Кога кой ход има смисъл, казва основната стратегия."* (End of the "Moves" section, pointing to the "Basic Strategy" section).
*   **Flagged text:** *"Преди истинските пари има безплатен начин да усвоите всичко това."* (Opening of the Demo section).
*   **Recommendation:** Delete both sentences entirely. Human writers rely on subheadings (H2s) to introduce new concepts. Let the H2 "Какво е основната стратегия" do its job. For the demo section, start directly with the actionable advice: "Демо режимът пуска блекджек без депозит..."

### 2. Narrated Emotion & Over-explaining (The Didactic Voice)
AI frequently assigns qualitative traits to basic facts (e.g., calling a rule "special" or "predictable") and then over-explains *why* it is so, rather than just stating the rule.

*   **Flagged text:** *"Гъвкавостта на асото прави ръцете с него специални."*
*   **Flagged text:** *"Липсата на избор прави играта предвидима, защото знаете предварително какво ще направи дилърът при всяка своя открита карта."*
*   **Recommendation:** Strip out the subjective filler. Remove the sentence about the ace being "special" entirely—the surrounding sentences already explain its value perfectly. For the dealer section, delete the flagged sentence; the fact that the dealer must hit to 17 already implies the game is predictable. You don't need to spoon-feed the realization to the reader.

### 3. The "Infomercial" Hook
AI often starts paragraphs by assigning a human emotion or temptation to a concept, only to immediately debunk it in the same breath.

*   **Flagged text:** *"Застраховката е примамлива и почти винаги грешна."*
*   **Recommendation:** Remove the subjective "примамлива" (tempting). Make the opening punchier and strictly factual. Suggestion: start directly with the fact that it is almost always a mathematical mistake, without assuming the reader finds it tempting.

### 4. Breathless Run-on Sentences (Over-coordination)
When AI tries to summarize a complex thought, it often strings too many clauses together using conjunctions like "а", "които", and "така че", resulting in a breathless, robotic rhythm.

*   **Flagged text:** *"Броенето не е и лесна печеливша система на живо в зала, а умение, което иска условия, каквито онлайн средата премахва нарочно, така че не е разумно да се разчита на него като на план за печалба."*
*   **Recommendation:** Break this massive sentence into two distinct, shorter sentences. Remove the "така че" (so that) transition, which is a classic AI crutch used to force a conclusion into a single breath. 

### 5. The "Clever" Wrap-up
AI models are trained to conclude thoughts neatly, often resulting in a slightly dramatic or philosophical summary at the end of a paragraph.

*   **Flagged text:** *"Застраховката не застрахова нищо: тя е отделен залог, който губите по-често, отколкото печелите."*
*   **Recommendation:** While this is actually a good line, combined with the other patterns, it feels like a ChatGPT punchline. Keep the second half ("тя е отделен залог, който губите по-често..."), but remove the dramatic "Застраховката не застрахова нищо:" setup to make it sound more like a dry, professional gambling guide.

***

*Note on Hard Rules: The responsible gambling language, 18+ markers, and boilerplate text at the end of the article are perfectly placed and formatted. Do not alter or remove any of this text.*
