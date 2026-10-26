# 8 Ways to Make Your Clothes Look New Again (Without Buying More) - the edit, beat by beat.
# Copies the reference "The Most Elegant (Easy) Hairstyles For All Hair Types" (EDITING-DNA.md, measured second by second):
#   hook in full-screen scenes -> photos appearing one by one on white -> white "In today's video" card -> full-screen scene
#   with "Episode N:" title; per point: white number card (on screen only, never spoken), full-screen scenes, a row of tall
#   panels on the caramel backdrop, ONE tall tutorial clip CENTRED on caramel held while the voice teaches, the creator's
#   handle in small script at its lower right and a small script tip on the left, photo rows on white (the named woman as
#   photos on white, as the reference does with the Princess of Wales); logo top-left except on white; outro on a calm
#   window scene, then the white end card.
# Footage: creators' Pinterest video pins (raw/meta.json: creator, pin id, source link), every segment checked on the
# strips (st/P_*.jpg), AI scan aiscan.json. Each footage segment used once.

WHITE = 'assets/white.mp4'
def logo_off(t0, t1):
    tw.append(f'tl.to("#logo",{{opacity:0,duration:0.35,ease:"sine.inOut"}},{t0:.3f});')
    tw.append(f'tl.to("#logo",{{opacity:0.92,duration:0.45,ease:"sine.inOut"}},{t1:.3f});')
def wbg(t0, t1):
    """plain white background (reference 0:06-0:09, 0:26-0:30, 2:53-2:56, 5:32-5:37, 6:58-7:06); no logo on white"""
    i = nid('wb')
    els.append(f'<div id="{i}" class="w" style="left:0;top:0;width:{W}px;height:{H}px;opacity:0">'
               f'<video id="{i}v" class="med" src="{WHITE}" muted playsinline data-start="{t0:.3f}" data-duration="{t1-t0+0.6:.3f}"></video></div>')
    fade_in(i, t0, 0.4); fade_out(i, t1, 0.5); logo_off(t0, t1 + 0.1); return i
def wrow(specs, times, t_end, h=820, gap=34):
    """photos / clips appearing one by one, side by side, on white"""
    n = len(specs); w = {1: 560, 2: 520, 3: 470, 4: 400}[n]
    x = (W - n * w - (n - 1) * gap) // 2; y0 = (H - h) // 2
    wbg(times[0] - 0.35, t_end)
    for k, (s, tt) in enumerate(zip(specs, times)):
        x0 = x + k * (w + gap); panel(s, x0, x0 + w, tt, t_end, entry='centre', y0=y0, y1=y0 + h)
def row4(specs, times, t_end, w=440, gapx=18):
    """2-4 tall panels on the caramel backdrop, one per spoken item (reference 0:53-1:09, 5:40-5:47)"""
    n = len(specs); x = (W - n * w - (n - 1) * gapx) // 2
    for k, (s, tt) in enumerate(zip(specs, times)):
        x0 = x + k * (w + gapx); panel(s, x0, x0 + w, tt, t_end, origin='50% 0%', y0=60, y1=H - 60)
def handle(key):
    u = (META.get(key, {}).get('user') or '').strip()
    return f'@{u}' if u else ''
def credit(txt, t0, t1, x0):
    """the creator's handle, small script, lower right of the tall frame (reference '@... on TikTok')"""
    if not txt: return
    i = nid('cl'); els.append(f'<div id="{i}" class="cl" style="left:{x0+PW-620}px;top:1000px;width:600px;text-align:right;font-size:34px;opacity:0">{txt}</div>')
    fade_in(i, t0 + 0.4, 0.5); fade_out(i, t1, 0.4)
def one(shots, t1):
    """ONE tall clip centred on caramel, held; the pictures change inside it on the word; creator credited"""
    x0 = (W - PW) // 2
    i = stage(shots, t1, x0=x0, entry='centre')
    for k, (spec, t) in enumerate(shots):
        tend = shots[k + 1][1] if k + 1 < len(shots) else t1
        credit(handle(spec[0]), t, tend, x0)
    return i
def tip(txt, t0, t1, y=500, size=58):
    """small script tip on the left of the tall frame (reference: '* We recommend using a french pin *')"""
    i = nid('cl'); els.append(f'<div id="{i}" class="cl" style="left:20px;top:{y}px;width:600px;font-size:{size}px;opacity:0">{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:14}},{{opacity:1,y:0,duration:0.8,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.5)
def full(shots, t1, xf=0.45):
    """full-bleed scene(s): close-ups of fabric fill the frame (reference 0:13-0:21)"""
    return demo(shots, t1, x0=0, w=W, xf=xf)
def scene(spec, t0, t1, fin=0.6):
    """full-screen scene from a vertical reel (blurred copy fills the frame, the sharp clip in the middle)"""
    return canvas_full(spec, t0, t1, fin=fin)
def cardg(txt, i_next, t0=None, style=''):
    """white number card in the silent gap before line i_next (headings are on screen only, never spoken)"""
    t0 = (en(i_next - 1) + 0.2) if t0 is None else t0
    white(t0, st(i_next) + 0.3); text(txt, 'card', t0 + 0.3, st(i_next) + 0.2, dur=1.2, out=0.45, style=style)
CROP['darks18'] = (90, 290, 960)        # the Spanish caption bubble at the top stays out of frame

# ================= HOOK =================
# 1 "You might think looking polished means buying new clothes. But what if I told you the pieces you already own can look new again, without wasting money on more?"
scene(C('whitecoat32', 0.0, 9.1), 0.0, at(1, 'But what if') - 0.1, fin=0.01)
scene(C('oldmoney3', 0.0, 12.4), at(1, 'But what if') - 0.1, en(1) + 0.3)
# 2 "Most of the time, your clothes haven't lost their charm. It's the small signs of wear. Fuzz on a favourite sweater.
#    Black that has quietly turned grey. Trousers that are just slightly too long. And most of that can be fixed at home, or for very little."
scene(C('sweaterwoman38', 0.0, 7.7), st(2) - 0.2, at(2, 'Fuzz') - 0.35)
wrow([C('depill33', 0.0, 9.5), C('darks18', 1.5, 1.5), C('tailor8', 0.0, 6.5)],
     [at(2, 'Fuzz'), at(2, 'Black that'), at(2, 'Trousers')], at(2, 'And most') - 0.1)
one([(C('buttons10', 0.0, 9.0), at(2, 'And most') - 0.2), (C('taperpants24', 0.0, 8.5), at(2, 'or for very little') - 0.2)], en(2) + 0.3)
# 3 "In today's video, we're sharing eight ways to bring your clothes back: how to tell what's worth saving, what to do for
#    each problem, and when it's kinder to let a piece go. Let's get started."
white(st(3) - 0.2, at(3, 'eight ways') + 0.3); logo_off(st(3) - 0.2, at(3, 'eight ways') + 0.3)
text("In today's video", 'card', st(3) + 0.05, at(3, 'eight ways') + 0.2, dur=1.2, out=0.45)
scene(C('closetaes30', 0.0, 5.0), at(3, 'eight ways'), at(3, 'worth saving') - 0.3)
wrow([C('dryflat7', 0.0, 7.0), C('steamer37', 0.0, 8.8), C('closetaes35', 0.0, 9.4)],
     [at(3, 'worth saving'), at(3, 'each problem'), at(3, 'let a piece go')], at(3, "Let's get started") - 0.1)
scene(C('daylight0', 0.0, 10.9), at(3, "Let's get started") - 0.3, en(3) + 2.3)
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Episode 14:</div><div class="big" style="font-size:84px">8 Ways to Make Your Clothes Look New Again</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.1,ease:"power2.out"}},{at(3, "Let") + 0.2:.3f});'); fade_out(i, en(3) + 2.0, 0.45)

# ================= 1. Tired or worn out? =================
cardg('1. Tired or worn out?', 4, t0=en(3) + 2.2)
# 4 "Before you fix anything, take the piece to a window and look at it in daylight. Indoor light is kind, and it hides a lot. Then ask which kind of problem you're looking at."
scene(C('daylight8', 0.0, 8.2), st(4) + 0.1, at(4, 'Indoor light') - 0.1)
scene(C('daylight18', 0.0, 5.6), at(4, 'Indoor light') - 0.1, at(4, 'Then ask') - 0.1)
one([(C('dryflat4', 0.0, 10.9), at(4, 'Then ask') - 0.2)], at(5, 'Lint') - 0.2)
tip('* look at it in daylight *', at(4, 'Then ask'), en(4) + 0.2)
# 5 "Some things only need care. Lint, fuzz, creases, a fresh stain."
wrow([C('lintroller40', 2.0, 5.6), C('depill19', 0.0, 3.5), C('steamer16', 5.0, 12.0), C('darks17', 3.7, 5.4)],
     [at(5, 'Lint'), at(5, 'fuzz'), at(5, 'creases'), at(5, 'a fresh stain')], en(5) + 0.3)
# 6 "Some need a small repair. A loose button, a seam that has opened while the fabric around it is still strong, a hem that has
#    dropped, a zip that has stopped working. A needle and thread or a local tailor can often bring those back."
one([(C('buttons10', 20.5, 28.0), st(6) - 0.2)], at(6, 'A loose button') - 0.1)
row4([C('replacebuttons4', 2.3, 10.0), C('reshape32', 0.0, 9.5), C('hem5', 7.0, 13.0), C('zipper14', 0.0, 3.0)],
     [at(6, 'A loose button'), at(6, 'a seam'), at(6, 'a hem'), at(6, 'a zip')], at(6, 'A needle') - 0.1)
one([(C('buttons10', 9.5, 20.0), at(6, 'A needle') - 0.2), (C('taperpants7', 0.0, 8.1), at(6, 'a local tailor'))], en(6) + 0.3)
tip('* a needle and thread,<br>or a local tailor *', at(6, 'A needle'), en(6) + 0.2)
# 7 "And some mean the fabric itself is worn. If you can see light through it where it rubs, or a hole keeps growing, no amount of care will make it look new again."
one([(C('sweaterwoman9', 0.0, 10.8), st(7) - 0.2)], en(7) + 0.3)
tip('* light through it?<br>a growing hole? *', at(7, 'If you can see'), en(7) + 0.2)
# 8 "So ask yourself one question. If this were fixed, would I reach for it every week? If yes, it's worth the effort.
#    If not, let it become something you wear at home, and make room for the pieces you truly love."
one([(C('closetaes32', 0.0, 9.0), st(8) - 0.2), (C('mirrorcheck2', 0.0, 6.9), at(8, 'If yes')),
     (C('sweaterwoman16', 0.0, 4.5), at(8, 'If not')), (C('closetaes1', 0.0, 13.5), at(8, 'make room'))], en(8) + 0.3)
tip('* would I reach for it<br>every week? *', at(8, 'If this'), at(8, 'If not') - 0.2)
tip('* if not, wear it at home *', at(8, 'If not'), en(8) + 0.2)

# ================= 2. The right tool for the fabric =================
cardg('2. The right tool for the fabric', 9, style='font-size:104px')
# 9 "Pilling is often what makes a good sweater look older than it is, and the tool you use matters more than you might think."
full([(C('depill45', 1.5, 1.5), st(9) - 0.2), (C('shaver8', 0.0, 9.0), at(9, 'and the tool'))], en(9) + 0.3)
# 10 "A lint roller is lovely for lint and hair, but it can't lift pills, the little balls of fibre that form where fabric rubs."
wrow([C('lintroller7', 0.0, 9.0), C('lintroller25', 2.4, 4.6)], [st(10), at(10, 'lint and hair')], at(10, 'but it') - 0.1)
one([(C('shaver25', 2.0, 7.7), at(10, 'but it') - 0.2)], en(10) + 0.3)
tip('* pills: little balls of fibre *', at(10, 'the little balls'), en(10) + 0.2)
# 11 "For pills, a fabric shaver with a guard is the safest choice for most sweaters. Lay the sweater flat on a table rather than
#     your bed, and glide the shaver over it gently, with very little pressure."
one([(C('shaver41', 5.0, 14.0), st(11) - 0.2), (C('shaver42', 0.0, 3.6), at(11, 'Lay the sweater')),
     (C('shaver36', 4.0, 19.0), at(11, 'glide the shaver'))], en(11) + 0.3)
tip('* a fabric shaver<br>with a guard *', at(11, 'a fabric shaver'), at(11, 'Lay the sweater') - 0.2)
tip('* flat, on a table *', at(11, 'Lay the sweater'), at(11, 'glide') - 0.2)
tip('* very little pressure *', at(11, 'glide'), en(11) + 0.2)
# 12 "A sweater comb can work too, used very gently. A razor might seem quicker, but one slip can leave a hole that no care will undo.
#     And if a knit is loose, delicate or fuzzy by design, try a small hidden area first."
one([(C('depill25', 0.0, 9.5), st(12) - 0.2), (C('depill37', 1.0, 6.2), at(12, 'A razor')),
     (C('depill25', 18.5, 26.0), at(12, 'And if a knit'))], en(12) + 0.3)
tip('* used very gently *', at(12, 'used very gently'), at(12, 'A razor') - 0.2)
tip('* try a hidden area first *', at(12, 'try a small'), en(12) + 0.2)
# 13 "Next time, turn your knits inside out before washing and skip the fabric softener, and the pills come back more slowly."
one([(C('darks1', 1.8, 8.5), st(13) - 0.2)], en(13) + 0.3)
tip('* inside out,<br>no fabric softener *', at(13, 'turn your knits'), en(13) + 0.2)

# ================= 3. Read the label, then steam or press =================
cardg('3. Read the label, then steam or press', 14, style='font-size:92px')
# 14 "Before you smooth anything with heat, find the little iron on the care label. One dot means a cool iron, two dots medium,
#     three dots hot. An iron crossed out means don't iron at all, and some labels show that steam shouldn't be used either."
wrow([C('carelabel0', 33.0, 38.5), C('carelabel9', 0.0, 2.4)], [st(14) + 0.2, at(14, 'care label')], at(14, 'One dot') - 0.1)
one([(C('ironing13', 0.0, 4.9), at(14, 'One dot') - 0.2), (C('ironing27', 0.0, 10.0), at(14, 'An iron crossed out'))], en(14) + 0.3)
tip('one dot: cool', at(14, 'One dot'), at(14, 'An iron crossed') - 0.2, y=330)
tip('two dots: medium', at(14, 'two dots'), at(14, 'An iron crossed') - 0.2, y=450)
tip('three dots: hot', at(14, 'three dots'), at(14, 'An iron crossed') - 0.2, y=570)
tip('* crossed out: no iron *', at(14, 'An iron crossed'), en(14) + 0.2)
# 15 "Then choose your method. Steam suits knits, dresses and blouses, anything soft you want to fall smoothly.
#     Hold the fabric gently taut, move slowly, and let it dry before you wear it."
scene(C('steamer2', 0.0, 3.6), st(15) - 0.2, at(15, 'knits') - 0.1)
row4([C('steamer9', 0.0, 9.0), C('steamer12', 0.0, 12.0), C('steamer45', 1.0, 16.0)], [at(15, 'knits'), at(15, 'dresses'), at(15, 'blouses')], at(15, 'Hold the fabric') - 0.1, w=520)
one([(C('steamer38', 0.0, 10.0), at(15, 'Hold the fabric') - 0.2), (C('steamer16', 20.0, 30.0), at(15, 'let it dry'))], en(15) + 0.3)
tip('* gently taut, move slowly *', at(15, 'Hold the fabric'), at(15, 'let it dry') - 0.2)
tip('* let it dry first *', at(15, 'let it dry'), en(15) + 0.2)
# 16 "Pressing suits a crisp cotton shirt or the crease of a trouser. Lower the iron, lift it, and move on, rather than sliding it back
#     and forth. On wool or dark trousers, put a thin cloth between the iron and the fabric. That's what prevents the shiny,
#     over-ironed look that makes trousers look older than they are."
scene(C('ironing41', 0.0, 12.0), st(16) - 0.2, at(16, 'Lower the iron') - 0.1)
one([(C('ironing24', 10.0, 18.0), at(16, 'Lower the iron') - 0.2), (C('ironing24', 0.5, 3.4), at(16, 'rather than sliding')),
     (C('ironing31', 0.0, 12.0), at(16, 'On wool')), (C('ironing31', 13.0, 24.0), at(16, "That's what"))], en(16) + 0.3)
tip('* lower, lift, move on *', at(16, 'Lower the iron'), at(16, 'On wool') - 0.2)
tip('* a thin cloth between<br>the iron and the fabric *', at(16, 'put a thin cloth'), en(16) + 0.2)
# 17 "And one thing people often miss. If there's a stain, deal with it first, because heat from an iron or a dryer can set it."
one([(C('darks17', 5.5, 9.4), st(17) - 0.2), (C('laundry0', 15.0, 21.8), at(17, 'deal with it'))], en(17) + 0.3)
tip('* stain first, then heat *', at(17, 'deal with it first'), en(17) + 0.2)

# ================= 4. Store and reshape your knits =================
cardg('4. Store and reshape your knits', 18, style='font-size:104px')
# 18 "A sweater left on a hanger slowly stretches. Its own weight pulls it down, and the hanger leaves little bumps at the shoulders,
#     wire hangers most of all. So fold your knits instead."
one([(C('hanger5', 0.0, 6.6), st(18) - 0.2), (C('hanger5', 4.4, 4.4), at(18, 'and the hanger')), (C('foldsweater27', 1.5, 12.7), at(18, 'So fold'))], en(18) + 0.3)
tip('* fold your knits *', at(18, 'So fold'), en(18) + 0.2)
# 19 "If a wool sweater has lost its shape at the cuffs or hem, check the care label, then dip just those areas in warm water,
#     around thirty to forty degrees Celsius, massage them gently, and dry the whole sweater flat, away from radiators and direct sun."
one([(C('reshape19', 6.0, 11.0), st(19) - 0.2), (C('dryflat1', 0.0, 4.8), at(19, 'dip just those')),
     (C('dryflat31', 0.0, 6.0), at(19, 'massage')), (C('dryflat12', 1.2, 7.0), at(19, 'dry the whole')),
     (C('dryflat1', 5.0, 15.0), at(19, 'away from'))], en(19) + 0.3)
tip('* warm water, 30-40 °C *', at(19, 'around thirty'), at(19, 'dry the whole') - 0.2)
tip('* dry it flat *', at(19, 'dry the whole'), en(19) + 0.2)
# 20 "Be honest about the limits, though. This works best on wool. A sweater that has shrunk and turned thick and matted is usually
#     very hard to bring back, and many synthetic knits stretched by heat don't fully recover. That's why folding and drying flat
#     from the start matter so much."
one([(C('sweaterwoman9', 11.0, 21.0), st(20) - 0.2), (C('dryflat30', 0.0, 5.2), at(20, 'many synthetic')),
     (C('foldsweater44', 3.0, 23.0), at(20, "That's why"))], en(20) + 0.3)
tip('* works best on wool *', at(20, 'This works best'), at(20, "That's why") - 0.2)
# 21 guide plug: "And if you'd like to know which colours, shapes and pieces suit you best, our personal stylist guide is linked
#     in the description. It will be sent instantly to your email."
scene(C('sweaterwoman30', 0.0, 13.0), st(21) - 0.2, en(21) + 0.6)
i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, at(21, 'our personal stylist'), 0.8); fade_out(i, en(21) + 0.6, 0.5)
text('Check the description for', 'gtx1', at(21, 'our personal stylist') + 0.5, en(21) + 0.55, dur=1.1)
text('Personal stylist guide', 'gtx2', at(21, 'our personal stylist') + 0.9, en(21) + 0.55, dur=1.6)

# ================= 5. Find out why the colour changed =================
cardg('5. Find out why the colour changed', 22, style='font-size:96px')
# 22 "When colour looks tired, find out why first, because each cause has a different answer."
one([(C('darks11', 0.0, 8.0), st(22) - 0.1)], en(22) + 0.3)
# 23 "If darks look dull or streaky, it may simply be too much detergent. Measure it, and use the amount on the container."
one([(C('detergent17', 0.0, 3.2), st(23) - 0.2), (C('laundry0', 1.5, 6.5), at(23, 'too much detergent')),
     (C('detergent4', 14.5, 20.0), at(23, 'use the amount'))], en(23) + 0.3)
tip('* measure it *', at(23, 'Measure it'), en(23) + 0.2)
# 24 "If whites have turned grey, it's often dirt passing from other clothes in the wash, or not enough detergent. Wash them on their
#     own and don't overfill the machine. If the care label allows bleach, an oxygen-based whitener can help, following its
#     instructions, and never on wool or silk."
wrow([C('laundry28', 0.0, 12.0), C('whites11', 0.0, 5.0)], [st(24), at(24, 'dirt passing')], at(24, 'Wash them') - 0.1)
one([(C('laundry13', 15.0, 30.0), at(24, 'Wash them') - 0.2), (C('detergent21', 0.5, 8.0), at(24, 'If the care label')),
     (C('clothesbrush11', 9.0, 15.0), at(24, 'never on wool'))], en(24) + 0.3)
tip("* don't overfill *", at(24, "don't overfill"), at(24, 'If the care label') - 0.2)
tip('* only if the label<br>allows bleach *', at(24, 'If the care label'), at(24, 'never on wool') - 0.2)
tip('* never on wool or silk *', at(24, 'never on wool'), en(24) + 0.2)
# 25 "If another colour has bled onto a piece, keep it out of the dryer. Rewash it on its own in cool water, and check the mark has
#     gone before it meets any heat."
one([(C('whites18', 2.0, 8.8), st(25) - 0.2), (C('laundry13', 3.0, 14.0), at(25, 'and check'))], en(25) + 0.3)
tip('* rewash in cool water *', at(25, 'Rewash'), en(25) + 0.2)
# 26 "And if a colour has truly faded, washing won't bring it back. Protect what's left by washing darks inside out, in cold water,
#     and skipping the dryer when you can. For a washable cotton or linen piece you love, a fabric dye can restore it, as long as
#     you follow the dye's instructions and accept the result can vary."
one([(C('darks14', 0.0, 7.6), st(26) - 0.2), (C('darks11', 10.5, 16.5), at(26, 'in cold water')),
     (C('laundry17', 0.0, 12.4), at(26, 'skipping the dryer')), (C('dye5', 3.1, 9.4), at(26, 'a fabric dye'))], en(26) + 0.3)
tip('* inside out, cold water *', at(26, 'inside out'), at(26, 'skipping') - 0.2)
tip('* skip the dryer *', at(26, 'skipping'), at(26, 'For a washable') - 0.2)
tip('* cotton or linen:<br>a fabric dye *', at(26, 'a fabric dye'), en(26) + 0.2)

# ================= 6. Make it fit you again =================
cardg('6. Make it fit you again', 27)
# 27 "Many pieces we stop wearing aren't worn out at all. They just don't fit the way we live now, or the body we have now.
#     And fit is what makes clothing look intentional on you."
scene(C('closetaes22', 0.0, 9.0), st(27) - 0.1, at(27, 'And fit') - 0.1)
scene(C('closetaes15', 0.0, 12.0), at(27, 'And fit') - 0.1, en(27) + 0.3)
# 28 "Some alterations make a big difference for very little. Hemming trousers so they skim your shoe, shortening sleeves, taking in
#     a loose waist, shortening a strap. For a hem, wear or bring the shoes you'll actually wear with them, so the length is right."
one([(C('taperpants34', 0.0, 7.0), st(28) - 0.2)], at(28, 'Hemming') - 0.1)
row4([C('hem5', 14.0, 21.0), C('reshape19', 0.5, 5.5), C('tailor32', 8.0, 22.0), C('fitting3', 2.0, 4.6)],
     [at(28, 'Hemming'), at(28, 'shortening sleeves'), at(28, 'taking in'), at(28, 'shortening a strap')], at(28, 'For a hem') - 0.1)
one([(C('tailor8', 6.6, 13.1), at(28, 'For a hem') - 0.2)], en(28) + 0.3)
tip('* bring the shoes you will wear *', at(28, 'wear or bring'), en(28) + 0.2, size=52)
# 29 "Others are harder. Changing the shoulders of a coat is complicated and costly, and letting something out depends on how much
#     spare fabric is hidden in the seams. Often there isn't much."
one([(C('taperpants36', 2.0, 14.0), st(29) - 0.2), (C('taperpants17', 4.0, 20.0), at(29, 'letting something out'))], en(29) + 0.3)
# 30 "So before you agree, ask whether the fabric is still in good condition, and whether the price is worth it for a piece you love.
#     A tailor can tell you what's possible first."
one([(C('fitting19', 0.0, 10.0), st(30) - 0.2), (C('taperpants24', 10.5, 16.0), at(30, 'A tailor can'))], en(30) + 0.3)
tip('* good fabric?<br>worth the price? *', at(30, 'ask whether'), at(30, 'A tailor') - 0.2)
tip('* ask a tailor first *', at(30, 'A tailor'), en(30) + 0.2)
# 31 "Even royal wardrobes work this way. At the 2023 BAFTAs, the Princess of Wales wore the white Alexander McQueen gown she'd first
#     worn there in 2019, now altered at the shoulder and paired with black opera gloves."  (photos on white, as the reference does)
scene(C('fitting3', 5.0, 9.0), st(31) - 0.2, at(31, 'At the 2023') - 0.3)
wrow([C('katebafta8', 0, 12), C('kate20198', 0, 12)], [at(31, 'At the 2023'), at(31, "she'd first")], at(31, 'now altered'))
wrow([C('katebafta29', 0, 12)], [at(31, 'now altered')], en(31) + 0.3, h=860)

# ================= 7. Replace what wears out first =================
cardg('7. Replace what wears out first', 32, style='font-size:104px')
# 32 "On most clothes and shoes, the same few parts wear out long before the rest. The buttons, the zip, and the heel. And because
#     they're the details people notice up close, renewing them makes the whole piece feel cared for again."
scene(C('cobbler36', 0.0, 8.2), st(32) - 0.1, at(32, 'The buttons') - 0.35)
wrow([C('replacebuttons30', 14.0, 20.0), C('zipper38', 0.0, 6.0), C('heeltip3', 0.0, 3.6)],
     [at(32, 'The buttons'), at(32, 'the zip'), at(32, 'the heel')], at(32, 'And because') - 0.1)
scene(C('sweaterwoman38', 8.0, 14.0), at(32, 'And because') - 0.2, en(32) + 0.3)
# 33 "If a button is missing or a few no longer match, replacing the whole set can make a coat or cardigan look new again. Horn, shell
#     or a good resin in a soft shade often looks more refined than basic plastic. Take the garment with you when you choose,
#     because buttons look different against the fabric."
one([(C('buttons3', 12.0, 16.5), st(33) - 0.2), (C('replacebuttons30', 2.0, 14.0), at(33, 'replacing the whole set')),
     (C('buttons3', 0.0, 6.4), at(33, 'Horn') - 0.2), (C('buttons3', 6.5, 10.5), at(33, 'Take the garment'))], en(33) + 0.3)
tip('* replace the whole set *', at(33, 'replacing the whole'), at(33, 'Horn') - 0.2)
tip('* horn, shell<br>or a good resin *', at(33, 'Horn'), at(33, 'Take the garment') - 0.2)
tip('* bring the garment *', at(33, 'Take the garment'), en(33) + 0.2)
# 34 "A broken zip doesn't have to be the end of a skirt or jacket either. If the fabric is good, a tailor can usually replace it."
one([(C('zipper14', 3.1, 7.5), st(34) - 0.2), (C('zipper30', 0.0, 10.0), at(34, 'If the fabric'))], en(34) + 0.3)
# 35 "And on shoes, watch the small tip at the bottom of the heel. Having a cobbler replace it early, before the wear reaches the heel
#     itself, is usually quick and far cheaper than waiting."
one([(C('heeltip3', 4.0, 9.5), st(35) - 0.2), (C('heeltip0', 5.0, 20.0), at(35, 'Having a cobbler')),
     (C('cobbler1', 2.0, 20.0), at(35, 'is usually quick'))], en(35) + 0.3)
tip('* the small tip<br>at the bottom of the heel *', at(35, 'the small tip'), at(35, 'Having') - 0.2)
tip('* replace it early *', at(35, 'Having'), en(35) + 0.2)

# ================= 8. Wear, air, then wash =================
cardg('8. Wear, air, then wash', 36)
# 36 "Every wash wears a piece a little, so washing less often is one of the kindest things you can do for your clothes."
scene(C('laundry4', 0.0, 10.0), st(36) - 0.1, en(36) + 0.3)
# 37 "Wool, especially, often just needs air. After you wear a coat or blazer, hang it on a wide, shaped hanger that supports the
#     shoulders, let it air, and brush it gently in the direction of the fabric. Save washing or dry cleaning for when it's truly
#     needed, and follow the care label."
scene(C('clothesbrush5', 1.5, 10.7), st(37) - 0.2, at(37, 'hang it on') - 0.1)
wrow([C('woodhanger33', 2.0, 12.0), C('woodhanger19', 8.5, 12.5)], [at(37, 'hang it on'), at(37, 'supports the shoulders')], at(37, 'let it air') - 0.1)
one([(C('airing4', 0.0, 8.2), at(37, 'let it air') - 0.2), (C('clothesbrush11', 0.0, 3.6), at(37, 'brush it gently')),
     (C('laundry40', 9.0, 17.5), at(37, 'Save washing'))], en(37) + 0.3)
tip('* let it air *', at(37, 'let it air'), at(37, 'brush it') - 0.2)
tip('* brush with the grain *', at(37, 'brush it'), at(37, 'Save washing') - 0.2)
tip('* wash only when needed *', at(37, 'Save washing'), en(37) + 0.2)
# 38 "And when your clothes last, you get to know them. They become the pieces people quietly associate with you."
scene(C('airing20', 0.0, 4.0), st(38) - 0.2, at(38, 'They become') - 0.1)
scene(C('sweaterwoman17', 0.0, 6.2), at(38, 'They become') - 0.1, en(38) + 0.6)

# ================= recap 39: one calm frame on the left, the checklist builds =================
# 39 "So, know what's worth saving, choose the right tool, read the label before heat, store and reshape your knits, find out why the
#     colour changed, make it fit, replace what wears out first, and wear, air, then wash."
stage([(C('mirrorcheck10', 0.0, 13.5), st(39) - 0.3)], en(39) + 0.5, x0=250)
items = ["know what's worth saving", 'choose the right tool', 'read the label before heat', 'store and reshape your knits',
         'find out why the colour changed', 'make it fit', 'replace what wears out first', 'wear, air, then wash']
cues = ["know what", 'choose the right', 'read the label', 'store and reshape', 'find out why', 'make it fit', 'replace what', 'wear, air']
for k, (txt, cue) in enumerate(zip(items, cues)):
    tt = at(39, cue) - 0.1; i = nid('ck')
    els.append(f'<div id="{i}" class="chk" style="top:{118 + k*104}px;opacity:0"><svg viewBox="0 0 54 54"><path id="{i}p" d="M12 28 L23 39 L42 15"/></svg>{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,x:-24}},{{opacity:1,x:0,duration:0.7,ease:"power2.out"}},{tt:.3f});')
    tw.append(f'tl.to("#{i}p",{{strokeDashoffset:0,duration:0.5,ease:"power2.out"}},{tt+0.3:.3f});')
    fade_out(i, en(39) + 0.5, 0.6)

# ================= close =================
# 40 "None of this needs a new wardrobe. It needs a little attention, and that attention is a gentle way of caring for yourself."
scene(C('sweaterwoman16', 5.0, 12.4), st(40) - 0.2, en(40) + 0.3)
# 41 "Which piece in your closet will you bring back first? Let us know in the comments."
scene(C('closetaes15', 13.0, 21.3), st(41) - 0.2, en(41) + 0.3)
# 42 "And if you found something helpful today, a simple like or comment would truly mean the world to us. You'll find the personal
#     stylist guide in the description. Until next time. Bye, my loves."   (reference outro: a calm window scene, then the end card)
scene(C('sweaterwoman38', 14.5, 20.0), st(42) - 0.2, at(42, "You'll find") - 0.1)
scene(C('sweaterwoman25', 0.0, 3.7), at(42, "You'll find") - 0.1, at(42, 'Until next time') - 0.1)
scene(C('windowmorning45', 0.0, 10.9), at(42, 'Until next time') - 0.1, total - 2.6)
i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, at(42, "You'll find"), 0.8); fade_out(i, at(42, 'Until next time'), 0.5)
text('Check the description for', 'gtx1', at(42, "You'll find") + 0.4, at(42, 'Until next time') - 0.1, dur=1.1)
text('Personal stylist guide', 'gtx2', at(42, "You'll find") + 0.8, at(42, 'Until next time') - 0.1, dur=1.6)
