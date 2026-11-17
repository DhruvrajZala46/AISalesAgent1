# vsall.py - one row per chosen clip window: 8 frames across the window at 216 px wide, slot, key, window, creator
import json, subprocess, io, os, sys
from PIL import Image, ImageDraw
from concurrent.futures import ThreadPoolExecutor
exec('CROP={};MAXSLOW={}\n' + open('clips.py').read())
meta = json.load(open('raw/meta.json'))
order = [l.strip() for l in open('slot_order.txt')] if os.path.exists('slot_order.txt') else list(C)
FW, FH, N = 216, 384, 8
def frame(k, t):
    b = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', f'raw/{k}.mp4', '-frames:v', '1', '-vf',
                        f'scale={FW}:{FH}:force_original_aspect_ratio=decrease,pad={FW}:{FH}:(ow-iw)/2:(oh-ih)/2', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
    try: return Image.open(io.BytesIO(b)).convert('RGB')
    except Exception: return Image.new('RGB', (FW, FH), 'grey')
os.makedirs('vs', exist_ok=True); EX = ThreadPoolExecutor(8); per = 4
for pg in range(0, len(order), per):
    sh = Image.new('RGB', (N * (FW + 4), per * (FH + 26)), 'white'); dr = ImageDraw.Draw(sh)
    for r, slot in enumerate(order[pg:pg + per]):
        k, a, b = C[slot]; y = r * (FH + 26)
        dr.text((3, y + 4), f"{slot}  {k}  {a}-{b}  @{meta.get(k, {}).get('user', '?')}", fill='red')
        ts = [a + (b - a) * j / (N - 1) for j in range(N)]
        for j, im in enumerate(EX.map(lambda t_: frame(k, t_), ts)):
            sh.paste(im, (j * (FW + 4), y + 22)); dr.text((j * (FW + 4) + 3, y + 24), f'{ts[j]:.1f}', fill='yellow')
    sh.save(f'vs/v_{pg // per:02d}.jpg', quality=82)
print('sheets', (len(order) + per - 1) // per)
