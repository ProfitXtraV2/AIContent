# 06 — Verification · vk-0052 · Каскадни символи (tumble)

## Surviving flags
None. 0 × [VERIFY], 0 × [DATA NEEDED], 0 × [CONFLICT]. Every specific figure is public,
web-reachable game/mechanic data (not operator T&C, not НАП), verified below.

## Fact checks (time-insensitive / evergreen game data)
1. **Cascades do NOT change theoretical RTP; they redistribute wins into streaks →
   higher/streakier volatility.** Verified against multiple mechanic explainers:
   - gamblingzone.com/uk/the-zone/casino/cascading-reel-slots-explained/
   - casinobloke.com/articles/slot-cascade-feature-explained... ("cascading reels do not
     inherently affect a game's theoretical RTP … reshape how that RTP is spread")
   - acrpoker.eu/casino-strategy/exploring-tumbling-reels-slots-with-high-rtp...
   Marketing framing "cascades = higher / steadier RTP" was found and EXCLUDED.

2. **Gonzo's Quest (NetEnt, Avalanche) multiplier ladder** — base game 1x → 2x → 3x → 5x;
   Free Fall (10 free spins) 3x → 6x → 9x → 15x; RTP 95.97%.
   - games.netent.com/video-slots/gonzos-quest/ (RTP 95.97%, Avalanche)
   - askgamblers.com / slotcatalog.com (Free Fall ladder 3x/6x/9x/15x, 10 free falls)
   - Consistent with our own vk-0044 (Gonzo's Quest) established facts.
   Article states these ladders exactly; the article does NOT quote 95.97% (it uses the
   generic 96% illustrative RTP), so no operator-precision claim rides on it.

3. **Multiplier resets each spin** (does not carry across paid spins). Standard Avalanche/
   tumble behaviour, verified in the same Gonzo's Quest references. Article states it.

4. **Sweet Bonanza (Pragmatic Play):** pay-anywhere + tumble; multiplier "bombs" 2x–100x
   only in the free-spins round. Verified in our own live-linked article
   (/blog/sweet-bonanza/, 2026-09-08 draft) and Pragmatic game data. Article states 2x–100x.

5. **Reactoonz (Play'n GO)** cluster pays + cascades; **Sugar Rush (Pragmatic)** cluster pays
   + tumble + multiplier spots. Named in plain text only (not linked — pages not yet live).
   - pokernews.com/casino/slots/reactoonz-slot-review.htm (cluster pays, RTP 96.51%).

## One figure recalculated (working shown)
Claim in text: "Слот с обявени 96% връща тези 96% в дългосрочен план със или без каскади."
- Domain (house) edge = 100% − 96% = **4%**.
- Illustrative €1,000 turnover: expected return = 1000 × 0.96 = **€960**; expected loss =
  1000 × 0.04 = **€40**, spread across many spins. The tumble mechanic changes only WHEN the
  €960 lands (long dry stretches, then a compensating chain), not the €960 itself. Confirmed:
  RTP is a per-unit-staked long-run statistic, independent of how a single paid spin resolves
  into one or several cascade hits. (No € figure is printed in the article body; kept generic
  to avoid an unlabelled specific — the 96%/96% identity is the only quoted number.)

## Images (Step 8)
images: 3 (hero 85 PASS · cascade-mechanic+RTP infographic 100 PASS · multiplier-ladder
infographic 100 PASS). 1 fix pass applied (infographic A RTP-box clearance, infographic B
arrow margins); re-review 100/100, no integrity drops, every number traced 1:1 to 05b.

## Gemini text check (Step 7)
Initial draft: "Shows AI patterns 85%" → human-likeness **15**.
Humaniser pass 1 (apply Gemini recs): "Likely human-written 90%" → human-likeness **90** =
**PASS** (≥80). Keep-best = pass 1 (current 05b, HL 90). 07-gemini-check-1.md / -2.md hold the
verbatim verdicts. No API step skipped (GEMINI_API_KEY present; both text checks and both image
reviews ran, exit 0).

## Compliance recap
Byline Георги Тодоров; brand "Всички Казина"; dates 12.09.2026; verbatim 18+ line + RG
signposting (/otgovorna-igra/ + регистър на уязвимите лица НАП); affiliate-licensing footer
verbatim (заявление подадено, очаква издаване). No operator recommended → no affiliate link
needed. No tax claim. 0 em-dashes. Brand Gate 94/100, 0 criticals.
