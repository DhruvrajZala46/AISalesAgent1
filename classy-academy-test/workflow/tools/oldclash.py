# oldclash.py (run in the new work folder; ../cwp = the last video's folder) - new clips whose footage matches a clip USED in the last video (cwp/used.txt), by 1 fps dHash
import json, sys, numpy as np
old = json.load(open('../cwp/dhash.json')); used = [k for k in open('../cwp/used.txt').read().split() if k in old and old[k]]
new = json.load(open('dhash.json'))
ob = {k: np.unpackbits(np.array(old[k], np.uint8), axis=1) for k in used}
hits = {}
for k, h in new.items():
    if not h: continue
    A = np.unpackbits(np.array(h, np.uint8), axis=1)
    for o, B in ob.items():
        d = (A[:, None, :] != B[None, :, :]).sum(2)
        if int((d.min(1) <= 5).sum()) >= 2: hits.setdefault(k, []).append(o)
json.dump(hits, open('oldclash.json', 'w'), indent=0)
print(len(hits), 'new clips repeat footage of the last video:', ' '.join(sorted(hits)))
