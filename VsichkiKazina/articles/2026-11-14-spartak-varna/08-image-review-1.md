# 08 — Image review, pass 1 (Спартак Варна)

Command: `python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-11-14-spartak-varna/05b-final-draft.md VsichkiKazina/articles/2026-11-14-spartak-varna/images/spartak-varna-fakti.svg`
Exit: 2

Verbatim output:
```
GEMINI_ERROR: HTTP 402 {
  "error": {
    "code": 402,
    "message": "Your prepayment credits are depleted. ...",
    "status": "RESOURCE_EXHAUSTED"
  }
}
```

Interpretation: GEMINI_UNAVAILABLE (billing/credits depleted — persistent since 2026-11-10).
Per daily-run Step 8: unavailable/non-zero exit → `image review: skipped (Gemini unavailable)`; keep the image.

## Manual integrity check (hand-done because Gemini is down) — PASS
Image: `images/spartak-varna-fakti.svg` (hand-authored SVG infographic).
Rendered via Chromium (deviceScaleFactor 2) → clean: 0 text overlap, 0 clipping, balanced 4+4 layout, all 8 figures legible.
- No operator logos / brand names / fake screenshots. ✓
- No people / faces. ✓
- No glamorised winning, no chips/cash/jackpot imagery. ✓
- No invented bonus / RTP / licence numbers. ✓
- Every number traces 1:1 to 05b: 1918, 1932, 8, ~7 000 (labelled „около“), 1961/62, 1983/84, 286 (Илия Кирчев), 56 (Стефан Найденов). ✓
- Specific Bulgarian ALT text + caption present in 05b. ✓

Result: integrity PASS. Keep the infographic (1 image). AI hero not added (decorative-optional; API down anyway).
