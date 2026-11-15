import re,sys
W=sys.argv[1]
t=open(W+'/03-humanised.md',encoding='utf-8').read()
page=t.split('## PHASE 2: EDITED PAGE',1)[1].split('## CHANGE LOG',1)[0].strip()
page=page.split('\n',2)[2].strip()  # drop "Page:" line
reps=[('## Как се формира цената {#cena}','## Как се формира цената на онлайн магазина {#cena}'),
('q = "На коя платформа изработвате магазина?"','q = "Коя платформа за онлайн магазин използвате?"')]
for a,b in reps:
    assert page.count(a)==1,a; page=page.replace(a,b)
page=page.rstrip('-\n ').strip()
open(W+'/_tmp/page4.md','w',encoding='utf-8').write(page)
title="Изработка на онлайн магазин с автоматизации | BizGrow"
meta="Изработка на онлайн магазин за малкия бизнес, с AI отговори за пратки, SEO описания на продукти и напомняния за колички. Започнете с безплатна диагностика."
print(len(title),len(meta))
body=page.split('## PROPOSED FAQ')[0]
vis=re.sub(r'\[OWNER CONFIRM:[^\]]*\]','',body)
vis=re.sub(r'<!--.*?-->','',vis)
words=re.sub(r'[#{}\[\]()*]',' ',vis.split('\n',1)[1]).split()
print('first100 has term:', 'изработка на онлайн магазин' in ' '.join(words[:100]).lower())
print('H2:',len(re.findall(r'^## ',body,re.M)),'FAQ:',page.count('[[faq]]'))
low=page.lower()
for k in ['изработка на онлайн магазин','изработката на онлайн магазин','създаване на онлайн магазин','създаването на онлайн магазин','изработване на онлайн магазин','изработването на онлайн магазин','платформа за онлайн магазин','цената на онлайн магазина','изработка на сайт','seo оптимизация','seo за онлайн магазин','ai асистент','seo копирайтинг','автоматизация на бизнес процеси']:
    print(k, low.count(k))
for pat in ['—','доклад','гарантир','гаранци','първо място','топ позиц','най-добр','уникал','невероят','лв','евро','€','отстъпк','промоци','отзив','безплатн','седмиц','часа','дни',' ти ','твой','24/7']:
    if pat.lower() in low: print('HIT',pat,[m.start() for m in re.finditer(re.escape(pat.lower()),low)][:5])
print(re.findall(r'\d+',re.sub(r'\{\{[A-Z_]+\}\}','',vis)))
print(re.findall(r'\]\((/[^)]*)\)',body), re.findall(r'\]\((/[^)]*)\)',page.split('## PROPOSED FAQ')[1]))
print('words body', len(words))
for w in re.findall(r'\b(вие|ви|вас|ваш\w*)\b',vis): print('lower',w)
