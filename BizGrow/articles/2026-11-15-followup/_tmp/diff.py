import json,sys
a=json.load(open(sys.argv[1]));b=json.load(open(sys.argv[2]))
def walk(x,y,p):
  if isinstance(x,dict) or isinstance(y,dict):
    for k in list(dict.fromkeys(list((x or {}).keys())+list((y or {}).keys()))):
      walk((x or {}).get(k),(y or {}).get(k),p+"."+k if p else k)
  elif isinstance(x,list) and isinstance(y,list) and all(isinstance(i,dict) and 'id' in i for i in x+y):
    dx={i['id']:i for i in x}; dy={i['id']:i for i in y}
    for k in dict.fromkeys(list(dx)+list(dy)): walk(dx.get(k),dy.get(k),f"{p}[{k}]")
  elif isinstance(x,list) and isinstance(y,list) and len(x)==len(y) and all(isinstance(i,(dict,str)) for i in x):
    for i,(u,v) in enumerate(zip(x,y)): walk(u,v,f"{p}[{i}]")
  elif x!=y:
    print(f"- `{p}`\n  - before: {json.dumps(x,ensure_ascii=False)}\n  - after: {json.dumps(y,ensure_ascii=False)}")
walk(a,b,"")
