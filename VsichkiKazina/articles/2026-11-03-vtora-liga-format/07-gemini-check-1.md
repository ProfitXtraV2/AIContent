# Step 7 — External Gemini check — pass 1 (INITIAL DRAFT)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-11-03-vtora-liga-format/05b-final-draft.md`
Date (UTC): 2026-11-03

## Normalized score
Verdict: **Shows AI patterns, 85% confidence** → HUMAN-LIKENESS = 100 − 85 = **15** (< GEMINI_TARGET_CONFIDENCE 80 → needs changes)

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 85% confidence.**

While the article is grammatically flawless, well-structured, and successfully avoids the most egregious AI buzzwords (like "в днешния забързан свят" or "нека се потопим"), it suffers heavily from a classic LLM structural tell: **meta-commentary and over-justification**.

The AI was clearly given instructions to write an "evergreen" guide that doesn't lock in specific seasonal numbers. Instead of simply executing this, the AI repeatedly *explains to the reader* why it is omitting these numbers, resulting in a highly self-referential, robotic tone. It reads like a machine explaining its own prompt constraints.

Here is the breakdown of the specific patterns and how to fix them.

---

### 1. Meta-Commentary and Signposting
**The Pattern:** The text constantly talks about its own structure and justifies its editorial choices.
**Flagged Passages:**
*   „...затова самата бройка идва по-надолу." (Signposting)
*   „...затова няма смисъл да се помнят като вечна истина." (Editorializing its own omission)
*   „...а не евъргрийн гид като този." (Breaking the fourth wall)
*   „...самата тази разнобойка показва защо не фиксираме число." (Over-justification)
*   „...затова не го назоваваме..." (Over-justification)

**Recommendations:** Remove all self-referential explanations. Do not tell the reader *why* you are omitting a number or sponsor name. State plainly: "The sponsor name and exact number of teams change depending on the season's regulations." Delete the phrase "евъргрийн гид като този".

### 2. The "Robotic Disclaimer"
**Flagged Passage:** „Шампион за сезон 2025/26 е Дунав (Русе), което остава като завършена историческа справка, а не като текуща позиция в класирането."
**Recommendation:** Cut the second half. End at: „Шампион за сезон 2025/26 е Дунав (Русе)."

### 3. Pedantic / Dictionary-Style Exposition
**Flagged Passage:** „Победата носи три точки, равенството една, загубата нула, а подреждането в класирането върви по събрания сбор."
**Recommendation:** Gemini suggested deleting it (audience already knows football scoring). [PIPELINE NOTE: the numbers 3/1/0 are untouchable per the number-preservation rule — the points fact is KEPT; only the trailing "а подреждането..." clause may be trimmed.]

### 4. Formulaic Juxtaposition & Didactic Conclusions
**Flagged Passages:**
*   „Футболът е едно, залагането около него е друго." (Stiff binary transition)
*   „Историческите справки за Втора лига носят точни дати и точни числа. Изходът от следващия мач не се знае предварително и никой залог не го гарантира." (Didactic summarizing conclusion)
**Recommendations:** Soften/drop the "Football is one thing..." setup. Remove the final philosophical wrap-up paragraph (the preceding RG paragraph ends the section perfectly). *Note from Gemini: Do not touch the actual responsible-gambling warnings, just this stylistic wrap-up.*
