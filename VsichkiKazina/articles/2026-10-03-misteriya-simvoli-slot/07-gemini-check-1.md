# 07 — GEMINI CHECK 1 (Step 7, verbatim) · vk-0247

NORMALIZATION: verdict „Likely human-written (or heavily human-edited), 85% confidence" → human-likeness = **85**. 85 ≥ 80 → **PASS** on the initial 05b (no humaniser pass required).
KEEP-BEST: only one version seen (initial 05b, HL 85). Highest = **85** → kept. gemini column = human 85.
Script: `python3 scripts/gemini_check.py …/05b-final-draft.md` → ONLINE, exit 0. No 429/rate-limit.
RESIDUAL suggestions below NOT applied: threshold cleared on first check; each change carries voice-strip/regression risk per MAX_GEMINI_PASSES policy. (Note: Gemini's rec #2 suggested deleting „Тук няма едно правило…"; its rec #3 to cut the asymmetric verdict line; these are stylistic preferences, not compliance issues, and removing the asymmetric closing would weaken the brand-required opinionated ending.)

---

**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**

This article reads exceptionally well and contains highly natural, gritty Bulgarian phrasing that AI almost never generates organically (e.g., "люшкането" for variance, "нискостоен боклук" for low-value symbols, "не ги мерете с една мярка"). These are strong indicators of a human author who understands slot mechanics deeply. 

However, the structural scaffolding of the article still clings to a few classic AI/SEO writing patterns—specifically in how it transitions between paragraphs, sets boundaries on what it will discuss, and wraps up with a slightly preachy conclusion. 

Here are the specific passages that trigger AI detection filters, along with actionable recommendations to smooth them out.

### 1. Pattern: Signposting / Over-explaining Scope
AI models love to narrate the structure of their own text, explicitly telling the reader what they are *not* going to talk about to keep their context windows neatly compartmentalized. This happens twice in close succession.

*   **Flagged Text 1:** *"Самото задействане на бонус с разпръснати (scatter) символи е друга механика със свой разбор; тук говорим какво прави покритата позиция на самите барабани."*
*   **Flagged Text 2:** *"Когато излезе wild, вече навлизаме в темата за дивите символи, която има свой отделен разбор."*
*   **Recommendation:** Remove the meta-commentary about what the article is *not* covering. You don't need to announce that scatters or wilds have their own separate articles ("свой разбор"). For the first flag, simply end the paragraph after "...я нямаше на екрана." For the second flag, just state that mystery symbols can reveal as wilds, and move straight to the next sentence about checking the game's rules.

### 2. Pattern: Formulaic Hedging / Filler Transitions
When AI needs to explain that slot mechanics vary by provider, it often defaults to a generic, slightly robotic opening phrase before getting to the actual point.

*   **Flagged Text:** *"Тук няма едно правило за всички заглавия. Мистерия символът може да се разкрие като..."*
*   **Recommendation:** Delete the filler sentence ("Тук няма едно правило за всички заглавия."). Start the paragraph directly with the meat of the information: "Мистерия символът може да се разкрие като обикновен плащащ символ..." It makes the text punchier and more confident.

### 3. Pattern: The Didactic / Moralizing Wrap-up
AI struggles to end articles without delivering a final "lesson" or moral judgment to the reader. It often uses an "If you do X, you are doing it wrong" structure to create a sense of finality.

*   **Flagged Text:** *"Ако избирате игра по това колко красиво се разкриват скритите символи, избирате по грешната причина."*
*   **Recommendation:** Cut this specific sentence entirely. The preceding sentences about setting limits and understanding the long-term price of the slot are excellent, mature, and sufficient. Ending on a finger-wagging note ("избирате по грешната причина") feels like an AI trying to force a profound conclusion. *(Note: Do not touch the "18+ Хазартът може да пристрасти. Играйте отговорно." markers that immediately follow this sentence—leave them exactly as they are).*

### 4. Pattern: Conversational Filler ("Да, но...")
AI sometimes tries to mimic human conversational tone by inserting artificial pauses or agreements with itself. 

*   **Flagged Text:** *"Повече покрити позиции на един спин, да, но всяка от тях се подчинява на абсолютно същата математика като всяко друго завъртане."*
*   **Recommendation:** Remove the "да, но" construction. It will read much more authoritatively as: "Дори при повече покрити позиции на един спин, всяка от тях се подчинява на абсолютно същата математика..."
