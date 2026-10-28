# 8 Things Elegant Ladies Never Wear in Winter - the edit, beat by beat (Episode 32).
# Format copied from the channel's own "Never Wear" videos (CHANNEL-DNA-REPORT.md, how-you-edit.md):
#   hook in full-screen street-style reels -> white "in today's video..." card -> "Episode 32" title over a clip ->
#   per point: white number card on the spoken "Number one..." -> the mistake shown literally, one tall panel per
#   spoken item on the caramel backdrop -> the principle as one line (white serif, one word in script) ->
#   "Instead..." as one centred reel growing from the centre, then the good examples -> a full-screen clip -> white.
#   Guide plug: full-screen clip, haze, "Check the description for / Personal Stylist Guide". White end card + logo.
# Footage: creators' Pinterest video pins (raw/meta.json), every segment checked on the strips (st/P_*.jpg, ok.txt),
# AI scan aiscan.json. 1980s-90s film scenes only where the line calls for them (owner's decision, SOURCES-LOG.md).
# Sound: the voice, one soft piano bed ~12 dB under it, no sound effects; film clips are silent.
import re as _re
SB = []                                   # storyboard log -> storyboard.json -> STORYBOARD.md
def _log(kind, specs, t0, t1, move):
    SB.append(dict(kind=kind, clips=[[s[0], s[1], s[2]] for s in specs], t0=round(t0, 2), t1=round(t1, 2), move=move))
def _plain(s): return _re.sub(r'<[^>]+>', ' ', s).replace('  ', ' ').strip()
def FULL(spec, t0, t1, fin=0.6):
    _log('full screen', [spec], t0, t1, f'dissolve {fin:.1f} s, slow push-in'); return canvas_full(spec, t0, t1, fin=fin)
def ROW(specs, times, t_end):
    _log(f'row of {len(specs)} tall panels', specs, times[0], t_end, 'each panel grows from its corner on its word'); row(specs, times, t_end)
def PAIR(specs, times, t_end):
    _log('two panels on caramel', specs, times[0], t_end, 'each panel grows from its corner on its word'); pair(specs, times, t_end)
def ONE(spec, t0, t1):
    _log('one centred reel on caramel', [spec], t0, t1, 'grows from the centre 1.2 s'); return single(spec, t0, t1)
def QUOTE(spec, t0, t1, l1, ta, l2, tb):
    """a reel on the left, the line to remember on the right (their 'Elegant style works with you' screens)"""
    _log('reel left + principle line', [spec], t0, t1, f'line wipes in: "{_plain(l1)} {_plain(l2)}"')
    panel(spec, 170, 170 + PW, t0, t1, entry='fade'); text(l1, 'qs1', ta, t1, dur=1.4); text(l2, 'qs2', tb, t1, dur=1.2)
def LINE(l1, ta, l2, tb, t1):
    """the principle as text on the caramel backdrop (their 'True elegance whispers / It doesn't shout')"""
    _log('principle line on caramel', [], ta, t1, f'line wipes in: "{_plain(l1)} {_plain(l2 or "")}"')
    text(l1, 'q1', ta, t1, dur=1.3)
    if l2: text(l2, 'q2', tb, t1, dur=1.3)
def CARD(txt, i, t_in=None, style=''):
    t0 = (en(i - 1) + 0.35) if t_in is None else t_in
    _log('white number card', [], t0, en(i) + 0.35, f'fade to white, black script wipes in: "{_plain(txt)}"')
    card(txt, i, t_in=t_in, style=style)
def GUIDE(t0, t1):
    i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, t0, 0.8); fade_out(i, t1, 0.5)
    text('Check the description for', 'gtx1', t0 + 0.5, t1 - 0.05, dur=1.1); text('Personal Stylist Guide', 'gtx2', t0 + 0.9, t1 - 0.05, dur=1.6)
    _log('guide text over the clip', [], t0, t1, 'haze, "Check the description for / Personal Stylist Guide"')
TWO = 'font-size:96px;line-height:1.3;text-align:center'
CROP['flw5'] = (62, 0, 1060)              # the burned-in "Little Women (1994)" caption stays out of frame

# ================= HOOK =================
# 1 "Have you ever seen a woman on a freezing winter day, walking calmly down the street in a long wool coat, a soft
#    scarf, beautiful gloves, and thought, 'How does she look so elegant... when I just look cold?'"
FULL(C('f80winter6', 0.0, 8.4), 0.0, at(1, 'walking calmly'), fin=0.01)
FULL(C('fymail10', 0.0, 2.9), at(1, 'walking calmly'), at(1, 'in a long wool'))          # You've Got Mail (1998)
ROW([C('coatwalk11', 0.0, 6.0), C('scarfwrap2', 13.0, 21.7), C('gloves12', 0.0, 6.0)],
    [at(1, 'a long wool coat'), at(1, 'a soft scarf'), at(1, 'beautiful gloves')], at(1, 'and thought') - 0.1)
FULL(C('snowcoat16', 0.0, 4.5), at(1, 'and thought') - 0.1, at(1, 'when I just'))
FULL(C('snowcoat9', 0.0, 5.5), at(1, 'when I just'), en(1) + 0.3)
# 2 "She isn't shivering. She isn't buried under ten layers. And yet she looks polished, warm, and completely at ease."
FULL(C('commute37', 0.0, 8.0), st(2) - 0.1, at(2, 'And yet'))
FULL(C('coatwalk17', 0.0, 6.3), at(2, 'And yet'), en(2) + 0.3)
# 3 "That kind of elegance isn't accidental. And the secret, it's often not about how much she's wearing, it's about
#    what she knows not to wear."
FULL(C('coatwalk36', 0.0, 6.8), st(3) - 0.1, at(3, 'And the secret'))
FULL(C('longcoat8', 0.0, 6.0), at(3, 'And the secret'), at(3, "it's about what"))
FULL(C('fymail10', 9.0, 11.9), at(3, "it's about what"), en(3) + 0.3)                      # You've Got Mail (1998)
# 4 "Welcome to The Classy Elegance. I'm so glad you're here. And if you've been with us for a while, yes, we have a new
#    name. Same channel, same timeless style, just a new chapter."
FULL(C('oldwinter19', 0.0, 10.1), st(4) - 0.1, at(4, "And if you've"))
FULL(C('cozyhome38', 0.0, 10.1), at(4, "And if you've"), at(4, 'Same channel'))
ROW([C('gloves8', 0.0, 9.0), C('coatwalk43', 0.0, 5.5), C('commute26', 0.0, 6.0)],
    [at(4, 'Same channel'), at(4, 'same timeless'), at(4, 'just a new')], en(4) + 0.35)
# 5 "In today's video, we're uncovering eight things elegant women never wear in winter and the smarter swaps that keep
#    you warmer and look far more expensive."
white(en(4) + 0.45, st(5) + 1.6)
_log('white card', [], en(4) + 0.45, st(5) + 1.6, 'black script wipes in: "in today\'s video..."')
text("in today's video...", 'card', st(5) - 0.05, st(5) + 1.45, dur=1.0, out=0.4)
FULL(C('snowparis13', 0.0, 7.0), st(5) + 1.5, at(5, 'and the smarter'))
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Episode 32</div><div class="big" style="font-size:86px">8 Things Elegant Ladies Never Wear in Winter</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.2,ease:"power2.out"}},{st(5)+1.9:.3f});'); fade_out(i, at(5, 'and the smarter') - 0.1, 0.5)
_log('title over the clip', [], st(5) + 1.9, at(5, 'and the smarter'), '"Episode 32" serif + title in white script, fades up 1.2 s')
ONE(C('coattry40', 0.0, 4.0), at(5, 'and the smarter'), at(5, 'keep you warmer'))
ROW([C('snowcoat45', 0.0, 4.4), C('gloves44', 13.0, 19.0), C('coatwalk4', 13.3, 16.5)],
    [at(5, 'keep you warmer'), at(5, 'and look far'), at(5, 'more expensive')], en(5) + 0.35)
# 6 "Some of these may surprise you, because a few of the pieces we reach for to stay warm can actually leave us colder.
#    But once you see them, you'll never unsee them. Let's get started."
ONE(C('snowcoat33', 0.0, 8.5), st(6) - 0.05, at(6, 'But once'))
ROW([C('commute37', 8.5, 14.7), C('coatwalk4', 0.0, 3.5), C('commute10', 0.0, 4.4)],
    [at(6, 'But once'), at(6, "you'll never unsee"), at(6, "Let's get started")], en(6) + 0.35)

# ================= 1. A chunky sweater squeezed under a fitted coat =================
CARD('1. A chunky sweater squeezed under a fitted coat', 7, style='font-size:90px')
# 8 "We've all done this. It's freezing, so you grab your thickest knit, pull your coat over the top, and suddenly you
#    can barely bend your arms. It feels like the warmest choice."
FULL(C('snowcoat14', 17.0, 21.8), en(7) + 0.3, at(8, 'you grab'))
ROW([C('chunky12', 5.5, 12.5), C('undercoat20', 4.5, 11.7), C('chunky4', 7.0, 13.4)],
    [at(8, 'you grab'), at(8, 'pull your coat'), at(8, 'and suddenly')], at(8, 'It feels like') - 0.1)
FULL(C('chunky6', 8.0, 15.1), at(8, 'It feels like') - 0.1, en(8) + 0.3)
# 9 "But here's what most people don't realize. What keeps you warm isn't really the fabric itself. It's the still air
#    trapped inside it."
ONE(C('chunky34', 5.5, 8.3), st(9) - 0.05, at(9, 'What keeps'))
FULL(C('merino0', 0.0, 7.0), at(9, 'What keeps'), at(9, "It's the still") - 0.1)
QUOTE(C('merino29', 0.0, 8.7), at(9, "It's the still") - 0.1, en(9) + 0.45,
      "It's the still <i>air</i>", at(9, "It's the still") + 0.2, 'trapped inside it', at(9, 'trapped'))
# 10 "When a thick sweater is pressed tight against the inside of a coat, both get squashed, and that warm pocket of air
#     gets squeezed out."
FULL(C('undercoat20', 0.0, 4.5), st(10) - 0.1, at(10, 'both get squashed'))
ONE(C('merino0', 7.5, 14.0), at(10, 'both get squashed'), en(10) + 0.35)
# 11 "So you look bulkier, your coat pulls across the shoulders and buttons, and you're often not as warm as you'd expect."
ROW([C('chunky6', 0.0, 7.6), C('coattry3', 0.0, 8.2), C('snowcoat34', 0.0, 2.9)],
    [st(11), at(11, 'your coat pulls'), at(11, "and you're often")], en(11) + 0.35)
# 12 "Instead, try a fine merino or cashmere knit under your coat. It's thin, but it holds warmth beautifully without the bulk."
ONE(C('merino13', 0.0, 7.7), st(12) - 0.05, at(12, "It's thin"))
PAIR([C('coattry25', 0.0, 6.4), C('label18', 0.0, 4.0)], [at(12, "It's thin"), at(12, 'holds warmth')], en(12) + 0.35)
# 13 "And if you love your chunky cable knit, and honestly, who doesn't, let it be the star. Wear it on its own on milder
#     days or under a coat cut roomy enough to fit over it."
FULL(C('chunky12', 12.5, 21.7), st(13) - 0.1, at(13, 'Wear it on'))
PAIR([C('chunky14', 0.0, 8.3), C('coattry12', 0.0, 10.0)], [at(13, 'Wear it on'), at(13, 'or under a coat')], en(13) + 0.35)
# 14 "When you shop for a coat, try it on over the thickest sweater you plan to wear. If you can lift your arms and button it
#     without pulling, that's the one. So chic."
FULL(C('longcoat19', 0.0, 11.0), st(14) - 0.1, at(14, 'If you can'))
ONE(C('longcoat37', 6.0, 10.2), at(14, 'If you can'), at(14, 'So chic'))
FULL(C('coatwalk3', 0.0, 4.4), at(14, 'So chic'), en(14) + 0.3)

# ================= 2. Cotton next to your skin =================
CARD('2. Cotton next to your skin<br>on busy, rushing around days', 15, style=TWO)
# 16 "Cotton is lovely. Soft, breathable, easy. But in winter, there's one situation where it quietly works against you."
ROW([C('label28', 0.0, 6.0), C('label23', 14.0, 19.5), C('label23', 33.0, 38.0)],
    [en(15) + 0.3, at(16, 'Soft'), at(16, 'breathable')], at(16, 'But in winter') - 0.1)
FULL(C('commute25', 0.0, 6.5), at(16, 'But in winter') - 0.1, en(16) + 0.3)
# 17 "Cotton soaks up moisture and dries slowly, and once it's damp, it loses much of its ability to keep you warm. And that
#     moisture doesn't only come from the rain."
ONE(C('label23', 24.0, 31.0), st(17) - 0.05, at(17, "and once it's"))
FULL(C('commute13', 0.0, 6.0), at(17, "and once it's"), at(17, 'And that moisture'))
FULL(C('commute9', 0.0, 5.9), at(17, 'And that moisture'), en(17) + 0.3)
# 18 "Think about a typical winter day. You hurry to the train, walk briskly in your coat, step into a heated shop or office,
#     and you start to warm up."
FULL(C('snowcoat17', 0.0, 3.6), st(18) - 0.1, at(18, 'You hurry'))
ROW([C('commute26', 6.0, 11.7), C('commute27', 3.1, 6.6), C('heels16', 8.6, 10.7)],
    [at(18, 'You hurry'), at(18, 'walk briskly'), at(18, 'step into a heated')], at(18, 'and you start') - 0.1)
FULL(C('commute35', 22.0, 31.0), at(18, 'and you start') - 0.1, en(18) + 0.3)
# 19 "Your cotton tee absorbs that little bit of sweat and holds on to it. Then you step back outside, and suddenly you feel
#     colder than when you left the house. Sound familiar?"
ONE(C('silklayer17', 7.5, 11.6), st(19) - 0.05, at(19, 'Then you step'))
FULL(C('coldhands39', 7.0, 9.5), at(19, 'Then you step'), at(19, 'and suddenly'))
FULL(C('snowparis14', 0.0, 8.3), at(19, 'and suddenly'), at(19, 'Sound familiar'))
FULL(C('snowcoat45', 4.5, 9.0), at(19, 'Sound familiar'), en(19) + 0.3)
# 20 "Instead, choose a base layer that handles moisture better. Merino wool is a beautiful option."
ONE(C('merino0', 14.5, 21.9), st(20) - 0.05, at(20, 'Merino wool'))
FULL(C('merino22', 0.0, 4.6), at(20, 'Merino wool'), en(20) + 0.3)
# 21 "Wool can absorb around a third of its weight in moisture vapor before it even starts to feel wet, so it stays
#     comfortable as you move between the cold street and a warm room."
QUOTE(C('merino2', 0.0, 7.1), st(21) - 0.1, at(21, 'as you move'),
      'Wool can absorb', st(21) + 0.3, 'around <i>a third</i> of its weight', at(21, 'around a third'))
PAIR([C('commute14', 2.8, 11.3), C('cozyhome42', 0.0, 12.9)], [at(21, 'as you move'), at(21, 'a warm room')], en(21) + 0.35)
# 22 "A thin silk layer or a good synthetic thermal works well, too, and dries quickly."
PAIR([C('silklayer43', 2.0, 9.0), C('label35', 0.6, 4.6)], [st(22) - 0.05, at(22, 'a good synthetic')], en(22) + 0.35)
# 23 "And here's a little trick hikers swear by. Dress for how you'll feel 10 minutes into your walk, not the moment you open the door."
FULL(C('snowcoat14', 0.0, 8.5), st(23) - 0.1, at(23, 'Dress for how') - 0.1)
QUOTE(C('snowcoat14', 8.6, 16.5), at(23, 'Dress for how') - 0.1, en(23) + 0.45,
      "Dress for how you'll feel", at(23, 'Dress for how') + 0.2, '<i>10 minutes</i> into your walk', at(23, '10 minutes'))
# 24 "Now, this doesn't mean cotton is off limits. On a dry day when you're mostly indoors, your favorite cotton shirt is
#     perfectly fine. It's the damp, active, in-and-out days where it lets you down."
FULL(C('label28', 7.0, 16.7), st(24) - 0.1, at(24, 'On a dry day'))
ONE(C('cozyhome1', 0.0, 9.4), at(24, 'On a dry day'), at(24, "It's the damp") - 0.1)
ROW([C('commute25', 7.0, 13.1), C('commute35', 10.0, 15.5), C('heels16', 5.0, 8.4)],
    [at(24, "It's the damp") - 0.1, at(24, 'active'), at(24, 'in-and-out')], en(24) + 0.35)

# ================= 3. The cozy acrylic sweater =================
CARD('3. The cozy acrylic sweater', 25)
# 26 "It looks soft on the hanger, it's often a fraction of the price, and it feels warm the moment you put it on."
ONE(C('label23', 0.0, 5.5), en(25) + 0.3, at(26, 'and it feels warm'))
FULL(C('acrylic38', 0.5, 4.5), at(26, 'and it feels warm'), en(26) + 0.3)
# 27 "But acrylic absorbs very little moisture. So when you go from the cold outside into a heated room, the warmth and
#     moisture your body gives off has nowhere to go. That's why some acrylic knits feel toasty one minute and strangely
#     clammy the next."
ONE(C('acrylic38', 5.5, 11.0), st(27) - 0.05, at(27, 'So when you go'))
PAIR([C('snowcoat8', 0.0, 9.8), C('cozyhome37', 0.0, 10.5)], [at(27, 'the cold outside'), at(27, 'into a heated room')], at(27, "That's why") - 0.1)
LINE('<i>toasty</i> one minute', at(27, 'feel toasty'), 'and strangely clammy the next', at(27, 'and strangely'), en(27) + 0.45)
# 28 "And many acrylic sweaters pill quickly. Those little fuzzy balls that appear under the arms and along the sides after
#     just a few wears."
FULL(C('acrylic18', 0.0, 12.0), st(28) - 0.1, at(28, 'under the arms'))
PAIR([C('acrylic18', 28.0, 34.0), C('acrylic8', 0.0, 3.5)], [at(28, 'under the arms'), at(28, 'along the sides')], en(28) + 0.35)
# 29 "And as we've said before on this channel, nothing takes away from an elegant look faster than clothing that looks worn down."
FULL(C('coatfabric10', 13.0, 20.0), st(29) - 0.1, at(29, 'faster than'))
ONE(C('acrylic18', 12.5, 19.0), at(29, 'faster than'), en(29) + 0.35)
# 30 "Instead, flip to the label before you buy. Look for wool, merino, cashmere, or a wool-rich blend."
ONE(C('label23', 9.0, 13.5), st(30) - 0.05, at(30, 'Look for wool'))
ROW([C('merino2', 7.2, 11.2), C('beanie5', 8.6, 11.0), C('label18', 4.5, 8.0)],
    [at(30, 'Look for wool'), at(30, 'cashmere'), at(30, 'wool-rich blend')], en(30) + 0.35)
# 31 "Then give the knit a gentle stretch. A quality knit feels dense and springs right back into shape. If it stays
#     stretched out or you can see straight through it, put it back."
ONE(C('acrylic18', 23.0, 27.5), st(31) - 0.05, at(31, 'A quality knit'))
FULL(C('mittens5', 5.0, 11.5), at(31, 'A quality knit'), at(31, 'If it stays'))
FULL(C('silklayer43', 9.5, 17.5), at(31, 'If it stays'), en(31) + 0.3)
# 32 "Now, a little acrylic in a blend isn't a bad thing. It can make a sweater more affordable and easier to care for.
#     Just let it be the supporting fiber, not the whole sweater."
FULL(C('chunky4', 0.0, 6.5), st(32) - 0.1, at(32, 'It can make'))
ONE(C('washknit12', 0.0, 5.0), at(32, 'It can make'), at(32, 'Just let it'))
FULL(C('label18', 8.0, 11.4), at(32, 'Just let it'), en(32) + 0.3)
# 33 "And washing your knits inside out on a gentle cycle helps them stay smooth for so much longer."
ONE(C('washknit24', 5.9, 8.9), st(33) - 0.05, at(33, 'on a gentle'))
FULL(C('washknit12', 5.2, 8.5), at(33, 'on a gentle'), at(33, 'stay smooth'))
FULL(C('acrylic8', 5.8, 8.3), at(33, 'stay smooth'), en(33) + 0.3)
# 34 "And here's a secret many well-dressed women don't share. They know exactly what flatters them. The colors that make
#     their skin glow in that soft winter light and the coat shapes that complement their figure."
FULL(C('coatwalk3', 4.5, 10.4), st(34) - 0.1, at(34, 'They know exactly'))
ONE(C('winterlook29', 0.0, 10.3), at(34, 'They know exactly'), at(34, 'The colors'))
PAIR([C('beret12', 0.0, 8.2), C('coatlabel14', 0.0, 10.0)], [at(34, 'The colors'), at(34, 'and the coat shapes')], en(34) + 0.35)
# 35 guide plug: "If you'd like to discover what suits you best ... our personal stylist guide is linked in the description.
#     It's sent instantly to your email after access. Now, let's continue."
FULL(C('winterlook33', 0.0, 11.1), st(35) - 0.1, at(35, 'our personal stylist'))
FULL(C('gloves8', 20.0, 29.3), at(35, 'our personal stylist'), at(35, "Now, let's"))
GUIDE(at(35, 'our personal stylist') + 0.1, at(35, "Now, let's") - 0.05)
FULL(C('coatwalk4', 5.6, 7.7), at(35, "Now, let's"), en(35) + 0.3)

# ================= 4. Boots that fit perfectly in October =================
CARD('4. Boots that fit perfectly in October', 36)
# 37 "You buy them in early fall, wear them with thin socks, and they fit like a dream. Then winter arrives, you add your
#     thickest socks, and suddenly they're snug across the toes."
FULL(C('boots41', 0.0, 9.0), en(36) + 0.3, at(37, 'wear them with'))
FULL(C('heels0', 0.0, 8.0), at(37, 'wear them with'), at(37, 'Then winter') - 0.1)
ROW([C('flw7', 0.0, 7.0), C('socks18', 0.0, 5.0), C('boots2', 0.0, 5.4)],
    [at(37, 'Then winter') - 0.1, at(37, 'you add your'), at(37, 'and suddenly')], en(37) + 0.35)
# 38 "It feels like you've just made them warmer, but often it's the opposite. When your boots are too tight, they squeeze
#     your feet, and that can restrict the blood flow that keeps your toes warm."
ONE(C('boots16', 0.0, 6.0), st(38) - 0.05, at(38, 'When your boots'))
PAIR([C('socks12', 3.5, 9.9), C('boots23', 5.5, 9.0)], [at(38, 'When your boots'), at(38, 'and that can restrict')], en(38) + 0.35)
# 39 "The tightness also crushes the insulation in your socks and in the boot itself. So the thickest sock in a tight boot
#     can leave you with colder feet than a thinner sock with a little room."
FULL(C('boots7', 2.0, 12.0), st(39) - 0.1, at(39, 'So the thickest'))
ONE(C('socks6', 9.0, 16.0), at(39, 'So the thickest'), at(39, 'than a thinner'))
FULL(C('socks13', 2.0, 5.0), at(39, 'than a thinner'), en(39) + 0.3)
# 40 "Instead, aim for enough space to wiggle your toes freely while your heel stays snugly in place. A fine merino sock
#     gives you warmth without the bulk."
ONE(C('boots16', 6.0, 14.0), st(40) - 0.05, at(40, 'A fine merino'))
FULL(C('socks12', 0.0, 3.4), at(40, 'A fine merino'), en(40) + 0.3)
# 41 "And when you shop for winter boots, try them on in the afternoon, wearing the socks you'll actually wear with them."
FULL(C('boots41', 14.5, 24.0), st(41) - 0.1, at(41, 'wearing the socks'))
ONE(C('socks18', 5.5, 10.0), at(41, 'wearing the socks'), en(41) + 0.35)
# 42 "Of course, you don't want boots that are too loose either. If your foot slides around, cold air moves around inside
#     with it. The goal is room for your toes and support for your heel."
FULL(C('heels38', 3.0, 6.4), st(42) - 0.1, at(42, 'If your foot'))
ONE(C('boots23', 0.0, 5.4), at(42, 'If your foot'), at(42, 'The goal is') - 0.1)
QUOTE(C('boots7', 12.5, 21.0), at(42, 'The goal is') - 0.1, en(42) + 0.45,
      'room for your <i>toes</i>', at(42, 'room for your'), 'and support for your heel', at(42, 'and support'))

# ================= 5. Smooth soles on icy days =================
CARD('5. Smooth soles on icy days', 43)
# 44 "There's nothing more elegant than a sleek leather boot or a pointed-toe heel with a long coat. But on ice, a smooth sole
#     has almost nothing to grip with. And no outfit looks graceful while you're tiptoeing down the pavement or worse, slipping."
FULL(C('heels17', 0.0, 6.5), en(43) + 0.3, at(44, 'or a pointed-toe'))
FULL(C('longcoat14', 14.0, 22.5), at(44, 'or a pointed-toe'), at(44, 'But on ice'))
FULL(C('icy1', 0.0, 4.6), at(44, 'But on ice'), at(44, 'And no outfit'))
ONE(C('heels17', 7.0, 13.7), at(44, 'And no outfit'), en(44) + 0.35)
# 45 "Here's something that surprised me. Researchers at Toronto's WinterLab tested nearly a hundred types of winter footwear
#     on ice, and fewer than one in 10 met their minimum standard for grip."
FULL(C('snowcoat17', 8.0, 16.6), st(45) - 0.1, at(45, 'tested nearly'))
ROW([C('boots41', 9.2, 14.3), C('treadboots14', 7.0, 12.9), C('treadboots10', 2.5, 4.9)],
    [at(45, 'tested nearly'), at(45, 'types of winter'), at(45, 'on ice')], at(45, 'and fewer') - 0.1)
LINE('fewer than <i>one in 10</i>', at(45, 'and fewer'), 'met their minimum standard for grip', at(45, 'met their'), en(45) + 0.45)
# 46 "The ones that performed best had special soles with tiny grit-like particles built right into the rubber. So even a
#     boot sold as a winter boot isn't automatically safe on ice."
FULL(C('boots7', 21.0, 33.0), st(46) - 0.1, at(46, 'sold as a'))
FULL(C('icy1', 4.7, 9.0), at(46, 'sold as a'), en(46) + 0.3)
# 47 "Instead, keep one pair with a deeply treaded rubber sole for icy mornings. Many now come in sleek black or brown
#     leather that look just as polished."
ONE(C('treadboots1', 0.0, 6.8), st(47) - 0.05, at(47, 'Many now come'))
PAIR([C('treadboots14', 0.0, 6.5), C('treadboots10', 4.95, 8.1)], [at(47, 'Many now come'), at(47, 'or brown leather')], en(47) + 0.35)
# 48 "You can also ask a cobbler to add a thin rubber sole protector to your favorite leather-soled shoes. It's affordable and adds grip."
FULL(C('cobbler2_22', 0.0, 13.0), st(48) - 0.1, at(48, "It's affordable"))
ONE(C('cobbler2_13', 17.0, 26.0), at(48, "It's affordable"), en(48) + 0.35)
# 49 "And for truly icy days, a pair of slip-on ice grips can live in your bag and come off the moment you arrive."
FULL(C('icegrips3', 9.8, 12.5), st(49) - 0.1, at(49, 'a pair of slip-on'))
ONE(C('icegrips0', 0.0, 1.95), at(49, 'a pair of slip-on'), at(49, 'can live in'))
FULL(C('gloves22', 14.0, 19.0), at(49, 'can live in'), en(49) + 0.3)
# 50 "Now, on dry, cleared pavement, wear your elegant soles and enjoy them. It's simply about knowing which days call for something more."
FULL(C('heels0', 8.2, 21.0), st(50) - 0.1, en(50) + 0.3)

# ================= 6. Thin, unlined leather gloves =================
CARD('6. Thin, unlined leather gloves', 51)
# 52 "Leather gloves are a winter classic and for good reason. They're timeless, sleek, and they finish a coat beautifully."
FULL(C('gloves15', 0.0, 6.5), en(51) + 0.3, at(52, "They're timeless"))
ROW([C('gloves25', 0.0, 7.0), C('gloves44', 5.0, 12.0), C('gloves22', 0.0, 12.0)],
    [at(52, "They're timeless"), at(52, 'sleek'), at(52, 'and they finish')], en(52) + 0.35)
# 53 "But a very thin, unlined pair on a freezing, windy day leaves just a fine layer of leather between your fingers and the cold."
ONE(C('gloves31', 0.0, 5.8), st(53) - 0.05, at(53, 'on a freezing'))
FULL(C('windycoat41', 0.0, 7.6), at(53, 'on a freezing'), at(53, 'leaves just'))
FULL(C('coldhands5', 0.0, 9.0), at(53, 'leaves just'), en(53) + 0.3)
# 54 "And when your hands are cold, you tense up. Your shoulders rise, you rush, you hide your hands in your sleeves. Not
#     exactly the calm, composed presence we're going for."
FULL(C('snowcoat9', 6.0, 15.5), st(54) - 0.1, at(54, 'Not exactly') - 0.1)
QUOTE(C('coatwalk11', 6.0, 15.2), at(54, 'Not exactly') - 0.1, en(54) + 0.45,
      'the calm,', at(54, 'the calm'), '<i>composed</i> presence', at(54, 'composed'))
# 55 "Instead, look for leather gloves lined in cashmere, wool, or fleece. They keep the same slim, elegant shape with far more warmth inside."
ONE(C('gloves12', 12.5, 21.2), st(55) - 0.05, at(55, 'They keep'))
PAIR([C('gloves31', 6.2, 12.4), C('gloves25', 8.0, 16.1)], [at(55, 'They keep'), at(55, 'far more warmth')], en(55) + 0.35)
# 56 "And on the coldest days, consider mittens. When they're made from the same materials, mittens are warmer than gloves
#     because your fingers share their warmth instead of each one facing the cold on its own."
FULL(C('mittens0', 0.0, 5.2), st(56) - 0.1, at(56, "When they're made"))
PAIR([C('mittens40', 0.0, 14.0), C('mittens5', 12.0, 20.2)], [at(56, "When they're made"), at(56, 'because your fingers')], en(56) + 0.35)
# 57 "A soft lined leather or knit mitten looks incredibly chic with a long wool coat. And if you need your fingers free, a
#     thin liner glove underneath a mitten gives you the best of both."
FULL(C('mittens40', 15.0, 27.0), st(57) - 0.1, at(57, 'with a long wool'))
FULL(C('scarfwrap48', 14.5, 20.2), at(57, 'with a long wool'), at(57, 'And if you need'))
ONE(C('mittens1', 0.0, 11.7), at(57, 'And if you need'), en(57) + 0.35)

# ================= 7. Nothing on your head =================
CARD("7. Nothing on your head because<br>you don't want to ruin your hair", 58, style=TWO)
# 59 "I completely understand this one. You've done a beautiful blowout, and the last thing you want is hat hair."
FULL(C('blowout4', 0.0, 6.5), en(58) + 0.3, at(59, 'and the last thing'))
ONE(C('blowout12', 0.0, 3.0), at(59, 'and the last thing'), en(59) + 0.35)
# 60 "And you may have heard that we lose most of our body heat through our heads. That's actually a myth."
FULL(C('coldhands39', 10.0, 14.9), st(60) - 0.1, at(60, "That's actually") - 0.1)
LINE("That's actually a <i>myth</i>.", at(60, "That's actually"), None, None, en(60) + 0.45)
# 61 "Researchers writing in the British Medical Journal traced it back to a flawed interpretation of an old military
#     experiment. Your head loses heat much like any other uncovered part of your body."
FULL(C('flw5', 0.0, 4.4), st(61) - 0.1, at(61, 'traced it back'))                          # Little Women (1994)
FULL(C('flw5', 4.5, 9.9), at(61, 'traced it back'), at(61, 'Your head loses'))           # Little Women (1994)
FULL(C('commute13', 6.0, 14.6), at(61, 'Your head loses'), en(61) + 0.3)
# 62 "But here's what does matter. Your ears are one of the areas most vulnerable to frostbite, along with your fingers,
#     toes, nose, cheeks, and chin. And on a windy day, cold, stinging ears can make you miserable in minutes."
ONE(C('earmuff1', 0.0, 5.2), st(62) - 0.05, at(62, 'along with your'))
FULL(C('scarfwrap3', 0.0, 4.5), at(62, 'along with your'), at(62, 'And on a windy'))
FULL(C('windycoat43', 17.0, 25.0), at(62, 'And on a windy'), en(62) + 0.3)
# 63 "So instead of skipping it altogether, choose something that protects your ears and your hairstyle."
ONE(C('snowparis41', 0.0, 8.0), st(63) - 0.05, en(63) + 0.35)
# 64 "A wide knit or cashmere headband keeps your ears covered and looks beautiful with a sleek low bun or a soft blowout."
PAIR([C('headband5', 0.95, 5.2), C('headband12', 2.5, 8.8)], [st(64) - 0.05, at(64, 'cashmere headband')], at(64, 'with a sleek'))
PAIR([C('winterbun28', 0.0, 12.4), C('blowout12', 28.0, 38.0)], [at(64, 'with a sleek'), at(64, 'or a soft blowout')], en(64) + 0.35)
# 65 "A wool beret is timeless and effortlessly chic. And if you love a beanie, choose a fine merino or cashmere one rather
#     than a stiff, heavy knit. Just make sure your hair is completely dry before you put it on. So pretty."
ROW([C('beret15', 3.0, 11.5), C('snowparis29', 0.0, 6.0), C('beret3', 0.0, 3.5)],
    [st(65) - 0.05, at(65, 'is timeless'), at(65, 'effortlessly chic')], at(65, 'And if you love') - 0.1)
ONE(C('beanie5', 0.0, 4.6), at(65, 'And if you love') - 0.1, at(65, 'rather than'))
FULL(C('snowparis3', 0.0, 8.0), at(65, 'rather than'), at(65, 'Just make sure'))
FULL(C('beret3', 11.0, 14.5), at(65, 'Just make sure'), at(65, 'before you put'))
FULL(C('beret16', 0.0, 6.5), at(65, 'before you put'), en(65) + 0.3)

# ================= 8. The coat that only looks warm =================
# 66 "Saving one of my favorites for last. Number eight, the coat that only looks warm."
FULL(C('longcoat37', 2.0, 5.8), st(66) - 0.1, at(66, 'Number eight') - 0.3)
CARD('8. The coat that only looks warm', 66, t_in=at(66, 'Number eight') - 0.35)
# 67 "Your coat is often the first thing people notice in winter, and it's the piece doing most of the work to keep you warm."
FULL(C('longcoat8', 6.0, 11.6), en(66) + 0.3, at(67, "and it's the piece"))
ONE(C('longcoat19', 12.0, 20.0), at(67, "and it's the piece"), en(67) + 0.35)
# 68 "But two coats can look almost identical on the hanger and feel completely different on a windy street. The difference is often the fabric."
PAIR([C('woolcare10', 2.0, 9.5), C('windycoat27', 0.0, 9.0)], [st(68) - 0.05, at(68, 'and feel completely')], at(68, 'The difference') - 0.1)
FULL(C('coatfabric21', 0.0, 8.0), at(68, 'The difference') - 0.1, en(68) + 0.3)
# 69 "A loosely woven coat can let the wind cut straight through it, no matter how thick it looks. Dense, tightly woven, or
#     felted wool fabrics like melton or boiled wool hold up far better against the wind, and they keep their shape
#     beautifully year after year."
ONE(C('coatfabric2', 0.0, 6.5), st(69) - 0.05, at(69, 'no matter how'))
FULL(C('windycoat43', 25.5, 30.5), at(69, 'no matter how'), at(69, 'Dense'))
PAIR([C('coatfabric21', 8.5, 19.5), C('coatweave40', 0.0, 6.0)], [at(69, 'Dense'), at(69, 'like melton')], at(69, 'hold up far') - 0.1)
FULL(C('longcoat19', 20.0, 28.9), at(69, 'hold up far') - 0.1, en(69) + 0.3)
# 70 "Before you buy, check the label. A high wool content is what you're looking for. And a small amount of nylon or
#     polyester is perfectly fine. It can actually make a coat more durable."
ONE(C('coatlabel24', 0.1, 2.45), st(70) + 0.3, at(70, 'A high wool'))
FULL(C('coatweave40', 6.2, 11.7), at(70, 'A high wool'), at(70, 'And a small'))
PAIR([C('coatweave13', 0.0, 9.0), C('coatweave4', 4.5, 12.2)], [at(70, 'And a small'), at(70, 'It can actually')], en(70) + 0.35)
# 71 "Then try this simple test. Hold the fabric up to a window or a bright light. If light shines easily through the weave,
#     chances are the wind will, too."
ONE(C('coatfabric15', 0.0, 9.4), st(71) - 0.05, at(71, 'chances are'))
FULL(C('windycoat37', 0.0, 4.1), at(71, 'chances are'), en(71) + 0.3)
# 72 "And finally, look at the length. On truly cold, windy days, a coat that covers your hips and upper thighs protects far
#     more of you than a cropped style. And that long, clean line always looks elegant."
FULL(C('snowwalk15', 0.0, 4.8), st(72) - 0.1, at(72, 'On truly cold'))
FULL(C('windycoat25', 0.0, 7.0), at(72, 'On truly cold'), at(72, 'than a cropped'))
ONE(C('croppedjk25', 0.0, 6.0), at(72, 'than a cropped'), at(72, 'And that long') - 0.1)
FULL(C('snowparis0', 0.0, 8.3), at(72, 'And that long') - 0.1, en(72) + 0.3)
# 73 "When you find that coat, the right weave, the right weight, the right fit, it becomes the piece you reach for every
#     single winter. That's quiet luxury in its truest form."
ROW([C('coatweave15', 0.0, 4.2), C('coatweave4', 0.0, 3.0), C('coatweave13', 9.5, 19.0)],
    [st(73) - 0.05, at(73, 'the right weight'), at(73, 'the right fit')], at(73, 'it becomes') - 0.1)
FULL(C('snowparis15', 0.0, 8.0), at(73, 'it becomes') - 0.1, at(73, "That's quiet") - 0.1)
QUOTE(C('windycoat38', 3.0, 11.6), at(73, "That's quiet") - 0.1, en(73) + 0.6,
      'quiet <i>luxury</i>', at(73, "That's quiet") + 0.2, 'in its truest form', at(73, 'in its truest'))

# ================= close =================
# 74 "Staying warm and looking elegant were never opposites. Often it's simply about choosing the right pieces for the weather you're actually in."
FULL(C('snowparis44', 0.0, 6.7), st(74) - 0.1, at(74, "Often it's"))
FULL(C('earmuff15', 0.0, 10.0), at(74, "Often it's"), en(74) + 0.3)
# 75 "And I'm curious, what's the one winter piece you could never live without? Let me know in the comments. I always love hearing from you."
FULL(C('wintercafe6', 0.0, 5.7), st(75) - 0.1, at(75, 'Let me know'))
FULL(C('wintercafe2', 0.0, 7.0), at(75, 'Let me know'), en(75) + 0.3)
# 76 "If you'd like a part two with even more winter style tips, just comment part two. And if you found this video helpful,
#     a simple like or comment would truly mean the world to us."
ROW([C('scarfwrap29', 0.0, 10.0), C('snowparis29', 6.5, 12.2), C('earmuff23', 0.0, 10.8)],
    [st(76) - 0.05, at(76, 'even more winter'), at(76, 'just comment')], at(76, 'And if you found') - 0.1)
FULL(C('wintercafe47', 0.0, 8.7), at(76, 'And if you found') - 0.1, en(76) + 0.3)
# 77 "If you're ready to elevate your style even further, be sure to check out the personal stylist guide linked in the
#     description. It's sent instantly to your email after access."
FULL(C('scarfwrap2', 0.0, 12.0), st(77) - 0.1, at(77, 'be sure to check'))
FULL(C('wintercafe37', 0.0, 9.5), at(77, 'be sure to check'), en(77) + 0.3)
GUIDE(at(77, 'the personal stylist'), en(77) + 0.25)
# 78 "Thank you so much for spending your time with us today. Until next time. Bye, my loves."
FULL(C('wintercafe39', 0.0, 4.0), st(78) - 0.1, at(78, 'Until next time'))
FULL(C('wintercafe40', 0.0, 6.6), at(78, 'Until next time'), total - 2.6)

json.dump(SB, open('storyboard.json', 'w'), indent=0)
