import re,sys
t=open(sys.argv[1],encoding='utf-8').read()
page=t[t.index('## PAGE FIELDS'):t.index('## CHANGE SUMMARY')]
open(sys.argv[2],'w',encoding='utf-8').write(page)
f=dict(re.findall(r'^- (meta\.title|meta\.description|summary|label|eyebrow|h1|lead): (.*)$',page,re.M))
for k in ['meta.title','meta.description','summary']: print(k,len(f[k]))
body=page[page.index('\n## Какво'):page.index('## FAQ')]
faq=page[page.index('## FAQ'):]
h2=re.findall(r'^## (.*)$',body,re.M); print('H2',len(h2)); [print(' ',h) for h in h2]
clean=re.sub(r'\[(VERIFY|OWNER CONFIRM)[^\]]*\]','',body)
clean=re.sub(r'^## .*$','',clean,flags=re.M)
clean=re.sub(r'\]\([^)]*\)',']',clean)
print('words',len(re.findall(r'\w+',clean)))
print('FAQ',len(re.findall(r'^\*\*В:',faq,re.M)))
print('BOOKING',page.count('{{BOOKING_URL}}'))
allt=page
for pat in ['—','–','доклад','48','седмиц','за дни','часа','гарант','най-добр','лидер','безплатн','промоц','отстъп','отзив','!','ти ','твой','теб ','Ahrefs','Semrush','Ranktracker','Planner','seo копирайтинг','seo оптимизация','копирайтър','изработка на сайт','реклама в гугъл','бизнес профил']:
    for m in re.finditer(re.escape(pat),allt,re.I):
        s=allt[max(0,m.start()-40):m.end()+40].replace('\n',' ')
        print(f'[{pat}]',s)
print('DIGITS:')
for m in re.finditer(r'\d+',re.sub(r'https?://\S+','',allt)):
    print(' ',allt[max(0,m.start()-30):m.end()+20].replace('\n',' '))
print('lower вие forms:')
for m in re.finditer(r'(?<![А-Яа-я])(вие|ви|вас|ваш\w*)(?![А-Яа-я])',allt):
    print(' ',allt[max(0,m.start()-30):m.end()+20].replace('\n',' '))
for m in re.finditer(r'ключов\w* дум\w*',allt,re.I):
    print('MT',allt[max(0,m.start()-25):m.end()+5].replace('\n',' '))
