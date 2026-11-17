# ffr.py - fast renderer for the video page: same index.html, same timeline, drawn with numpy/OpenCV + FFmpeg
# instead of a browser screenshot per frame. Text/graphics are captured once from Chrome (ffr_capture.js), so fonts match.
# Speed here: ~4.3 min per minute of video (the browser renderer: ~11). Checked frame by frame against the browser.
# usage (inside the work folder, after build.py):
#   node $T/ffr_capture.js $PWD $PWD $PWD/ff/sprites                 # once per build: text + graphics as PNG sprites
#   python3 $T/ffr_cmp.py                                             # vs browser snapshots in snapcmp/: every diff < 10
#   python3 $T/ffr.py . 0 <duration> out/<slug>_v1.mp4 4              # <project> <t0> <t1> <out.mp4> [workers]
# env: FFR_PRESET (default veryfast), FFR_CRF (default 16).
import sys, os, re, json, math, subprocess
from html.parser import HTMLParser
import numpy as np, cv2

P, T0, T1, OUT = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
WORKERS = int(sys.argv[5]) if len(sys.argv) > 5 else 4
FPS, W, H = 30, 1920, 1080
SP = os.path.join(P, 'ff', 'sprites')
html = open(os.path.join(P, 'index.html'), encoding='utf-8').read()

# ---------------- parse the stage ----------------
class Node:
    def __init__(s, tag, a, parent):
        s.tag, s.a, s.parent, s.kids = tag, a, parent, []
        s.id = a.get('id'); s.cls = (a.get('class') or '').split(); s.style = {}
        for kv in (a.get('style') or '').split(';'):
            if ':' in kv: k, v = kv.split(':', 1); s.style[k.strip()] = v.strip()
class Parse(HTMLParser):
    def __init__(s):
        super().__init__(); s.root = Node('root', {}, None); s.cur = s.root
    def handle_starttag(s, tag, attrs):
        n = Node(tag, dict(attrs), s.cur); s.cur.kids.append(n)
        if tag not in ('img', 'source', 'br', 'path', 'meta', 'link'): s.cur = n
    def handle_endtag(s, tag):
        if tag in ('img', 'source', 'br', 'path'): return
        if s.cur.parent: s.cur = s.cur.parent
body = html[html.index('<div id="root"'):html.index('<script>\nconst tl')]
pp = Parse(); pp.feed(body); ROOT = pp.root.kids[0]
px = lambda v: float(str(v).replace('px', '')) if v not in (None, '') else 0.0

# ---------------- parse the timeline ----------------
def jsobj(s):
    s = re.sub(r'([{,])\s*"?([A-Za-z_\-][\w\-]*)"?\s*:', r'\1"\2":', s)
    return json.loads(s)
TW = {}   # id -> prop -> [tween]
for m in re.finditer(r'tl\.(fromTo|to|set)\("#([\w]+)",(\{[^}]*\})(?:,(\{[^}]*\}))?,([\d.]+)\);', html):
    kind, id_, a, b, t = m.group(1), m.group(2), jsobj(m.group(3)), m.group(4), float(m.group(5))
    b = jsobj(b) if b else None
    if kind == 'fromTo': frm, to = a, b
    elif kind == 'to': frm, to = None, a
    else: frm, to = None, dict(a, duration=0)
    d = float(to.get('duration', 0)); ease = to.get('ease', 'power1.out'); org = to.get('transformOrigin')
    for k, v in to.items():
        if k in ('duration', 'ease', 'transformOrigin'): continue
        TW.setdefault(id_, {}).setdefault(k, []).append(dict(t=t, d=d, ease=ease, frm=None if frm is None else frm.get(k), to=v, org=org))
DUR = float(re.search(r'data-duration="([\d.]+)"', html).group(1))
for k, v in [('bg', None)]:
    pass
m = re.search(r'tl\.fromTo\("#bg",\s*\{\s*x:\s*(-?[\d.]+),\s*y:\s*(-?[\d.]+),\s*rotation:\s*0\s*\},\s*\{\s*x:\s*(-?[\d.]+),\s*y:\s*(-?[\d.]+),\s*rotation:\s*([\d.]+)', html)
BGT = tuple(float(x) for x in m.groups())
TW.setdefault('black', {})['opacity'] = [dict(t=0, d=1.0, ease='none', frm=1, to=0, org=None)]
for ts in TW.values():
    for lst in ts.values(): lst.sort(key=lambda z: z['t'])

def ease(name, x):
    x = min(1.0, max(0.0, x))
    if name in ('none', 'linear'): return x
    if name == 'sine.inOut': return -(math.cos(math.pi * x) - 1) / 2
    if name.startswith('power'):
        p = {'power1': 2, 'power2': 3, 'power3': 4, 'power4': 5}[name.split('.')[0]]
        if name.endswith('.out'): return 1 - (1 - x) ** p
        if name.endswith('.in'): return x ** p
        return (2 ** (p - 1)) * x ** p if x < 0.5 else 1 - (-2 * x + 2) ** p / 2
    if name == 'expo.out': return 1.0 if x >= 1 else 1 - 2 ** (-10 * x)
    return x
def val(id_, prop, t, default):
    lst = TW.get(id_, {}).get(prop)
    if not lst: return default
    started = [z for z in lst if z['t'] <= t + 1e-9]
    if not started:
        f = lst[0]; return f['frm'] if f['frm'] is not None else default
    z = started[-1]
    if z['frm'] is not None: a = z['frm']
    else:
        prev = [y for y in lst if y['t'] < z['t'] - 1e-9]
        a = val(id_, prop, z['t'] - 1e-6, default) if prev else default
    if z['d'] <= 0: return z['to']
    return a + (z['to'] - a) * ease(z['ease'], (t - z['t']) / z['d'])
def origin(id_):
    for lst in TW.get(id_, {}).values():
        for z in lst:
            if z['org']: return z['org']
    return '50% 50%'

# ---------------- colour: CSS filter matrices (sRGB) ----------------
def m_contrast(c): return np.array([[c, 0, 0, (0.5 - 0.5 * c)], [0, c, 0, (0.5 - 0.5 * c)], [0, 0, c, (0.5 - 0.5 * c)]])
def m_sat(s): return np.array([[0.213 + 0.787 * s, 0.715 - 0.715 * s, 0.072 - 0.072 * s, 0], [0.213 - 0.213 * s, 0.715 + 0.285 * s, 0.072 - 0.072 * s, 0], [0.213 - 0.213 * s, 0.715 - 0.715 * s, 0.072 + 0.928 * s, 0]])
def m_sepia(a): return np.array([[0.393 + 0.607 * (1 - a), 0.769 - 0.769 * (1 - a), 0.189 - 0.189 * (1 - a), 0], [0.349 - 0.349 * (1 - a), 0.686 + 0.314 * (1 - a), 0.168 - 0.168 * (1 - a), 0], [0.272 - 0.272 * (1 - a), 0.534 - 0.534 * (1 - a), 0.131 + 0.869 * (1 - a), 0]])
def m_bright(b): return np.array([[b, 0, 0, 0], [0, b, 0, 0], [0, 0, b, 0]])
def chain(*ms):
    R = np.eye(4)
    for mm in ms: R = np.vstack([mm, [0, 0, 0, 1]]) @ R
    R = R[:3].copy(); R[:, 3] *= 255; return R.astype(np.float32)
def bgr(M):
    Pm = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], np.float32)
    out = np.zeros((3, 4), np.float32); out[:, :3] = Pm @ M[:, :3] @ Pm; out[:, 3] = Pm @ M[:, 3]; return out
GRADE = bgr(chain(m_contrast(1.03), m_sat(0.95), m_sepia(0.05)))
CANVASBG = bgr(chain(m_bright(0.82), m_sat(0.9)))

# ---------------- media ----------------
class Clip:
    """Sequential frame reader for a prepared 720x1280 clip, frame index = floor((t-start)*fps)."""
    def __init__(s, f, start):
        s.f, s.start = os.path.join(P, f), start; s.p = None; s.idx = -1; s.frame = None; s.done = False; s.last = start
        pr = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', s.f], capture_output=True, text=True).stdout.split(',')
        s.w, s.h = int(pr[0]), int(pr[1])
    def get(s, t):
        k = max(0, int(math.floor((t - s.start) * FPS + 1e-6))); s.last = t
        if s.p is None:
            s.p = subprocess.Popen(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{k / FPS:.4f}', '-i', s.f, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
            s.idx = k - 1
        while s.idx < k and not s.done:
            b = s.p.stdout.read(s.w * s.h * 3)
            if len(b) < s.w * s.h * 3: s.done = True; break
            s.frame = np.frombuffer(b, np.uint8).reshape(s.h, s.w, 3); s.idx += 1
        return s.frame
    def close(s):
        if s.p: s.p.kill(); s.p = None

def load_sprite(key):
    im = cv2.imread(os.path.join(SP, key + '.png'), cv2.IMREAD_UNCHANGED)
    if im.shape[2] == 3: im = np.dstack([im, np.full(im.shape[:2], 255, np.uint8)])
    rgb = im[..., :3].astype(np.float32); a = im[..., 3:4].astype(np.float32) / 255
    return rgb * a, a          # premultiplied
SPR = json.load(open(os.path.join(SP, 'sprites.json')))

# ---------------- build layers ----------------
TEXTZ = {'card': 49, 'hint': 45, 'q1': 45, 'q2': 45, 'qr1': 45, 'qr2': 45, 'qs1': 45, 'qs2': 45, 'gtx1': 45, 'gtx2': 45, 'rcp': 45,
         'title': 45, 'cl': 46, 'hd': 46, 'chk': 46, 'logo': 47, 'endlogo': 62, 'ann': 46, 'alab': 46, 'kick': 46}
layers = []   # (z, order, layer)
def vwin(v): return float(v.a.get('data-start')), float(v.a.get('data-start')) + float(v.a.get('data-duration'))
for order, n in enumerate(ROOT.kids):
    c = n.cls
    if n.id == 'bg': layers.append((0, order, dict(kind='bg'))); continue
    if 'w' in c:
        x0, y0, w, h = px(n.style.get('left')), px(n.style.get('top')), px(n.style.get('width')), px(n.style.get('height'))
        canv = [k for k in n.kids if 'canvas' in k.cls]
        if canv:
            bgv = canv[0].kids[0]; fgw = [k for k in n.kids if 'w' in k.cls][0]; fgv = fgw.kids[0]
            layers.append((0, order, dict(kind='canvas', id=n.id, bg=bgv.a['src'], fg=fgv.a['src'], fgid=fgv.id, win=vwin(fgv),
                                          fx=px(fgw.style.get('left')), fw=px(fgw.style.get('width')))))
        else:
            vids = [k for k in n.kids if k.tag == 'video']
            layers.append((0, order, dict(kind='box', id=n.id, x=x0, y=y0, w=w, h=h,
                                          vids=[dict(id=v.id, src=v.a['src'], win=vwin(v), grade='filter' in (v.a.get('style') or '')) for v in vids])))
        continue
    if 'white' in c or 'endwhite' in c: layers.append((48 if 'white' in c else 61, order, dict(kind='fill', id=n.id, col=(255, 255, 255), a=1.0))); continue
    if 'haze' in c: layers.append((44, order, dict(kind='fill', id=n.id, col=(228, 238, 248), a=0.42))); continue      # rgba(248,238,228,.42) in BGR
    if 'black' in c: layers.append((60, order, dict(kind='fill', id='black', col=(0, 0, 0), a=1.0))); continue
    z = next((TEXTZ[k] for k in c if k in TEXTZ), None)
    if z is not None and n.id:
        if 'chk' in c: layers.append((z, order, dict(kind='chk', id=n.id, pid=next((k.id for k in (n.kids[0].kids if n.kids else []) if k.tag == 'path' and k.id), None))))
        else: layers.append((z, order, dict(kind='sprite', id=n.id, masked=SPR.get(n.id + '_all', {}).get('masked', False),
                                            init_op=0.92 if 'logo' in c else (float(n.style.get('opacity', 1)) if 'opacity' in n.style else 1.0))))
layers.sort(key=lambda z: (z[0], z[1])); LAYERS = [l for _, _, l in layers]
CACHE = {}
def sprite(key):
    if key not in CACHE: CACHE[key] = load_sprite(key)
    return CACHE[key]

# ---------------- drawing helpers (float32 premultiplied BGR canvas) ----------------
def affine(scale, ox, oy, tx, ty):
    # x' = ox + (x-ox)*s + tx
    return np.array([[scale, 0, ox - ox * scale + tx], [0, scale, oy - oy * scale + ty]], np.float32)
def comp(dst, rgb, a, M, op):
    """Composite premultiplied (rgb, a) through affine M (src->dst) with opacity op."""
    if op <= 0.002: return
    if M is None and rgb.shape[:2] == dst.shape[:2]:
        dst *= (1 - a * op); dst += rgb * op; return
    hs, ws = rgb.shape[:2]
    corners = np.array([[0, 0, 1], [ws, 0, 1], [0, hs, 1], [ws, hs, 1]], np.float32) @ M.T
    x0, y0 = max(0, int(math.floor(corners[:, 0].min()))), max(0, int(math.floor(corners[:, 1].min())))
    x1, y1 = min(W, int(math.ceil(corners[:, 0].max()))), min(H, int(math.ceil(corners[:, 1].max())))
    if x1 <= x0 or y1 <= y0: return
    M2 = M.copy(); M2[0, 2] -= x0; M2[1, 2] -= y0
    integer = abs(M[0, 0] - 1) < 1e-6 and abs(M[1, 1] - 1) < 1e-6 and abs(M[0, 2] - round(M[0, 2])) < 1e-6 and abs(M[1, 2] - round(M[1, 2])) < 1e-6
    if integer:
        sx, sy = int(round(x0 - M[0, 2])), int(round(y0 - M[1, 2]))
        r = rgb[sy:sy + (y1 - y0), sx:sx + (x1 - x0)]; aa = a[sy:sy + (y1 - y0), sx:sx + (x1 - x0)]
    else:
        r = cv2.warpAffine(rgb, M2, (x1 - x0, y1 - y0), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        aa = cv2.warpAffine(a, M2, (x1 - x0, y1 - y0), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        if aa.ndim == 2: aa = aa[..., None]
    reg = dst[y0:y1, x0:x1]
    reg *= (1 - aa * op); reg += r * op
def cover(frame, w, h, drift, grade):
    """object-fit: cover of a source frame into w x h, then CSS scale(drift) about the centre, clipped to the box."""
    fh, fw = frame.shape[:2]; s = max(w / fw, h / fh) * drift
    M = np.array([[s, 0, w / 2 - fw * s / 2], [0, s, h / 2 - fh * s / 2]], np.float32)
    out = cv2.warpAffine(frame, M, (int(round(w)), int(round(h))), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    if grade is not None: out = cv2.transform(out, grade)
    return out.astype(np.float32)
ONES = {}
def ones(h, w):
    if (h, w) not in ONES: ONES[(h, w)] = np.ones((h, w, 1), np.float32)
    return ONES[(h, w)]
def wipe_alpha(w, p):
    """mask: linear-gradient(90deg,#000 45%,transparent 55%), mask-size 220%, mask-position p% (p: 100 hidden -> 0 shown)."""
    x = np.arange(w, dtype=np.float32) + 0.5; mw = 2.2 * w; off = (w - mw) * p / 100.0
    mx = x - off
    a = np.clip((0.55 * mw - mx) / (0.10 * mw), 0, 1)
    return a[None, :, None]

BG = None
ROOTC = np.array([98, 141, 195], np.float32)       # #c38d62 (BGR)
def draw_bg(dst, t):
    global BG
    m = SPR['bg_all']
    if BG is None:
        rgb, a = sprite('bg_all'); BG = rgb + ROOTC * (1 - a)
    k = ease('sine.inOut', t / DUR)
    tx, ty, rot = BGT[0] + (BGT[2] - BGT[0]) * k, BGT[1] + (BGT[3] - BGT[1]) * k, BGT[4] * k
    cx, cy = m['bx'] + m['bw'] / 2, m['by'] + m['bh'] / 2
    R = cv2.getRotationMatrix2D((cx - m['x'], cy - m['y']), -rot, 1.0).astype(np.float32)
    R[0, 2] += m['x'] + tx; R[1, 2] += m['y'] + ty
    cv2.warpAffine(BG, R, (W, H), dst=dst, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=tuple(float(x) for x in ROOTC))

CLIPS = {}
def clip(src, start):
    if src not in CLIPS: CLIPS[src] = Clip(src, start)
    return CLIPS[src]
BLURBG = {}
def canvas_bg(src, frame, t):
    # .canvas inset:-60px -> 2040x1200 at (-60,-60); object-fit cover; blur(38px) brightness(.82) saturate(.9)
    key = (src, id(frame))
    if key in BLURBG: return BLURBG[key]
    q = 4; w, h = 2040 // q, 1200 // q; pad = 48
    fh, fw = frame.shape[:2]; s = max(w / fw, h / fh)
    small = cv2.resize(frame, (int(round(fw * s)), int(round(fh * s))), interpolation=cv2.INTER_AREA)
    yy, xx = (small.shape[0] - h) // 2, (small.shape[1] - w) // 2; small = cv2.transform(small[yy:yy + h, xx:xx + w], CANVASBG)
    big = np.zeros((h + 2 * pad, w + 2 * pad, 4), np.float32)
    big[pad:pad + h, pad:pad + w, :3] = small; big[pad:pad + h, pad:pad + w, 3] = 1
    big = cv2.GaussianBlur(big, (0, 0), 38 / q)
    M = np.array([[q, 0, -(pad * q + 60) + (q - 1) / 2], [0, q, -(pad * q + 60) + (q - 1) / 2]], np.float32)   # region starts at (-60,-60): .canvas inset -60px
    up = cv2.warpAffine(big, M, (W, H), flags=cv2.INTER_LINEAR)
    res = (up[..., :3], up[..., 3:4]); BLURBG.clear(); BLURBG[key] = res
    return res

def render(t):
    dst = np.empty((H, W, 3), np.float32); draw_bg(dst, t)
    for L in LAYERS:
        k = L['kind']
        if k == 'box':
            op = val(L['id'], 'opacity', t, 0.0)
            if op <= 0.002: continue
            w, h = int(round(L['w'])), int(round(L['h'])); content = np.zeros((h, w, 3), np.float32); ca = np.zeros((h, w, 1), np.float32)
            for v in L['vids']:
                a0, a1 = v['win']
                if not (a0 - 1e-6 <= t < a1): continue
                vo = val(v['id'], 'opacity', t, 1.0)
                if vo <= 0.002: continue
                fr = clip(v['src'], a0).get(t)
                if fr is None: continue
                img = cover(fr, w, h, val(v['id'], 'scale', t, 1.0), GRADE if v['grade'] else None)
                content *= (1 - vo); content += img * vo; ca *= (1 - vo); ca += vo
            s = val(L['id'], 'scale', t, 1.0); ty = val(L['id'], 'y', t, 0.0)
            ox, oy = [float(z.strip('%')) / 100 for z in origin(L['id']).split()]
            M = affine(s, L['x'] + w * ox, L['y'] + h * oy, 0, ty); M[0, 2] += L['x'] * s; M[1, 2] += L['y'] * s
            # affine() maps local box coords about the origin; build explicitly instead:
            M = np.array([[s, 0, L['x'] + w * ox - w * ox * s], [0, s, L['y'] + h * oy - h * oy * s + ty]], np.float32)
            comp(dst, content, ca, M, op)
        elif k == 'canvas':
            op = val(L['id'], 'opacity', t, 0.0)
            if op <= 0.002: continue
            a0, a1 = L['win']
            if not (a0 - 1e-6 <= t < a1): continue
            fr = clip(L['fg'], a0).get(t)
            if fr is None: continue
            brgb, ba = canvas_bg(L['bg'], fr, t)
            layer = brgb.copy(); la = ba.copy()
            fw = int(round(L['fw'])); fx = int(round(L['fx']))
            fg = cover(fr, fw, H, val(L['fgid'], 'scale', t, 1.0), GRADE)
            layer[:, fx:fx + fw] = fg; la[:, fx:fx + fw] = 1
            comp(dst, layer, la, None, op)
        elif k == 'fill':
            op = val(L['id'], 'opacity', t, 0.0 if L['id'] != 'black' else 1.0) * L['a']
            if op <= 0.002: continue
            dst *= (1 - op); dst += np.array(L['col'], np.float32) * op
        elif k == 'sprite':
            op = val(L['id'], 'opacity', t, L['init_op'])
            if op <= 0.002: continue
            key = L['id'] + '_all'; m = SPR[key]; rgb, a = sprite(key)
            if L['masked']:
                p = val(L['id'], '--p', t, 100.0)
                wa = wipe_alpha(int(m['w']), p); rgb = rgb * wa; a = a * wa
            s = val(L['id'], 'scale', t, 1.0); ty = val(L['id'], 'y', t, 0.0); tx = val(L['id'], 'x', t, 0.0)
            cx, cy = m['bx'] + m['bw'] / 2, m['by'] + m['bh'] / 2
            M = np.array([[s, 0, cx + (m['x'] - cx) * s + tx], [0, s, cy + (m['y'] - cy) * s + ty]], np.float32)
            comp(dst, rgb, a, M, op)
        elif k == 'chk':
            op = val(L['id'], 'opacity', t, 0.0)
            if op <= 0.002: continue
            tx = val(L['id'], 'x', t, 0.0)
            for part in ('text', 'mark'):
                key = f"{L['id']}_{part}"; m = SPR[key]; rgb, a = sprite(key)
                po = 1.0
                if part == 'mark' and L['pid']:
                    po = 1 - val(L['pid'], 'strokeDashoffset', t, 80.0) / 80.0
                M = np.array([[1, 0, m['x'] + tx], [0, 1, m['y']]], np.float32)
                comp(dst, rgb, a, M, op * max(0.0, min(1.0, po)))
    return dst

# ---------------- run: split the range across workers, encode, concat, add audio ----------------
def run_part(i, a, b, path):
    enc = subprocess.Popen(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-preset', os.environ.get('FFR_PRESET', 'veryfast'), '-crf', os.environ.get('FFR_CRF', '16'), '-pix_fmt', 'yuv420p', '-g', '60', path], stdin=subprocess.PIPE)
    k0, k1 = int(round(a * FPS)), int(round(b * FPS))
    for k in range(k0, k1):
        f = render(k / FPS)
        enc.stdin.write(cv2.convertScaleAbs(f).tobytes())
        for src in list(CLIPS):                      # free decoders of clips that left the screen (memory)
            if k / FPS - CLIPS[src].last > 1.0: CLIPS.pop(src).close()
    enc.stdin.close(); enc.wait()
    for c in CLIPS.values(): c.close()
if __name__ == '__main__':
    import time
    tm = time.time()
    if WORKERS <= 1:
        run_part(0, T0, T1, OUT)
    else:
        bounds = [T0 + (T1 - T0) * i / WORKERS for i in range(WORKERS + 1)]
        bounds = [round(x * FPS) / FPS for x in bounds]
        procs, parts = [], []
        for i in range(WORKERS):
            pth = f'{OUT}.part{i}.mp4'; parts.append(pth)
            pid = os.fork()
            if pid == 0:
                run_part(i, bounds[i], bounds[i + 1], pth); os._exit(0)
            procs.append(pid)
        for pid in procs:
            _, st = os.waitpid(pid, 0)
            assert st == 0, f'render worker {pid} failed (status {st}) - out of memory? use fewer workers'
        for i, pth in enumerate(parts):              # every part must hold exactly its frames
            n = int(subprocess.run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets',
                                    '-of', 'csv=p=0', pth], capture_output=True, text=True).stdout.strip() or 0)
            want = int(round(bounds[i + 1] * FPS)) - int(round(bounds[i] * FPS))
            assert n == want, f'part {i} has {n} frames, expected {want}'
        lst = OUT + '.txt'; open(lst, 'w').write(''.join(f"file '{os.path.abspath(p)}'\n" for p in parts))
        subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', OUT + '.v.mp4'], check=True)
        audio = os.path.join(P, 'assets', 'mix.wav')
        subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', OUT + '.v.mp4', '-ss', f'{T0}', '-t', f'{T1 - T0}', '-i', audio,
                        '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ac', '2', '-shortest', OUT], check=True)
        for p in parts + [lst, OUT + '.v.mp4']: os.remove(p)
    print(f'rendered {T1 - T0:.1f}s in {time.time() - tm:.1f}s')
