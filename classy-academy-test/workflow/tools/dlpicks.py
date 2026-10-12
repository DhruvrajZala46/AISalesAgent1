import re,json,os,sys,subprocess
# usage (inside the work folder): python3 dlpicks.py  -> downloads every <tag><n> named in picks.md
# lines starting with SKIP / DUP / CHECK / TODO / # are notes and are never downloaded.
# a tag that ends in a digit gets an underscore: over60 + 6 -> over60_6 (never the ambiguous over606).
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pin_dl import dl
F=os.getcwd(); P=F+'/pin'; R=F+'/raw'; os.makedirs(R,exist_ok=True)
tags=sorted([f[:-5] for f in os.listdir(P) if f.endswith('.json')],key=len,reverse=True)
txt=open(F+'/picks.md').read()
skip=set(); body=[]
for line in txt.splitlines():
    if line.startswith('SKIP'): skip.update(re.findall(r'\b([a-z]+\d*_?\d+)\b', line))
    if not re.match(r'(SKIP|DUP|CHECK|TODO|#)', line): body.append(line)
key=lambda t, i: f'{t}_{i}' if t[-1].isdigit() else f'{t}{i}'
toks=[]
for tok in re.findall(r'\b([a-z]+\d*_?\d+)\b','\n'.join(body)):
    for t in tags:
        m=re.fullmatch(re.escape(t)+r'_?(\d+)',tok)
        if m: toks.append((t,int(m.group(1)))); break
seen=set(); meta={}; jobs=[]
if os.path.exists(F+'/raw/meta.json'): meta=json.load(open(F+'/raw/meta.json'))
for t,i in toks:
    k=key(t, i)
    if k in seen or k in skip: continue
    seen.add(k); out=f'{R}/{k}.mp4'
    pins=json.load(open(f'{P}/{t}.json'))
    if i>=len(pins) or not pins[i]['videos']: print('novideo',k); continue
    p=pins[i]; meta[k]=dict(url=p['url'],creator=p['creator'],user=p['creator_user'],src=p['src_link'],title=p['title'])
    if os.path.exists(out) and os.path.getsize(out)>10000: continue
    jobs.append((k,p['videos'][0],out))
json.dump(meta,open(F+'/raw/meta.json','w'),indent=0)
def one(j):
    k,u,out=j
    try: dl(u,out); return f'ok {k}'
    except Exception as e: return f'fail {k} {e}'
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(6) as ex:
    for r in ex.map(one,jobs): print(r,flush=True)
# the same pin found by two searches is downloaded once per name: report it so only one name is used
byurl={}
for k in sorted(meta):
    u=meta[k]['url']
    if u in byurl and os.path.exists(f'{R}/{k}.mp4'): print('DUP',k,'==',byurl[u])
    byurl.setdefault(u,k)
print('DLDONE')
