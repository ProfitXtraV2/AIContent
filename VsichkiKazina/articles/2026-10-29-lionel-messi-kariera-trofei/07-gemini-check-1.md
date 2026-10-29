# 07 — Gemini check, pass 1 (initial draft) — FINAL / PASS

**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**
→ human-likeness = **85** → **PASS** (≥ GEMINI_TARGET_CONFIDENCE 80) and the **best state seen**.

No Humaniser pass applied: the initial draft already clears the bar. Over-editing a passing
draft risks lowering the score and stripping voice (daily-run keep-best + MAX_GEMINI_PASSES
policy), so the initial 05b is kept verbatim. Recommendations below are optional polish only;
not applied (no fact/number/RG/link touched either way).

## Verbatim verdict + flagged patterns (Gemini, gemini_check.py)

> **Verdict: Likely human-written (or heavily human-edited), 85% confidence.**
>
> This article reads exceptionally well and avoids the vast majority of raw LLM tells. The final
> section ("На пари, отдалеч...") is the strongest indicator of human authorship. It uses a
> grounded, slightly cynical, and highly colloquial tone ("доста по-приземена тема", "горе-долу
> единствената гаранция в цялата схема") that AI fundamentally struggles to replicate. AI usually
> handles gambling disclaimers with robotic, preachy solemnity; this writer handles it with
> natural, conversational pragmatism.
>
> However, the first half of the article (the biographical sports section) exhibits a few minor
> structural rigidities and formulaic phrasing patterns.
>
> **1. The "Thesis Statement" Hook** — *"Тази цифра сама обяснява защо разговорът за най-добрия
> футболист на всички времена почти винаги минава през неговото име."* LLMs tend to justify why
> an article is being written in the intro (meta-commentary about "the conversation").
>
> **2. The Cliché Triad** — *"Дрибъл на тясно пространство, точен последен пас и изпълнение на
> преки свободни удари са запазената му марка."* Three-part noun list capped with a cliché
> ("запазената му марка").
>
> **3. Encyclopedic Signposting** — the H2 sequence reads like a standard generated outline;
> isolated "database entries" rather than a flowing narrative.
>
> Recommendations: state the Ballon d'Or impact directly without meta-commentary; break the triad
> into active verbs; add transitional tissue between sections.
>
> *(Note: responsible-gambling language, 18+ markers and affiliate disclosures are perfectly
> integrated, compliant, and were not factored into AI-detection scoring per the hard rules.)*

## Keep-best ledger (human-likeness)
| state | file | HL | note |
|---|---|---|---|
| initial draft | check 1 | **85** | PASS; 3 optional style flags, none applied (already ≥80) |

**Winner = initial draft (current 05b), human-likeness 85.** Recorded in content-queue `gemini`
column as **human 85**.
