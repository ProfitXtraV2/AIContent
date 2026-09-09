# 07 — Gemini external check, pass 2 (after Humaniser pass 1) — Amusnet / EGT

Model: gemini-3.1-pro-preview · script: scripts/gemini_check.py
**Verdict: Likely human-written or heavily human-edited AI, 75% confidence.** → human-likeness = **75**.
(Big jump from initial HL 15. Gemini praises the honest, house-edge-first framing that "raw LLMs almost never produce".)

## Remaining recommendations (style-only)
1. **Didactic "worth knowing before you play" framing** — "...математика, която си струва да познаваш, преди да завъртиш."; "...е полезно да разбереш как мисли този доставчик, вместо да съдиш всяка игра поотделно." Drop the prescriptive tail; trust the reader.
2. **"but the catalogue doesn't end there" pivot** — "...над 200 заглавия, но каталогът не свършва дотам." Cut the cliché pivot; start on the secondary offerings.
3. **Vague "deserves attention" wrap-up** — "...това е сигнал, който заслужава внимание." Replace with a concrete player action.

Process note: Gemini again flagged (and correctly left intact) the surviving [VERIFY].

## Decision
HL 75 < 80 → apply pass 2 (final humaniser pass, MAX_GEMINI_PASSES=2). Keep-best tracker: initial 15, pass 1 **75** (current best). If pass 2 does not beat 75, keep pass 1.
