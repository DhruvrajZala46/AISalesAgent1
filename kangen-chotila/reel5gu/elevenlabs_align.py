# align2.py: ElevenLabs take -> pauses capped (dramatic ones kept), light tempo to fit <= 89.85 s, beats.json with word times
import json, re, subprocess, difflib, numpy as np
import sys
SR = 44100; MAXDUR = 89.85; LEAD = 0.2; TAIL = 1.1; SRC = sys.argv[1] if len(sys.argv) > 1 else 'ritesh_take1.mp3'
WJ = sys.argv[2] if len(sys.argv) > 2 else 'scribe_words.json'
STEADY = '--steady' in sys.argv
for _a in sys.argv:
    if _a.startswith('--target='): MAXDUR = float(_a.split('=')[1])
CAP_IN, CAP_LINE = (0.1, 0.18) if '--fast' in sys.argv else (0.13, 0.24)
lines = [l.strip() for l in open('../beats.txt') if l.strip()]
tts_lines = [l.strip() for l in open('script_tags.txt') if l.strip()]
SW = json.load(open(WJ))
def norm(t): return re.sub(r'[^઀-૿a-zA-Z0-9]', '', t)
toks = []
for li, (disp, tl) in enumerate(zip(lines, tts_lines)):
    tw = re.sub(r'\[[^\]]+\]', ' ', tl).split(); dw = disp.split()
    if len(tw) != len(dw): dw = tw
    for d, t in zip(dw, tw): toks.append((li, d, norm(t)))
a = [t[2] for t in toks]; b = [norm(w['text']) for w in SW]
assert a == b, 'script/word mismatch'
tm = [(w['start'], w['end']) for w in SW]
y = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', SRC, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout, np.float32)
sil = []
_err = subprocess.run(['ffmpeg', '-nostats', '-i', SRC, '-af', 'silencedetect=n=-40dB:d=0.12', '-f', 'null', '-'], capture_output=True, text=True).stderr
_ss = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', _err)]; _se = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', _err)]
sil = list(zip(_ss, _se))
bounds = [(max(tm[k][1] for k in range(len(toks)) if toks[k][0] == li), min(tm[k][0] for k in range(len(toks)) if toks[k][0] == li + 1)) for li in range(len(lines) - 1)]
def word_at(t): return next((k for k in range(len(toks)) if tm[k][0] - 0.02 <= t <= tm[k][1] + 0.02), None)
DRAMA = {('છે…', 2): 0.32, ('પણ…', 6): 0.34, ('વિચારો…', 9): 0.32, ('આવે.', 10): 0.5}
cuts = []   # (start, end) of audio to drop
for s, e in sil:
    d = e - s; cap = CAP_IN
    if any(s - 0.25 <= be <= e + 0.25 or s <= bs <= e for be, bs in bounds): cap = CAP_LINE
    if not STEADY and any(abs(s - bounds[i][0]) < 0.6 for i in (9,)): cap = 0.36       # after "આખું ઘર અટકી જાય છે."
    k = word_at(s)
    if not STEADY and k is not None and (toks[k][1], toks[k][0]) in DRAMA: cap = DRAMA[(toks[k][1], toks[k][0])]
    if d > cap: m = (s + e) / 2; cuts.append((m - (d - cap) / 2, m + (d - cap) / 2))
def warp(t): return t - sum(min(max(0, t - c0), c1 - c0) for c0, c1 in cuts)
keep, last = [], 0.0
for c0, c1 in cuts:
    keep.append(y[int(last * SR):int(c0 * SR)]); last = c1
keep.append(y[int(last * SR):int((tm[-1][1] + 0.12) * SR)])
body = np.concatenate(keep); body_d = len(body) / SR
total = LEAD + body_d + TAIL; tempo = max(1.0, total / MAXDUR)
TAIL_S = TAIL
print('cuts', len(cuts), 'removed', round(sum(c1 - c0 for c0, c1 in cuts), 2), 's; body', round(body_d, 2), 'total', round(total, 2), 'tempo', round(tempo, 4))
v = np.concatenate([np.zeros(int(SR * LEAD), np.float32), body, np.zeros(int(SR * TAIL), np.float32)])
v.astype(np.float32).tofile('voice.f32')
af = f'atempo={tempo:.4f},' if tempo > 1.0 else ''
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', 'voice.f32', '-af', f'{af}highpass=f=70,acompressor=threshold=-20dB:ratio=2:attack=8:release=120,loudnorm=I=-15:TP=-1.5:LRA=9', '-ar', '48000', '../assets/voice.wav'], check=True)
T = lambda t: round((LEAD + warp(t)) / tempo, 3)
out = []
for li in range(len(lines)):
    ks = [k for k in range(len(toks)) if toks[k][0] == li]
    out.append(dict(i=li + 1, text=lines[li], start=T(tm[ks[0]][0]), end=T(tm[ks[-1]][1]), words=[[toks[k][1], T(tm[k][0]), T(tm[k][1])] for k in ks]))
json.dump(out, open('../beats.json', 'w'), ensure_ascii=False, indent=0)
d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', '../assets/voice.wav'], capture_output=True, text=True).stdout)
print('voice.wav', round(d, 2), 's; last word ends', out[-1]['end'])
for b in out: print(b['i'], b['start'], b['end'], b['text'][:30])
