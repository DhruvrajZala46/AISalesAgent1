# oldclash.py - new clips whose footage matches a clip USED in the last Diana video (1 fps dHash, blank frames ignored),
# plus new clips from a creator account used in any earlier video (their footage cannot be compared: old media is gone).
import json, numpy as np
def bits(h): return np.unpackbits(np.array(h, np.uint8), axis=1)
def real(B): pc = B.sum(1); return B[(pc >= 10) & (pc <= 54)]
old = json.load(open('olddi/dhash.json')); ob = {}
for k, h in old.items():
    if h:
        B = real(bits(h))
        if len(B): ob['diana:' + k] = B
new = json.load(open('dhash.json')); hits = {}
for k, h in new.items():
    if not h: continue
    A = real(bits(h))
    if not len(A): continue
    for o, B in ob.items():
        d = (A[:, None, :] != B[None, :, :]).sum(2)
        if int((d.min(1) <= 5).sum()) >= 2: hits.setdefault(k, []).append(o)
users = set(json.load(open('old_used.json'))['users']); meta = json.load(open('raw/meta.json')) if __import__('os').path.exists('raw/meta.json') else {}
acc = {k: 'account:' + (m.get('user') or '').lower() for k, m in meta.items() if (m.get('user') or '').lower() in users}
json.dump(dict(footage=hits, account=acc), open('oldclash.json', 'w'), indent=0)
print(len(ob), 'old clips;', len(hits), 'new clips repeat old Diana footage:', ' '.join(sorted(hits)), '|', len(acc), 'from accounts used before:', ' '.join(sorted(acc)))
