# dedupe.py: finds the same footage downloaded under different searches (dHash of 3 frames per clip) inside the work folder.
# Writes dups.json {key: first key with the same footage}; build a video from one copy only.
import json, os, subprocess, io, glob, sys
import numpy as np
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
C = json.load(open('dhash.json')) if os.path.exists('dhash.json') else {}
def dur(f):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout.strip()
    try: return float(r)
    except: return 0
def dh(f, t):
    r = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', f, '-frames:v', '1', '-vf', 'scale=9:16,format=gray', '-f', 'rawvideo', '-'], capture_output=True).stdout
    if len(r) < 144: return None
    a = np.frombuffer(r[:144], np.uint8).reshape(16, 9).astype(int); return ''.join('1' if x else '0' for x in (a[:, 1:] > a[:, :-1]).flatten())
def one(f):
    k = os.path.basename(f)[:-4]
    if k in C: return k, C[k]
    d = dur(f); return k, [dh(f, d * p) for p in (0.15, 0.5, 0.85)] + [d]
fs = sorted(glob.glob('raw/*.mp4'))
with ThreadPoolExecutor(3) as ex:
    for k, v in ex.map(one, fs): C[k] = v
json.dump(C, open('dhash.json', 'w'))
def dist(a, b): return sum(x != y for x, y in zip(a, b)) if a and b else 999
# order = picks order (groups.json) so the first-listed copy is kept
G = json.load(open('groups.json')); order = [k for _, ks in G for k in ks] + sorted(C)
seen = []; D = {}
for k in dict.fromkeys(order):
    if k not in C: continue
    h = C[k]
    for s in seen:
        hs = C[s]
        # same footage if any frame pair matches closely (clips can be trimmed differently)
        m = min(dist(a, b) for a in h[:3] for b in hs[:3])
        if m <= 10 and sum(1 for a in h[:3] for b in hs[:3] if dist(a, b) <= 14) >= 2: D[k] = s; break
    else: seen.append(k)
json.dump(D, open('dups.json', 'w'), indent=0)
print(len(C), 'clips', len(D), 'duplicates')
