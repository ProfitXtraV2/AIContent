# 08 — IMAGE REVIEW (Step 8), pass 1 · Bac Bo (Evolution): как се играе, множители и RTP

IMAGES CREATED: 1 hand-authored SVG data infographic — images/bac-bo-zalozi-i-rtp-infografika.svg
AI HERO: SKIPPED — gemini_image_gen.py depends on the same Gemini API (HTTP 402). Logged
`image gen: skipped (Gemini unavailable)`. Infographic ships alone (never blocks the PR).

GEMINI VISUAL REVIEW:
COMMAND: python3 scripts/gemini_image_review.py articles/2026-09-27-bac-bo/05b-final-draft.md images/bac-bo-zalozi-i-rtp-infografika.svg
RESULT: SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). Logged `image review: skipped (Gemini unavailable)`.
Per rules: keep the image, do NOT halt.

MANUAL INTEGRITY CHECK (orchestrator, since automated review is offline): PASS.
- Every number in the SVG (text + aria-label) is copied verbatim from 05b — verified programmatically (SVG numeric/data tokens ⊂ body). ✓
- No operator logos/names, no fake screenshots. ✓
- No invented bonus/RTP/licence numbers (all figures trace to sourced 05b, unverified ones carry [VERIFY] in the body). ✓
- No people/faces; no glamorised winning (honest framing: max-win/множител e таван, не очаквана печалба). ✓
- Descriptive lowercase-hyphenated filename; specific Bulgarian ALT + caption referenced from 05b. ✓

images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS).
