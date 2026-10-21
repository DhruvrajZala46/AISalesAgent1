# normalize.py : every chosen video -> media/clips/<name>.mp4, a clean constant 30 fps copy (no sound).
# Why: about half of the Pinterest HLS downloads carry a broken frame clock (thousands of junk packets in their last half
# second, "avg 323 fps"), so frame-index seeking lands on the wrong pictures or black. ffmpeg's fps filter keeps the real
# timeline, so the workers' in-points (chosen with ffmpeg) stay valid.
import json, os, glob, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = {b['id'] for b in json.load(open(f'{L}/plan/briefs.json'))}
files = set()
for aid in B:
    f = f'{L}/picks/{aid}.json'
    if os.path.exists(f):
        p = json.load(open(f))
        if not p.get('gap') and p.get('file', '').endswith('.mp4'): files.add(p['file'])
        for extra in p.get('also_files', []): files.add(extra)
os.makedirs(f'{L}/media/clips', exist_ok=True)
def job(rel):
    src = f'{L}/{rel}'; dst = f'{L}/media/clips/{os.path.basename(rel)}'
    if os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(src): return rel, 'ok'
    r = subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-vf', 'fps=30,scale=trunc(iw/2)*2:trunc(ih/2)*2', '-an', '-c:v', 'libx264',
                        '-crf', '15', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', dst], capture_output=True, text=True)
    return rel, 'made' if r.returncode == 0 else 'FAILED ' + r.stderr[-200:]
with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(job, sorted(files)))
print(len(res), 'clips;', sum(1 for _, s in res if s == 'made'), 'made;', [r for r in res if r[1].startswith('FAILED')])
