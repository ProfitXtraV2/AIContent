# Step 7 — Gemini cross-model check — PASS 3 (after humaniser pass 2) — FINAL / KEEP-BEST

**Date:** 2026-10-27
**Checked file:** 05b-final-draft.md (after humaniser pass 2)
**Model:** gemini-3.1-pro-preview

## Verdict (verbatim)
**Likely human-written (or heavily human-edited AI), 75% confidence.**

→ This is a "Likely human-written, X%" verdict → HUMAN-LIKENESS = X = **75**.

## Keep-best ledger (mandatory)
| version | check file | verdict | human-likeness |
|---|---|---|---|
| baseline 05b | 07-gemini-check-1 | Shows AI patterns, 75% | **25** |
| humaniser pass 1 | 07-gemini-check-2 | Shows AI patterns, 80% | **20** |
| **humaniser pass 2** | 07-gemini-check-3 | **Likely human-written, 75%** | **75** ← HIGHEST |

MAX_GEMINI_PASSES (2) reached (2 Gemini-driven humaniser re-passes done).
**KEEP-BEST = humaniser pass 2 (HL 75)** — it is the highest human-likeness seen AND the only "human-written" verdict; the verdict TYPE flipped from "Shows AI patterns" to "Likely human-written". Pass 2 is already the committed HEAD of 05b, so no revert is needed. A later/lower version is never kept just because it came last; here the last version also happens to be the best.

HL 75 is just below the GEMINI_TARGET_CONFIDENCE gate (80), so this does NOT auto-PASS — it is kept-best after the cap and handed to the human reviewer for the final call. The detector was noisy across the loop (each pass relocated its complaints to an entirely different set of passages — links/persona/transitions on check 1, redundancy/calque/hook on check 2, caveat-repetition/neat-bow/signposting on check 3 — and the raw score moved 25→20→75), so over-editing further would strip the strong voice without a reliable gain. Gemini praised the idioms („Въртенето е театър; сметката е готова преди него.") as "highly uncharacteristic of raw AI output in Bulgarian".

## Gemini check-3 residual flags (verbatim summary, NOT applied — cap reached, kept-best)
1. Repetitive caveating: „на дълъг пробег" ~6× (safety-bias). (Factually correct phrasing; left intact — removing risks implying short-run promises.)
2. "Neat bow" paragraph wrap-ups (aphoristic closers). (These are the strong idioms Gemini itself praised.)
3. Mechanical signposting: „Оттам идва…", „Обърнато,…", „За една вечер… важи друго.".
4. "Kitchen-sink" list in the bonus section + parenthetical „(които заместват други)".
Note (Gemini, verbatim): the RG language + 18+ markers were bypassed in the critique and must remain exactly as is.

## Recording
- gemini column: **`ai 25`** (winning version's verbatim scale: human-likeness 75 < 80 → `ai <100−75>`; verdict was the "Likely human-written, 75%" type — borderline, handed to human).
- No fact, number, link, RG line, or flag was ever touched by any Gemini pass (style-only).
