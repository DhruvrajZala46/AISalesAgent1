# empty.py - finds moments where only the caramel backdrop is on screen (no clip, little or no text).
# usage (inside the work folder, after the render): python3 $T/empty.py out/<slug>_v1.mp4
# Prints each run with talking=True/False (from beats.json). A run while the voice talks is a gap to fix,
# unless it is one of the edit's own text screens: open the frame and look (thin script text counts as "empty").
import sys, os, json, subprocess
import numpy as np, cv2
VID = sys.argv[1]
sys.argv = ['ffr.py', '.', '0', '1', 'x.mp4', '1']
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ffr.py')).read().split("if __name__ == '__main__':")[0])
beats = json.load(open('beats.json'))
def talking(t): return any(b['start'] - 0.05 <= t <= b['end'] + 0.05 for b in beats)
w, h, fps = 480, 270, 4
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', VID, '-vf', f'fps={fps},scale={w}:{h}', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
buf = np.empty((H, W, 3), np.float32); k = 0; runs = []
while True:
    b = p.stdout.read(w * h * 3)
    if len(b) < w * h * 3: break
    t = k / fps; k += 1
    o = np.frombuffer(b, np.uint8).reshape(h, w, 3).astype(np.float32)
    draw_bg(buf, t); bg = cv2.resize(cv2.convertScaleAbs(buf), (w, h)).astype(np.float32)
    if (np.abs(o - bg).max(axis=2) > 18).mean() < 0.02:          # < 2% of the picture differs from the bare backdrop
        if runs and abs(t - runs[-1][1] - 1 / fps) < 1e-6: runs[-1][1] = t; runs[-1][2] |= talking(t)
        else: runs.append([t, t, talking(t)])
for a, z, tk in runs: print(f'empty {a:7.2f}-{z:7.2f} ({z - a + 1 / fps:.2f}s) talking={tk}')
print('runs:', len(runs), ' while talking:', sum(1 for r in runs if r[2]))
