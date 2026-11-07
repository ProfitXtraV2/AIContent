# Step 7 — Gemini cross-model check (pass 1, INITIAL draft)

Script: `python3 scripts/gemini_check.py 05b-final-draft.md` · $GEMINI_API_KEY set · 2026-11-06

## Normalized score
Verdict phrasing: **"Likely human-written (or heavily human-edited), 85% confidence on the prose"**
→ human-likeness = **85** (phrasing „Likely human-written, X%" → HL = X).
85 ≥ GEMINI_TARGET_CONFIDENCE (80) → **PASS on the initial draft.**
Keep-best: baseline is the only + highest version (85). No humaniser pass (a pass risks lowering HL; PASS stops the loop).

## Gemini verdict + recommendations (verbatim)

**Verdict: Likely human-written (or heavily human-edited), 85% confidence on the prose, but with obvious AI-assisted workflow remnants.**

The actual prose of this article is excellent and reads like a native Bulgarian human wrote it. It avoids the classic AI buzzwords (no "В днешния забързан свят" or "Нека се потопим"), uses highly natural idioms ("различен на вкус", "едва ли ще мръднат скоро"), and features a grounded, almost cynical tone in the gambling section ("доста по-приземен въпрос от романтиката на тревата") that AI struggles to replicate without sounding overly dramatic.

However, the structural framing and the metadata/image tags give away that an AI was used in the drafting or production process.

### 1. The "Midjourney Prompt" Alt Text (Workflow Tell)
Pattern: AI image generation prompts left as HTML alt text.
Quote: `![Плоска илюстрация на тревен тенис корт, видян отгоре, със стилизирана мрежа и бели очертания на игрището, без играчи, без лица, без лога](images/uimbaldon-treven-kort-hero.webp)`
Why it flags: Phrases like "без играчи, без лица, без лога" are negative prompts used to control AI output, not descriptive alt text.
Recommendation: Rewrite the alt text to describe the image naturally; strip the negative-prompt instructions.

### 2. The "Neat Bow" Summary Conclusion (Structural Pattern)
Quote: "Уимбълдън устоя на изкушението да мине на бързи синтетични настилки и остана верен на тревата, на бялото и на ягодите. Затова и след почти век и половина е турнирът, който мнозина искат да спечелят повече от всеки друг."
Why it flags: reads like a checklist of the H2s (grass, white clothes, strawberries).
Recommendation: Delete the first sentence of the conclusion; let it start directly with the prestige / merge into the betting warning.

### 3. The Formulaic H1 (Structural Pattern)
Quote: "Уимбълдън: най-старият тенис турнир и какво го прави различен"
Why it flags: ChatGPT defaults to "Topic: Description and what makes it unique".
Recommendation: Tighten the H1; drop "какво го прави различен" half or make it more specific.

### 4. Unresolved Editor Tags (Process Issue)
Quote: "...се сочи Роджър Федерер с осем титли на сингъл [VERIFY], а при жените Мартина Навратилова с девет [VERIFY]."
Why it flags: editorial placeholders. Recommendation: route to fact-checking to verify + remove [VERIFY] before publication. (Per your rules, I am not touching or removing these myself.)

## Decision
PASS at 85 human-likeness. Recommendations #1–#3 are style-only and below the iterate trigger (already ≥80);
#4 is a required human-owned fact-check flag that the pipeline deliberately preserves in the text.
No humaniser pass applied. `gemini` column → `human 85`.
