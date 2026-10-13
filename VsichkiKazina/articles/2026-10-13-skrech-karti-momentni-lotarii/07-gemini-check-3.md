# Step 7 — Gemini cross-model check — PASS 3 (after Humaniser pass 2) — FINAL / cap reached

**Normalized human-likeness: 25** (Gemini verdict "Shows AI patterns, 75% confidence" → 100 − 75 = 25).

MAX_GEMINI_PASSES (2) reached. **KEEP-BEST decision:**
| version | human-likeness |
|---|---|
| pass 0 (initial 05b) | **35 ← BEST, kept** |
| pass 1 (humaniser 1) | 20 |
| pass 2 (humaniser 2) | 25 |

The final `05b-final-draft.md` is restored to the **pass-0** version (highest human-likeness seen). Both Humaniser passes LOWERED the score — the detector is noisy and relocates its goalposts each pass (it re-flagged the "На практика" heading it had itself asked us to create, then flagged the trimmed conclusion as "semantic satiation"). This is the known whack-a-mole behavior documented in markets/bg/author.md. Keeping the best-scoring version per daily-run Step-7 keep-best mandate.

`gemini` column value: **ai 65** (the winning pass-0 version's own verdict: "Shows AI patterns, 65%"). Below 80 → human editor attention advised at Step 6; the piece is factually strong (gate 94/100) and the high AI-confidence is detector noise, not a content defect.

Model: gemini (scripts/gemini_check.py). Date: 2026-10-13.

---

## Gemini verbatim verdict + recommendations (pass 2 output)

**Verdict: Shows AI patterns, 75% confidence.**

While this article is highly factual, well-researched, and accurately cites Bulgarian gambling law (ЗХ), its underlying skeleton relies heavily on classic LLM writing patterns: semantic satiation (repeating the core concept in slightly different ways), dramatic staccato transitions, and a symmetrical formulaic summary.

### 1. Semantic Satiation (over-explaining the core premise)
Flagged: "Резултатът… вече съществува"; "под него стои резултат, който е отпечатан там отдавна"; "всичко вече е преброено"; "никое действие на играча не мести изхода"; "просто се появява вече готовият отговор"; "събитието… вече е минало"; "предварително отпечатаните резултати"; "резултатът върху конкретния билет е вече отпечатан". Rec: state the mechanic once or twice, strip 4-5 redundant variations.

### 2. Staccato Rhythm & Dramatic Transitions
Flagged: "В тази разлика няма измама."; "Скреч е само външността."; "Разликата не е само юридическа. Тя е и в математиката."; "Друго няма да ви каже." Rec: blend into surrounding text with natural conjunctions.

### 3. Didactic / Moralizing Tone
(telling the reader how to perceive probability rather than presenting it) — recommendations continue in the same vein.

### Keep-best note
Because applying these recommendations across two passes dropped human-likeness (35 → 20 → 25), no further passes are run (cap reached) and the highest-scoring version (pass 0) is kept. Over-editing strips voice; the detector score is noisy. Flags, RG language, 18+ and facts untouched throughout.
