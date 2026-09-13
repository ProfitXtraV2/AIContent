# 06 — Verification (2026-09-13-hacksaw-gaming, vk-0067)

## Surviving flags
- **None in the body.** No [VERIFY] / [DATA NEEDED] strings remain in 05b-final-draft.md.
- One figure deliberately NOT stated to avoid false precision: **Chaos Crew exact RTP** varies across
  reachable sources (~95.9%–96.4%), so the body states only its max win (10,000x) and high volatility,
  never a precise RTP. This is a resolved omission, not a surviving flag.

## Time-sensitive / factual claims + primary-source URLs
| Claim in 05b | Source(s) reached | Note |
|---|---|---|
| Founded 2017, Мсида, Малта | hacksawgaming.com; igamingexpress.com/brands/hacksaw-gaming; gamingsoft.com blog | Multiple DBs + studio agree |
| Started with scratch/instant-win, pivoted to video slots ~2019 | igamingexpress.com; gamingsoft.com | Consistent |
| Studio licences MGA + UKGC | igamingexpress.com; worldcasinodirectory | Studio-level, not operator/НАП |
| Wanted Dead or a Wild 2021, 12,500x, RTP 96.38% (down to 88.42%), high vol 4/5, feature buy 80x/200x/400x | slotcatalog.com/en/slots/Wanted-Dead-or-a-Wild; hacksawgaming.com; aboutslots.com | All figures confirmed on SlotCatalog |
| Chaos Crew 2020, 10,000x, high volatility | slotcatalog; gameshub; bigwinboard | Max win + year confirmed; exact RTP left out |
| Le Bandit 10,000x, RTP 96.30% | slotcatalog listing / olbg; slotark | Confirmed |
| RIP City 12,500x, RTP 96.22%, medium vol 3/5, Maxx bonus 200x | slotcatalog.com/en/slots/RIP-City; bigwinboard | Confirmed |

All figures come from internationally reachable pages (studio site + game DBs). No geo-blocked BG
operator T&C / НАП pages were used, per scope.

## Recalculation (one figure, with working)
Default RTP 96.38%, turnover €1000:
- Player return = 1000 × 0.9638 = **€963.80 → ~€964** (stated).
- House take = 1000 − 963.80 = **€36.20 → ~€36** (stated). House edge = 100 − 96.38 = **3.62%** (stated). ✔
Low version 88.42%, turnover €1000:
- Player return = 1000 × 0.8842 = **€884.20 → ~€884** (stated).
- House take = 1000 − 884.20 = **€115.80 → ~€116** (stated). ✔

## Gemini verdict (Step 7)
- Pass 1 (saved 07-gemini-check-1.md): "Likely human-written, 90% confidence" → **HL 90**.
  (An earlier run of the same file returned 85%.) PASS ≥80 on first check; no humaniser pass needed.
- KEEP-BEST: pass 1, **HL 90%**.

## Images (Step 8)
- images: 2 (1 SVG infographic „titles → max-win", 1 decorative AI hero WebP).
- Image review 1 (08-image-review-1.md): **85/100 PASS**, no integrity failures for either asset;
  all SVG numbers match 05b; no logos/faces/fake UI/glamorised winning.

## Brand Gate
- Self-run: 92/100, zero criticals, PASS (05-gate-report.md).
