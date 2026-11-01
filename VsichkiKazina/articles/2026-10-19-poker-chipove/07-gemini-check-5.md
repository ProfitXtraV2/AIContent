# 07 — Gemini Step-7 check · pass 5 (nightly quality re-run) · vk-0285

**Date:** 2026-10-22
**Model:** gemini-3.1-pro-preview (patient run; 180s timeout, cleared on this ~248-word draft).
**Checked version:** current shipped 05b = the kept initial draft (recorded best HL 35 / `ai 65`).

## Tonight's measurements
| version | verdict (verbatim) | human-likeness |
|---|---|---|
| shipped 05b (initial draft, re-measured tonight) | Shows AI patterns, 75% | **25** |
| fresh deep rhythm rewrite (this run, brand-safe) | Shows AI patterns, 80% | 20 — LOWER, discarded |

## What was attempted and why it was reverted
A single, genuinely **new** humaniser pass was tried this run — deliberately NOT a repeat of
the 2026-10-21 edits, which only deleted the flagged sentences. This time the four flagged
LLM-tells were *rephrased* for natural rhythm (not merely cut), and the sentences the detector
had relocated its complaints onto last night were pre-emptively varied too. **No fact, number,
link, image, RG/18+ line, affiliate disclosure, byline (Георги Тодоров) or brand (Всички Казина)
was changed** — verified: all 7 links identical, full numeric distribution identical, all
compliance blocks intact, 0 em-dashes.

Re-check scored **80% (HL 20) — worse** than the untouched draft's own tonight baseline (HL 25)
and far below the recorded best (HL 35). The detector again **relocated the goalposts**: it
flagged a phrase this pass introduced, re-flagged an *untouched* transition („Турнирните чипове
работят иначе."), and newly condemned the **arithmetic examples** („Четири купчини по 20 правят
80…", „сто чипа по 5 правят 500…") as „pedantic over-explanation" — i.e. it now demands cutting
the fact-bearing numbers, which the hard rules forbid. Same adversarial / non-monotonic behaviour
on dry BG reference content recorded across passes 1–4 and on vk-0008 / vk-0024 / vk-0257 / the
toto pillars: applying the detector's own recommendations lowers the score.

## Keep-best decision (mandatory rule)
Per "the final 05b MUST be the version with the highest human-likeness seen, even if that is the
untouched original; NEVER keep a later, lower version": the shipped 05b stays the **initial draft
(recorded best HL 35)**. Tonight's rewrite was **discarded** (kept only in scratch, nothing of it
committed to the article). `gemini` column stays **`ai 65`** (the winning version's own verbatim
verdict). RG/18+/affiliate disclosures confirmed intact and must remain.

## Conclusion
Five automated passes now agree: this short, dry reference piece cannot be cleared by the detector
through rephrasing — every pass that touches it scores lower. **No further automated passes are
productive here.** Flagged for human editor (Step 6): a human judgement call on whether the content
is acceptable as-is. Content is publish-ready (0 blocking flags).
