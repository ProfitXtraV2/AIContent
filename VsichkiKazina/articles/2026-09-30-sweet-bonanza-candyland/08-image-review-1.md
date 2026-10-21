# Step 8 — Image review, pass 1

## Environment
- AI hero generation: **SKIPPED** — image API offline (Gemini HTTP 402, probed 30.09.2026).
- Gemini visual review: **SKIPPED** — Gemini offline (HTTP 402, probed 30.09.2026).
- No Gemini/image script was called. Fallback: MANUAL INTEGRITY CHECK by the writer.

## Image 1 — images/sweet-bonanza-candyland-koleloto.svg (hand-authored infographic)
MANUAL INTEGRITY CHECK:
- **Every SVG number/label ⊂ body (05b):** 54 сегмента, 23/42.59%, 15/27.78%, 7/12.96%, 3/5.56% (×2), 2/3.70%, 1/1.85%, 1:1, 2:1, 5:1, „2x до 10x", „5x/10x/25x", „до 1000x", „до 20 000x", „20 000x", „500 000 евро", 91.59%, 96.83% — all present in body prose/table. Verified grep-verbatim. ✓
- Segment counts sum to 54; probabilities recomputed (n/54) match. ✓
- aria-label figures all trace to body. ✓
- **No operator logos, no operator screenshots, no faces/people, no invented numbers, no glamorised winning.** Neutral probability bar-chart + max-win/RTP panels. ✓
- **Filename** descriptive lowercase-hyphenated (sweet-bonanza-candyland-koleloto.svg). **ALT** full Bulgarian, describes every data point. **Caption** marks „Числата са публично обявени" + „RTP-то зависи от позицията". ✓
- **Layout hygiene:** dark 720×486 card (rect 8/8/704/470 rx18 #0f172a); labels start x=32/52; bars from x=380, longest 308 px ends at 688 (right rail); % text right-aligned at x=372; two sub-panels + bottom strip. NO em-dash. ✓

## Conclusion
images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS)
