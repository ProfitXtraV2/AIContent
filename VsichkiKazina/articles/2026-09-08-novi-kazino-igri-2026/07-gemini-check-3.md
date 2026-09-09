# 07 — Gemini external check · pass 3 (re-check after Humaniser pass 2 — FINAL)

Model: gemini-3.1-pro-preview · run 2026-09-08 · article: 2026-09-08-novi-kazino-igri-2026
Verdict normalization: "Shows AI patterns, 65%" → **human-likeness = 100 − 65 = 35**.

## KEEP-BEST LEDGER (mandatory)
| version | Gemini verdict | human-likeness |
|---|---|---|
| initial 05b (check 1) | Shows AI patterns, 75% | 25 |
| Humaniser pass 1 (check 2) | Shows strong AI patterns, 85% | 15 |
| **Humaniser pass 2 (check 3) — KEPT** | **Shows AI patterns, 65%** | **35 (highest)** |

MAX_GEMINI_PASSES = 2 reached. Highest human-likeness seen = **35 (pass 2)** = the current 05b, so pass 2 is KEPT (no revert). Ends below 80 after the cap → content-queue `gemini` column = **ai 65** (the kept version's own verdict, verbatim scale).

Context: Gemini's AI-pattern score is low and high-variance on this piece (25 → 15 → 35 across three reads; the same instability was recorded on vk-0008, 25–90). The internal Brand Gate passed it 93/100 with zero criticals and the internal Humaniser rated it ~50/60 HUMAN-LIKE. Several of Gemini's earlier recommendations conflicted with mandatory brand rules (bullets, removing the required worked example, removing the [VERIFY] flag) and were correctly rejected. The compliant subset was applied across two passes; pass 2 is the best result and is handed to the human at Step 6. No further passes permitted by policy.

## Gemini verbatim verdict + recommendations (pass 2 re-check)

**Verdict: Shows AI patterns, 65% confidence.**

This article is actually quite good and features several strong, human-sounding observations (e.g., describing Megaways as "повече визуален шум, отколкото сметка" and hold-and-win as "по-бавно и по-нервно"). However, the structural skeleton and the transitional phrasing heavily betray AI involvement. It reads like a piece where a human expert provided excellent core insights, but an LLM was used to stitch them together, resulting in classic AI didacticism, melodramatic transitions, and run-on sentences.

Here are the specific patterns that triggered this assessment, along with actionable recommendations to fix them.

### 1. Clunky Conversational Filler (Word-Looping)
**The Passage:** *"С това си струва да започнете, преди да завъртите нещо, пуснато тази седмица, само защото е пуснато тази седмица."*
**The Pattern:** LLMs often try to mimic a conversational, engaging tone but end up looping words awkwardly to fill space. The repetition of "пуснато тази седмица" feels like a robotic attempt at emphasis rather than natural human phrasing.
**Recommendation:** Tighten this sentence. Suggest removing the repetitive second clause ("само защото е пуснато тази седмица") so the introduction ends on a punchier, more direct note.

### 2. Didactic Wrap-Ups (The "Moral of the Story" Pattern)
**The Passages:**
*   *"Съобразете волатилността с бюджета си и с това колко дълго планирате да играете."* (End of Volatility section)
*   *"Колкото и ново да е името и лъскава графиката, всяко от тези заглавия е построено така, че операторът да излиза на печалба в дългосрочен план."* (End of Formats section)
**The Pattern:** AI struggles to end paragraphs organically. It almost always defaults to a summarizing, preachy, or advisory concluding sentence that tells the reader what to do or reminds them of a "lesson."
**Recommendation:** Delete these generic wrap-up sentences. The paragraphs are strong enough to end on their factual points (e.g., ending the formats section on the point about fast-paced crash games emptying budgets quickly). You don't need the AI to summarize the moral of the paragraph.

### 3. Melodramatic Signposting / Narrated Emotion
**The Passage:** *"Тук е и рискът, който идва с новостта. А блясъкът на всяко ново заглавие е точно това, за което да сте нащрек."*
**The Pattern:** LLMs frequently use overly dramatic, slightly ominous transitions to move between concepts (e.g., "Herein lies the risk," "But beware the shine"). It feels like a narrator in a documentary rather than a casino guide.
**Recommendation:** Cut the theatrical buildup. Suggest starting that thought directly with the factual observation that follows it: "Свежата графика и усещането..." This removes the AI "throat-clearing" and keeps the tone professional.

### 4. The "Breathless Compliance" Run-On Sentence
**The Passage:** *"Хазартът не е финансова стратегия, а платено развлечение с известна предварително цена, затова, ако ще пробвате ново заглавие, направете го с пари, които можете да загубите изцяло, и с лимити за депозит и загуба, зададени преди първия депозит, не след него."*
**The Pattern:** When prompted to include responsible gambling warnings, AI tends to cram every single compliance directive into one massive, comma-spliced run-on sentence.
**Recommendation:** Do not remove any of this responsible gambling language—it is vital and required. However, suggest splitting this massive block into two or three shorter, distinct sentences. For example, place a period after "цена" and start a new sentence. This will make the warning read like a serious human directive rather than an AI data dump.

***

**Process Note:** The article correctly retains the `[VERIFY: допустимост на bonus buy при лицензирани BG оператори]` flag and all required 18+/Responsible Gambling boilerplate text at the bottom. These should remain exactly as they are for the final editorial/compliance review.
