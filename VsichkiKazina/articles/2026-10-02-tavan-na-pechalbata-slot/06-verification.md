# 06 Verification - 2026-10-02-tavan-na-pechalbata-slot (vk-0238)

## Surviving flags
[VERIFY] 0 | [DATA NEEDED] 0 | [CONFLICT] 0. No flags in the text. Source-quality notes for the human (not flags in text):
1. Gates of Olympus max-win probability "1 на 718 391 завъртания": single published estimate (OLBG). A secondary search snippet cited 1 in 697,350; not used. Text attributes it to OLBG.
2. Tombstone Slaughter "приблизително 1 на 189 милиона" (500,000x): secondary source (hearthstats.net), text labels it "приблизителна оценка".
3. Sweet Bonanza "десетки хиляди бонус рундове": independent analysis page (sweet-bonanza-australia.readme.io), secondary; text says "независим анализ".
4. Sweet Bonanza volatility: SlotCatalog "medium-high" vs other listings "high"; text says "средна до висока".
5. Starburst max win conflicts across sources (500x vs 800x in an earlier article): deliberately NOT used.

## Time-sensitive / sourced claims (accessed 02.10.2026)
- Max win definition, per-round scope, truncation, 2,000x-50,000x typical, extremes: https://win.gg/how-max-win-works-online-slots/ ; https://slotdecoded.com/max-win-slots-explained/
- Gates of Olympus 5,000x, RTP 96.50% (+95.51%, 94.50%), hit frequency 28.82% (every 3.47 spins), 1 in 718,391, high volatility: https://www.olbg.com/slots/games/gates-olympus ; https://slotcatalog.com/en/slots/Gates-of-Olympus (bets EUR 0.20-100, multipliers 2x-500x, FS multipliers accumulate); Pragmatic Play official page https://www.pragmaticplay.com/en/games/gates-of-olympus/ confirms RTP 96.50% and multiplier symbols up to 500x (states no max win).
- Sweet Bonanza 21,100x, RTP 96.51%, hard ceiling, free-spins only: https://slotcatalog.com/en/slots/Sweet-Bonanza ; https://sweet-bonanza-australia.readme.io/reference/sweet-bonanza-max-win
- Book of Dead 5,000x, RTP 96.21%, high volatility: https://slotcatalog.com/en/slots/Book-of-Dead
- Tombstone Slaughter 500,000x / ~1 in 189M: https://hearthstats.net/the-max-win-cap-controversy-when-slots-cut-you-off-at-10000x-or-25000x/
- Figures are for default RTP builds; operator may run lower builds (stated in text). No tax, licence or operator claims made.

## Recalculated figure (working)
Expected loss over one average max-win interval at €1 per spin: 718 391 spins x €1 = €718 391 staked. House edge = 100% - 96.50% = 3.50%. 718 391 x 0.035 = €25 143.685, rounded "около €25 144". Prize at cap: 5 000 x €1 = €5 000. Also: 5 000 x €0.20 = €1 000; 5 000 x €100 = €500 000; 21 100 x €0.20 = €4 220; 718 391 x €100 = €71 839 100. All match 05b.

## Number diffs between stages (log)
02 -> 03: all numbers preserved except "5 000" in the removed sentence "За мен 5 000x е интересен факт..." (deleted intentionally: unsupported first-person claim, figure still stated elsewhere). 03 -> 04: one number added intentionally, "500x" (Gates random multipliers up to 500x, Pragmatic Play official page + SlotCatalog). 04 -> 05b: 0 changes. 05b v0 -> final: 0 number changes (text edits only). Infographic numbers verified identical to 05b.

## Gemini (Step 7)
check 1 (v0): 90 PASS. check 2 (v0 + top-up sentences): conservative 25, needs changes. humaniser pass 1 applied recs -> check 3: 90 PASS. Final human-likeness 90, 1 humaniser pass, kept = pass 1 version (tied with v0, meets length floor). Verdicts verbatim in 07-gemini-check-1/2/3.md; keep-best record in 07-keep-best.md.

## Images
images: 2 (infographic 100, hero 82); 0 integrity failures; no people, logos, screenshots or invented numbers; infographic layout rendered to PNG and checked (no overlap/clipping).

## Compliance
Em-dashes in 05b: 0. Byline Георги Тодоров. Internal links: /kazino-igri/, /depoziti-i-teglenia/, /otgovorna-igra/ (x2 incl. footer), /kak-ocenyavame/. No affiliate links in body; affiliate-disclosure footer kept. No Протокол на тегленето (concept guide). Body word count ~986 (H1 to before the 18+ line, incl. table and image captions); whole file ~1,190 incl. meta and footer.
