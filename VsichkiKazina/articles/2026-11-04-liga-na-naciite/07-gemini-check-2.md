# 07 — Gemini Step-7 check — pass 2 (after humaniser pass 1)

**Verdict: Shows AI patterns, 80% confidence.** → human-likeness = 100 − 80 = **20**.

NOTE (keep-best tracking): this is LOWER than the initial draft (HL 35). The detector is anchored
~65–80% "AI" on dense factual BG content and relocates its flags each pass (it now flags a transition
that pass-1 itself introduced). Same whack-a-mole behaviour the sibling league guides recorded.

Gemini (verbatim, trimmed to the actionable flags):

### Verdict: Shows AI patterns, 80% confidence.

**1. The "More Than Meets the Eye" Cliché**
> "Точно това прави Лигата на нациите по-интересна, отколкото изглежда на пръв поглед: тя превърна старите контроли в нещо, което носи последствия."
Pattern: AI filler telling the reader how to feel. Recommendation: remove the "more interesting than it looks" hype; connect the first sentence directly to the consequence fact.

**2. Cross-Lingual Semantic Artifacts (Unnatural Vocabulary)**
> "Вместо товарни приятелски срещи без залог..." — "товарни" (freight) is a strange adjective for friendlies.
> "Вътре всяка дивизия е нарязана на групи..." — "нарязана" (sliced) is an unnatural metaphor.
Recommendation: replace "товарни" with a natural BG term for meaningless matches; change "нарязана" to the standard verb for dividing teams into groups.

**3. Over-Polished / Poetic Summaries**
> "Така върхът и дъното на всяка дивизия се разместват всяко издание, без турнирът да замръзва в едни и същи имена."
Pattern: neat summarising sentence + overly poetic "freezing in the same names". Recommendation: flatten to "the format ensures constant rotation".

**4. The "Not Just X" Transition**
> "Турнирът не свършва с вдигането на трофея. Лигата на нациите отваря допълнителен път..."
Pattern: dramatic pivot. Recommendation: delete the opening sentence; start directly with how the Nations League opens the extra path.

Gemini note: RG disclosures / 18+ / footer bypassed in critique, do not alter.

→ Action: humaniser pass 2 (the MAX_GEMINI_PASSES cap) applying the genuinely natural fixes (esp.
товарни→безцелни, нарязана→разделена, flatten poetic summary, cut dramatic pivot). Re-run check 3.
Then KEEP-BEST across initial(35)/pass1(20)/pass2(?).
