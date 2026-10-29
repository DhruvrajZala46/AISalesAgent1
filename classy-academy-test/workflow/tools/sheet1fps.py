# sheet1fps.py <video> <words.json> <outprefix> [t0] [t1]: 1 frame/s, each tile with the words spoken in that second
import sys, json, subprocess, numpy as np, cv2
V, WJ, OUT = sys.argv[1:4]; t0 = float(sys.argv[4]) if len(sys.argv) > 4 else 0; t1 = float(sys.argv[5]) if len(sys.argv) > 5 else 1e9
W = json.load(open(WJ)); w, h = 320, 180
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', str(t0), '-i', V, '-vf', f'fps=1,scale={w}:{h}', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
tiles = []; k = 0
while True:
    b = p.stdout.read(w * h * 3)
    if len(b) < w * h * 3: break
    t = t0 + k + 0.5; k += 1
    if t > t1: break
    im = np.frombuffer(b, np.uint8).reshape(h, w, 3).copy()
    txt = ' '.join(x[0] for x in W if t - 0.9 <= x[1] < t + 0.4)
    im = cv2.copyMakeBorder(im, 0, 34, 0, 0, cv2.BORDER_CONSTANT, value=(255, 255, 255))
    cv2.putText(im, f'{int(t // 60)}:{int(t % 60):02d}', (3, 15), 0, 0.5, (0, 0, 255), 2)
    cv2.putText(im, txt[:44], (2, h + 14), 0, 0.42, (0, 0, 0), 1); cv2.putText(im, txt[44:88], (2, h + 30), 0, 0.42, (0, 0, 0), 1)
    tiles.append(im)
per = 48
for i in range(0, len(tiles), per):
    g = tiles[i:i + per]
    while len(g) % 6: g.append(np.full_like(tiles[0], 255))
    cv2.imwrite(f'{OUT}_{i // per:02d}.jpg', np.vstack([np.hstack(g[j:j + 6]) for j in range(0, len(g), 6)]), [cv2.IMWRITE_JPEG_QUALITY, 80])
print(len(tiles))
