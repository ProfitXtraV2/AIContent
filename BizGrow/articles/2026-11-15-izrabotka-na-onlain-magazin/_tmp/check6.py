import tomllib, json, re, sys
md=open('content/izrabotka-na-onlain-magazin.md').read()
fm=md.split('+++')[1]; body=md.split('+++',2)[2]
d=tomllib.loads(fm); print('TOML ok; sections',len(d['sections']),'faq',len(d['faq']),'owner',len(d['owner_items']))
port=json.load(open('content/izrabotka-na-onlain-magazin.port.json'))
print('title',len(d['title']),'meta',len(d['meta_description']), 'port title',len(port['meta']['title']))
alltxt=md+json.dumps(port,ensure_ascii=False)
for pat in ['—','–','[OWNER','[VERIFY','[DATA','[LINK','доклад','48 часа','седмиц','за дни']:
    print(repr(pat), alltxt.count(pat))
vis=body+' '.join(f['q']+' '+f['a'] for f in d['faq'])+d['title']+d['meta_description']+port['summary']+port['eyebrow']
ti=re.findall(r'(?i)\b(ти|теб|тебе|твой|твоя|твоят|твоите|твоето|губиш|попълваш|получаваш|открий|запази)\b',vis); print('ти forms',ti)
low=re.findall(r'(?<![А-Яа-я])(вие|ви|вас|ваш[а-я]*)(?![А-Яа-я])',vis); print('lowercase formal',low)
ban=r'(?i)(гарантир|гаранци|първо място|топ позиции|№1|#1|лидер|най-добр|революцион|магия|магическ|невероят|уникал|безпрецедент|следващо ниво|без никакви усилия|напълно автоматично|мощен ai|10x|удвои|100%|сертифиц|само днес|ограничени места|побързайте|промоци|отстъпк|ваучер|отзив|доволни клиенти)'
print('banned',re.findall(ban,vis))
print('free words',re.findall(r'(?i)безплатн\w*\s+\w+',vis))
print('price',re.findall(r'\d+\s*(лв|лева|евро|€|EUR|BGN|\$)',vis))
print('numbers',re.findall(r'\d+',re.sub(r'\{\{[A-Z_]+\}\}','',body+' '.join(f['a'] for f in d['faq']))))
ids=[s['id'] for s in d['sections']]; bids=re.findall(r'^## (.+) \{#([a-z-]+)\}$',body,re.M)
print('ids match', ids==[b[1] for b in bids], all(s['heading']==b[0] for s,b in zip(d['sections'],bids)))
print('links',sorted(set(re.findall(r'\]\(([^)]+)\)',md))))
pk=d['primary_keyword']; 
print('pk title',d['title'].lower().count(pk),'h1',d['h1'].lower().count(pk),'first100',' '.join(port['lead'].split()[:100]).lower().count(pk),'H2s',[b[0] for b in bids[1:] if pk in b[0].lower()], 'meta', pk in d['meta_description'].lower())
print('pk total body', body.lower().count(pk))
# md vs port string equality
for s in port['sections']:
    for k in ('paragraphs','bullets','steps','closing'):
        for x in s.get(k,[]): assert x in md, x
for f in port['faq']: assert f['question'] in md and f['answer'] in md
assert port['lead'] in md and port['h1']==d['h1'] and port['meta']['description']==d['meta_description']
print('port strings in md: ok; related',port['related'])
words=re.sub(r'\{\{[A-Z_]+\}\}|\[|\]\([^)]*\)|[#*{}]',' ',body)
print('body words',len(re.findall(r'[\wА-Яа-я„“-]+',words)), 'with faq', len(re.findall(r'[\wА-Яа-я„“-]+',words+' '.join(f['q']+' '+f['a'] for f in d['faq']))))
