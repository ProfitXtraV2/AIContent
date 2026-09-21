# 07 — Gemini external check, pass 1 (initial draft) — Moon Princess

Model: gemini-3.1-pro-preview · script: scripts/gemini_check.py
**Verdict: Likely human-written (or heavily human-edited AI), 85% confidence.** → human-likeness = **85**. → **PASS** (≥ GEMINI_TARGET_CONFIDENCE 80) on the first check.

## Decision
Human-likeness 85 ≥ 80 → PASS, keep the initial draft. No Humaniser pass applied (a pass risks lowering the score; keep-best keeps the highest seen). content-queue gemini = `human 85`. All untouchables intact (5×5/3/2017/1–2/4/5/8/x20/96.50/94.51/3.50/€1000/€965/€35/5000, the 1 [VERIFY], 18+ line, RG, affiliate footer, byline, brand, dates). Gemini explicitly left the [VERIFY] flag, 18+ markers and RG boilerplate intact.

## Gemini raw verdict + recommendations (verbatim)

Here is my assessment of the article based on LLM writing patterns and AI-generated text detection.

### **Verdict**
**Likely human-written (or heavily human-edited AI), 85% confidence.**

This text is exceptionally clean and avoids the vast majority of AI hallmarks. It lacks the typical bloated introductions ("В забързания свят на онлайн казината..."), avoids summary conclusions ("В заключение..."), and uses highly idiomatic, natural Bulgarian phrasing (e.g., "няма да те завари на масата", "не значат нищо, докато не се допрат").

However, there are a few lingering structural and stylistic patterns that occasionally trigger AI detection algorithms. These are minor but worth addressing to make the text completely bulletproof.

---

### **Flagged Passages & AI Patterns**

**1. Formulaic Contrast/Transition**
> *"Ефектът е приятен за окото, но зад каскадите работи конкретна математика с висока волатилност, която е добре да познаваш преди първото завъртане."*
* **The Pattern:** AI models frequently use a "surface vs. reality" contrast to transition from an introduction into technical details (e.g., "While X is fun/beautiful, behind it lies Y that you must understand"). It feels slightly manufactured.

**2. Signposting (Forward Referencing)**
> *"По пътя дотам всяка печеливша каскада качва и множителя, за който става дума по-долу."*
* **The Pattern:** "Signposting." LLMs love to hold the reader's hand and announce what they are going to talk about later ("as discussed below," "which we will cover in the next section"). Human writers usually just let the reader discover the next section naturally.

**3. Staccato Rhythm / Robotic Listing**
> *"Love превръща един тип символ в друг, за да събере съвпадения. Star добавя един или два wild символа. Storm премахва два типа символи от решетката и разчиства място за нови."*
* **The Pattern:** Formulaic sentence structure. When explaining game mechanics, AI often defaults to a repetitive Subject-Verb-Object rhythm. Here, we have three consecutive sentences with the exact same cadence and length, creating a robotic, staccato feel.

**4. Cliché Metaphor (Narrated Importance)**
> *"Множителят е сърцето на рунда."*
* **The Pattern:** AI struggles to convey importance without resorting to stock metaphors. "X is the heart of Y," "At the core of X lies Y," or "X is the key to Y" are classic ChatGPT crutches used to inject artificial excitement.

---

### **Concrete Recommendations**

*   **For the Intro Transition:** Remove the artificial contrast. You can simply state that the game features anime styling and three princesses, and then directly introduce the math/volatility in the next sentence without the "приятен за окото, но..." bridge.
*   **For the Signposting:** Simply delete the phrase *, за който става дума по-долу*. The sentence works perfectly as "По пътя дотам всяка печеливша каскада качва и множителя." The reader will naturally see the multiplier explained in the very next section.
*   **For the Staccato Rhythm:** Break up the repetitive syntax in the Princesses section. You can either format these three powers as a concise bulleted list, or combine them using conjunctions and varied punctuation so they don't read like a manual (e.g., explaining what Love does, while noting that Star adds wilds, and Storm clears the grid).
*   **For the Cliché Metaphor:** Cut "Множителят е сърцето на рунда." Start the paragraph directly with the mechanics: "По време на рунда множителят расте с по едно при всяка печеливша каскада..." The mechanics themselves prove its importance; you don't need to narrate it.

*(Note on process: The [VERIFY] tag in the RTP section, the 18+ markers, and the responsible gambling boilerplate at the end have been noted and left entirely intact, as they represent proper compliance and editorial workflow.)*
