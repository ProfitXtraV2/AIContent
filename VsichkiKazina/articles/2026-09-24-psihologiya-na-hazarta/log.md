# LOG · vk-0169 · 2026-09-24-psihologiya-na-hazarta

## Pipeline stages
- 00-brief: real web research (WebSearch ×4) on gambler's fallacy / Monte Carlo 1913 origin, near-miss neuroscience (Clark et al. 2009), Langer illusion of control, loss chasing. Sources cited in 00-brief. Two hard figures flagged and deliberately omitted (near-miss ~30%; loss-chasing >82%).
- 01-synthesis: entity union, verified facts, excluded claims (RNG internals + bankroll sizing excluded for anti-cannibalization), no material conflicts.
- 01.5-outline: 6 sections + intro, deliberately varied shapes, infographic marker placement, link placement.
- 02-draft: editorial voice (patient teacher), signed Георги Тодоров. Concept-only, no numbers to fabricate.
- 03-humanised: Phase-1 MIXED → surgical fixes (removed demonstrative amplifiers „Именно/точно затова", reveal lead-ins „простия факт:"/„...е проста:", and the „не е песимизъм, а..." antithesis). Voice preserved.
- 04-seo: title tag + meta (both under limit, primary keyword present); added English search variants „gambler's fallacy"/„near-miss" on first mention; 3 internal links from approved live set. Final-stage enrichment (see below) mirrored here.
- 05-gate: PASS, 90/100, zero criticals.
- 05b-final-draft: skeleton followed exactly; HERO_IMAGE + INFOGRAPHIC_1 markers in place; verbatim RG + affiliate footers + byline block pasted verbatim.

## Final-stage enrichment (to clear 900-word floor with real substance, not padding)
Added ~100 words of sourced concept detail across three sections (mirrored in 04-seo):
- GF: result boards / spin-history displays exist to feed the „закъснял" feeling though they carry no predictive info.
- Illusion of control: Langer's lottery-ticket experiment (self-chosen ticket valued higher at equal odds).
- Loss chasing: the sunk-cost feel („вече вложеното") that makes standing up harder.

## Final self-check
- `grep -c "—" 05b-final-draft.md` = 0 (em-dash) ✔
- en-dash „–": 1 occurrence, in the time range 10:00–17:00 (allowed) ✔
- Byline „Георги Тодоров" present ✔
- Brand „Всички Казина" spelled correctly (footers) ✔
- Verbatim „18+ Хазартът може да пристрасти. Играйте отговорно." present (body + footer) ✔
- `/otgovorna-igra/` (×3) + национален регистър на уязвимите лица (НАП) + Солидарност 0888 99 18 66 present ✔
- Affiliate footer present verbatim ✔
- Internal links (3 distinct, approved live set): /blog/rechnik-kazino-termini/, /otgovorna-igra/, /blog/responsible-gambling/ ✔
- Body word count: 946 (target 900–1500, aim ~1000–1200; within range) ✔
- Surviving [VERIFY] flags in body: NONE. (Two figures kept out of text by design — see 00-brief/05-gate.)

## Notes for orchestrator
- INFOGRAPHIC_1: concept diagram „четирите капана" (капан → защо мами → какво да помниш). NO numbers — concept labels only. Suggested rows below.
- HERO metaphor: abstract brain/head silhouette as a circuit or maze with a slot-reel/dice pattern inside and looping arrows; textless, no faces.

--- orchestrator (fire 3, 2026-09-24) ---
Step 7 (Gemini text): initial HL15 → p1 HL20 → p2 HL20, kept best p2 (cleanest), recorded ai 80 (niche baseline ~20-25)
Step 8 (images): 2 (faceless brain/circuit hero + 4-traps SVG); review 100 PASS p1, 0 integrity
Verification: 0 [VERIFY], 0 [DATA NEEDED], 0 [CONFLICT]. Hard rules: 0 em-dashes, byline Георги Тодоров, brand Всички Казина, verbatim 18+ + /otgovorna-igra/ + НАП регистър + Солидарност, affiliate footer. Guides-only scope respected (0 operator/НАП facts).
Outcome: drafted → content PR. Human owns Step-6 flag-resolution/approve/merge/publish.
