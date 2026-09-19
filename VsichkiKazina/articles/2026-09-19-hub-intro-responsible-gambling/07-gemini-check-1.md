# Step 7 — Gemini check, pass 1

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-09-19-hub-intro-responsible-gambling/05b-final-draft.md`

Normalized human-likeness: **85** ("Likely human-written, 85% confidence" → human-likeness = 85).
GEMINI_TARGET_CONFIDENCE = 80 → **PASS** (85 ≥ 80). No Humaniser re-pass needed.

## Verbatim Gemini output

**Verdict: Likely human-written, 85% confidence.**

This text reads like it was written by an experienced human iGaming writer or affiliate manager. It contains cynical, pragmatic nuances that AI almost never generates on its own without highly specific prompting (e.g., noting that support won't cancel self-exclusion "колкото и убедително да звучи молбата" [no matter how convincing the request sounds], or calling out offshore licenses as being hung on the site "колкото да изглежда сериозно" [just to look serious]).

However, the structural formatting and some repetitive phrasing mimic AI patterns. It looks like a human wrote it, but they wrote it in dense, blocky paragraphs that visually resemble a zero-shot ChatGPT output.

Here is the breakdown of the patterns that trigger AI-detection flags and how to fix them.

### 1. Pattern: Inline Listing (The "Wall of Text")
AI often struggles with formatting unless explicitly told to use bullet points, resulting in long, comma-separated lists buried inside thick paragraphs. Humans reading online hate this; AI defaults to it.

*   **Flagged Passage:** *"Признаци, че играта вече е проблем: увеличаване на залога след загуба с цел да се навакса, заемане на пари за игра, укриване пред близки на времето или сумите, поредица от депозити в една вечер след предходна загуба."*
*   **Recommendation:** Break this specific sentence out into a bulleted list. Give "Признаци, че играта вече е проблем:" its own line, followed by 3-4 bullet points. This immediately shatters the "AI wall of text" illusion and improves UX.

### 2. Pattern: Thematic Looping (Echoing the Thesis)
AI models are trained to be helpful and comprehensive, which often results in them stating their main thesis in the intro, repeating it in the body, and summarizing it again at the end.

*   **Flagged Passages:**
    *   *(Intro)* "...зададени преди първия залог."
    *   *(H2 1)* "Лимитите работят само ако са зададени предварително, не при първия сигнал за проблем."
    *   *(H2 2 Conclusion)* "Хазартът остава развлечение с предвидима цена само докато лимитите са зададени предварително, а не след първата по-голяма загуба, когато вече е късно да помогнат."
*   **Recommendation:** The repetition at the very end of the article feels like an AI generating a concluding summary. I recommend trimming or entirely cutting the final sentence of the article. The preceding sentence (about where to file complaints) is a much stronger, more natural place to end the text.

### 3. Pattern: Over-Defensive / Robotic Caveats
When AI is prompted to be objective or compliant, it often generates clunky, overly defensive meta-commentary to explain *why* it is mentioning a brand.

*   **Flagged Passage:** *"Изборът на казино с лиценз от НАП, като Betano, тук не е препоръка какво да предпочетеш за игра, а илюстрация на условието по-горе: без лиценз няма гаранция, че лимитите изобщо съществуват извън общите условия, само на хартия."*
*   **Recommendation:** Smooth out this sentence. You can keep the compliance aspect, but advise the writer to make it punchier. Instead of the robotic "this is not a recommendation but an illustration of the condition above," suggest they simply state that brands like Betano are examples of licensed operators where limits are guaranteed, whereas offshore sites only offer them on paper.

### 4. Pattern: Asyndeton / List Fatigue
AI frequently strings together nouns or scenarios without conjunctions to sound authoritative and comprehensive.

*   **Flagged Passage:** *"При спор с оператор, забавено теглене, отказано плащане, оспорен бонус, жалбата се подава писмено..."*
*   **Recommendation:** Suggest adding a conjunction (like "или" / "or") before the final item in that list to make it flow like natural human speech, rather than a robotic data dump.

***Note on Hard Rules:** The mandatory responsible gambling text ("18+ Хазартът може да пристрасти. Играйте отговорно.") at the end of the intro is perfectly placed. Do not alter or move it.*

## Disposition
PASS at 85 ≥ 80 — per daily-run.md Step 7 policy, no Humaniser re-pass is required on
a PASS. Recommendations noted for the record but not applied: item 3's suggested rewrite
would weaken the required non-promotional disclaimer for the Betano link (task brief
explicitly requires framing it as NOT a recommendation), so it is kept as-is rather than
"smoothed" per the recommendation. Items 1/2/4 are minor formatting/style preferences
that would not move the score meaningfully and risk the hub-intro's no-list constraint
(item 1 suggests bullets; hub-intro spec keeps this as prose, no new lists). 05b-final-
draft.md is unchanged and is the version kept (highest/only human-likeness seen: 85).
