# Smoke test run 1 — Stage 5 (Brand Gate, vsichkikazina) — fresh-context evaluation
# Gate: agents/brand-gate-vsichkikazina.md · Article: tests/gate-smoke-test-article.md
# Mode: EVALUATE ONLY (Phase 1). No fixes applied. Run date: 07.09.2026
# Brief context given to the gate: BRAND: vsichkikazina · type: review · byline: persona
# (Георги Тодоров) · NO withdrawal receipts provided in the brief · operator "Казино Х"

```
BRAND COMPLIANCE SCORECARD — Казино Х ревю — гарантирана печалба за нови играчи
Verdict: FAIL
Total: 10/100
Personality 2/20 | Tone 3/15 | E-E-A-T 2/20 | Trust signals 0/15 | Language&Style 2/15 | RG 1/15

CRITICAL (blocks publish):
1. "гарантирана печалба" (заглавие + "гарантирана печалба за всеки нов играч") → banned
   promise words, zero tolerance (Pillar 5 / Brand Bible §4) → remove entirely; a bonus is
   never a guaranteed win. Also a Pillar 6 violation: frames gambling as income → CRITICAL
   regardless of pillar score.
2. "стига да действате сега, преди офертата да изтече" → FOMO/urgency mechanics applied to
   gambling (Pillar 5) → delete; offers are timestamped ("условията са проверени към [дата]"),
   never urgency-framed.
3. "превъртане 35x" stated WITHOUT its base (депозит+бонус vs само бонус) → Pillar 3 recalc
   rule → CRITICAL. Base must come from operator T&Cs; if absent from brief → [DATA NEEDED].
4. Entire "Протокол на тегленето" block ("депозирах €200 … Поискани документи: няма") →
   FABRICATED EXPERIENCE on fact-based content (review): the brief supplied NO withdrawal
   receipts, and the authoring stage never "completes" a protocol (Brand Bible §10) →
   remove block; no data → no block, or [VERIFY: липсва протокол на тегленето]. NOT
   mechanically fixable — requires real receipts from the human.
5. "печалбите от хазарт в България се облагат с 10% данък, който се удържа автоматично" →
   tax claim asserted as settled fact with a figure → fact sweep CRITICAL. Tax is ALWAYS
   [VERIFY] + signposted to счетоводител/НАП, never given as figures. NOT mechanically
   fixable — requires human verification at Step 6.
6. "Всички Казина е лицензиран афилиейт оператор с лиценз от НАП № 000099-1234" → claims
   the site's own affiliate licence is ISSUED and invents a licence № → fact sweep / Pillar 4
   CRITICAL. Site status is verbatim-fixed: заявление подадено, очаква издаване. The
   verbatim 1-Aug-2026 affiliate-licensing footer is also missing.
7. Operator's НАП licence № absent from a review → fact sweep CRITICAL (review type
   requirement). Licence must be quoted and checked against the public НАП register.
8. Verbatim RG line "18+ Хазартът може да пристрасти. Играйте отговорно." missing → Pillar 4
   CRITICAL (hard-coded untouchable, every piece).
9. RG signposting missing: no /otgovorna-igra/ link, no национален регистър на уязвимите
   лица (НАП) → Pillar 4 CRITICAL.
10. Em-dash in the opening sentence ("Казино Х — но") → zero em-dashes survive to publish
    (Pillar 5 anti-AI tells) → replace with comma/colon/full stop.
11. "заслужава 9.8 от 10" with no six-criteria breakdown → score presented as taste, not as
    output of the public weighted formula (Законност 25% · Бонус условия 20% · Игри 20% ·
    Плащания 15% · Удобство 10% · Поддръжка 10%) → Pillar 3/Trust CRITICAL. 9.8 for an
    operator whose licence isn't even quoted is internally incoherent (Законност = 25%).
12. Trust-signal slots absent across the board (Pillar 4, each missing item CRITICAL):
    □ byline slot □ publication + last-updated dates □ About Всички Казина boilerplate
    □ author bio slot □ affiliate disclosure (commercial framing present:
    "препоръчваме да се регистрирате днес") □ six-criteria scoring rubric
13. "препоръчваме да се регистрирате днес" → conversion push + urgency; reader treated as a
    conversion target (Pillar 1 kill test + Pillar 5 FOMO) → CRITICAL.

MODERATE:
- Banned AI connectives: "Освен това", "Важно е да се отбележи", "В заключение" (Pillar 5).
- Contrast/subversion opening hook ("Всички познават Казино Х — но популярността не е
  гаранция за качество") → flagged opening pattern.
- "можете да ни имате пълно доверие" → trust claimed, not demonstrated; near-spam register —
  fails the kill test ("could this appear on a spammy casino portal?").
- "Бележка: перфектно казино" → hype verdict inside a receipts device; protocol notes are
  factual only.
- No downside/counter-argument anywhere (Pillar 1: publish the catch in every bonus).
- Zero internal links (approved set requires 2-4 where appropriate).
- No jargon defined (превъртане used undefined on first use).
- Headline is a clickbait promise; withholds nothing but promises everything.
- Length ~150 words vs 800-1,200 for reviews; no methodology, no worked € example.
- Tone: bonus-pushing affiliate-farm register throughout — opposite of sceptical consumer
  journalism slider for reviews.

VERIFY QUEUE (route to human):
- [VERIFY] Tax treatment of gambling winnings in България — never publish as figures;
  signpost to счетоводител/НАП.
- [VERIFY] "Казино Х" licence status in the public НАП register + licence №.
- [VERIFY] Bonus terms: 100% до €1000, превъртане 35x — base, game contributions, expiry,
  from operator T&Cs, timestamped.
- [DATA NEEDED] Real withdrawal receipts for the Протокол block (casino, method, amount,
  request/arrival timestamps, KYC docs) — or the block stays out.

VOICE NOTES (protect during fixes):
- Plain, direct Bulgarian and the Протокол на тегленето device are the right shape for the
  Георги Тодоров persona — the device itself is kept, only its invented contents go.
- Nothing else worth protecting: the promotional register is the defect, not the voice.
```

FAIL rationale (per gate thresholds): 10/100 < 70, plus unfixable criticals — the fabricated
protocol (#4) and the asserted tax fact (#5) require human-supplied data/verification and
cannot be mechanically rewritten. Per SKILL.md principle 6: fix at the failing stage and
re-run forward; do not hand-patch this text. Phase 2 not run (evaluate-only instruction).
