# 07 — Gemini Step-7 Check · Pass 1 (initial draft)

Script: scripts/gemini_check.py · Date: 2026-09-19

## Verdict (verbatim summary)
**Verdict: Likely human-edited AI draft (or heavily AI-assisted human writing), 75% confidence.**
Normalized HUMAN-LIKENESS = 75 → below target (80). Iterate.

Grounded, factual, avoids egregious clichés. Flagged:
1. POV shift — intro uses formal "сте пускали / сте виждали", body uses informal "ти" (Отвори/Задай си).
2. Hero alt-text reads like a generative image prompt ("вдъхновена от студио като Thunderkick").
3. Bow-tie summary endings: "Този бутиков подход обяснява защо..., а не като поредната ротативка"; "...което прави разликата между дребен и едър резултат."
4. Dictionary insertion: "висока, тоест печалбите са редки, но потенциално големи."
5. Filler signpost: "Няколко заглавия направиха студиото разпознаваемо."

## Decision
Below 80 → apply recommendations via Humaniser (step-7b), preserve every number/link/RG/byline/brand,
then re-check (pass 2). Baseline human-likeness recorded = 75 for keep-best.
