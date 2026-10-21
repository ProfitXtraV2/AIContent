# 06 — VERIFICATION (Step 6, human-owned) · vk-0177
Article: Gamble/Double функция в слотовете: как работи рисковата игра · guide · signed Георги Тодоров · checked 25.09.2026
gate: PASS 94/100 · humanisation: HUMAN-LIKE (Stage 3 MIXED 44/60 → rewrite → HUMAN-LIKE)

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped. Only the initial draft exists; it stands as final 05b (keep-best trivial). See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (survival ladder 0.5^N; numbers verbatim to 05b, labelled математически/примерни). AI hero SKIPPED (gemini_image_gen.py HTTP 402). Image review SKIPPED (HTTP 402); manual integrity check PASSED (no fabricated logo/number/screenshot, no faces, no glamorised winning). images: 1 (infographic, review skipped — API down). See 08-image-review-1.md.

## SURVIVING FLAGS
Count: 0. No [VERIFY], [DATA NEEDED] or [CONFLICT] flag remains in the text. The piece is a how-it-works mechanic guide: it names no operator, no game title, no НАП licence, no bonus terms, no tax claim, and asserts no specific game's gamble RTP/cap/bias. Every figure is either universal, stable public game-math (labelled математически/примерни in the text) or a sourced general-mechanic statement, listed below. The human still confirms the sourced-claims table before publish.

## CLAIMS TO CONFIRM (general mechanic + fairness — source URLs)
| # | Claim in text | What the source shows | Source URL |
|---|---|---|---|
| 1 | Gamble/double е опционална стъпка след печалба; играчът може да прибере (Collect) | „It's always opt-in. You can collect your win at any time and skip the gamble entirely." | https://www.vegasslotsonline.com/features/gamble-buttons/ |
| 2 | Познай цвят (червено/черно) ~50/50, удвоява печалбата (x2) | „The game shows a face-down card, and you pick red or black. A correct guess doubles the gambled amount." (approximately even odds) | https://www.vegasslotsonline.com/features/gamble-buttons/ |
| 3 | Познай боя (suit) ~25% шанс, x4 | „The suit pick gamble offers a roughly 25% chance to quadruple your win by guessing the exact suit." | https://www.vegasslotsonline.com/features/gamble-buttons/ |
| 4 | Верига: 2 верни = 4x, 3 = 8x; 5 поредни ~3% | „Two correct picks in a row pays 4x. Three pays 8x. The probability of stringing together five correct calls is about 3%." | https://www.vegasslotsonline.com/features/gamble-buttons/ |
| 5 | Стълбица (ladder): продължи / задръж / слез | „a step-by-step climb where each rung represents a different prize value, and you decide whether to move up, hold, or drop." | https://www.vegasslotsonline.com/features/gamble-buttons/ |
| 6 | Доставчиците/юрисдикциите ограничават или изключват функцията (таван на поредни удвоявания / само печалби под стойност) | „Many titles cap the number of consecutive gambles, or limit the round to wins under a set value." | https://www.vegasslotsonline.com/features/gamble-buttons/ |
| 7 | Честното удвояване е с нулево предимство и 100% връщане; не сваля RTP на основната игра | „The double up feature is truly fair and has no house edge."; „Any legitimate game maker has the double up feature as a truly fair bet with a 100% return."; „doubling up does not lower the house edge of video poker." | https://wizardofodds.com/ask-the-wizard/video-poker/double-up/ |

## PURE-MATH / ПРИМЕРНИ FIGURES — stated as such in text, not verified against any real game
| Figure in text | Role | Marked in text |
|---|---|---|
| €20 → €40 или €0, средно €20 | EV-neutrality of a fair x2 step | „Числата в примера са примерни" |
| 0,25 × 4 = печалбата (suit x4 EV-neutral) | EV-neutrality of the x4 step | same примерни frame |
| Survival ladder 50% / 25% / 12,5% / 6,25% / 3,125% | 0.5^N over N=1..5 | „числата са математически, при допускане за честни 50/50 шансове" |
| 0.5 на степен N (формула) | the ladder's rule | „числата са математически" |
| €20 × 16 = €320 след 4 удвоявания; шанс 6,25% ≈ 1 на 16 | worked variance example | „Стойностите са примерни" |

## RECALCULATION SHOWN — the 0.5^N survival ladder (working)
Survival probability after N consecutive fair 50/50 doubles = 0.5^N:
- N=1: 0.5^1 = 0.5 = 50%
- N=2: 0.5^2 = 0.25 = 25%
- N=3: 0.5^3 = 0.125 = 12.5%
- N=4: 0.5^4 = 0.0625 = 6.25%
- N=5: 0.5^5 = 0.03125 = 3.125%
Cross-check against the source's „about 3%" for five correct calls: 3.125% ≈ 3% → consistent.
Supporting recalcs:
- Fair x2 EV: 0.5 × €40 + 0.5 × €0 = €20 = amount staked → EV-neutral. ✓
- Suit x4 EV: 0.25 × 4 × W = 1 × W = W → EV-neutral. ✓
- Chain multiplier 2^N: N=2 → 2² = 4x; N=3 → 2³ = 8x. ✓
- €20 after 4 wins: 20 × 2^4 = 20 × 16 = €320; survival 0.5^4 = 6.25% ≈ 1 in 16, so 15 of 16 chains break to €0. ✓

## COMPLIANCE SPOT-CHECK
- Em-dashes (—) in title, meta, body, footers, image ALT/caption and SVG = 0 (grep confirmed). En-dashes (–) = 2, both legitimate: verbatim RG footer „10:00–17:00" and the numeric range „1–5" in the image caption. Neither is an em-dash.
- Byline Георги Тодоров; pub + updated dates 25.09.2026; About boilerplate left as literal placeholder for Step 8.
- Verbatim „18+ Хазартът може да пристрасти. Играйте отговорно." present inline in the body and inside the RG footer.
- RG signposting to /otgovorna-igra/ (inline + footer) + национален регистър на уязвимите лица (НАП, in writing, affected person only) + Солидарност 0888 99 18 66.
- Affiliate footer verbatim; site licence stated as заявление подадено / очаква издаване (no „issued" claim, no invented №).
- No operator name, no НАП licence №, no bonus terms, no превъртане, no tax claim — correct for a mechanic guide.

## BODY WORD COUNT
1020 words (target 1000–1500). ✓

## INTERNAL LINKS USED (brief-approved set, 4 total)
- /kazino-igri/ (anchor: „отделните слот игри")
- /blog/paytable-tablica-izplashtania/ (anchor: „таблицата с изплащания")
- /blog/avtomatichno-zavartane-autoplay/ (anchor: „автоматично завъртане")
- /otgovorna-igra/ (anchor: „инструментите за отговорна игра" — inline body signpost + RG footer)

## HUMAN-ACTION LIST
1. Confirm the 7 sourced statements above against the two live URLs (WoO Double Up; VSO gamble buttons).
2. Fill the About Всички Казина boilerplate placeholder at Step 8.
3. Optional: run the deferred external (Gemini) human-likeness check.
