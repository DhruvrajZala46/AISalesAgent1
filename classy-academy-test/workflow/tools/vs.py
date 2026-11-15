# vs.py name key:a:b ...  -> vs/<name>.jpg, 8 frames per clip across the window (whole clip when no window)
import sys, json, subprocess
D = json.load(open('dur.json')); args = []
for it in sys.argv[2:]:
    p = it.split(':'); k = p[0]
    if k not in D: print('NO CLIP', k); continue
    a = float(p[1]) if len(p) > 1 else 0.3; b = float(p[2]) if len(p) > 2 else D[k][0] - 0.3
    b = min(b, D[k][0] - 0.15); args.append(f'{k}:{a}:{b}:{max(0.2, (b - a) / 7.001):.3f}')
subprocess.run(['python3', 'big.py', f'vs/{sys.argv[1]}.jpg'] + args)
