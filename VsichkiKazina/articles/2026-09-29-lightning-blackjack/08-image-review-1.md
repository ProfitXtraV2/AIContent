# 08 — IMAGE REVIEW (Step 8), pass 1 · Lightning Blackjack (Evolution)

IMAGES CREATED: 1 hand-authored SVG data infographic — images/lightning-blackjack-taksa-mnozhiteli-rtp-infografika.svg
AI HERO: SKIPPED — gemini_image_gen.py depends on the same Gemini API (HTTP 402). Logged
`image gen: skipped (Gemini unavailable)`. Infographic ships alone (never blocks the PR).

GEMINI VISUAL REVIEW:
COMMAND: python3 scripts/gemini_image_review.py articles/2026-09-29-lightning-blackjack/05b-final-draft.md images/lightning-blackjack-taksa-mnozhiteli-rtp-infografika.svg
RESULT: SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). Logged `image review: skipped (Gemini unavailable)`.
Per rules: keep the image, do NOT halt.

MANUAL INTEGRITY CHECK (orchestrator, since automated review is offline): PASS.
- Every number in the SVG (text + aria-label) is copied verbatim from 05b — verified programmatically (такса 100%, €10/€20, множители 2x/25x, 3:2, 8 тестета, 180 дни, RTP 99,56%, реално ~82%, edge 17,6%/9%, класика под €1/€100, €9, €17–18 all ⊂ body). ✓
- No operator logos/names, no fake screenshots. ✓
- No invented bonus/RTP/licence numbers (all figures trace to sourced 05b; unverified ones carry in-text version-dependence cautions). ✓
- No people/faces; no glamorised winning (honest framing: множителите платени от таксата; реалното връщане ≈82%; показното 25x е примамка). ✓
- Descriptive lowercase-hyphenated filename; specific Bulgarian ALT + caption referenced from 05b. ✓
- Layout: viewBox 720×512, ≥16px inner padding; left labels start x=32/48, right никой елемент не докосва ръба; текстовите редове не се застъпват (проверени y-разстояния ≥18px). ✓

images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS).
