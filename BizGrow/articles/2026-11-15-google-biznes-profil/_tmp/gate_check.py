import re,sys
f=sys.argv[1]
t=open(f,encoding='utf-8').read()
page=t[t.index('## OPTIMISED PAGE'):]
def field(n):
    m=re.search(r'^- '+n+r': (.*)$',page,re.M); return m.group(1).strip()
for n in ['title','meta_description','summary']:
    v=field(n); print(n,len(v),v)
body=page[page.index('## Какво е'):page.index('## FAQ')]
faq=page[page.index('## FAQ'):page.index('- related')]
clean=re.sub(r'\[(VERIFY|OWNER CONFIRM)[^\]]*\]','',body)
clean=re.sub(r'\{#[^}]*\}','',clean)
clean=re.sub(r'\]\([^)]*\)',']',clean)
words=re.findall(r'[\wА-Яа-я„“{}-]+',clean)
words=[w for w in clean.split() if re.search(r'\w',w)]
print('body words',len(words))
print('H2',len(re.findall(r'^## (?!FAQ)',body,re.M)), [h for h in re.findall(r'^## (.*)$',body,re.M)])
print('FAQ',len(re.findall(r'^q:',faq,re.M)))
full=page[:page.index('## FLAGS')]
vis=re.sub(r'\[(VERIFY|OWNER CONFIRM)[^\]]*\]','',full)
print('BOOKING',full.count('{{BOOKING_URL}}'),'emdash',full.count('—'),'endash',full.count('–'),'excl',vis.count('!'))
for p in ['безплатн','доклад','отзив','гаранц','гарантир','ти ','твой','теб','№1','лидер','най-добр','уникал','промоци','лв','€','евро','седмиц','часа','дни','за дни']:
    c=len(re.findall(p,vis,re.I));
    if c: print(p,c,[vis[max(0,m.start()-40):m.end()+30].replace('\n',' ') for m in re.finditer(p,vis,re.I)])
print('digits',re.findall(r'\d+[^\s]*',re.sub(r'\{#[^}]*\}|^\d+\.','',vis,flags=re.M)))
print('links',re.findall(r'\]\(([^)]*)\)',full))
print('main term',len(re.findall('бизнес профил в гугъл',vis,re.I)))
