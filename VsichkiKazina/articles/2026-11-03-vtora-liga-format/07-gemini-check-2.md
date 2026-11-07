# Step 7 — External Gemini check — pass 2 (after humaniser pass 1)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-11-03-vtora-liga-format/05b-final-draft.md`
Date (UTC): 2026-11-03

## Normalized score
Verdict: **Shows AI patterns, 65% confidence** → HUMAN-LIKENESS = 100 − 65 = **35** (< 80 → still needs changes; improved from HL 15 at pass 1)

## Keep-best ledger so far
- pass 0 (initial draft): HL 15
- pass 1 (humaniser, apply check-1 recs): **HL 35** ← current best
- one humaniser pass remains (MAX_GEMINI_PASSES = 2)

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 65% confidence**

While this article is highly disciplined, avoids flowery adjectives (no "thrilling matches" or "dynamic clashes"), and features a very human-sounding, compliance-aware gambling section at the end, the core informational paragraphs exhibit classic LLM structural tells. It reads like a heavily prompted AI draft that has been polished by a human, or a human writer strictly following an AI-generated outline. The primary issues are over-explaining universal concepts and heavy use of structural "signposting."

### 1. Over-explaining universal knowledge (The "Alien" Explanation)
**The Passage:** "Победата носи три точки, равенството една, загубата нула, а сборът от тях нарежда отборите в класирането."
**The Pattern:** LLMs explain universally understood concepts as if the reader is new to the subject.
**Recommendation:** Delete this sentence entirely. [PIPELINE NOTE: 3/1/0 are untouchable numbers per the number-preservation rule; the points values are KEPT — we integrate them more tightly into the format description instead of leaving a standalone didactic sentence.]

### 2. Signposting and Formulaic Transitions
**The Passages:**
*   "Механиката кой се качва и кой пада е проста и постоянна..." (Intro)
*   "Движението в двете посоки следва един и същ прост принцип." (H2: Нагоре и надолу)
*   "Дотук всичко е постоянно. Това, което се мени от сезон на сезон, са точните подробности:"
**The Pattern:** AI relies on meta-commentary to glue paragraphs together, announcing *how* it will give the information.
**Recommendation:** Remove the meta-commentary. Cut the intro "simple and constant" line; delete the "same simple principle" opener and start directly with the champion; remove "Дотук всичко е постоянно. Това, което се мени..." and simply state that exact spots/playoff opponents are set by the seasonal regulations.

### 3. The "Numbered List" Intro
**The Passage:** "Четири неща около Втора лига не са заковани и се уреждат по регламента за всеки сезон."
**The Pattern:** LLMs count the items and announce the number in the intro sentence.
**Recommendation:** Remove the word "Четири"; state that certain elements are not fixed and depend on the seasonal regulations, then let the bullets speak.

*(Note: The responsible-gambling language, disclosures, and footer are perfectly formatted for compliance and were left entirely untouched in this review.)*
