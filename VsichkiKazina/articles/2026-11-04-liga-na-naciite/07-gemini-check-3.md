# 07 — Gemini Step-7 check — pass 3 (after humaniser pass 2) + keep-best decision

**Verdict (pass-2 version, check 3): Shows AI patterns, 70% confidence.** → human-likeness = **30**.

Gemini flagged (verbatim, trimmed): (1) "Wikipedia-scrape" definitional opening of „Какво е Лигата на
нациите" with a dates dump; (2) over-explaining the 3-1-0 point system to a betting audience; (3) flat
transition „Световното първенство ползва турнира по сходен начин."; (4) preachy „check official
sources" hedge on the place-allocation line. It again praised the „На пари, отдалеч" section + footer
as "highly localized… human-written/edited" and said to leave them untouched.

## KEEP-BEST ANALYSIS (MAX_GEMINI_PASSES=2 reached — loop ends)

Human-likeness by version/sample (higher = better):
- INITIAL draft: **35** (check 1), then on fair re-sampling **80** ("Likely human-written") and **15**
  ("Shows AI patterns 85%") — THREE identical-input samples span HL 15 → 80.
- Humaniser pass 1: **20** (check 2).
- Humaniser pass 2: **30** (check 3).

Conclusion: the external detector is **non-deterministic noise** on this dense, factual Bulgarian
content — the very same initial text scored 15, 35 and 80. "Highest human-likeness seen" (the lone 80
outlier) is therefore NOT a reliable selection signal: any version could be re-sampled up to ~80 or
down to ~15. This is the same detector behaviour the sibling league guides recorded (anchored
~65–85% "AI" on dense BG facts). No version is distinguishable from the others within this noise.

**Decision:** Among noise-equivalent versions, keep the one with the best human PROSE quality.
That is **humaniser pass 2** (the current 05b): it removed genuine AI tells (signposting setup,
tautological filler, theatrical/poetic bridges, the past/future "profound" contrast) AND two
objectively awkward Bulgarian collocations Gemini correctly caught — „товарни приятелски срещи"
→ „безцелни приятелски срещи" and „нарязана на групи" → „разделена на групи". These are real
copy improvements independent of the (noisy) score. This mirrors the sibling precedent: detector
noise → keep the cleaner prose in the same band.

Every untouchable preserved across all passes: all numbers/dates (2014, 2018/19, 2018, 55, 4 дивизии
A–D, 2020/21, 16, 7, 3/1/0, 2024/25, 2019, 2021, 2023, 2025, 2026), all 5 internal links, RG lines,
18+, disclosures, byline Георги Тодоров, brand Всички Казина. 0 number-drift across 02→03(p1)→05b(p2).

**Recorded result:** gemini = **ai 70** (honest modal; the kept version's own check-3 verdict,
HL 30). Below the 80 target → **marked for human review** (not a fabrication issue; pure style-detector
noise). Style-only throughout: 0 facts/numbers/links/RG touched.
