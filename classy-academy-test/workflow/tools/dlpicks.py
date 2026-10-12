import re,json,os,sys,subprocess
# usage (inside the work folder): python3 dlpicks.py  -> downloads every <tag><n> named in picks.md (skips SKIP: lines)
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pin_dl import dl
F=os.getcwd(); P=F+'/pin'; R=F+'/raw'; os.makedirs(R,exist_ok=True)
tags=sorted([f[:-5] for f in os.listdir(P) if f.endswith('.json')],key=len,reverse=True)
txt=open(F+'/picks.md').read()
skip=set()
for line in txt.splitlines():
    if line.startswith('SKIP:'): skip.update(line[5:].split())
toks=[]
for tok in re.findall(r'\b([a-z]+\d*_?\d+)\b',txt):
    for t in tags:
        m=re.fullmatch(re.escape(t)+r'_?(\d+)',tok)
        if m: toks.append((t,int(m.group(1)))); break
seen=set(); meta={}
if os.path.exists(F+'/raw/meta.json'): meta=json.load(open(F+'/raw/meta.json'))
for t,i in toks:
    k=f'{t}{i}'
    if k in seen or k in skip: continue
    seen.add(k); out=f'{R}/{k}.mp4'
    pins=json.load(open(f'{P}/{t}.json'))
    if i>=len(pins) or not pins[i]['videos']: print('novideo',k); continue
    p=pins[i]; meta[k]=dict(url=p['url'],creator=p['creator'],user=p['creator_user'],src=p['src_link'],title=p['title'])
    if os.path.exists(out) and os.path.getsize(out)>10000: continue
    try: dl(p['videos'][0],out); print('ok',k,flush=True)
    except Exception as e: print('fail',k,e,flush=True)
    json.dump(meta,open(F+'/raw/meta.json','w'),indent=0)
json.dump(meta,open(F+'/raw/meta.json','w'),indent=0); print('DLDONE')
