# 8 Ways to Dress for Your Body Shape - the edit, beat by beat (the "demo" edit, Oct 2026).
# Why it changed: videos/body-shape/edit-evidence.md. In short (topic winners' replay peaks + the 79-video study):
#   white number card -> ONE real woman per point in one frame on the left, doing the tip on herself (mistake -> fix -> payoff),
#   the tip DRAWN on her at the word (lines, rings, labels; the biggest topic peak is a labelled hand test, 10.7x),
#   a tick/cross list building on the right (the screenshot of the point), the line-up of real women who name their own shape,
#   no full-screen mood clips mid-point, a new picture <= 5 s, the guide plug <= 10 s at the end of point 4, recap brings the women back.
# Coordinates for the drawings are measured on full frames of each clip (st/a*.jpg, 720x1280 space). No AI clips (aiscan + meta_check).
after = lambda i: en(i) + 0.1

# burned-in captions / watermarks cut out (x0, y0, h in 720x1280 space)
CROP.update({'loosedress11': (66, 235, 1045), 'loosedress2': (58, 205, 1075), 'loosedress19': (0, 140, 1140),
             'pearshape22': (80, 250, 950), 'rectangle30': (90, 360, 920), 'appleshape39': (60, 230, 1050),
             'invtri2': (67, 240, 1040), 'lowrise23': (85, 300, 980), 'shorttorso39': (118, 0, 860), 'hourglass42': (115, 120, 750),
             'bigbust3': (0, 0, 1100), 'earrings16': (85, 300, 980), 'empire18': (0, 100, 960), 'appletips43': (0, 120, 700), 'torso23': (0, 0, 1280)})
def PT(key, px, py, x0=None):
    """a point measured on the clip (720x1280, before the crop) -> screen pixels in the demo frame"""
    if key in CROP:
        cx, cy, ch = CROP[key]; f = 1280 / ch; px, py = (px - cx) * f, (py - cy) * f
    return to_screen(px, py, x0)
def L(key, xa, xb, y, t0, t1, dash=False):
    a = PT(key, xa, y); b = PT(key, xb, y); return hline(a[1], a[0], b[0], t0, t1, dash=dash)
TAGX = FX0 + 22          # labels sit inside the frame, near its left edge
def tg(txt, y, t0, t1): return tag(txt, TAGX, y, t0, t1)

# ================= HOOK (0-22 s) =================
# 1 "Before you blame your body for one more outfit, stop."   (the woman in the shapeless dress; she comes back fixed in point 3)
canvas_full(C('loosedress11', 0.15, 1.95), 0.0, 1.9, fin=0.01)
canvas_full(C('loosedress11', 1.95, 1.95), 1.9, en(1) + 0.25, fin=0.25)
# 2 "Which 8 ways to dress for your body shape make clothes look made for you, at any age?"
row([C('wrapdress13', 20.5, 26.5), C('cream26', 0.0, 6.0), C('petitetips21', 2.0, 8.0)],
    [st(2) - 0.1, at(2, 'body shape'), at(2, 'made for you')], en(2) + 0.35)
# 3 "There's no right or wrong body. Only clothes that are cut for it, or not."   (XS to XL, the same dress)
canvas_full(C('samedress4', 1.0, 6.6), st(3) - 0.15, en(3) + 0.3, fin=0.5)
# 4 "If no one ever showed you how, we will today. Let's begin."
canvas_full(C('olderyounger34', 13.5, 19.5), st(4) - 0.1, en(4) + 0.5, fin=0.5)
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Episode 12</div><div class="big" style="font-size:88px">8 Ways to Dress for Your Body Shape</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.1,ease:"power2.out"}},{at(4, "we will today"):.3f});'); fade_out(i, en(4) + 0.3, 0.45)

# ================= 1. Find your shape =================
card('1. Find your shape', 5)
# 6 "It's easy to shop by size and hope for the best."
# 7 "But two women can wear the same size and have completely different shapes, and that's why the same dress looks so different on each of them."
# 8 "Elegant women don't dress for a size. They dress for their shape."
# 9 "Try this now. In front of a full-length mirror, in daylight and fitted clothes, look at three widths only: your shoulders, your waist and your hips."
t9 = at(9, 'look at three widths')
demo([(C('fitroom33', 0.0, 3.9), after(5)), (C('samedress17', 0.0, 8.1), st(7) - 0.1), (C('samedress14', 14.0, 19.0), st(8) - 0.1),
      (C('shapetest0', 24.0, 29.0), st(9) - 0.1), (C('shapetest0', 40.6, 45.6), t9, 1.0)], en(9) + 0.3)
for key_y, (xa, xb, y), word in [(0, (200, 520, 592), 'shoulders'), (1, (250, 470, 815), 'waist'), (2, (225, 495, 975), 'hips')]:
    tt = at(9, 'your ' + word) - 0.1
    L('shapetest0', xa, xb, y, tt, en(9) + 0.25)
    tg(word, PT('shapetest0', 0, y)[1] - 70, tt + 0.2, en(9) + 0.25)
kicker('find your shape', after(5), en(9) + 0.3)
steps([('yes', 'shop for shape, not size', at(8, 'dress for their shape')), ('yes', 'a mirror, daylight', at(9, 'full-length mirror')),
       ('yes', 'shoulders, waist, hips', t9)], en(9) + 0.3)
# 10 "Hips wider than shoulders is often called a pear. Shoulders wider than hips, an inverted triangle. Even, with a clear waist,
#     an hourglass. Even, with a straighter waist, a rectangle. And fuller through the middle, an apple."   (each woman named her own shape)
row([C('pearshape22', 40.0, 53.5), C('invtri2', 0.0, 8.4), C('hourglass42', 4.0, 13.7), C('rectangle30', 1.0, 8.8), C('appleshape39', 3.0, 17.8)],
    [st(10) - 0.1, at(10, 'Shoulders wider'), at(10, 'Even, with a clear'), at(10, 'Even, with a straighter'), at(10, 'And fuller')], en(10) + 0.4,
    labels=['pear', 'inverted triangle', 'hourglass', 'rectangle', 'apple'])
# 11 "Not sure? Notice where clothes feel tight first. And if you're a little of two, that's perfectly normal."
# 12 "These are only descriptions, nothing good or bad, and they can change over the years. Once you know yours, shopping stops being a guess, and you choose with calm confidence."
demo([(C('bigbust3', 4.1, 7.9), st(11) - 0.1), (C('samedress24', 1.0, 6.0), at(11, 'And if')),
      (C('samedress23', 4.0, 11.2), st(12) - 0.1), (C('mirror50_15', 2.0, 9.0), at(12, 'Once you know'))], en(12) + 0.6)
kicker('find your shape', st(11) - 0.1, en(12) + 0.5)
steps([('yes', 'where is it tight first?', at(11, 'Notice')), ('yes', 'a little of two? normal', at(11, 'a little of two')),
       ('yes', 'nothing good or bad', at(12, 'nothing good or bad'))], en(12) + 0.5)

# ================= 2. Thirds, not halves =================
card('2. Thirds, not halves', 13)
# 14 "It's tempting to reach for a long top because it feels safe, and then wonder why the outfit looks heavy."   (her own "don't", 1/2)
# 15 "A top that ends mid-thigh divides you into two equal halves, so the eye stops right in the middle. The eye loves thirds: ..."
# 16 "Where that line falls depends on your torso. Here's a quick test. Place both hands flat, one above the other, right under your bust. ..."
# 17 "A longer torso looks lovely with high-rise trousers and a tucked top or a shorter jacket. A shorter torso feels best in a mid rise, ..."
# 18 "Either way, skip low rise. It cuts you in half at the widest part of the hips."
# 19 "And if a tuck doesn't suit your bust or your tummy, a fitted jacket that ends just above the hip bone creates the same thirds."   (the same woman, her "do")
# 20 "Get the thirds right, and the whole outfit looks intentional, without changing a thing about you."
t16 = at(16, 'Place both hands'); t16b = at(16, 'If they cover')
demo([(C('thirds1', 3.0, 8.7), after(13)), (C('thirds9', 5.0, 11.3), st(15) - 0.1), (C('thirds9', 11.5, 21.5), at(15, 'The eye loves thirds')),
      (C('torso23', 9.3, 15.0), st(16) - 0.1), (C('torso23', 15.0, 27.5), t16, 1.0),
      (C('longtorso4', 11.0, 21.0), st(17) - 0.1), (C('shorttorso39', 22.0, 28.5), at(17, 'A shorter torso')),
      (C('lowrise23', 5.5, 11.6), st(18) - 0.1, 1.0), (C('thirds1', 9.6, 19.0), st(19) - 0.1), (C('jacket33', 6.6, 11.0), st(20) - 0.1)], en(20) + 0.6)
ring(*PT('torso23', 300, 825), 250, 80, t16 + 0.9, en(16))
for k_, (txt, w_) in enumerate([('covers it: short torso', 'short'), ('at the edge: balanced', 'balanced'), ('below: long torso', 'long.')]):
    tg(txt, 760 + k_ * 72, at(16, w_) - 0.2, en(16))
L('lowrise23', 95, 260, 770, at(18, 'skip low rise'), en(18))
tg('low rise', PT('lowrise23', 0, 770)[1] + 24, at(18, 'skip low rise') + 0.2, en(18))
kicker('thirds, not halves', after(13), en(20) + 0.5)
steps([('no', 'a top to mid-thigh', at(15, 'two equal halves')), ('yes', 'one third top, two below', at(15, 'The eye loves thirds')),
       ('yes', 'both hands under the bust', t16), ('yes', 'long torso: high rise', at(17, 'high-rise')),
       ('yes', 'short torso: mid rise', at(17, 'mid rise')), ('no', 'low rise', at(18, 'skip low rise'))], en(20) + 0.5)

# ================= 3. Show your narrowest point =================
card('3. Show your narrowest point', 21)
# 22 "When we don't love a part of our body, it's tempting to cover everything in loose clothes."
# 23 "But fabric that hangs straight down from your fullest point makes you look wider all over, because the eye can't find your shape."
# 24 "Elegant women don't hide. They let one narrow point show."   (the hook woman, fixed)
# 25 "Mark a clear waist with a classic wrap dress or a belted coat. If you're fuller through the middle, mark the narrow place just under
#     your bust, with an empire line. And if your waist is straighter, let a peplum or a structured jacket create the shape, rather than a belt."
# 26 "It starts underneath. A well-fitted bra, wired or soft, lifts and gives you back the space between your bust and your waist."
# 27 "And for a dress you already own, turn it inside out, pin a safety pin on each side seam at the waist, thread a soft ribbon through both, ..."
# 28 "One clear point of shape, and you look at ease in your clothes instead of lost in them."
t23 = at(23, 'hangs straight down')
demo([(C('wrapdress13', 0.3, 6.4), after(21)), (C('loosedress2', 1.0, 1.0), st(23) - 0.1, 1.06), (C('frustrated15', 0.1, 3.6), at(23, 'makes you look wider')),
      (C('loosedress11', 5.8, 8.8), st(24) - 0.1, 1.0), (C('wrapdress13', 8.5, 20.0), st(25) - 0.1),
      (C('empire18', 4.3, 9.4), at(25, "If you're fuller"), 1.0), (C('peplum13', 0.0, 8.8), at(25, 'And if your waist')),
      (C('brafit40', 104.0, 113.0), st(26) - 0.1), (C('loosedress19', 6.0, 16.5), st(27) - 0.1), (C('loosedress19', 19.0, 25.0), st(28) - 0.1)], en(28) + 0.6)
for x_ in (165, 455):
    a_ = PT('loosedress2', x_, 470); b_ = PT('loosedress2', x_, 820); vline(a_[0], a_[1], b_[1], t23, at(23, 'makes you look wider') - 0.4, dash=True)
tg('hangs from the fullest point', PT('loosedress2', 0, 860)[1], t23 + 0.3, at(23, 'makes you look wider') - 0.4)
ring(*PT('loosedress11', 372, 670), 92, 58, at(24, 'one narrow point'), en(24))
L('empire18', 270, 430, 540, at(25, 'just under'), at(25, 'And if your waist') - 0.45)
tg('just under the bust', PT('empire18', 0, 540)[1] - 70, at(25, 'just under') + 0.2, at(25, 'And if your waist') - 0.45)
kicker('your narrowest point', after(21), en(28) + 0.5)
steps([('no', 'loose all over', t23), ('yes', 'clear waist: a wrap dress', at(25, 'classic wrap dress')),
       ('yes', 'fuller middle: under the bust', at(25, 'just under')), ('yes', 'straighter: peplum, structure', at(25, 'peplum')),
       ('yes', 'a bra that lifts', at(26, 'lifts')), ('yes', 'the safety-pin trick', at(27, 'pin a safety pin'))], en(28) + 0.5)

# ================= 4. Lead the eye to what you love =================
card('4. Lead the eye to what you love', 29, style='font-size:104px')
# 30 "Many of us were taught to hide the part we like least. But colour, pattern and detail draw the eye first, so wherever you place them, ..."
# 31 "So put the detail where you love, and keep everything else calm."
# 32 "Wider hips? Wear the print, the lighter colour and the earrings on top, with darker trousers. Wider shoulders? Try the opposite: a simple top,
#     with the colour and a wide leg below. Fuller through the middle? Bring the detail up to your face, with earrings or a scarf, because it draws the eye up."
# 33 "And if you love your shoulders or your hips, show them off, with confidence. These are choices, never rules."
demo([(C('earrings16', 6.0, 14.8), after(29)), (C('earrings5', 0.0, 5.5), st(31) - 0.1),
      (C('pearshape22', 62.5, 70.0), st(32) - 0.1), (C('halter24', 13.7, 21.0), at(32, 'Wider shoulders')),
      (C('appletips43', 3.0, 12.0), at(32, 'Fuller through')), (C('halter24', 27.0, 35.0), st(33) - 0.1)], en(33) + 0.4)
kicker('lead the eye', after(29), en(33) + 0.3)
steps([('yes', 'the detail where you love', st(31)), ('yes', 'wider hips: detail on top', st(32)),
       ('yes', 'wider shoulders: below', at(32, 'Wider shoulders')), ('yes', 'fuller middle: by your face', at(32, 'Fuller through')),
       ('yes', 'love it? show it', st(33))], en(33) + 0.3)
# 34 "Tell us in the comments, which shape are you closest to, or are you a blend?"
text('which shape are you <i>closest to</i>?', 'q1', st(34) - 0.1, en(34) + 0.35, style='top:400px')
text('or are you a <i>blend</i>?', 'q2', at(34, 'or are you'), en(34) + 0.35, style='top:520px')
# 35 guide plug, 9 s, at the END of the point, the next number card right after it
canvas_full(C('cream23', 3.5, 8.2), st(35) - 0.2, at(35, 'our personal stylist') + 0.2, fin=0.5)
canvas_full(C('tonal12', 12.5, 18.0), at(35, 'our personal stylist') + 0.2, en(35) + 0.6, fin=0.5)
i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, at(35, 'our personal stylist'), 0.8); fade_out(i, en(35) + 0.6, 0.5)
text('Check the description for', 'gtx1', at(35, 'our personal stylist') + 0.5, en(35) + 0.55, dur=1.1)
text('Personal stylist guide', 'gtx2', at(35, 'our personal stylist') + 0.9, en(35) + 0.55, dur=1.6)

# ================= 5. One colour, top to toe =================
card('5. One colour, top to toe', 36)
# 37 "A crisp white blouse with black trousers is classic, and it can be beautiful."
# 38 "But a strong colour break at the waist or the hips draws a line straight across you, and that's exactly where the eye stops."
# 39 "One colour, or close tones of one colour, creates one long line from top to toe."
# 40 "Try navy with navy, a soft beige knit with beige trousers, or cream with ivory, and mix textures, so it looks rich, never flat."
# 41 "Then add a long cardigan or coat, worn open, to frame the column. And the layer underneath still works when the coat comes off."
# 42 "And if you love contrast, keep it. Just add a jacket or a scarf that ties the two colours together."
# 43 "It's timeless, it feels effortless and polished, and it's the easiest outfit you'll put together all week."
t38 = at(38, 'draws a line'); t39 = at(39, 'creates one long line')
demo([(C('scarf29', 7.4, 10.4), after(36)), (C('mono27', 5.5, 7.0), at(37, 'and it can')), (C('scarf29', 4.8, 7.4), st(38) - 0.1, 1.0), (C('frustrated15', 5.6, 9.4), at(38, 'straight across')),
      (C('mono11', 1.9, 3.5), st(39) - 0.1), (C('mono11', 3.5, 3.5), st(39) + 2.1, 1.06),
      (C('mono11', 5.2, 9.2), at(40, 'navy with navy')), (C('mono11', 10.0, 13.4), at(40, 'soft beige knit')),
      (C('cream23', 0.0, 3.5), at(40, 'cream with ivory')), (C('tonal12', 9.0, 12.2), at(40, 'mix textures')),
      (C('coatopen8', 0.1, 3.3), st(41) - 0.1), (C('coatopen14', 6.6, 9.8), at(41, 'to frame')), (C('mono27', 0.0, 5.4), at(41, 'And the layer')), (C('scarf27', 2.0, 9.0), st(42) - 0.1), (C('scarf27', 13.0, 21.7), at(42, 'Just add')),
      (C('cream14', 0.0, 5.4), st(43) - 0.1), (C('tonal12', 0.0, 6.0), at(43, 'easiest'))], en(43) + 0.6)
L('scarf29', 60, 480, 840, t38, at(38, 'straight across') - 0.4, dash=True)
tg('the eye stops here', PT('scarf29', 0, 840)[1] + 26, t38 + 0.3, at(38, 'straight across') - 0.4)
a_ = PT('mono11', 372, 330); b_ = PT('mono11', 372, 1210); vline(a_[0], a_[1], b_[1], t39, en(39) + 0.2)
kicker('one colour', after(36), en(43) + 0.5)
steps([('no', 'a break at the waist', t38), ('yes', 'one colour, top to toe', t39), ('yes', 'mix textures', at(40, 'mix textures')),
       ('yes', 'a long layer, open', at(41, 'worn open')), ('yes', 'contrast? tie it together', at(42, 'ties the two'))], en(43) + 0.5)

# ================= 6. Open the neckline =================
card('6. Open the neckline', 44)
# 45 "It can feel safer to cover up with a high neck, especially with a full bust."   (one woman: turtleneck -> wrap V -> blazer)
# 46 "But a high, closed neck makes the upper body look shorter and fuller, and the eye goes to the chest instead of your face."
# 47 "A little open space at the neck brings the eye up to your face."
# 48 "Choose a soft V, a scoop, a square neck or a wrap. A light V-neck knit or a classic wrap top suits almost every shape."
# 49 "And if you prefer more coverage, keep your crew neck and add a long pendant necklace. It creates the same long V."
# 50 "When people see your face first, you feel seen, and you carry yourself with quiet confidence."
t46 = at(46, 'closed neck')
demo([(C('bigbust3', 12.0, 16.4), after(44)), (C('bigbust3', 13.0, 13.0), st(46) - 0.1, 1.07), (C('bigbust3', 26.9, 31.6), st(47) - 0.1),
      (C('bigbust50_8', 2.0, 6.0), at(48, 'a soft V')), (C('squareneck33', 0.3, 3.5), at(48, 'a scoop')),
      (C('inv50_21', 0.0, 3.5), at(48, 'a square neck')), (C('wrapdress5', 2.3, 6.0), at(48, 'or a wrap')),
      (C('bigbust50_8', 12.0, 18.0), at(48, 'A light V-neck')), (C('pendant22', 0.3, 7.6), st(49) - 0.1),
      (C('bigbust3', 34.5, 41.0), st(50) - 0.1)], en(50) + 0.6)
ring(*PT('bigbust3', 350, 545), 105, 62, t46, en(46))
tg('closed neck', PT('bigbust3', 0, 545)[1] - 110, t46 + 0.2, en(46))
for w_, lab in [('a soft V', 'soft V'), ('a scoop', 'scoop'), ('a square neck', 'square'), ('or a wrap', 'wrap')]:
    nx = {'a soft V': 'a scoop', 'a scoop': 'a square neck', 'a square neck': 'or a wrap', 'or a wrap': 'A light V-neck'}[w_]
    tg(lab, 150, at(48, w_) + 0.15, at(48, nx) - 0.05)
kicker('open the neckline', after(44), en(50) + 0.5)
steps([('no', 'high, closed neck', t46), ('yes', 'a little open space', st(47)), ('yes', 'soft V, scoop, square, wrap', at(48, 'a soft V')),
       ('yes', 'or a long pendant', at(49, 'long pendant'))], en(50) + 0.5)

# ================= 7. Fine knits, not chunky =================
card('7. Fine knits, not chunky', 51)
# 52 "We get it. A chunky knit feels so cosy when the weather turns cold."
# 53 "But thick cable knits, padding and fur add their own width on top of yours, often right where you're fullest."   (one woman: cable knit, then padding)
# 54 "Let the fabric skim your shape, never add to it."
# 55 "Choose fine knits, like a light cashmere or a thin wool, and fabrics that drape, like crepe and fine linen. Before you buy, hold it, move it, and see how it falls."
# 56 "On a really cold day, warmth comes first. A fine knit under a warm coat keeps you cosy without the bulk."
# 57 "And if your hips are wider than your shoulders, a chunky knit on top can be lovely, because it adds volume where you're narrower."
# 58 "Soft fabric moves with you, so you feel comfortable and graceful from morning to night."
demo([(C('chunky41', 0.0, 6.3), after(51)), (C('chunky40', 2.0, 9.5), st(53) - 0.1), (C('chunky40', 11.0, 13.7), at(53, 'padding')),
      (C('fineknit25', 8.5, 12.8), at(53, 'often right')), (C('fineknit25', 13.0, 22.0), st(55) - 0.1), (C('fineknit29', 2.0, 5.5), at(55, 'Before you buy')),
      (C('coatopen14', 0.0, 6.4), st(56) - 0.1), (C('chunky43', 8.0, 12.6), st(57) - 0.1), (C('chunky41', 6.3, 8.5), at(57, 'because it adds')), (C('fineknit29', 5.6, 10.5), st(58) - 0.1)], en(58) + 0.6)
tg('thick cable knit', 150, at(53, 'thick cable') + 0.1, at(53, 'padding') - 0.05)
tg('padding', 150, at(53, 'padding') + 0.15, en(53))
kicker('fine knits', after(51), en(58) + 0.5)
steps([('no', 'thick cable knit, padding', at(53, 'thick cable')), ('yes', 'fine knits that skim', st(54)),
       ('yes', 'hold it, move it', at(55, 'hold it')), ('yes', 'cold? fine knit, warm coat', at(56, 'A fine knit under')),
       ('yes', 'wider hips: chunky on top', at(57, 'chunky knit on top'))], en(58) + 0.5)

# ================= 8. Shoes that continue the line =================
card('8. Shoes that continue the line', 59, style='font-size:104px')
# 60 "It's easy to choose shoes last."   (one woman, her own crosses and ticks)
# 61 "But a shoe in strong contrast, or a strap across the ankle, ends the leg in one hard stop, and the eye drops to your feet."
# 62 "The shoe should continue the line, not stop it."
# 63 "With trousers, choose the same colour family, navy with navy, black with black. With skirts and dresses, a shade close to your skin tone feels like part of the leg."
# 64 "And you don't need heels. A pointed-toe flat, a low block heel or a sleek loafer continues the line just as well."
# 65 "If your feet need a wider strap or a rounder toe, comfort comes first. Choose it in your skin tone or your trouser colour, and let the colour do the work."
# 66 "When nothing stops the eye, you look finished from head to toe, and you walk with ease."
t61 = at(61, 'one hard stop'); t62 = at(62, 'continue the line')
demo([(C('shorttorso32', 0.1, 4.6), after(59)), (C('shorttorso32', 8.4, 13.9), st(61) - 0.1, 1.0),
      (C('loafers29', 0.3, 9.3), en(61) - 0.2), (C('anklestrap10', 17.9, 26.0), at(63, 'With skirts')),
      (C('flats31', 0.3, 7.8), st(64) - 0.1), (C('flats1', 1.0, 7.5), at(64, 'A pointed-toe flat')),
      (C('sandals5', 0.0, 6.0), st(65) - 0.1), (C('sandals17', 1.0, 6.5), at(65, 'Choose it')), (C('flats31', 9.3, 15.5), st(66) - 0.1)], en(66) + 0.6)
ring(*PT('shorttorso32', 150, 1180), 90, 60, t61, en(61) - 0.5)
tg('hard stop', PT('shorttorso32', 0, 1180)[1] - 120, t61 + 0.2, en(61) - 0.5)
tg('one long line', 150, st(62) + 0.3, en(62) + 0.2)
kicker('shoes', after(59), en(66) + 0.5)
steps([('no', 'a hard stop at the ankle', t61), ('yes', 'trousers: same colour', st(63)), ('yes', 'skirts: your skin tone', at(63, 'skin tone')),
       ('yes', 'no heels needed', at(64, "don't need heels")), ('yes', 'comfort first, colour works', at(65, 'comfort comes first'))], en(66) + 0.5)

# ================= recap 67-75: each point's woman comes back as its name is said, the list ticks =================
white(en(66) + 0.35, st(67) + 0.5)
demo([(C('samedress23', 0.0, 3.8), st(67) - 0.1), (C('shapetest0', 30.0, 33.0), st(68) - 0.1), (C('thirds9', 22.0, 24.5), st(69) - 0.1),
      (C('loosedress19', 16.5, 19.0), st(70) - 0.1), (C('halter24', 22.0, 26.0), st(71) - 0.1), (C('mono11', 19.8, 23.0), st(72) - 0.1),
      (C('bigbust50_8', 19.0, 22.0), st(73) - 0.1), (C('fineknit25', 24.0, 28.0), st(74) - 0.1), (C('flats31', 16.0, 21.0), st(75) - 0.1)],
     en(75) + 0.6, x0=250)
items = ['find your shape', 'thirds, not halves', 'show your narrowest point', 'lead the eye to what you love',
         'one colour, top to toe', 'open the neckline', 'fine knits, not chunky', 'shoes that continue the line']
for k, txt in enumerate(items):
    tt = st(68 + k) - 0.1; i = nid('ck')
    els.append(f'<div id="{i}" class="chk" style="top:{118 + k*104}px;opacity:0"><svg viewBox="0 0 54 54"><path id="{i}p" d="M12 28 L23 39 L42 15"/></svg>{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,x:-24}},{{opacity:1,x:0,duration:0.7,ease:"power2.out"}},{tt:.3f});')
    tw.append(f'tl.to("#{i}p",{{strokeDashoffset:0,duration:0.5,ease:"power2.out"}},{tt+0.3:.3f});')
    fade_out(i, en(75) + 0.6, 0.6)

# ================= close =================
# 76 "None of these ask you to change your body, and you don't need a new wardrobe. They're timeless, so try just one this week, with what you already own, and notice how you feel."
row([C('mirror50_29', 1.0, 13.0), C('appleshape35', 0.0, 12.0), C('mirror50_15', 10.0, 20.0)],
    [st(76) - 0.1, at(76, 'a new wardrobe'), at(76, "They're timeless")], at(76, 'and notice') - 0.1)
# 77 "What's one thing that works on your shape, something you learned yourself or from the women in your family? Tell us in the comments, ..."
demo([(C('mirror50_29', 14.0, 20.0), at(76, 'and notice') - 0.3), (C('olderyounger34', 0.0, 8.0), at(77, 'from the women')),
      (C('olderyounger23', 0.0, 7.6), at(77, 'Tell us'))], en(77) + 0.3)
text('what works on <i>your</i> shape?', 'qr1', st(77) - 0.1, en(77) + 0.2, style='left:1010px;top:400px;font-size:60px')
text('tell us in the comments', 'qr2', at(77, 'Tell us'), en(77) + 0.2, style='left:1010px;top:520px;font-size:48px')
# 78 "A simple like or comment would mean so much to us. Until next time, bye everyone."
canvas_full(C('loafers29', 9.5, 14.1), st(78) - 0.2, at(78, 'Until next time'), fin=0.6)
canvas_full(C('jacket33', 12.2, 16.5), at(78, 'Until next time'), total - 2.6, fin=0.6)
