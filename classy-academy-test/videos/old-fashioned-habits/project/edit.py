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


def build():
    sc = []
    INTRO = S('H1') - 0.25
    # ================= INTRO: the channel's logo on black =================
    sc.append(Scene(0, INTRO, 'black', [UserLogo(0.0, INTRO + 0.3, width=470, fin=0.5, fout=0.0)], logo=False, name='intro'))
    # ================= HOOK =================
    t_h1b = S('H1b')
    hk = INTRO + (t_h1b - INTRO) / 2
    sc.append(Scene(INTRO, hk, None, [full(FH, M(1, 8.2), INTRO, hk, FB)], trans='dissolve', tdur=0.5, name='hook1'))
    sc.append(Scene(hk, t_h1b, None, [full(FH, M(1, 13.5), hk, t_h1b, FB)], trans='dissolve', name='hook2'))
    t_one, t_other = Wd('H1b', 'one'), Wd('H1b', 'other')
    sc.append(Scene(t_h1b, t_one - 0.1, None, [full(AR, M(5, 52), t_h1b, t_one, FB)], trans='dissolve', name='twowomen'))
    sc.append(Scene(t_one - 0.1, S('H2') - 0.2, 'caramel', [
        Clip(FH, M(12, 25.5), t_one - 0.1, S('H2'), PANEL2[0], appear='top', focus=(0.5, 0.5)),
        Clip(OE, M(3, 39.9), t_other - 0.1, S('H2'), PANEL2[1], appear='top', focus=(0.5, 0.3), hold=1.9)], trans='cut', name='twopanels'))
    t_happ = Wd('H2', 'everything')
    sc.append(Scene(S('H2') - 0.2, t_happ - 0.1, None, [full(HB, M(4, 1.2), S('H2') - 0.2, t_happ, FB)], trans='cut', name='redcoat'))
    sc.append(Scene(t_happ - 0.1, S('H3') - 0.1, None, [full(HW, M(1, 17), t_happ - 0.1, S('H3'), FB, hold=3.4)], trans='dissolve', name='ironclose'))
    t_cls = Wd('H3', 'classroom')
    sc.append(Scene(S('H3') - 0.1, E('H3') + 0.3, 'cream', [
        framed(HW, 6.0, S('H3') - 0.1, t_cls, appear='grow'),
        framed(HP, 6.5, t_cls, Wd('H3', 'exactly')),
        framed(HW, 45.8, Wd('H3', 'exactly'), E('H3') + 0.3, hold=4.1)], trans='dissolve', name='titlecards'))
    h1, h2, h3 = Wd('H4', 'how', 1), Wd('H4', 'how', 2), Wd('H4', 'how', 3)
    sc.append(Scene(E('H3') + 0.3, S('H5') - 0.1, 'caramel', [
        Clip(HW, M(1, 20.6), h1, S('H5'), PANEL3[0], appear='top', focus=(0.45, 0.5), speed=0.55),
        Clip(AR, M(5, 19.2), h2, S('H5'), PANEL3[1], appear='top', focus=(0.5, 0.6), hold=3.8),
        Clip(AR, M(4, 14.2), h3, S('H5'), PANEL3[2], appear='top', focus=(0.5, 0.5))], trans='dissolve', name='howto'))
    t_quiet = Wd('H5', 'quiet')
    sc.append(Scene(S('H5') - 0.1, t_quiet - 0.2, None, [full(GO, M(1, 14.6), S('H5') - 0.1, t_quiet, FB)], trans='dissolve', name='veil'))
    sc.append(Scene(t_quiet - 0.2, S('H6') - 0.1, None, [full(FH, M(12, 59.5), t_quiet - 0.2, S('H6'), FB)], trans='dissolve', name='rw_redcoat'))
    tt = S('H6') - 0.1; tm = Wd('H6', 'they'); te = E('H6') + 0.4
    title_layers = [full(FH, M(13, 33.5), tt, tm + 0.1, FB), full(FH, M(13, 5), tm, te, FB), Dim(0.22, tt, te)]
    T1 = Text('The Classy Elegance', 'serif', 46, WHITE, W / 2, 330, tt + 0.5, te, wdur=0.3, fout=0.4, shadow=True, fade_in=True)
    T2 = Text('7 Old-Fashioned Habits', 'script', 118, WHITE, W / 2, 400, tt + 0.8, te, wdur=0.7, fout=0.4, shadow=True)
    T3 = Text('That Make Any Outfit Look Expensive', 'script', 96, WHITE, W / 2, 545, tt + 1.4, te, wdur=0.8, fout=0.4, shadow=True, max_w=1600)
    sc.append(Scene(tt, te, None, title_layers + [T1, T2, T3], trans='dissolve', out_white=0.5, name='title'))

    # ================= 1. PRESS =================
    sc.append(card(1, 'They Press Before They Dress', te, E('A1') + 0.45))
    t0 = E('A1') + 0.45
    sc.append(split([L(HP, M(3, 1), t0, S('A3'), focus=(0.6, 0.5)), L(AR, M(1, 28.5), S('A3'), S('A4'), appear='fade', focus=(0.3, 0.5))], 'caramel',
                    [('A wrinkled shirt looks careless,', 'serif', 54, Wd('A2', 'careless') - 0.3),
                     ('a pressed one looks considered.', 'script', 84, Wd('A3', 'considered') - 0.3)], t0, S('A4') - 0.1, trans='cut'))
    ta = S('A4') - 0.1; tb = Wd('A4', 'a')
    sc.append(Scene(ta, tb, None, [full(HW, M(2, 20.4), ta, tb, FB, crop=(210, 230, 420, 250))], trans='dissolve', name='ironhands'))
    sc.append(Scene(tb, S('A4b') - 0.1, None, [full(AR, M(1, 22.2), tb, S('A4b'), FB, hold=4.8)], trans='dissolve', name='crisp'))
    tc = Wd('A4b', 'so')
    sc.append(Scene(S('A4b') - 0.1, S('A5') - 0.1, 'caramel', [
        Clip(AR, M(7, 18.2), S('A4b') - 0.1, S('A5'), PANEL2[0], appear='top'),
        Clip(AR, M(5, 9.2), tc, S('A5'), PANEL2[1], appear='top')], trans='dissolve', name='silkwool'))
    c1, c2, c3 = Wd('A5', 'collar'), Wd('A5', 'cuffs'), Wd('A5', 'front')
    sc.append(Scene(S('A5') - 0.1, c1 - 0.1, None, [full(HW, M(6, 20.2), S('A5') - 0.1, c1, FB)], trans='dissolve', name='busymorning'))
    sc.append(Scene(c1 - 0.1, S('A5b') - 0.1, 'caramel', [
        Clip(OE, M(1, 9.1), c1 - 0.1, S('A5b'), PANEL3[0], appear='top', focus=(0.5, 0.5)),
        Clip(AR, M(7, 35.0), c2 - 0.1, S('A5b'), PANEL3[1], appear='top', focus=(0.5, 0.5), hold=2.0),
        Clip(AR, M(1, 48.2), c3 - 0.1, S('A5b'), PANEL3[2], appear='top', focus=(0.5, 0.5), hold=1.7)], trans='cut', name='collarcuffs'))
    sc.append(Scene(S('A5b') - 0.1, S('A6') - 0.1, 'cream', [
        framed(HW, M(5, 47), S('A5b') - 0.1, Wd('A5b', 'so')),
        framed(HW, M(6, 26.5), Wd('A5b', 'so'), S('A6'), hold=3.4)], trans='dissolve', name='hangstraight'))
    tw = Wd('A6', 'than')
    sc.append(Scene(S('A6') - 0.1, tw, None, [full(FH, M(12, 41), S('A6') - 0.1, tw, FB)], trans='dissolve', name='whitecoat'))
    sc.append(Scene(tw, E('A6') + 0.45, None, [full(FH, M(12, 32), tw, E('A6') + 0.5, FB)], trans='dissolve', out_white=0.5, name='whitecoat2'))

    # ================= 2. HANG =================
    sc.append(card(2, 'They Hang It Up the Moment They Take It Off', E('A6') + 0.45, E('B1') + 0.45))
    t0 = E('B1') + 0.45; tm = Wd('B2', 'wake')
    sc.append(Scene(t0, tm, None, [full(HP, M(3, 54.6), t0, tm, FB, hold=3.6)], name='chairpile'))
    sc.append(Scene(tm, S('B3') - 0.1, None, [full(HP, M(3, 31), tm, S('B3'), FB)], trans='dissolve', name='messyroom'))
    sc.append(split([L(HP, M(2, 12), S('B3') - 0.1, S('B4'), focus=(0.55, 0.5)), L(HP, M(2, 0), S('B4'), S('B4b'), appear='fade', focus=(0.5, 0.5))], 'caramel',
                    [('Coats on a shaped hanger.', 'serif', 54, Wd('B3', 'jackets') - 0.2),
                     ('Knitwear, gently folded.', 'script', 84, Wd('B4', 'knitwear') - 0.2)], S('B3') - 0.1, S('B4b') - 0.1))
    tw = Wd('B4b', 'over')
    sc.append(Scene(S('B4b') - 0.1, tw, None, [full(HW, M(6, 11.8), S('B4b') - 0.1, tw, FB, hold=2.4)], trans='dissolve', name='blouses'))
    sc.append(Scene(tw, S('B5') - 0.1, None, [full(AR, M(3, 29.5), tw, S('B5'), FB)], trans='dissolve', name='shoulders'))
    sc.append(Scene(S('B5') - 0.1, S('B6') - 0.1, 'cream', [
        framed(HW, M(3, 13.5), S('B5') - 0.1, Wd('B5', 'before')),
        framed(HP, M(12, 6), Wd('B5', 'before'), S('B6'))], trans='dissolve', name='nightair'))
    sc.append(Scene(S('B6') - 0.1, E('B6') + 0.45, None, [full(HB, M(2, 32), S('B6') - 0.1, E('B6') + 0.5, FB)], trans='dissolve', out_white=0.5, name='park'))

    # ================= 3. MEND =================
    sc.append(card(3, 'They Mend Things Right Away', E('B6') + 0.45, E('C1') + 0.45))
    t0 = E('C1') + 0.45; b2, b3 = Wd('C2', 'hem'), Wd('C2', 'tear')
    sc.append(Scene(t0, S('C3') - 0.1, 'caramel', [
        Clip(HW, M(1, 44.1), t0, S('C3'), PANEL3[0], appear='top', focus=(0.5, 0.5), hold=1.7),
        Clip(AR, M(5, 25.2), b2 - 0.1, S('C3'), PANEL3[1], appear='top', focus=(0.5, 0.6)),
        Clip(FH, M(10, 30), b3 - 0.1, S('C3'), PANEL3[2], appear='top', focus=(0.5, 0.5))], trans='cut', name='button_hem'))
    sc.append(Scene(S('C3') - 0.1, S('C3b') - 0.1, None, [full(HB, M(5, 2.5), S('C3') - 0.1, S('C3b'), FB)], trans='dissolve', name='eyefinds'))
    sc.append(white_quote([('The fix takes less time', 'serif', 50, S('C3b')),
                           ('than choosing a different outfit.', 'script', 84, Wd('C3b', 'choosing') - 0.2)], S('C3b') - 0.1, S('C4') - 0.1))
    k1, k2, k3 = Wd('C5', 'black'), Wd('C5', 'white'), Wd('C5', 'beige')
    sc.append(Scene(S('C4') - 0.1, k1 - 0.1, 'cream', [
        framed(HW, M(2, 13.1), S('C4') - 0.1, Wd('C4', 'a'), hold=2.8),
        framed(HW, M(2, 15.9), Wd('C4', 'a'), k1, speed=0.48)], trans='dissolve', name='sewingbox'))
    sw = [(240, 200, 440, 620), (740, 200, 440, 620), (1240, 200, 440, 620)]
    sl = swatch(INK + 18, 'BLACK', sw[0], k1 - 0.1, S('C6')) + swatch(hx('F4F1EA'), 'WHITE', sw[1], k2 - 0.1, S('C6')) + \
         swatch(hx('D8C3A5'), 'BEIGE', sw[2], k3 - 0.1, S('C6'))
    sc.append(Scene(k1 - 0.1, S('C6') - 0.1, 'caramel', sl, trans='cut', name='threads'))
    tt = Wd('C6', 'tailor')
    sc.append(Scene(S('C6') - 0.1, tt, None, [full(HB, M(0, 35.2), S('C6') - 0.1, tt, FB)], trans='dissolve', name='fitting'))
    sc.append(Scene(tt, E('C6') + 0.45, None, [full(FH, M(12, 5), tt, E('C6') + 0.5, FB)], trans='dissolve', out_white=0.5, name='tailored'))

    # ================= 4. BRUSH =================
    sc.append(card(4, 'They Brush Their Coats', E('C6') + 0.45, E('D1') + 0.45))
    t0 = E('D1') + 0.45
    sc.append(Scene(t0, S('D3') - 0.1, None, [full(HB, M(4, 24.8), t0, S('D3'), FB)], name='darkcoat'))
    sc.append(Scene(S('D3') - 0.1, S('D3b') - 0.1, 'cream', [
        framed(SP, M(2, 24.2), S('D3') - 0.1, Wd('D3', 'lifts'), hold=4.3),
        framed(SP, M(2, 28.4), Wd('D3', 'lifts'), S('D3b'), crop=(40, 60, 440, 330), hold=3.0)], trans='dissolve', name='brush'))
    sc.append(split([L(FH, M(1, 11.0), S('D3b') - 0.1, Wd('D3b', 'neglected'), focus=(0.5, 0.5), hold=1.8),
                     L(HP, M(3, 16), Wd('D3b', 'neglected'), S('D4'), appear='fade', focus=(0.6, 0.5))], 'caramel',
                    [('A brushed coat', 'serif', 54, Wd('D3b', 'brushed') - 0.2),
                     ('looks deep and dark.', 'script', 88, Wd('D3b', 'deep') - 0.2)], S('D3b') - 0.1, S('D4') - 0.1))
    ta = Wd('D4', 'and')
    sc.append(Scene(S('D4') - 0.1, ta, None, [full(HW, M(9, 44.7), S('D4') - 0.1, ta, FB)], trans='dissolve', name='coatcloset'))
    sc.append(Scene(ta, S('D5') - 0.1, None, [full(HB, M(4, 11.9), ta, S('D5'), FB, hold=4.4)], trans='dissolve', name='richcoat'))
    tb = Wd('D5', 'but')
    sc.append(Scene(S('D5') - 0.1, tb, None, [full(HW, M(9, 53.4), S('D5') - 0.1, tb, FB)], trans='dissolve', name='hatgloves'))
    sc.append(Scene(tb, E('D5') + 0.45, None, [full(HW, M(10, 3.8), tb, E('D5') + 0.5, FB, hold=2.0)], trans='dissolve', out_white=0.5, name='doorface'))

    # ================= 5. SHOES =================
    sc.append(card(5, 'They Look After Their Shoes', E('D5') + 0.45, E('E1') + 0.45))
    t0 = E('E1') + 0.45
    sc.append(Scene(t0, S('E3') - 0.1, None, [full(SP, M(5, 54.6), t0, S('E3'), FB, speed=0.75)], name='shoesclose'))
    sc.append(Scene(S('E3') - 0.1, S('E4') - 0.1, 'cream', [framed(SP, M(2, 10.2), S('E3') - 0.1, S('E4'))], trans='dissolve', name='wipe'))
    sc.append(Scene(S('E4') - 0.1, S('E4b') - 0.1, 'caramel', [
        Clip(SS, M(1, 6.2), S('E4') - 0.1, S('E4b'), PANEL2[0], appear='top'),
        Clip(SS, M(2, 44.2), Wd('E4', 'dry') - 0.1, S('E4b'), PANEL2[1], appear='top')], trans='dissolve', name='shoetrees'))
    sc.append(Scene(S('E4b') - 0.1, S('E5') - 0.1, None, [full(SS, M(4, 37.9), S('E4b') - 0.1, S('E5'), FB)], trans='dissolve', name='rest'))
    tcb = Wd('E5', 'cobbler')
    sc.append(Scene(S('E5') - 0.1, tcb - 0.1, None, [full(SS, M(7, 38.3), S('E5') - 0.1, tcb, FB)], trans='dissolve', name='heel'))
    sc.append(Scene(tcb - 0.1, S('E6') - 0.1, None, [full(SS, M(4, 26.2), tcb - 0.1, S('E6'), FB)], trans='dissolve', name='cobbler'))
    sc.append(Scene(S('E6') - 0.1, E('E6') + 0.45, None, [full(FH, M(1, 16.6), S('E6') - 0.1, E('E6') + 0.5, FB, hold=3.8)], trans='dissolve', out_white=0.5, name='walkwhite'))

    # ================= 6. NIGHT BEFORE =================
    sc.append(card(6, 'They Prepare the Night Before', E('E6') + 0.45, E('F1') + 0.45))
    t0 = E('F1') + 0.45
    sc.append(Scene(t0, S('F3') - 0.1, None, [full(HW, M(3, 38.4), t0, S('F3'), FB, hold=3.5)], name='clock'))
    n2, n3 = Wd('F3', 'nails'), Wd('F3', 'hair')
    sc.append(Scene(S('F3') - 0.1, S('F4') - 0.1, 'caramel', [
        Clip(HP, M(11, 40), S('F3') - 0.1, S('F4'), PANEL3[0], appear='top', focus=(0.4, 0.5)),
        Clip(HW, M(2, 48.8), n2 - 0.1, S('F4'), PANEL3[1], appear='top', focus=(0.5, 0.5), hold=7.0),
        Clip(HW, M(2, 36.5), n3 - 0.1, S('F4'), PANEL3[2], appear='top', focus=(0.62, 0.5))], trans='dissolve', name='nightpanels'))
    sc.append(Scene(S('F4') - 0.1, S('F5') - 0.1, 'cream', [
        framed(HP, M(11, 48.6), S('F4') - 0.1, Wd('F4', 'check')),
        framed(HW, M(6, 1.5), Wd('F4', 'check'), S('F5'))], trans='dissolve', name='choose'))
    sc.append(split([L(HW, M(2, 58.6), S('F5') - 0.1, S('F5b'), focus=(0.75, 0.5))], 'caramel',
                    [('Your hair starts the morning', 'serif', 54, Wd('F5', 'starts') - 0.25),
                     ('with shape.', 'script', 96, Wd('F5', 'shape') - 0.2)], S('F5') - 0.1, S('F5b') - 0.1))
    tl = Wd('F5b', 'leaving')
    sc.append(Scene(S('F5b') - 0.1, tl, None, [full(HP, M(3, 40), S('F5b') - 0.1, tl, FB)], trans='dissolve', name='rush'))
    sc.append(Scene(tl, S('F6') - 0.1, None, [full(HP, M(12, 27), tl, S('F6'), FB)], trans='dissolve', name='calmnight'))
    sc.append(white_quote([('The morning becomes calm,', 'serif', 52, S('F6')),
                           ('every decision already made.', 'script', 86, Wd('F6', 'every') - 0.2)], S('F6') - 0.1, E('F6') + 0.45, trans='dissolve'))

    # ================= 7. LAST LOOK & STAND TALL =================
    sc.append(card(7, 'They Take One Last Look, and Stand Tall', E('F6') + 0.45, E('G1') + 0.45))
    t0 = E('G1') + 0.45
    sc.append(Scene(t0, S('G3') - 0.1, None, [full(HW, M(8, 43.5), t0, S('G3'), FB)], name='mirror'))
    g2, g3 = Wd('G3', 'lint'), Wd('G3', 'strap')
    sc.append(Scene(S('G3') - 0.1, S('G4') - 0.1, 'caramel', [
        Clip(HW, M(8, 20), S('G3') - 0.1, S('G4'), PANEL3[0], appear='top', focus=(0.45, 0.5)),
        Clip(AR, M(4, 1), g2 - 0.1, S('G4'), PANEL3[1], appear='top', focus=(0.5, 0.5)),
        Clip(HP, M(11, 12), g3 - 0.1, S('G4'), PANEL3[2], appear='top', focus=(0.5, 0.5))], trans='dissolve', name='checks'))
    sc.append(Scene(S('G4') - 0.1, S('G5') - 0.1, None, [full(GO, M(1, 2.0), S('G4') - 0.1, S('G5'), FB)], trans='dissolve', name='smile'))
    sc.append(Scene(S('G5') - 0.1, S('G6') - 0.1, 'cream', [framed(SP, 8.5, S('G5') - 0.1, S('G6'), hold=5.4)], trans='dissolve', name='speechtitle'))
    sc.append(Scene(S('G6') - 0.1, S('G7') - 0.1, None, [full(SP, M(4, 44.6), S('G6') - 0.1, S('G7'), FB, hold=9.2)], trans='cut', name='thinktall'))
    tu = Wd('G7', 'that')
    sc.append(Scene(S('G7') - 0.1, tu, None, [full(BC, M(1, 34), S('G7') - 0.1, tu, FB)], trans='dissolve', name='walkbook'))
    sc.append(Scene(tu, S('G7b') - 0.1, None, [full(HB, M(6, 7), tu, S('G7b'), FB)], trans='dissolve', name='walkyellow'))
    sc.append(split([L(DF, M(5, 8.5), S('G7b') - 0.1, E('G7b') + 0.6, focus=(0.5, 0.5))], 'caramel',
                    [('Good clothes look their best', 'serif', 54, S('G7b') + 0.1),
                     ('on a woman who carries them with ease.', 'script', 80, Wd('G7b', 'woman') - 0.2)], S('G7b') - 0.1, E('G7b') + 0.6))

    # ================= ENDING =================
    sc.append(Scene(E('G7b') + 0.6, S('Z2') - 0.1, None, [full(AR, M(8, 45), E('G7b') + 0.6, S('Z2'), FB)], trans='dissolve', name='group'))
    sc.append(white_quote([('It was never about having more.', 'serif', 50, S('Z2')),
                           ('It was about caring for what you already have.', 'script', 78, Wd('Z2', 'caring') - 0.6)], S('Z2') - 0.1, S('Z2b') - 0.1, trans='dissolve'))
    # spoken recap: one callback shot per habit (no on-screen list)
    rec = [('press', HW, M(1, 21.2)), ('hang', HP, M(12, 0.2)), ('mend', HW, M(2, 17.2)), ('brush', SP, M(2, 25.5)),
           ('care', SS, M(2, 46.5)), ('prepare', HW, M(3, 22.5)), ('one', SP, M(5, 42))]
    times = [S('Z2b') - 0.1] + [Wd('Z2b', w) - 0.1 for w, _, _ in rec[1:]] + [S('Z3') - 0.1]
    for i, (w, key, tin) in enumerate(rec):
        mode = FB
        sc.append(Scene(times[i], times[i + 1], None, [full(key, tin, times[i], times[i + 1], mode)], trans='dissolve' if i else 'cut', tdur=0.25, name=f'recap_{w}'))
    tz = Wd('Z3', 'every', 1)
    sc.append(Scene(S('Z3') - 0.1, tz - 0.1, None, [full(FH, M(13, 25.5), S('Z3') - 0.1, tz, FB)], trans='dissolve', name='care'))
    sc.append(Scene(tz - 0.1, S('Z4') - 0.1, None, [full(AR, M(7, 12.2), tz - 0.1, S('Z4'), FB)], trans='dissolve', name='rw_phone'))
    sc.append(Scene(S('Z4') - 0.1, S('Z5') - 0.1, None, [full(AR, M(6, 26), S('Z4') - 0.1, S('Z5'), FB)], trans='dissolve', name='comments'))
    sc.append(Scene(S('Z5') - 0.1, E('Z5') + 0.5, None, [full(AR, M(9, 14), S('Z5') - 0.1, E('Z5') + 0.5, FB)], trans='dissolve', name='welcome'))
    # ================= OUTRO: the channel's logo on black, held for the end screen =================
    sc.append(Scene(E('Z5') + 0.5, DUR, 'black', [UserLogo(E('Z5') + 0.5, DUR, width=470, fin=0.8, fout=0.8)],
                    logo=False, trans='dissolve', tdur=0.8, name='outro'))
    for a, b in zip(sc, sc[1:]):
        assert b.t0 > a.t0, (a.name, b.name)
        a.t1 = b.t0
    return sc

if __name__ == '__main__':
    sc = build()
    for s in sc: print(f'{s.t0:7.2f}-{s.t1:7.2f} {s.t1-s.t0:5.2f} {s.name}')
    print(len(sc), 'scenes; duration', DUR)
