# oldclash.py - new clips whose footage matches a clip USED in an earlier video (1 fps dHash); run in the new work folder.
# Edit the list of earlier work folders (here cwp, cwc) to the last videos' folders.
import json, numpy as np
S = '/tmp/claude-0/-home-user-AISalesAgent1/140e17c2-af15-50d0-a685-731162836c6b/scratchpad/'
ob = {}
for w in ('cwp', 'cwc'):
    old = json.load(open(S + w + '/dhash.json'))
    for k in open(S + w + '/used.txt').read().split():
        if old.get(k): ob[f'{w}:{k}'] = np.unpackbits(np.array(old[k], np.uint8), axis=1)
new = json.load(open('dhash.json')); hits = {}
for k, h in new.items():
    if not h: continue
    A = np.unpackbits(np.array(h, np.uint8), axis=1)
    for o, B in ob.items():
        d = (A[:, None, :] != B[None, :, :]).sum(2)
        if int((d.min(1) <= 5).sum()) >= 2: hits.setdefault(k, []).append(o)
json.dump(hits, open('oldclash.json', 'w'), indent=0)
print(len(ob), 'old clips;', len(hits), 'new clips repeat earlier footage:', ' '.join(sorted(hits)))
