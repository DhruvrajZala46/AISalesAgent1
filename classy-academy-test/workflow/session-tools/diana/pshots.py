# parallel shots.json (same format as tools/shots.py), saved every 20 clips; skips excluded.txt
import os, json, subprocess, re, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
R = 'raw'; ex = set(open('excluded.txt').read().split()) if os.path.exists('excluded.txt') else set()
S = json.load(open('shots.json')) if os.path.exists('shots.json') else {}
def probe(f):
    pr = json.loads(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height,color_transfer:format=duration','-of','json',f],capture_output=True,text=True).stdout)
    return float(pr['format']['duration']), pr['streams'][0]['width'], pr['streams'][0]['height'], pr['streams'][0].get('color_transfer','')
def one(k):
    f = f'{R}/{k}.mp4'; d, w, h, tr = probe(f)
    o = subprocess.run(['ffmpeg','-nostdin','-threads','1','-skip_frame','nokey' if d > 60 else 'default','-i',f,'-vf',"fps=10,scale=160:-2,select='gt(scene,0.32)',showinfo",'-an','-f','null','-'],capture_output=True,text=True).stderr
    cuts = [float(x) for x in re.findall(r'pts_time:([\d.]+)', o)]
    b = [0] + [c for c in cuts if 0.4 < c < d - 0.4] + [d]
    seg = [[round(a,2), round(c,2)] for a, c in zip(b, b[1:]) if c - a >= 0.5]
    return k, dict(d=round(d,2), w=w, h=h, hdr=tr in ('arib-std-b67','smpte2084'), seg=seg)
keys = sorted(f[:-4] for f in os.listdir(R) if f.endswith('.mp4') and f[:-4] not in ex and f[:-4] not in S)
n = 0
with ThreadPoolExecutor(8) as ex_:
    for fu in as_completed([ex_.submit(one, k) for k in keys]):
        try: k, v = fu.result(); S[k] = v
        except Exception as e: print('fail', e, flush=True)
        n += 1
        if n % 20 == 0: json.dump(S, open('shots.json','w'), indent=0); print(n, '/', len(keys), flush=True)
json.dump(S, open('shots.json','w'), indent=0); print('PSHOTSDONE', len(S), flush=True)
