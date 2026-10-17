# 6 More Ways to INSTANTLY Sound More Elegant (Part 2) - the edit, beat by beat.
# Built on the creator's own teaching layouts, measured in "6 Ways to INSTANTLY Sound More Elegant" (VISUAL-EDITING-DNA.md):
# white card per habit; the reason / payoff as one sentence on the caramel backdrop; the exact words in script beside a
# framed real conversation on cream (the replay peaks of Part 1); full-screen scenes for the place; one word alone on a
# card ("Like" in Part 1, "Just." and "Pardon?" here); the named woman seen AND heard (Audrey Hepburn, Charade, 1963).
# Footage: Charade (1963, US public domain) + Mixkit clips under the Stock Video Free License only. No AI.

def full(shots, t1, xf=0.4):
    """full-screen scene(s): shots = [(spec, t), ...], soft dissolves between them"""
    return demo(shots, t1, x0=0, w=W, xf=xf)

els.append('''<style>
.cream { position:absolute; inset:0; background:#f5ede4; }
.ph { position:absolute; z-index:46; left:1090px; width:740px; text-align:center; }
.ph .s { font-family:"Playfair"; font-size:30px; letter-spacing:4px; text-transform:uppercase; color:#9c7c64; }
.ph .b { font-family:"Playfair"; font-style:italic; font-size:44px; color:#a68b77; text-decoration:line-through; text-decoration-color:rgba(168,67,47,.75); text-decoration-thickness:2px; }
.ph .q { font-family:"Playfair"; font-style:italic; font-size:50px; color:#7d6252; }
.ph .a { font-family:"Pinyon"; font-size:84px; line-height:1.08; color:#3b2a20; }
.ph .a.sm { font-size:66px; }
.wordc { position:absolute; z-index:46; left:0; right:0; text-align:center; font-family:"Pinyon"; color:#2f2119; }
.wsub { position:absolute; z-index:46; left:0; right:0; text-align:center; font-family:"Playfair"; font-style:italic; font-size:48px; color:#7d6252; }
.cmt { position:absolute; z-index:46; left:360px; width:1200px; background:#fbf7f2; border-radius:22px; box-shadow:0 26px 60px rgba(60,30,12,.28); padding:44px 60px 50px; box-sizing:border-box; }
.cmt .h { font-family:"Playfair"; font-size:28px; letter-spacing:5px; text-transform:uppercase; color:#a07c62; }
.cmt .t { font-family:"Playfair"; font-style:italic; font-size:50px; line-height:1.3; color:#3b2a20; margin-top:18px; }
.flab { position:absolute; z-index:46; left:70px; bottom:60px; font-family:"Playfair"; font-size:32px; letter-spacing:2px; color:#fff; text-shadow:0 2px 14px rgba(0,0,0,.6); }
.hl { position:absolute; z-index:46; left:560px; font-family:"Playfair"; font-size:52px; color:#fff; text-shadow:0 2px 16px rgba(60,40,25,.3); white-space:nowrap; }
.hl b { font-family:"Pinyon"; font-weight:normal; font-size:76px; margin-right:26px; }
</style>''')

def rise(i, t, d=0.6):
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:14}},{{opacity:1,y:0,duration:{d},ease:"power2.out"}},{t:.3f});')

def cream(t0, t1):
    i = nid('cr'); els.append(f'<div id="{i}" class="cream" style="opacity:0"></div>'); fade_in(i, t0, 0.45); fade_out(i, t1, 0.5); return i

FX, FY, FWID = 130, 262, 920          # the framed clip: 16:9, rounded, soft shadow, left of centre
def framed(shots, t1, xf=0.4):
    """Part 1's peak layout: cream screen, one rounded framed clip on the left (clips dissolve inside it)"""
    t0 = shots[0][1]; cream(t0 - 0.05, t1)
    return _framed(shots, t1, xf)
def _framed(shots, t1, xf):
    inner = []; t0 = shots[0][1]; fh = round(FWID * 9 / 16)
    for k, (spec, t) in enumerate(shots):
        tend = (shots[k + 1][1] + xf) if k + 1 < len(shots) else t1 + 0.55
        v, h = vid(spec, t, tend, style=GRADE + 'position:absolute;left:0;top:0;')
        drift(v, t, tend, 1.035)
        if k: tw.append(f'tl.fromTo("#{v}",{{opacity:0}},{{opacity:1,duration:{xf},ease:"sine.inOut"}},{t:.3f});')
        inner.append(h)
    i = box(FX, FY, FX + FWID, FY + fh, ''.join(inner), z='border-radius:26px;box-shadow:0 26px 60px rgba(70,40,20,.26);')
    fade_in(i, t0, 0.5); fade_out(i, t1, 0.5); return i

def phrase(lines, t0, t1, y=None):
    """the words beside the frame. lines = [(cls, html)], cls: 's' small label, 'b' the habit to drop (struck through),
    'q' an example said the usual way, 'a' the words to say (script). All appear together at t0."""
    html = ''.join(f'<div class="{c}">{h}</div>' for c, h in lines)
    i = nid('ph'); yy = 330 if y is None else y
    els.append(f'<div id="{i}" class="ph" style="top:{yy}px;opacity:0">{html}</div>'); rise(i, t0); fade_out(i, t1, 0.4); return i

def word_card(word, t0, t1, size=230, y=330):
    cream(t0 - 0.05, t1)
    i = nid('wc'); els.append(f'<div id="{i}" class="wordc" style="top:{y}px;font-size:{size}px;opacity:0">{word}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,scale:0.94}},{{opacity:1,scale:1,duration:0.7,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.45)

def wsub(html, t0, t1, y):
    i = nid('ws'); els.append(f'<div id="{i}" class="wsub" style="top:{y}px;opacity:0">{html}</div>'); rise(i, t0); fade_out(i, t1, 0.4)

def comment(text_, t0, t1, y=330):
    i = nid('cm')
    els.append(f'<div id="{i}" class="cmt" style="top:{y}px;opacity:0"><div class="h">&#9825;&nbsp; from your comments</div><div class="t">&#8220;{text_}&#8221;</div></div>')
    rise(i, t0, 0.7); fade_out(i, t1, 0.45); return i

def quote(l1, t1_, t_end, l2=None, t2=None):
    """the reason / payoff as one sentence on the caramel backdrop (one word in script)"""
    text(l1, 'q1', t1_, t_end, dur=1.4)
    if l2: text(l2, 'q2', t2, t_end, dur=1.2)

def flabel(txt, t0, t1):
    i = nid('fl'); els.append(f'<div id="{i}" class="flab" style="opacity:0">{txt}</div>'); rise(i, t0); fade_out(i, t1, 0.4)

def guide(t0, t1):
    i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, t0, 0.6); fade_out(i, t1, 0.5)
    text('your personal stylist guide', 'gtx1', t0 + 0.3, t1, dur=1.2); text('in the description', 'gtx2', t0 + 0.9, t1, dur=1.4)

CH = lambda k, a, b: C('charade', a, b)        # Charade (1963), raw/charade.mp4 = film 2:30-7:30
M = lambda k, a, b: C('mk' + str(k), a, b)
nx = lambda i: st(i) - 0.1                       # a picture comes in just before its line
TO = lambda i: st(i) + 0.3                       # ...and stays until just after the next line starts

# ================= HOOK =================
full([(M(52195, 0.3, 6.6), 0.0)], TO(2))                                       # 1 sure of it ... sounding like a question
full([(M(52190, 8.5, 14.5), nx(2))], TO(3))                                    # 2 someone talks right over you
full([(CH(0, 154.0, 164.8), nx(3))], TO(4))                                    # 3 our first video (Audrey, Charade)
full([(CH(0, 74.2, 79.6), nx(4)), (CH(0, 81.1, 86.0), at(4, 'Six more')),       # 4 title over Audrey
      (M(12122, 0.5, 5.0), at(4, 'from the first word')), (M(52191, 0.5, 5.5), at(4, 'to the moment'))], TO(5))
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Part 2</div><div class="big">How to Speak Elegantly</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.1,ease:"power2.out"}},{st(4) + 0.2:.3f});'); fade_out(i, at(4, 'from the first word') - 0.2, 0.5)
comment('I tried speaking softly. They took over the conversation as if I wasn&#8217;t there.', nx(5), en(5) + 0.35, y=250)
comment('I hope the next video will be about how to start a conversation.', st(5) + 1.2, en(5) + 0.35, y=600)

# ================= 1. Let your sentences land =================
card('1. Let Your Sentences Land', 6)
full([(M(52188, 0.3, 5.6), en(6) + 0.2), (M(12123, 8.2, 13.0), at(7, 'even when'))], at(7, "I'm Claire") + 0.2)
framed([(M(12120, 0.3, 7.0), at(7, "I'm Claire") - 0.3)], en(7) + 0.35)
phrase([('s', 'it sounds like'), ('q', '&#8220;I&#8217;m Claire?<br>I work in design?&#8221;')], at(7, "I'm Claire"), en(7) + 0.3)
quote('It quietly asks for <i>permission</i>', st(8) + 0.2, en(8) + 0.3, 'and makes you sound unsure', at(8, 'and it makes'))
full([(CH(0, 95.2, 104.8), nx(9)), (CH(0, 113.8, 117.1), at(9, 'every sentence'))], en(9) + 0.35)
FS = en(9) + 0.3                                                                # Audrey heard: "Because I already know an awful lot of people..."
full([(CH(0, 179.35, 184.45), FS)], FS + 5.05, xf=0.2)
FILMAUDIO.append(('charade', 179.35, 184.45, FS))
flabel('Audrey Hepburn &nbsp;&#183;&nbsp; Charade, 1963', FS + 0.4, FS + 4.9)
quote('Light, playful, and completely <i>certain</i>', st(10) + 0.1, en(10) + 0.3)
full([(M(30005, 0.3, 7.0), nx(11))], at(11, 'let your voice') + 0.3)
framed([(M(52184, 0.5, 7.0), at(11, 'let your voice')), (M(41229, 0.3, 9.6), nx(12))], en(12) + 0.35)
phrase([('b', '&#8220;I&#8217;m Claire? I work in design?&#8221;'), ('a', 'I&#8217;m Claire.<br>I work in design.')], at(11, 'let your voice') + 0.3, nx(12) - 0.1, y=300)
phrase([('s', 'when you order'), ('a', 'I&#8217;d like the table<br>by the window.')], at(12, "I'd like"), en(12) + 0.3, y=300)
phrase([('q', 'a full stop, not a question mark')], at(12, 'A full stop'), en(12) + 0.3, y=640)
full([(M(42666, 0.3, 9.0), nx(13)), (M(52195, 6.7, 11.9), at(13, 'The pause'))], TO(14))
quote('A sentence that lands sounds like a <i>decision</i>', st(14) + 0.2, en(14) + 0.3,
      'A sentence that rises sounds like a request', at(14, 'A sentence that rises'))

# ================= 2. Speak clearly, not loudly =================
card('2. Speak Clearly, Not Loudly', 15)
comment('I tried speaking softly. They took over the conversation and told me to speak louder.', en(15) + 0.3, at(16, 'people talked') - 0.5)
full([(M(52177, 0.5, 13.3), at(16, 'people talked') - 0.3)], TO(17))
quote('Soft doesn&#8217;t mean <i>swallowed</i>', st(17) + 0.2, en(17) + 0.3, 'A graceful voice is never hard to follow', at(17, 'A graceful'))
framed([(M(52185, 0.3, 9.2), nx(18))], en(18) + 0.35)
phrase([('s', 'finish the ends of your words')], st(18) + 0.4, en(18) + 0.3, y=250)
phrase([('b', 'thank-yuh'), ('a', 'Thank you')], at(18, 'Thank you'), en(18) + 0.3, y=340)
phrase([('b', 'gonna'), ('a', 'going to')], at(18, "I'm going to"), en(18) + 0.3, y=560)
full([(M(12119, 0.3, 8.0), nx(19)), (M(52179, 8.6, 15.6), at(19, 'keep your chin'))], TO(20))
full([(M(41810, 0.3, 4.6), nx(20)), (M(41810, 4.8, 9.1), at(20, 'Lean in'))], TO(21))
full([(M(49916, 0.3, 9.0), nx(21)), (M(43250, 0.3, 6.0), at(21, 'read two')), (M(972, 0.2, 6.0), at(21, 'out loud')),
      (M(3183, 0.5, 14.2), at(21, 'It takes one'))], TO(22))
quote('Soft and clear will always be <i>heard</i>', st(22) + 0.1, en(22) + 0.3, 'Loud and rushed only gets noticed', at(22, 'Loud and rushed'))

# ================= 3. Opening a conversation =================
card('3. Opening a Conversation', 23)
comment('I hope the next video will be about how to start a conversation with people.', en(23) + 0.3, at(24, 'especially'))
full([(M(12117, 8.5, 16.0), at(24, 'especially') - 0.3)], TO(25))
framed([(M(51529, 0.5, 13.3), nx(25))], en(25) + 0.35)
phrase([('b', 'the weather&#8230;')], at(25, 'the weather'), en(25) + 0.3, y=300)
phrase([('b', '&#8220;So, what do you do?&#8221;')], at(25, 'So what'), en(25) + 0.3, y=420)
quote('A small, warm question about the <i>moment</i>', st(26) + 0.2, en(26) + 0.3, 'you&#8217;re both in', at(26, "you're both"))
framed([(M(12129, 0.3, 10.0), st(27) - 0.2), (M(51224, 3.0, 10.0), nx(28)), (M(4788, 0.3, 8.7), nx(29))], en(29) + 0.4)
phrase([('s', 'at a dinner'), ('a', 'How do you know<br>the hosts?')], st(27), nx(28) - 0.1, y=300)
phrase([('s', 'at a wedding'), ('a', 'What&#8217;s been your favorite<br>moment so far?')], st(28), nx(29) - 0.1, y=300)
phrase([('s', 'at a class or an event'), ('a', 'What brought you<br>here today?')], st(29), en(29) + 0.35, y=300)
full([(M(52196, 0.5, 7.5), nx(30))], TO(31))
canvas_full(M(41234, 0.5, 8.5), nx(31), at(31, 'and ask about') + 0.3)
full([(M(12122, 5.0, 9.0), at(31, 'and ask about'))], TO(32))
full([(M(51051, 0.3, 11.6), nx(32))], en(32) + 0.4)
guide(at(32, 'to discover'), en(32) + 0.35)

# ================= 4. Holding your place, gracefully =================
card('4. Holding Your Place, Gracefully', 33, style='font-size:100px')
full([(M(52190, 0.4, 7.6), en(33) + 0.2)], TO(35))
full([(M(12123, 0.5, 8.0), nx(35)), (M(10452, 0.3, 7.0), at(35, 'or we raise'))], TO(36))
framed([(M(52184, 7.2, 15.0), nx(36)), (M(52188, 5.8, 11.2), nx(37))], en(37) + 0.35)
phrase([('s', 'a calmer way')], st(36) + 0.6, nx(37) - 0.1, y=250)
phrase([('q', 'pause &#183; breathe &#183; look at them kindly')], at(36, 'Pause for'), nx(37) - 0.1, y=320)
phrase([('a', 'Let me just finish<br>this thought.')], at(36, 'Let me just'), nx(37) - 0.1, y=420)
phrase([('s', 'or, even softer'), ('a', 'One moment, I&#8217;d love<br>to hear that, right<br>after I finish.')], at(37, 'One moment'), en(37) + 0.3, y=260)
full([(M(52193, 0.3, 6.8), nx(38))], TO(39))
framed([(M(52179, 0.5, 8.0), nx(39))], en(39) + 0.35)
phrase([('s', 'then give the floor back'), ('a', 'Sorry, you were<br>saying?')], at(39, 'Sorry you'), en(39) + 0.3, y=300)
quote('You didn&#8217;t fight for the room,', st(40) + 0.1, en(40) + 0.3, 'you simply kept your <i>place</i>', at(40, 'You simply'))

# ================= 5. Talking about yourself =================
card('5. Talking About Yourself', 41)
full([(M(51531, 0.3, 5.0), en(41) + 0.2)], at(42, 'Just') + 0.2)
word_card('Just.', at(42, 'Just') - 0.1, en(42) + 0.35, y=250)
wsub('&#8220;Oh, I&#8217;m just a stay-at-home mom.&#8221;', at(42, 'Oh'), en(42) + 0.3, 600)
wsub('&#8220;It&#8217;s just a little job.&#8221;', at(42, "It's just"), en(42) + 0.3, 690)
quote('One little word makes your life sound <i>smaller</i>', st(43) + 0.2, en(43) + 0.3)
framed([(M(4549, 0.3, 11.0), nx(44)), (M(4833, 0.5, 14.8), nx(45)), (M(49916, 14.0, 24.0), nx(46))], en(46) + 0.4)
phrase([('s', 'one calm, true sentence')], st(44) + 0.4, en(46) + 0.3, y=230)
phrase([('a', 'I&#8217;m raising three children,<br>and I love it.')], at(44, "I'm raising"), nx(45) - 0.1, y=330)
phrase([('a', 'I work at a dental clinic.<br>I look after the patients.')], st(45) + 0.1, nx(46) - 0.1, y=330)
phrase([('a', 'I&#8217;m between jobs, and<br>I&#8217;m enjoying the pause.')], st(46) + 0.1, en(46) + 0.3, y=330)
full([(M(52196, 8.5, 18.9), nx(47))], TO(48))
quote('Sound like you respect your own <i>story</i>', st(48) + 0.2, en(48) + 0.3)

# ================= 6. Introducing people =================
card('6. Introducing People', 49)
full([(M(42716, 0.5, 16.7), en(49) + 0.2)], TO(51))
framed([(M(12128, 0.3, 8.0), nx(51))], en(51) + 0.35)
phrase([('b', '&#8220;This is Sophie.&#8221;'), ('q', '&#8230;and then silence')], at(51, 'This is Sophie'), en(51) + 0.3, y=330)
quote('The name, and a little <i>bridge</i>', st(52) + 0.2, en(52) + 0.3)
framed([(M(12127, 0.3, 8.0), st(53) - 0.2)], en(53) + 0.4)
phrase([('a', 'Clara, this is my<br>friend Sophie.')], st(53) + 0.1, en(53) + 0.35, y=230)
phrase([('a sm', 'Sophie just came back from<br>Lisbon, and Clara, you&#8217;ve<br>always wanted to go.')], at(53, 'Sophie just'), en(53) + 0.35, y=500)
full([(M(51531, 5.2, 10.1), nx(54))], TO(55))
full([(M(30005, 7.2, 10.6), nx(55)), (M(51224, 10.2, 16.6), at(55, 'and smile')), (M(43829, 0.5, 12.2), at(55, 'It takes ten'))], en(55) + 0.4)

# ================= And one more tiny thing =================
card('And One More Tiny Thing', 56, style='font-size:104px')
full([(M(52191, 6.0, 15.3), en(56) + 0.2)], at(57, 'And one of you') + 0.3)
comment('&#8216;Say that again&#8217; feels demanding. I just ask, &#8216;Pardon?&#8217;', at(57, 'And one of you'), en(57) + 0.35)
cream(st(58) - 0.1, en(58) + 0.35)
word_card('Pardon?', at(58, 'Pardon') - 0.2, en(58) + 0.35, y=250)
wsub('if you didn&#8217;t catch something', st(58) + 0.2, en(58) + 0.3, 200)
wsub('&#8220;Sorry, I didn&#8217;t quite catch that.&#8221;', at(58, 'Sorry I'), en(58) + 0.3, 640)
quote('Small words, said slowly,', st(59) + 0.1, en(59) + 0.35, 'carry the most <i>grace</i>', at(59, 'carry'))

# ================= Close =================
full([(CH(0, 86.3, 92.6), nx(60))], TO(61))
HL = ['Let your sentences land', 'Speak clearly, not loudly', 'Opening a conversation', 'Holding your place', 'Talking about yourself', 'Introducing people']
for k, h in enumerate(HL):
    i = nid('hl'); els.append(f'<div id="{i}" class="hl" style="top:{170 + k * 122}px;opacity:0"><b>{k + 1}.</b>{h}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,x:-20}},{{opacity:1,x:0,duration:0.55,ease:"power2.out"}},{st(61) + 0.1 + k * 0.45:.3f});'); fade_out(i, en(61) + 0.3, 0.45)
canvas_full(M(41236, 0.5, 16.3), nx(62), en(62) + 0.4)
guide(st(62) + 0.4, en(62) + 0.35)
full([(CH(0, 254.0, 258.9), nx(63))], at(63, 'A simple like') + 0.3)
canvas_full(M(12132, 0.3, 8.0), at(63, 'A simple like'), en(64) + 3.0)
