import json, os, re
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B, E = "{{BOOKING_URL}}", "{{EMAIL}}"

meta = {
 "title": "AI automation for small business | BizGrow",
 "description": "AI automation for small business: a free diagnosis, a report with prioritised fixes and clear prices within 48 hours, and a build usually within 2 weeks.",
 "ogTitle": "BizGrow: AI automation for small businesses",
 "ogDescription": "A free diagnosis with no obligation. A report with clear one-time prices within 48 hours, and the fixes built usually within 2 weeks.",
 "ogLocale": "en_US",
}
a11y = {"skipToContent":"Skip to content","primaryNav":"Primary","home":"BizGrow home","openMenu":"Open menu","closeMenu":"Close menu","newTab":"(opens in a new tab)","language":"Language","results":"Free diagnosis","step":"Step","breadcrumb":"Breadcrumb"}
page = {"home":"Home","faq":"Frequently asked questions","related":"Related services","diagnosis":"Free diagnosis"}
nav = {"links":[{"label":"Services","href":"#services"},{"label":"Process","href":"#process"},{"label":"Contact us","href":"#contact"}],"cta":"Book a call"}
hero = {
 "line1":"AI automation for small businesses.",
 "line2":"Less busywork, more business.",
 "body":"BizGrow provides AI automation for small business: we find where your business loses time, choose the fixes worth building and build them for you. We start with a free diagnosis and a 30-minute call, and the build usually takes up to 2 weeks.",
 "primary":"Free diagnosis","secondary":"Explore services","imageSrc":"/bizgrow-banner.webp",
 "imageAlt":"BizGrow: AI and automation for small businesses. The banner reads: integrate AI, automate workflows, save time and costs, grow your business.",
 "overlayLabel":"Free diagnosis","overlayUnit":"usually within 2 weeks",
}
metrics = [{"value":"30 min","caption":"diagnosis call","label":"30 minutes"},{"value":"48 h","caption":"to the report with prices","label":"48 hours"},{"value":"0","caption":"obligation"}]
losses = {"title":"Where you lose customers and hours every day","items":[
 "Missed calls and messages after working hours",
 "Hours lost writing quotes and invoices by hand",
 "Messages on Messenger, Instagram or WhatsApp that go without a timely reply",
 "No time for content and social media while competitors grow",
 "Not knowing which numbers in your business actually matter"]}
services = {"title":"AI automation for small business, content and advertising in one place","items":[
 {"icon":"brain","title":"AI assistant and chatbot","body":"A chatbot is a chat assistant that answers repeated questions on Messenger, Instagram and WhatsApp. When it cannot help, it collects the customer's contact details."},
 {"icon":"loop","title":"Automations","body":"We build online booking with reminders, quotes that go from a filled-in form to a finished PDF, and automatic handling of documents and invoices. We also connect the programs you already use and set up a dashboard, one screen with your key figures."},
 {"icon":"spark","title":"SEO articles and copy","body":"Our own content tool writes articles about your industry and city, prepared for Google searches (SEO, search engine optimisation). Each article is published only after you approve it."},
 {"icon":"spark","title":"Social media and creatives","body":"Posts with text and an image go out on a schedule once you approve them. Every month we also prepare branded visuals and advertising materials."},
 {"icon":"loop","title":"Google and Facebook ads","body":"A real marketing specialist plans, runs and tracks your ads and reports the results to you with concrete numbers."},
 {"icon":"brain","title":"SEO optimisation","body":"We work on your website's technical SEO (how the site is set up for search engines), on the optimisation of individual pages and on the links that point to the site."}]}
process = {"title":"Three steps to a working solution","lead":"The work goes through three steps, from the first call to support for the finished solution.","steps":[
 {"n":"1","label":"Diagnosis","title":"Where time and money leak","body":"We start with a free diagnosis and a 30-minute call. You describe the problems you see in your business, and together we find exactly where it loses time and money."},
 {"n":"2","label":"Build","title":"A clear one-time price","body":"Within 48 hours you receive a report with prioritised fixes and clear one-time prices. We then build the specific AI solution, usually within 2 weeks."},
 {"n":"3","label":"Support","title":"A transparent report every month","body":"After launch we monitor the solution and improve it. Every month you receive a short report on the work done."}]}
results = {"title":"What the result can look like","note":"Example scenarios from our method, not figures from specific clients.","rows":[
 {"business":"Restaurant","problem":"Nobody picks up at peak hours.","outcome":"Bookings 24/7, about 10 hours less manual work a week."},
 {"business":"Online shop","problem":"Questions about deliveries sit unanswered for hours.","outcome":"80% of the repeated questions answered in seconds."},
 {"business":"Dental clinic","problem":"Missed calls and appointments moved around.","outcome":"Online booking at any time."}]}
reasons = {"title":"The little “extra” that changes the result","lead":"We explain every solution in plain language and build only AI tools that solve a specific problem in your business.","items":["We work under GDPR","No long-term contracts","Transparent prices","A result before a large investment"]}
cta = {"title":"The first step is free","body":"The diagnosis commits you to nothing. We show you exactly what we can fix and what it will cost.","button":"Book a free diagnosis"}
faq = {"title":"Frequently asked questions","items":[
 {"question":"What can a small business automate?","answer":"The most common candidates are answers to repeated questions on Messenger, Instagram and WhatsApp, online booking with reminders, quotes, documents and invoices. Business automation also covers connecting the programs you already use so that data fills itself in, and a dashboard with your key figures in one place."},
 {"question":"How much does it cost to build a solution?","answer":"Each solution has a one-time price that depends on what exactly is built. You find the price in the report you receive within 48 hours of the diagnosis, and we work without long-term contracts."},
 {"question":"Where do I start if I don't know what to automate?","answer":"Start with the free diagnosis: book a 30-minute call and tell us about the problems you see in your business. The diagnosis commits you to nothing."},
 {"question":"How long does the build take?","answer":"Once you have the report, we build the specific solution, usually within 2 weeks."},
 {"question":"Will AI replace the people on my team?","answer":"AI takes over repeated tasks, and you stay in control: articles and posts go out only after you approve them. Your advertising is run by a real marketing specialist, and when the chat assistant cannot help, it collects the customer's contact details."},
 {"question":"Is this suitable for my industry?","answer":"We work with small businesses: restaurants and cafés, hotels and guest houses, salons, online shops, retail shops and showrooms, clinics and practices, car services and tradespeople, real estate and B2B companies (businesses that sell to other businesses). After the diagnosis, the report shows which fixes make sense for your type of business."},
 {"question":"Do I have to sign a long-term contract?","answer":"No, we work without long-term contracts. During support we monitor the solution, and every month you receive a short report on the work done."}]}
contact = {"title":"Contact us","book":"Book a video call now","emailBefore":"Send us an email at","fields":{"name":"Name","email":"Email","description":"Description"},"submit":"Submit","mailSubject":"BizGrow message from"}
footer = {"descriptor":"We find where your business loses time and fix it with AI.","services":"Services","process":"Process","contact":"Contact us","privacy":"Privacy","rights":"All rights reserved."}

port = {"meta":meta,"a11y":a11y,"page":page,"nav":nav,"hero":hero,"metrics":metrics,"losses":losses,"services":services,
        "process":process,"results":results,"reasons":reasons,"cta":cta,"faq":faq,"contact":contact,"footer":footer}

owner_items = [
 "Title and H1 change. Title „BizGrow: Find where the business loses time“ (currently written with an em-dash) becomes „AI automation for small business | BizGrow“; meta description, ogTitle and ogDescription rewritten around the main term. H1 „Less busywork. / More business.“ becomes hero.line1 „AI automation for small businesses.“ + hero.line2 „Less busywork, more business.“ (slogan kept as line 2), mirroring the Bulgarian page.",
 "„in days, not months“ (current hero.body, hero.overlayUnit, meta.description, ogTitle/ogDescription) is not in the 2026-11-15 canon, so the page uses the canon „usually within 2 weeks“ in hero.body and hero.overlayUnit, as on the Bulgarian page. Confirm, or confirm the old phrase to restore it. Note: the hero overlay then shows „Free diagnosis“ next to „usually within 2 weeks“, which can read as if the diagnosis itself takes 2 weeks (same pairing on the Bulgarian page).",
 "Hero figures „8 short questions“ and „2 min to fill in“ are removed (the questionnaire no longer exists) and replaced by canon figures „30 min / diagnosis call“, „48 h / to the report with prices“, „0 / obligation“. Process step 1 no longer mentions the 2-minute questionnaire and, unlike the Bulgarian page, has no link to the checker (/diagnostika/ is Bulgarian-only). Confirm.",
 "Services: the four current cards (Automations, SEO copywriting, Creatives, Custom solutions) are replaced by six cards mirroring the Bulgarian page, with NO link (there are no English service pages): AI assistant and chatbot, Automations, SEO articles and copy, Social media and creatives, Google and Facebook ads, SEO optimisation. „Custom solutions“ is no longer a card. Confirm the set, titles and card texts, and whether the cards should later link to English service pages or to the Bulgarian ones.",
 "Card „Google and Facebook ads“: the platform names come from the keyword-map H1 of /reklama/ (canon says only advertising and marketing); no monthly cadence is stated for the specialist's report. Confirm the platforms, and say whether the specialist reports monthly (same item as on the Bulgarian page).",
 "Losses: no link under the list on /en/ (the Bulgarian page links the Bulgarian-only /diagnostika/ checker); heading „Every day you lose customers and hours“ becomes „Where you lose customers and hours every day“, mirroring the Bulgarian heading. Confirm.",
 "Example rows in #results kept verbatim with the label „Example scenarios from our method, not figures from specific clients.“: Restaurant („Bookings 24/7, about 10 hours less manual work a week.“), Online shop („80% of the repeated questions answered in seconds.“), Dental clinic („Online booking at any time.“). Heading „What the result looks like“ becomes „What the result can look like“. Confirm the rows and figures, or supply replacements.",
 "Rewritten copy: reasons.lead (old „No jargon, and no solutions “just in case”. Only tools that work, shaped to your business.“) becomes „We explain every solution in plain language and build only AI tools that solve a specific problem in your business.“; process.lead rewritten; footer.descriptor „the business“ → „your business“; contact.fields.name „Names“ → „Name“. CTA wording unchanged. Confirm.",
 "New FAQ section (#faq, 7 questions mirroring the Bulgarian FAQ) between #audit and #contact, answered only from the canon, with no links. FAQ 6 ends with „After the diagnosis, the report shows which fixes make sense for your type of business.“ instead of the Bulgarian „examples in the diagnosis“ (that refers to the Bulgarian-only checker). No GDPR/data question was added because the canon allows only „We work under GDPR“; supply wording if wanted.",
 "hero.imageAlt reworded without the em-dash: „BizGrow: AI and automation for small businesses. The banner reads: integrate AI, automate workflows, save time and costs, grow your business.“ Confirm, together with the plain-word glosses „dashboard, one screen with your key figures“, „technical SEO (how the site is set up for search engines)“ and „B2B companies (businesses that sell to other businesses)“.",
 "The page does not say whether BizGrow works in English or serves businesses outside Bulgaria (not in the canon). Confirm the English service scope if the owner wants it stated.",
]

sections = [
 ("hero", hero["line1"]+" "+hero["line2"], "hero", "hero"),
 ("losses", losses["title"], "list", "losses"),
 ("services", services["title"], "cards", "services"),
 ("process", process["title"], "steps", "process"),
 ("results", results["title"], "table", "results"),
 ("reasons", reasons["title"], "list", "reasons"),
 ("audit", cta["title"], "cta", "cta"),
 ("faq", faq["title"], "faq", ""),
 ("contact", contact["title"], "contact", "contact"),
]
def q(s): return json.dumps(s, ensure_ascii=False)
fm = ["+++",
 f"title = {q(meta['title'])}", f"meta_description = {q(meta['description'])}",
 f"h1 = {q(hero['line1']+' '+hero['line2'])}",
 f"og_title = {q(meta['ogTitle'])}", f"og_description = {q(meta['ogDescription'])}",
 'slug = "en-home"', 'locale = "en"', 'primary_keyword = "ai automation for small business"',
 'secondary_keywords = ["business automation"]',
 'status = "draft"', 'last_updated = "2026-11-15"', ""]
for i,h,k,dk in sections:
    fm += ["[[sections]]", f"id = {q(i)}", f"heading = {q(h)}", f"kind = {q(k)}", f"dictionary_key = {q(dk)}", ""]
for it in faq["items"]:
    fm += ["[[faq]]", f"q = {q(it['question'])}", f"a = {q(it['answer'])}", ""]
for o in owner_items:
    fm += ["[[owner_items]]", f"item = {q(o)}", 'decision = ""', 'decided_by = ""', 'decided_on = ""', ""]
fm[-1] = "+++"
body = []
body += [f"## {sections[0][1]} {{#hero}}", "", hero["body"], "", f"[{hero['primary']}]({B})", "", f"[{hero['secondary']}](#services)", ""]
body += [f"- **{m['value']}** {m['caption']}" for m in metrics] + [""]
body += [f"## {losses['title']} {{#losses}}", ""] + [f"- {x}" for x in losses["items"]] + [""]
body += [f"## {services['title']} {{#services}}", ""] + [f"- **{c['title']}.** {c['body']}" for c in services["items"]] + [""]
body += [f"## {process['title']} {{#process}}", "", process["lead"], ""] + [f"{s['n']}. **{s['label']}: {s['title']}.** {s['body']}" for s in process["steps"]] + [""]
body += [f"## {results['title']} {{#results}}", "", results["note"], "", "| Business | Problem | Result |", "|---|---|---|"] + [f"| {r['business']} | {r['problem']} | {r['outcome']} |" for r in results["rows"]] + [""]
body += [f"## {reasons['title']} {{#reasons}}", "", reasons["lead"], ""] + [f"- {x}" for x in reasons["items"]] + [""]
body += [f"## {cta['title']} {{#audit}}", "", cta["body"], "", f"[{cta['button']}]({B})", ""]
body += [f"## {faq['title']} {{#faq}}", ""]
for it in faq["items"]: body += [f"**{it['question']}**", "", it["answer"], ""]
body += [f"## {contact['title']} {{#contact}}", "", f"[{contact['book']}]({B})", "", f"{contact['emailBefore']} {E}", ""]
body += [f"- {v}" for v in contact["fields"].values()] + ["", f"[{contact['submit']}](mailto:{E})", ""]
open(os.path.join(D,"content","en-home.md"),"w").write("\n".join(fm)+"\n\n"+"\n".join(body))
open(os.path.join(D,"content","en-home.port.json"),"w").write(json.dumps(port, ensure_ascii=False, indent=2)+"\n")
