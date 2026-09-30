# 06 — VERIFICATION · vk-0178 · Ultimate Texas Hold'em

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 0 · [DATA NEEDED] 0 · [CONFLICT] 0.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped. Only the initial draft exists; it stands as final 05b (keep-best trivial). See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (house edge 0.53% element-of-risk vs 2.185% of ante + the 4x/2x/1x raise ladder; numbers verbatim to 05b). AI hero SKIPPED (gemini_image_gen.py HTTP 402). Image review SKIPPED (HTTP 402); manual integrity check PASSED. images: 1 (infographic, review skipped — API down). See 08-image-review-1.md.

Body word count: 1147 (prose, excluding the Blind and Trips tables, the image ALT and the caption; excludes the footer boilerplate blocks). Within the 1000–1500 guide band.

## EVERY SPECIFIC FIGURE → PRIMARY SOURCE
Both sources reached and read on 25.09.2026.
Source A (primary game-math + strategy): Wizard of Odds — Ultimate Texas Hold'em — https://wizardofodds.com/games/ultimate-texas-hold-em/ (+ /strategy/)
Source B (rules corroboration): Wikipedia — Ultimate Texas Hold'em — https://en.wikipedia.org/wiki/Ultimate_Texas_Hold'em

| Figure in body | Value | Source |
|---|---|---|
| Тесте / раздадени карти | 52 карти; 2 закрити на играч и дилър, 5 общи | A, B |
| Задължителни залози | Ante и Blind, еднакви по размер | A, B |
| Незадължителен страничен залог | Trips (само върху ръката на играча) | A, B |
| Вдигане Play — преди флопа | до 4x Антето (някои маси и 3x) | A, B |
| Вдигане Play — след флопа | 2x Антето | A, B |
| Вдигане Play — на ривъра | 1x Антето или пас | A, B |
| Дилър се класира с | чифт или по-добра ръка | A, B |
| Дилър не се класира → Анте | връща се (push); Play и Blind се изплащат нормално | A, B |
| Blind — роял флъш | 500:1 | A, B |
| Blind — стрейт флъш | 50:1 | A, B |
| Blind — каре | 10:1 | A, B |
| Blind — фул хаус | 3:1 | A, B |
| Blind — флъш | 3:2 | A, B |
| Blind — кента | 1:1 | A, B |
| Blind — под кента | връща се (push); при загуба на ръката отпада | A, B |
| Trips (най-щедра таблица) | роял 50:1, стрейт флъш 40:1, каре 30:1, фул хаус 9:1, флъш 7:1, кента 4:1, три от вид 3:1 | A |
| Trips — домашно предимство (тази таблица) | ≈0.90% | A |
| Trips — по-стиснати таблици | домашно предимство до ≈6% (6.1808% най-стиснатата) | A |
| Домашно предимство спрямо Антето (оптимална игра) | 2.185% | A |
| Element of risk спрямо оборота (оптимална игра) | 0.526% (≈0.53%) | A |
| Опростена стратегия | 2.43% спрямо Антето / 0.58% спрямо оборота | A |
| RTP (спрямо оборота, оптимална игра) | ≈99.47% (= 100% − 0.526%) | derived from A |
| Стратегия — вдигане 4x преди флопа | чифт 3-3+, асо-/поп-карта от боя, дама/вале-висока от боя (и офсют прагове) | A (/strategy/) |
| Стратегия — вдигане 2x след флопа | две двойки+ или скрит чифт | A (/strategy/) |
| Стратегия — ривър | 1x, освен ако ≥21 карти на дилъра те бият → пас | A (/strategy/) |

Note: Trips pay tables VARY by casino; the body presents the most generous common table and states explicitly that stingier tables raise the edge (check the felt). The €10/€10/€40 example is labelled примерни (illustrative) in body and infographic.

## RECALCULATION 1 — RTP from house edge (with working)
RTP (спрямо оборота) = 100% − element of risk = 100% − 0.526% = 99.474% ≈ 99.47%. ✓ Body states ≈99.47% over the long run (thousands of hands), not a session promise.
RTP спрямо Антето = 100% − 2.185% = 97.815% ≈ 97.82% (not quoted in body; internal check). Consistent.
Element of risk 0.526% < 2.185% (ante): consistent, because the player raises Play (often 4x) on most playable hands, so total wagered is several × the Ante; dividing the same expected loss by the larger denominator gives the smaller %.

## RECALCULATION 2 — why the Blind pay table ranks as it does (5-card frequencies, C(52,5)=2,598,960)
royal flush 4 · straight flush (non-royal) 36 · four of a kind 624 · full house 3,744 · flush (non-SF) 5,108 · straight (non-SF) 10,200.
Rarer hand → higher Blind payout: royal (4) 500:1 > straight flush (36) 50:1 > quads (624) 10:1 > full house (3,744) 3:1 > flush (5,108) 3:2 > straight (10,200) 1:1. Monotonic with rarity. ✓ Body's ordering is correct.

## INTERNAL LINKS USED (4, all live in sitemap 25.09.2026)
1. /blog/kak-se-igrae-poker-kazino/ — anchor „покера в неговия по-общ вид" (sibling overview; this article is the deep dive)
2. /kazino-igri/ — anchor „игрите на маса в казиното"
3. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG touch)
4. /kak-ocenyavame/ — anchor „публична методика, а не през усещане"

## HUMAN CHECK BEFORE PUBLISH
- Confirm the Blind pay table (500/50/10/3/3:2/1, push below straight) and the Trips "9-7" table + 0.90% edge against the live Wizard of Odds page; confirm which Trips table the target BG operator actually uses (the felt decides the edge).
- Confirm 2.185% (ante) / 0.526% (element of risk) optimal figures vs Wizard of Odds; the 2.43%/0.58% pair is the simplified-strategy version (do not mix).
- No operator named, no НАП licence claim, no tax claim, no affiliate link — correct for an educational guide.
- Fill [About Всички Казина boilerplate] and [author-bio] slots at publish (Step 8/6).
