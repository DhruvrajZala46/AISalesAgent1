# strips.py - what happens INSIDE each clip: one row per clip, a frame every ~2 s with its time,
# so a before -> after or a hands-on step can be cut to the exact second (shot sheets show one frame per shot only).
# usage (inside the video work folder): python3 strips.py <out_prefix> key1 key2 ...   -> <out_prefix>_N.jpg (7 clips per sheet)
#   key:a:b zooms in: 15 frames between a and b seconds (e.g. proportion3:0:16 -> one frame per ~1 s)
import os, sys, json, subprocess, io
from PIL import Image, ImageDraw
F = os.getcwd(); R = F + '/raw'; meta = json.load(open(R + '/meta.json'))
S = json.load(open(F + '/shots.json')) if os.path.exists(F + '/shots.json') else {}
out = sys.argv[1]; keys = [k for k in sys.argv[2:] if os.path.exists(f"{R}/{k.split(':')[0]}.mp4")]
FW, FH, N = 100, 178, 15
def frame(k, t):
    b = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', f'{R}/{k}.mp4', '-frames:v', '1',
                        '-vf', f'scale={FW}:{FH}:force_original_aspect_ratio=increase,crop={FW}:{FH}', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
    try: return Image.open(io.BytesIO(b)).convert('RGB')
    except Exception: return None
for pg in range(0, len(keys), 7):
    sh = Image.new('RGB', (N * (FW + 2), 7 * (FH + 30)), 'white'); dr = ImageDraw.Draw(sh)
    for r, kk in enumerate(keys[pg:pg + 7]):
        k, *ab = kk.split(':')
        d = S.get(k, {}).get('d') or float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'{R}/{k}.mp4'], capture_output=True, text=True).stdout)
        a0, a1 = (float(ab[0]), float(ab[1])) if ab else (0.0, d)
        step = (a1 - a0) / N if ab else max(1.0, d / N); y = r * (FH + 30); m = meta.get(k, {})
        cuts = ' cuts:' + ','.join(f'{a:g}' for a, _ in S[k]['seg'][1:]) if k in S and len(S[k]['seg']) > 1 else ''
        dr.text((3, y + 1), f"{kk} {d:.1f}s @{m.get('user','?')}{cuts}", fill='red')
        for j in range(N):
            t = a0 + j * step + (0.05 if ab else 0.3)
            if t > min(d, a1) - 0.05: break
            im = frame(k, t)
            if im: sh.paste(im, (j * (FW + 2), y + 14)); dr.text((j * (FW + 2) + 2, y + 14 + FH), f'{t:.1f}', fill='blue')
    sh.save(f'{out}_{pg // 7}.jpg', quality=82); print(f'{out}_{pg // 7}.jpg', keys[pg:pg + 7], flush=True)
