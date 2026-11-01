# 07 — Gemini check, pass 1 (baseline draft) · vk-0297

Model: gemini-3.1-pro-preview · file checked: 05b-final-draft.md (initial)
Normalized HUMAN-LIKENESS = 100 − 85 = **15** ("Shows AI patterns, 85% confidence").

## Verdict (verbatim)
Shows AI patterns, 85% confidence. While the text successfully avoids the most egregious AI clichés (like „В днешно време" or „Нека се потопим в..."), it exhibits a highly specific "prompt-adherence" pattern. It reads exactly like an LLM that was given strict instructions to "not hallucinate," "be objective," and "flag unverified information." The result is a robotic, overly cautious tone where the "author" constantly narrates their own editorial limitations. Additionally, there is a glaring process issue: the [VERIFY: ...] tags have survived into the final text (not suggested for removal; flagged as a workflow tell).

## Flagged passages / patterns (verbatim)
1. Instruction-leak / robotic over-hedging:
   - „...не го твърдим, преди да го видим потвърдено;"
   - „...не посочваме конкретна сума за прага, преди да я сверим с официалните правила."
   - „...но не твърдим число, преди да го потвърдим в правилника на играта или на пункта."
2. Meta-commentary / signposting:
   - „Печелившите числа няма да ги изписваме тук, защото се сменят с всеки тираж; ще ви покажем къде стоят официалните."
   - „...ние нарочно не ги преписваме, защото се менят на всеки тираж и на другия ден подвеждат."
3. Forced metaphor / AI "cleverness": heading „Преди да хванете калкулатора на късмета".
4. Formulaic didactic RG tone: „Лотарията е платено забавление, а не план за доходи, и един печеливш фиш не променя това."

## Concrete recommendations (verbatim, condensed)
- Fix over-hedging: shift focus to the user's action / the dynamic nature of the rules, not „we refuse to claim". App → advise exploring the app's current features; payout threshold → state it depends on current operator rules.
- Eliminate meta-commentary: just state where official winning numbers are, drop the „we won't write them here because…" framing.
- Neutralize the metaphor heading → e.g. „Разумна игра" or „Цена на играта и отговорност".
- Process: resolve the [VERIFY] tags (human fact-check team) — do NOT hide them.

## Decision
HL 15 < gate 80 → iterate. Apply the style recs through a fresh Humaniser pass (step-7b),
KEEPING every [VERIFY] flag, link, RG substance, byline/brand/footer; never paste Gemini's text.
Record baseline HL=15 for keep-best.
