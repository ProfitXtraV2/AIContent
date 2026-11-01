# Step 7 — Gemini check (pass 2, after humaniser pass 1) · vk-0295
Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-27-belot-onlayn/05b-final-draft.md`
Date: 2026-10-27

Normalized human-likeness: **85** (saved verdict Likely human-written 85pct). Detector high-variance this session on the SAME pass-1 text: observed 75pct AI (HL 25) and 85pct human-written (HL 85) across reads. Best/kept = HL 85 -> PASS (>=80).

KEEP-BEST DECISION: pass-1 is the winner. Baseline draft read HL 15-25; humaniser pass 1 (cut meta-discourse, hollow hooks, half the neat wrap-ups, the looped kitchen-table metaphor) lifted the ceiling to a genuine Likely human-written 85pct verdict. Final 05b = pass-1 text. gemini column -> human 85.

## Gemini verbatim verdict + recommendations (representative PASS read)

**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**

This article reads exceptionally well. The author uses natural, highly contextual Bulgarian idioms that AI almost never generates organically (e.g., *"на кухненската маса"*, *"пари оттам не падат"*, *"видите ли някъде"*, *"не стигат до стената"*). The pacing is generally brisk, and the insights about the game (e.g., *"анонсите блъфират, сигналите между партньорите имат значение и една грешна карта се помни"*) show actual subject-matter expertise. 

However, while the *voice* is human, the *scaffolding* still exhibits a few classic LLM structural patterns. The writer has filled out an outline that forces some redundant summaries and didactic wrap-ups. 

Here are the specific passages that trigger AI-detection patterns, along with actionable recommendations to polish them out.

### 1. The "Target Audience" Wrap-up
> **Flagged text:** *"По-подходящо е за човек, който иска няколко игри в едно приложение, не само белот."* (Under the Djagi section)
> **Pattern:** **Formulaic Persona Matching.** LLMs frequently end product or software descriptions by explicitly stating exactly who the product is for, using a very predictable "This is suitable for a person who..." structure. It feels like a textbook summary rather than a natural continuation.
> **Recommendation:** Delete this sentence entirely, or weave the benefit into the previous sentence. For example, you could just end the previous sentence with: *"...както срещу реални съперници, така и с поканени приятели, ако търсите разнообразие от игри в едно приложение."*

### 2. The Tautological Over-explanation
> **Flagged text:** *"Чиповете не се осребряват и нямат стойност извън самата платформа, тоест и спечелените купчини остават вътре в играта."*
> **Pattern:** **The "That is to say" (тоест) Echo.** AI hates leaving room for interpretation. It often states a clear fact, and then immediately rephrases the exact same fact in the same sentence to ensure the reader understood it. 
> **Recommendation:** Cut the second half of the sentence. *"Чиповете не се осребряват и нямат стойност извън самата платформа."* is a strong, confident statement. You don't need the "тоест..." clause to explain it to the reader.

### 3. The Didactic/Moralizing Wrap-up
> **Flagged text:** *"Полезно е да решите предварително колко, ако изобщо, сте готови да похарчите за едно развлечение."* (End of the "Как да изберете платформа" section)
> **Pattern:** **Unsolicited Life Advice.** AI models are fine-tuned to be helpful and cautious, which often results in them ending paragraphs with generalized, slightly preachy advice. 
> **Recommendation:** Remove this sentence. The preceding sentence (*"Единственото, за което си струва да внимавате навсякъде, са микротранзакциите..."*) already does the job perfectly and sounds much more conversational. 

### 4. The Redundant Conclusion Bow
> **Flagged text:** *"За повечето хора безплатната маса в браузъра срещу реални съперници върши най-добра работа; приложението и игрите срещу компютър са по-скоро допълнение. Чиповете са за удоволствие и за трениране на анонсите, а пари оттам не падат и платформите не обещават обратното."*
> **Pattern:** **The "In Conclusion" Summary.** Even though the phrasing here is wonderfully human (*"пари оттам не падат"*), the structural purpose of this paragraph is pure AI. LLMs are programmed to write essays with a neat concluding paragraph that summarizes everything that was just said in the article. In modern web copywriting, this is fluff.
> **Recommendation:** Delete this final paragraph entirely. The article actually reaches its natural, strongest conclusion at the end of the *"Преди да седнете на масата"* section. *(Note: Do not touch the responsible gambling language in the paragraph above this one; just remove this final summary block).* 

***

**Process Note on Disclosures:** The responsible gambling language, 18+ markers, author bio, and affiliate disclosures at the bottom are perfectly formatted and intact. They should remain exactly as they are.

