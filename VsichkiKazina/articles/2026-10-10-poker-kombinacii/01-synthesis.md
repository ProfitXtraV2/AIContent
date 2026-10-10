# 01 — Synthesis · vk-0263 · Покер комбинации

**Primary intent:** reference lookup — „покер комбинации" = подредбата на ръцете, от най-силната
към най-слабата. Searcher wants the hierarchy fast, plus how ties break.

**Casino framing (what makes this OUR page, not a generic poker page):**
- В казино покера играеш срещу дилъра или срещу платежна таблица, не срещу масата от играчи.
  Комбинацията решава showdown-а и колко плаща ръката, нищо повече.
- Подредбата е еднаква за 5-картовите варианти (Casino Hold'em, Caribbean Stud, Ultimate Texas,
  видеопокер). Три карти покер е изключението: при 3 карти стрейтът е по-рядък от флъша, затова
  там стрейт бие флъш — важен нюанс, който обърква хората.
- Знанието на подредбата = правилни решения на showdown, но НЕ мени домашното предимство (то
  е заключено в правилата и таблицата на конкретния вариант). Това е честният ъгъл.

**Core facts (standard, verified web 2026-10-10):**
1. Роял флъш — A-K-Q-J-10 от една боя (най-силната, асо-висок стрейт флъш).
2. Стрейт флъш — 5 последователни от една боя.
3. Каре — 4 еднакви ранга.
4. Фул хаус — 3 + 2.
5. Флъш (цвят) — 5 от една боя, без ред.
6. Стрейт (кента) — 5 последователни, смесени бои.
7. Тройка (трика) — 3 еднакви ранга.
8. Два чифта.
9. Чифт (двойка).
10. Старша (най-висока) карта.

**Tie-breakers:** по-високата карта в стрейт/флъш; при еднакъв чифт решава кикерът (най-високата
странична карта). Асо високо (10-J-Q-K-A) или ниско (A-2-3-4-5 „колело").

**Structure decision (anti-template):** core = ranking ladder (list, но с разнородни описания, не
еднакъв шаблон на ред). После: как се решават равни ръце; казино изключението (3 карти); защо
подредбата не мени предимството. Asymmetric close (practical, not a both-sides bow).

**Flags anticipated:** none mandatory. No operator/НАП/tax. Any probability figure → примерни or omit.
**Images:** 1 SVG ladder-infographic (ranks 1–10 + example-card notation; all „numbers" = rank
positions/card notations traceable to 05b), + optional decorative hero (textless card motif).
