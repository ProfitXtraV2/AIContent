# 08 — IMAGE REVIEW (Step 8), pass 1 · Lightning Dice (Evolution)

IMAGES CREATED: 1 hand-authored SVG data infographic — images/lightning-dice-izplashtaniya-mnozhiteli-rtp-infografika.svg
AI HERO: SKIPPED — gemini_image_gen.py depends on the same Gemini API (HTTP 402). Logged
`image gen: skipped (Gemini unavailable)`. Infographic ships alone (never blocks the PR).

GEMINI VISUAL REVIEW:
COMMAND: python3 scripts/gemini_image_review.py articles/2026-09-28-lightning-dice/05b-final-draft.md images/lightning-dice-izplashtaniya-mnozhiteli-rtp-infografika.svg
RESULT: SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). Logged `image review: skipped (Gemini unavailable)`.
Per rules: keep the image, do NOT halt.

MANUAL INTEGRITY CHECK (orchestrator, since automated review is offline): PASS.
- Every number in the SVG (text + aria-label) is copied verbatim from 05b — verified programmatically (payout ladder 149:1…4:1, multipliers 5x/500x/1000x, RTP 96,21%/96,03%, edge 3,8–4% all ⊂ body). ✓
- No operator logos/names, no fake screenshots. ✓
- No invented bonus/RTP/licence numbers (all figures trace to sourced 05b; unverified ones carry in-text version-dependence cautions). ✓
- No people/faces; no glamorised winning (honest framing: множителите платени от свалените изплащания; най-едрите падат най-рядко). ✓
- Descriptive lowercase-hyphenated filename; specific Bulgarian ALT + caption referenced from 05b. ✓
- Layout: viewBox 720×524, ≥16px inner padding; every <text> width estimated (widest left label ≈322px from x=48; right values end-anchored at x=688) — no overlap, no clipping, nothing touches the card edge. ✓

images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS).
