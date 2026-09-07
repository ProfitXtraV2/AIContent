# Step 7 — External cross-model check (Gemini)

Canonical prompt sent to Gemini (a different model family than the writer) to detect
AI-writing patterns. **Recommendations only** — the article is rewritten, if needed, by a
fresh Humaniser pass (`step-7b-apply-gemini-recs.md`), never by Gemini directly.

## PROMPT (verbatim — send with the finished article appended)

Act as a senior copywriter with deep knowledge of LLM writing patterns and AI-generated text detection. You will be given a finished, human-verified article. Evaluate whether it reads as AI-written.

Give me:

- A verdict with confidence level (e.g. "Likely human-written, 80% confidence" or "Shows AI patterns, 65% confidence").
- The specific passages and patterns that triggered your assessment — quote the exact text and name the pattern (e.g. staccato rhythm, signposting, narrated emotion, formulaic structure, over-polished tables/lists, em-dash overuse).
- Concrete recommendations to make it read less AI-written — specific, actionable, tied to the passages you flagged.

IMPORTANT — hard rules:

- Do NOT change, question, or second-guess any facts, figures, odds, names, dates, or claims in the article. Your job is style detection only, not fact-checking.
- Do NOT rewrite the article yourself. Recommendations only — never output a rewritten version.
- Do NOT remove or suggest removing any responsible-gambling language, disclosures, 18+ markers, or [VERIFY]/[DATA NEEDED] flags — if any survive to this stage, note it as a process issue but do not touch it yourself.

## Accept / iterate policy (used by daily-run.md Step 7)
- **PASS** if the verdict is "human-written" with confidence **≥ 80%** (target = 80; 80 is acceptable).
- Otherwise (shows AI patterns, or human-written < 80%): apply the flagged recommendations
  via a FRESH Humaniser pass (`step-7b-apply-gemini-recs.md`), preserving every untouchable,
  then re-run this check. Repeat up to `MAX_GEMINI_PASSES` (default 2).
- If still below 80 after the cap: keep the best-scoring version and log the verdict for the
  human — do not loop indefinitely (detector scores are noisy; over-editing strips voice).
