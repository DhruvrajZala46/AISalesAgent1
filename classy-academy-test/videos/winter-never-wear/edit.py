# 8 Things Elegant Ladies Never Wear in Winter - the edit, beat by beat (Episode 15), v4 after the owner's review.
# Rebuilt from the channel's own videos, re-checked frame by frame on 29 Oct (restudy/*.jpg):
#   "8 Things Elegant Ladies Never Wear" (1.2M) and "7 Things Elegant Ladies Avoid in Fall" open on FULL-BLEED scenes:
#   the reel fills the frame edge to edge, a slow push-in, ~0.4 s dissolves between scenes. There is NO blurred copy behind
#   the opening scenes, so the blurred-canvas layout of v1-v3 is gone from the whole video.
#   Then: white "in today's video..." card -> "Episode N" + title in white script over a full-bleed scene -> per point:
#   white number card on the spoken "Number one..." -> the caramel backdrop with ONE centred reel (pictures change inside
#   it on the words) or rows of tall reels that grow in one per spoken item -> the principle as one line in white serif with
#   one word in script -> exit on a full-bleed scene -> white. Guide plug over a full-bleed scene. White end card + logo.
# Every visual is chosen for the exact words under it (STORYBOARD.md lists each one); footage segments come from ok.txt.
# Transitions (the owner flagged some as wrong): a scene that follows is drawn ON TOP and dissolves in, and the one before
#   stays until it is covered, so nothing ever dips through to the backdrop; caramel layouts follow a scene the way the
#   reference does (the scene dissolves to the backdrop while the reel grows from the centre).
# Sound: the voice, one soft piano bed ~12 dB under it, no sound effects; the film scenes are silent.
import re as _re
SB = []
def _log(kind, specs, t0, t1, move):
    SB.append(dict(kind=kind, clips=[[s[0], s[1], s[2]] for s in specs], t0=round(t0, 2), t1=round(t1, 2), move=move))
def _plain(s): return _re.sub(r'<[^>]+>', ' ', s).replace('  ', ' ').strip()

SEQ = []          # (t, kind, fn(t0, t1, prev_kind)) in time order; flush() gives each its end time from the next one
def add(t, kind, fn): SEQ.append((t, kind, fn))

def _bleed(spec, t0, t1, fin):
    v, h = vid(spec, t0, t1 + 0.5); drift(v, t0, t1 + 0.5, 1.045)
    i = box(0, 0, W, H, h); fade_in(i, t0, fin); fade_out(i, t1, 0.45); return i
def SC(spec, t, fin=0.4):
    """full-bleed scene (fills the frame, no blurred copy); spec = CB(key, a, b, fy)"""
    add(t, 'bleed', lambda t0, t1, pk: (_bleed(spec, t0, t1, 0.01 if t0 < 0.1 else fin), _log('full-bleed scene', [spec], t0, t1, 'dissolves in on top, slow push-in')))
def ONE(shots):
    """one centred reel on caramel; shots = [(C(...), t), ...] change inside the frame with a soft dissolve"""
    def fn(t0, t1, pk):
        stage(shots, t1, entry='fade' if pk == 'one' else 'centre')
        _log('one centred reel on caramel', [s for s, _ in shots], t0, t1, 'dissolves from the reel before' if pk == 'one' else 'grows from the centre')
    add(shots[0][1], 'one', fn)
def ROW(specs, times):
    def fn(t0, t1, pk):
        row(specs, times, t1); _log(f'row of {len(specs)} tall reels', specs, t0, t1, 'each grows from its corner on its word')
    add(times[0], 'row', fn)
def PAIR(specs, times):
    def fn(t0, t1, pk):
        pair(specs, times, t1); _log('two tall reels on caramel', specs, t0, t1, 'each grows from its corner on its word')
    add(times[0], 'row', fn)
def QUOTE(spec, t, l1, ta, l2, tb):
    """a reel on the left, the line to remember on the right (their 'Elegant style works with you' screens)"""
    def fn(t0, t1, pk):
        panel(spec, 170, 170 + PW, t0, t1, entry='fade'); text(l1, 'qs1', ta, t1, dur=1.4); text(l2, 'qs2', tb, t1, dur=1.2)
        _log('reel left + principle line', [spec], t0, t1, f'line wipes in: "{_plain(l1)} {_plain(l2)}"')
    add(t, 'quote', fn)
def CARD(txt, i, t_in=None, style=''):
    t = (en(i - 1) + 0.35) if t_in is None else t_in
    def fn(t0, t1, pk):
        white(t0, t1); text(txt, 'card', t0 + 0.3, t1 - 0.1, dur=1.2, out=0.45, style=style)
        _log('white number card', [], t0, t1, f'fade to white, black script wipes in: "{_plain(txt)}"')
    add(t, 'card', fn)
def flush(t_last):
    SEQ.sort(key=lambda s: s[0]); pk = None
    for k, (t, kind, fn) in enumerate(SEQ):
        if k + 1 < len(SEQ):
            nt, nk, _ = SEQ[k + 1]
            assert nt > t + 0.6, f'{kind} at {t:.2f} is followed too soon by {nk} at {nt:.2f}'
            t1 = nt + (0.45 if nk in ('bleed', 'card') else 0.5 if (nk == 'one' and kind == 'one') else 0.0)
        else: t1 = t_last
        fn(t, t1, pk); pk = kind
def GUIDE(t0, t1):
    i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, t0, 0.8); fade_out(i, t1, 0.5)
    text('Check the description for', 'gtx1', t0 + 0.5, t1 - 0.05, dur=1.1); text('Personal Stylist Guide', 'gtx2', t0 + 0.9, t1 - 0.05, dur=1.6)
    _log('guide text over the scene', [], t0, t1, 'haze, "Check the description for / Personal Stylist Guide"')
TWO = 'font-size:96px;line-height:1.3;text-align:center'
CROP['flw5'] = (62, 0, 1060)              # the burned-in "Little Women (1994)" caption stays out of frame

# ================= HOOK: full-bleed scenes, cut on the words =================
# 1 "Have you ever seen a woman on a freezing winter day, walking calmly down the street in a long wool coat, a soft scarf,
#    beautiful gloves, and thought, 'How does she look so elegant... when I just look cold?'"
SC(CB('f80winter6', 0.0, 8.4, 0.6), 0.0)
SC(CB('coatwalk11', 0.0, 6.0, 0.2), at(1, 'walking calmly') - 0.15)
SC(CB('scarfwrap2', 13.0, 21.7, 0.3), at(1, 'a soft scarf') - 0.1)
SC(CB('gloves12', 0.0, 6.0, 0.55), at(1, 'beautiful gloves') - 0.1)
SC(CB('commute37', 0.0, 8.0, 0.28), at(1, 'and thought') - 0.1)
SC(CB('snowcoat9', 0.0, 5.5, 0.3), at(1, 'when I just') - 0.1)
# 2 "She isn't shivering. She isn't buried under ten layers. And yet she looks polished, warm, and completely at ease."
SC(CB('coatwalk17', 0.0, 6.3, 0.3), st(2) - 0.1)
SC(CB('longcoat8', 0.0, 6.0, 0.3), at(2, "She isn't buried") - 0.1)
SC(CB('phonecoffee11', 0.0, 10.0, 0.3), at(2, 'And yet') - 0.1)
# 3 "That kind of elegance isn't accidental. And the secret, it's often not about how much she's wearing,
#    it's about what she knows not to wear."
SC(CB('coatwalk36', 0.0, 6.8, 0.3), st(3) - 0.1)
SC(CB('grabknit11', 0.0, 5.5, 0.3), at(3, 'how much') - 0.1)
SC(CB('opendoor4', 0.0, 10.0, 0.45), at(3, "it's about what") - 0.1)
# 4 "Welcome to The Classy Elegance. I'm so glad you're here. And if you've been with us for a while, yes, we have a new
#    name. Same channel, same timeless style, just a new chapter."
SC(CB('oldwinter19', 0.0, 10.1, 0.3), st(4) - 0.1)
SC(CB('phonecoffee15', 0.0, 3.95, 0.35), at(4, "I'm so glad") - 0.1)
SC(CB('wintercafe6', 0.0, 5.7, 0.35), at(4, "And if you've") - 0.1)
def _newname(t0, t1, pk):          # "yes, we have a new name": the new name's monogram on white (the end card's look)
    white(t0, t1); j = nid('nn'); els.append(f'<img id="{j}" class="endlogo" src="assets/logo_ce_dark.png" style="opacity:0">')
    tw.append(f'tl.fromTo("#{j}",{{opacity:0,scale:0.96}},{{opacity:1,scale:1,duration:1.0,ease:"power2.out"}},{t0 + 0.3:.3f});'); fade_out(j, t1 - 0.05, 0.45)
    _log('white card with the new monogram', [], t0, t1, 'fade to white, the CE monogram fades up')
add(at(4, 'yes, we have') - 0.2, 'card', _newname)
ROW([C('gloves8', 0.0, 9.0), C('coatwalk43', 0.0, 5.5), C('commute26', 0.0, 6.0)],
    [at(4, 'Same channel'), at(4, 'same timeless'), at(4, 'just a new')])
# 5 "In today's video, we're uncovering eight things elegant women never wear in winter and the smarter swaps that keep
#    you warmer and look far more expensive."
def _today(t0, t1, pk):
    white(t0, t1); text("in today's video...", 'card', t0 + 0.3, t1 - 0.1, dur=1.0, out=0.4)
    _log('white card', [], t0, t1, 'black script wipes in: "in today\'s video..."')
add(en(4) + 0.4, 'card', _today)
SC(CB('snowparis0', 0.0, 8.3, 0.3), st(5) + 1.5)
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Episode 15</div><div class="big" style="font-size:86px">8 Things Elegant Ladies Never Wear in Winter</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.2,ease:"power2.out"}},{st(5)+1.9:.3f});'); fade_out(i, at(5, 'and the smarter') - 0.1, 0.5)
_log('title over the scene', [], st(5) + 1.9, at(5, 'and the smarter'), '"Episode 15" serif + title in white script, fades up 1.2 s')
ROW([C('merinotop45', 0.0, 14.0), C('snowcoat45', 0.0, 4.4), C('gloves44', 13.0, 19.0)],
    [at(5, 'and the smarter'), at(5, 'keep you warmer'), at(5, 'more expensive')])
# 6 "Some of these may surprise you, because a few of the pieces we reach for to stay warm can actually leave us colder.
#    But once you see them, you'll never unsee them. Let's get started."
ONE([(C('snowcoat33', 0.0, 8.5), st(6) - 0.05), (C('grabknit10', 0.0, 3.2), at(6, 'the pieces we reach')),
     (C('coverears3', 0.0, 4.4), at(6, 'can actually leave'))])
SC(CB('mirrorcoat7', 0.0, 6.6, 0.25), at(6, 'But once') - 0.1)
SC(CB('commute10', 0.0, 4.4, 0.3), at(6, "Let's get started") - 0.1)

# ================= 1. A chunky sweater squeezed under a fitted coat =================
CARD('1. A chunky sweater squeezed under a fitted coat', 7, style='font-size:90px')
# 8 "We've all done this. It's freezing, so you grab your thickest knit, pull your coat over the top, and suddenly you
#    can barely bend your arms. It feels like the warmest choice."
ONE([(C('coldhands39', 7.0, 9.5), en(7) + 0.3), (C('coldhands39', 10.0, 14.9), at(8, "It's freezing"))])
ROW([C('grabknit39', 15.0, 24.0), C('grabknit46', 4.0, 11.0), C('mirrorcoat11', 4.0, 11.0)],
    [at(8, 'so you grab'), at(8, 'pull your coat'), at(8, 'and suddenly')])
ONE([(C('pullsweater1', 0.0, 6.5), at(8, 'It feels like') - 0.1)])
# 9 "But here's what most people don't realize. What keeps you warm isn't really the fabric itself. It's the still air
#    trapped inside it."
ONE([(C('chunky34', 5.5, 8.3), st(9) - 0.05), (C('merino0', 7.5, 14.0), at(9, 'What keeps'))])
QUOTE(C('merino29', 0.0, 8.7), at(9, "It's the still") - 0.1, "It's the still <i>air</i>", at(9, "It's the still") + 0.2, 'trapped inside it', at(9, 'trapped'))
# 10 "When a thick sweater is pressed tight against the inside of a coat, both get squashed, and that warm pocket of air
#     gets squeezed out."
ONE([(C('undercoat20', 0.0, 4.5), st(10) - 0.05), (C('undercoat20', 4.6, 11.7), at(10, 'both get squashed')),
     (C('coattry3', 0.0, 8.2), at(10, 'and that warm'))])
# 11 "So you look bulkier, your coat pulls across the shoulders and buttons, and you're often not as warm as you'd expect."
ROW([C('stiffarms14', 4.0, 13.0), C('mirrorcoat3', 8.5, 17.5), C('snowcoat34', 0.0, 2.9)],
    [st(11), at(11, 'your coat pulls'), at(11, "and you're often")])
# 12 "Instead, try a fine merino or cashmere knit under your coat. It's thin, but it holds warmth beautifully without the bulk."
ONE([(C('merinotop35', 0.0, 6.0), st(12) - 0.05), (C('longcoat14', 14.0, 22.5), at(12, 'under your coat'))])
PAIR([C('merinotop17', 0.0, 10.0), C('merino13', 0.0, 7.7)], [at(12, "It's thin"), at(12, 'holds warmth')])
# 13 "And if you love your chunky cable knit, and honestly, who doesn't, let it be the star. Wear it on its own on milder
#     days or under a coat cut roomy enough to fit over it."
ONE([(C('chunky12', 12.5, 21.7), st(13) - 0.05), (C('chunky14', 0.0, 8.3), at(13, 'Wear it on')),
     (C('coattry12', 0.0, 10.0), at(13, 'or under a coat'))])
# 14 "When you shop for a coat, try it on over the thickest sweater you plan to wear. If you can lift your arms and button it
#     without pulling, that's the one. So chic."
ONE([(C('woolcare23', 0.0, 6.0), st(14) - 0.05), (C('mirrorcoat11', 12.0, 24.0), at(14, 'try it on')),
     (C('stiffarms25', 3.0, 13.4), at(14, 'If you can lift')), (C('mirrorcoat23', 0.0, 4.8), at(14, "that's the one") - 0.1)])

# ================= 2. Cotton next to your skin =================
CARD('2. Cotton next to your skin<br>on busy, rushing around days', 15, style=TWO)
# 16 "Cotton is lovely. Soft, breathable, easy. But in winter, there's one situation where it quietly works against you."
ROW([C('label28', 0.0, 6.0), C('label23', 14.0, 19.5), C('cottonshirt34', 0.0, 3.5)],
    [en(15) + 0.3, at(16, 'Soft'), at(16, 'easy')])
SC(CB('commute25', 0.0, 6.5, 0.3), at(16, 'But in winter') - 0.1)
# 17 "Cotton soaks up moisture and dries slowly, and once it's damp, it loses much of its ability to keep you warm. And that
#     moisture doesn't only come from the rain."
ONE([(C('wetfabric0', 0.0, 12.0), st(17) - 0.05), (C('coverears14', 0.0, 16.7), at(17, 'it loses much'))])
SC(CB('commute9', 0.0, 5.9, 0.3), at(17, 'And that moisture') - 0.1)
# 18 "Think about a typical winter day. You hurry to the train, walk briskly in your coat, step into a heated shop or office,
#     and you start to warm up."
SC(CB('snowcoat17', 0.0, 3.6, 0.5), st(18) - 0.1)
ROW([C('commute26', 6.0, 11.7), C('hikewinter31', 0.0, 6.0), C('heels16', 8.6, 10.7)],
    [at(18, 'You hurry'), at(18, 'walk briskly'), at(18, 'step into a heated')])
ONE([(C('commute35', 22.0, 31.0), at(18, 'and you start') - 0.1)])
# 19 "Your cotton tee absorbs that little bit of sweat and holds on to it. Then you step back outside, and suddenly you feel
#     colder than when you left the house. Sound familiar?"
ONE([(C('silklayer17', 7.5, 11.6), st(19) - 0.05), (C('wetfabric0', 13.0, 25.0), at(19, 'and holds on'))])
SC(CB('opendoor12', 0.0, 4.5, 0.3), at(19, 'Then you step') - 0.1)
SC(CB('snowcoat9', 6.0, 15.5, 0.3), at(19, 'and suddenly') - 0.1)
SC(CB('snowcoat45', 4.5, 9.0, 0.3), at(19, 'Sound familiar') - 0.1)
# 20 "Instead, choose a base layer that handles moisture better. Merino wool is a beautiful option."
ONE([(C('thermaltop11', 0.0, 8.0), st(20) - 0.05), (C('merino22', 0.0, 4.6), at(20, 'Merino wool'))])
# 21 "Wool can absorb around a third of its weight in moisture vapor before it even starts to feel wet, so it stays
#     comfortable as you move between the cold street and a warm room."
QUOTE(C('merino2', 0.0, 7.1), st(21) - 0.1, 'Wool can absorb', st(21) + 0.3, 'around <i>a third</i> of its weight', at(21, 'around a third'))
PAIR([C('commute14', 2.8, 11.3), C('cozyhome42', 0.0, 12.9)], [at(21, 'as you move'), at(21, 'a warm room')])
# 22 "A thin silk layer or a good synthetic thermal works well, too, and dries quickly."
PAIR([C('silkcami35', 0.0, 9.0), C('thermaltop9', 1.5, 8.5)], [st(22) - 0.05, at(22, 'or a good synthetic')])
# 23 "And here's a little trick hikers swear by. Dress for how you'll feel 10 minutes into your walk, not the moment you
#     open the door."
SC(CB('hikewinter31', 6.0, 13.7, 0.3), st(23) - 0.1)
QUOTE(C('snowcoat14', 0.0, 16.0), at(23, 'Dress for how') - 0.1, "Dress for how you'll feel", at(23, 'Dress for how') + 0.2, '<i>10 minutes</i> into your walk', at(23, '10 minutes'))
ONE([(C('opendoor0', 0.0, 9.2), at(23, 'not the moment') - 0.1)])
# 24 "Now, this doesn't mean cotton is off limits. On a dry day when you're mostly indoors, your favorite cotton shirt is
#     perfectly fine. It's the damp, active, in-and-out days where it lets you down."
ONE([(C('label28', 7.0, 16.7), st(24) - 0.05), (C('cottonshirt34', 5.5, 9.5), at(24, 'On a dry day')),
     (C('cottonshirt31', 0.0, 4.5), at(24, 'your favorite cotton'))])
ROW([C('commute25', 7.0, 13.1), C('commute35', 10.0, 15.5), C('heels16', 5.0, 8.4)],
    [at(24, "It's the damp") - 0.1, at(24, 'active'), at(24, 'in-and-out')])

# ================= 3. The cozy acrylic sweater =================
CARD('3. The cozy acrylic sweater', 25)
# 26 "It looks soft on the hanger, it's often a fraction of the price, and it feels warm the moment you put it on."
ONE([(C('pricetag38', 0.0, 9.3), en(25) + 0.3), (C('pricetag3', 6.5, 9.0), at(26, "it's often")),
     (C('acrylic38', 0.5, 4.5), at(26, 'and it feels warm'))])
# 27 "But acrylic absorbs very little moisture. So when you go from the cold outside into a heated room, the warmth and
#     moisture your body gives off has nowhere to go. That's why some acrylic knits feel toasty one minute and strangely
#     clammy the next."
ONE([(C('wetfabric34', 1.0, 10.0), st(27) - 0.05)])
PAIR([C('snowcoat8', 0.0, 9.8), C('cozyhome37', 0.0, 10.5)], [at(27, 'the cold outside'), at(27, 'into a heated room')])
QUOTE(C('acrylic38', 5.5, 11.0), at(27, "That's why") - 0.1, '<i>toasty</i> one minute', at(27, 'feel toasty'), 'and strangely clammy the next', at(27, 'and strangely'))
# 28 "And many acrylic sweaters pill quickly. Those little fuzzy balls that appear under the arms and along the sides after
#     just a few wears."
ONE([(C('acrylic18', 0.0, 12.0), st(28) - 0.05)])
PAIR([C('acrylic18', 28.0, 34.0), C('acrylic8', 0.0, 3.5)], [at(28, 'under the arms'), at(28, 'along the sides')])
# 29 "And as we've said before on this channel, nothing takes away from an elegant look faster than clothing that looks worn down."
SC(CB('coatfabric10', 13.0, 20.0, 0.3), st(29) - 0.1)
ONE([(C('acrylic18', 12.5, 19.0), at(29, 'faster than'))])
# 30 "Instead, flip to the label before you buy. Look for wool, merino, cashmere, or a wool-rich blend."
ONE([(C('careabel27', 1.0, 5.0), st(30) - 0.05)])
ROW([C('merino2', 7.2, 11.2), C('merinotop30', 0.0, 11.0), C('careabel6', 5.3, 8.0)],
    [at(30, 'Look for wool'), at(30, 'cashmere'), at(30, 'wool-rich blend')])
# 31 "Then give the knit a gentle stretch. A quality knit feels dense and springs right back into shape. If it stays
#     stretched out or you can see straight through it, put it back."
ONE([(C('knitstretch10', 0.0, 8.0), st(31) - 0.05), (C('knitstretch10', 10.0, 20.0), at(31, 'A quality knit')),
     (C('fabriclight3', 0.0, 5.8), at(31, 'see straight through'))])
# 32 "Now, a little acrylic in a blend isn't a bad thing. It can make a sweater more affordable and easier to care for.
#     Just let it be the supporting fiber, not the whole sweater."
ONE([(C('knitstretch6', 0.0, 9.0), st(32) - 0.05), (C('pricetag16', 0.0, 7.0), at(32, 'It can make')),
     (C('washknit12', 0.0, 5.0), at(32, 'and easier to care')), (C('label18', 8.0, 10.5), at(32, 'Just let it')),
     (C('sleeves49', 0.0, 14.5), at(32, 'not the whole'))])
# 33 "And washing your knits inside out on a gentle cycle helps them stay smooth for so much longer."
ONE([(C('knitstretch28', 0.0, 15.0), st(33) - 0.05), (C('washknit12', 5.2, 8.5), at(33, 'on a gentle')),
     (C('insideout39', 0.0, 14.0), at(33, 'helps them'))])
# 34 "And here's a secret many well-dressed women don't share. They know exactly what flatters them. The colors that make
#     their skin glow in that soft winter light and the coat shapes that complement their figure."
SC(CB('coatwalk3', 4.5, 10.4, 0.3), st(34) - 0.1)
ONE([(C('winterlook29', 0.0, 10.3), at(34, 'They know exactly'))])
PAIR([C('beret12', 0.0, 8.2), C('coatlabel14', 0.0, 10.0)], [at(34, 'The colors'), at(34, 'and the coat shapes')])
# 35 guide plug: "If you'd like to discover what suits you best ... our personal stylist guide is linked in the description.
#     It's sent instantly to your email after access. Now, let's continue."
SC(CB('winterlook33', 0.0, 11.1, 0.1), st(35) - 0.1)
SC(CB('gloves8', 20.0, 29.3, 0.3), at(35, 'our personal stylist'))
GUIDE(at(35, 'our personal stylist') + 0.1, at(35, "Now, let's") - 0.05)
SC(CB('coatwalk4', 13.3, 16.5, 0.3), at(35, "Now, let's"))

# ================= 4. Boots that fit perfectly in October =================
CARD('4. Boots that fit perfectly in October', 36)
# 37 "You buy them in early fall, wear them with thin socks, and they fit like a dream. Then winter arrives, you add your
#     thickest socks, and suddenly they're snug across the toes."
ONE([(C('boots41', 0.0, 9.0), en(36) + 0.3), (C('heels0', 0.0, 8.0), at(37, 'wear them with'))])
SC(CB('flw7', 0.0, 7.0, 0.5), at(37, 'Then winter') - 0.1)
PAIR([C('socks18', 0.0, 5.0), C('boots2', 0.0, 5.4)], [at(37, 'you add your'), at(37, 'and suddenly')])
# 38 "It feels like you've just made them warmer, but often it's the opposite. When your boots are too tight, they squeeze
#     your feet, and that can restrict the blood flow that keeps your toes warm."
ONE([(C('socks12', 3.5, 9.9), st(38) - 0.05), (C('boots23', 0.0, 9.0), at(38, 'When your boots'))])
# 39 "The tightness also crushes the insulation in your socks and in the boot itself. So the thickest sock in a tight boot
#     can leave you with colder feet than a thinner sock with a little room."
ONE([(C('socks6', 9.0, 12.5), st(39) - 0.05), (C('boots41', 14.5, 24.0), at(39, 'and in the boot')), (C('socks18', 5.5, 9.8), at(39, 'So the thickest')),
     (C('socks13', 2.0, 5.0), at(39, 'than a thinner'))])
# 40 "Instead, aim for enough space to wiggle your toes freely while your heel stays snugly in place. A fine merino sock
#     gives you warmth without the bulk."
ONE([(C('boots16', 0.0, 8.0), st(40) - 0.05), (C('socks12', 0.0, 3.4), at(40, 'without the bulk'))])
# 41 "And when you shop for winter boots, try them on in the afternoon, wearing the socks you'll actually wear with them."
ONE([(C('boots7', 2.0, 12.0), st(41) - 0.05), (C('boots16', 8.0, 14.0), at(41, 'try them on')),
     (C('socks6', 12.6, 16.0), at(41, 'wearing the socks'))])
# 42 "Of course, you don't want boots that are too loose either. If your foot slides around, cold air moves around inside
#     with it. The goal is room for your toes and support for your heel."
ONE([(C('heels38', 3.0, 6.4), st(42) - 0.05), (C('slipice10', 0.0, 4.6), at(42, 'If your foot'))])
QUOTE(C('boots7', 12.5, 21.0), at(42, 'The goal is') - 0.1, 'room for your <i>toes</i>', at(42, 'room for your'), 'and support for your heel', at(42, 'and support'))

# ================= 5. Smooth soles on icy days =================
CARD('5. Smooth soles on icy days', 43)
# 44 "There's nothing more elegant than a sleek leather boot or a pointed-toe heel with a long coat. But on ice, a smooth sole
#     has almost nothing to grip with. And no outfit looks graceful while you're tiptoeing down the pavement or worse, slipping."
SC(CB('heels17', 0.0, 6.5, 0.75), en(43) + 0.3)
SC(CB('slipice19', 0.0, 6.2, 0.6), at(44, 'or a pointed-toe') - 0.1)
ONE([(C('icy1', 0.0, 4.6), at(44, 'But on ice')), (C('icy20', 0.0, 2.0), at(44, 'nothing to grip')),
     (C('slipice46', 0.0, 10.5), at(44, 'And no outfit')), (C('slipice1', 0.0, 6.1), at(44, "you're tiptoeing"))])
# 45 "Here's something that surprised me. Researchers at Toronto's WinterLab tested nearly a hundred types of winter footwear
#     on ice, and fewer than one in 10 met their minimum standard for grip."
SC(CB('snowcoat17', 8.0, 16.6, 0.5), st(45) - 0.1)
ONE([(C('boots7', 21.0, 33.0), at(45, 'Researchers'))])
QUOTE(C('icy1', 4.7, 9.0), at(45, 'and fewer') - 0.1, 'fewer than <i>one in 10</i>', at(45, 'and fewer'), 'met their minimum standard for grip', at(45, 'met their'))
# 46 "The ones that performed best had special soles with tiny grit-like particles built right into the rubber. So even a
#     boot sold as a winter boot isn't automatically safe on ice."
ONE([(C('treadboots1', 0.0, 6.8), st(46) - 0.05), (C('boots41', 9.2, 14.3), at(46, 'sold as a'))])
# 47 "Instead, keep one pair with a deeply treaded rubber sole for icy mornings. Many now come in sleek black or brown
#     leather that look just as polished."
ONE([(C('treadboots14', 0.0, 6.5), st(47) - 0.05)])
PAIR([C('treadboots14', 7.0, 12.9), C('cobbler2_13', 17.0, 26.0)], [at(47, 'Many now come'), at(47, 'or brown leather')])
# 48 "You can also ask a cobbler to add a thin rubber sole protector to your favorite leather-soled shoes. It's affordable and adds grip."
ONE([(C('cobbler2_22', 0.4, 6.25), st(48) - 0.05), (C('cobbler2_13', 0.0, 14.0), at(48, "It's affordable") - 0.25)])
# 49 "And for truly icy days, a pair of slip-on ice grips can live in your bag and come off the moment you arrive."
SC(CB('icegrips3', 9.8, 12.5, 0.5), st(49) - 0.1)
ONE([(C('gripsbag2', 0.3, 2.3), at(49, 'a pair of slip-on')), (C('icegrips0', 0.0, 1.95), at(49, 'can live in')),
     (C('opendoor48', 8.0, 13.7), at(49, 'and come off'))])
# 50 "Now, on dry, cleared pavement, wear your elegant soles and enjoy them. It's simply about knowing which days call for something more."
SC(CB('heels0', 8.2, 21.0, 0.45), st(50) - 0.1)
SC(CB('phonecoffee32', 4.5, 9.4, 0.3), at(50, "It's simply") - 0.1)

# ================= 6. Thin, unlined leather gloves =================
CARD('6. Thin, unlined leather gloves', 51)
# 52 "Leather gloves are a winter classic and for good reason. They're timeless, sleek, and they finish a coat beautifully."
ONE([(C('gloves15', 0.0, 6.5), en(51) + 0.3)])
ROW([C('gloves25', 0.0, 7.0), C('gloves44', 5.0, 12.0), C('gloves22', 0.0, 12.0)],
    [at(52, "They're timeless"), at(52, 'sleek'), at(52, 'and they finish')])
# 53 "But a very thin, unlined pair on a freezing, windy day leaves just a fine layer of leather between your fingers and the cold."
ONE([(C('gloves31', 0.0, 5.8), st(53) - 0.05)])
SC(CB('windycoat41', 2.0, 7.6, 0.68), at(53, 'on a freezing') - 0.1)
ONE([(C('coldhands5', 0.0, 9.0), at(53, 'leaves just'))])
# 54 "And when your hands are cold, you tense up. Your shoulders rise, you rush, you hide your hands in your sleeves. Not
#     exactly the calm, composed presence we're going for."
ONE([(C('coverears15', 0.0, 8.0), st(54) - 0.05), (C('commute13', 0.0, 5.5), at(54, 'Your shoulders rise')),
     (C('sleeves3', 0.0, 6.7), at(54, 'you hide your'))])
QUOTE(C('coatwalk11', 6.0, 15.2), at(54, 'Not exactly') - 0.1, 'the calm,', at(54, 'the calm'), '<i>composed</i> presence', at(54, 'composed'))
# 55 "Instead, look for leather gloves lined in cashmere, wool, or fleece. They keep the same slim, elegant shape with far more warmth inside."
ONE([(C('gloves12', 12.5, 21.2), st(55) - 0.05)])
PAIR([C('gloves31', 6.2, 12.4), C('gloves25', 8.0, 16.1)], [at(55, 'They keep'), at(55, 'far more warmth')])
# 56 "And on the coldest days, consider mittens. When they're made from the same materials, mittens are warmer than gloves
#     because your fingers share their warmth instead of each one facing the cold on its own."
ONE([(C('mittens0', 0.0, 5.2), st(56) - 0.05)])
PAIR([C('mittens40', 0.0, 14.0), C('mittens5', 12.0, 20.2)], [at(56, "When they're made"), at(56, 'because your fingers')])
# 57 "A soft lined leather or knit mitten looks incredibly chic with a long wool coat. And if you need your fingers free, a
#     thin liner glove underneath a mitten gives you the best of both."
ONE([(C('mittens40', 15.0, 27.0), st(57) - 0.05), (C('scarfwrap48', 14.5, 20.2), at(57, 'with a long wool')),
     (C('mittens1', 0.0, 11.7), at(57, 'And if you need'))])

# ================= 7. Nothing on your head =================
CARD("7. Nothing on your head because<br>you don't want to ruin your hair", 58, style=TWO)
# 59 "I completely understand this one. You've done a beautiful blowout, and the last thing you want is hat hair."
ONE([(C('blowdry29', 4.0, 8.7), en(58) + 0.3), (C('blowdry3', 5.5, 12.9), at(59, "You've done")),
     (C('hathair4', 0.0, 9.0), at(59, 'and the last thing'))])
# 60 "And you may have heard that we lose most of our body heat through our heads. That's actually a myth."
ONE([(C('hathair7', 9.0, 20.0), st(60) - 0.05)])
QUOTE(C('blowout4', 0.0, 6.5), at(60, "That's actually") - 0.1, "That's actually", at(60, "That's actually"), 'a <i>myth</i>.', at(60, 'a myth'))
# 61 "Researchers writing in the British Medical Journal traced it back to a flawed interpretation of an old military
#     experiment. Your head loses heat much like any other uncovered part of your body."
SC(CB('readpaper3', 0.0, 6.9, 0.35), st(61) - 0.1)
SC(CB('readpaper4', 0.0, 7.4, 0.5), at(61, 'traced it back') - 0.1)
SC(CB('snowwalk23', 0.0, 8.8, 0.25), at(61, 'Your head loses') - 0.1)
# 62 "But here's what does matter. Your ears are one of the areas most vulnerable to frostbite, along with your fingers,
#     toes, nose, cheeks, and chin. And on a windy day, cold, stinging ears can make you miserable in minutes."
ONE([(C('earmuff1', 0.0, 5.2), st(62) - 0.05), (C('earmuff23', 0.0, 10.8), at(62, 'Your ears')),
     (C('scarfwrap3', 0.0, 4.5), at(62, 'along with your'))])
SC(CB('coverears16', 0.0, 9.3, 0.15), at(62, 'And on a windy') - 0.1)
# 63 "So instead of skipping it altogether, choose something that protects your ears and your hairstyle."
ONE([(C('snowparis41', 0.0, 8.0), st(63) - 0.05)])
# 64 "A wide knit or cashmere headband keeps your ears covered and looks beautiful with a sleek low bun or a soft blowout."
PAIR([C('headband5', 0.95, 5.2), C('headband12', 2.5, 8.8)], [st(64) - 0.05, at(64, 'cashmere headband')])
PAIR([C('winterbun28', 0.0, 12.4), C('blowout12', 28.0, 38.0)], [at(64, 'with a sleek'), at(64, 'or a soft blowout')])
# 65 "A wool beret is timeless and effortlessly chic. And if you love a beanie, choose a fine merino or cashmere one rather
#     than a stiff, heavy knit. Just make sure your hair is completely dry before you put it on. So pretty."
ROW([C('snowparis29', 0.0, 6.0), C('beret3', 0.0, 3.5), C('beret15', 3.0, 5.8)],
    [st(65) - 0.05, at(65, 'is timeless'), at(65, 'effortlessly chic')])
ONE([(C('beanie5', 0.3, 4.6), at(65, 'And if you love') - 0.1), (C('snowparis3', 0.0, 8.0), at(65, 'rather than')),
     (C('blowdry12', 21.0, 33.0), at(65, 'Just make sure')), (C('hathair7', 20.0, 32.0), at(65, 'before you put'))])
SC(CB('beret16', 0.0, 6.5, 0.3), at(65, 'So pretty') - 0.1)

# ================= 8. The coat that only looks warm =================
# 66 "Saving one of my favorites for last. Number eight, the coat that only looks warm."
SC(CB('longcoat37', 2.0, 5.8, 0.3), st(66) - 0.1)
CARD('8. The coat that only looks warm', 66, t_in=at(66, 'Number eight') - 0.35)
# 67 "Your coat is often the first thing people notice in winter, and it's the piece doing most of the work to keep you warm."
SC(CB('longcoat8', 6.0, 11.6, 0.3), en(66) + 0.3)
ONE([(C('longcoat19', 12.0, 20.0), at(67, "and it's the piece"))])
# 68 "But two coats can look almost identical on the hanger and feel completely different on a windy street. The difference is often the fabric."
PAIR([C('woolcare10', 2.0, 9.5), C('windycoat27', 0.0, 9.0)], [st(68) - 0.05, at(68, 'and feel completely')])
ONE([(C('coatfabric21', 0.0, 8.0), at(68, 'The difference') - 0.1)])
# 69 "A loosely woven coat can let the wind cut straight through it, no matter how thick it looks. Dense, tightly woven, or
#     felted wool fabrics like melton or boiled wool hold up far better against the wind, and they keep their shape
#     beautifully year after year."
ONE([(C('coatfabric2', 0.0, 6.5), st(69) - 0.05)])
SC(CB('windycoat43', 25.5, 30.5, 0.3), at(69, 'no matter how') - 0.1)
PAIR([C('coatfabric21', 8.5, 19.5), C('coatweave40', 0.0, 6.0)], [at(69, 'Dense'), at(69, 'like melton')])
ONE([(C('longcoat19', 20.0, 28.9), at(69, 'hold up far') - 0.1)])
# 70 "Before you buy, check the label. A high wool content is what you're looking for. And a small amount of nylon or
#     polyester is perfectly fine. It can actually make a coat more durable."
ONE([(C('coatlabel24', 0.1, 2.45), st(70) + 0.3), (C('coatweave40', 6.2, 11.7), at(70, 'A high wool'))])
PAIR([C('coatweave13', 0.0, 9.0), C('coatweave4', 4.5, 12.2)], [at(70, 'And a small'), at(70, 'It can actually')])
# 71 "Then try this simple test. Hold the fabric up to a window or a bright light. If light shines easily through the weave,
#     chances are the wind will, too."
ONE([(C('coatfabric15', 0.0, 9.4), st(71) - 0.05), (C('fabriclight0', 0.0, 10.0), at(71, 'Hold the fabric')),
     (C('fabriclight18', 8.5, 12.5), at(71, 'If light shines'))])
SC(CB('windycoat37', 0.0, 4.1, 0.3), at(71, 'chances are') - 0.1)
# 72 "And finally, look at the length. On truly cold, windy days, a coat that covers your hips and upper thighs protects far
#     more of you than a cropped style. And that long, clean line always looks elegant."
SC(CB('snowwalk15', 0.0, 4.8, 0.3), st(72) - 0.1)
SC(CB('windycoat25', 0.0, 7.0, 0.3), at(72, 'On truly cold') - 0.1)
ONE([(C('coattry25', 0.0, 6.4), at(72, 'a coat that covers')), (C('croppedjk25', 0.0, 6.0), at(72, 'than a cropped')),
     (C('longcoat5', 4.0, 11.4), at(72, 'And that long') - 0.1)])
SC(CB('snowparis15', 0.0, 8.0, 0.5), at(72, 'always looks elegant') - 0.1)
# 73 "When you find that coat, the right weave, the right weight, the right fit, it becomes the piece you reach for every
#     single winter. That's quiet luxury in its truest form."
ROW([C('coatweave15', 0.0, 4.2), C('coatweave4', 0.0, 3.0), C('coatweave13', 9.5, 19.0)],
    [at(73, 'the right weave'), at(73, 'the right weight'), at(73, 'the right fit')])
SC(CB('snowparis44', 0.0, 6.7, 0.3), at(73, 'it becomes') - 0.1)
QUOTE(C('windycoat38', 3.0, 11.6), at(73, "That's quiet") - 0.1, 'quiet <i>luxury</i>', at(73, "That's quiet") + 0.2, 'in its truest form', at(73, 'in its truest'))

# ================= close =================
# 74 "Staying warm and looking elegant were never opposites. Often it's simply about choosing the right pieces for the weather you're actually in."
SC(CB('earmuff15', 0.0, 6.0, 0.5), st(74) - 0.1)
SC(CB('waveby2', 0.0, 9.0, 0.3), at(74, "Often it's") - 0.1)
# 75 "And I'm curious, what's the one winter piece you could never live without? Let me know in the comments. I always love hearing from you."
SC(CB('wintercafe2', 0.2, 7.0, 0.8), st(75) - 0.1)
SC(CB('phonecoffee7', 0.0, 11.4, 0.4), at(75, 'Let me know') - 0.1)
SC(CB('flw5', 0.0, 2.2, 0.4), at(75, 'I always love') + 0.05)                    # Little Women (1994): a letter from home
# 76 "If you'd like a part two with even more winter style tips, just comment part two. And if you found this video helpful,
#     a simple like or comment would truly mean the world to us."
ROW([C('scarfwrap29', 0.0, 10.0), C('snowparis29', 6.5, 12.2), C('earmuff19', 0.0, 11.5)],
    [st(76) - 0.05, at(76, 'even more winter'), at(76, 'just comment')])
SC(CB('wintercafe47', 0.0, 8.7, 0.4), at(76, 'And if you found') - 0.1)
# 77 "If you're ready to elevate your style even further, be sure to check out the personal stylist guide linked in the
#     description. It's sent instantly to your email after access."
SC(CB('scarfwrap2', 0.0, 12.0, 0.3), st(77) - 0.1)
SC(CB('waveby2', 9.1, 18.7, 0.3), at(77, 'be sure to check') - 0.1)
GUIDE(at(77, 'the personal stylist'), en(77) + 0.25)
# 78 "Thank you so much for spending your time with us today. Until next time. Bye, my loves."
SC(CB('wintercafe39', 0.0, 4.0, 0.45), st(78) - 0.1)
SC(CB('wintercafe40', 0.0, 6.6, 0.45), at(78, 'Until next time') - 0.1)

flush(total - 2.6)
json.dump(SB, open('storyboard.json', 'w'), indent=0)
