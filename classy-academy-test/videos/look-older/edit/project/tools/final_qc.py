# final_qc.py - checks the exported file itself: length of picture and sound, black or frozen stretches, loudness, and contact
# sheets taken from the file (a frame every 2 s with the spoken words) -> qc/final_NN.jpg, qc/final_qc.json
#   python3 -I final_qc.py out/<file>.mp4
import sys, json, re, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont
f = sys.argv[1]
probe = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,codec_name,width,height,r_frame_rate,duration,bit_rate:format=duration,size',
                                   '-of', 'json', f], capture_output=True, text=True).stdout)
err = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', f, '-vf', 'blackdetect=d=0.25:pix_th=0.06', '-af', 'ebur128=peak=true',
                      '-f', 'null', '-'], capture_output=True, text=True).stderr
black = re.findall(r'black_start:([\d.]+) black_end:([\d.]+)', err)
I = re.findall(r'I:\s+(-?[\d.]+) LUFS', err); TP = re.findall(r'Peak:\s+(-?[\d.]+) dBFS', err)
# frozen pictures: 2 fps, compare consecutive frames (a long run of identical frames = a stalled clip)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vf', 'fps=2,scale=160:90', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 90, 160).astype(np.int16)
d = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))
frozen, run = [], 0
for k, x in enumerate(d):
    run = run + 1 if x < 0.15 else 0
    if run == 6: frozen.append(round((k - 5) / 2, 1))          # 3 s with no change at all
res = dict(probe=probe, black=black, lufs=float(I[-1]) if I else None, true_peak=float(TP[-1]) if TP else None, frozen_3s_starts=frozen)
json.dump(res, open('qc/final_qc.json', 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != 'probe'}), json.dumps(probe['format']))
# sheets from the file
S = json.load(open('project/clock.json'))['sentences']
def words(t):
    for s in S:
        if s['start'] <= t < s['end']:
            k = int(len(s['text']) * (t - s['start']) / (s['end'] - s['start'])); return s['text'][max(0, k - 22):k + 22]
    return '(pause)'
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vf', 'fps=0.5,scale=480:270', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
F2 = np.frombuffer(raw, np.uint8).reshape(-1, 270, 480, 3)
for n0 in range(0, len(F2), 40):
    sh = Image.new('RGB', (5 * 484, 8 * 300), 'white'); dr = ImageDraw.Draw(sh)
    for k in range(n0, min(n0 + 40, len(F2))):
        x, y = ((k - n0) % 5) * 484, ((k - n0) // 5) * 300; t = k * 2.0
        sh.paste(Image.fromarray(F2[k]), (x + 2, y))
        dr.text((x + 4, y + 272), f'{int(t // 60)}:{t % 60:04.1f}', fill='blue', font=F); dr.text((x + 4, y + 285), words(t), fill='black', font=F)
    sh.save(f'qc/final_{n0 // 40:02d}.jpg', quality=80)
print('sheets', (len(F2) + 39) // 40)
