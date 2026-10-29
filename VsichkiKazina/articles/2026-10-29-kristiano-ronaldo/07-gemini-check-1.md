# 07 — Gemini check, pass 1 (initial draft)

**Verdict: Hybrid / Shows strong AI patterns in the core content, 85% confidence.**
→ normalize: "Shows AI patterns, 85%" → human-likeness = 100 − 85 = **15** → below GEMINI_TARGET_CONFIDENCE (80) → iterate (Humaniser pass 1, apply recs).

## Verbatim verdict + flagged patterns (Gemini, gemini_check.py)

> ### Verdict
> **Hybrid / Shows strong AI patterns in the core content (85% confidence).**
> The article exhibits a classic "cyborg" footprint. The first 75% (the biographical sections about Ronaldo) reads like a standard, zero-shot LLM generation—it is rigidly chronological, highly formulaic, and relies on sweeping, grandiose conclusions. However, the final section (`На пари, отдалеч...`) and the compliance footers are strikingly human, featuring grounded, colloquial Bulgarian phrasing and highly specific local regulatory knowledge.
>
> **1. Pattern: Paragraph-Ending Grandiosity (The "Epoch" Wrap-up)**
> LLMs almost always default to profound, sweeping statements that summarize an era or tell the reader how to feel.
> - „...а това съперничество белязва цяло футболно десетилетие и вдигна летвата за всички около тях."
> - „...се превърна в разпознаваема картина от едно цяло поколение."
> - „Там, на „Олд Трафорд", талантът за пръв път се превръща в постоянни резултати."
>
> **2. Pattern: Formulaic Chronological Signposting**
> The subheadings read like an LLM outlining a prompt chronologically rather than thematically.
> - „От Мадейра до „Манчестър Юнайтед" -> „Годините в Англия" -> „Рекордите с „Реал Мадрид" -> „Ювентус", кратко завръщане и Саудитска Арабия"
>
> **3. Pattern: Cliché / Sports Documentary Voiceover**
> - „...от техничар по фланга в истински голаджия." (too-colloquial attempt at localized slang)
> - „...доиграе мача от резервната скамейка, помагайки с думи." (awkward phrasing; a human writer would say he motivated the team from the touchline)
>
> **Recommendations:** kill the grandiose paragraph-ending summaries (let the facts carry the weight); break/soften the chronological formula; fix awkward literal translations („помагайки с думи" → надъхвайки съотборниците си от тъчлинията); carry the grounded voice of the final section into the biographical sections.
>
> *Note on Compliance: responsible-gambling language, 18+ markers, the ZDB 2026 affiliate disclosure and the NAP references are perfectly executed. Do not touch or alter any of this text.*

## Keep-best ledger (human-likeness)
| state | file | HL | note |
|---|---|---|---|
| initial draft | check 1 | **15** | below 80 → apply Humaniser pass 1 (style-only; facts/numbers/links/RG untouched) |

→ Proceed to Humaniser pass 1 using pipeline/prompts/step-7b-apply-gemini-recs.md.
