# 07 — Gemini external check · pass 3 · vk-0167
Model: gemini-3.1-pro-preview. Ran on 05b after Humaniser pass 2 (step-7b: combined the назряла/изстинал pair, replaced the personification with a plain mathematical statement, softened „осигурява само едно"/„потвърждава конкретно следното"/„оборва две заблуди", merged the TRNG contrast).

VERDICT (verbatim): "Shows strong AI patterns, 85% confidence."
Normalised human-likeness = 100 − 85 = **15** → still below 80; equal to pass 2.

Observation: Gemini now flags the very sentences created to break symmetry (it re-labels „оборва две често срещани заблуди" and „потвърждава конкретно следното:" as signposting). The detector is stuck at ~85% for this concept-explainer shape regardless of edits, exactly the noisy-over-editing case the Step-7 policy warns about ("detector scores are noisy; over-editing strips voice").

DECISION — KEEP-BEST: max Gemini passes (2 Humaniser passes) reached. Scores: initial draft v0 = 25 (best), Humaniser pass 1 v1 = 15, Humaniser pass 2 v2 = 15. Kept version = v0 (the initial 05b, human-likeness 25), restored to 05b-final-draft.md. Logged for the human per policy. All facts/numbers, internal links, verbatim 18+/RG lines, dates, [VERIFY] flag UNTOUCHED across every pass.
