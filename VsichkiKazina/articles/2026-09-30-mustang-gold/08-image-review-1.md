# Step 8 — Image review, pass 1

## Environment
- AI hero generation: **SKIPPED** — image API offline (Gemini HTTP 402, probed 30.09.2026).
- Gemini visual review: **SKIPPED** — Gemini offline (HTTP 402, probed 30.09.2026).
- No Gemini/image script was called. Fallback: MANUAL INTEGRITY CHECK by the writer.

## Image 1 — images/mustang-gold-rtp-infografika.svg (hand-authored infographic)
MANUAL INTEGRITY CHECK:
- **Every SVG number/label ⊂ body (05b):** 96.53%, 3.47%, €965.30, €34.70, 95.54%, „5x3", „25 фиксирани линии", „Money Collect", „1000 пъти", „200 пъти", „100 пъти", „50 пъти", „12 000 пъти залога", Grand, Major, Minor, Mini — all present in body prose. Verified grep-verbatim. ✓
- aria-label figures all trace to body. ✓
- **No operator logos, no operator screenshots, no faces/people, no invented numbers, no glamorised winning.** Neutral RTP/house split + jackpot ladder + key facts. ✓
- **Filename** descriptive lowercase-hyphenated (mustang-gold-rtp-infografika.svg). **ALT** full Bulgarian, describes every data point. **Caption** marks „Примерни стойности" + „операторът може да пусне 95.54%… провери инфо-панела". ✓
- **Layout hygiene:** dark 720×560 card (rect 8/8/704/544 rx18 #0f172a); labels start x=32/52; RTP bar player 633 px + house 23 px inside 32..688 track; jackpot sub-panels (#111f38) 2×2 grid; bottom strip present. NO em-dash. ✓

## Conclusion
images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS)
