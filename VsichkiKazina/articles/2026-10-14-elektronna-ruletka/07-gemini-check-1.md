# Step 7 — Gemini external check (pass 1 / baseline)

Script: `python3 scripts/gemini_check.py 05b-final-draft.md`
Run: 2026-10-14 · GEMINI_API_KEY set · model: gemini (cross-model probe)

## Normalized result
- Verdict phrasing: **"Likely human-written (or heavily human-edited), 80% confidence."**
- HUMAN-LIKENESS = **80** (verdict is "Likely human-written, 80%").
- PASS test: human-likeness 80 ≥ GEMINI_TARGET_CONFIDENCE (80) → **PASS** on the baseline draft.
- Decision: no Humaniser pass applied. Baseline 05b is the keep-best version (highest human-likeness seen). Recommendations below are style-only and NOT applied (PASS already reached; applying them risks lowering the score and could touch voice — kept for the human editor's optional consideration). Gemini never touches facts/RG/disclosures/flags.

## Gemini verbatim verdict + recommendations

**Verdict: Likely human-written (or heavily human-edited), 80% confidence.**

This article is exceptionally well-crafted and avoids the most glaring LLM hallmarks (there are no "В днешно време" / "Nowadays", no endless bulleted lists, and no robotic "Важно е да се отбележи" / "It is important to note"). The deep integration of specific Bulgarian legal frameworks (Закон за хазарта, НАП articles) and the highly natural, conversational explanations of casino mechanics ("топчето не дължи черно на никого") point to a skilled human writer or a very heavily prompted and meticulously edited AI draft.

However, there are a few lingering stylistic flourishes that trigger AI detection. LLMs love to personify abstract concepts, use dramatic signposting, and wrap everything up in a neat, philosophical bow at the end.

Here are the specific patterns that still read as AI-generated, along with actionable recommendations to iron them out.

### 1. Pattern: Personification of Abstract Concepts (Narrated Drama)
AI models frequently try to make technical explanations "engaging" by giving human traits or dramatic actions to inanimate objects or mathematical concepts.
*   **Flagged Passage 1:** *"Скоростта носи тиха последица за играча."* (Speed brings a silent consequence for the player.)
*   **Flagged Passage 2:** *"Домашното предимство мълчи за следващото завъртане; казва само накъде клони сумата..."* (The house edge is silent about the next spin; it only says where the sum leans...)
*   **Recommendation:** Remove the poetic personification. For the first passage, state directly that faster gameplay simply means more bets per hour. For the second passage, replace the idea of the house edge "being silent" and "speaking" with a direct statement about how statistical probability applies to long-term variance rather than individual spins.

### 2. Pattern: Clunky/Translated Idioms
Sometimes AI attempts to use idioms or metaphors that sound great in English but translate slightly unnaturally into Bulgarian, feeling overly stylized.
*   **Flagged Passage 1:** *"...но колелото не е честно към играча, и причината се събира в зеленото зеро."* ("...the reason gathers in the green zero.")
*   **Flagged Passage 2:** *"Нелицензираните сайтове са другата страна на сметката."* ("Unlicensed sites are the other side of the bill/equation.")
*   **Recommendation:** Adjust the verbs and nouns to standard Bulgarian phrasing. Change "се събира в" to something more natural like "се крие в" (hides in) or "се дължи на" (is due to). Change "другата страна на сметката" to a more direct transition, such as simply stating the risks associated with playing outside the licensed framework.

### 3. Pattern: Dramatic Signposting
LLMs often use theatrical transitions to introduce a new point, rather than letting the argument flow naturally.
*   **Flagged Passage:** *"Тук се разпада и най-устойчивият мит."* (Here falls apart the most persistent myth.)
*   **Recommendation:** Tone down the theatricality. You can transition into the topic of betting systems directly by stating that because spins are independent, betting systems cannot overcome the mathematical edge.

### 4. Pattern: The "Neat Bow" Summary Conclusion
AI almost always insists on writing a final paragraph that perfectly summarizes the thesis of the entire article, often mirroring the introduction.
*   **Flagged Passage:** *"Електронната рулетка не е нито по-щедра, нито по-измамна от колелото на масата. Тя е същата игра с друг двигател и със същото зелено зеро, което държи предимството на страната на казиното на всяко едно завъртане."*
*   **Recommendation:** Cut or merge this paragraph. Human writers writing for the web often end on the most practical note—in this case, the excellent "Разумната сметка" section about bankroll management and responsible gambling. Ending abruptly on the practical advice leaves a stronger, more authoritative impression than adding a philosophical summary at the very end.

***

**A note on process:** The responsible gambling language, the 18+ markers, the author bio, and the legal disclaimers at the bottom are perfectly formatted and highly professional. Per your rules, these have not been evaluated for style and should remain exactly as they are. The integration of the upcoming 2026 affiliate licensing law is a fantastic touch of human expertise.
