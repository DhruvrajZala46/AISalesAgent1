# oldclash.py - new clips whose footage matches a clip USED in an earlier video (1 fps dHash); run in the work folder.
# Black or blank frames are ignored (their hash matches every other blank frame and chained unrelated clips on 16 Nov).
import json, numpy as np
S = '/tmp/claude-0/-home-user-AISalesAgent1/140e17c2-af15-50d0-a685-731162836c6b/scratchpad/'
def bits(h): return np.unpackbits(np.array(h, np.uint8), axis=1)
def real(B): pc = B.sum(1); return B[(pc >= 10) & (pc <= 54)]
ob = {}
for w in ('cwp', 'cwc', 'cwa', 'cwh', 'cwl', 'cwx', 'cwy', 'cwz', 'cwf', 'cwg', 'cws', 'cwe', 'cwu'):
    old = json.load(open(S + w + '/dhash.json'))
    for k in open(S + w + '/used.txt').read().split():
        if old.get(k):
            B = real(bits(old[k]))
            if len(B): ob[f'{w}:{k}'] = B
new = json.load(open('dhash.json')); hits = {}
for k, h in new.items():
    if not h: continue
    A = real(bits(h))
    if not len(A): continue
    for o, B in ob.items():
        d = (A[:, None, :] != B[None, :, :]).sum(2)
        if int((d.min(1) <= 5).sum()) >= 2: hits.setdefault(k, []).append(o)
json.dump(hits, open('oldclash.json', 'w'), indent=0); json.dump(hits, open('oldclash_real.json', 'w'), indent=0)
print(len(ob), 'old clips;', len(hits), 'new clips repeat earlier footage:', ' '.join(sorted(hits)))
