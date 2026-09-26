# 08 — Image review, pass 1 (Casino Hold'em)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-26-casino-holdem/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-26-casino-holdem/images/casino-holdem-pravila-i-koeficienti.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted; same billing outage as Step 7).
Also gemini_image_gen.py → HTTP 402 (image model). AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: 2 hole + 3 flop; Call = 2× Ante; dealer qualifies двойка четворки;
  Ante paytable 100:1 / 20:1 / 10:1 / 3:1 / 2:1 / 1:1; house edge ≈2,16% (Ante) and ≈6% (AA). ✓
- No fabricated figure; no per-version paytable invented; coefficients match 05b and source. ✓
- No operator logos/names, no fake screenshots, no invented bonus/licence/RTP. No provider named on the graphic. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно" + „коефициентите зависят от версията" note. ✓
- Validated as XML (viewBox 0 0 720 540, card #0f172a, Arial, headers #93c5fd, right-anchored stat values, note box).
  Text-extent check per formula (chars × font-size × 0,62): longest detail line „Некласиран дилър: Call се връща, Ante
  плаща по таблицата" @12px ≈ 409px from x48 → ends ~457 < card inner edge 696; paytable right sub-column label „Стрейт
  или по-слабо" @13px ends ~537, value right-anchored at x688 starts ~664 → 127px gap, no overlap; note-box text within
  its rect. No overlap/clip; ≥16px inner margin. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down).
