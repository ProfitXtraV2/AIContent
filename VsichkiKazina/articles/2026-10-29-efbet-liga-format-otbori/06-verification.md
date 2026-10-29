# 06 — Verification — 2026-10-29-efbet-liga-format-otbori (vk-0314)

## Surviving flags
- [VERIFY]: 0
- [DATA NEEDED]: 0
Nothing blocks on flags. The text contains no operator T&C/bonus/licence claim and no tax claim.

## Time-sensitive / changeable claims — framing + sources
All season-variable facts are stamped or deferred to official sources (brand anti-stale rule):
- Team count & group split: presented as the **2025/26** arrangement (16 отбора; горна четворка 1–4 /
  бараж-група 5–8 / оставане 9–16) and explicitly flagged that the league reverts to **14 отбора from
  2026/27** and that the exact per-season schema is in the БФС/ПФЛ regulation. No single season's split
  is asserted as the permanent format.
- Live standings / results / TV-rights holder: NOT printed; reader pointed to the official league/БФС
  channels (they change every round / per rights cycle).
- Trophy counts stamped „към 2026 г.".
Sources (evergreen/encyclopaedic, no live data):
- en.wikipedia.org/wiki/First_Professional_Football_League_(Bulgaria)
- en.wikipedia.org/wiki/2025–26_First_Professional_Football_League_(Bulgaria)
- bg.wikipedia.org/wiki/Първа_професионална_футболна_лига
These three agree on: renaming 7 June 2016; efbet title sponsor since 2019; league since 1948 (A Group),
championship since 1924; organisers БФС + ПФЛ; records ЦСКА 31 / Левски 27 / Лудогорец 14 (record 14
consecutive). The pages themselves flag season-to-season format variance → handled by the stamped +
defer-to-official framing above.

## Recalculated figure (working shown)
Claim: „16 отбора · 30 кръга · всеки срещу всеки, разменени гостувания" (2025/26).
Check: in a double round-robin each club plays every other club twice (home + away).
  opponents per club = 16 − 1 = 15; rounds = 15 × 2 = 30. ✓ Matches „30 кръга".

## External check (Gemini Step 7) — cross-model, style-only
- check 1 (initial 05b): „Shows AI patterns 75%" → human-likeness 25.
- check 2 (humaniser pass 1): „Shows strong AI patterns 85%" → human-likeness 15.
- check 3 (humaniser pass 2): UNSTABLE on identical text — 85% (HL 15) then 65% (HL 35) on re-run.
- KEEP-BEST = humaniser pass 2 (highest HL seen = 35; editorially tightest; incorporated Gemini's own
  redundancy fixes). 2 humaniser passes applied (= MAX_GEMINI_PASSES). All versions below the 80 gate →
  gemini column `ai 65`, flagged for the human's Step-6 read. Detector noise documented in 07-check-3.
  Gemini touched no facts/numbers/links/RG/disclosures (style-only; its „remove the official-source
  pointers" suggestion was NOT applied — those are a deliberate brand anti-stale compliance feature).

## Images (Step 8)
images: 2 (infographic 100, hero 100). Gemini image review pass 1 = **100 PASS**, 0 integrity failure.
- efbet-liga-format-sezon.svg — numbers 1:1 from 05b, rendered & layout-verified (no clip/overlap).
- efbet-liga-struktura-hero.webp — 7 KB, abstract pitch/tiers, no text/logos/people.

## Brand Gate (Step 5)
PASS 95/100, 0 CRITICAL. Byline Георги Тодоров; brand „Всички Казина"; 0 em-dashes; verbatim 18+ RG line
+ /otgovorna-igra/ + регистър на уязвимите лица + Солидарност; affiliate footer verbatim (pending licence,
no №). 4 body internal links (zakonno-li-e, bonus-ruletka/sport/vsichki, blog/futbol,
blog/responsible-gambling) + /otgovorna-igra/ footer. ~816 words.

## Human-action list (Step 6, owner)
- Routine style read: Gemini scored this below 80 (noisy detector). Optionally a light human pass, but
  the keep-best (pass 2) is the tightest version and compliant.
- Add sibling club links (Лудогорец/Левски/ЦСКА) once those profiles go live on the sitemap.
- Nothing to resolve: 0 flags.
