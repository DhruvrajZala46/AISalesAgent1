import json, os, sys, time, urllib.request, concurrent.futures as cf
G=os.path.dirname(os.path.abspath(__file__)); KEY=open(os.path.join(G,'.key')).read().strip()
MODELS=os.environ.get('GMODELS','gemini-3.6-flash gemini-3.5-flash gemini-3-flash-preview').split(); OUT=os.path.join(G,'out'); os.makedirs(OUT,exist_ok=True)
PROMPT=open(os.path.join(G,'prompt.txt')).read()
def ask(vid):
    out=os.path.join(OUT,f'{vid}.json')
    if os.path.exists(out) and os.path.getsize(out)>500: return vid,'cached'
    body={"contents":[{"parts":[{"file_data":{"file_uri":f"https://www.youtube.com/watch?v={vid}"}},{"text":PROMPT}]}],
          "generationConfig":{"responseMimeType":"application/json","temperature":0.2}}
    err='none'
    for attempt in range(len(MODELS)*2):
        MODEL=MODELS[attempt % len(MODELS)]
        req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
            data=json.dumps(body).encode(),headers={"x-goog-api-key":KEY,"Content-Type":"application/json"})
        try:
            r=json.loads(urllib.request.urlopen(req,timeout=150).read())
            txt=r['candidates'][0]['content']['parts'][0]['text']; d=json.loads(txt)
            d['_model']=MODEL; d['_usage']=r.get('usageMetadata',{})
            json.dump(d,open(out,'w'),indent=1); return vid,'ok'
        except urllib.error.HTTPError as e:
            msg=e.read().decode()[:300]
            err=f'HTTP {e.code} {msg[:120]}'
            if e.code in (429,500,503): time.sleep(3); continue
            return vid,f'HTTP {e.code} {msg}'
        except Exception as e:
            err=str(e)[:200]; time.sleep(10)
    return vid,'failed '+err
if __name__=='__main__':
    ids=json.load(open(sys.argv[1])) if len(sys.argv)>1 and sys.argv[1].endswith('.json') else (sys.argv[1:] or json.load(open(os.path.join(G,'ids.json'))))
    with cf.ThreadPoolExecutor(int(os.environ.get('PAR','4'))) as ex:
        for vid,st in ex.map(ask,ids): print(vid,st,flush=True)
