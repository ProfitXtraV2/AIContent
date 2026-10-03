# 01 — SYNTHESIS · vk-0244

QUERY: Размер на залога в слота (монети, нива и линии): как се образува общият залог
MARKET: bg · BYLINE: persona (Георги Тодоров) · TYPE: guide
INTENT: A player sees three controls in a slot (монета, ниво/залог, линии) and does not understand how they combine into the number that is actually deducted per spin, nor why two different setups can cost the same. Wants the formula, a worked example, and the practical consequence for the budget.

## ENTITY UNION (facts in)
- общ залог / залог на завъртане (total bet per spin) = the deducted amount.
- стойност на монета (coin value): monetary worth of one coin (e.g. €0.01, €0.05).
- ниво на залог / монети на линия (bet level / coins per line): how many coins per line.
- активни линии / начини (active paylines or ways-to-win).
- FORMULA: общ залог = стойност на монета × ниво на залог × брой активни линии.
- Same displayed total can be built differently; per-line stake is what governs payout scaling.
- RNG produces the outcome; stake controls do not change odds.
- On a standard fixed-RTP slot, stake size does not change RTP; it scales payout size.
- Variable-RTP exception exists per game (check paytable) — do not assert a figure.
- Fixed vs selectable lines; fewer lines = fewer win-check paths.
- Session length depends on общ залог, not coin value.

## CONFLICTS
None. All three source clusters agree on the formula and on "stake size scales payout, not odds/RTP". The only divergence is the variable-RTP exception (a minority of titles), which is reported as a labelled nuance, not the rule. No [CONFLICT] flag.

## EXCLUDED CLAIMS (out of scope / covered by other pillars)
- Deep payline / ways-to-win mechanics (243/1024/Megaways) → owned by vk-0008 „Линии на печалба"; cross-link only.
- Bankroll sizing rules → owned by vk-0166 „Управление на банкрол"; cross-link only.
- Reading the full paytable → owned by vk-0058 „Четене на paytable"; cross-link only.
- Table limits → vk-0243; not slots, not referenced.
- Any named-game RTP %, max win, jackpot → excluded (would need a game-DB figure; out of this guide's scope).
- Bonus/превъртане/operator/НАП/tax → none used.

## FLAGS
- [VERIFY per game] noted for the variable-RTP exception only — handled in text by telling the reader to check that game's paytable, NOT by stating a number. No numeric flag reaches the body.
- No [DATA NEEDED]. No [CONFLICT].

## ORIGINAL DRAFT (facts-in, expression-out — raw, pre-outline)
Three controls, one number that matters. A slot shows you a coin value, a bet level (coins per line), and a number of lines. The amount actually taken from your balance each spin is all three multiplied: coin value × bet level × lines = total bet. At €0.05 a coin, level 2, 20 lines, that is €2.00 a spin. Change the coin value to €0.05, level 3, 25 lines and it is €3.75. The coin value in the corner is not your bet; the total bet is.

Because it is a product of three numbers, the same total can be assembled more than one way. €0.02 × 1 coin × 20 lines is €0.40; €0.01 × 2 coins × 20 lines is also €0.40, with the same per-line stake and the same payouts. So the displayed coin value tells you very little on its own.

The spin result comes from the RNG and does not care how you set those three dials. Raising the bet does not improve your odds; it scales the stake up, and with it the size of any payout. On a normal fixed-RTP slot, splitting the stake differently does not move the RTP either; a handful of variable-RTP titles publish an RTP range tied to the max coin level, which you confirm in that game's paytable rather than assume.

Fixed vs selectable lines: some games lock every line on, some let you drop lines to lower the total bet, which also drops the win-check paths. The practical takeaway is budget-shaped: session length tracks the total bet, not the coin value, so the number to watch before the first spin is the общ залог.

## SUGGESTED PERSONA
Георги Тодоров (the tester), editorial-leaning education register. Doctrine fit: "банерът е реклама" maps to "the coin value in the corner is the banner; the total bet is the contract." Worked € examples at small realistic stakes, illustrative-labelled. One RG touch tying total bet to session length and limits.
