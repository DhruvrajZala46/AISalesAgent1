# compile_picks.py : picks/<ID>.json (the sourcing records) -> project/picks.json (render settings: file, in, speed, focus, zoom)
# Product photos (kind C) render from their cut-out media/cut/<ID>.png (tools/cutout.py).
import json, os, glob
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = {b['id']: b for b in json.load(open(f'{L}/plan/briefs.json'))}
out, gaps = {}, []
for aid, b in B.items():
    f = f'{L}/picks/{aid}.json'
    if not os.path.exists(f): gaps.append(aid + '(none)'); continue
    p = json.load(open(f))
    if p.get('gap'): gaps.append(aid); continue
    m = dict(file=p['file'], focus=p.get('focus_auto') or p.get('focus', [0.5, 0.42]), note=p.get('note', ''))   # focus_auto: tools/facefocus.py
    for k in ('in', 'speed', 'zoom', 'pan'):
        if p.get(k) is not None: m[k] = p[k]
    if b['kind'] == 'C': m['file'] = f'media/cut/{aid}.png'
    elif m['file'].endswith('.mp4'):                      # render from the clean 30 fps copy (tools/normalize.py)
        m['file'] = 'media/clips/' + os.path.basename(m['file'])
        assert os.path.exists(f"{L}/{m['file']}"), f'{aid}: run tools/normalize.py'
    out[aid] = m
json.dump(out, open(f'{L}/project/picks.json', 'w'), indent=1)
print('picks', len(out), '| gaps', gaps)
