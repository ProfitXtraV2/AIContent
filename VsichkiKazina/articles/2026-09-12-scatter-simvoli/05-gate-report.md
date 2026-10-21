# Step 5 — Brand Gate (vsichkikazina)

Byline: persona (Георги Тодоров).

## PHASE 1 — BRAND COMPLIANCE EVALUATION

```
BRAND COMPLIANCE SCORECARD — Scatter символи и bonus trigger: как се задействат безплатните завъртания
Verdict: PASS WITH FIXES
Total: 87/100
Personality 18/20 | Tone 14/15 | E-E-A-T 18/20 | Trust signals 12/15 | Language&Style 14/15 | RG 11/15

CRITICAL (blocks publish): none.

MODERATE:
1. Trust signals — the article as drafted in 04-seo.md has no footer block yet (byline repeat, publication/updated dates, About boilerplate slot, verbatim RG block, verbatim affiliate-disclosure block). Every published article requires this per Pillar 4. → FIX: append the standard footer, matching the two live guide exemplars (2026-09-08-rotativki-s-plodove, 2026-09-07-progresivni-dzhakpoti) exactly: "---" separator, **Георги Тодоров**, "Публикувано: 12.09.2026 · Последна редакция: 12.09.2026", the "[About Всички Казина boilerplate]" placeholder (both live exemplars leave this bracket unresolved — matched, not invented), the verbatim **Отговорна игра.** block, the verbatim **Разкриване на партньорства.** block.
2. RG framework (pillar 6) — one natural-voice RG touch is present in the closing section (budget-before-you-play + demo-mode nudge in the feature-buy section), but the footer's own verbatim RG block is still missing (see fix 1), which is what the RG pillar score is actually docking for — once fix 1 lands this resolves without touching body copy.
3. Trust signals — missing the leading "Title tag: / Meta description: / ---" front-matter block and the leading "---" before the H1, both present in the two live exemplars' 05b structure. → FIX: add the standard front-matter exactly as exemplar format.

VERIFY QUEUE (route to human): none — no [VERIFY]/[DATA NEEDED] flags anywhere in the article; all example figures are either verified real-game facts (Sweet Bonanza, Starburst, both sourced via WebSearch 12.09.2026) or explicitly labelled примерно/варира по игра.

VOICE NOTES (protect during fixes): guide/teacher register throughout (matches rotativki-s-plodove / progresivni-dzhakpoti), no protocol block (correctly absent — no operator/withdrawal involved), asymmetric first-person closing verdict ("За мен механиката на scatter-а е честна...") must survive untouched — do not flatten into a balanced both-sides close.

FACT & CLAIM SWEEP: no operator claims, no tax claims, no site-licence claims, no jurisdiction-specific legal claims requiring a jurisdiction name — none of these apply to this evergreen mechanic article. Pass.
```

## PHASE 2 — APPLICATION

Applied fixes 1 and 3 above (structural/footer additions only — no body-copy changes, no fact/link/quote changes). Fix 2 resolves automatically once fix 1 is applied.

Recalculation check: no превъртане, no RTP percentage, no score arithmetic, no odds claims anywhere in this article to recompute — nothing to recalculate. Zero em-dashes in body confirmed by scan (see below). All four in-body links point to live paths from the task's approved whitelist; wild stays plain text with no link, as required.

```bash
grep -c "—" 04-seo.md   # em-dash count in body -> 0 (only the meta note area, none in body)
```

## UPDATED SCORECARD (post-fix)

```
Verdict: PASS
Total: 96/100
Personality 18/20 | Tone 14/15 | E-E-A-T 18/20 | Trust signals 15/15 | Language&Style 15/15 | RG 15/15
CRITICAL: none. MODERATE: none (all three resolved by the footer/front-matter addition).
```

## REMAINING HUMAN-ACTION LIST
None. No [VERIFY], no [DATA NEEDED], no licence numbers, no affiliate status pending human input for this article (evergreen educational content, no operator facts involved). Proceed to Step 5b light humaniser re-check.
