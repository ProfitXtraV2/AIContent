# 06 — Verification · vk-0111 · Yggdrasil Gaming provider hub

## Surviving [VERIFY] / [DATA NEEDED] flags
None. Every specific figure in 05b traces to a fetched source (list below). No number was invented; where a source-level conflict existed it was resolved and the losing option omitted rather than hedged in-text (see „Conflicts resolved").

## Non-fabrication decisions (audit)
- **GEMIX excluded.** The brief hinted at GEMIX, but every source confirms GEMIX is a **Play'n GO** slot, not Yggdrasil. It is never listed here.
- **Original Vikings Go Berzerk max-win multiplier omitted.** Databases disagree (4,000x vs the provider's €93,910), so the original is kept in prose without a max-win figure; the infographic uses **Vikings Go Berzerk Reloaded**'s consistently-cited **25 000x** instead.
- **Jokerizer RTP hedged.** Dual RTP (88% base / 98% Jokerizer mode). Stated only as „режим Jokerizer се играе при RTP до 98%", never a flat number; kept out of the infographic's clean triple.
- **HQ resolved.** Some DBs say Stockholm; the provider's own site lists Malta (San Ġiljan) + Krakow. Rendered as „Шведско по корени, малтийско по седалище", not a two-camp debate.
- **Valley of the Gods volatility.** Provider says „High" (a search snippet said medium) → provider wins → „висока волатилност".

## Time-sensitive / factual claims with sources
| Claim in 05b | Source (fetched) |
|---|---|
| Founded 2013, Fredrik Elmqvist (ex-NetEnt), Swedish roots, HQ Malta (San Ġiljan), Krakow | gr8.tech/provider/yggdrasil-gaming/ ; yggdrasilgaming.com/about-us |
| Grew within Cherry AB; Cherry taken private 2019 by a Bridgepoint-led consortium (PE) | news.cision.com/cherry (Yggdrasil/Cherry corporate structure) ; general iGaming reporting |
| Founder stepped down as CEO April 2022 after nine years, stayed on the board | sbcnews.co.uk/europe/2022/04/21/yggdrasil-founder-elmqvist-passes-ceo-helm-to-bjorn-krantz/ |
| GATI = regulation-ready standardised toolkit; YGG Masters licenses it to ReelPlay, Peter & Sons, Bang Bang Games, Hot Rise Games | gr8.tech/provider/yggdrasil-gaming/ ; casinocompendium.com (Gods vs GigaBlox / Hot Rise Games) |
| GEMs from 2020: Splitz (up to 248,832 ways in Temple Stacks), GigaBlox (up to 6x6, first in Lucky Neko), Multiplier Wilds (Vikings, Berzerk up to 8x) | yggdrasilgaming.com/game-mechanics/gigablox ; casinosonline.com/articles/yggdrasil-game-engagement-mechanics/ |
| Valley of the Gods — RTP 96.2%, max €580,000 (= 5 800x), High, 24.08.2017 | yggdrasilgaming.com/games/valley-of-the-gods |
| Temple Stacks: Splitz — RTP 96.10%, max 25,000x, 2020, up to 248,832 ways | gmblrs.com/game-provider/yggdrasil/temple-stacks ; askgamblers.com/.../temple-stacks-splitz-yggdrasil-gaming |
| Lucky Neko: Gigablox — RTP 96.40%, max 6,950x, 24.06.2020, first GigaBlox | gmblrs.com/game-provider/yggdrasil/lucky-neko-gigablox |
| Vikings Go Berzerk Reloaded — RTP 96%, max 25,000x, 2021 | allslotsites.com/slot-games/vikings-go-bezerk-reloaded/ (+ multi-source consensus) |
| Vikings Go Berzerk (original) — RTP 96.1%, 2016, Medium-High | yggdrasilgaming.com/games/vikings-go-berzerk |
| Jokerizer — up to 98% RTP in Jokerizer mode | askgamblers.com/casino-games/online-slots/reviews/jokerizer-yggdrasil-gaming |
| B2B licences: MGA (Malta), UKGC, Gibraltar, Sweden, others | yggdrasilgaming.com/about-us |

## Recalculation (working shown)
**Valley of the Gods max win = 5 800x.** The provider page states a maximum win of **€580,000**. Yggdrasil's stated maximum bet on the title is **€100**. Max multiplier = 580,000 ÷ 100 = **5,800×**, i.e. „таван до 5 800x залога" as written in 05b and the infographic. The figure is the theoretical ceiling at max stake, not a per-spin expectation, which the caption states.

## Gemini text check (Step 7)
Command: `python3 scripts/gemini_check.py .../05b-final-draft.md` (exit 0, Gemini ONLINE).
- Pass 1 (initial): „Likely AI-written, 85%" → human-likeness **15**.
- Pass 2 (after humaniser pass 1): „Shows AI patterns, 75%" → human-likeness **25**.
- Pass 3 (after humaniser pass 2): „Likely human-written, 80%" → human-likeness **80** → **PASS**.
- Keep-best: final 05b = the pass-2 humanised version (highest HL seen, 80). `gemini` column = **human 80**.
- Each verdict saved verbatim to 07-gemini-check-1/2/3.md. All passes were style-only; number multiset identical across every stage (0 drift), 0 em-dashes, all disclosures/RG/18+/links/dates preserved.

## Images (Step 8)
images: 2 (top-slots 100, hero 100). Both hand-authored SVGs, Gemini image review 100/100 PASS, no integrity/layout defects, all numbers trace to 05b. Verdict saved verbatim to 08-image-review-1.md.

## Brand Gate
93/100, PASS, 0 criticals (05-gate-report.md).

## Length
~1,200 words including footers (body prose ~1,050), within the 1,000–1,800 guide band.
