import json,re,tomllib,sys
md=open('content/klyuchovi-dumi.md').read(); p=json.load(open('content/klyuchovi-dumi.port.json'))
src=open('05b-final-draft.md').read()
src_clean=re.sub(r'\s*\[(VERIFY|OWNER CONFIRM)[^\]]*\]','',src)
fm=md.split('+++')[1]; t=tomllib.loads(fm); print('TOML ok; owner_items',len(t['owner_items']),'sources',len(t['sources']))
strs=[p['meta']['title'],p['meta']['description'],p['label'],p['summary'],p['h1'],p['lead']]
for s in p['sections']:
    strs.append(s['title']); [strs.extend(s.get(k,[])) for k in ('paragraphs','steps','bullets','closing')]
for f in p['faq']: strs+= [f['question'],f['answer']]
miss=[s for s in strs if s not in src_clean]; print('strings not verbatim in 05b:',miss)
miss2=[s for s in strs if s not in md]; print('strings not in content md:',miss2)
allt='\n'.join(strs)
print('title len',len(p['meta']['title']),'meta len',len(p['meta']['description']),'summary',len(p['summary']))
print('emdash',allt.count('—')+md.count('—'),'endash',allt.count('–'))
print('ти forms',re.findall(r'(?<![А-Яа-я])(ти|теб|твой|твоя|твоят|твоите|твоето)(?![А-Яа-я])',allt))
print('lower ви/вас/ваш',re.findall(r'(?<![А-Яа-я])(ви|вас|ваш[а-я]*)(?![А-Яа-я])',allt))
print('доклад',allt.count('доклад'),'periods',re.findall(r'до \d+ (часа|седмици|дни)|за дни',allt))
print('markers',re.findall(r'\[(VERIFY|OWNER|LINK|DATA)',md))
print('links',re.findall(r'\]\(([^)]+)\)',allt),'booking count',allt.count('{{BOOKING_URL}}'))
body=[]
for s in p['sections']:
    for k in ('paragraphs','steps','bullets','closing'): body+=s.get(k,[])
w=len(re.findall(r'\S+',' '.join(body))); print('body words (sections, excl lead/H2/FAQ)',w, ' +lead',w+len(p['lead'].split()))
first100=' '.join((p['lead']).split()[:100]).lower()
print('kw in title/h1/first100:', 'ключови думи' in p['meta']['title'].lower(), 'ключови думи' in p['h1'].lower(), 'ключови думи' in first100)
print('H2 with kw:',[s['id'] for s in p['sections'] if 'ключови думи' in s['title'].lower()])
print('H2 count',len(p['sections']),'faq',len(p['faq']),'service' in p, p['related'])
ids=[x['id'] for x in t['sections']]; bids=re.findall(r'\{#([a-z\-]+)\}',md.split('+++')[2]); print('ids match',ids==bids)
for bad in ['seo копирайтинг','seo оптимизация']: print(bad, bad in allt.lower())
