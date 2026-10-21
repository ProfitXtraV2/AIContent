# 07 — Gemini cross-model check · pass 3 (on 05b after Humaniser pass 2 / apply-recs)
Model: gemini-3.1-pro-preview (scripts/gemini_check.py) · run 24.09.2026

VERDICT (verbatim): **Predominantly human-written or heavily human-edited, 75% confidence.**
Normalized human-likeness = **75/100** (human-written branch → X = 75).
Below the 80 PASS target, but the HIGHEST of the three versions (pass-1 baseline 25, pass-2 15, pass-3 75).
Humaniser pass cap (2) reached → STOP. KEEP-BEST winner = this version (pass 2 humanised, hl 75).

Gemini praised human idioms it now reads as authentic: „Тук се къса най-често", „само добро намерение",
„парчето за едно сядане". Remaining residual notes (not applied — cap reached, and several conflict with
brand requirements / would risk figures): subheading echo in the самоизключване section, the reused
„наем/ток/храна" cluster, a couple of definitional openings, repeated „на трезва глава" idiom, and the
„един от най-опасните капани" phrase. Score jumped +50 vs the previous version, confirming the contrastive/
metaphor/summary edits were the right direction.

Compliance: Gemini's own note confirms the 18+ line, RG language and all disclosures are intact and must
stay exactly as they are (its only suggestion there was a formatting nicety, not a content change).
No untouchable altered across any pass; no [VERIFY]/[DATA NEEDED] flag exists to preserve.
