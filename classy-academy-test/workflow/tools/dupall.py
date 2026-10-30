# dupall.py - group every downloaded clip by FOOTAGE (dHash at 1 frame/s): re-pins of one reel end up in one group.
# usage (in the work folder): python3 dupall.py -> dupgroups.json ; python3 dupall.py check used.txt -> clashes among used
import sys, subprocess, json, os, io
import numpy as np
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
keys = sorted(f[:-4] for f in os.listdir('raw') if f.endswith('.mp4'))
CACHE = 'dhash.json'; C = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
def hashes(k):
    out = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-i', f'raw/{k}.mp4', '-vf', 'fps=1,scale=9:8,format=gray', '-f', 'rawvideo', '-'], capture_output=True).stdout
    a = np.frombuffer(out, np.uint8).reshape(-1, 8, 9).astype(np.int16)
    return [np.packbits((f[:, 1:] > f[:, :-1]).flatten()).tolist() for f in a]
todo = [k for k in keys if k not in C]
with ThreadPoolExecutor(8) as ex:
    for k, h in zip(todo, ex.map(hashes, todo)): C[k] = h
json.dump(C, open(CACHE, 'w'))
ks = [k for k in keys if C.get(k)]
bits = {k: np.unpackbits(np.array(C[k], np.uint8), axis=1) for k in ks}
def same(a, b):
    A, B = bits[a], bits[b]
    d = (A[:, None, :] != B[None, :, :]).sum(2)
    return int((d.min(1) <= 5).sum()) >= 2 and int((d.min(0) <= 5).sum()) >= 2
par = {k: k for k in ks}
def find(x):
    while par[x] != x: par[x] = par[par[x]]; x = par[x]
    return x
for i, a in enumerate(ks):
    for b in ks[i + 1:]:
        if find(a) != find(b) and same(a, b): par[find(b)] = find(a)
groups = {}
for k in ks: groups.setdefault(find(k), []).append(k)
G = [sorted(v) for v in groups.values() if len(v) > 1]
json.dump(G, open('dupgroups.json', 'w'), indent=0)
print(len(G), 'groups of re-pinned footage among', len(ks), 'clips')
if len(sys.argv) > 2 and sys.argv[1] == 'check':
    used = set(open(sys.argv[2]).read().split()); bad = 0
    for g in G:
        u = [k for k in g if k in used]
        if len(u) > 1: bad += 1; print('SAME FOOTAGE USED TWICE:', u)
    print('clashes among used clips:', bad)
