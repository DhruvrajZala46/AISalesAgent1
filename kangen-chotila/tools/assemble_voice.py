# assemble_voice.py -> assets/voice.wav + beats.json [{i,text,start,end,words:[[disp,start,end]]}]
import json, subprocess, numpy as np
SR = 48000
W = json.load(open('words.json')); B = [l.strip() for l in open('beats.txt') if l.strip()]
GAP = {1: 0.35, 2: 0.45, 3: 0.35, 4: 0.40, 5: 0.40, 6: 0.40, 7: 0.40, 8: 0.0}
LEAD = 0.25; TAIL = 2.2; CUT0 = 0.05
def load(i):
    a = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'tts/c{i:03d}.wav', '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(a, np.float32)
parts = [np.zeros(int(SR * LEAD), np.float32)]; t = LEAD; out = []
for i, text in enumerate(B, 1):
    y = load(i); ws = W[str(i)]
    end = min(len(y) / SR, ws[-1][2] + 0.12)
    seg = y[int(CUT0 * SR):int(end * SR)].copy()
    n = int(0.01 * SR); seg[:n] *= np.linspace(0, 1, n); seg[-n:] *= np.linspace(1, 0, n)
    disp = text.split(' ')
    assert len(disp) == len(ws), (i, len(disp), len(ws))
    words = [[d, round(t + w[1] - CUT0, 3), round(t + w[2] - CUT0, 3)] for d, w in zip(disp, ws)]
    d = len(seg) / SR
    out.append(dict(i=i, text=text, start=round(t, 3), end=round(t + d, 3), words=words))
    parts += [seg, np.zeros(int(SR * GAP[i]), np.float32)]; t += d + GAP[i]
parts.append(np.zeros(int(SR * TAIL), np.float32))
v = np.concatenate(parts)
v.astype(np.float32).tofile('assets/voice.f32')
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', 'assets/voice.f32', 'assets/voice_raw.wav'], check=True)
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', 'assets/voice_raw.wav', '-af', 'highpass=f=70,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,loudnorm=I=-15:TP=-1.5:LRA=7', '-ar', str(SR), 'assets/voice.wav'], check=True)
json.dump(out, open('beats.json', 'w'), ensure_ascii=False, indent=0)
print('duration', round(len(v) / SR, 2))
for b in out: print(b['i'], b['start'], b['end'], b['text'][:40])
