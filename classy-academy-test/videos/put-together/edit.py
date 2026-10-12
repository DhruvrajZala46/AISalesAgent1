# 8 Ways to Always Look Put Together — the edit, beat by beat.
# Every clip segment was checked on its shot sheet (see ok.txt); each clip is used once; no AI clips.

# ================= HOOK =================
# 1 "Before you buy one more outfit, stop. Which 8 quiet habits make some women always look put together, and why do they cost you almost nothing?"
canvas_full(C('closet1', 0, 40.1), 0.0, wd(1, 0.36), fin=0.01)
canvas_full(C('coffeewalk20', 0, 6.87), wd(1, 0.36), en(1) + 0.3)
text('8 quiet <i>habits</i>', 'hint', wd(1, 0.4), wd(1, 0.78), dur=1.1, out=0.45)
# 2 "Have you ever passed a woman in a simple sweater and plain trousers, and thought, she looks completely put together?"
canvas_full(C('sweaterst24', 0, 12.33), st(2) - 0.1, en(2) + 0.3)
# 3 "Nothing she's wearing is expensive, and yet everything about her feels intentional."
row([C('sweaterst33', 0, 6.4), C('bwchic19', 0, 7.78), C('over60_16', 0, 12.84)], [st(3), wd(3, 0.3), wd(3, 0.58)], en(3) + 0.35)
# 4 "It isn't money. It isn't being born beautiful. And it isn't hours in front of the mirror."
quote_side(C('sweaterst35', 0, 13.35), st(4) - 0.1, en(4) + 0.45, "It isn't money,", 'or <i>perfect</i> looks.', wd(4, 0.4))
# 5 "It's a few quiet habits, and the belief that you're worth them."
canvas_full(C('watch3', 0, 14.3), st(5) - 0.1, en(5) + 0.3)
text("you're <i>worth</i> them", 'hint', wd(5, 0.45), en(5) + 0.25, dur=1.0, out=0.4)

# 6 "In today's video, we're sharing 8 ways to always look put together, at any age, on any budget, with what you already own."
white(en(5) + 0.45, st(6) + 1.6)
text("in today's video...", 'card', st(6) - 0.05, st(6) + 1.45, dur=1.0, out=0.4)
canvas_full(C('golden10', 0, 6.2), st(6) + 1.5, wd(6, 0.6), fin=0.6)
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Episode 10</div><div class="big">8 Ways to Always Look Put Together</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.2,ease:"power2.out"}},{st(6)+1.9:.3f});'); fade_out(i, wd(6, 0.6) - 0.1, 0.5)
row([C('over60_40', 0, 40.1), C('thirdpiece9', 0, 14.57), C('jeansblazer15', 1.13, 12.19)], [wd(6, 0.6), wd(6, 0.7), wd(6, 0.8)], en(6) + 0.4,
    labels=['at any age', 'any budget', 'what you own'])
# 7 "Some of these may surprise you, but once you see them, you'll never unsee them. Let's get started."
single(C('sweaterst38', 0, 9.67), st(7) - 0.05, wd(7, 0.58))
pair([C('midiskirt17', 0.6, 5.9), C('creambrown40', 0, 7.8)], [wd(7, 0.58), wd(7, 0.72)], en(7) + 0.4)

# ================= 1. Decide your outfits once =================
card('1. Decide your outfits once', 8)
# 9 "We get it. Mornings start in a rush, and in front of a full closet, it can feel like you have nothing to wear."
canvas_full(C('closet5', 0, 10.0), en(8) + 0.3, en(9) + 0.3)
# 10 "So you grab whatever is closest, and the outfit looks exactly that, rushed."
pair([C('closet36', 8.63, 15.87), C('rush47', 0, 4.03)], [st(10) - 0.05, wd(10, 0.62)], en(10) + 0.4)
# 11 "Women who always look put together aren't more talented. They simply decided in advance."
quote_side(C('trouserknit34', 6.47, 16.69), st(11) - 0.1, en(11) + 0.45, 'Not more talented.', 'They <i>decided</i> in advance.', wd(11, 0.5))
# 12 "Elegant women tend to have a few outfit formulas they know work, a quiet personal uniform."
row([C('layout26', 0, 12.96), C('layout7', 2.17, 9.2), C('layout4', 0.5, 3.73)], [st(12) - 0.05, wd(12, 0.3), wd(12, 0.55)], en(12) + 0.4)
text('a quiet personal <i>uniform</i>', 'hint', wd(12, 0.72), en(12) + 0.35, dur=1.1, style='top:900px;font-size:80px')
# 13 "Try this. On a calm afternoon, put together three outfits you love from what you already own."
single(C('sweaterst8', 0, 9.37), st(13) - 0.05, en(13) + 0.4)
# 14 "Straight trousers, a fine knit and loafers. A midi skirt, a soft sweater and boots. Dark jeans, a white shirt and a blazer."
row([C('trouserknit27', 0, 7.87), C('midiskirt1', 0, 6.03), C('jeansblazer21', 0, 14.6)], [st(14) - 0.05, wd(14, 0.36), wd(14, 0.68)], en(14) + 0.4,
    labels=['trousers, knit, loafers', 'midi skirt + sweater', 'jeans + blazer'])
# 15 "Take a photo of each, shoes and bag included. On a rushed morning, you simply choose."
pair([C('fullmirror15', 3.67, 9.43), C('mselfie20', 1.23, 6.93)], [st(15) - 0.05, wd(15, 0.42)], en(15) + 0.4)
# 16 "It's not about more clothes. It's about calm mornings, and leaving the house feeling like yourself."
canvas_full(C('doorway19', 0, 6.72), st(16) - 0.1, wd(16, 0.52))
canvas_full(C('coffeewalk0', 0, 4.5), wd(16, 0.52), en(16) + 0.3)
text('calm <i>mornings</i>', 'hint', wd(16, 0.3), wd(16, 0.62), dur=1.0, out=0.4)
# 17 "What's your go-to outfit? Tell us in the comments."
quote_side(C('sweaterst13', 0, 11.1), st(17) - 0.1, en(17) + 0.5, "What's your", '<i>go-to</i> outfit?', wd(17, 0.25))

# ================= 2. A closet that goes together =================
card('2. A closet that goes together', 18)
# 19 "Colour is a beautiful part of getting dressed, and you never have to give up the colours you love."
canvas_full(C('colour2_12', 0, 13.43), en(18) + 0.3, wd(19, 0.5))
single(C('colour2_23', 0, 18.73), wd(19, 0.5), en(19) + 0.35)
# 20 "But when every piece speaks a different language, getting dressed becomes a puzzle every morning."
canvas_full(C('messycloset41', 0, 20.57), st(20) - 0.1, wd(20, 0.55))
canvas_full(C('closet13', 0, 3.97), wd(20, 0.55), en(20) + 0.3)
# 21 "A put together look starts in the closet."
canvas_full(C('closetopen14', 0, 5.17), st(21) - 0.1, en(21) + 0.3)
text('it starts in the <i>closet</i>', 'hint', wd(21, 0.25), en(21) + 0.25, dur=1.0, out=0.4)
# 22 "Women who always look polished build on two or three timeless base colours, and add the colours they love on top."
single(C('closetopen20', 2.23, 9.03), st(22) - 0.05, en(22) + 0.35)
# 23 "Choose your base. Navy and camel. Cream and chocolate brown. Black and grey."
text('choose your <i>base</i>', 'hint', st(23) - 0.05, wd(23, 0.24), dur=0.9, out=0.35)
row([C('navycamel15', 1.8, 9.2), C('creambrown26', 1.27, 5.7), C('blackgrey12', 0, 29.0)], [wd(23, 0.24), wd(23, 0.5), wd(23, 0.76)], en(23) + 0.4,
    labels=['navy + camel', 'cream + chocolate', 'black + grey'])
# 24 "Then pick one or two colours that make you glow, like burgundy, sage or soft blue, as your accents."
single(C('creambrown4', 3.5, 8.43), st(24) - 0.05, wd(24, 0.46))
row([C('burgundy13', 0, 5.03), C('sage4', 0, 8.0), C('watch27', 0, 13.78)], [wd(24, 0.46), wd(24, 0.58), wd(24, 0.7)], en(24) + 0.4,
    labels=['burgundy', 'sage', 'soft blue'])
# 25 "Before you buy anything new, ask, does this go with three things I already own?"
quote_side(C('sweaterst45', 0, 15.48), st(25) - 0.1, en(25) + 0.45, 'Does it go with', '<i>three</i> things I own?', wd(25, 0.45))
# 26 "Suddenly almost everything works together. Fewer decisions, more ease."
canvas_full(C('trouserknit25', 3.97, 17.1), st(26) - 0.1, en(26) + 0.4)
text('more <i>ease</i>', 'hint', wd(26, 0.62), en(26) + 0.35, dur=1.0, out=0.4)

# ================= 3. Finish the outfit =================
card('3. Finish the outfit', 27)
# 28 "Have you ever put on an outfit where everything matches, yet something still feels missing?"
canvas_full(C('plaintee12', 0, 6.3), en(27) + 0.3, en(28) + 0.3)
# 29 "There's nothing wrong with it, it's just unfinished. A finished outfit looks chosen. An unfinished one looks grabbed."
single(C('sleeves42', 0, 16.4), st(29) - 0.05, wd(29, 0.5))
compare(C('plaintee26', 0, 35.79), C('sweaterst10', 0, 6.0), 'grabbed', 'chosen', wd(29, 0.5), wd(29, 0.66), en(29) + 0.4)
# 30 "The finish takes thirty seconds. Tuck just the front of your top to show your waist."
single(C('tuck41', 0, 10.42), st(30) - 0.05, wd(30, 0.45))
pair([C('tuck45', 0, 29.41), C('over60_42', 0, 40.1)], [wd(30, 0.45), wd(30, 0.62)], en(30) + 0.4, labels=['a front tuck', None])
# 31 "Push your sleeves just below the elbow. Add a slim belt in the same colour family as your shoes."
pair([C('sleeves38', 0, 15.95), C('belt0', 1.24, 6.04)], [st(31) - 0.05, wd(31, 0.48)], en(31) + 0.4, labels=['sleeves pushed up', 'a slim belt'])
# 32 "And if a tuck doesn't feel comfortable, that's completely fine. Instead, wear a third piece open, a shirt, a blazer or a long fine cardigan."
canvas_full(C('over60_23', 0, 40.1), st(32) - 0.1, wd(32, 0.44))
row([C('jeansblazer25', 0, 13.6), C('thirdpiece15', 0, 5.83), C('belt26', 0, 6.34)], [wd(32, 0.44), wd(32, 0.62), wd(32, 0.8)], en(32) + 0.4)
# 33 "The open edges draw two long lines from your shoulders down, and the look instantly feels more structured."
canvas_full(C('thirdpiece0', 19.53, 31.98), st(33) - 0.1, en(33) + 0.4)
# 34 "Then add one small detail, gold earrings or a timeless watch, and stop there."
single(C('necklace49', 0, 3.4), st(34) - 0.05, wd(34, 0.34))
pair([C('earrings3', 0, 6.75), C('watch24', 0, 8.97)], [wd(34, 0.34), wd(34, 0.55)], en(34) + 0.4, labels=['gold earrings', 'a timeless watch'])
# 35 "These tiny touches tell the world, and remind you, that you showed up with intention."
canvas_full(C('watch4', 0, 9.54), st(35) - 0.1, en(35) + 0.4)
text('with <i>intention</i>', 'hint', wd(35, 0.6), en(35) + 0.35, dur=1.0, out=0.4)

# ================= mid-roll: the stylist guide =================
text('the secret...', 'hint', st(36) - 0.05, wd(36, 0.28), dur=1.0, out=0.4)
pair([C('midiskirt34', 2.37, 12.33), C('navycamel9', 0, 52.1)], [wd(36, 0.28), wd(36, 0.45)], en(36) + 0.4)
canvas_full(C('golden4', 0, 6.3), st(37) - 0.1, en(37) + 0.6, fin=0.8)
i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, st(37), 0.9); fade_out(i, en(37) + 0.6, 0.55)
text('Check the description for', 'gtx1', st(37) + 0.7, en(37) + 0.55, dur=1.1); text('Elegant women style guide', 'gtx2', st(37) + 1.1, en(37) + 0.55, dur=1.7)

# ================= 4. Stay ready =================
card('4. Stay ready', 38)
# 39 "We've all been there. You find the perfect top, then notice the crease or the loose button."
canvas_full(C('shelf1', 2.2, 6.87), en(38) + 0.3, wd(39, 0.45))
pair([C('wrinkle5', 0, 2.5), C('sew2_44', 2.7, 16.27)], [wd(39, 0.45), wd(39, 0.78)], en(39) - 0.25, labels=['the crease', 'the loose button'])
# 40 "Those small details quietly take away from everything else you did right."
canvas_full(C('wrinkle19', 0, 1.97), st(40) - 0.1, wd(40, 0.4))
single(C('shoeclean31', 0, 8.87), wd(40, 0.4), en(40) + 0.35)
# 41 "Women who always look put together don't start from scratch every morning. Their clothes are ready and waiting."
single(C('pill8', 28.37, 34.4), st(41) - 0.05, en(41) + 0.2)
text('ready and <i>waiting</i>', 'hint', wd(41, 0.66), en(41) + 0.2, dur=1.0, out=0.35, style='top:900px;font-size:80px')
# 42 "Try this. Once a week, take ten minutes to steam what you'll wear, lint-roll your coat, wipe your shoes and sew that button back on."
text('ten minutes, once a <i>week</i>', 'hint', st(42) - 0.05, wd(42, 0.3), dur=1.1, out=0.4)
row([C('wrinkle30', 0, 16.73), C('lint2_37', 1.75, 19.19), C('shoeclean1', 11.0, 18.97), C('sew2_0', 6.83, 9.83)],
    [wd(42, 0.3), wd(42, 0.5), wd(42, 0.66), wd(42, 0.82)], en(42) + 0.4, labels=['steam', 'lint roll', 'wipe', 'sew'])
# 43 "Keep a tiny sewing kit and a lint roller by the door."
pair([C('sewkit11', 0, 23.69), C('lint2_1', 1.87, 8.9)], [st(43) - 0.05, wd(43, 0.5)], en(43) + 0.4, labels=['a tiny sewing kit', 'a lint roller'])
# 44 "Empty your bag every few days, so it keeps its shape."
pair([C('bagempty42', 0, 8.17), C('bagempty24', 7.53, 14.37)], [st(44) - 0.05, wd(44, 0.5)], en(44) + 0.4)
# 45 "And when a piece is truly tired, faded or pilled, let it go with gratitude."
text('when a piece is <i>tired</i>', 'q1', st(45) - 0.05, wd(45, 0.3) + 0.15, dur=1.0)   # no empty backdrop before the clip
single(C('pill2', 0, 1.8), wd(45, 0.3), wd(45, 0.6))
canvas_full(C('knitset13', 0.77, 4.33), wd(45, 0.6), en(45) + 0.3)
text('with <i>gratitude</i>', 'hint', wd(45, 0.72), en(45) + 0.3, dur=1.0, out=0.4)
# 46 "A small ritual, and every morning begins with ease, because everything is ready."
canvas_full(C('wfh17', 0, 9.27), st(46) - 0.1, en(46) + 0.4)
text('everything is <i>ready</i>', 'hint', wd(46, 0.62), en(46) + 0.35, dur=1.0, out=0.4)

# ================= 5. Hair that looks done in five minutes =================
card('5. Hair, done in five minutes', 47)
# 48 "We get it, mornings are busy, and your hair doesn't need a salon or an hour of your time."
canvas_full(C('trim5', 0, 15.02), en(47) + 0.3, wd(48, 0.5))
canvas_full(C('clawclip24', 0, 11.1), wd(48, 0.5), en(48) + 0.3)
# 49 "But your hair frames your face. When it looks cared for, even a simple sweater looks intentional."
single(C('lowbun22', 3.63, 15.13), st(49) - 0.05, en(49) + 0.4)
# 50 "Done doesn't mean perfect. It means cared for."
quote_side(C('ponytail7', 0, 19.83), st(50) - 0.1, en(50) + 0.5, "Done isn't perfect.", "It's <i>cared for</i>.", wd(50, 0.48))
# 51 "Choose one five-minute style. A low bun, smooth at the front. A sleek low ponytail, a strand wrapped around the band. Or a twist held with a claw clip."
text('one five-minute <i>style</i>', 'hint', st(51) - 0.05, wd(51, 0.2), dur=1.0, out=0.35)
row([C('naturalbun41', 4.03, 25.3), C('ponytail28', 3.1, 13.17), C('clawclip7', 1.87, 22.27)], [wd(51, 0.2), wd(51, 0.42), wd(51, 0.78)], en(51) + 0.4,
    labels=['a low bun', 'a sleek ponytail', 'a claw clip twist'])
# 52 "With curly hair, refresh your curls with water and a little leave-in, and sleep with them loosely piled on top, on a satin pillowcase."
pair([C('curlspray0', 3.03, 15.43), C('pineapple0', 0, 11.33)], [st(52) - 0.05, wd(52, 0.55)], en(52) + 0.4, labels=['refresh with water', 'satin at night'])
# 53 "And keep your ends trimmed. Healthy ends make any style look polished."
pair([C('trim3', 0, 10.97), C('ponytail44', 0, 13.9)], [st(53) - 0.05, wd(53, 0.5)], en(53) + 0.4)
# 54 "When your hair feels done, you feel ready for the day."
canvas_full(C('clawclip3', 2.63, 25.6), st(54) - 0.1, en(54) + 0.4)

# ================= 6. The ten-second check =================
card('6. The ten-second check', 55)
# 56 "It's easy to check only your face, grab your keys and walk out of the door."
canvas_full(C('doorway21', 0, 4.74), en(55) + 0.3, en(56) + 0.3)
# 57 "But others see the whole picture, your shoes, your bag, even the back of your coat."
text('the <i>whole</i> picture', 'q1', st(57) - 0.05, wd(57, 0.38) + 0.15, dur=1.0)   # no empty backdrop before the row
row([C('shoeclean25', 0, 42.82), C('bagempty29', 1.0, 4.9), C('belt6', 0, 6.88)], [wd(57, 0.38), wd(57, 0.55), wd(57, 0.72)], en(57) + 0.4,
    labels=['your shoes', 'your bag', 'your coat'])
# 58 "Look at yourself the way the world will see you."
text('the way the <i>world</i> sees you', 'q1', st(58) - 0.05, en(58) + 0.4, dur=1.2)
# 59 "Step back from a full-length mirror, ideally in daylight. Look at the front, then turn around."
canvas_full(C('fullmirror8', 1.03, 8.93), st(59) - 0.1, en(59) + 0.35)
# 60 "Ask three quick questions. Does everything sit smoothly? Is anything fighting for attention? Does it look finished?"
single(C('fullmirror0', 0, 8.43), st(60) - 0.05, en(60) + 0.4)
for k_, (q_, f_) in enumerate([('does it sit <i>smoothly</i>?', 0.22), ('anything <i>competing</i>?', 0.52), ('does it look <i>finished</i>?', 0.78)]):
    text(q_, 'hint', wd(60, f_), wd(60, f_ + 0.27) if k_ < 2 else en(60) + 0.3, dur=0.9, out=0.3, style='top:880px;font-size:76px')
# 61 "If one thing feels like too much, take it off."
canvas_full(C('necklace37', 5.97, 17.0), st(61) - 0.1, en(61) + 0.3)
# 62 "And once in a while, take a photo. The camera shows what the mirror doesn't, and the outfits you love become your formulas."
single(C('mselfie40', 0, 6.0), st(62) - 0.05, wd(62, 0.6))
single(C('blackgrey29', 0, 12.05), wd(62, 0.6), en(62) + 0.4)
# 63 "Ten seconds, and you walk out without a single doubt."
canvas_full(C('gracewalk38', 0, 6.13), st(63) - 0.1, en(63) + 0.4)

# ================= 7. Carry it well =================
card('7. Carry it well', 64)
# 65 "Most of us spend our days bent over phones and desks, so it's completely natural to slouch."
canvas_full(C('slouch23', 0, 13.58), en(64) + 0.3, en(65) + 0.3)
# 66 "But when your shoulders round forward, even a beautiful blazer folds in on itself, and you can look tired before you say a word."
compare(C('wfh3', 0, 13.73), C('posture11', 0, 8.9), 'rounded', 'tall', st(66) - 0.05, wd(66, 0.5), en(66) + 0.4)
# 67 "Elegance isn't only worn. It's carried."
text("Elegance isn't only worn.", 'q1', st(67) - 0.05, en(67) + 0.5, dur=1.1, style='top:380px')
text("It's <i>carried</i>.", 'q1', wd(67, 0.55), en(67) + 0.5, dur=0.9, style='top:500px')
# 68 "Try this. Imagine a soft thread lifting the top of your head. Let your shoulders settle back and down, chin level."
canvas_full(C('posture37', 0, 12.55), st(68) - 0.1, en(68) + 0.3)
# 69 "Then walk a little slower than you think you need to."
canvas_full(C('gracewalk1', 7.8, 10.75), st(69) - 0.1, en(69) + 0.3)
# 70 "Every shop window you pass is your reminder."
pair([C('window11', 0, 9.97), C('window2', 0, 2.23)], [st(70) - 0.05, wd(70, 0.42)], en(70) + 0.1)
# 71 "And when you stand tall, you don't only look more confident. You start to feel it."
canvas_full(C('bwchic46', 0, 8.0), st(71) - 0.1, en(71) + 0.4)
text('you start to <i>feel</i> it', 'hint', wd(71, 0.6), en(71) + 0.35, dur=1.0, out=0.4)

# ================= 8. Wear your good things on ordinary days =================
card('8. Your good things, on ordinary days', 72)
# 73 "So many of us save a beautiful sweater, a favourite blouse or lovely shoes for someday."
canvas_full(C('shelf0', 0, 21.41), en(72) + 0.3, wd(73, 0.62))
single(C('necklace14', 0, 2.07), wd(73, 0.63), en(73) - 0.1)
# 74 "A special dinner, a trip, a better version of our life."
pair([C('dinner3', 0, 10.37), C('suitcase4', 2.77, 15.8)], [st(74) - 0.05, wd(74, 0.42)], en(74) + 0.35, labels=['a special dinner', 'a trip'])
# 75 "But someday rarely comes. Meanwhile, we spend our real days in the clothes we care about least, and slowly, that starts to feel like all we deserve."
canvas_full(C('homelazy4', 0, 40.17), st(75) - 0.1, en(75) + 0.3)
# 76 "Looking put together isn't for someone else. It's for you."
quote_side(C('curlspray13', 8.33, 16.57), st(76) - 0.1, en(76) + 0.5, "It isn't for anyone else.", "It's for <i>you</i>.", wd(76, 0.55))
# 77 "Women who always look put together don't wait for a reason. An ordinary Tuesday is reason enough."
canvas_full(C('market44', 0.97, 9.07), st(77) - 0.1, en(77) + 0.3)
text('an ordinary <i>Tuesday</i>', 'hint', wd(77, 0.55), en(77) + 0.25, dur=1.0, out=0.4)
# 78 "So this week, wear the nice sweater to the market. Put on earrings to work from home. Choose a soft knit set over the oldest t-shirt you own."
row([C('market41', 0, 15.11), C('mirrorsmile22', 0, 15.6), C('wfh16', 0, 13.77)], [st(78) - 0.05, wd(78, 0.38), wd(78, 0.7)], en(78) + 0.4)
# 79 "Because taking care of how you look is a quiet way of telling yourself, I am worth the effort. Today, not someday."
canvas_full(C('knitset0', 0, 7.53), st(79) - 0.1, en(79) + 0.4)
text('I am <i>worth</i> the effort', 'q1', wd(79, 0.45), en(79) + 0.4, dur=1.3)

# ================= recap 80-88: a checklist that builds, ✓ for each habit =================
white(en(79) + 0.45, st(80) + 0.6)
for s_, a_, b_ in [(C('styling45', 0, 40.1), st(80) + 0.3, st(84)), (C('lowbun2', 0, 12.2), st(84), st(87)), (C('tuck48', 0, 27.42), st(87), en(88) + 0.6)]:
    panel(s_, 170, 170 + PW, a_, b_, entry='fade')
items = ['decide your outfits once', 'a closet that goes together', 'finish the outfit', 'stay ready',
         'hair done in five minutes', 'the ten-second check', 'carry it well', 'your good things, every day']
for k, txt in enumerate(items):
    tt = st(81 + k); i = nid('ck')
    els.append(f'<div id="{i}" class="chk" style="top:{118 + k*104}px;opacity:0"><svg viewBox="0 0 54 54"><path id="{i}p" d="M12 28 L23 39 L42 15"/></svg>{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,x:-24}},{{opacity:1,x:0,duration:0.7,ease:"power2.out"}},{tt:.3f});')
    tw.append(f'tl.to("#{i}p",{{strokeDashoffset:0,duration:0.5,ease:"power2.out"}},{tt+0.3:.3f});')
    fade_out(i, en(88) + 0.6, 0.6)
# 89 "None of them need a big budget, a certain age or a certain size. Just timeless habits, a little intention, and the belief that you're worth it."
pair([C('bwchic33', 0, 38.83), C('over60_6', 0, 15.03)], [st(89) - 0.05, wd(89, 0.22)], wd(89, 0.62))
text("the belief that you're <i>worth</i> it", 'hint', wd(89, 0.64), en(89) + 0.4, dur=1.2, out=0.4)

# ================= close =================
# 90 "Which one will you try first? Tell us in the comments, and if you'd like a part two, let us know."
canvas_full(C('sweaterst36', 0, 9.43), st(90) - 0.1, en(90) + 0.3)
text('Which one <i>first</i>?', 'q1', wd(90, 0.1), en(90) + 0.25, dur=1.2)
# 91 "A simple like or comment would mean so much to us. Until next time, bye everyone."
canvas_full(C('golden31', 0, 7.4), st(91) - 0.1, total - 2.6, fin=0.8)
