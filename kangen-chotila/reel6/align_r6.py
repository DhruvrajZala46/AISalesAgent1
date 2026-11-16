# align_r6.py: ElevenLabs take + edge-tts word proportions -> beats.json + assets/voice.wav (pauses capped, tempo to TARGET)
import json, re, subprocess, numpy as np, sys
SR = 44100; SRC = 'voice_raw.mp3'; TARGET = float(sys.argv[1]) if len(sys.argv) > 1 else 38.0; LEAD, TAIL = 0.15, 0.9
lines = [l.strip() for l in open('beats.txt') if l.strip()]
E = json.load(open('words.json'))                       # edge-tts: {line: [[w, s, e], ...]}
edur = [E[str(i + 1)][-1][2] - E[str(i + 1)][0][1] for i in range(len(lines))]
err = subprocess.run(['ffmpeg', '-nostats', '-i', SRC, '-af', 'silencedetect=n=-40dB:d=0.1', '-f', 'null', '-'], capture_output=True, text=True).stderr
sil = list(zip([float(x) for x in re.findall(r'silence_start: ([\d.]+)', err)], [float(x) for x in re.findall(r'silence_end: ([\d.]+)', err)]))
y = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', SRC, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout, np.float32)
total = len(y) / SR
v0 = 0.0; v1 = sil[-1][0] if sil and sil[-1][1] >= total - 0.05 else total
# choose the 9 line-break silences by dynamic programming: line lengths should match edge-tts lengths x one global ratio
import math
C = [(s0, e0) for s0, e0 in sil if e0 - s0 >= 0.15 and e0 < v1 - 0.05 and s0 > 0.3]
n, K = len(C), len(lines) - 1
def solve(r):
    INF = 1e9; dp = [[INF] * n for _ in range(K)]; bk = [[-1] * n for _ in range(K)]
    def cost(k, a0, b0): d = b0 - a0; return INF if d <= 0.3 else (math.log(d / (r * edur[k]))) ** 2
    for j in range(n): dp[0][j] = cost(0, v0, C[j][0]) - 0.8 * (C[j][1] - C[j][0])
    for k in range(1, K):
        for j in range(n):
            for i in range(j):
                v = dp[k - 1][i] + cost(k, C[i][1], C[j][0]) - 0.8 * (C[j][1] - C[j][0])
                if v < dp[k][j]: dp[k][j], bk[k][j] = v, i
    best = min(range(n), key=lambda j: dp[K - 1][j] + cost(K, C[j][1], v1)); path = [best]
    for k in range(K - 1, 0, -1): path.append(bk[k][path[-1]])
    return [C[j] for j in reversed(path)]
r = (v1 - v0) * 0.85 / sum(edur)
for _ in range(3):
    bounds = solve(r); prev = v0; durs = []
    for s0, e0 in bounds: durs.append(s0 - prev); prev = e0
    durs.append(v1 - prev); r = sum(durs) / sum(edur)
spans = []; prev = v0
for s, e in bounds: spans.append((prev, s)); prev = e
spans.append((prev, v1))
print('line spans:', ' '.join(f'{a:.2f}-{b:.2f}' for a, b in spans))
# word times by edge proportions
W = []
for li, (a, b) in enumerate(spans):
    ew = E[str(li + 1)]; e0 = ew[0][1]; e1 = ew[-1][2]; disp = lines[li].split()
    if len(disp) != len(ew): disp = [w[0] for w in ew]
    W.append([[d, a + (w[1] - e0) / (e1 - e0) * (b - a), a + (w[2] - e0) / (e1 - e0) * (b - a)] for d, w in zip(disp, ew)])
# cap pauses: between lines 0.18 s, inside lines 0.10 s
cuts = []
for s, e in sil:
    if e > total - 0.02 or s < 0.02: continue
    cap = 0.18 if (s, e) in bounds else 0.10
    if e - s > cap: m = (s + e) / 2; cuts.append((m - (e - s - cap) / 2, m + (e - s - cap) / 2))
def warp(t): return t - sum(min(max(0, t - c0), c1 - c0) for c0, c1 in cuts)
keep, last = [], 0.0
for c0, c1 in cuts: keep.append(y[int(last * SR):int(c0 * SR)]); last = c1
keep.append(y[int(last * SR):int((v1 + 0.08) * SR)])
body = np.concatenate(keep); tot = LEAD + len(body) / SR + TAIL; tempo = max(1.0, tot / TARGET)
print('removed', round(sum(c1 - c0 for c0, c1 in cuts), 2), 's; before tempo', round(tot, 2), 'tempo', round(tempo, 3))
np.concatenate([np.zeros(int(SR * LEAD), np.float32), body, np.zeros(int(SR * TAIL), np.float32)]).astype(np.float32).tofile('voice.f32')
af = f'atempo={tempo:.4f},' if tempo > 1 else ''
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', 'voice.f32', '-af', f'{af}highpass=f=70,acompressor=threshold=-20dB:ratio=2:attack=8:release=120,loudnorm=I=-15:TP=-1.5:LRA=9', '-ar', '48000', 'assets/voice.wav'], check=True)
T = lambda t: round((LEAD + warp(t)) / tempo, 3)
out = [dict(i=li + 1, text=lines[li], start=T(W[li][0][1]), end=T(W[li][-1][2]), words=[[d, T(s), T(e)] for d, s, e in W[li]]) for li in range(len(lines))]
json.dump(out, open('beats.json', 'w'), ensure_ascii=False, indent=0)
d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', 'assets/voice.wav'], capture_output=True, text=True).stdout)
print('voice.wav', round(d, 2))
for b in out: print(b['i'], b['start'], b['end'], ' '.join(f"{w[0]}@{w[1]:.2f}" for w in b['words'])[:150])
