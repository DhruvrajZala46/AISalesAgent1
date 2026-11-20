"""Generate images with Meta Muse Image (OpenAI-compatible images endpoint).
usage: MODEL_API_KEY=... python3 -I tools/meta_image.py jobs.json
jobs.json = [["out_name", "prompt", "1024x1792"], ...]   -> out_name.webp (size comes back as 1152x2016 for 9:16, 1600x1600 for square)
The key is read from the MODEL_API_KEY environment variable only; never write it into the repo."""
import json,urllib.request,base64,time,sys,os,concurrent.futures as cf
key=os.environ['MODEL_API_KEY']
def gen(name,prompt,size="1024x1792"):
    body={"model":"muse-image-1.0","prompt":prompt,"n":1,"size":size,"response_format":"b64_json"}
    t=time.time(); req=urllib.request.Request('https://api.meta.ai/v1/images/generations',data=json.dumps(body).encode(),
        headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
    try: r=json.load(urllib.request.urlopen(req,timeout=300))
    except urllib.error.HTTPError as e: return name,'HTTP %d %s'%(e.code,e.read().decode()[:300])
    open(name+'.webp','wb').write(base64.b64decode(r['data'][0]['b64_json']))
    return name,'%.0fs %s tokens %s'%(time.time()-t,r.get('size'),r.get('usage',{}).get('total_tokens'))
with cf.ThreadPoolExecutor(4) as ex:
    for n,res in ex.map(lambda j:gen(*j),json.load(open(sys.argv[1]))): print(n,res)
