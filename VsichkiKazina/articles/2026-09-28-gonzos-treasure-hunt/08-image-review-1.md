# 08 — IMAGE REVIEW (Step 8), pass 1 · Gonzo's Treasure Hunt (Evolution)

IMAGES CREATED: 1 hand-authored SVG data infographic — images/gonzos-treasure-hunt-kamani-mnozhiteli-rtp-infografika.svg
AI HERO: SKIPPED — gemini_image_gen.py depends on the same Gemini API (HTTP 402). Logged
`image gen: skipped (Gemini unavailable)`. Infographic ships alone (never blocks the PR).

GEMINI VISUAL REVIEW:
COMMAND: python3 scripts/gemini_image_review.py articles/2026-09-28-gonzos-treasure-hunt/05b-final-draft.md images/gonzos-treasure-hunt-kamani-mnozhiteli-rtp-infografika.svg
RESULT: SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). Logged `image review: skipped (Gemini unavailable)`.
Per rules: keep the image, do NOT halt.

MANUAL INTEGRITY CHECK (orchestrator): PASS.
- Every number in the SVG (text + aria-label) copied verbatim from 05b — verified programmatically
  (70 / 6 / 1:1 / 2:1 / 4:1 / 8:1 / 20:1 / 65:1 / 2x / 10x / "0 и 7" / "3 и 100" / "1 до 20" /
  96,56% / висока / €1 000 000 all ⊂ body). ✓
- No operator logos/names, no fake screenshots. ✓
- No invented RTP/max/licence numbers (all trace to sourced 05b; single-stone cap 20 000 carries
  in-text "провери за конкретната версия" caution and is NOT put in the graphic). ✓
- No people/faces (Gonzo character is not depicted; no likeness); no glamorised winning (honest
  framing: изборът е илюзия за контрол; 65:1 = цена на риска). ✓
- Descriptive lowercase-hyphenated filename; specific Bulgarian ALT + caption referenced from 05b. ✓
- Layout: viewBox 720×560, two-column table + panels, ≥16px padding; end-anchored values; SVG
  well-formed (xml parse OK); no overlap/clipping. ✓

images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS).
