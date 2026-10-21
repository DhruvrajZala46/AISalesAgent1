# empty_check.py - finds moments in an exported file where only the caramel (or cream/white) backdrop is on screen,
# with no picture and no text, and says whether the voice is talking then.  python3 -I empty_check.py out/<file>.mp4
import sys, json, subprocess
import numpy as np, cv2
f = sys.argv[1]; S = json.load(open('project/clock.json'))['sentences']
def talking(t): return any(s['start'] - 0.05 <= t <= s['end'] + 0.05 for s in S)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vf', 'fps=4,scale=320:180', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
F = np.frombuffer(raw, np.uint8).reshape(-1, 180, 320, 3)
empty = []
for k, fr in enumerate(F):
    g = cv2.cvtColor(fr, cv2.COLOR_RGB2GRAY).astype(np.float32); g[:45, :80] = g[45:90, :80]          # ignore the logo corner
    edges = (np.abs(cv2.Sobel(g, cv2.CV_32F, 1, 0)) + np.abs(cv2.Sobel(g, cv2.CV_32F, 0, 1)) > 40).mean()
    if edges < 0.0015: empty.append(k / 4)
runs, cur = [], None
for t in empty:
    if cur and t - cur[1] <= 0.26: cur[1] = t
    else:
        if cur: runs.append(cur)
        cur = [t, t]
if cur: runs.append(cur)
for a, b in runs:
    tk = any(talking(a + x * 0.25) for x in range(int((b - a) * 4) + 1))
    print(f'{int(a // 60)}:{a % 60:05.2f}-{int(b // 60)}:{b % 60:05.2f}  {b - a + 0.25:.2f}s  talking={tk}')
print('runs', len(runs))
