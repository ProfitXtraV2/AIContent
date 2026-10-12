# 07 — Gemini Step-7 external check — PASS 1 (initial 05b)

Tool: `python3 scripts/gemini_check.py 05b-final-draft.md` · exit 0 · date 2026-10-12

**Normalised result:** Verdict „Shows AI patterns, 75%" → HUMAN-LIKENESS = 100 − 75 = **25** (< 80 target → needs changes).

Note: Gemini's detector partly flags the bracketed `[VERIFY: …]` tags themselves as AI-tells. Per pipeline, [VERIFY] flags are DESIGNED to stay for the human and are NOT removed. Recommendations are style-only; facts/RG/disclosures/flags untouched.

---

## VERBATIM GEMINI VERDICT + RECOMMENDATIONS

**Verdict: Shows AI patterns, 75% confidence.**

While the article is highly polished, factually dense, and avoids the most egregious AI fluff (like "In the fast-paced world of online casinos..."), it still relies heavily on structural AI tells. It uses classic LLM signposting, translated English idioms, and the distinct "preachy/moralizing" wrap-up sentences that models like GPT-4 and Claude use when instructed to write about gambling or "systems."

Additionally, there is a clear **process issue**: multiple `[VERIFY: ...]` tags have survived into this "finished" draft. Per your instructions, I am flagging this for your editorial team to resolve, but I will not touch them.

### 1. Pattern: Didactic Signposting & Meta-Commentary
- „Оттук нататък темата е само броенето."
- „Знаците не са избрани случайно."
- „Плиткото проникване е и първият намек защо онлайн броенето няма да проработи."
- Recommendation: Delete the meta-commentary. Just start talking about counting; start the paragraph by explaining why high cards favor the player; let the online section introduce itself.

### 2. Pattern: Translated AI Idioms (English phrasing in Bulgarian)
- „Дълбочината на проникване (penetration) е лостът на цялата техника." (reads like "the lever of the whole technique")
- „Тук проникването затваря кръга." (direct translation of "comes full circle")
- Recommendation: Replace with natural Bulgarian. Instead of „лостът", use „основата" or „ключът"; instead of „затваря кръга", state the logical conclusion plainly.

### 3. Pattern: The "Moralizing/Preachy" Wrap-Up
- „Който го продава като билет за бързи пари, продава илюзия."
- „…и единственото сигурно в такава оферта е, че печели онзи, който ти я продава."
- Recommendation: Tone down the dramatic punchlines. End on the hard facts (the math makes it impossible) rather than philosophical warnings.

### 4. Pattern: Formulaic "In Short" (Накратко) Summaries
- The entire „Накратко" section reiterates points already made.
- Recommendation: Consider cutting „Накратко"; let the article end after the legal section into the RG disclaimer.

### Process Note: Unresolved Editorial Tags
- `[VERIFY: Торп, Beat the Dealer, 1962]`, `[VERIFY: точният процент…]`, `[VERIFY: обща формулировка…]`
- Recommendation: left untouched (correct — flags stay for the human per pipeline design).
