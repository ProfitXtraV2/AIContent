# 07 — Gemini external check — PASS 3 (after humaniser pass 2) · FINAL (cap reached)

**Date:** 2026-10-16 · **Script:** `scripts/gemini_check.py 05b-final-draft.md`
**Verdict (verbatim):** Shows AI patterns, 85% confidence.
**Normalized human-likeness:** 100 − 85 = **15**.

## KEEP-BEST DECISION (MAX_GEMINI_PASSES=2 reached)
| version | verdict | human-likeness |
|---|---|---|
| baseline 05b | Shows AI patterns, 85% | 15 |
| humaniser pass 1 | Shows strong AI patterns, 85% | 15 |
| humaniser pass 2 (THIS) | Shows AI patterns, 85% | 15 |

All three tie at HL **15**. The Gemini style detector stays flat on this dry, statute-anchored
regulatory explainer and relocates its flags each pass (circular callback → neat-bow summary →
micro-conclusions/signposting) without the score ever moving — the same noisy/adversarial
behaviour recorded on prior legal/RG explainers (vk-0260, vk-0279, vk-0055, vk-0171). Both
humaniser passes applied genuine, legitimate de-AI edits (broke the circular narrative, removed the
"зад кулисите" idiom, cut summary signposts, de-dramatized headings, trimmed filler) and improved
readability while preserving every number, ЗХ article, [VERIFY] flag, link and footer.

**KEEP:** humaniser **pass 2** — equal-highest HL (15) AND the most polished version; it is NOT a
lower later version, so keep-best is satisfied (never keep a later *lower* version — this one is equal).
**gemini column:** `ai 85` (below 80 after cap → winning version's own verdict). Human editor advised
for a style polish; the 3 [VERIFY] flags still require human resolution at Step 6.

---

## Gemini verbatim output (pass 3)

**Verdict: Shows AI patterns, 85% confidence.**

Highly informative, grammatically flawless, correct legal terminology, but the structure relies on
classic LLM patterns: tautological wrap-ups (ending sections by restating the paragraph), didactic
signposting (telling the reader how to feel about a fact), and symmetrical/forced rhythm.

Flagged: micro-conclusions („Законната зала няма да изникне до входа на гимназия..."; „В легалната
зала това предупреждение го има; липсата му е в разрез със закона."; „Зала, която покрива всички
тези изисквания, работи законно."); didactic signposts („Това е първата проверка и най-важната...";
„Самата разлика между 750 000 и 1 500 000 лв. е и най-прекият законов знак..."); symmetrical phrasing
(„За наземната зала това означава...; за организатора е задължение...").

Recommendations: amputate micro-conclusions, remove importance signposts, break symmetrical phrasing,
trim the summary sentences in the final section.

*(Gemini note: several [VERIFY] flags survived — left untouched per the rules; to be resolved by the human at Step 6.)*
