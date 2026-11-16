import re,sys,json,subprocess,os
D=os.path.dirname(os.path.abspath(__file__))
src=open(sys.argv[1]).read()
md=re.search(r"````markdown\n(.*?)\n````",src,re.S).group(1)
ts=re.search(r"````ts\n(.*?)\n````",src,re.S).group(1)
js=json.loads(re.search(r"````json\n(.*?)\n````",src,re.S).group(1))
open(D+"/docs/forma-bezplatna-konsultacia.md","w").write(md+"\n")
out=subprocess.run(["node",D+"/site/scripts/sync.mjs"],env={**os.environ,"FORM_ROOT":D},capture_output=True,text=True)
print(out.stderr.strip() or out.stdout.splitlines()[0])
ids=[l.strip() for l in out.stdout.splitlines()[2:]]
before=[l.strip() for l in open(D+"/ids-before.txt").read().splitlines()[2:]]
print("ids identical to source:", ids==before, len(ids))
gen=open(D+"/site/src/content/consultation-form.bg.ts").read()
g=json.loads(gen.split("= ",1)[1].rstrip().rstrip(";"))
b=json.loads(open(D+"/bg-before.ts").read().split("= ",1)[1].rstrip().rstrip(";"))
def shape(f): return [(s["id"],[(x["id"],x["kind"],x.get("max"),x.get("required"),x.get("optional"),len(x.get("options") or [])) for x in s["fields"]]) for s in f["sections"]]
print("field kinds/limits identical:", shape(g)==shape(b))
print("consent parsed:", repr(g.get("consent")))
s7=[o["label"] for o in g["sections"][6]["fields"][0]["options"]]; s7b=[o["label"] for o in b["sections"][6]["fields"][0]["options"]]
print("s7 options identical:", s7==s7b)
keys=re.findall(r'^\s*"?([\w.]+)"?:',ts,re.M); old=re.findall(r'^\s*"?([\w.]+)"?:',open("/Users/georgitodorov/Work/biz-grow/site/src/content/consultation-form.en.ts").read(),re.M)
print("EN keys: missing",set(old)-set(keys),"added",set(keys)-set(old))
print("EN keys not in ids:", set(keys)-set(ids)-{"consent"}, "ids w/o EN:", set(ids)-set(keys)-{"intro"})
print("contact key counts", {k:len(v) for k,v in js.items()}, set(js["bg"])^set(js["en"]))
print("em-dash count", src.count("—"))
