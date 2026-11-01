# 07 — Gemini check, pass 1 (baseline 05b)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Normalized human-likeness: **75** ("Likely human-written, 75% confidence") → below GEMINI_TARGET_CONFIDENCE (80); needs changes.

## Gemini verbatim verdict + recommendations

**Verdict: Likely human-written (or heavily human-edited), 75% confidence.**

This article is highly readable and features excellent, natural Bulgarian phrasing that AI rarely generates organically (e.g., "спасителни пояса", "не каса", "върви по една и съща рецепта"). The author's voice is distinct and authoritative. However, the text still leans on a few classic AI structural crutches—specifically in its transitions, categorizations, and conclusion—that give it a slight synthetic aftertaste.

### 1. Pattern: Intro Signposting (The "In this article" trope)
* **The Quote:** *"Долу са правилата на предаването, както и къде се играе безплатната онлайн версия, ако искате сами да опитате стълбата."*
* **The Recommendation:** Delete this sentence entirely. The preceding sentence ("Печели се със знание: няма зарове, няма залог и изходът не опира до късмет.") is a fantastic, punchy hook. Let it stand alone.

### 2. Pattern: Binary/Categorical Setup (The "Two things" trope)
* **The Quote:** *"Търсещите „стани богат онлайн“ обикновено имат предвид едно от две неща. Едното е да гледат предаването... Другото, по-интересното, е да играят сами."*
* **The Recommendation:** Break the formulaic "one is X, the other is Y" structure. Combine into a single fluid sentence that acknowledges Voyo viewers but pivots to the browser game, removing the "едно от две неща" framing.

### 3. Pattern: The "Wrap-up Bow" (Forced Call-to-Action)
* **The Quote:** *"Правилата се учат за една вечер пред телевизора. ... Седнете и опитайте."*
* **The Recommendation:** Cut the final sentence ("Седнете и опитайте."). Ending on "...понякога само ти се струва, че го знаеш." leaves a stronger, more human impact.

### 4. Process Issues (Flags & Prompts) — flagged, Gemini did not touch
* Unresolved `[VERIFY: ...]` tags survived into the draft. (KEEP — brand rule: they stay for human Step 6.)
* Raw image prompts in alt-text (hero). (FIX — rewrite as descriptive alt-text.)
* Minor typo: *"честно казана"* should be *"честно казано"*. (FIX.)

## Decision
Apply recs 1–3 (style, preserve all untouchables), the typo fix, and the hero alt-text cleanup via a fresh Humaniser pass (step-7b). Keep [VERIFY] flags. Re-run Gemini; keep the highest human-likeness version seen.
Baseline HL = 75.
