# 07 — Gemini cross-model check · PASS 2 (after humaniser pass 1)

Model: gemini-3.1-pro-preview · script: scripts/gemini_check.py · exit 0
Verdict raw: **"Shows AI patterns (Likely AI-generated with heavy human editing), 75% confidence."**
Normalized HUMAN-LIKENESS = 100 − 75 = **25** → still below 80 → apply humaniser pass 2 (final in budget).

Note: score identical to pass 1 (25). Detector is noisy and surfaces DIFFERENT nitpicks each round
(pass 1 praised „Илюстративно" as natural human hedging; pass 2 flags the same word as clunky).
Recs this round are conservative, voice- and number-safe, so applying them once more is low-risk.

## Verbatim Gemini output

**Verdict: Shows AI patterns (Likely AI-generated with heavy human editing), 75% confidence.**

This article is exceptionally well-localized for Bulgarian. It uses excellent, natural idioms ("не пипат", "проточва", "назрява") that usually escape basic AI translations. However, beneath the polished vocabulary, the structural skeleton is distinctly LLM-generated. It relies heavily on algorithmic pacing, dramatic signposting, binary "if/then" explanations, and didactic hand-holding—all classic hallmarks of AI copywriting.

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the text.

---

### 1. The "Dramatic Setup" (Signposting)
**The Flagged Passage:**
> "Затова всичко опира до едно: колко монети ще задържиш, преди респините да свършат."

**The Pattern:**
AI models love to end introductory paragraphs with a dramatic, colon-punctuated summary statement (e.g., "It all comes down to one thing:", "Ultimately, the goal is simple:"). It feels like a movie trailer voiceover rather than an informative article.

**The Recommendation:**
Remove the dramatic "всичко опира до едно:" framing. Simply state the objective of the round directly and conversationally, integrating it into the previous sentence.

### 2. Robotic/Academic Transitions
**The Flagged Passage:**
> "Илюстративно една такава стълбица може да изглежда като Мини 20x, Минор 50x..."

**The Pattern:**
"Илюстративно" is a clunky, direct translation of the AI-favorite transition "Illustratively" or "As an illustration." Human writers rarely use this word in Bulgarian when talking about slot machines; they just say "For example."

**The Recommendation:**
Replace "Илюстративно" with a natural conversational connector like "Например" (For example) or simply "Една типична стълбица изглежда така:".

### 3. Algorithmic / Binary Branching
**The Flagged Passage:**
> "Рундът свършва, когато или изтекат респините, или монетите запълнят цялата решетка. Изтекат ли респините, всички събрани стойности се сумират в едно плащане. Напълни ли се решетката преди това, обикновено пада горният джакпот..."

**The Pattern:**
This is the "If A, then X; If B, then Y" formulaic structure. AI often explains mechanics like a software manual or a flowchart, breaking down every possible binary outcome in perfectly symmetrical sentences.

**The Recommendation:**
Break the symmetry. Instead of repeating the two conditions mechanically, combine the thoughts to focus on the ultimate goal (filling the grid for the jackpot) and treat the expiration of respins as the standard default outcome.

### 4. Didactic Hand-Holding (The Preachy Warning)
**The Flagged Passage:**
> "...така че двете не бива да се бъркат."

**The Pattern:**
AI assumes the reader has zero reading comprehension and constantly inserts little warnings telling them how to think or what not to do (e.g., "It's important to remember," "Therefore, they should not be confused").

**The Recommendation:**
Delete the phrase entirely. You have already clearly explained the difference between *Wolf Gold* and *The Dog House*. Trust the reader to understand the contrast without explicitly instructing them not to confuse the two.

### 5. Repetitive Parallel Structure (Anaphora)
**The Flagged Passage:**
> "**Понякога това е** кеш стойност, кратна на залога, да речем 1x, 2x или 5x. **Понякога е** етикет за джакпот от няколко нива."

**The Pattern:**
LLMs frequently use parallel sentence structures to list options, essentially writing a bulleted list disguised as a paragraph. It creates a rhythmic, staccato "robot heartbeat" in the text.

**The Recommendation:**
Vary the syntax. Merge the two sentences or change the opening of the second sentence so they don't mirror each other perfectly (e.g., "Може да бъде кеш стойност... или пък етикет за джакпот...").

---

*Note on Compliance:* The responsible gambling language, 18+ markers, and affiliate disclosures at the bottom of the text, as well as the RG integration in the final paragraph, are perfectly placed. Per your instructions, these have been ignored in the critique and should remain exactly as they are.

## Disposition for humaniser pass 2
- §1 dramatic colon setup „всичко опира до едно:" → restated directly, no colon reveal.
- §3 „Илюстративно" → „Например"; anaphora „Понякога… Понякога…" → „Понякога… Друг път…".
  Figures stay marked illustrative (Например + „да речем" + SVG caption „примерни"). Compliance ok.
- §4 binary branch smoothed: expiration = default outcome, full grid = the rarer jackpot case.
- §4 „така че двете не бива да се бъркат." deleted (didactic hand-holding); sentence ends on the fact.
- UNTOUCHED: numbers, 4 internal links, RG/18+, disclosures, dates, byline, brand.
