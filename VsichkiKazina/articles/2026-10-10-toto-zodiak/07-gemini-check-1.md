# Step 7 — Gemini cross-model check — PASS 1 (initial 05b)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-10 (cloud reconcile of HANDOFF row)

## Verdict (verbatim)

→ Normalized HUMAN-LIKENESS = 100 − 95 = **5**  (PASS threshold = 80) — needs changes

---

**Verdict: Shows AI patterns, 95% confidence.**

While the text is exceptionally well-prompted and mimics a human copywriter’s tone beautifully (using colloquialisms like "Плащате за тръпката от тегленето, и толкова" and specific, grounded examples), it contains structural tells and one massive, undeniable AI artifact at the very end that gives the game away. 

Here is the breakdown of the patterns that triggered this assessment, along with actionable recommendations.

### 1. Prompt Leakage / Meta-Commentary (The Smoking Gun)
**The Pattern:** LLMs instructed to follow strict style guides often generate a "compliance report" or meta-commentary at the end of their output to prove they followed the rules.
**The Passage:** 
> `<!-- 5b changes: no changes. No em-dashes (only en-dashes in the brand name "ТОТО 2 – Зодиак" and range "3–8"), no signposting lead-ins or banned connectives, no bullet lists; 10-row prize-groups table kept (real comparative work); no parallel-structure/hedge/heading tells found; both 18+ footer lines left untouched. -->`
* **Recommendation:** Delete this HTML comment entirely. It is a direct artifact of the AI evaluating its own output against a set of negative constraints (likely your own prompt instructions). 

### 2. Robotic Signposting (The "In this article" Trope)
**The Pattern:** AI models love to open articles with a literal, bulleted, or explicitly stated roadmap of what the text will and will not do. It feels like a syllabus rather than an engaging hook.
**The Passage:** 
> "*Какво покрива статията: правилата, графика на тиражите, печелившите групи и реалните шансове. Какво не покрива: числа за залагане и съвети кога или колко да играете.*"
* **Recommendation:** Remove this italicized block. You already have a strong, natural hook in the following sentence ("Шансът да спечелите джакпота... е 1 на 25 425 120"). If you must keep the disclaimer about not providing betting numbers, weave it naturally into the prose (e.g., "В този текст ще разгледаме правилата и математиката зад играта, без да ви залъгваме с 'печеливши' числа.").

### 3. AI Hedging / Over-Clarification
**The Pattern:** LLMs are hardwired by safety guidelines to avoid making financial or gambling predictions. When they use a hypothetical number, they often immediately follow it with a defensive disclaimer explaining that it is not a guarantee. Humans usually trust the reader to understand obvious hyperbole or mathematical scale.
**The Passage:** 
> "С една комбинация във всеки от двата тиража седмично ще чакате средно около 244 000 години до първия джакпот. *Числото служи само да покаже мащаба; прогноза няма как да бъде.*"
* **Recommendation:** Delete the second sentence ("Числото служи само..."). The 244,000-year metric is a great, punchy piece of human-like copywriting. Explaining to the reader that a 244,000-year wait is "not a prediction" kills the rhetorical impact and sounds like a legal compliance bot.

### 4. Formulaic FAQ Summarization
**The Pattern:** AI-generated FAQs often read like a robotic regurgitation of the exact H2s and data points already covered in the text, asked in a highly sterile format. 
**The Passage:** 
> "**Само зодия печели ли нещо?** Да, това е 10-а група, с шанс 1 на 20,8; в тираж 76 тя е платила €0,60."
* **Recommendation:** To make the FAQ read less like an AI summarizing its own article, rephrase the answers to be conversational rather than data-dumps. For example, change the answer to: "Да, дори да не познаете нито едно число, уцелената зодия ви носи малка печалба (обикновено стотинки), която ви връща част от залога."

---

**A Note on Process:** 
As requested, I have not touched or suggested removing any of the `[VERIFY]`, `[CONFLICT]`, or `[DATA NEEDED]` tags, nor the 18+ responsible gambling footers. However, from an editorial standpoint, the fact that these bracketed tags survived into a "finished, human-verified article" indicates a gap in the editing pipeline. A human editor needs to resolve those specific data conflicts (like the BNT vs. Facebook broadcast time) before this goes live.
