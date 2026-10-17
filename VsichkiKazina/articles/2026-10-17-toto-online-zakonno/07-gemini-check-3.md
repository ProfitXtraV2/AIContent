# Step 7 — Gemini cross-model check · PASS 3 (after humaniser pass 2) + KEEP-BEST decision

**Script:** `python3 scripts/gemini_check.py 05b-final-draft.md`
**Input version:** 05b after humaniser pass 2 (killed „не X, а Y" contrast, softened „цената е" closer, reduced colon-gluing, integrated link signposting)

## Verdict (verbatim, normalized)
**"Shows AI patterns (heavily constrained/prompt-engineered AI), 75% confidence."**
→ human-likeness = 100 − 75 = **25**

"This article is highly disciplined. It successfully avoids the most egregious AI hallmarks — no flowery language, no hyperbolic adjectives, no cliché introductions. However, it reads like an advanced LLM given strict negative constraints… overly sterile, rigidly structured."

Notable: Gemini now flags the very idiom it PRAISED in checks 1–2 („няма да опрете до затворена врата") and the closer it already made me soften — textbook whack-a-mole / adversarial-detector goalpost relocation on dry legal/procedural content.

## KEEP-BEST LEDGER (human-likeness)
| version | what | HL |
|---|---|---|
| pass 0 | baseline post-5b (Brand Gate output) | **35** ← HIGHEST |
| pass 1 | applied check-1 recs (removed summary/signposting/filler/truism) | 30 |
| pass 2 | applied check-2 recs (contrast/colons/links/soften) | 25 |

Each humaniser pass LOWERED the measured score (35 → 30 → 25). MAX_GEMINI_PASSES = 2 reached.

## DECISION (mandatory keep-best)
Restore and ship **pass 0** (the highest-HL version, HL 35). Final 05b = baseline post-Brand-Gate draft. The two humaniser passes are preserved in git history + checks 1–3 as the audit trail, but NOT kept as the final text (a later, lower version is never kept just because it came last).

- gemini column: **ai 65** (HL 35 < 80 → `ai <100−hl>` = ai 65).
- Human editor attention advised: the detector is noisy/adversarial on dry statute+procedure content (same pattern as vk-0063/0264/0279/0282); facts, flags, RG and disclosures are all correct and untouched. The brand's own confirmed tells (the single „не X, а Y" contrast, some colon-gluing) remain in the kept pass-0 version — a light human voice polish can remove them without touching any fact.
