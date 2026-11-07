# 07 — Gemini check (pass 1) — Снукър: правила и точкуване

**Command:** `python3 scripts/gemini_check.py 05b-final-draft.md` (model gemini-3.1-pro-preview), exit 0.

**Normalized human-likeness: 90** (verdict "Likely human-written, 90% confidence") → **PASS** (≥ 80).
Initial draft passes on pass 1; no humaniser pass applied (keep-best = initial draft, HL 90).
Recommendations are optional/style-only and were NOT applied, to avoid lowering a passing score (keep-best discipline). 0 facts/numbers/links/RG/dates/byline would be touched regardless.

---
## Gemini verbatim verdict + recommendations

**Verdict: Likely human-written, 90% confidence.**

This is an exceptionally well-crafted piece. In Bulgarian, AI models typically struggle with natural idioms, often producing stiff, overly literal translations of English phrasing. This text, however, uses highly natural, conversational Bulgarian phrasing ("свирка фал", "веднъж като хората", "както дойде", "чиста аритметика"). The sentence length varies beautifully, and the tone is authoritative yet accessible. 

However, there are a few subtle structural tropes—mostly in the transitions and wrap-ups—that echo common LLM rhetorical devices. If an AI assisted in drafting or structuring this, it was heavily and expertly edited. 

Here are the minor patterns that trigger a slight AI-detection flag, along with recommendations to make them completely bulletproof.

### Passages and Patterns Flagged

**1. The "Journey of Understanding" Intro Wrap-up**
*   **Quote:** *"Веднъж щом разбереш стойностите и реда, цялата тази тишина около масата започва да има смисъл."*
*   **Pattern:** **Thematic Resolution / "Once you X, Y" framing.** LLMs love to end introductory paragraphs with a promise of clarity, often using a "Once you understand [Topic], [Abstract concept] makes sense" formula to neatly tie a bow on the hook.

**2. The "Not merely X, but Y" Elevation**
*   **Quote:** *"Играчът не гони просто топки в джобовете, а събира точки в правилния ред и същевременно гледа къде ще остане бялата топка..."*
*   **Pattern:** **Contrast for Elevation.** AI frequently defines things by first stating what they are *not* (or not *just*), in order to make the actual definition sound more profound or strategic. 

**3. The Appended Dramatic Noun Phrase**
*   **Quote:** *"Сбери двете и получаваш 147, идеалният фрейм."*
*   **Pattern:** **Theatrical Summarization.** LLMs often tack on a descriptive noun phrase at the very end of a mathematical or factual explanation to give it a dramatic, conclusive flair (e.g., "...resulting in 147, the ultimate achievement").

**4. The "That is exactly why" Concluding Bow**
*   **Quote:** *"Правилата на снукъра са едни и същи от десетилетия и точно затова си заслужава да ги научиш веднъж като хората."*
*   **Pattern:** **Justified Conclusion.** AI struggles to just let an article end; it usually feels compelled to justify *why* the reader just read the article, often using "and that is why" or "ultimately" to validate the topic's importance.

*(Note: The responsible gambling section and disclosures at the bottom are perfectly integrated. Per your instructions, I am ignoring them for stylistic critique, though I will note that the thematic bridge used there—"колкото и подредена да изглежда играта"—is a classic AI contrast technique. However, it works well enough here and should not be touched).*

### Concrete Recommendations

*   **For the Intro Wrap-up:** Remove the "Once you understand..." framing. You can make it punchier and more human by just stating the reality of the game directly. *Recommendation: Change the final sentence of the intro to simply state that the silence around the table is actually the sound of players calculating their next three moves.*
*   **For the "Not merely X" Elevation:** Drop the negative contrast. *Recommendation: Start the sentence directly with the action. Instead of saying the player "doesn't just chase balls," say "The player's goal is to collect points in the right order while positioning the white ball..."*
*   **For the Dramatic Noun Phrase:** Let the math speak for itself. The phrase "чиста аритметика" earlier in the paragraph already sets the tone perfectly. *Recommendation: End the sentence cleanly at "получаваш 147". You don't need "идеалният фрейм" to sell the importance of the number.*
*   **For the Concluding Bow:** Remove the justification ("и точно затова си заслужава..."). *Recommendation: Rephrase the opening of the final paragraph to be a simple, standalone observation. For example, state that because the rules haven't changed in decades, learning them pays off forever—without the "and that is exactly why" connective tissue.*
