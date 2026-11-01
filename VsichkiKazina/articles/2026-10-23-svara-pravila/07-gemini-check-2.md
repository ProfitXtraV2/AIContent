# 07 — Gemini check, pass 2 (after humaniser pass 1)

Command: `python3 scripts/gemini_check.py .../05b-final-draft.md`
Exit: 0

**Verdict: Shows AI patterns, 80% confidence.** → normalized human-likeness = 100 − 80 = **20** (< 80) → needs changes.
NOTE: pass 1 was HL25; this pass dropped to HL20 (humaniser pass LOWERED the score — classic noisy/adversarial detector, goalposts relocate each pass: it now flags "advisory wrap-ups" it did not flag before, and praises nothing). Keep-best will apply at loop end.

---
(verbatim Gemini output)

**Verdict: Shows AI patterns, 80% confidence.**

Structural skeleton gives it away: "neatly packaged" paragraphs ending in a moralizing/summarizing wrap-up, explicit signposting, mild unearned drama in simple card mechanics.

### 1. Over-Philosophical Hook / Narrated Drama
"…но залагането около картите тежи поне колкото тях: често банката отива при онзи, който е накарал останалите да се откажат…" → "not just X but Y", inflates bluffing. Rec: state plainly winning is about betting/forcing folds, not just best cards.

### 2. Explicit Signposting
"…а за свара на пари става дума по-долу." → fourth-wall layout announcement. Rec: delete; end at "играта е друга работа".

### 3. Advisory Wrap-Up (formulaic endings)
"…затова е добре да се сверите, преди да седнете." / "Дали я играете изобщо е една от уговорките, които се разбират преди игра." / "…всичко това се сверява на масата." → "bow-tie" advisory enders; the "agree on rules beforehand" idea reused to tie off 3 sections. Rec: truncate; consolidate variations into "Какво се уговаря на масата" only.

### 4. Dictionary-Style Opening
"Свара е и името на играта, и името на това, което става при равенство." → tautological definitional framing. Rec: merge into the action — explain the tie, note it's where the game gets its name.

### 5. Melodramatic Transition
"Сметката се мени в мига, в който залагате реални пари срещу непознат в интернет." → stylized cliché pivot. Rec: plainer transition.

(Compliance/RG/bio/affiliate ignored per instructions.)
