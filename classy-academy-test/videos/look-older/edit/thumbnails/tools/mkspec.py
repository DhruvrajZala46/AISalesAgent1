# mkspec.py out.json : builds thumb_ce specs from a short plan, reading face boxes from each candidate folder's faces.json
import json, os, sys
B = '/tmp/claude-0/-home-user-AISalesAgent1/73fc3aa5-807d-530d-b865-5c7bcc671679/scratchpad'
LOGO = B + '/hairvid/assets/logo_ca_white.png'
TXT = {'A': ('Details That Make You', 'Look Older', '*wear this instead*', None),
       'B': ('How to Look', 'Younger', '*at any age*', None),
       'C': ('Elegant Ladies', 'Never Look Dated', '*what to wear instead*', 'Never')}
def face(path):
    d = json.load(open(os.path.join(os.path.dirname(path), 'faces.json')))
    return d[os.path.basename(path)]['face']
def spec(concept, out, panels, opts=None):
    t, b, s, u = TXT[concept]
    sp = {'logo': LOGO, 'darken': 25, 'bright': 1.0, 'out': out, 'top': t, 'big': b, 'small': s, 'panels': []}
    if u: sp['underline'] = u
    sp.update(opts or {})
    for img, fw, fy, *rest in panels:
        p = {'img': img, 'face': face(img), 'fw': fw, 'fy': fy}
        for r in rest: p.update(r if isinstance(r, dict) else {'dx': r})
        sp['panels'].append(p)
    return sp
if __name__ == '__main__':
    plan = json.load(open(sys.argv[1]))
    json.dump([spec(*x) for x in plan], open(sys.argv[2], 'w'), indent=1)
