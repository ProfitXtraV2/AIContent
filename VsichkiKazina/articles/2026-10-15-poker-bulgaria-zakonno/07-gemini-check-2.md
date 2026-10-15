# 07 — GEMINI CHECK — pass 2 (after Humaniser pass 1 applying pass-1 recs)

Command: python3 scripts/gemini_check.py 05b-final-draft.md
Normalized HUMAN-LIKENESS = **85** (verdict: Likely human-written, 85% confidence). **PASS** (≥ 80).
KEEP-BEST: baseline HL 30 (pass 1) → HL 85 (pass 2, humaniser pass 1). Winner = current 05b (pass 1 revision). Loop ends on PASS; no further pass needed. Pass-2 recs are optional polish, NOT applied (already PASS).

## Gemini verbatim verdict + recommendations

Here is my evaluation of the article from the perspective of a senior copywriter and AI-text detection specialist.

### **Verdict: Likely human-written (or heavily human-edited), 85% confidence.**
This article reads exceptionally well and avoids almost all the classic AI pitfalls (there is no "In the ever-evolving landscape of...", no fluffy introductions, and no overly dramatic adjectives). The writer uses natural Bulgarian phrasing ("не е прищявка на сайта", "сивата зона") and demonstrates a deep, highly specific understanding of local law. 

However, there are a few mechanical quirks and structural tells that occasionally make it sound like an AI trying to be hyper-accurate, or a human writer following a very rigid SEO/legal brief. 

Here are the specific patterns that triggered my radar, along with actionable recommendations to smooth them out.

---

### **Flagged Passages, Patterns, and Recommendations**

#### **1. Pattern: Robotic Precision / Over-calculation**
AI models love exact math and often fail to understand when a human would naturally round numbers for readability, especially when converting currencies. 
*   **The Quote:** *"По фиксирания курс 1,95583 лв. за 1 евро това е около 255,65 € до 1022,58 €..."*
*   **The Issue:** No human writer calculating a rough estimate for a legal fine includes five decimal places for the exchange rate and two decimal places for the final euro amount. It reads like a direct output from a ChatGPT prompt asking to "convert the fine to Euros."
*   **Recommendation:** Soften the math to sound like a human speaking. Suggestion: Keep the exact BGN fine as dictated by law, but round the Euro conversion to whole numbers (e.g., "около 255 до 1022 евро") to remove the robotic exactness.

#### **2. Pattern: Repetitive Safety Disclaimers (AI Guardrails)**
AI models are hardcoded to avoid giving legal or financial advice, which often results in them injecting "this is not legal advice" disclaimers multiple times throughout a single text.
*   **The Quotes:** 
    *   *(Intro):* "*Тази статия обяснява правната рамка на разбираем език и не е правен съвет.*"
    *   *(Section: Данъчно третиране...):* "Това не е правен съвет за конкретен случай, а само прочит на общото правило."
*   **The Issue:** While the first disclaimer in the intro is excellent and professional, repeating the exact same sentiment later in the text feels like an AI safety trigger going off because the prompt mentioned "home games" and "law."
*   **Recommendation:** Keep the italicized disclaimer in the introduction exactly as is. In the "Данъчно третиране" section, remove the second disclaimer sentence entirely. The intro already covers the whole article, and removing the repetition will make the author sound more confident.

#### **3. Pattern: Mechanical Signposting for Internal Links**
AI (and sometimes junior SEO writers) struggles to weave internal links naturally into a narrative, instead relying on a rigid "We talk about X here, but this article is about Y" formula.
*   **The Quotes:** 
    *   "Как да се уверите... описахме отделно в [ръководството за проверка на лиценз]; общата рамка на онлайн хазарта събрахме в [законен ли е онлайн хазартът в България]."
    *   "Самите правила на играта... разглеждаме в [как се играе покер в казино]; тук темата е само правният статут."
*   **The Issue:** Using this exact "we wrote about X here" structure three times makes the text feel a bit like a textbook syllabus rather than an engaging article. 
*   **Recommendation:** Integrate the anchor text more organically into the active sentences. For example, instead of stopping the paragraph to announce where the rules are, you could advise the writer to blend it: *"Докато [правилата на играта и подредбата на ръцете] са еднакви навсякъде, правният статут изисква..."* (Note: Do not use this exact rewrite, just advise the writer to blend the links into the natural flow of the sentences rather than pointing to them).

#### **4. Pattern: Over-explaining the Negative**
AI often uses a specific logical structure where it states a rule, and then immediately explains the inverse of the rule to pad the word count.
*   **The Quote:** *"Чл. 41, ал. 2 позволява всички изброени игри да се организират и онлайн, с изключение на томболата и моментната лотарийна игра, а покерът не е сред тези две изключения."*
*   **The Issue:** The phrase "and poker is not among these two exceptions" is logically redundant and slightly clunky. A human expert would usually just state that the law allows casino games (including poker) to be played online.
*   **Recommendation:** Advise the writer to trim the redundant logical loop. They can simply state that the law allows casino games to be organized online, without needing to list the exceptions (tombola/lottery) just to prove poker isn't one of them.

---

### **Process Note on Hard Rules:**
*   The **[VERIFY: данъчното третиране...]** flag is present and intact. This is excellent editorial practice for legal/tax content. Do not remove it until the fact-checker clears it.
*   The **18+ and Responsible Gambling** language, as well as the affiliate disclosures, are perfectly placed and highly specific to Bulgarian regulations (including the upcoming 2026 affiliate licensing). They have been left completely untouched.
EXIT=0
