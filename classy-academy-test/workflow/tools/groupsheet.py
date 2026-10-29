# groupsheet.py <group index...>: verification sheets for pick groups (groups.json: [[name, [keys]], ...]), 10 clips per sheet,
# 7 frames each with their times, so every pick is checked by eye before use (EDIT-RULES.md section 6). Duplicates in dups.json are skipped.
import json, os, subprocess, io, sys
from PIL import Image, ImageDraw
from concurrent.futures import ThreadPoolExecutor
G = json.load(open('groups.json')); os.makedirs('vs', exist_ok=True)
N, w, h = 7, 112, 200
def dur(k):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'raw/{k}.mp4'], capture_output=True, text=True).stdout.strip()
    try: return float(r)
    except: return 0
def fr(a):
    k, t = a
    r = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', f'raw/{k}.mp4', '-frames:v', '1', '-vf', f'scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:white', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
    try: return Image.open(io.BytesIO(r)).convert('RGB')
    except Exception: return Image.new('RGB', (w, h), 'black')
DUP = json.load(open("dups.json")) if os.path.exists("dups.json") else {}
for gi in map(int, sys.argv[1:]):
    name, ks = G[gi]; ks = [k for k in ks if os.path.exists(f'raw/{k}.mp4') and k not in DUP]
    for p in range(0, len(ks), 10):
        out = f'vs/G{gi:02d}_{p // 10}.jpg'; kk = ks[p:p + 10]; cw = 150 + N * (w + 2); rn = (len(kk) + 1) // 2
        sh = Image.new('RGB', (2 * cw, rn * (h + 16) + 18), 'white'); dr = ImageDraw.Draw(sh); dr.text((4, 2), name, fill='black')
        for r, k in enumerate(kk):
            d = dur(k); ts = [d * (j + 0.5) / N for j in range(N)]
            with ThreadPoolExecutor(4) as ex: ims = list(ex.map(fr, [(k, t) for t in ts]))
            x0 = (r % 2) * cw; y = 18 + (r // 2) * (h + 16)
            dr.text((x0 + 3, y + 3), f'{k}\n{d:.1f}s', fill='red')
            for j, (im, t) in enumerate(zip(ims, ts)):
                x = x0 + 150 + j * (w + 2); sh.paste(im, (x, y)); dr.text((x + 2, y + h + 1), f'{t:.1f}', fill='blue')
        sh.save(out, quality=80); print(out, flush=True)
