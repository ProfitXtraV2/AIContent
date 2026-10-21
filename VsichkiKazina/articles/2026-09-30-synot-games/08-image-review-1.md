# Step 8 — Image review, pass 1

## Environment
- AI hero generation: **SKIPPED** — image API offline (Gemini HTTP 402, probed 30.09.2026).
- Gemini visual review: **SKIPPED** — Gemini offline (HTTP 402, probed 30.09.2026).
- No Gemini/image script was called. Fallback: MANUAL INTEGRITY CHECK by the writer.

## Image 1 — images/synot-games-klyuchovi-fakti.svg (hand-authored infographic)
MANUAL INTEGRITY CHECK:
- **Every SVG number/label ⊂ body (05b):** 1991, 2016, „над 200", „около 250", „ноември 2024", UKGC, Швеция, Дания, Белгия, Малта, MGA, Гърция, Италия, Испания, Перу, „ISO/IEC 27001", „Book of Secrets", „разширяващ символ", „Respin Joker", „лепкав", 85.02%, 98.02%, „операторът настройва" — all present in body prose. Verified grep-verbatim. ✓ (Числото „10" [години] ⊂ „10-годишен".)
- aria-label figures all trace to body. ✓
- **No operator logos, no operator screenshots, no faces/people, no invented numbers, no glamorised winning.** Neutral key-facts panel (provider profile). ✓
- **Filename** descriptive lowercase-hyphenated (synot-games-klyuchovi-fakti.svg). **ALT** full Bulgarian, describes every data point. **Caption** marks „Числата са публично обявени" + „активният RTP при конкретно казино се вижда в инфо-панела". ✓
- **Layout hygiene:** dark 720×540 card (rect 8/8/704/524 rx18 #0f172a); labels start x=32/52; all text lines end within the right rail (≤688); rounded sub-panels (#111f38); bottom strip present („Публично обявени числа… 18+ Играйте отговорно."). NO em-dash. ✓

## Conclusion
images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS)
