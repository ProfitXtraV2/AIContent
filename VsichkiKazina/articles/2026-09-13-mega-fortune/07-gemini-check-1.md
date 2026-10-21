# 07 — Gemini external check, pass 1 (initial draft) — Mega Fortune

Model: gemini-3.1-pro-preview · script: scripts/gemini_check.py

**Verdict: Highly likely human-written, 95% confidence.** → human-likeness = **95**. → **PASS** (≥ GEMINI_TARGET_CONFIDENCE 80) on the first check.

## Gemini verbatim verdict

**Verdict: Highly likely human-written, 95% confidence.**

This article is an excellent example of high-quality, human-led copywriting. It successfully avoids almost all common LLM pitfalls. The text features native Bulgarian syntactic structures that AI rarely generates naturally (e.g., the conditional phrasing *"Паднеш ли на стрелка, продължаваш навътре"* and colloquialisms like *"поддържат банката жива"*).

Furthermore, the tone is distinctly human: it is grounded, slightly cynical, and highly practical. AI models are typically aligned to be overly enthusiastic or neutrally encyclopedic; they rarely produce punchy, realistic warnings like *"Останалото е математиката"* or *"Числото на екрана е истинско. Просто почти сигурно не е за теб."* The breakdown of the RTP math is also exceptionally clear and practical, avoiding the abstract fluff AI usually relies on when explaining slot mechanics.

However, there are a few minor structural and phrasing patterns that feel slightly formulaic or "SEO-robotic." If you want to polish it to 100% human perfection, here is what you should look at.

### Flagged Passages, Patterns, and Recommendations

1. **Forced SEO signposting / clunky anchor integration** — the two internal-link references („която сме разгледали отделно в…", „профилът на доставчиците… стъпва на същата логика") read as meta-references. Recommendation: weave links into the active concept without announcing a separate article.
2. **The „deceptive surface" hook** — „Числото звучи нормално за ротативка, но крие уловка…". Recommendation: drop the intrigue word „уловка" and let the 96.6% vs 89% contrast create the impact directly.
3. **Formulaic feature-to-outcome phrasing** — „скромен множител прави скромен рунд". Recommendation: break the symmetry with a blunter phrasing.

### Process note
Gemini noted the in-text 18+ RG line overlaps with the footer boilerplate. This is a DELIBERATE brand requirement (one natural RG touch beyond the footer, verbatim 18+ line) — NOT a defect. Left as-is per hard rules.

## Decision
Human-likeness 95 ≥ 80 → **PASS**, keep the initial draft. No Humaniser pass run: HL 95 is already very high and applying recommendations risks lowering it; keep-best keeps the highest score seen (95). content-queue gemini = `human 95`. All untouchables intact (96.6/89/7.6/62.8/16.8/9.3/3.4/€1000/€890/€76/€34/€966/1700x/5x3/25/€4 милиона/€17 861 813/€17,8 милиона/20.01.2013/€0.25/2009, 18+ line, RG signposting, affiliate footer, byline, brand, dates). The three optional nits are style-only and do not threaten the gate or the score.
