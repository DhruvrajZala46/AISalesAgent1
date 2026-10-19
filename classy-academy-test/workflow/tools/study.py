# study.py - second-by-second study kit for one of the channel's own videos (vid/<id>.mp4 + vid/<id>.en.json3)
#   python3 -I study.py <id>
# -> study/<id>/sheet_MM.jpg  one sheet per minute: 60 frames (1 per second) with time, measured layout and the spoken words
#    study/<id>/seconds.json  per second: layout, spoken words, loudness; cuts.json: every picture change (cut / dissolve)
#    study/<id>/audio.json    voice level, music level in the pauses, possible sound effects
import sys, os, json, subprocess, re
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
vid = sys.argv[1]; V = f'vid/{vid}.mp4'; O = f'study/{vid}'; os.makedirs(O, exist_ok=True)
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', V], capture_output=True, text=True).stdout)
# ---------- frames at 10 fps (small) for cuts, 1 fps (bigger) for the sheets
def frames(fps, w, h):
    p = subprocess.run(['ffmpeg', '-v', 'error', '-i', V, '-vf', f'fps={fps},scale={w}:{h}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                       capture_output=True).stdout
    return np.frombuffer(p, np.uint8).reshape(-1, h, w, 3)
F10 = frames(10, 128, 72).astype(np.float32); F1 = frames(1, 288, 162)
# ---------- picture changes: a cut = one big jump; a dissolve = a run of medium changes ending in a different picture
d = np.abs(np.diff(F10, axis=0)).mean(axis=(1, 2, 3))
cuts, i = [], 0
while i < len(d):
    if d[i] > 28: cuts.append(dict(t=round((i + 1) / 10, 1), kind='cut', size=round(float(d[i]), 1))); i += 2; continue
    if d[i] > 5:
        j = i
        while j < len(d) and d[j] > 4: j += 1
        if j - i >= 3 and np.abs(F10[j] - F10[i]).mean() > 25:
            cuts.append(dict(t=round(i / 10, 1), kind='dissolve', dur=round((j - i) / 10, 1))); i = j; continue
    i += 1
json.dump(cuts, open(f'{O}/cuts.json', 'w'))
# ---------- layout of every second (measured from the pixels)
def caramel(px):  # warm caramel/beige backdrop: r>g>b, saturated, mid-bright
    r, g, b = px[..., 0], px[..., 1], px[..., 2]
    return ((r > g + 12) & (g > b + 12) & (r > 120) & (r < 245)).mean()
def layout(f):
    f = f.astype(np.float32); m = f.mean()
    if m > 238 and f.std() < 25: return 'WHITE/CARD'
    if m < 14: return 'BLACK'
    L, R, C = f[:, :40], f[:, -40:], f[:, 110:178]
    smooth = lambda a: np.abs(np.diff(a, axis=1)).mean() < 3.5
    if caramel(L) > 0.8 and caramel(R) > 0.8 and smooth(L) and smooth(R):
        if caramel(C) > 0.8 and smooth(C): return 'CARAMEL(text/empty)'
        return 'CARAMEL+centre'
    g = np.abs(np.diff(f.mean(2), axis=1)); colsedge = (g > 25).mean(0)
    edges = [x for x in range(20, 268) if colsedge[x] > 0.6]
    if edges: return f'ROW/PANELS({len(set(e // 10 for e in edges)) + 1})'
    if (f > 235).all(axis=2).mean() > 0.35: return 'CREAM/WHITE+picture'
    return 'FULL'
lay = [layout(f) for f in F1]
# ---------- words per second from the captions
words = [''] * (len(F1) + 2)
cj = f'vid/{vid}.en.json3'
if os.path.exists(cj):
    for e in json.load(open(cj)).get('events', []):
        for s in e.get('segs') or []:
            t = (e['tStartMs'] + s.get('tOffsetMs', 0)) / 1000; w = s.get('utf8', '').strip()
            if w and int(t) < len(words): words[int(t)] += (' ' if words[int(t)] else '') + w
# ---------- sound: loudness per 100 ms; voice = seconds with words; music = level in word-free stretches
pcm = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', V, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout, np.int16).astype(np.float32) / 32768
blk = 1600; n = len(pcm) // blk; rms = np.sqrt((pcm[:n * blk].reshape(n, blk) ** 2).mean(1) + 1e-12); db = 20 * np.log10(rms + 1e-9)
voiced = np.zeros(n, bool)
for sec, w in enumerate(words):
    if w: voiced[sec * 10:(sec + 1) * 10] = True
gap = ~voiced
for k in range(n):   # only stretches of >= 0.6 s without words, away from speech edges
    if gap[k] and not (gap[max(0, k - 3):k + 4].all()): gap[k] = False
voice_db = float(np.percentile(db[voiced & (db > -60)], 60)) if (voiced & (db > -60)).any() else None
music_db = float(np.median(db[gap & (db > -70)])) if (gap & (db > -70)).any() else None
spikes = [round(k / 10, 1) for k in range(1, n - 1) if gap[k] and db[k] > (music_db or -99) + 12 and db[k] > db[k - 1] + 8]
json.dump(dict(voice_db=voice_db, music_db_in_pauses=music_db, music_under_voice=(round(voice_db - music_db, 1) if voice_db and music_db else None),
               possible_sfx=spikes[:40], silent_start=float(np.argmax(db > -50) / 10), duration=dur), open(f'{O}/audio.json', 'w'), indent=1)
# ---------- per-second record
cut_s = {}
for c in cuts: cut_s.setdefault(int(c['t']), []).append(c['kind'][0])
secs = [dict(t=s, layout=lay[s], words=words[s], change=''.join(cut_s.get(s, [])), db=round(float(db[s * 10:(s + 1) * 10].mean()), 1) if s * 10 < n else None)
        for s in range(len(F1))]
json.dump(secs, open(f'{O}/seconds.json', 'w'), indent=0)
# ---------- sheets: one per minute, 6 rows x 10 frames, layout + words under each frame
font = ImageFont.load_default()
for m0 in range(0, len(F1), 60):
    part = range(m0, min(m0 + 60, len(F1)))
    sh = Image.new('RGB', (10 * 292, 6 * 222 + 20), 'white'); dr = ImageDraw.Draw(sh)
    dr.text((4, 4), f'{vid}  minute {m0 // 60}', fill='red')
    for k, s in enumerate(part):
        x, y = (k % 10) * 292, 20 + (k // 10) * 222
        sh.paste(Image.fromarray(F1[s]), (x + 2, y))
        ch = secs[s]['change']
        dr.text((x + 2, y + 163), f"{s // 60}:{s % 60:02d} {lay[s][:22]} {('cut' if 'c' in ch else '') + (' diss' if 'd' in ch else '')}", fill='blue')
        w = secs[s]['words']
        dr.text((x + 2, y + 176), w[:46], fill='black'); dr.text((x + 2, y + 188), w[46:92], fill='black'); dr.text((x + 2, y + 200), w[92:138], fill='black')
    sh.save(f'{O}/sheet_{m0 // 60:02d}.jpg', quality=80)
# ---------- summary
from collections import Counter
cnt = Counter(l.split('(')[0] for l in lay)
shots = [c for c in cuts]; dis = [c for c in cuts if c['kind'] == 'dissolve']
print(json.dumps(dict(id=vid, seconds=len(F1), layout_share={k: round(v / len(lay), 2) for k, v in cnt.most_common()},
                      picture_changes=len(shots), dissolves=len(dis), median_dissolve=(float(np.median([c['dur'] for c in dis])) if dis else None),
                      changes_per_min=round(len(shots) / (dur / 60), 1), audio=json.load(open(f'{O}/audio.json')))))
