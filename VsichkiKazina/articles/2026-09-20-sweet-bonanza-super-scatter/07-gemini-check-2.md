# 07 — Gemini external check, pass 2 (on the final, length-expanded + style-fixed draft)

Context: the initial draft (pass 1, HL 90) was under the mandatory ~1000-word guide length, so it was
expanded with sourced material only. The expanded draft was re-checked (HL 85) and then given ONE fresh
step-7b Humaniser pass applying Gemini's safe style recs (functional hero ALT text; broke the "if/then"
intro symmetry; removed a wrap-up bow sentence). No facts, numbers, links, RG lines, disclosures, dates or
[VERIFY] flags touched.

Normalized: verdict „Likely human-written, 85% confidence" → human-likeness = **85** → **PASS** (≥80).

## Keep-best ledger
- pass 1 (initial SHORT draft): HL 90 — PASS, but NOT length-compliant (≈684 words vs ~1000–1500 brief) → superseded (07-gemini-check-1.md).
- pass 2a (expanded draft, pre style-fix): HL 85 — PASS.
- pass 2b (expanded + step-7b style fixes): HL 85 — PASS → **KEPT** (equal HL, objectively cleaner: ALT leakage, if/then hook and one wrap-bow removed).
- content-queue gemini = `human 85`. Humaniser-driven passes used: 1 (≤ MAX 2).
- „Илюстративно" labels retained on both illustrative figures: brand REQUIRES illustrative figures marked as such (documented guardrail in markets/bg/author.md), so this is compliance, not a tell to strip.
- [VERIFY] tags flagged by Gemini as a process point and correctly NOT removed — they STAY for the human at Step 6.

---

## VERBATIM GEMINI VERDICT (pass 2b — final draft)

**Verdict: Likely human-written (or heavily human-edited AI), 85% confidence.**

This is an exceptionally strong piece of content. If an LLM wrote this, it was guided by a masterful prompt and heavily edited by a native speaker. The text features highly idiomatic Bulgarian ("груб залък", "мести откъде идват парите", "балансът пак ще подскача еднакво нервно") and a grounded, almost cynical tone regarding gambling math ("шансът да го докоснете е нищожен", "математиката работи за казиното"). AI typically struggles to produce this level of anti-hype realism out-of-the-box.

However, beneath the excellent vocabulary, there are a few structural "tells" and formulaic rhythms that occasionally trigger AI detection algorithms or read as slightly robotic.

Here are the specific patterns flagged and how to smooth them out.

### 1. Pattern: Repetitive Transitional Signposting
LLMs often latch onto a specific, slightly formal transition word when explaining concepts and reuse it across different sections as a structural crutch.

*   **Flagged text:**
    *   *"Илюстративно, при залог 1 € обикновеното купуване..."* (Под "Две копчета за купуване...")
    *   *"Илюстративно: при обявен RTP около 96%..."* (Под "RTP: коя версия...")
*   **Recommendation:** Keep the first one, but change the second instance to a more conversational phrase to break the mechanical repetition.

### 2. Pattern: The "Neat Bow" Paragraph Ending (Over-comparison)
*   **Flagged text:** *"...така че един и същ символ едновременно може да ви плати на момента и да ви прати в бонуса. В оригинала тези две роли са разделени и близалката отговаря само за втората."*
*   **Recommendation:** Delete the bolded sentence entirely.

### 3. Pattern: The "If X, then Y" Recommendation Template
*   **Flagged text:** *"Ако харесвате оригинала заради ритъма... Ако предпочитате повече контрол..."*
*   **Recommendation:** Break the formulaic "Ако... Ако..." structure into declarative observations.

### 4. Pattern: Staccato / Bullet-Point Phrasing
*   **Flagged text:** *"Супер скатерът върши и втора работа. Той се брои към скатерите, които пускат безплатните завъртания..."*
*   **Recommendation:** Combine these into a single, fluid sentence.

***

**Process Note on Hard Rules:**
The responsible gambling language, 18+ markers, and the affiliate disclosure (including the specific 2026 legal reference) are perfectly integrated. Furthermore, the `[VERIFY: ...]` tags have survived to this stage. As per instructions, I am noting their presence as a process issue (they need to be resolved by the editorial/upload team before publishing), but no recommendations have been made to alter or remove them.

*(Note: residual recs above are NON-blocking at PASS 85 and were NOT further applied — keep-best forbids over-editing that risks voice/score; and the „Илюстративно" labels are a required compliance marker, not a tell.)*
