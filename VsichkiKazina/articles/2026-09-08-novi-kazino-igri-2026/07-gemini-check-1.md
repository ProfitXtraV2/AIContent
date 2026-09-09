# 07 — Gemini external check · pass 1 (initial 05b)

Model: gemini-3.1-pro-preview · run 2026-09-08 · article: 2026-09-08-novi-kazino-igri-2026
Verdict normalization: "Shows AI patterns, 75%" → **human-likeness = 100 − 75 = 25** → needs changes (below 80).

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 75% confidence.**

While this article is highly informative, grammatically flawless, and contains excellent localized context (which suggests good prompting or human outlining), the underlying skeleton relies heavily on classic Large Language Model (LLM) rhetorical devices. It suffers from a didactic tone, formulaic paragraph conclusions, and the classic AI tendency to over-explain concepts using balanced dichotomies and grand summary statements.

Here is the breakdown of the specific AI patterns detected and how to humanize them.

### 1. The "Ultimate Takeaway" Framing (Formulaic Summary)
**The Pattern:** AI models struggle to end articles naturally. They almost always rely on a grand, sweeping summary statement, often framed as "If you only remember one thing..." or "Ultimately..."
**The Flagged Text:** *"Ако от 2026 трябва да остане едно изречение: форматът се сменя, математиката не."*
**The Recommendation:** Remove the dramatic "If one sentence should remain from 2026" setup. It sounds like a high school essay conclusion. Just state the core thought directly—start the concluding paragraph immediately with the fact that while formats change, the math remains the same.

### 2. The "It's Not X, It's Y" Balanced Dichotomy
**The Pattern:** When explaining two different concepts (like high vs. low volatility), AI avoids taking a stance by using a philosophical, balanced dichotomy to wrap up the thought.
**The Flagged Text:** *"Въпросът не е коя игра е „по-добра", а коя пасва на бюджета и търпението ви."*
**The Recommendation:** Drop the philosophical "The question isn't which is better" framing. Make it a direct, practical instruction. Tell the reader directly to match the game's volatility to their bankroll and session length, rather than framing it as a profound realization.

### 3. The "Simple Fact" Moralization (Preachy Tone)
**The Pattern:** AI frequently ends paragraphs with a moralizing or grounding statement, often using phrases like "doesn't change the fact that" or "the reality remains." It feels overly preachy for a casino guide.
**The Flagged Text:** *"Новото име и лъскавата графика не променят простия факт, че всяко от тези заглавия е построено така, че операторът да излиза на печалба в дългосрочен план."*
**The Recommendation:** Cut the cliché *"не променят простия факт, че"* (do not change the simple fact that). You can deliver the exact same warning about the operator's long-term profit margin directly and conversationally without the dramatic, finger-wagging preamble.

### 4. The Meta-Explanatory Crutch
**The Pattern:** When defining terms, AI often uses meta-language—pointing at its own words to explain a concept, which reads as overly academic.
**The Flagged Text:** *"Думите тук са „средно" и „в дългосрочен план": една вечер спокойно завършва далеч над или далеч под това число..."*
**The Recommendation:** Remove the meta-commentary *"Думите тук са..."* (The words here are...). Instead of pointing at the vocabulary, just merge the explanation directly into the sentence (e.g., explain that because RTP is a long-term average, a single evening can end far above or below it).

### 5. Staccato Openings (Signposting)
**The Pattern:** AI loves to open paragraphs with a very short, 3-to-4 word definitive sentence to "signpost" the topic before expanding on it.
**The Flagged Text:** *"Разработчикът има значение."* (Followed immediately by *"Установен доставчик със заглавия..."*)
**The Recommendation:** Combine this staccato opening with the sentence that follows it. A human writer would typically weave the importance of the developer directly into the comparison between established providers and anonymous studios, rather than isolating it as a standalone thesis statement.

---

**A Note on Process & Compliance:**
I see a **[VERIFY: допустимост на bonus buy при лицензирани BG оператори]** flag in the text, as well as mandatory 18+ markers, responsible gambling boilerplate, and affiliate disclosures. Per your hard rules, I have not touched, altered, or suggested removing any of this language. The presence of the `[VERIFY]` tag indicates this draft is still in the editorial pipeline—ensure your fact-checking team resolves that specific prompt before final publication.

## Decision
human-likeness 25 < 80 → iterate. Apply recs 1–5 via a FRESH Humaniser pass (step-7b), preserving every untouchable (numbers, links, RG lines, 18+, disclosures, dates, byline, brand, the [VERIFY] flag). Then re-check. Record best-of.
