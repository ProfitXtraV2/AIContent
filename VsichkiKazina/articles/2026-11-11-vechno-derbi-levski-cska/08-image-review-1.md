# 08 — Gemini image review (pass 1)

Command: python3 scripts/gemini_image_review.py 05b-final-draft.md images/vechno-derbi-cifri.svg

Result (verbatim):
GEMINI_ERROR: HTTP 402 {
  "error": {
    "code": 402,
    "message": "Your prepayment credits are depleted. Please go to AI Studio ... to manage your project and billing.",
    "status": "RESOURCE_EXHAUSTED"
  }
}

Interpretation: Gemini image review UNAVAILABLE (same 402 billing exhaustion as the text check
and the 2026-11-10 run). Per daily-run.md Step 8: DO NOT halt → review skipped, keep the image.

MANUAL INTEGRITY PASS (hand-verified, hard-hygiene rules):
- Numbers trace to 05b verbatim: 1948, 1:0, 12 000 („Юнак", 1948), 220+ (над 220), 22:9 (22
  победи срещу 9 — Купа), 7:1 (1994), 70 000 (1967). Cross-checked by grep → all present. ✓
- 0 operator logos / casino brand names / fake screenshots (only the football clubs Левски и
  ЦСКА, which are the article's subject, appear — not gambling operators). ✓
- 0 invented bonus / RTP / licence numbers. ✓
- 0 people / faces / photoreal gambling imagery. ✓
- 0 glamorised winning; carries „18+ Играйте отговорно". ✓
- SVG valid XML, 3.0 KB, 0 em-dashes, clean two-column layout with margins, no overlap/clip. ✓

Verdict: manual integrity PASS (automated score unavailable). Image shipped.
AI hero: skipped (Gemini image gen HTTP 402). Infographic ships alone.
