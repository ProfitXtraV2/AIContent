# Gemini endpoint — validated for Step-7 external AI-pattern check

Validated: 2026-09-07 (one-time Step-7 validation run). `GEMINI_API_KEY` works.

## Working configuration

| Field | Value |
|-------|-------|
| Base URL | `https://generativelanguage.googleapis.com/v1beta` |
| Endpoint | `POST /models/{model}:generateContent` |
| **Working model** | **`gemini-3.1-pro-preview`** (strongest current pro-tier TEXT model with `generateContent`) |
| Auth header | `x-goog-api-key: $GEMINI_API_KEY` |
| Content type | `Content-Type: application/json` |
| Service tier | `standard` |

Full URL used:
`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent`

### Why not `gemini-2.5-pro`
The previous default `gemini-2.5-pro` now returns **HTTP 404 NOT_FOUND** for this key:

> "This model models/gemini-2.5-pro is no longer available to new users. Please update
> your code to use models/gemini-3.1-pro-preview for the latest features and improvements."

Google's own error names `gemini-3.1-pro-preview` as the replacement, so that is what
`DEFAULT_MODEL` in `scripts/gemini_check.py` now points to. (`gemini-pro-latest` is a
floating alias to the newest pro model and also works, but the validation pins the
explicit preview id for reproducibility.)

## Request JSON shape

```json
{
  "contents": [
    { "parts": [ { "text": "<Step-7 prompt>\n\n---ARTICLE---\n\n<article text>" } ] }
  ],
  "generationConfig": { "temperature": 0.2 }
}
```

## Response shape

Verdict text at `candidates[0].content.parts[0].text`. This is a thinking model, so
responses also carry `usageMetadata.thoughtsTokenCount` (internal reasoning tokens, billed
but not returned as text). Example for a 1-word probe: `promptTokenCount: 7`,
`candidatesTokenCount: 1`, `thoughtsTokenCount: 105`, `totalTokenCount: 113`,
`modelVersion: gemini-3.1-pro-preview`.

## Rate / units info

No `X-RateLimit-*` / quota headers are exposed on responses (checked verbatim; none
present). Usage is reported per-call in `usageMetadata` (token counts above). Quota is
governed server-side by the Google AI Studio / Gemini API project limits for the key;
on limit you would see HTTP 429 with a `RESOURCE_EXHAUSTED` status (not observed in this
run).

## Sample verdict returned (verbatim, test article)

Test article: `05b-final-draft.md` from PR branch
`content/2026-09-07-kak-raboti-razigravaneto` (the wagering guide).

> **Shows AI patterns, 75% confidence.**
> While the text has clearly been scrubbed of basic AI tropes (like bulleted lists,
> em-dashes, and "В заключение" signposts), the underlying *rhythm and rhetorical
> structure* still heavily betray an AI origin. The text relies on perfectly symmetrical
> contrasts, didactic imperatives, dramatic transitions, and slightly unnatural translated
> idioms that human Bulgarian writers rarely use. It reads like a highly polished AI draft
> that has been manually de-formatted but not structurally rewritten.

(Full run also returned flagged passages — symmetrical contrasts, translated idioms such
as „идва с часовник“ / „окото хваща банера“, dramatic transitions, didactic imperatives,
and a run-on hypothetical-player sentence — plus concrete per-passage recommendations. RG
language, 18+ markers, and disclosures were correctly left untouched.)

## Step-7 accept-threshold result for this sample

- **Confidence: 75% "Shows AI patterns"** → human-written confidence is **below the 80%
  PASS threshold**.
- **Result: WOULD NOT PASS → triggers a Humaniser pass** (`step-7b-apply-gemini-recs.md`),
  then re-check, per `daily-run.md` Step-7 accept/iterate policy (up to `MAX_GEMINI_PASSES`).
