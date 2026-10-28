# Step 7 — Gemini check, pass 2 — danaci-pechalbi-onlajn-kazino

Run: 2026-10-28 · model gemini-3.1-pro-preview · file 05b-final-draft.md (after humaniser pass 1)
Normalized human-likeness = 100 − 85 = **15** (verdict: Shows AI patterns, 85%). Still below 80 → humaniser pass 2 (final; MAX_GEMINI_PASSES=2), keep-best.

---
## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 85% confidence.**

While the article is grammatically flawless and adheres well to the YMYL tax guide constraints (neutral register, no first-person anecdotes), it exhibits several classic LLM writing patterns. The most prominent issue is "semantic looping"—the AI makes a core point and then compulsively rephrases it multiple times across consecutive paragraphs. It also relies on formulaic signposting and slightly unnatural phrasing that reads like translated English AI structures. 

*(Note: As requested, I have noted the surviving `[VERIFY]` and `[About boilerplate slot]` tags. These are clearly prompt/template artifacts that survived the editorial process. Per your hard rules, I am noting this as a process issue but will not recommend their removal or touch them in my feedback).*

Here is the breakdown of the specific patterns and how to fix them.

### 1. Semantic Repetition (The "Loop")
**The Pattern:** LLMs often struggle to move a narrative forward, instead choosing to hammer the same premise using different words to pad the word count. 
**The Passages:**
*   *Paragraph 1:* "Решаващият фактор за данъка върху печалба от хазарт е лицензът на организатора, а не размерът на печалбата..."
*   *Paragraph 2:* "Законът гледа кой стои зад играта, не каква сума е излязла..."
*   *Paragraph 3:* "Текстът на закона не се интересува колко сте спечелили. Интересува се кой е организирал играта."
*   *Paragraph 3:* "Има ли такъв лиценз, печалбата на играча е необлагаема, независимо дали става дума за €20 или за сериозна сума."
**Recommendation:** Condense these four variations into a single, authoritative statement. You can merge the introduction and the "Защо данъкът..." section to state the rule once: the exemption depends entirely on the license, regardless of the amount won. 

### 2. Formulaic Signposting & Forced Keyword Insertion
**The Pattern:** AI frequently uses clunky, transitional setups to force exact-match keywords into the text, reading like a direct translation of "Therefore, the question of [Keyword] has a short answer."
**The Passage:** "Затова въпросът „данък печалба от хазарт" в България има кратък отговор за масовия случай: спечелите ли от казино с редовен лиценз, върху самата печалба не дължите данък..."
**Recommendation:** Remove the artificial setup ("въпросът... има кратък отговор за масовия случай"). Connect the legal premise directly to the practical outcome for the user. 

### 3. Unnatural Word Choice ("Translationese")
**The Pattern:** LLMs sometimes select words that are technically correct in a dictionary sense but contextually awkward in Bulgarian legal/tax writing.
**The Passage:** "Щом цялата защита стъпва на лиценза, него проверявате първо..."
**Recommendation:** The word "защита" (protection) is highly unnatural in a tax context. A human tax writer would use "освобождаване" (exemption), "облекчение" (relief), or simply "правило" (rule). Replace "защита" with a more accurate administrative term.

### 4. Narrated Emotion / Over-reassurance
**The Pattern:** When discussing potentially stressful topics (like bank AML checks or taxes), AI tends to adopt a pacifying, overly reassuring tone.
**The Passage:** "Минава се спокойно, когато документите са в ред..." and "Това обикновено е обяснението, което затваря въпроса."
**Recommendation:** Strip the subjective reassurance. A neutral YMYL editorial register should state facts, not tell the reader how to feel. Change the phrasing to objectively state that providing the transaction history and license proof is standard procedure for fulfilling bank AML requirements.

### 5. The "Robotic FAQ" Structure
**The Pattern:** AI-generated FAQs often feature identical, repetitive sentence structures for every answer, rather than natural conversational variance.
**The Passages:** 
*   "Не, стига организаторът да е лицензиран по Закона за хазарта..."
*   "Не, когато организаторът е лицензиран."
**Recommendation:** Vary the syntax in the FAQ answers. While the legal answer remains the same, a human writer would combine these or phrase the answers differently (e.g., starting one with "Печалбите от тото са освободени от налог при условие че...") to avoid the robotic "Не, [условие]" repetition.
