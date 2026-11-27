# edit.py - the edit: every scene timed to the voice (beats.json / words.json)
import json, re, os, sys, difflib
sys.path.insert(0, os.path.dirname(__file__))
from scenes import *

ROOTD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = {b['k']: b for b in json.load(open(ROOTD + '/beats.json'))['beats']}
DUR = json.load(open(ROOTD + '/beats.json'))['duration']
WORDS = json.load(open(ROOTD + '/words.json'))
def S(k): return B[k]['s']
def E(k): return B[k]['e']
def Wd(k, word, n=1):
    """time a word starts inside beat k (n-th occurrence)"""
    c = 0
    for w in WORDS:
        ww = re.sub(r'[^a-z]', '', w['w'].lower())
        if S(k) - 0.35 <= w['s'] <= E(k) + 0.2 and (ww == word or (len(word) > 4 and difflib.SequenceMatcher(None, ww, word).ratio() > 0.78)):
            c += 1
            if c == n: return w['s']
    raise KeyError(f'{word} not in {k}')

M = lambda m, s=0: m * 60 + s  # source timecode helper

# ---------------- layout helpers ----------------
FULL = None
def full(key, tin, t0, t1, mode='cover', focus=(0.5, 0.5), crop=None, appear='none', **kw):
    return Clip(key, tin, t0, t1, None, mode, crop, appear, focus=focus, **kw)

PANEL3 = [(140, 110, 520, 860), (700, 110, 520, 860), (1260, 110, 520, 860)]
PANEL2 = [(250, 110, 690, 860), (980, 110, 690, 860)]

def card(n, title, t0, t1):
    """White number card; black script writes on left to right (~1.2 s), fades out 0.4 s."""
    txt = f'{n}. {title}'
    T = Text(txt, 'script', 112, INK, W / 2, 0, t0 + 0.30, t1, wdur=1.25, fout=0.4, max_w=1500)
    w, h = T.size(); T.top = H / 2 - h / 2 - 8
    return Scene(t0, t1, 'white', [T], logo=False, trans='cut', name=f'card{n}')

def quote_lines(lines, cx, ytop, col, gap=18, wdur=0.55, t1=None):
    """lines: [(text, kind, size, t_in)] stacked, centred on cx"""
    out = []; y = ytop
    for txt, kind, size, tin in lines:
        T = Text(txt, kind, size, col, cx, y, tin, t1, wdur=wdur, fout=0.0, max_w=1050)
        out.append(T); y += T.size()[1] * (0.62 if kind == 'serif' else 0.7) + gap
    tot = y - ytop
    return out, tot

def centred_quote(lines, cx, cy, col, t1):
    tmp, tot = quote_lines(lines, cx, 0, col, t1=t1)
    Ls, _ = quote_lines(lines, cx, cy - tot / 2 - 20, col, t1=t1)
    return Ls

def split(clips, side_bg, lines, t0, t1, trans='dissolve', out_white=0.0, name='split'):
    """Clip on the left third, caramel (or white) on the right two-thirds with the principle line."""
    layers = list(clips)
    col = WHITE if side_bg == 'caramel' else INK
    layers += centred_quote(lines, 640 + 640, H / 2, col, t1)
    return Scene(t0, t1, side_bg, layers, logo=True, trans=trans, out_white=out_white, name=name)

def L(key, tin, t0, t1, i=0, n=1, appear='none', focus=(0.5, 0.5), crop=None, **kw):
    """left-third clip"""
    return Clip(key, tin, t0, t1, (0, 0, 640, 1080), 'cover', crop, appear, focus=focus, **kw)

def framed(key, tin, t0, t1, ratio=4 / 3, appear='none', crop=None, focus=(0.5, 0.5), h=780, **kw):
    w = int(h * ratio); return Clip(key, tin, t0, t1, ((W - w) // 2, (H - h) // 2 + 10, w, h), 'cover', crop, appear, focus=focus, **kw)

def white_quote(lines, t0, t1, trans='cut', out_white=0.0):
    Ls = centred_quote(lines, W / 2, H / 2, INK, t1)
    return Scene(t0, t1, 'white', Ls, logo=False, trans=trans, out_white=out_white, name='wquote')

def swatch(col, label, box, t0, t1):
    x, y, w, h = box
    tex = np.empty((h, w, 3), np.float32); tex[:] = col
    tex += np.random.default_rng(int(col.sum())).normal(0, 3.0, (h, w, 1)).astype(np.float32)
    lab_col = INK if col.mean() > 150 else WHITE
    R = Rect(tex, box, t0, t1, appear='none')
    T = Text(label, 'caps', 46, lab_col, x + w / 2, y + h / 2 - 40, t0 + 0.15, t1, wdur=0.6, fout=0, tracking=9)
    return [R, T]

CH, AR, HW, HP, SP, BC, SS, RW, OE, CN = ('charade_fhd', 'Aristocr1940', 'HowtoBeW1949', 'HabitPat1954', 'SpeechPl1949',
                                          'BodyCare1948', 'story_of_shoes_2', 'royal-wedding-1951', 'OfficeEt1950', 'Careofth1951')
FB = 'fitblur'
FH, HB, GO, DF = 'FashionH1940', 'HarpersBazaa', 'Girlonth1940', 'Designfo1956'

