# 07 — Gemini Step-7 check · pass 4 (nightly quality re-run) · vk-0285

**Date:** 2026-10-21
**Model:** gemini-3.1-pro-preview (patient run; script 120s timeout cleared on this ~245-word draft).
**Checked version:** current shipped 05b = the kept initial draft (HL 35 from the 2026-10-19 keep-best decision).

## Tonight's measurements
| version | verdict (verbatim) | human-likeness |
|---|---|---|
| shipped 05b (initial draft, re-measured tonight) | Shows AI patterns, 75% | **25** |
| brand-safe humaniser attempt (this run) | Shows AI patterns, 80% | 20 — LOWER, discarded |

## What was attempted and why it was reverted
A single brand-safe humaniser pass was applied, targeting only the clearest, most
legitimate LLM tells flagged tonight — **no fact, number, link, RG/18+, disclosure,
byline or brand change**:
- cut the intro "table-of-contents" roadmap sentence, ending the intro on the hook;
- de-dramatised „Има и по-тиха причина." into a grounded budget transition;
- replaced the „Не X, а Y" aphorism („Подреждането не е естетика, а скорост.") with a direct statement;
- reframed the „Начинаещите често очакват…" beginner-generalisation as the misconception itself;
- trimmed the „…и нищо повече" philosophical framing from the conclusion (link kept).

Re-check scored **80% (HL 20) — worse** than the untouched draft's own tonight baseline (HL 25)
and far below the recorded best (HL 35). The detector **relocated the goalposts again**: it now
flags sentences the edit never touched („Чиповете решават няколко практични проблема наведнъж.",
„Това е разликата, която пряко засяга джоба.") and **contradicts its own pass-1/2 advice** — it
had demanded the „beginners" generalisation be removed, then this pass condemned the
de-personalised „Разпространено е схващането…" rephrase as a „strawman". Same adversarial/noisy
behaviour on dry BG reference content logged on vk-0008 / vk-0024 / vk-0257 / the toto pillars,
where applying the detector's own recommendations lowers the score.

## Keep-best decision (mandatory rule)
Per "the final 05b MUST be the version with the highest human-likeness seen, even if that is the
untouched original; NEVER keep a later, lower version": the shipped 05b stays the **initial draft
(HL 35)**. The nightly humaniser edits were **reverted** (working tree discarded, nothing of the
rewrite committed). `gemini` column stays **`ai 65`** (the winning version's own verbatim verdict).

RG/18+/affiliate disclosures confirmed intact and must remain. Flagged for human editor (Step 6):
the detector will not clear this piece by rewriting; a human judgement call is needed on whether
the content is acceptable as-is. No further automated passes are productive here.
