# Monthly SEO Review — VsichkiKazina — 2026-11

**Run:** automated daily-fire gate (first fire of the month), 2026-11-01.
**Pass type:** **LIGHT** (budget rule — workspace units remaining ~11k < 20k at start).
Steps 2 + 3 executed; steps 3b / 4 / 5 / 6 deferred to the next full pass (unit reset 2026-11-15).

## Units
- Subscription: Lite, billed monthly. Reset **2026-11-15**.
- Workspace at start: 188,938 / 200,000 used → ~11,062 remaining → LIGHT pass.
- Spent this review: ~516 units (DR + metrics + one batched `overview` of 8 pillar heads).
- Workspace after: 189,454 / 200,000 used → ~10,546 remaining.

## 1. DR + footprint trend (step 2)
| month | DR | organic_keywords | traffic/mo |
|---|---|---|---|
| 2026-10 (baseline) | 6 | 12 | 90 |
| **2026-11** | **5** | **5** | **42** |

**Signal: DECLINING, not rising.** DR 6→5, organic keywords 12→5, estimated traffic 90→42.
The off-site authority kit is **not yet lifting DR** (disavow was uploaded in Oct; the 100%-toxic
backlink profile cleanup may still be settling, and new authority links are pending). No basis to
raise `SITE_MAX_WINNABLE_KD` — **cap held at 40**.

## 2. Pillar graduation (step 3)
Re-pulled KD (`keywords-explorer/overview`, country=bg) for the tracked deferred pillar heads:

| keyword | volume | KD | verdict |
|---|---|---|---|
| казино игри | 11,000 | 78 | Pillar (hold) |
| безплатни казино игри | 9,900 | 43 | **near-cap watch** (was 52/66; now 43, 3 over cap) — cluster already covered by vk-0003 |
| казино игри безплатно | 4,900 | 61 | Pillar (hold) |
| без депозит | 450 | 37 | **KD now ≤40** but bare head folds into no-deposit pillar vk-0004 (cluster covered) → no new write |
| plinko | 600 | 78 | Pillar (hold) |
| gates of olympus | 350 | 83 | Pillar (hold) |
| book of ra | 150 | 69 | Pillar (hold) |
| video poker (EN) | 40 | 78 | Pillar (hold) — BG „видео покер онлайн" 150 remains the writable candidate |

**Graduated to a NEW writable candidate: 0.** `без депозит` crossed the KD cap but is
anti-cannibalized by the existing `/blog/bonus-bez-depozit-2026/` pillar (vk-0004) — recorded as a
fold-in, not a candidate. `безплатни казино игри` dropped to KD 43 (near the cap) and is on watch,
but its cluster is already covered by vk-0003, so even a future graduation is a fold-in, not a new page.

## FINDINGS
- **DR/traffic declining** (6→5, 90→42). The leading indicator for the whole winnability model is
  moving the wrong way. Re-run the full winnable-topic performance check (step 3b) at the next
  full pass to see which (if any) posted articles are ranking; if none rank after 8+ weeks, the
  intent/format of those briefs needs a re-check. Prioritise off-site authority work.
- Only **5 organic keywords** ranking (metrics endpoint). Footprint is still tiny — consistent with
  a young domain mid backlink-cleanup.

## Deferred to next FULL pass (unit reset 2026-11-15)
- Step 3b — winnable-topic performance check (`site-explorer/organic-keywords`, expensive).
- Step 4 — competitor content-gap re-pull (casinoslots.bg, bg.casinority.com, 7sport.net).
- Step 5 — discovery top-up (`matching-terms`).
- Step 6 — refdomains / disavow alert.

## MANUAL ACTIONS
- **None auto-applicable this month.** No `SITE_MAX_WINNABLE_KD` bump (DR declined).
- **Off-site:** DR is falling — the off-site authority kit (quality referring domains) is the gating
  work for everything downstream. No new toxic refdomains were pulled this pass (step 6 deferred);
  re-check `site-explorer/refdomains` at the next full pass and append any toxic `domain:` lines to
  `WebPortals/VsichkiKazina/docs/seo/disavow.txt`, then re-upload to Google Search Console.

## Self-mark
`docs/data/seo-review.json` → `last_monthly_review = "2026-11"` (idempotent; re-running this month is a no-op).
