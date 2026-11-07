# 07 — Gemini check, pass 2 (on 05b after humaniser pass 1)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-29-efbet-liga-format-otbori/05b-final-draft.md`

**Verdict: Shows strong AI patterns, 85% confidence.** → human-likeness = 100 − 85 = **15**
(LOWER than the initial draft's 25 → noisy/adversarial detector; keep-best currently = initial draft.)

---

### 1. Circular Padding (Redundancy)
The official-name-vs-sponsor-name point is explained ~three times in the first 100 words (H1 intro + first H2).
Recommendation: consolidate the intro and the first H2 into one opening; state it once.

### 2. The Didactic Disclaimer Loop (Preachiness)
„check official sources, not last year's numbers" repeated three times:
- „…за актуалния формат винаги гледай официалния регламент, а не миналогодишните числа."
- „Най-сигурният начин да не сгрешиш е да провериш актуалния носител на правата…"
- final paragraph „…регламентът на БФС и ПФЛ, не миналогодишните числа."
Recommendation: keep ONE instance; delete „не миналогодишните числа" and „Най-сигурният начин да не сгрешиш".

### 3. Unnatural Phrasing / Translation Idioms
- „се е местило" → unnatural for rule/format changes; use „се е променяло / варирало".
- Heading „На пари, отдалеч" reads forced.
Recommendation: fix the verb; make the betting/RG heading more standard.

### 4. The Orphaned Summary (Formulaic Structure)
The final paragraph is a tacked-on essay-style summary after the RG section.
Recommendation: delete it; end naturally on the RG advice.

Note (Gemini): RG disclosures, 18+ markers, affiliate text, author bio are perfectly formatted and must remain exactly as they are.

---
## Decision
Apply the genuine improvements (consolidation, de-looping, verb fix, heading, delete orphaned
summary) as humaniser pass 2 — these tighten the article for a human reader regardless of the noisy
score. Then re-check (check 3) and apply the mandatory keep-best across {initial 25, pass1 15, pass2}.
