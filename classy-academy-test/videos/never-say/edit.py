# 8 Things Elegant Women Never Say - the edit, beat by beat (the "scene" edit, Oct 2026).
# Why it changed (videos/never-say/edit-evidence.md): the speech winners that are big AND loved are full-screen real
# scenes of people in conversation with a card per swap (Manners Matters 10.6x / 12.7x, 4.69% liked); their replay peaks
# sit on the acted-out phrase and the "instead of X, say Y" swap (1.5-3.4x their median); dips on abstract talk and intros.
# So: one cast per point, filmed in one shoot (shot / reverse shot, the same table), a new shot every 3-6 s inside the point,
# soft 0.35 s dissolves; the swap as a cream pill pair at the exact words (red cross phrase, green tick phrase);
# white number cards (our proven card); the recap is the screenshot list of all 8 swaps on our caramel.
# Footage: Mixkit clips under the Mixkit Stock Video FREE licence only (commercial use; the "restricted" ones were dropped),
# plus one credited creator clip (Jeanne Caldarera). No AI.
after = lambda i: en(i) + 0.1
M = lambda k, a, b: C('mk' + str(k), a, b)
def scene(shots, t1, xf=0.35):
    """one full-screen scene: shots = [(spec, t), ...], the same cast, soft dissolves inside"""
    return demo(shots, t1, x0=0, w=W, xf=xf)
RED, GRN = '#a8432f', '#4f6b3a'
def pill(html, x, y, t0, t1, size=50):
    i = nid('al'); els.append(f'<div id="{i}" class="alab" style="left:{x}px;top:{y}px;width:1700px;opacity:0"><span style="font-size:{size}px">{html}</span></div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:12}},{{opacity:1,y:0,duration:0.5,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.4); return i
NO = lambda s: f'<b style="color:{RED}">&#10005;</b>&nbsp; {s}'
YES = lambda s: f'<b style="color:{GRN}">&#10003;</b>&nbsp; {s}'
def swap(no, yes, t_no, t_yes, t_end, x=110, y=770):
    pill(NO(no), x, y, t_no, t_end); pill(YES(yes), x, y + 116, t_yes, t_end)

# ================= HOOK =================
# 1 Before you reply "whatever" or "me too" again, stop.
scene([(M(41216, 6.0, 10.5), 0.0)], en(1) + 0.2)
# 2 Which of these eight phrases do you say without noticing?
scene([(M(52195, 0.5, 5.2), en(1) + 0.1)], en(2) + 0.25)
pill('&#8220;whatever&#8221;', 150, 830, at(1, 'whatever'), en(2) + 0.2, 46)
pill('&#8220;me too&#8221;', 560, 830, at(1, 'me too'), en(2) + 0.2, 46)
pill('&#8220;I know&#8221;', 905, 830, st(2) + 0.4, en(2) + 0.2, 46)
pill('&#8220;calm down&#8221;', 1235, 830, at(2, 'say without'), en(2) + 0.2, 46)
# 3 We all say them. They feel harmless, even friendly. But each one quietly changes how people feel around you, and how you feel too.
scene([(M(41222, 0.3, 4.5), en(2) + 0.1), (M(12129, 0.4, 4.5), at(3, 'even friendly')), (M(41846, 3.0, 8.0), at(3, 'how people feel'))], en(3) + 0.25)
# 4 In today's video, we're sharing eight everyday phrases elegant women gently replace, and exactly what to say instead.
scene([(M(52190, 9.0, 15.0), en(3) + 0.1), (M(52191, 0.3, 5.0), at(4, 'gently replace'))], en(4) + 0.25)
# 5 Some of these may surprise you, but once you hear them, you'll never unhear them. Let's get started.
scene([(M(41236, 7.5, 15.5), en(4) + 0.1)], en(5) + 0.35)
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Episode 13</div><div class="big" style="font-size:96px">8 Things Elegant Women Never Say</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.1,ease:"power2.out"}},{at(5, "but once"):.3f});'); fade_out(i, en(5) + 0.3, 0.45)

def fill(segs, t0, t1):
    """spread these shots evenly over [t0, t1): a new picture every (t1-t0)/n s, each clip from its own start"""
    n = len(segs); d = (t1 - t0) / n
    return [(M(k, a_, min(b_, a_ + d + 0.6)), t0 + i_ * d) for i_, (k, a_, b_) in enumerate(segs)]

# ================= 1. Can I get =================  (the café pair: they order at the counter, the waiter brings it, they laugh)
card('1. &#8220;Can I get&#8230;&#8221;', 6)
scene(fill([(41229, 0.2, 5.0), (41220, 5.0, 10.0)], after(6), st(8) - 0.1)                          # 7 ordering at the counter
      + fill([(41222, 4.6, 9.0), (41223, 0.3, 4.5), (41214, 0.5, 5.0)], st(8) - 0.1, st(9) - 0.1)
      + fill([(41218, 0.2, 4.2), (41234, 0.5, 4.5)], st(9) - 0.1, at(9, 'please Instead of'))        # 9 the waiter serves them
      + fill([(41233, 0.3, 4.0), (41219, 0.5, 4.5)], at(9, 'please Instead of'), st(10) - 0.1)
      + [(M(41213, 0.2, 5.9), st(10) - 0.1), (M(41221, 0.3, 5.5), at(10, "it's my pleasure"))]      # 10 thank you / my pleasure
      + fill([(41216, 11.0, 15.0), (41232, 0.3, 4.5), (41235, 1.0, 5.0)], st(11) - 0.1, st(12) - 0.1)
      + fill([(41225, 0.3, 4.5), (41230, 1.0, 5.0), (41236, 1.0, 5.0)], st(12) - 0.1, en(12) + 0.3), en(12) + 0.3)
swap('&#8220;Can I get the salmon?&#8221;', '&#8220;I&#8217;d like the salmon, please.&#8221;', st(9), at(9, "try I'd like"), at(9, 'please Instead of') - 0.15)
swap('&#8220;Can I get a table by the window?&#8221;', '&#8220;May I have a table by the window, please?&#8221;', at(9, 'please Instead of') + 0.2, at(9, 'May I have'), en(9) + 0.4)
swap('&#8220;You&#8217;re welcome.&#8221;', '&#8220;It&#8217;s my pleasure.&#8221;', at(10, "you're welcome"), at(10, "it's my pleasure"), en(10) + 0.4)

# ================= 2. Me too =================  (the sofa pair, the same afternoon)
card('2. &#8220;Me too!&#8221;', 13)
scene([(M(12119, 0.3, 4.6), after(13)), (M(12120, 1.5, 6.8), at(14, 'And before'))]
      + fill([(12122, 0.3, 4.5), (12121, 0.5, 4.5)], st(15) - 0.1, st(16) - 0.1)
      + [(M(12132, 0.3, 4.6), st(16) - 0.1), (M(12131, 3.5, 9.0), at(16, 'Instead of'))]
      + fill([(12121, 6.0, 10.5), (12125, 0.3, 4.8)], st(17) - 0.1, st(18) - 0.1)
      + [(M(12124, 3.5, 9.0), st(18) - 0.1), (M(12123, 0.5, 7.0), st(19) - 0.1)], en(19) + 0.3)
pill(NO('&#8220;Me too! I barely slept.&#8221;'), 110, 790, at(14, 'Me too'), at(16, 'Instead of') - 0.2)
swap('&#8220;Me too!&#8221;', '&#8220;That sounds exhausting. What&#8217;s been going on?&#8221;', at(16, 'Instead of'), at(16, 'That sounds exhausting'), en(17) + 0.3)

# ================= 3. I know =================  (the café-phone pair: she shows her friend something on her phone)
card('3. &#8220;I know.&#8221;', 20)
scene(fill([(43257, 0.3, 4.5), (43253, 0.5, 4.5), (43257, 6.5, 11.0)], after(20), st(22) - 0.1)
      + [(M(43256, 0.3, 4.6), st(22) - 0.1), (M(43251, 0.3, 4.5), at(22, 'and it closes'))]
      + fill([(43266, 2.0, 6.5), (43254, 0.5, 5.0)], st(23) - 0.1, st(24) - 0.1)
      + fill([(43265, 0.3, 4.5), (43249, 0.3, 5.0)], st(24) - 0.1, st(25) - 0.1)
      + fill([(43247, 0.3, 4.5), (43261, 0.5, 5.0)], st(25) - 0.1, en(25) + 0.3), en(25) + 0.3)
pill(NO('&#8220;I know.&#8221;'), 110, 790, at(21, 'I know'), st(22) + 1.0)
swap('&#8220;I know.&#8221;', '&#8220;That&#8217;s interesting. What did you think of it?&#8221;', st(23), at(23, "That's interesting"), en(23) + 0.3)

# ================= 4. Oh yes, of course =================  (a dinner with friends)
card('4. &#8220;Oh yes, of course&#8221;', 26)
scene(fill([(42144, 0.5, 5.0), (42139, 0.3, 4.6)], after(26), at(27, 'and we nod'))
      + [(M(42145, 0.3, 5.5), at(27, 'and we nod'))]
      + fill([(42155, 0.3, 5.4), (42154, 0.3, 4.5), (42145, 5.6, 10.9)], st(28) - 0.1, st(29) - 0.1)
      + [(M(42157, 0.3, 5.0), st(29) - 0.1), (M(42159, 3.8, 7.4), at(29, 'and that ease')), (M(42143, 0.3, 7.6), at(29, 'Instead of pretending'))]
      + fill([(42158, 0.5, 5.0), (42138, 8.8, 13.0), (42152, 0.3, 5.0)], st(30) - 0.1, en(31) + 0.3), en(31) + 0.3)
pill(NO('&#8220;Oh yes, of course.&#8221;'), 110, 790, at(27, 'and we nod'), at(29, 'Instead of pretending') - 0.2)
swap('&#8220;Oh yes, of course.&#8221;', '&#8220;I haven&#8217;t seen it yet. Tell me about it.&#8221;', at(29, 'Instead of pretending'), at(29, "I haven't seen"), en(30) + 0.3)

# 32 guide plug (<= 10 s, at the end of point 4)
scene(fill([(42733, 0.5, 5.5), (42733, 9.5, 15.0)], after(31), en(32) + 0.4), en(32) + 0.4)
i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, at(32, 'our personal stylist'), 0.8); fade_out(i, en(32) + 0.4, 0.5)
text('Check the description for', 'gtx1', at(32, 'our personal stylist') + 0.4, en(32) + 0.35, dur=1.1)
text('Personal stylist guide', 'gtx2', at(32, 'our personal stylist') + 0.8, en(32) + 0.35, dur=1.6)
# 33 which phrase do you catch yourself saying most?
scene(fill([(52196, 0.3, 5.0), (52185, 0.5, 5.0)], en(32) + 0.25, en(33) + 0.3), en(33) + 0.3)
for k, (w_, x_) in enumerate([('&#8220;Can I get&#8221;', 110), ('&#8220;me too&#8221;', 520), ('&#8220;I know&#8221;', 860), ('&#8220;of course&#8221;', 1190)]):
    pill(w_, x_, 830, at(33, 'which of these') + 0.35 * k, en(33) + 0.2, 46)
pill('which one is yours? &nbsp;tell us below', 110, 720, at(33, 'Tell us'), en(33) + 0.2, 40)

# ================= 5. Whatever =================  (the friends in yellow: where shall we eat?)
card('5. &#8220;Whatever&#8221;', 34)
scene(fill([(41811, 0.3, 4.6), (41816, 0.5, 4.5), (41812, 0.3, 4.5)], after(34), st(36) - 0.1)
      + [(M(41814, 3.0, 9.0), st(36) - 0.1), (M(41810, 4.5, 9.0), at(36, 'because people'))]
      + fill([(41850, 0.5, 5.0), (41853, 0.5, 5.0)], st(37) - 0.1, st(38) - 0.1)
      + fill([(41854, 0.3, 4.5), (41849, 4.0, 9.0)], st(38) - 0.1, st(39) - 0.1)
      + [(M(41846, 8.0, 15.0), st(39) - 0.1)] + fill([(41815, 6.0, 10.5), (41816, 9.0, 14.5)], st(40) - 0.1, en(40) + 0.3), en(40) + 0.3)
pill(NO('&#8220;I don&#8217;t mind.&#8221;'), 110, 790, at(35, "I don't mind"), en(35) + 0.3)
swap('&#8220;Whatever you want.&#8221;', '&#8220;I&#8217;d love the little bistro on the corner, if that suits you.&#8221;', at(37, 'Elegant women'), at(37, "I'd love"), en(37) + 0.3)
swap('&#8220;I don&#8217;t care.&#8221;', '&#8220;That&#8217;s not really my preference, but thank you.&#8221;', at(38, "I don't care"), at(38, "That's not really"), en(38) + 0.3)

# ================= 6. Calm down =================  (an upset moment, then a calm voice)
card('6. &#8220;Calm down.&#8221;', 41)
scene([(M(39790, 0.3, 6.5), after(41)), (M(4513, 0.3, 6.0), at(42, 'But have you')),
       (M(4513, 6.0, 11.2), st(43) - 0.1),
       (M(52195, 5.5, 11.8), st(44) - 0.1)]
      + fill([(52191, 5.0, 10.0), (52182, 0.5, 5.0), (52184, 0.5, 5.0)], st(45) - 0.1, st(46) - 0.1)
      + [(M(8739, 0.5, 7.5), st(46) - 0.1), (M(8739, 8.0, 14.5), at(46, 'before they speak'))]
      + fill([(52190, 0.3, 4.6), (52180, 0.5, 5.0)], st(47) - 0.1, en(47) + 0.3), en(47) + 0.3)
pill(NO('&#8220;Calm down.&#8221;'), 110, 790, at(42, 'calm down'), en(43) + 0.2)
swap('&#8220;Calm down.&#8221;', '&#8220;Let&#8217;s take a moment.&#8221;', st(44), at(44, "Let's take a moment"), en(44) + 0.3)
swap('&#8220;You made me feel ignored.&#8221;', '&#8220;When that happened, I felt a little ignored.&#8221;', at(45, 'You made me feel'), at(45, 'When that happened'), en(45) + 0.3)

# ================= 7. About another woman =================  (the restaurant pair leaning in; then a friend, a mother and daughter)
card('7. About another woman', 48)
scene(fill([(51237, 0.3, 4.6), (51239, 1.0, 5.5)], after(48), st(50) - 0.1) + [
       (M(51238, 0.3, 6.0), st(50) - 0.1), (M(51240, 0.3, 6.0), at(50, 'what we')),
       (M(51242, 0.3, 6.5), st(51) - 0.1), (M(51234, 0.5, 7.0), at(51, 'and then turn'))], en(51) + 0.3)
scene([(M(4735, 0.3, 8.6), en(51) + 0.15)], en(52) + 0.3)
scene(fill([(52238, 0.3, 5.0), (52238, 9.5, 13.8)], en(52) + 0.15, st(54) - 0.1) + fill([(4581, 0.5, 5.0), (12129, 5.0, 10.0)], st(54) - 0.1, en(54) + 0.3), en(54) + 0.3)
swap('&#8220;Did you see what she wore?&#8221;', '&#8220;Oh, I wouldn&#8217;t know about that. How was your trip?&#8221;', st(51), at(51, "I wouldn't know"), en(51) + 0.2)
swap('&#8220;I never liked him anyway.&#8221;', '&#8220;I&#8217;m here. How are you holding up?&#8221;', at(52, 'I never liked'), at(52, "I'm here"), en(52) + 0.2)

# ================= 8. About yourself =================  (a woman at her mirror; a compliment; a 70s woman trying on a coat)
card('8. About yourself', 55)
scene(fill([(4515, 0.5, 5.0), (4515, 9.0, 15.0)], after(55), at(57, 'But people listen')) + [(M(4573, 0.5, 9.0), at(57, 'But people listen')),
       (M(52193, 0.2, 6.6), st(58) - 0.1), (M(52194, 0.3, 6.0), at(58, 'Thank you')),
       (M(52188, 0.3, 4.8), st(59) - 0.1), (M(52197, 1.0, 6.0), at(59, "Instead of I'm too old"))], en(59) + 0.3)
for k, s in enumerate(['&#8220;Oh, I look awful today.&#8221;', '&#8220;I&#8217;m hopeless with names.&#8221;', '&#8220;I&#8217;m too old for that.&#8221;']):
    pill(NO(s), 110, 540 + 116 * k, at(56, ['look awful', 'hopeless with', 'too old'][k]) - 0.2, en(56) + 0.4)
swap('&#8220;Oh, I look awful today.&#8221;', '&#8220;Thank you.&#8221;', st(58), at(58, 'Thank you'), en(58) + 0.2)
swap('&#8220;I&#8217;m hopeless at this.&#8221;', '&#8220;I&#8217;m still learning.&#8221;', at(59, 'And instead of'), at(59, "I'm still learning"), at(59, "Instead of I'm too old") - 0.15)
swap('&#8220;I&#8217;m too old for that.&#8221;', '&#8220;I&#8217;d love to try that.&#8221;', at(59, "Instead of I'm too old") + 0.15, at(59, "I'd love to try"), en(59) + 0.3)
canvas_full(C('mirror50_29', 1.0, 6.0), en(59) + 0.15, at(60, "It's about"), fin=0.5)
canvas_full(C('mirror50_15', 2.0, 9.0), at(60, "It's about"), en(60) + 0.3, fin=0.4)   # Jeanne, in her 70s, at her mirror, smiling
scene([(M(4781, 1.0, 8.5), en(60) + 0.2)], en(61) + 0.35)

# ================= recap 62-70: the screenshot list of all 8 swaps, on our caramel =================
kicker('the 8 swaps', st(62) - 0.1, en(70) + 0.6, x=100, y=40)
demo([(M(41214, 6.0, 10.0), st(62) - 0.1), (M(41229, 5.5, 9.6), st(63) - 0.1), (M(12119, 4.8, 8.0), st(64) - 0.1),
      (M(43249, 6.0, 11.0), st(65) - 0.1), (M(42157, 5.2, 9.1), st(66) - 0.1), (M(41850, 10.0, 14.0), st(67) - 0.1),
      (M(52180, 6.0, 10.0), st(68) - 0.1), (M(51239, 6.0, 10.0), st(69) - 0.1), (M(52194, 6.5, 10.5), st(70) - 0.1)],
     en(70) + 0.6, x0=1230)
R_ = [('Can I get', 'May I have&#8230;, please'), ('Me too!', 'one more question'), ('I know', 'What did you think of it?'),
      ('Oh yes, of course', 'Tell me about it'), ('Whatever', 'your gentle preference'), ('Calm down', 'Let&#8217;s take a moment'),
      ('unkind words about others', 'kind silence'), ('unkind words about yourself', 'Thank you')]
for k, (a_, b_) in enumerate(R_):
    pill(f'<b style="color:{RED}">&#10005;</b>&nbsp; <span style="all:unset;opacity:.55;text-decoration:line-through">{a_}</span>&nbsp; &#8594;&nbsp; '
         f'<b style="color:{GRN}">&#10003;</b>&nbsp; {b_}', 90, 175 + 108 * k, st(63 + k) - 0.15, en(70) + 0.6, 48)

# ================= close =================
scene([(M(41219, 6.0, 12.4), en(70) + 0.5), (M(12135, 0.3, 7.8), at(71, 'You already own'))], en(71) + 0.3)
scene([(M(43248, 6.0, 10.2), en(71) + 0.15), (M(43261, 6.0, 10.5), at(72, 'and how calm'))], en(72) + 0.3)
scene(fill([(4581, 9.5, 14.0), (52238, 0.3, 0.3)][:1] + [(4781, 8.6, 14.5)], en(72) + 0.15, en(73) + 0.3), en(73) + 0.3)
pill('a gracious phrase from your mother or grandmother?', 110, 830, at(73, "What's one"), en(73) + 0.2, 40)
scene([(M(12125, 5.2, 10.0), en(73) + 0.15), (M(41225, 4.6, 8.5), st(74) + 3.0)], total - 2.4)
