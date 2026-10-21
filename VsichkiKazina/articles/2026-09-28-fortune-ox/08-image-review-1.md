# 08 — IMAGE REVIEW (Step 8), pass 1 · Fortune Ox (PG Soft)

IMAGES CREATED: 1 hand-authored SVG data infographic — images/fortune-ox-rtp-mnozhitel-specifikacii-infografika.svg
AI HERO: SKIPPED — gemini_image_gen.py depends on the same Gemini API (HTTP 402). Logged
`image gen: skipped (Gemini unavailable)`. Infographic ships alone (never blocks the PR).

GEMINI VISUAL REVIEW:
COMMAND: python3 scripts/gemini_image_review.py articles/2026-09-28-fortune-ox/05b-final-draft.md images/fortune-ox-rtp-mnozhitel-specifikacii-infografika.svg
RESULT: SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). Logged `image review: skipped (Gemini unavailable)`.
Per rules: keep the image, do NOT halt.

MANUAL INTEGRITY CHECK (orchestrator): PASS.
- Every number in the SVG (text + aria-label) copied verbatim from 05b — verified programmatically
  (3-4-3 / 10 линии / 96,75% / 2000x / средна / €0,20 / €200 / 20x / x10 all ⊂ body). ✓
- No operator logos/names, no fake screenshots. ✓
- No invented RTP/max/licence numbers (all trace to sourced 05b; RTP carries in-text
  operator-configurable caution; wild 20x carries in-text "провери в самата игра" caution). ✓
- No people/faces; no glamorised winning (honest framing: малкият грид не значи по-добри шансове;
  таванът иска рядък пълен екран; респинът гарантира минимум, не максимум). ✓
- Descriptive lowercase-hyphenated filename; specific Bulgarian ALT + caption referenced from 05b. ✓
- Layout: viewBox 720×496, ≥16px padding; end-anchored values at x=688; no overlap/clipping. ✓

images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS).
