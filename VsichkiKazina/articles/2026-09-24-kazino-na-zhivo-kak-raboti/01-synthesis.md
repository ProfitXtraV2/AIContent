# 01-SYNTHESIS — 2026-09-24-kazino-na-zhivo-kak-raboti (vk-0170)

## SYNTHESIS REPORT
Entity union across the three gaming-tech sources is consistent; no conflicts. All sources agree on the
core chain: real dealer in a purpose-built studio → multiple HD cameras → GCU on the table encodes video +
game data → OCR reads the physical outcome (cards/roulette) into digital data with no manual input →
result pushed to the player's betting interface. Fairness rests on physical randomness (wheel/deck) plus
recording, scheduled inspection/replacement of cards & wheels, independent audits and licensing oversight.

CONFLICTS: none. Latency figures differ by source („under a second under normal conditions" vs „a couple
of seconds") — resolved by stating a verified RANGE (under a second to a few seconds, connection-dependent)
rather than a single fabricated number.

EXCLUDED CLAIMS (not written): any specific RTP figure; any named operator's studio details as fact; any
exact GCU dimension beyond „small device" (the „shoebox" size appears in secondary results only, kept as a
soft comparison, not a spec); precise ms latency figures. RFID is stated as present on „some" tables
(cross-check), matching the qualified source wording.

## ORIGINAL DRAFT (facts in, expression out; ~1,150w)
[what live casino is — real dealer, studio, real-time stream, bet through interface, distinct from RNG]
[the studio & cameras — multi-angle rig, broadcast lighting, director]
[GCU — small device on the table, encodes video + game data, keeps stream and result in sync]
[OCR — reads card value/suit and roulette number automatically, milliseconds, removes manual-input error;
 RFID cross-check on some tables]
[table types — рулетка, блекджек, бакара, покер, game shows]
[latency & betting timer — small delay, timer closes bets before the dealer acts; adaptive bitrate degrades
 video instead of freezing]
[fairness & oversight — physical wheel/deck decides, tech only captures; recorded, inspected/replaced,
 independently audited, licensing oversight; house edge still built into the rules]
[close — impressive tech but still designed entertainment with a built-in cost; RG touch; defer „where to
 play" to the category page]

Suggested byline: editorial (neutral „ние"; published Георги Тодоров). No first-hand testing angle needed;
this is a mechanism explainer, no protocol block.

FLAGS: [VERIFY]=0 · [CONFLICT]=0 · [DATA NEEDED]=0.
