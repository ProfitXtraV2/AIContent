# 06 — Verification (vk-0293, пасианс)

## Surviving flags
NONE. 0 [VERIFY] · 0 [DATA NEEDED] · 0 [CONFLICT]. Guides-only scope satisfied: 0 operator/НАП/tax claims. Nothing for the human to resolve at Step 6.

## Facts & sources (public international game databases — reachable, no geo-block)
- Клондайк rules — https://en.wikipedia.org/wiki/Klondike_(solitaire) (52 карти, 7 колони/28 раздадени/24 талон, 4 основи А→К, редуване на цветовете, празна колона=поп, теглене по 1 или 3).
- Паяк rules — https://en.wikipedia.org/wiki/Spider_(solitaire) (104 карти/2 тестета, 10 колони, 54 раздадени = 4×6+6×5, 50 талон, надолу независимо от боята, еднобойна поредица се мести, пълна К→А еднобойна се сваля, 8 поредици, 1/2/4 бои). Corroboration on same-suit K→A removal + 8 sequences: solitairebliss.com / solitaire365.com spider rules.
- FreeCell rules — https://en.wikipedia.org/wiki/FreeCell (52 карти, 8 колони = 4×7+4×6, всички открити, 4 свободни клетки, 4 основи А→К, редуване на цветовете, move = (1+клетки)×2^(празни) = до 5, ~99.999% решими).

These are evergreen game mechanics, not time-sensitive; no dated operator terms.

## Recalculation (working shown)
- Клондайк раздаване: 1+2+3+4+5+6+7 = 28 карти на масата; 52 − 28 = 24 в талона. ✓ (matches text)
- Паяк раздаване: (4×6) + (6×5) = 24 + 30 = 54 раздадени; 104 − 54 = 50 в талона; победа 8 × 13 = 104 (цялото двойно тесте). ✓
- FreeCell: (4×7) + (4×6) = 28 + 24 = 52; местене (1 + 4 свободни клетки) × 2^0 = 5 карти. ✓

## Gemini Step-7 (text)
Final: **human 90** (keep-best = baseline/pass 1, „Likely human-written 90%", PASS ≥ 80). Pass 2 (humaniser via recs) scored HL 15 (noisy detector relocated flags) → reverted to baseline per keep-best. MAX_GEMINI_PASSES (2) reached. Facts/numbers/RG/disclosures confirmed intact both passes.

## Step-8 images
images: 3 (hero webp 22.3KB + infographic klondike-nachalna-podredba.svg + infographic pasians-trite-vida-sravnenie.svg). Gemini image review PASS, score 100, 0 integrity failure, every infographic number 1:1 vs 05b. Hero carries no text/numbers.

## Trust/compliance
Byline Георги Тодоров · brand „Всички Казина" exact · pub+updated 27.10.2026 · About boilerplate · author bio · verbatim „18+ Хазартът може да пристрасти. Играйте отговорно." + RG signposting /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" line · no affiliate links (пасиансът не е на пари) → „Тази статия не съдържа партньорски връзки" + site affiliate-licensing footer stated PENDING. 4 internal links (/otgovorna-igra/, /blog/belot-pravila/, /blog/santase-pravila/, /blog/tabla-pravila/) + /kak-ocenyavame/ in boilerplate. 0 em-dashes.

Brand Gate: PASS 94/100, 0 critical.
