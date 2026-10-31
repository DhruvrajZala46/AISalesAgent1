# SRT subtitles from the voice word timings: run inside the video work folder (beats.json + words.json).
# usage: python3 srt_from_words.py out.srt   (max 2 lines x 42 characters, 1-6 s per cue, splits at sentences and commas)
import json, textwrap, sys
b = {x['i']: x for x in json.load(open('beats.json'))}; W = json.load(open('words.json'))
words = []
for i in sorted(b):
    for t, s, e in W[str(i)]: words.append((t, b[i]['start'] + s, b[i]['start'] + e))
MAXC = 42
def wrap(s):
    if len(s) <= MAXC: return [s]
    ws = s.split(); best = None
    for j in range(1, len(ws)):
        a, c = ' '.join(ws[:j]), ' '.join(ws[j:])
        if len(a) <= MAXC and len(c) <= MAXC:
            sc = max(len(a), len(c)) - (12 if ws[j-1][-1] in '.?!"' else 5 if ws[j-1][-1] in ',;:' else 0)
            if best is None or sc < best[0]: best = (sc, [a, c])
    return best[1] if best else textwrap.wrap(s, MAXC)
def text(ws): return ' '.join(w[0] for w in ws)
def fits(ws): return len(wrap(text(ws))) <= 2 and ws[-1][2] - ws[0][1] <= 6.0
def split(ws):
    if fits(ws): return [ws]
    n = len(ws); best = None
    for j in range(2, n - 1):                      # split after word j-1, both sides >= 2 words
        a, c = ws[:j], ws[j:]
        bal = abs(len(text(a)) - len(text(c))) / len(text(ws))
        punct = ws[j-1][0][-1] in ',;:—' or ws[j-1][0].endswith(('."', '?"', '!"', '."'))
        pause = ws[j][1] - ws[j-1][2]
        score = bal - (0.35 if punct else 0) - min(pause, 0.6) * 0.5
        if best is None or score < best[0]: best = (score, j)
    j = best[1]; return split(ws[:j]) + split(ws[j:])
# sentences
sents, cur = [], []
for k, w in enumerate(words):
    cur.append(w)
    nxt = words[k+1] if k + 1 < len(words) else None
    if w[0][-1] in '.?!' or w[0][-2:] in ('."', '?"', '!"'):
        if nxt is None or nxt[1] - w[2] > 0.2: sents.append(cur); cur = []
if cur: sents.append(cur)
cues = []
for s in sents:
    # merge very short sentence with the previous cue if it still fits and follows closely
    dur = lambda c: c[-1][2] - c[0][1]
    if cues and fits(cues[-1] + s) and s[0][1] - cues[-1][-1][2] < 0.9 and (dur(s) < 1.2 or dur(cues[-1]) < 1.2): cues[-1] = cues[-1] + s
    else: cues += split(s)
def ts(t):
    ms = int(round(t * 1000)); return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'
out = []
for n, c in enumerate(cues):
    st = c[0][1]; en = c[-1][2] + 0.4
    if n + 1 < len(cues): en = min(en, cues[n+1][0][1] - 0.05)
    en = max(en, min(st + 1.0, cues[n+1][0][1] - 0.05) if n + 1 < len(cues) else st + 1.0)
    out.append(f'{n+1}\n{ts(st)} --> {ts(en)}\n' + '\n'.join(wrap(text(c))) + '\n')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out))
L = [len(l) for c in cues for l in wrap(text(c))]; d = [c[-1][2] - c[0][1] for c in cues]
one = [text(c) for c in cues if len(c) == 1]
print('short <1s:', [(round(c[0][1],1), text(c)) for c in cues if c[-1][2]-c[0][1] < 1.0]); print(len(cues), 'cues; max line', max(L), '; dur', round(min(d), 2), '-', round(max(d), 2), '; one-word cues:', one,
      '; words', sum(len(c) for c in cues), '/', len(words))
