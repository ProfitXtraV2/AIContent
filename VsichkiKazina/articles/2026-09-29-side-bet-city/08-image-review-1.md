# 08 — IMAGE REVIEW (Step 8), pass 1 · Side Bet City (Evolution)

IMAGES CREATED: 1 hand-authored SVG data infographic — images/side-bet-city-izplashtaniya-rtp-infografika.svg
AI HERO: SKIPPED — gemini_image_gen.py depends on the same Gemini API (HTTP 402). Logged
`image gen: skipped (Gemini unavailable)`. Infographic ships alone (never blocks the PR).

GEMINI VISUAL REVIEW:
COMMAND: python3 scripts/gemini_image_review.py articles/2026-09-29-side-bet-city/05b-final-draft.md images/side-bet-city-izplashtaniya-rtp-infografika.svg
RESULT: SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). Logged `image review: skipped (Gemini unavailable)`.
Per rules: keep the image, do NOT halt.

MANUAL INTEGRITY CHECK (orchestrator, since automated review is offline): PASS.
- Every number in the SVG (text + aria-label) is copied verbatim from 05b — verified programmatically (3/5/7 карти, All Lose 0,70:1, RTP 96,69% / 96,29% / 95,21% / 94,34%, роял флош 1000:1 / 500:1 / 100:1, 52 карти all ⊂ body). ✓
- No operator logos/names, no fake screenshots. ✓
- No invented bonus/RTP/licence numbers (all figures trace to sourced 05b; unverified ones carry in-text version-dependence cautions). ✓
- No people/faces; no glamorised winning (honest framing: повече карти = по-лоша сделка; 7-card royal chase връща най-малко; роял флош изключително рядко). ✓
- Descriptive lowercase-hyphenated filename; specific Bulgarian ALT + caption referenced from 05b. ✓
- Layout: viewBox 720×520, ≥16px inner padding; RTP/payout rows end-anchored at x=688, left labels from x=48; текстовите редове не се застъпват (y-разстояния ≥18px). ✓

images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS).
