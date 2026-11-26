#!/usr/bin/env python3
"""Measure a Short's visual and sound "style numbers" so ours can be compared with a reference creator.

Usage: python3 -I style_metrics.py name=video.mp4 [name2=video2.mp4 ...]   (writes nothing; prints one block per video)

Measures (all from the file itself):
  motion   - share of frames with no visible change, drawing changes per second, hard cuts, whole-frame camera moves
  colour   - median saturation / brightness, 6 dominant colours (k-means on frames every 0.5 s)
  ink      - median outline thickness at 720 px width (dark runs between light pixels)
  sound    - integrated loudness (LUFS), music+SFX bed level under the voice, SFX hits per minute
             (demucs voice split + onsets more than 7 dB over a 1.5 s rolling median of the non-voice stem)
"""
import sys, os, subprocess, tempfile, json
import numpy as np
from scipy.ndimage import median_filter


def gray_frames(p, w=120, fps=30):
    h = int(w * 16 / 9)
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'scale={w}:{h},fps={fps}', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'],
                         capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)


def motion(p):
    F = gray_frames(p)
    d = np.abs(np.diff(F, axis=0)).mean((1, 2))
    cuts = [round((i + 1) / 30, 2) for i, x in enumerate(d) if x > 25]
    moves = 0
    for i in range(len(F) - 1):
        if d[i] > 25 or d[i] < 0.3:
            continue
        a, b = F[i + 1] - F[i + 1].mean(), F[i] - F[i].mean()
        R = np.fft.fft2(a) * np.conj(np.fft.fft2(b)); R /= np.abs(R) + 1e-9
        r = np.abs(np.fft.ifft2(R)); y, x = np.unravel_index(r.argmax(), r.shape)
        if (y not in (0,) or x not in (0,)) and r.max() > 0.3:
            moves += 1
    return dict(still_pct=round(float((d < 0.3).mean() * 100), 1), changes_per_s=round(float((d > 0.25).sum() / (len(F) / 30)), 1),
                hard_cuts=len(cuts), camera_move_frames=moves, seconds=round(len(F) / 30, 1))


def colour(p):
    w = 180; h = 320
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'scale={w}:{h},fps=2', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                         capture_output=True).stdout
    F = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3)
    X = F.reshape(-1, 3)[::7].astype(float)
    mx, mn = X.max(1), X.min(1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1) * 255, 0)
    rng = np.random.default_rng(0); C = X[rng.choice(len(X), 8, replace=False)]
    for _ in range(15):
        l = ((X[:, None] - C[None]) ** 2).sum(2).argmin(1)
        for j in range(len(C)):
            if (l == j).any():
                C[j] = X[l == j].mean(0)
    cnt = np.bincount(l, minlength=len(C)); o = np.argsort(-cnt)[:6]
    return dict(median_saturation=int(np.median(sat)), median_brightness=int(np.median(mx)),
                top_colours=['#%02x%02x%02x %d%%' % (*[int(v) for v in C[i]], round(cnt[i] / cnt.sum() * 100)) for i in o])


def ink(p):
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)
    runs = []
    for t in np.linspace(d * 0.1, d * 0.9, 6):
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.2f}', '-i', p, '-frames:v', '1', '-vf', 'scale=720:1280:flags=lanczos',
                              '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True).stdout
        a = np.frombuffer(raw, np.uint8).reshape(1280, 720).astype(int)
        for row in a[::6]:
            dark = row < 90; i = 0
            while i < len(row):
                if dark[i]:
                    j = i
                    while j < len(row) and dark[j]:
                        j += 1
                    if 0 < i and j < len(row) and row[i - 1] > 150 and row[j] > 150 and j - i <= 12:
                        runs.append(j - i)
                    i = j
                else:
                    i += 1
    return dict(outline_px_at_720=float(np.median(runs)) if runs else None)


def sound(p, tmp):
    lufs = subprocess.run(['ffmpeg', '-nostats', '-i', p, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    I = [l for l in lufs.split('\n') if ' I:' in l][-1].split()[1]
    wav = os.path.join(tmp, 'a.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-ac', '2', '-ar', '44100', wav])
    subprocess.run([sys.executable, '-m', 'demucs', '-n', 'htdemucs', '-o', tmp, wav], capture_output=True)
    d = os.path.join(tmp, 'htdemucs', 'a')

    def load(n):
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(d, n + '.wav'), '-ac', '1', '-ar', '16000', '-f', 's16le', '-'],
                             capture_output=True).stdout
        return np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    vo = load('vocals'); nv = load('drums') + load('other') + load('bass')
    db = lambda x: 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-9)
    hop = 320
    ev = np.array([db(vo[i:i + hop]) for i in range(0, len(vo) - hop, hop)]); en = np.array([db(nv[i:i + hop]) for i in range(0, len(nv) - hop, hop)])
    sp = ev > -35
    base = median_filter(en, size=75); hits = 0; i = 0
    while i < len(en):
        if en[i] - base[i] > 7 and en[i] > -38:
            j = i
            while j < len(en) and en[j] - base[j] > 3:
                j += 1
            hits += 1; i = j
        i += 1
    secs = len(vo) / 16000
    return dict(lufs=float(I), bed_under_voice_db=round(float(np.median(en[sp]) - np.median(ev[sp])), 1), sfx_hits_per_min=round(hits / secs * 60))


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        name, p = arg.split('=', 1)
        with tempfile.TemporaryDirectory() as tmp:
            out = dict(name=name, **motion(p), **colour(p), **ink(p), **sound(p, tmp))
        print(json.dumps(out))
