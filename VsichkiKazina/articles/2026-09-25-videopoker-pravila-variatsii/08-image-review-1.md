# 08 — Image review, pass 1 (видеопокер)

Command: python3 scripts/gemini_image_review.py .../05b-final-draft.md images/videopoker-rtp-tablitsi-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted, same billing outage as Step 7).
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: 99.54% / 98.45% / 97.30% (Jacks or Better 9/6·9/5·8/5),
  100.76% (Deuces Wild пълна), 100.17% (Double Bonus 10/7 пълна). No fabricated figure. ✓
- No operator logos/names, no fake screenshots, no invented RTP/bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+". ✓
- Rendered to PNG at 720px: no clipping, no overlap, all text within card, values inside bars. ✓
Decision: KEEP (1 infographic). AI hero SKIPPED — gemini_image_gen.py also HTTP 402.
images: 1 (infographic, review skipped — API down)
