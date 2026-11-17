# motion.py - how much each chosen window really moves (static "videos" are often AI stills): mean abs difference of frames 1 s apart
import json, subprocess, numpy as np, re
from concurrent.futures import ThreadPoolExecutor
exec("CROP={};MAXSLOW={}\n" + open('clips.py').read()); M = json.load(open('raw/meta.json'))
def fr(k, t):
    b = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', f'raw/{k}.mp4', '-frames:v', '1', '-vf', 'scale=90:160,format=gray', '-f', 'rawvideo', '-'], capture_output=True).stdout
    return np.frombuffer(b, np.uint8).astype(float) if len(b) == 14400 else None
def mot(it):
    s, (k, a, b) = it
    if b - a < 0.5: return s, k, -1
    ts = np.arange(a, b - 0.01, 1.0); fs = [fr(k, t) for t in ts] + [fr(k, b - 0.05)]; fs = [f for f in fs if f is not None]
    d = [np.abs(x - y).mean() for x, y in zip(fs, fs[1:])]
    return s, k, (float(np.mean(d)) if d else -1)
with ThreadPoolExecutor(8) as ex: res = list(ex.map(mot, C.items()))
for s, k, m in sorted(res, key=lambda r: r[2]):
    mm = M.get(k, {}); print(f"{m:6.1f} {s:5s} {k:10s} @{mm.get('user','')[:22]:22s} {re.sub(r'https?://', '', mm.get('src',''))[:30]:30s} {mm.get('title','')[:50]}")
