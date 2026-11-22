import sys as _sys
# DISABLED by the user on 22 Nov 2026: "no more Meta image generation" (keys deleted, no paid billing). Do not re-enable, do not
# work around this guard, and do not switch to another paid image API without the user's explicit OK.
_sys.exit("Meta Muse Image is disabled by the user (22 Nov 2026). Reuse the art library or ask the user first.")
import json,urllib.request,base64,time,uuid,sys,concurrent.futures as cf
import os; key=os.environ['MODEL_API_KEY']
def call(path,body,files=None):
    if files is None:
        req=urllib.request.Request('https://api.meta.ai/v1/'+path,data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
    else:
        b=uuid.uuid4().hex; parts=[f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode() for k,v in body.items()]
        for f in files: parts.append(f'--{b}\r\nContent-Disposition: form-data; name="image"; filename="in.png"\r\nContent-Type: image/png\r\n\r\n'.encode()+open(f,'rb').read()+b'\r\n')
        parts.append(f'--{b}--\r\n'.encode())
        req=urllib.request.Request('https://api.meta.ai/v1/'+path,data=b''.join(parts),headers={'Authorization':'Bearer '+key,'Content-Type':'multipart/form-data; boundary='+b})
    for attempt in range(2):
        try: return json.load(urllib.request.urlopen(req,timeout=400))
        except urllib.error.HTTPError as e:
            msg=e.read().decode()[:300]
            if e.code in (429,500,502,503) and attempt==0: time.sleep(20); continue
            return {'error':f'HTTP {e.code} {msg}'}
        except Exception as e:   # dropped connection / timeout: retry once, then report instead of crashing the batch
            if attempt==0: time.sleep(15); continue
            return {'error':f'{type(e).__name__}: {e}'}
def job(j):
    name,prompt,size,src=j['name'],j['prompt'],j.get('size','1024x1024'),j.get('src')
    t=time.time(); body={'model':'muse-image-1.0','prompt':prompt,'size':size,'response_format':'b64_json'}
    r=call('images/edits',body,[src]) if src else call('images/generations',dict(body,n=1))
    if 'error' in r: return name,r['error']
    open(name+'.webp','wb').write(base64.b64decode(r['data'][0]['b64_json']))
    return name,'%.0fs %s %s'%(time.time()-t,r.get('size'),r.get('usage',{}).get('total_tokens'))
jobs=json.load(open(sys.argv[1]))
with cf.ThreadPoolExecutor(int(sys.argv[2]) if len(sys.argv)>2 else 4) as ex:
    for n,res in ex.map(job,jobs): print(n,res,flush=True)
