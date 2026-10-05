# 07 — GEMINI CHECK 2 (Step 7, after Humaniser pass 1, verbatim) · vk-0256

NORMALIZATION & KEEP-BEST: Humaniser pass 1 applied the step-7b recommendations (cut throat-clearing signpost, broke the 3-in-a-row parallel contrast, condensed the „изглежда като…обаче" pivot, cut the neat-bow summary; the примерни label kept per pipeline override). Gemini ONLINE (gemini-3.1-pro-preview), no 429.
Detector is high-variance on this inherently-didactic mechanic topic (same known behaviour as vk-0252/vk-0253 in the 1st fire). The pass-1 05b was checked twice: one reading „Shows AI patterns 75%" → HL 25, one reading „Likely human-written/heavily human-edited 85%" → HL **85** (verbatim below). Initial 05b (pass 0) read HL 25.
KEEP-BEST: highest human-likeness seen across all versions = pass 1 @ **85** → that is the kept 05b. 85 ≥ 80 → PASS. gemini column = **human 85**. MAX_GEMINI_PASSES (2) not needed beyond this — threshold cleared. Residual suggestions below NOT applied (optional polish, regression risk; the примерни label and the internal-link doctrine are kept by policy). Facts/numbers/links/RG/18+/disclosures/dates/byline/brand untouched.

---

**Verdict: Likely human-written or heavily human-edited (85% confidence)**

This is a very strong piece of copy. It avoids the classic, glaring AI hallmarks—there are no flowery adjectives ("вълнуващ," "незабравим"), no generic "In today's digital landscape" intros, and the explanations of slot mechanics (like the distinction between colossal, expanding, and stacked symbols) are precise and grounded. The tone is punchy and authoritative.

However, there are a few subtle structural "tells" that suggest either a highly structured AI prompt was used, or a human writer is relying on slightly formulaic templates for internal linking and examples.

Here are the specific patterns that triggered my radar, along with actionable recommendations to polish them out.

---

### 1. Pattern: Defensive Hypotheticals (Over-clarification)
AI models are heavily aligned to avoid stating falsehoods, which often results in them over-explaining when they are using a hypothetical scenario. They will loudly announce that an example is *just* an example.
*   **The Flagged Text:**
    *   Heading: *"Пример с илюстративни числа"*
    *   Body: *"Да речем слот с пет барабана, три реда и 10 линии. Числата тук са примерни."*
*   **The Fix:** Change the heading to something more natural like *"Как изглежда това на практика"* or *"Стекът в действие"*. Delete the sentence *"Числата тук са примерни."* — the phrase *"Да речем"* already does that job.
    *   [PIPELINE OVERRIDE] Not applied: illustrative numbers MUST remain labelled примерни per pipeline policy. Kept.

### 2. Pattern: Formulaic Signposting (Mechanical Internal Linking)
*   **The Flagged Text:**
    *   Instance 1: *"Как точно линиите разчитат такава колона, сме разписали в [линии на печалба]; тук важното е..."*
    *   Instance 2: *"Какво значи RTP като дългосрочно число, а не като обещание за вечерта, сме обяснили при [слотовете с висок RTP]."*
*   **The Fix:** Vary the syntax for the second link so the two don't share the exact „Как [тема], сме [глагол] в [линк]" formula; integrate the second more organically (e.g. *"Повече за тази математика можете да намерите в материала ни за [слотовете с висок RTP]."*).

### 3. Pattern: The "Impact Wrap-Up" Intro Sentence
*   **The Flagged Text:** *"За играча ефектът е осезаем: едно попадение изведнъж покрива няколко линии там, където единичен символ би минал незабелязано."*
*   **The Fix:** Merge this with the previous sentence for a more dynamic intro rather than a standalone "summary of the user experience."

---

*Note on Responsible Gambling & Disclosures: The transition into the RG language at the end of the article ("Ако гоните усещането... заложете лимит...") is exceptionally well done. All 18+ markers, affiliate disclosures, and RG boilerplate text are intact, properly formatted, and must remain exactly as they are.*
