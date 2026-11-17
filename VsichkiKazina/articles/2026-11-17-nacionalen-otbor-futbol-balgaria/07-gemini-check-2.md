# 07 — Gemini External Check · Pass 2 (on 05b after Humaniser pass 1)

Tool: `scripts/gemini_check.py` (API ONLINE). Date: 2026-11-17.

## Verbatim verdict

**Verdict: Likely human-written, 90% confidence.**

Normalized HUMAN-LIKENESS = **90** → ≥ GEMINI_TARGET_CONFIDENCE (80): **PASS**.

Keep-best ledger: initial draft = 15 (Shows AI patterns 85%); Humaniser pass 1 = **90**
(Likely human-written 90%). Highest = 90 → KEEP the pass-1 version as final 05b. Loop ends on PASS
within MAX_GEMINI_PASSES (2). gemini column = `human 90`.

## Verbatim recommendations (minor polish only — article already PASSED)

This article reads like the work of a professional human copywriter or content marketer. It lacks the
classic LLM hallmarks: no fluff, no robotic transitions („Въпреки това", „В заключение"), no generic
breathless excitement. The headings are narrative rather than formulaic, and the integration of strict
compliance/RG policies with sports history is handled with a nuanced, brand-specific voice.

1. Translated/unnatural idiom: „Организираният футбол в България получава своя гръб през 1923 г." —
   „получава своя гръб" reads like a literal calque. Suggested: „поставя своите основи" / „придобива
   официална структура".
2. Mixed metaphor / preposition: „...тема, върху която сядат и хора..." — suggested „около която се
   обединяват" / „на която се спират".
3. SEO directory signposting: „...за които Всички Казина има отделни ръководства: ..." reads slightly
   like a table of contents; suggested weaving the links into the narrative without the announce-colon.

Process/compliance note: Gemini saw the `[VERIFY: точен брой и дали е наравно с Христо Бонев]` flag and
the RG/affiliate disclosures and explicitly did NOT touch them (correct — flags stay; human resolves at
Step 6).

## Decision
PASS at 90. Per daily-run ("PASS when human-likeness ≥ 80 — log and continue"), the loop stops; no
further Humaniser pass is run (a fresh pass could lower the score and keep-best forbids keeping a lower
later version). Items 1–3 above are forwarded to the human editor in 06-verification.md as OPTIONAL
polish; they touch no number, link, flag, RG line, date, or byline.
