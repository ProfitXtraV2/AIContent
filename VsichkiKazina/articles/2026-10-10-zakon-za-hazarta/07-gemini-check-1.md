# Step 7 — Gemini cross-model check — PASS 1 (initial 05b)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-10 (cloud reconcile of HANDOFF row)

## Verdict (verbatim)

→ Normalized HUMAN-LIKENESS = **85**  (PASS threshold = 80) — PASS

---

**Verdict: Likely human-written, 85% confidence.**

This is a highly specific, well-researched piece of content. The phrasing contains excellent, natural Bulgarian idioms and journalistic flair that AI almost never generates organically (e.g., *"Законът гледа и от другата страна на екрана"*, *"друга защитима позиция при тази конструкция няма"*, *"банерът е реклама, общите условия са договорът"*). AI writing in Bulgarian typically relies on clunky English calques, which are entirely absent here. 

However, the text does exhibit a few structural "SEO/AI-isms"—patterns that writers often adopt when using AI to outline, summarize, or insert internal links. 

Here is the breakdown of the specific patterns that triggered my radar, along with actionable recommendations.

### 1. The "Data Dump" / Front-Loaded Summary Intro
**The Pattern:** AI models are frequently prompted to "include all keywords and summarize the updates in the introduction." This results in a breathless, dense opening paragraph that tries to tell the whole story before the article has even started.
**The Passage:** 
> *"Законът за хазарта (ЗХ) урежда кой може да организира хазартни игри в България и при какви условия, но има текстове и за самия играч. Надзорът е при НАП. До игра се допускат само пълнолетни, а участието при организатор без лиценз е забранено и за играча (чл. 9, ал. 14), не само за сайта. От 01.01.2026 залозите и печалбите се провеждат в евро. Последните промени влязоха в сила от 01.08.2026: лиценз за афилиейт сайтове и блокиране на нелицензирани страници по решение на НАП в рамките на 24 часа. В процедура е и проект за пълна забрана на хазартната реклама, засега без силата на закон."*
**Recommendation:** Give the reader room to breathe. Instead of listing every single date and change in the first paragraph, focus the intro on the *premise* (the law is changing, and it affects players directly, not just casinos). Let the timeline section do the heavy lifting for the specific dates and euro transitions. 

### 2. Formulaic SEO Signposting (The "We wrote about this here" bridge)
**The Pattern:** When AI is asked to insert internal links, it often creates a dedicated, slightly robotic sentence at the end of a paragraph specifically to house the link, rather than weaving it naturally into the narrative.
**The Passages:**
> *"Как да се уверите, че конкретен сайт наистина има такъв лиценз, описахме в [ръководството за проверка на лиценз]."*
> *"Как се подава искането и какви други инструменти имате, обяснихме в раздела за [отговорна игра]."*
> *"Какво стана с депозитите и бонусите след смяната, разгледахме в [статията за еврото в хазарта]."*
**Recommendation:** Integrate these links organically into the active sentences preceding them. For example, instead of adding a new sentence to link the license guide, hyperlink a relevant phrase in the previous sentence (e.g., link "данните за всеки залог в лицензиран сайт" or "проверката на самоличността"). This removes the mechanical "If you want X, click Y" rhythm.

### 3. The "What's Next" Wrap-Up Heading
**The Pattern:** AI struggles to end articles naturally. It almost always relies on a concluding header like "Conclusion," "Final Thoughts," or "What's Next for [Subject]." 
**The Passage:** 
> *"## Какво следва за играча"*
**Recommendation:** Change this heading to something more specific to the actual advice being given in that paragraph. Since the paragraph is about the risks of playing on unlicensed sites and setting budgets, a heading like *"Рисковете при игра без лиценз"* or *"Защита на играча и лични лимити"* would feel much more like human editorial choice than a generic AI wrap-up prompt.

### 4. Process Issue Note: Surviving Editorial Flags
**The Pattern:** Leftover prompt brackets or editorial markers.
**The Passages:** 
> *"[VERIFY: начин на прилагане на евро-равностойността...]"*
> *"[VERIFY: предишният минимален срок от 30 дни...]"*
> *"[VERIFY: § 79 от проекта...]"*
> *"[VERIFY: препоръката на НАП за 5%...]"*
**Recommendation:** As per my instructions, I am not touching or suggesting the removal of these flags. However, from a senior copywriter's perspective, I must note this as a critical workflow/process issue. These internal fact-checking markers have survived into the "finished" text and need to be resolved by your editorial/legal team before publication.
