# 07 — Gemini Step-7 check · pass 3 (re-check after Humaniser pass 2) · vk-0285

**Date:** 2026-10-19
**Model:** gemini-3.1-pro-preview (patient 300s run; 120s script runs kept timing out today).
**Checked version:** 05b after Humaniser pass 2.
**Verdict (verbatim):** Shows AI patterns, 75% confidence.
**Human-likeness (normalized):** 100 − 75 = **25** → below target (80).

## Keep-best decision (loop ended at MAX_GEMINI_PASSES = 2)
| version | verdict (verbatim) | human-likeness |
|---|---|---|
| initial draft | Shows AI patterns, 65% | **35 — HIGHEST, KEPT** |
| humaniser pass 1 | Shows AI patterns, 85% | 15 |
| humaniser pass 2 | Shows AI patterns, 75% | 25 |

The detector is adversarial/noisy on this dry BG reference content: each pass flagged a DIFFERENT set
of sentences, and applying its own recommendations LOWERED the score (35 → 15), then a second,
brand-safe rewrite recovered only to 25 — still below the 35 of the untouched original, and pass 3 even
penalised the intro/conclusion consolidation it had implicitly invited. No version came near 80. Per the
mandatory keep-best rule ("the final 05b MUST be the version with the highest human-likeness seen, even
if that is the untouched original; NEVER keep a later, lower version"), the shipped 05b is reverted to
the **initial draft (HL 35)**. `gemini` column → `ai 65` (the winning version's own verbatim verdict).

Pass-3 recommendations are recorded for the human editor (Step 6) but NOT applied, since a 3rd humaniser
pass would exceed MAX_GEMINI_PASSES and the initial version already scores highest:
1. „Плъстмаса"/plastic motif + the budget warning repeat between Section 1 and the conclusion → consolidate.
2. Forced SEO bridge „…няма какво да „победиш"… докато в покер комбинациите…" → more natural next-step phrasing.
3. „Начинаещите често очакват… В действителност…" and „Няколко неписани правила спестяват неудобни моменти."
   buffer/signpost openers → start on the fact.
(These are style notes; the human owns final polish at Step 6. RG/18+/disclosures confirmed correct by
Gemini and must remain.)
