# 06 — VERIFICATION · Crazy Coin Flip (Evolution): как се играе и RTP

STATUS: for human sign-off before publish. FLAGS STAY IN THE TEXT.
Type: guide (branded live-game explainer) · byline: Георги Тодоров · gate: PASS 92/100 · humanisation: single draft (external check offline) · run date: 28.09.2026
Surviving flags: [VERIFY] 1 · [DATA NEEDED] 0 · [CONFLICT] 0.

## Surviving flags (carried for human)
1. [VERIFY] Точна дата на пускане 2022 (14 vs 27 юни според източниците) — тялото твърди само „2022 г.". §Intro.
(Design note, not a flag: подхвърлянето е описано като „балансирано... близо до 50 на 50" — замисъл, не отпечатана вероятност.)

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, probed live 28.09.2026). gemini=skipped. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~1,040 prose (excluding Title/Meta, ALT/caption, footer). Within the 1,000–1,800 guide band.

## SOURCES REACHED (28.09.2026)
- Evolution — Crazy Coin Flip game page (3 phases, scatters, coin flip, spin modes): https://games.evolution.com/live-casino/crazy-coin-flip/
- Evolution — Crazy Coin Flip announcement (first live slot game): https://www.evolution.com/news/us-debut-for-evolutions-crazy-coin-flip-a-unique-slot-game-with-live-bonus-round-and-super-sic-bo-a-super-engaging-live-version-of-the-ancient-dice-game/
- LiveCasinoComparer — Crazy Coin Flip (initial coin values 5x–100x, RTP 96.05%, Top-Up 95.06%, no multiplier cap, €500,000): https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/crazy-coin-flip/
- casino.org/CasinoScores — how to play (Top-Up ~50s, up to 50x): https://www.casino.org/casinoscores/blog/how-to-play-crazy-coin-flip/

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Пусната | 2022 (14 vs 27 юни) | evolution.com; livecasinocomparer.com; bigwinboard.com — [VERIFY] date |
| Квалификационен слот | 5 барабана, 3 реда; 3 скатера | evolution.com; livecasinocomparer.com |
| Допълнителен слот (Top-Up) | по избор, ≈ 50 сек; множители до 50x | casino.org/CasinoScores |
| Начални множители на страна | 5x–100x | livecasinocomparer.com |
| Комбиниране | начални + top-up + скатер множители (сбор) | evolution.com; livecasinocomparer.com |
| Таван на множителя | няма фиксиран | livecasinocomparer.com |
| Таван на печалбата | 500 000 € | livecasinocomparer.com |
| Режими | Normal 1x; XXXtreme 5x (≥1 скатер); Super XXXtreme 50x (2 скатера) | evolution.com; bigwinboard.com |
| RTP обща (оптимална) | ≈ 96,05% (edge ≈ 3,95%) | livecasinocomparer.com; casino.org |
| RTP Top-Up | ≈ 95,06% | livecasinocomparer.com; casino.org |

## NOT USED (avoid fabrication)
- 25,000x max multiplier → not verified for this game (likely Crazy Time); replaced with "no multiplier cap + €500,000 payout cap".
- "Dual RED + BLUE bet in qualification" → unconfirmed on authoritative sources; NOT claimed. Red/blue described in Top-Up and the coin only.
- Exact 50.00% flip probability → design intent, not a printed figure; stated as "балансирано".
- Min/max stakes ($0.10 / $3,000) → operator-specific; not stated.
- Secondary RTP variant (top-up 95.27% / 95.02%) → lower confidence; primary 95.06% used.

## RECALCULATION (with working)
- Edge from RTP: 100% − 96,05% = 3,95%. ✓
- On €100 at 96,05%: ≈ €96 returned long-run; ≈ €4 house. ✓
- Top-Up lowers return: 95,06% < 96,05% ⇒ opting into Top-Up reduces expected value. ✓
- Spin-mode logic: Normal 1x, XXXtreme 5x (≥1 scatter), Super XXXtreme 50x (2 scatters); none delivers the 3rd required scatter. ✓
- SVG numbers ⊂ body numbers. Verified programmatically. ✓

## COMPLIANCE SPOT-CHECK
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text + footer). ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66. ✓
- Афилиейт footer (1 август 2026 режим), заявление подадено/очаква — без издаден лиценз, без измислен №. ✓
- Game explainer: NO BG operator, NO НАП licence №, NO tax, NO bonus terms, NO affiliate links. Evolution само като maker. ✓
- Byline Георги Тодоров; „Всички Казина" правилно. ✓ Zero em-dashes. ✓
- Internal links (live in sitemap): /blog/live-game-shows/, /kazino-igri/kazino-na-zhivo/, /kak-ocenyavame/, /otgovorna-igra/. ✓

## ANTI-CANNIBALIZATION (Step-6 human check)
Crazy Coin Flip live game-show spoke. Distinct format (slot-qualification + coin flip) from wheels
(Dream Catcher/Crazy Time/Funky/Monopoly), lotto (Mega Ball vk-0193), case (Deal or No Deal vk-0194),
ladder (Cash or Crash vk-0191), dice (Bac Bo vk-0197). Distinct primary kw (crazy coin flip). No other
Crazy Coin Flip page in queue/sitemap.

## HUMAN-ACTION LIST
1. Confirm the exact release date if a firm figure is wanted (resolve [VERIFY] 1) or leave as "2022".
2. Optional: when Gemini credits return, run Step-7 text + Step-8 image backfill.
