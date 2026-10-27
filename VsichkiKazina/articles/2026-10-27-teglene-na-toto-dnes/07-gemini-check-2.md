# 07 — Gemini text check, pass 2 (after humaniser pass 1) · vk (теглене на тото днес)

Command: `python3 scripts/gemini_check.py .../05b-final-draft.md`
Normalized human-likeness: **85** (verbatim: „Likely human-written (or heavily human-edited), 85% confidence.") → PASS (≥ 80), but LOWER than baseline.

## Verdict (verbatim, excerpt)
**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**
Reads exceptionally well; specific practical knowledge (the 18:40–19:10 site-down window), idiomatic Bulgarian, distinct editorial voice. New flags this pass: rhetorical cost-contrast („безплатно… не е безплатно"), internal-link signposting („сме писали отделно в…"), and slightly poetic phrasing. These existed in the baseline too; the detector is noisy and relocated its goalposts.

## Keep-best ledger (MANDATORY)
- Pass 1 (baseline, commit 3ee943e): **HL 90** (PASS).
- Pass 2 (humaniser pass 1): **HL 85** (PASS) — the applied recs did NOT raise the score; they lowered it.
- Highest HL seen = **90 (pass 1 / baseline)**.
- DECISION: KEEP BEST = pass 1. Revert 05b to the baseline version (restore from commit 3ee943e). Do NOT keep the later, lower pass-2 version.
- MAX_GEMINI_PASSES=2 reached. Final `gemini` column: **human 90**.

Note: Gemini's recs are style-only and advisory; the baseline already passed well above the gate. The link phrasing it dislikes is the brand's standard, honest internal-link style (also present in the live sibling vk-0297). No facts, numbers, RG lines, disclosures or [VERIFY] touched in either version.
