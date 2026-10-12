# 07 — Gemini Step-7 external check — PASS 2 (after humaniser pass 1)

Tool: `python3 scripts/gemini_check.py 05b-final-draft.md` · exit 0 · date 2026-10-12

**Normalised result:** Verdict „Shows AI patterns, 85%" → HUMAN-LIKENESS = 100 − 85 = **15** (< 80).

Keep-best tracking so far: initial 05b **HL 25** > humaniser pass 1 **HL 15**. The detector relocated its goalposts (pass-1 complaints were signposting/idioms/"Накратко"; pass-2 complaints are entirely new: the word „ръб"=edge and „Затова" transitions, which are standard BG). Noisy whack-a-mole detector, as seen on vk-0063/vk-0266. One more humaniser pass allowed (MAX_GEMINI_PASSES=2) before keep-best.

---

## VERBATIM GEMINI VERDICT + RECOMMENDATIONS

**Verdict: Shows AI patterns, 85% confidence.**

This article is highly structured, grammatically flawless, and does an excellent job of adhering to compliance and formatting rules. However, it exhibits classic LLM translation quirks, repetitive structural loops, and formulaic paragraph resolutions.

### 1. Literal Translation / Anglicisms (The "Edge")
„ръбът"/„ръб" is a literal translation of English "edge"; sounds unnatural. Flagged: „...по-голям е ръбът, който можеш да използваш.", heading „Колко голям е ръбът в действителност", „Ръбът се проявява върху огромен брой ръце...", „Ръбът на брояча е функция на дълбокото проникване...", „Нулево проникване дава нулев ръб...".
Recommendation: replace „ръбът"/„ръб" with „предимство" / „математическо предимство".

### 2. The "Затова" Wrap-Up (formulaic signposting)
Repeated „Затова" tying a bow on each paragraph. Flagged: „Затова се минава към реален брой...", „Затова ти трябва банкрол...", „Затова всяка оферта за „система..."", „Затова „система...“ няма как да съществува...".
Recommendation: break the „Затова" loop; state the action/fact directly.

### 3. Echoing / repetitive thematic summaries
The online-system conclusion is stated twice (once in „Защо броенето умира онлайн", once in the legality section).
Recommendation: delete the second instance.

### 4. Narrated emotion / theatrical flair
„...моментът не е твой."
Recommendation: make it objective, e.g. „предимството се връща при казиното" / „вероятността за успех намалява".

### Process & compliance note
[VERIFY] tags, RG language, 18+ markers, licensing disclosures: excellent and correctly placed. Do NOT touch/remove them. (Confirmed — they stay.)
