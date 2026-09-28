# 07 — Gemini external check, pass 1 (initial draft) — Endorphina

Model: gemini-3.1-pro-preview · script: scripts/gemini_check.py
**Verdict: Likely AI-generated (or heavily AI-assisted), 85% confidence.** → human-likeness = **100 − 85 = 15**. → **BELOW** GEMINI_TARGET_CONFIDENCE (80). Needs a Humaniser pass.

(A second probe of the same draft read "Shows AI patterns, 75%" → HL 25; the detector is noisy on this provider-profile structure. Either way the initial is below 80, so a Humaniser pass is warranted. Baseline recorded as HL 15.)

Gemini praised the semantics ("avoids casino fluff, correctly identifies that certificates don't change the house edge, realistic RTP advice") but flagged structural AI tells:
1. Faux-familiar hook: „едно от онези студиа, чиито игри разпознаваш по стила…".
2. "From X to Y, but the unifying factor is Z" spectrum formula in the themes sentence.
3. Paragraph-ending summary bows („Тази фокусираност личи…", „Те дават представа за диапазона…").
4. Didactic "let me explain" phrasing („За да е ясно какво значи този процент:"; textbook provider-vs-operator definition).
5. Prompt fixation: the "check the info panel" instruction hammered in intro + RTP + caption + top-titles.

Process note: Gemini correctly left the [VERIFY] flag intact and confirmed the 18+/RG/affiliate untouchables are unaltered.

## Decision
HL 15 < 80 → apply the flagged recommendations through a fresh Humaniser pass (step-7b), preserving every untouchable (numbers, MGA/ONJN/GLI, [VERIFY], 18+, RG, affiliate footer, byline, brand, dates, links, image refs), then re-check (pass 2).
