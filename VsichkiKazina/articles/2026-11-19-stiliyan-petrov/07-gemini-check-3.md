# 07 — Gemini text check · pass 3 (after humaniser pass 2) — FINAL, cap reached

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Exit: 0

## Verdict (verbatim)
**Verdict: Shows AI patterns, 75% confidence.**
→ human-likeness = 100 − 75 = **25**.

## Trajectory (keep-best)
- INITIAL draft      → check 1: AI patterns 90% → HL **10**
- Humaniser pass 1   → check 2: AI patterns 70% → HL **30**  ← HIGHEST
- Humaniser pass 2   → check 3: AI patterns 75% → HL **25**

MAX_GEMINI_PASSES (2) reached. Pass 2 LOWERED human-likeness (30 → 25), so per the mandatory
keep-best rule the final `05b` is reverted to the **pass-1 version (HL 30)**, not this last one.

## Note on the detector
Classic noisy-detector behaviour on football-biography copy (same pattern logged on vk-0314
Ефбет Лига, vk-0063, and vk-0338 ПСЖ, which also capped at HL ~30). Each pass applied genuine
Gemini style recs (removed prompt-echo, formulaic transitions, „beyond statistics" trope, meta-
pivot), yet the confidence oscillates 70↔75 and never clears 80. No fact/RG/disclosure/date was
touched in any pass. Below 80 after the cap → gemini column = `ai 70` (pass-1 winner's own
verdict) and the article is flagged for human review at Step 6.

→ Keep-best action: restore pass-1 `05b` (HL 30) as final; record `ai 70`.
