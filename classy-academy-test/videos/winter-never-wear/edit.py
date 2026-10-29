# 8 Things Elegant Ladies Never Wear in Winter - v5 edit, copied from the owner's own videos (workflow/EDIT-RULES.md).
# Geometry measured on "7 Things Elegant Ladies Avoid in Fall" (study sheets Loui0mjLavo_03/05) and "8 Things Elegant
# Ladies Never Wear":
#   ROW    the caramel backdrop with 2-4 tall reels side by side, each a whole 9:16 reel at full height (608 px wide, never
#          cropped or zoomed), growing in on its own word and holding for the sentence; slots may fill in any order
#   FRAMED 2-3 smaller reels with caramel gaps between them (her "but now the outfit feels elevated" screens)
#   ONE    one reel centred on caramel, growing from the centre; the pictures may change inside it
#   CREAM1 one reel centred on the cream screen (her "It doesn't shout. It whispers expensive.")
#   CUTS   product cut-outs on caramel, tall, one per spoken word, with a small serif label
#   QUOTE  a reel on the left, the principle on the right in white serif with one word in script
#   FS     full screen: landscape footage ONLY (Charade, 1963; landscape stock); a vertical reel is never blown up
#   CARD   the white number card, black script wiping in; GUIDE the guide plug over a landscape close-up
# Every line's picture is in VISUAL-SCRIPT.md (written before sourcing); every segment was checked on its strip (ok5.txt).
import re as _re
SB = []
def _log(kind, specs, t0, t1, move):
    SB.append(dict(kind=kind, clips=[[s[0], s[1], s[2]] for s in specs], t0=round(t0, 2), t1=round(t1, 2), move=move))
def _plain(s): return _re.sub(r'<[^>]+>', ' ', s).replace('  ', ' ').strip()
SEQ = []
def add(t, kind, fn): SEQ.append((t, kind, fn))
def flush(t_last):
    """each layout lasts until the next one starts; a short overlap gives her soft dissolves"""
    SEQ.sort(key=lambda s: s[0]); pk = None
    for k, (t, kind, fn) in enumerate(SEQ):
        if k + 1 < len(SEQ):
            nt, nk, _ = SEQ[k + 1]
            assert nt > t + 0.6, f'{kind} at {t:.2f} followed too soon by {nk} at {nt:.2f}'
            t1 = nt + (0.45 if nk in ('fs', 'card', 'cream') else 0.3)
        else: t1 = t_last
        fn(t, t1, pk); pk = kind

RW = 608                                    # a whole 9:16 reel at full height
def _pnl(spec, x0, y0, x1, y1, t0, t1, entry, origin='50% 50%', z=''):
    v, h = vid(spec, t0, t1 + 0.55); drift(v, t0, t1 + 0.55, 1.04)
    i = box(x0, y0, x1, y1, h, z)
    if entry == 'corner': grow_corner(i, t0, origin)
    elif entry == 'centre': grow_centre(i, t0)
    else: fade_in(i, t0, 0.6)
    fade_out(i, t1, 0.55); return i
def _lab(txt, cx, y, t0, t1, z=''):
    i = nid('lb'); els.append(f'<div id="{i}" class="cl" style="left:{cx-300}px;top:{y}px;width:600px;opacity:0;font-family:Playfair;font-size:40px;'
                              f'text-shadow:0 2px 14px rgba(40,25,15,.55);{z}">{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:12}},{{opacity:1,y:0,duration:0.7,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.45)

def ROW(specs, times, slots=None, labels=None):
    """2-4 tall reels on caramel, one per spoken item; slots = which position each one takes (default left to right)"""
    n = max(len(specs), (max(slots) + 1) if slots else 0); slots = slots or list(range(len(specs)))
    w = RW if n <= 3 else W // n; x0 = (W - n * w) // 2
    def fn(t0, t1, pk):
        for k, (s, tt, sl) in enumerate(zip(specs, times, slots)):
            org = '0% 50%' if sl == 0 else ('100% 50%' if sl == n - 1 else '50% 50%')
            _pnl(s, x0 + sl * w, 0, x0 + (sl + 1) * w, H, tt, t1, 'corner', org)
            if labels and labels[k]: _lab(labels[k], x0 + sl * w + w // 2, H - 110, tt + 0.5, t1)
        _log(f'row of {len(specs)} reels on caramel', specs, t0, t1, 'each grows in on its word, holds for the sentence' +
             (' (labels: ' + ', '.join(l for l in labels if l) + ')' if labels else ''))
    add(min(times), 'row', fn)

def FRAMED(specs, times, labels=None):
    """2-3 smaller reels with caramel gaps (her 'the outfit feels elevated' screens): the good examples"""
    n = len(specs); w, h, gap = (540, 960, 90) if n == 2 else (500, 890, 70)
    x0 = (W - n * w - (n - 1) * gap) // 2; y0 = (H - h) // 2
    def fn(t0, t1, pk):
        for k, (s, tt) in enumerate(zip(specs, times)):
            x = x0 + k * (w + gap)
            _pnl(s, x, y0, x + w, y0 + h, tt, t1, 'corner', '0% 50%' if k == 0 else ('100% 50%' if k == n - 1 else '50% 50%'))
            if labels and labels[k]: _lab(labels[k], x + w // 2, y0 + h - 100, tt + 0.5, t1)
        _log(f'{n} framed reels on caramel', specs, t0, t1, 'each grows in on its word' + (' (labels: ' + ', '.join(l for l in labels if l) + ')' if labels else ''))
    add(min(times), 'framed', fn)

def ONE(shots, label=None):
    """one tall reel centred on caramel; the picture changes inside it on the words"""
    def fn(t0, t1, pk):
        stage(shots, t1, entry='fade' if pk == 'one' else 'centre')
        if label: _lab(label, W // 2, H - 110, t0 + 0.6, t1)
        _log('one reel centred on caramel', [s for s, _ in shots], t0, t1, 'grows from the centre; pictures change inside it')
    add(shots[0][1], 'one', fn)

def CREAM1(shots, w=760, label=None):
    """one reel centred on the cream screen (logo hidden under the cream); pictures may change inside it"""
    def fn(t0, t1, pk):
        c = nid('cr'); els.append(f'<div id="{c}" class="cream" style="opacity:0"></div>'); fade_in(c, t0, 0.5); fade_out(c, t1, 0.5)
        x0 = (W - w) // 2; inner = []; ta = shots[0][1]
        for k, (spec, t) in enumerate(shots):
            tend = (shots[k + 1][1] + 0.4) if k + 1 < len(shots) else t1 + 0.55
            v, h = vid(spec, t, tend, style=GRADE + 'position:absolute;left:0;top:0;'); drift(v, t, tend, 1.04)
            if k: tw.append(f'tl.fromTo("#{v}",{{opacity:0}},{{opacity:1,duration:0.4,ease:"sine.inOut"}},{t:.3f});')
            inner.append(h)
        i = box(x0, 0, x0 + w, H, ''.join(inner), 'z-index:49'); fade_in(i, ta + 0.15, 0.6); fade_out(i, t1, 0.5)
        if label:
            j = nid('lb'); els.append(f'<div id="{j}" class="cl" style="left:{W//2-300}px;top:{H-110}px;width:600px;opacity:0;font-family:Playfair;font-size:40px;z-index:50">{label}</div>')
            tw.append(f'tl.fromTo("#{j}",{{opacity:0,y:12}},{{opacity:1,y:0,duration:0.7,ease:"power2.out"}},{ta+0.7:.3f});'); fade_out(j, t1, 0.45)
        _log('one reel on the cream screen', [s for s, _ in shots], t0, t1, 'cream fades up, the reel fades in centred')
    add(shots[0][1], 'cream', fn)

def QUOTE(spec, t, l1, ta, l2, tb):
    """a reel on the left, the principle on the right (white serif, one word in script)"""
    def fn(t0, t1, pk):
        _pnl(spec, 170, 0, 170 + RW, H, t0, t1, 'fade'); text(l1, 'qs1', ta, t1, dur=1.4); text(l2, 'qs2', tb, t1, dur=1.2)
        _log('reel left + principle line', [spec], t0, t1, f'line wipes in: "{_plain(l1)} / {_plain(l2)}"')
    add(t, 'quote', fn)

CUTS_USED = []
def CUTS(items):
    """product cut-outs on caramel, side by side, each rising in on its word with a small serif label (her trousers screen)
    items = [(png in assets/, label, t), ...]"""
    def fn(t0, t1, pk):
        n = len(items); slot = min(600, (W - 160) // n); x = (W - n * slot) // 2
        for k, (png, lab, tt) in enumerate(items):
            i = nid('ct'); CUTS_USED.append(png)
            els.append(f'<div id="{i}" class="cl" style="left:{x + k*slot}px;top:70px;width:{slot}px;height:960px;opacity:0;'
                       f'display:flex;flex-direction:column;align-items:center;justify-content:flex-end;text-shadow:none">'
                       f'<img src="assets/{png}" style="max-width:{slot-70}px;max-height:780px;filter:drop-shadow(0 16px 18px rgba(70,35,15,.32))">'
                       f'<div style="margin-top:20px;font-family:Playfair;font-size:40px;color:#fff;text-shadow:0 2px 12px rgba(60,40,25,.4)">{lab}</div></div>')
            tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:24}},{{opacity:1,y:0,duration:0.8,ease:"power2.out"}},{tt:.3f});'); fade_out(i, t1, 0.5)
        SB.append(dict(kind='product cut-outs on caramel', clips=[[p, 0, 0] for p, _, _ in items], t0=round(t0, 2), t1=round(t1, 2),
                       move='each rises in on its word, labelled: ' + ', '.join(l for _, l, _ in items)))
    add(min(tt for _, _, tt in items), 'cut', fn)

def _fs(spec, t0, t1, fin):
    v, h = vid(spec, t0, t1 + 0.5); drift(v, t0, t1 + 0.5, 1.04)
    i = box(0, 0, W, H, h); fade_in(i, t0, fin); fade_out(i, t1, 0.45); return i
def FS(spec, t, fin=0.5):
    """full screen: landscape footage only (the film scenes, landscape stock)"""
    assert land(spec[0]), f'{spec[0]} is not landscape: vertical reels are never shown full screen'
    add(t, 'fs', lambda t0, t1, pk: (_fs(spec, t0, t1, 0.01 if t0 < 0.1 else fin), _log('full screen (landscape)', [spec], t0, t1, 'dissolve, slow push-in')))

def CARD(txt, i, t_in=None, style=''):
    """her number card: white, black script wiping in left to right"""
    t = (en(i - 1) + 0.35) if t_in is None else t_in
    def fn(t0, t1, pk):
        white(t0, t1); text(txt, 'card', t0 + 0.3, t1 - 0.1, dur=1.2, out=0.45, style=style)
        _log('white number card', [], t0, t1, f'fade to white, black script wipes in: "{_plain(txt)}"')
    add(t, 'card', fn)

def GUIDE(t0, t1):
    i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, t0, 0.8); fade_out(i, t1, 0.5)
    text('Check the description for', 'gtx1', t0 + 0.5, t1 - 0.05, dur=1.1); text('Personal Stylist Guide', 'gtx2', t0 + 0.9, t1 - 0.05, dur=1.6)
    _log('guide text', [], t0, t1, 'haze, "Check the description for / Personal Stylist Guide"')
TWO = 'font-size:96px;line-height:1.3;text-align:center'

# ================= HOOK =================
# 1 "Have you ever seen a woman on a freezing winter day, walking calmly down the street in a long wool coat, a soft scarf,
#    beautiful gloves, and thought, 'How does she look so elegant... when I just look cold?'"
FS(C('film_alps', 0.0, 4.1), 0.0)                                        # Charade: the snowy Alps (freezing winter day)
FS(C('film_trench', 1.0, 3.6), at(1, 'walking calmly') - 0.1)            # Audrey walking calmly down a Paris street
ROW([C('a_buttoncoat17', 0.0, 9.5), C('b_rushing53', 0.0, 8.5), C('f_gloves4', 0.0, 4.6)],
    [at(1, 'long wool coat'), at(1, 'a soft scarf'), at(1, 'beautiful gloves')])
ONE([(C('f_coldhands6', 0.0, 4.4), at(1, 'when I just') - 0.1)])          # "...when I just look cold?"
# 2 "She isn't shivering. She isn't buried under ten layers. And yet she looks polished, warm, and completely at ease."
ROW([C('b_hikesnow2', 0.0, 9.9), C('a_buttoncoat50', 0.0, 10.1), C('b_hikesnow28', 0.0, 9.0)],
    [st(2) - 0.05, at(2, "She isn't buried"), at(2, 'polished')])
# 3 "That kind of elegance isn't accidental. And the secret, it's often not about how much she's wearing, it's about what
#    she knows not to wear."
ONE([(C('a_fineturtle42', 0.0, 3.6), st(3) - 0.05), (C('a_fineturtle27', 4.0, 11.6), at(3, 'And the secret'))])
FS(C('film_closeup2', 0.0, 3.4), at(3, "it's about what") - 0.1)
# 4 "Welcome to The Classy Elegance. I'm so glad you're here. And if you've been with us for a while, yes, we have a new
#    name. Same channel, same timeless style, just a new chapter."
FS(C('film_yellowcoat', 0.0, 6.6), st(4) - 0.1)
def _newname(t0, t1, pk):          # "yes, we have a new name": the new monogram on white (the end card's look)
    white(t0, t1); j = nid('nn'); els.append(f'<img id="{j}" class="endlogo" src="assets/logo_ce_dark.png" style="opacity:0">')
    tw.append(f'tl.fromTo("#{j}",{{opacity:0,scale:0.96}},{{opacity:1,scale:1,duration:1.0,ease:"power2.out"}},{t0 + 0.3:.3f});'); fade_out(j, t1 - 0.05, 0.45)
    _log('white card with the new monogram', [], t0, t1, 'fade to white, the CE monogram fades up')
add(at(4, 'yes, we have') - 0.2, 'card', _newname)
ROW([C('a_oversizedcoat23', 0.0, 6.0), C('a_oversizedcoat8', 0.0, 5.0), C('a_buttoncoat42', 2.5, 7.5)],
    [at(4, 'Same channel'), at(4, 'same timeless'), at(4, 'just a new')])
# 5 "In today's video, we're uncovering eight things elegant women never wear in winter and the smarter swaps that keep you
#    warmer and look far more expensive."
def _today(t0, t1, pk):
    white(t0, t1); text("in today's video...", 'card', t0 + 0.3, t1 - 0.1, dur=1.0, out=0.4)
    _log('white card', [], t0, t1, 'black script wipes in: "in today\'s video..."')
add(en(4) + 0.4, 'card', _today)
FS(C('film_terrace', 0.0, 6.0), st(5) + 1.4)
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Episode 15</div><div class="big" style="font-size:86px">8 Things Elegant Ladies Never Wear in Winter</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.2,ease:"power2.out"}},{st(5)+1.9:.3f});'); fade_out(i, at(5, 'and the smarter') - 0.1, 0.5)
_log('title over the film scene', [], st(5) + 1.9, at(5, 'and the smarter'), '"Episode 15" serif + title in white script, fades up 1.2 s')
ROW([C('a_cashmerecoat36', 0.0, 6.6), C('f_mittens24', 0.0, 9.5), C('a_buttoncoat68', 0.0, 8.0)],
    [at(5, 'and the smarter'), at(5, 'keep you warmer'), at(5, 'look far more')])
# 6 "Some of these may surprise you, because a few of the pieces we reach for to stay warm can actually leave us colder.
#    But once you see them, you'll never unsee them. Let's get started."
ONE([(C('c_fuzzy3', 0.0, 4.0), st(6) - 0.05), (C('a_bulkycoat28', 0.0, 6.4), at(6, 'the pieces we reach')),
     (C('f_coldhands39', 0.0, 4.0), at(6, 'can actually leave'))])
FS(C('film_closeup', 0.0, 5.0), at(6, 'But once') - 0.1)

# ================= 1. A CHUNKY SWEATER SQUEEZED UNDER A FITTED COAT =================
CARD('1. A chunky sweater squeezed under a fitted coat', 7, style='font-size:90px')
# 8 "We've all done this. It's freezing, so you grab your thickest knit, pull your coat over the top, and suddenly you can
#    barely bend your arms. It feels like the warmest choice."
FS(C('film_alps', 4.15, 7.04), st(8) - 0.05)                               # "It's freezing"
ROW([C('a_bulkycoat29', 0.0, 10.0), C('a_coatoversweater21', 11.5, 19.0), C('a_coatoversweater57', 8.0, 14.0)],
    [at(8, 'grab your thickest'), at(8, 'over the top'), at(8, 'barely bend')])
# 9 "But here's what most people don't realize. What keeps you warm isn't really the fabric itself. It's the still air
#    trapped inside it."
QUOTE(C('a_chunkyunder24', 0.0, 12.9), st(9) - 0.05, "It isn't the <i>fabric</i>", at(9, "isn't really"), "it's the still air trapped inside", at(9, "It's the still"))
# 10 "When a thick sweater is pressed tight against the inside of a coat, both get squashed, and that warm pocket of air
#     gets squeezed out."
CUTS([('cut_cableknit1.png', 'Thick knit', at(10, 'thick sweater')), ('cut_coat14.png', 'Fitted coat', at(10, 'inside of a coat'))])
# 11 "So you look bulkier, your coat pulls across the shoulders and buttons, and you're often not as warm as you'd expect."
ROW([C('x_bulkyunder14', 0.0, 9.0), C('a_coatoversweater44', 16.5, 23.0), C('f_coldhands0', 0.0, 6.0)],
    [at(11, 'look bulkier'), at(11, 'your coat pulls'), at(11, 'not as warm')])
# 12 "Instead, try a fine merino or cashmere knit under your coat. It's thin, but it holds warmth beautifully without the bulk."
CUTS([('cut_finemerino26.png', 'Fine merino', at(12, 'fine merino')), ('cut_cashmere12.png', 'Cashmere', at(12, 'cashmere'))])
FRAMED([C('a_fineturtle5', 1.5, 7.0), C('a_fineturtle25', 0.0, 8.0)], [at(12, "It's thin"), at(12, 'holds warmth')])
# 13 "And if you love your chunky cable knit, and honestly, who doesn't, let it be the star. Wear it on its own on milder
#     days or under a coat cut roomy enough to fit over it."
ROW([C('a_cableknit55', 0.0, 12.0), C('a_cableknit1', 0.0, 8.0), C('a_cableknit15', 0.0, 7.0)],
    [at(13, 'chunky cable'), at(13, 'let it be'), at(13, 'Wear it on')])
FRAMED([C('a_chunkyunder40', 0.0, 5.0), C('a_chunkyunder36', 0.0, 5.5)], [at(13, 'under a coat'), at(13, 'roomy enough')])
# 14 "When you shop for a coat, try it on over the thickest sweater you plan to wear. If you can lift your arms and button it
#     without pulling, that's the one. So chic."
ONE([(C('a_coattryon13', 0.0, 2.2), st(14) - 0.05), (C('a_coatoversweater15', 2.0, 7.0), at(14, 'try it on')),
     (C('a_oversizedcoat28', 7.5, 11.5), at(14, 'If you can')), (C('a_coattryon42', 3.0, 8.0), at(14, "that's the one"))])

# ================= 2. COTTON NEXT TO YOUR SKIN =================
CARD('2. Cotton next to your skin<br>on busy, rushing around days', 15, style=TWO)
# 16 "Cotton is lovely. Soft, breathable, easy. But in winter, there's one situation where it quietly works against you."
ROW([C('b_whitetee10', 2.0, 12.0), C('b_sweatshirt7', 12.0, 20.0), C('b_cottonshirt4', 0.0, 7.0)],
    [st(16) - 0.05, at(16, 'Soft'), at(16, 'easy')])
# 17 "Cotton soaks up moisture and dries slowly, and once it's damp, it loses much of its ability to keep you warm. And that
#     moisture doesn't only come from the rain."
ONE([(C('b_whitetee37', 0.0, 9.5), st(17) - 0.05)])
ROW([C('b_raincoat0', 0.0, 5.6), C('b_raincoat9', 0.0, 6.5), C('b_raincoat46', 0.0, 6.0)],
    [at(17, 'And that moisture'), at(17, 'only come'), at(17, 'the rain')])
# 18 "Think about a typical winter day. You hurry to the train, walk briskly in your coat, step into a heated shop or office,
#     and you start to warm up."
ROW([C('b_metro3', 0.0, 9.0), C('b_rushing17', 0.0, 7.5), C('b_office14', 0.0, 5.0)],
    [at(18, 'hurry to the train'), at(18, 'walk briskly'), at(18, 'step into')])
# 19 "Your cotton tee absorbs that little bit of sweat and holds on to it. Then you step back outside, and suddenly you feel
#     colder than when you left the house. Sound familiar?"
ONE([(C('b_whitetee10', 12.0, 18.0), st(19) - 0.05), (C('b_office38', 0.0, 2.5), at(19, 'Then you step')),
     (C('f_coldhands8', 0.0, 8.0), at(19, 'suddenly you feel'))])
# 20 "Instead, choose a base layer that handles moisture better. Merino wool is a beautiful option."
CUTS([('cut_merinotop22.png', 'Base layer', at(20, 'base layer')), ('cut_merinotop56.png', 'Merino wool', at(20, 'Merino wool'))])
# 21 "Wool can absorb around a third of its weight in moisture vapor before it even starts to feel wet, so it stays
#     comfortable as you move between the cold street and a warm room."
QUOTE(C('c_merino10', 0.0, 12.6), st(21) - 0.05, 'Wool can absorb', at(21, 'Wool can'), 'around <i>a third</i> of its weight', at(21, 'around a third'))
FRAMED([C('b_rushing47', 0.0, 6.9), C('c_merino51', 0.0, 6.0)], [at(21, 'the cold street'), at(21, 'a warm room')])
# 22 "A thin silk layer or a good synthetic thermal works well, too, and dries quickly."
CUTS([('cut_silk3.png', 'Silk', at(22, 'silk layer')), ('cut_thermal18.png', 'Thermal', at(22, 'synthetic thermal'))])
# 23 "And here's a little trick hikers swear by. Dress for how you'll feel 10 minutes into your walk, not the moment you open
#     the door."
ONE([(C('b_hikesnow17', 0.0, 4.5), st(23) - 0.05)])
QUOTE(C('b_hikesnow41', 0.0, 6.0), at(23, 'Dress for') - 0.1, "Dress for how you'll feel", at(23, 'Dress for'), '<i>10 minutes</i> into your walk', at(23, '10 minutes'))
ONE([(C('b_office36', 0.0, 3.0), at(23, 'open the door') - 0.3)])
# 24 "Now, this doesn't mean cotton is off limits. On a dry day when you're mostly indoors, your favorite cotton shirt is
#     perfectly fine. It's the damp, active, in-and-out days where it lets you down."
ROW([C('b_cottonshirt1', 0.0, 9.0), C('b_cottonshirt70', 1.5, 6.0), C('b_cottonshirt9', 0.0, 4.5)],
    [at(24, 'cotton is off'), at(24, 'your favorite'), at(24, 'perfectly fine')])
ROW([C('b_raincoat24', 4.0, 10.0), C('b_rushing57', 0.0, 5.0), C('b_rushing12', 1.4, 5.5)],
    [at(24, 'the damp'), at(24, 'active'), at(24, 'in-and-out')])

# ================= 3. THE COZY ACRYLIC SWEATER =================
CARD('3. The cozy acrylic sweater', 25)
# 26 "It looks soft on the hanger, it's often a fraction of the price, and it feels warm the moment you put it on."
ROW([C('c_sweatershop12', 0.0, 8.5), C('c_sweatershop36', 0.0, 7.9), C('c_fuzzy0', 0.0, 5.0)],
    [at(26, 'soft on the'), at(26, 'a fraction'), at(26, 'feels warm')])
# 27 "But acrylic absorbs very little moisture. So when you go from the cold outside into a heated room, the warmth and
#     moisture your body gives off has nowhere to go. That's why some acrylic knits feel toasty one minute and strangely
#     clammy the next."
ONE([(C('c_fuzzy15', 0.0, 4.5), st(27) - 0.05)])
FRAMED([C('b_hikesnow16', 2.0, 11.0), C('c_fuzzy19', 0.0, 8.0)], [at(27, 'the cold outside'), at(27, 'a heated room')])
QUOTE(C('c_fuzzy24', 0.0, 8.0), at(27, "That's why") - 0.1, 'toasty one minute', at(27, 'toasty'), 'strangely <i>clammy</i> the next', at(27, 'strangely'))
# 28 "And many acrylic sweaters pill quickly. Those little fuzzy balls that appear under the arms and along the sides after
#     just a few wears."
ONE([(C('c_pilling8', 0.0, 4.5), at(28, 'pill quickly') - 0.1), (C('c_pilling3', 0.0, 6.0), at(28, 'Those little')),
     (C('c_pilling20', 2.0, 12.0), at(28, 'under the arms'))])
# 29 "And as we've said before on this channel, nothing takes away from an elegant look faster than clothing that looks worn
#     down."
FRAMED([C('c_cashmere15', 0.0, 8.0), C('c_pilling20', 14.0, 21.0)], [at(29, 'an elegant look'), at(29, 'looks worn')])
# 30 "Instead, flip to the label before you buy. Look for wool, merino, cashmere, or a wool-rich blend."
ONE([(C('c_label26', 0.0, 6.8), at(30, 'flip to') - 0.1)])
CUTS([('cut_cableknit4.png', 'Wool', at(30, 'wool,')), ('cut_finemerino11.png', 'Merino', at(30, 'merino')),
      ('cut_cashmere4.png', 'Cashmere', at(30, 'cashmere')), ('cut_cashmere46.png', 'Wool-rich blend', at(30, 'wool-rich'))])
# 31 "Then give the knit a gentle stretch. A quality knit feels dense and springs right back into shape. If it stays stretched
#     out or you can see straight through it, put it back."
ONE([(C('c_label13', 0.0, 5.0), st(31) - 0.05), (C('c_label0', 0.0, 6.0), at(31, 'feels dense')),
     (C('c_label28', 0.0, 5.0), at(31, 'If it stays')), (C('c_sweatershop2', 0.0, 3.0), at(31, 'put it back'))])
# 32 "Now, a little acrylic in a blend isn't a bad thing. It can make a sweater more affordable and easier to care for. Just
#     let it be the supporting fiber, not the whole sweater."
ROW([C('c_cashmere25', 0.0, 10.0), C('c_cashmere10', 0.0, 8.0), C('c_merino69', 0.0, 4.0)],
    [at(32, 'a little acrylic'), at(32, 'more affordable'), at(32, 'supporting')])
# 33 "And washing your knits inside out on a gentle cycle helps them stay smooth for so much longer."
ONE([(C('c_wash11', 0.0, 8.0), st(33) - 0.05), (C('c_wash33', 12.5, 17.0), at(33, 'helps them'))])
# 34 "And here's a secret many well-dressed women don't share. They know exactly what flatters them. The colors that make
#     their skin glow in that soft winter light and the coat shapes that complement their figure."
FS(C('film_yellowclose', 0.0, 4.2), st(34) - 0.05)
ROW([C('b_whitetee12', 0.0, 16.0), C('a_buttoncoat36', 0.0, 7.9), C('a_buttoncoat23', 0.0, 5.0)],
    [at(34, 'They know'), at(34, 'skin glow'), at(34, 'coat shapes')])
# 35 guide plug: "...our personal stylist guide is linked in the description... Now, let's continue."
FS(C('film_headscarf', 0.0, 8.0), st(35) - 0.05)
FS(C('film_closeup2', 3.4, 12.0), at(35, 'our personal') - 0.1)
GUIDE(at(35, 'our personal stylist') + 0.1, at(35, "Now, let's") - 0.05)

# ================= 4. BOOTS THAT FIT PERFECTLY IN OCTOBER =================
CARD('4. Boots that fit perfectly in October', 36)
# 37 "You buy them in early fall, wear them with thin socks, and they fit like a dream. Then winter arrives, you add your
#     thickest socks, and suddenly they're snug across the toes."
ROW([C('d_bootstry1', 0.0, 7.0), C('d_ankleboots33', 0.0, 5.0), C('d_ankleboots21', 0.0, 6.0)],
    [st(37) - 0.05, at(37, 'wear them with'), at(37, 'fit like a dream')])
ONE([(C('b_hikesnow13', 0.0, 2.2), at(37, 'Then winter') - 0.1), (C('d_woolsocks25', 0.0, 3.4), at(37, 'you add your') - 0.1),
     (C('d_woolsocks18', 1.5, 7.0), at(37, 'suddenly'))])
# 38 "It feels like you've just made them warmer, but often it's the opposite. When your boots are too tight, they squeeze
#     your feet, and that can restrict the blood flow that keeps your toes warm."
ONE([(C('d_woolsocks13', 0.0, 3.0), st(38) - 0.05), (C('d_woolsocks25', 6.0, 12.0), at(38, 'but often')),
     (C('d_bootzip13', 0.0, 11.0), at(38, 'When your boots'))])
# 39 "The tightness also crushes the insulation in your socks and in the boot itself. So the thickest sock in a tight boot
#     can leave you with colder feet than a thinner sock with a little room."
ONE([(C('d_bootstry14', 0.0, 6.5), st(39) - 0.05)])
CUTS([('cut_socks42.png', 'Thickest sock', at(39, 'So the thickest')), ('cut_socks15.png', 'Thinner sock', at(39, 'a thinner sock'))])
# 40 "Instead, aim for enough space to wiggle your toes freely while your heel stays snugly in place. A fine merino sock
#     gives you warmth without the bulk."
FRAMED([C('d_kneeboots51', 0.0, 10.0), C('d_ankleboots46', 0.0, 6.0)], [st(40) - 0.05, at(40, 'while your heel')])
CUTS([('cut_socks46.png', 'Fine merino sock', at(40, 'A fine merino'))])
# 41 "And when you shop for winter boots, try them on in the afternoon, wearing the socks you'll actually wear with them."
ROW([C('d_bootstry56', 0.0, 9.0), C('d_bootstry43', 0.0, 7.0), C('d_bootstry39', 0.0, 7.0)],
    [st(41) - 0.05, at(41, 'try them on'), at(41, 'wearing the socks')])
# 42 "Of course, you don't want boots that are too loose either. If your foot slides around, cold air moves around inside
#     with it. The goal is room for your toes and support for your heel."
ONE([(C('d_kneeboots1', 0.0, 4.0), st(42) - 0.05), (C('d_bootzip18', 0.0, 6.5), at(42, 'If your foot'))])
QUOTE(C('d_kneeboots50', 0.0, 5.5), at(42, 'The goal') - 0.1, 'room for your <i>toes</i>', at(42, 'room for'), 'support for your heel', at(42, 'support'))

# ================= 5. SMOOTH SOLES ON ICY DAYS =================
CARD('5. Smooth soles on icy days', 43)
# 44 "There's nothing more elegant than a sleek leather boot or a pointed-toe heel with a long coat. But on ice, a smooth
#     sole has almost nothing to grip with. And no outfit looks graceful while you're tiptoeing down the pavement or worse,
#     slipping."
ROW([C('e_pointed6', 0.0, 6.5), C('e_pointed13', 0.0, 9.0), C('e_pointed10', 0.0, 8.5)],
    [at(44, 'a sleek leather'), at(44, 'pointed-toe'), at(44, 'long coat')])
ONE([(C('e_iceslip15', 0.0, 5.0), at(44, 'But on ice') - 0.1), (C('e_heelsstreet24', 2.8, 6.6), at(44, 'And no outfit')),
     (C('e_iceslip22', 0.0, 6.2), at(44, 'tiptoeing'))])
# 45 "Here's something that surprised me. Researchers at Toronto's WinterLab tested nearly a hundred types of winter footwear
#     on ice, and fewer than one in 10 met their minimum standard for grip."
ROW([C('d_ankleboots11', 0.0, 11.0), C('e_lugbrown12', 0.0, 6.0), C('d_bootstry55', 0.0, 5.0)],
    [st(45) - 0.05, at(45, 'tested nearly'), at(45, 'winter footwear')])
QUOTE(C('e_iceslip15', 5.0, 10.5), at(45, 'and fewer') - 0.1, 'fewer than <i>one in 10</i>', at(45, 'fewer than'), 'met the standard for grip', at(45, 'met their'))
# 46 "The ones that performed best had special soles with tiny grit-like particles built right into the rubber. So even a
#     boot sold as a winter boot isn't automatically safe on ice."
ONE([(C('d_bootstry55', 5.0, 11.4), st(46) - 0.05), (C('d_woolsocks38', 0.0, 6.0), at(46, 'So even'))])
# 47 "Instead, keep one pair with a deeply treaded rubber sole for icy mornings. Many now come in sleek black or brown leather
#     that look just as polished."
FRAMED([C('e_lugboots0', 6.0, 13.6), C('d_woolsocks38', 6.0, 12.9)], [st(47) - 0.05, at(47, 'for icy mornings')])
CUTS([('cut_lugboot46.png', 'Black leather', at(47, 'sleek black')), ('cut_lugboot38.png', 'Brown leather', at(47, 'brown leather'))])
# 48 "You can also ask a cobbler to add a thin rubber sole protector to your favorite leather-soled shoes. It's affordable
#     and adds grip."
ONE([(C('e_cobbler40', 0.0, 6.0), at(48, 'ask a cobbler') - 0.1), (C('e_cobbler56', 6.5, 13.5), at(48, 'thin rubber'))])
# 49 "And for truly icy days, a pair of slip-on ice grips can live in your bag and come off the moment you arrive."
ONE([(C('e_cleats2', 0.0, 8.0), st(49) - 0.05)])
# 50 "Now, on dry, cleared pavement, wear your elegant soles and enjoy them. It's simply about knowing which days call for
#     something more."
ROW([C('e_heelsstreet12', 0.0, 12.0), C('e_heelsstreet37', 0.0, 6.9), C('e_heelsstreet41', 0.0, 9.6)],
    [st(50) - 0.05, at(50, 'wear your elegant'), at(50, 'enjoy them')])

# ================= 6. THIN, UNLINED LEATHER GLOVES =================
CARD('6. Thin, unlined leather gloves', 51)
# 52 "Leather gloves are a winter classic and for good reason. They're timeless, sleek, and they finish a coat beautifully."
ROW([C('f_gloves1', 0.0, 9.0), C('f_gloves13', 0.0, 7.0), C('f_gloves18', 0.0, 7.0)],
    [st(52) - 0.05, at(52, 'sleek'), at(52, 'finish a coat')])
# 53 "But a very thin, unlined pair on a freezing, windy day leaves just a fine layer of leather between your fingers and
#     the cold."
ONE([(C('f_lined38', 0.0, 4.0), st(53) - 0.05), (C('h_windy35', 0.0, 3.5), at(53, 'freezing, windy')),
     (C('f_lined15', 0.0, 7.0), at(53, 'a fine layer'))])
# 54 "And when your hands are cold, you tense up. Your shoulders rise, you rush, you hide your hands in your sleeves. Not
#     exactly the calm, composed presence we're going for."
ROW([C('f_coldhands38', 0.0, 7.5), C('f_coldhands18', 0.0, 6.0), C('b_rushing22', 0.0, 5.1)],
    [at(54, 'you tense'), at(54, 'shoulders rise'), at(54, 'you rush')])
QUOTE(C('f_gloves13', 8.0, 15.7), at(54, 'Not exactly') - 0.1, 'the calm,', at(54, 'the calm'), '<i>composed</i> presence', at(54, 'composed'))
# 55 "Instead, look for leather gloves lined in cashmere, wool, or fleece. They keep the same slim, elegant shape with far
#     more warmth inside."
CUTS([('cut_gloves49.png', 'Cashmere-lined', at(55, 'cashmere')), ('cut_gloves28.png', 'Wool-lined', at(55, 'wool,')),
      ('cut_gloves60.png', 'Fleece-lined', at(55, 'fleece'))])
ONE([(C('f_lined0', 4.0, 10.5), at(55, 'They keep') - 0.1)])
# 56 "And on the coldest days, consider mittens. When they're made from the same materials, mittens are warmer than gloves
#     because your fingers share their warmth instead of each one facing the cold on its own."
ONE([(C('b_hikesnow27', 0.0, 5.2), at(56, 'consider mittens') - 0.1), (C('b_hikesnow28', 9.0, 21.5), at(56, 'mittens are warmer'))])
# 57 "A soft lined leather or knit mitten looks incredibly chic with a long wool coat. And if you need your fingers free, a thin
#     liner glove underneath a mitten gives you the best of both."
CUTS([('cut_mittens2.png', 'Lined leather mitten', at(57, 'soft lined')), ('cut_mittens14.png', 'Knit mitten', at(57, 'knit mitten'))])
ONE([(C('f_gloves15', 0.0, 8.0), at(57, 'chic with')), (C('f_lined16', 0.0, 6.0), at(57, 'a thin liner'))])

# ================= 7. NOTHING ON YOUR HEAD =================
CARD("7. Nothing on your head because<br>you don't want to ruin your hair", 58, style=TWO)
# 59 "I completely understand this one. You've done a beautiful blowout, and the last thing you want is hat hair."
ROW([C('g_blowout0', 0.0, 13.0), C('g_blowout1', 4.5, 13.0), C('x_hatoff7', 0.0, 4.5)],
    [st(59) - 0.05, at(59, 'beautiful blowout'), at(59, 'hat hair')])
# 60 "And you may have heard that we lose most of our body heat through our heads. That's actually a myth."
ONE([(C('g_coldears21', 0.0, 4.6), st(60) - 0.05)])
QUOTE(C('f_mittens25', 0.0, 4.4), at(60, "That's actually") - 0.1, "That's actually", at(60, "That's actually"), 'a <i>myth</i>.', at(60, 'a myth'))
# 61 "Researchers writing in the British Medical Journal traced it back to a flawed interpretation of an old military
#     experiment. Your head loses heat much like any other uncovered part of your body."
ONE([(C('b_office37', 0.0, 9.0), st(61) - 0.05), (C('g_coldears25', 0.0, 6.8), at(61, 'Your head loses'))])
# 62 "But here's what does matter. Your ears are one of the areas most vulnerable to frostbite, along with your fingers, toes,
#     nose, cheeks, and chin. And on a windy day, cold, stinging ears can make you miserable in minutes."
ONE([(C('f_coldhands51', 0.0, 9.0), st(62) - 0.05), (C('f_coldhands6', 4.5, 9.4), at(62, 'fingers')),
     (C('g_coldears3', 0.0, 9.3), at(62, 'And on a windy'))])
# 63 "So instead of skipping it altogether, choose something that protects your ears and your hairstyle."
ONE([(C('g_earmuffs18', 0.0, 6.0), st(63) - 0.05), (C('g_earmuffs1', 0.0, 5.2), at(63, 'choose something'))])
# 64 "A wide knit or cashmere headband keeps your ears covered and looks beautiful with a sleek low bun or a soft blowout."
ROW([C('g_headband25', 0.0, 12.7), C('g_lowbun17', 0.0, 8.0), C('g_headband9', 3.5, 9.5)],
    [st(64) - 0.05, at(64, 'sleek low bun'), at(64, 'soft blowout')])
# 65 "A wool beret is timeless and effortlessly chic. And if you love a beanie, choose a fine merino or cashmere one rather
#     than a stiff, heavy knit. Just make sure your hair is completely dry before you put it on. So pretty."
ROW([C('g_beret14', 0.0, 6.4), C('f_mittens35', 0.0, 8.0), C('g_beret46', 0.0, 4.1)],
    [st(65) - 0.05, at(65, 'is timeless'), at(65, 'effortlessly')])
FRAMED([C('g_beanie28', 0.0, 9.0), C('g_beanie5', 0.0, 8.0), C('g_beanie48', 0.0, 5.0)],
       [at(65, 'And if you love'), at(65, 'fine merino'), at(65, 'a stiff')])
ONE([(C('g_blowout2', 0.0, 7.6), at(65, 'Just make sure') - 0.1), (C('g_beret2', 0.0, 5.0), at(65, 'So pretty') - 0.3)])

# ================= 8. THE COAT THAT ONLY LOOKS WARM =================
FS(C('film_creamcoat', 0.0, 4.0), st(66) - 0.05)                               # "Saving one of my favorites for last": Audrey's cream coat
CARD('8. The coat that only looks warm', 66, t_in=at(66, 'Number eight') - 0.35)
# 67 "Your coat is often the first thing people notice in winter, and it's the piece doing most of the work to keep you warm."
ROW([C('a_oversizedcoat1', 0.0, 11.6), C('a_oversizedcoat4', 0.0, 8.0), C('f_mittens2', 0.0, 9.8)],
    [st(67) - 0.05, at(67, 'people notice'), at(67, 'doing most')])
# 68 "But two coats can look almost identical on the hanger and feel completely different on a windy street. The difference
#     is often the fabric."
FRAMED([C('h_coatrail0', 0.0, 7.2), C('h_windy1', 0.0, 7.0)], [at(68, 'on the hanger') - 0.6, at(68, 'feel completely')])
ONE([(C('a_coattryon13', 2.2, 9.0), at(68, 'The difference') - 0.1)])
# 69 "A loosely woven coat can let the wind cut straight through it, no matter how thick it looks. Dense, tightly woven, or
#     felted wool fabrics like melton or boiled wool hold up far better against the wind, and they keep their shape
#     beautifully year after year."
ONE([(C('h_windy7', 0.0, 8.2), st(69) - 0.05), (C('h_wool12', 0.0, 4.0), at(69, 'Dense, tightly')),
     (C('h_wool9', 0.0, 5.0), at(69, 'felted wool')), (C('h_windy31', 0.0, 11.1), at(69, 'hold up far'))])
# 70 "Before you buy, check the label. A high wool content is what you're looking for. And a small amount of nylon or
#     polyester is perfectly fine. It can actually make a coat more durable."
ONE([(C('a_coattryon35', 2.5, 8.0), st(70) - 0.05), (C('h_coatlabel38', 3.5, 7.2), at(70, 'A high wool')),
     (C('h_coatlabel12', 0.0, 10.6), at(70, 'And a small')), (C('a_coattryon57', 0.0, 9.4), at(70, 'It can actually'))])
# 71 "Then try this simple test. Hold the fabric up to a window or a bright light. If light shines easily through the weave,
#     chances are the wind will, too."
ONE([(C('x_sheer40', 0.0, 2.2), at(71, 'Hold the fabric') - 0.1), (C('x_sheer3', 4.6, 7.4), at(71, 'a bright light')),
     (C('x_sheer3', 13.3, 16.3), at(71, 'If light shines')), (C('h_windy59', 2.5, 7.6), at(71, 'chances are'))])
# 72 "And finally, look at the length. On truly cold, windy days, a coat that covers your hips and upper thighs protects far
#     more of you than a cropped style. And that long, clean line always looks elegant."
ONE([(C('h_longcoat19', 0.0, 8.4), at(72, 'look at the length') - 0.1)])
FRAMED([C('h_windy27', 0.0, 13.2), C('h_cropped16', 0.0, 5.6)], [at(72, 'a coat that covers'), at(72, 'than a cropped')],
       labels=['Covers hips and thighs', 'Cropped'])
ROW([C('h_longcoat24', 0.0, 9.0), C('h_longcoat5', 0.0, 8.9), C('h_longcoat43', 0.0, 4.4)],
    [at(72, 'And that long'), at(72, 'clean line'), at(72, 'always looks')])
# 73 "When you find that coat, the right weave, the right weight, the right fit, it becomes the piece you reach for every
#     single winter. That's quiet luxury in its truest form."
ROW([C('h_wool23', 0.0, 11.7), C('a_oversizedcoat32', 0.0, 9.0), C('h_longcoat31', 0.0, 7.2)],
    [at(73, 'the right weave'), at(73, 'the right weight'), at(73, 'the right fit')])
QUOTE(C('h_maxi23', 0.0, 8.0), at(73, "That's quiet") - 0.1, 'quiet <i>luxury</i>', at(73, 'quiet luxury'), 'in its truest form', at(73, 'in its truest'))

# ================= CLOSE =================
# 74 "Staying warm and looking elegant were never opposites. Often it's simply about choosing the right pieces for the weather
#     you're actually in."
FS(C('film_terrace', 6.0, 13.0), st(74) - 0.05)
ROW([C('a_oversizedcoat16', 0.0, 14.0), C('b_hikesnow18', 0.0, 9.0), C('a_cashmerecoat7', 14.0, 22.0)],
    [at(74, 'Often'), at(74, 'the right pieces'), at(74, 'the weather')])
# 75 "And I'm curious, what's the one winter piece you could never live without? Let me know in the comments. I always love
#     hearing from you."
CUTS([('cut_coat42.png', 'A wool coat', at(75, "what's the one")), ('cut_gloves0.png', 'Leather gloves', at(75, 'could never')),
      ('cut_cableknit24.png', 'A cable knit', at(75, 'live without'))])
ONE([(C('b_raincoat36', 0.0, 5.9), at(75, 'Let me know') - 0.1)])
# 76 "If you'd like a part two with even more winter style tips, just comment part two. And if you found this video helpful,
#     a simple like or comment would truly mean the world to us."
ROW([C('b_hikesnow14', 0.0, 9.3), C('a_oversizedcoat12', 0.0, 9.6), C('b_hikesnow32', 0.0, 7.2)],
    [st(76) - 0.05, at(76, 'even more winter'), at(76, 'just comment')])
ONE([(C('f_coldhands47', 0.0, 9.1), at(76, 'And if you found') - 0.1)])
# 77 guide plug: "...the personal stylist guide linked in the description. It's sent instantly to your email after access."
FS(C('film_pillbox', 0.0, 4.0), st(77) - 0.05)
FS(C('film_leopard', 0.0, 4.6), at(77, 'be sure to') - 0.1)
FS(C('film_creamwalk', 0.0, 8.0), at(77, 'linked in the') - 0.1)
GUIDE(at(77, 'the personal stylist'), en(77) + 0.25)
# 78 "Thank you so much for spending your time with us today. Until next time. Bye, my loves."
FS(C('film_gloves', 0.0, 4.6), st(78) - 0.05)
ONE([(C('b_rushing3', 1.0, 6.9), at(78, 'Until next') - 0.1)])

flush(total - 2.6)
json.dump(SB, open("storyboard.json", "w"), indent=0)
