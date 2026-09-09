# Flag Resolution Log

Record of editorial FLAG removal from `05b-final-draft.md` drafts so they pass the
publisher's hard block on leftover `[VERIFY]` / `[DATA NEEDED]` / `[CONFLICT]` /
bracket placeholders. Each entry: flags found, how each was resolved
(stated-with-caveat / softened / pointed-to-authority), post-fix gemini verdict.
Rules: no fabricated values; tax/licence/operator-T&C never asserted as fact.

---

## 2026-09-09 — batch flag resolution (5 branches)

Resolver: automated editorial pass. Public game/provider data may be stated;
disputed specifics softened to non-specific; no values invented.

### content/2026-09-08-20-super-hot
- **Flag (line 10):** `[VERIFY: точната година на пускане се цитира различно…]` — exact release year disputed across sources.
- **Resolution: softened.** Removed the specific-year claim entirely (no year was ever stated; the caveat itself was the risk). Rephrased to a true, non-specific statement: "Няма да заковаваме точна година на пускане: това е класика от епохата на наземните автомати, пренесена почти непроменена онлайн."
- **Post-fix gemini verdict:** humaniser critique only (H2 heading cadence, "като" overuse, wrap-up paragraph); no blocking issue. 0 markers, 0 em-dashes.

### content/2026-09-08-keno-pravila
- **Flag (line 22):** `[VERIFY: диапазонът 60%–95% за pick-6 е илюстративен ориентир…]` — paytable RTP range is illustrative, depends on the table.
- **Resolution: stated-with-caveat.** Kept the 60%/95% figures, folded the caveat in: "Тези проценти са ориентир от обучителни източници, а не фиксиран стандарт: реалният диапазон зависи изцяло от конкретната таблица на казиното, затова винаги проверявай нейните коефициенти, преди да заложиш."
- **Flag (line 30):** `[VERIFY: тези стойности са приблизителни…]` — hit-frequency estimates (1-in-4, 1-in-17, 1-in-73).
- **Resolution: stated-with-caveat.** Kept the frequencies, folded the caveat: "Това са приблизителни ориентири: точната честота зависи от това колко числа си избрал и от конкретната таблица."
- **Post-fix gemini verdict:** "Shows AI patterns, 85% confidence" (humaniser style flags: hooks, parallel structure, translated idioms). No blocking flag. 0 markers, 0 em-dashes.

### content/2026-09-09-40-super-hot
- **Flag (line 34):** `[VERIFY: операторите понякога пускат различни версии с различен RTP…]`
- **Resolution: stated-with-caveat / pointed-to-authority.** Kept the announced 95.81% RTP, folded the caveat pointing the reader to the game's info panel: "Имай предвид, че някои оператори пускат версии с различен RTP, затова провери точния процент в инфо-панела на конкретното казино, преди да заложиш." Internal /kak-ocenyavame/ link preserved.
- **Post-fix gemini verdict:** "Likely human-written (or heavily human-edited AI), 85% confidence." 0 markers, 0 em-dashes.

### content/2026-09-09-gates-of-olympus
- **Flag (line 26):** `[VERIFY: точните по-ниски версии на RTP и коя работи в конкретното казино…]`
- **Resolution: stated-with-caveat / pointed-to-authority.** Kept default 96.50% and the noted lower versions (95.5% / 94.5%), folded a check-the-info-panel caveat: "Коя точно работи при теб проверяваш в инфо-панела на играта в конкретното казино, защото именно там пише реалната стойност."
- **Flag (line 33):** `[VERIFY: наличността на купуването на бонуса зависи от пазара…]`
- **Resolution: softened / pointed-to-authority.** No market-specific assertion made; reworded to: "Дали купуването на бонуса изобщо е налично, зависи от пазара и от конкретния оператор, затова провери дали опцията присъства в самата игра, преди да разчиташ на нея."
- **Post-fix gemini verdict:** "Highly likely human-written, 90% confidence." 0 markers, 0 em-dashes.

### content/2026-09-09-live-game-shows
- **Flag (line 22):** `[VERIFY: точната долна граница на RTP по залог при Monopoly Live се сочи различно…; стабилно потвърден е върхът около 96.23%.]`
- **Resolution: stated-with-caveat (peak) + softened (lower bound).** Kept the confirmed peak of ~96.23% on number bets; kept the lower bound non-specific ("някъде към 80-те процента") and folded the caveat: "Точната долна граница се сочи различно в различните игрови бази, затова я приемай като груб ориентир, а не като заковано число; сигурно потвърдена е горната стойност от около 96.23% на залозите върху числата."
- **Post-fix gemini verdict:** "Likely human-written (or expertly human-edited), 85% confidence." 0 markers, 0 em-dashes.

### Summary
- Branches fixed: 5. Flags resolved: 7 (all `[VERIFY]`, all on public game/provider data).
- No tax / licence-number / operator-T&C fact was asserted. No value fabricated.
- Post-fix full-repo re-scan: zero blocking markers in any content branch `05b-final-draft.md`.
