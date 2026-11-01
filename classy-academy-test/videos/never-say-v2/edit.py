# 8 Things Elegant Ladies Never Say: What to Say Instead — Full Production Edit (edit.py)
# Built strictly on the measured Classy Academy Visual & Editing DNA:
#   - Primary Speech & Presence Reference: "6 Ways to INSTANTLY Sound More Elegant" (RUDXBR8nyHw, 336K views, 4.93% liked)
#   - Primary Title & Structural Reference: "8 Things Elegant Ladies Never Wear: What to Wear Instead" (My7qteRU9k0, 1.24M views)
#   - Companion References: "10 Microhabits That Instantly Elevate Your Presence" (MVrYflIex4c),
#     "7 Habits That Make You Instantly Classy" (-1BANqxakGA), "7 Things Elegant Ladies Never Share" (mFLqPSyb4eQ)
#
# Authentic Classy Academy Layouts Only (Zero Invented Templates):
#   1. card()             -> Full-screen crisp white (#FFFFFF) chapter card, centered black Pinyon Script wiping left-to-right (1.2s)
#   2. quote() / quote_side() -> Warm drifting caramel backdrop (#C38D62), Playfair Display + Pinyon Script keyword emphasis
#   3. framed() + phrase() -> Soft cream canvas (#F5EDE4), rounded 16:9 clip on left (x:130..1050) with internal clip dissolves
#                            every 4-6s, and struck-through mistake phrase + Pinyon Script replacement phrase on right (x:1090..1830)
#   4. word_card()        -> Single automatic "rough word" isolated in large Pinyon Script on soft cream ("What?")
#   5. full() / canvas_full() / row(3) / pair(2) / single() -> 4-pillar footage mix (iconic cinema, real public-figure interviews,
#                            refined lifestyle/creator reels, and curated everyday conversational stock)
#   6. FILMAUDIO          -> Real-voice demonstration insert in Point 8 (Audrey Hepburn / Princess Diana speaking softly, 4.4s)

def full(shots, t1, xf=0.4):
    """Full-screen 16:9 scene sequence: shots = [(spec, t), ...], soft 0.4s dissolves between connected shots."""
    return demo(shots, t1, x0=0, w=W, xf=xf)

els.append('''<style>
.cream { position:absolute; inset:0; background:#f5ede4; }
.ph { position:absolute; z-index:46; left:1090px; width:740px; text-align:center; }
.ph .b { font-family:"Playfair"; font-style:italic; font-size:42px; line-height:1.25; color:#a68b77; text-decoration:line-through; text-decoration-color:rgba(168,67,47,.75); text-decoration-thickness:2px; margin-bottom:22px; }
.ph .a { font-family:"Pinyon"; font-size:78px; line-height:1.10; color:#3b2a20; }
.ph .a.md { font-size:68px; line-height:1.12; }
.ph .a.sm { font-size:60px; line-height:1.14; }
.wordc { position:absolute; z-index:46; left:0; right:0; text-align:center; font-family:"Pinyon"; color:#2f2119; }
</style>''')

def rise(i, t, d=0.6):
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:14}},{{opacity:1,y:0,duration:{d},ease:"power2.out"}},{t:.3f});')

def cream(t0, t1):
    i = nid('cr'); els.append(f'<div id="{i}" class="cream" style="opacity:0"></div>'); fade_in(i, t0, 0.45); fade_out(i, t1, 0.5); return i

FX, FY, FWID = 130, 262, 920          # Verified RUDXBR8nyHw framed clip: 16:9, rounded corners, soft shadow, left of centre
def framed(shots, t1, xf=0.4):
    """RUDXBR8nyHw's 2.3x-2.4x replay-peak layout: soft cream screen, one rounded 16:9 frame on the left with internal clip dissolves."""
    t0 = shots[0][1]; cream(t0 - 0.05, t1)
    return _framed(shots, t1, xf)

def _framed(shots, t1, xf):
    inner = []; t0 = shots[0][1]; fh = round(FWID * 9 / 16)
    for k, (spec, t) in enumerate(shots):
        tend = (shots[k + 1][1] + xf) if k + 1 < len(shots) else t1 + 0.55
        v, h = vid(spec, t, tend, style=GRADE + 'position:absolute;left:0;top:0;')
        drift(v, t, tend, 1.04)
        if k: tw.append(f'tl.fromTo("#{v}",{{opacity:0}},{{opacity:1,duration:{xf},ease:"sine.inOut"}},{t:.3f});')
        inner.append(h)
    i = box(FX, FY, FX + FWID, FY + fh, ''.join(inner), z='border-radius:26px;box-shadow:0 26px 60px rgba(70,40,20,.26);')
    fade_in(i, t0, 0.5); fade_out(i, t1, 0.5); return i

def phrase(lines, t0, t1, y=None):
    """Exact words beside the rounded frame on cream.
    lines = [(cls, html)], where cls is:
      'b'     -> the phrase to avoid (Playfair Italic, struck through)
      'a'     -> the graceful phrase to say instead (Pinyon Script 78px)
      'a md'  -> medium phrase (Pinyon Script 68px)
      'a sm'  -> longer sentence swap (Pinyon Script 60px)
    Zero uppercase category eyebrows (.s) — matching RUDXBR8nyHw's clean look."""
    html = ''.join(f'<div class="{c}">{h}</div>' for c, h in lines)
    i = nid('ph'); yy = 320 if y is None else y
    els.append(f'<div id="{i}" class="ph" style="top:{yy}px;opacity:0">{html}</div>'); rise(i, t0); fade_out(i, t1, 0.4); return i

def word_card(word, t0, t1, size=220, y=340):
    """Single automatic rough/filler word isolated on cream (matching the 'Like' card at 2:28 in RUDXBR8nyHw)."""
    cream(t0 - 0.05, t1)
    i = nid('wc'); els.append(f'<div id="{i}" class="wordc" style="top:{y}px;font-size:{size}px;opacity:0">{word}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,scale:0.94}},{{opacity:1,scale:1,duration:0.7,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.45)

def quote(l1, t1_, t_end, l2=None, t2=None):
    """The psychological reason or principle as one sentence on the drifting caramel backdrop (#C38D62)."""
    text(l1, 'q1', t1_, t_end, dur=1.4)
    if l2: text(l2, 'q2', t2 if t2 is not None else (t1_ + 0.45), t_end, dur=1.2)

def guide_haze(t0, t1):
    """Authentic mid-video Personal Stylist Guide haze overlay (.haze + .gtx1 + .gtx2)."""
    i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, t0, 0.7); fade_out(i, t1, 0.5)
    text('Check the description for', 'gtx1', t0 + 0.35, t1, dur=1.1)
    text('Personal Stylist Guide', 'gtx2', t0 + 0.80, t1, dur=1.5)

nx = lambda i: st(i) - 0.10
TO = lambda i: st(i) + 0.25

# ==============================================================================
# SECTION 1: OPENING HOOK & INTRODUCTION (Lines 1-7)
# Connected visual sequence of iconic women speaking softly while others lean in
# ==============================================================================
# Line 1: Have you ever met a woman who didn't try to stand out, didn't speak the loudest in the room, and didn't try to impress anyone, and yet the moment she spoke, everyone naturally leaned in to listen?
# Line 2: Her presence felt calm, warm, and effortlessly magnetic.
full([
    (C('audrey_tiffany_table', 0.0, 6.2), 0.0),                                   # Audrey Hepburn at table, poised and unhurried
    (C('jolie_thr_listen', 0.5, 6.8), at(1, 'and yet the moment')),               # Angelina Jolie speaking softly at roundtable while others lean in
    (C('grace_kelly_blue', 0.4, 5.8), nx(2)),                                     # Grace Kelly turning with a warm, magnetic smile (To Catch a Thief)
], TO(3))

# Line 3: Most people assume that kind of poise comes from having a perfect vocabulary, an expensive education, or knowing exactly how to sound polished at all times.
# Line 4: But in reality, sounding truly elegant has very little to do with using big, complicated words or sounding rehearsed.
full([
    (C('emma_un_podium', 0.4, 5.2), nx(3)),                                       # Emma Watson in crisp white suit at podium
    (C('camelwalk14', 0.0, 4.6), at(3, 'an expensive education')),                # Refined woman in camel coat walking past classic facade
    (C('audrey_sabrina_bw', 0.5, 5.0), nx(4)),                                    # Audrey Hepburn in Sabrina (white headscarf, warm close-up)
    (C('amal_interview_smile', 0.4, 5.2), at(4, 'using big')),                    # Amal Clooney smiling with natural warmth in interview
], en(4) + 0.25)

# Line 5: More often than not, what separates a woman whose words carry quiet weight from someone who accidentally talks herself down comes down to what she knows never to say.
quote_side(
    C('over60chic37', 13.89, 18.52), st(5) - 0.05, en(5) + 0.30,
    'What she knows', '<i>never to say</i>', at(5, 'what she knows')
)

# Line 6: Because the truth is, there are small, everyday phrases that so many of us use out of habit—often just trying to be polite, relatable, or humble—that quietly chip away at our confidence and presence without us even realizing it.
row(
    [C('mk41236', 1.0, 7.5), C('over60chic14', 8.6, 13.7), C('mk12122', 0.3, 6.5)],
    [at(6, 'polite'), at(6, 'relatable'), at(6, 'humble')],
    en(6) + 0.25,
    labels=['polite', 'relatable', 'humble']
)

# Line 7: So today, we are going through eight things elegant ladies never say... So, let's get started, everyone.
full([
    (C('charade', 81.1, 86.0), nx(7)),                                            # Audrey Hepburn in Charade under the title card
    (C('diana_cream_smile', 0.3, 5.8), at(7, 'Some of these are tiny')),          # Princess Diana smiling warmly in cream jacket
], at(7, "once you hear them") + 0.20)
i_ti = nid('ti')
els.append(f'<div id="{i_ti}" class="title" style="opacity:0"><div class="ep">Classy Academy</div><div class="big" style="font-size:96px">8 Things Elegant Ladies Never Say</div></div>')
tw.append(f'tl.fromTo("#{i_ti}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.1,ease:"power2.out"}},{st(7) + 0.25:.3f});')
fade_out(i_ti, at(7, 'Some of these are tiny') - 0.15, 0.45)
single(C('camelwalk4', 0.0, 5.5), at(7, "once you hear them"), en(7) + 0.30)


# ==============================================================================
# SECTION 2: NUMBER 1 — DOWNGRADING YOURSELF WHEN COMPLIMENTED (Lines 8-18)
# ==============================================================================
# Line 8: Number one: downgrading yourself the moment someone gives you a compliment.
card('1. Downgrading Yourself', 8, style='font-size:104px')

# Line 9: We have all done this at some point.
full([(C('px8922355', 0.4, 4.8), en(8) + 0.20)], TO(10))

# Line 10: Someone looks at you and says, "I love your dress, you look amazing today," and before you even think about it, out comes, "Oh, this old thing? I got it on sale for ten dollars," or "Really? I feel like I look such a mess today, I barely slept."
framed([
    (C('mk12128', 0.3, 6.2), nx(10)),
    (C('compliment_wave_off', 0.5, 6.8), at(10, 'Oh, this old thing')),
], en(10) + 0.35)
phrase([
    ('b', '&#8220;Oh, this old thing?<br>I got it on sale for ten dollars.&#8221;')
], at(10, 'Oh, this old thing'), en(10) + 0.30, y=300)
phrase([
    ('b', '&#8220;I feel like I look such a mess today,<br>I barely slept.&#8221;')
], at(10, 'I feel like I look'), en(10) + 0.30, y=520)

# Line 11: Most of us do this because we don't want to seem vain or boastful.
# Line 12: We think brushing off a compliment makes us sound humble and approachable.
# (Continuous two-shot dinner sequence across connected lines 11-12)
full([
    (C('mk12129', 0.4, 5.6), nx(11)),
    (C('mk12127', 0.4, 5.4), nx(12)),
], en(12) + 0.25)

# Line 13: But think about what actually happens in that moment.
single(C('flowers_gift_smile', 0.5, 4.8), nx(13), en(13) + 0.25)

# Line 14: When someone gives you a genuine compliment, they are offering you a small gift of warmth and appreciation.
quote('A compliment is a small gift of', st(14) + 0.15, en(14) + 0.30, '<i>warmth and appreciation</i>', at(14, 'warmth and appreciation'))

# Line 15: When you immediately argue with them or point out a flaw they hadn't even noticed, two things happen at once. First, you unintentionally tell the other person that their judgment is wrong... And second, you train the room to look for your flaws...
pair(
    [C('awkward_giver_pause', 0.4, 8.8), C('sleeve_flaw_check', 0.4, 6.5)],
    [at(15, 'First, you'), at(15, 'And second, you')],
    en(15) + 0.30,
    labels=['questions their taste', 'points out flaws']
)

# Line 16: An elegant woman never uses self-deprecation to shrink away from kindness.
full([(C('grace_kelly_rear_window', 0.4, 6.2), nx(16))], en(16) + 0.25)

# Line 17: She receives a compliment the same way she would receive a bouquet of flowers—warmly, simply, and without making a fuss.
quote('Receive a compliment like a', st(17) + 0.15, en(17) + 0.30, '<i>bouquet of flowers</i>', at(17, 'bouquet of flowers'))

# Line 18: Next time someone compliments your outfit, your work, or the way you handled something, pause the urge to explain it away...
framed([
    (C('dinner_warm_smile', 0.4, 7.5), nx(18)),
    (C('amal_thank_you_nod', 0.3, 7.2), at(18, 'Thank you, that is so kind')),
    (C('over60chic19', 0.0, 8.2), at(18, 'If someone compliments something')),
    (C('sofa_wine_compliment', 0.5, 8.0), at(18, 'It takes two seconds')),
], en(18) + 0.35)
phrase([
    ('b', '&#8220;Oh, this old thing? It was on sale.&#8221;'),
    ('a', '&#8220;Thank you, that is so<br>kind of you to say.&#8221;')
], at(18, 'Thank you, that is so kind'), at(18, 'Thank you so much, you') - 0.15, y=280)
phrase([
    ('b', '&#8220;Oh, this old thing? It was on sale.&#8221;'),
    ('a', '&#8220;Thank you so much,<br>you just made my day.&#8221;')
], at(18, 'Thank you so much, you'), at(18, 'If someone compliments something') - 0.10, y=280)
phrase([
    ('b', '&#8220;I look such a mess today.&#8221;'),
    ('a md', '&#8220;Thank you, I really enjoyed<br>putting this together today.&#8221;')
], at(18, 'Thank you, I really enjoyed'), en(18) + 0.30, y=280)


# ==============================================================================
# SECTION 3: NUMBER 2 — PRE-APOLOGIZING BEFORE SHARING A THOUGHT (Lines 19-28)
# ==============================================================================
# Line 19: Number two: pre-apologizing before you even share a thought.
card('2. Pre-Apologizing Before You Speak', 19, style='font-size:96px')

# Line 20: Have you ever noticed how often women soften their own voice before they have even said anything wrong?
full([(C('meeting_hesitant_hand', 0.4, 6.2), en(19) + 0.20)], TO(21))

# Line 21: It sounds like starting a question at work with, "Sorry to bother you, this might be a silly question, but..." Or offering an idea in a group and saying, "I'm probably overthinking this, and I'm no expert, so correct me if I'm wrong, but..."
framed([
    (C('office_door_apology', 0.4, 6.5), nx(21)),
    (C('roundtable_uncertain', 0.5, 6.8), at(21, 'Or offering an idea')),
], en(21) + 0.35)
phrase([
    ('b', '&#8220;Sorry to bother you, this might<br>be a silly question, but&#8230;&#8221;')
], at(21, 'Sorry to bother you'), en(21) + 0.30, y=290)
phrase([
    ('b', '&#8220;I&#8217;m probably overthinking this,<br>correct me if I&#8217;m wrong&#8230;&#8221;')
], at(21, "I'm probably overthinking"), en(21) + 0.30, y=510)

# Line 22: Even in everyday life, we say "I'm sorry" when someone else bumps into us, when we ask a waiter for a glass of water, or when we simply need to reach past someone at a table.
row(
    [C('camelwalk15', 0.0, 4.0), C('mk41229', 0.3, 6.0), C('table_reach_water', 0.4, 6.0)],
    [at(22, 'bumps into us'), at(22, 'ask a waiter'), at(22, 'reach past someone')],
    en(22) + 0.25,
    labels=['bumping into someone', 'asking a waiter', 'at the table']
)

# Line 23: Of course, a sincere apology when you have genuinely hurt someone or made a mistake is a beautiful sign of maturity and character.
# Line 24: Elegant women apologize with complete grace when an apology is truly needed.
full([
    (C('mk12132', 0.3, 6.8), nx(23)),
    (C('diana_sincere_nod', 0.4, 5.5), nx(24)),
], TO(25))

# Line 25: The problem is that when you apologize simply for taking up space, asking a fair question, or having an opinion, you quietly signal to everyone listening that your presence is an inconvenience.
full([
    (C('emma_un_speaking', 0.5, 5.8), nx(25)),                                    # Emma Watson at the UN podium (RUDXBR8nyHw 1:09 callback)
    (C('amal_stage_composed', 0.4, 5.8), at(25, 'you quietly signal')),           # Amal Clooney speaking with calm authority
], en(25) + 0.25)

# Line 26: People take their cue on how to value your words from the way you introduce them.
quote('People value your words by', st(26) + 0.15, en(26) + 0.30, 'how you <i>introduce</i> them', at(26, 'introduce them'))

# Line 27: If you label your own thought as silly before anyone else has heard it, people will unconsciously listen to it as if it doesn't matter. One of the simplest, most powerful shifts you can make is trading unnecessary apologies for gratitude or direct warmth.
quote_side(
    C('navyblazer15', 3.09, 10.1), st(27) - 0.05, en(27) + 0.30,
    'Trade unnecessary apologies', 'for <i>gratitude</i>', at(27, 'trading unnecessary')
)

# Line 28: Instead of saying, "Sorry to bother you," try saying, "Do you have a quick moment?"...
framed([
    (C('colleague_warm_moment', 0.4, 7.2), nx(28)),
    (C('tracee_podcast_calm', 0.5, 7.5), at(28, 'This might sound silly')),
    (C('cafe_arrival_smile', 0.4, 7.5), at(28, 'when you are running')),
    (C('mk51051', 0.5, 8.5), at(28, 'Thank you for listening')),
], en(28) + 0.35)
phrase([
    ('b', '&#8220;Sorry to bother you&#8230;&#8221;'),
    ('a', '&#8220;Do you have a<br>quick moment?&#8221;')
], at(28, 'Sorry to bother you'), at(28, 'This might sound silly') - 0.10, y=300)
phrase([
    ('b', '&#8220;This might sound silly, but&#8230;&#8221;'),
    ('a md', '&#8220;Here is a thought<br>I&#8217;d love to share.&#8221;')
], at(28, 'This might sound silly'), at(28, 'when you are running') - 0.10, y=300)
phrase([
    ('b', '&#8220;Sorry I&#8217;m late.&#8221;'),
    ('a md', '&#8220;Thank you so much<br>for waiting for me.&#8221;')
], at(28, "Sorry I'm late"), at(28, 'Thank you for listening') - 0.10, y=300)
phrase([
    ('b', '&#8220;Sorry I&#8217;m rambling so much.&#8221;'),
    ('a md', '&#8220;Thank you for listening&#8212;<br>I value your perspective.&#8221;')
], at(28, 'Thank you for listening'), en(28) + 0.30, y=300)


# ==============================================================================
# SECTION 4: NUMBER 3 — OVER-EXPLAINING EVERY TIME YOU SAY "NO" (Lines 29-37)
# ==============================================================================
# Line 29: Number three: giving a long, nervous explanation every single time you say no.
card('3. Over-Explaining Your "No"', 29, style='font-size:100px')

# Line 30: Think about the last time you had to decline an invitation you couldn't attend, turn down an extra favor when your plate was already full, or even walk out of a boutique without buying the item you just tried on.
row(
    [C('px9520296', 0.4, 7.5), C('desk_notebook_coffee', 0.4, 6.5), C('fabrictest20', 0.0, 3.93)],
    [at(30, 'decline an invitation'), at(30, 'turn down an extra'), at(30, 'walk out of a boutique')],
    en(30) + 0.25,
    labels=['an invitation', 'a full schedule', 'in a boutique']
)

# Line 31: When we feel uncomfortable setting a boundary, our natural instinct is to build a wall of excuses so the other person won't be upset with us.
full([(C('zendaya_roundtable_drained', 0.4, 6.8), nx(31))], TO(32))

# Line 32: We end up giving a four-sentence timeline of our entire week—talking about how busy work has been, how tired we are, what errands we have to run, or telling the sales associate in a store, "I just need to check my bank account and I'll definitely come back for it in an hour!"
framed([
    (C('nervous_overexplaining_talk', 0.4, 6.8), nx(32)),
    (C('boutique_counter_hanger', 0.4, 6.8), at(32, 'sales associate in a store')),
], en(32) + 0.35)
phrase([
    ('b', '&#8220;I&#8217;m so sorry, work has been crazy,<br>I&#8217;m exhausted, maybe next time&#8230;&#8221;')
], at(32, 'talking about how busy'), en(32) + 0.30, y=290)
phrase([
    ('b', '&#8220;I&#8217;ll definitely come back<br>for it in an hour!&#8221;')
], at(32, 'I just need to check'), en(32) + 0.30, y=510)

# Line 33: Here is the quiet truth about over-explaining: the longer your excuse, the more it sounds like you are asking for permission rather than stating a decision. Worse still, when you give three specific reasons why you can't do something, people who are pushy will often treat those reasons as obstacles to negotiate around.
quote('A long excuse sounds like asking for', st(33) + 0.15, at(33, 'Worse still') - 0.15, '<i>permission</i>, not a decision', at(33, 'permission rather'))
full([(C('jolie_tourist_train', 0.4, 6.8), at(33, 'Worse still'))], TO(34))       # Angelina Jolie on train (3.13x replay peak from RUDXBR8nyHw 4:52)

# Line 34: An elegant woman understands that kindness and boundaries are not opposites. You can be deeply warm and completely clear at the exact same time. Her secret is that she swaps long excuses for a brief, gracious refusal paired with appreciation.
full([
    (C('gwyneth_vogue_garden', 0.4, 6.0), nx(34)),                                # Gwyneth Paltrow in garden (RUDXBR8nyHw 5:51 callback)
    (C('white_sofa_polkadot_calm', 0.4, 6.0), at(34, 'Her secret is')),           # Composed woman on white sofa (RUDXBR8nyHw 5:12 callback)
], en(34) + 0.25)
text('Kindness and boundaries are <i>not</i> opposites', 'q1', at(34, 'kindness and boundaries'), at(34, 'Her secret is') - 0.20, dur=1.3)

# Line 35: If you are declining a social invitation, you never need to list your schedule. Simply say, "I won't be able to make it this time, but thank you so much for thinking of me—I hope you have a wonderful evening."
# Line 36: If someone asks you to take on a commitment you don't have the capacity for, say, "My schedule won't allow me to give that the attention it deserves right now, so I'll have to pass, but I truly appreciate you thinking of me."
# Line 37: And when you are in a shop and decide something isn't for you, a warm smile and, "Thank you so much for your help today—I'm going to think on this before deciding," is all you ever need. It is calm, honest, and leaves your self-respect completely intact.
# (One continuous 35-second cream framed + phrase sequence across Lines 35-37, dissolving to caramel on "It is calm, honest")
framed([
    (C('doorway_warm_decline', 0.4, 8.5), nx(35)),
    (C('blazer_desk_calm_no', 0.4, 8.5), nx(36)),
    (C('woolcoat33', 0.0, 7.47), nx(37)),
], at(37, 'It is calm, honest') - 0.10)
phrase([
    ('b', '&#8220;I&#8217;m so sorry, my week is crazy&#8230;&#8221;'),
    ('a md', '&#8220;I won&#8217;t be able to make it this time,<br>but thank you so much for thinking of me.&#8221;')
], at(35, "I won't be able"), nx(36) - 0.10, y=280)
phrase([
    ('b', '&#8220;I have too much on my plate&#8230;&#8221;'),
    ('a sm', '&#8220;My schedule won&#8217;t allow me to give that<br>the attention it deserves, so I&#8217;ll have to pass.&#8221;')
], at(36, 'My schedule'), nx(37) - 0.10, y=280)
phrase([
    ('b', '&#8220;I&#8217;ll come back for it in an hour!&#8221;'),
    ('a md', '&#8220;Thank you so much for your help today&#8212;<br>I&#8217;m going to think on this before deciding.&#8221;')
], at(37, 'Thank you so much'), at(37, 'It is calm, honest') - 0.15, y=280)
quote('Calm, honest, and full of <i>self-respect</i>', at(37, 'It is calm, honest'), en(37) + 0.30)


# ==============================================================================
# SECTION 5: NUMBER 4 — TURNING "HOW ARE YOU?" INTO A COMPLAINT REPORT (Lines 38-46)
# ==============================================================================
# Line 38: Number four: turning a simple "How are you?" into an exhaustion or complaint report.
card('4. The Exhaustion Report', 38, style='font-size:104px')

# Line 39: We live in a culture where being stressed and busy is almost worn like a badge of honor.
full([(C('rushed_street_coffee_watch', 0.4, 6.2), en(38) + 0.20)], TO(40))

# Line 40: So when someone asks, "How has your week been?" it is remarkably easy to default into, "Ugh, don't even ask, I am so exhausted, work has been a nightmare, the traffic was terrible, and I have a million things to do."
framed([(C('coffee_sigh_exhausted', 0.4, 8.2), nx(40))], en(40) + 0.35)
phrase([
    ('b', '&#8220;Ugh, don&#8217;t even ask, I am so exhausted,<br>work has been a nightmare&#8230;&#8221;')
], at(40, "Ugh, don't even ask"), en(40) + 0.30, y=340)

# Line 41: Now, sharing your honest struggles with a close friend or a partner in a private, heart-to-heart conversation is healthy and completely human. Elegance is never about pretending your life is perfect or suppressing your real feelings.
# Line 42: However, in everyday social interactions, greetings, and casual conversations, unloading a list of complaints the moment someone says hello instantly drains the energy out of the room.
full([
    (C('mk3183', 0.5, 6.5), nx(41)),                                              # Close friends on sofa with tea
    (C('cozy_knit_window_calm', 0.4, 5.5), at(41, 'Elegance is never')),          # Peaceful woman at home window
    (C('dinner_drained_listener', 0.4, 7.5), nx(42)),                             # Casual greeting where listener looks weighed down
], en(42) + 0.25)

# Line 43: Interestingly, emotions are contagious—psychology shows that people naturally mirror the vocal tone and nervous system state of the person speaking to them. When every greeting turns into a heavy sigh about how tired or overwhelmed you are, people unconsciously begin to associate your presence with tension and heaviness.
quote('Emotions are <i>contagious</i>', st(43) + 0.15, at(43, 'When every greeting') - 0.15, 'People mirror the energy you bring', at(43, 'people naturally mirror'))
full([(C('calm_breath_daylight', 0.4, 6.5), at(43, 'When every greeting'))], TO(44))

# Line 44: A woman of poise knows how to stay honest and grounded while keeping her everyday energy light and uplifting. Even when she is having a busy or demanding week, she frames her answer with composure and gently turns the warmth back toward the other person.
full([
    (C('kate_middleton_warm_greeting', 0.4, 5.2), nx(44)),
    (C('mk12117', 8.5, 14.5), at(44, 'Even when she is')),
], en(44) + 0.25)

# Line 45: Instead of listing everything that went wrong that morning, try saying, "It's been a really full week, so I'm really enjoying slowing down today—how have you been?" Or, "Taking things one day at a time right now, and I'm so glad to be here with you—tell me what's new in your world."
# Line 46: And on a good week, sharing one small, specific positive detail—like, "Things have been lovely, I've really been enjoying the cooler mornings lately—what has been the highlight of your week?"—instantly makes you the breath of fresh air in someone else's day.
framed([
    (C('mk41810', 0.3, 6.5), nx(45)),
    (C('over60chic4', 0.0, 6.8), at(45, 'Taking things one day')),
    (C('mk49916', 0.3, 7.5), nx(46)),
], at(46, 'instantly makes you') - 0.10)
phrase([
    ('b', '&#8220;Ugh, everything went wrong today&#8230;&#8221;'),
    ('a md', '&#8220;It&#8217;s been a full week, so I&#8217;m enjoying<br>slowing down today&#8212;how have you been?&#8221;')
], at(45, "It's been a really full"), at(45, 'Taking things one day') - 0.10, y=280)
phrase([
    ('b', '&#8220;I have a million things to do&#8230;&#8221;'),
    ('a md', '&#8220;Taking things one day at a time, and<br>I&#8217;m so glad to be here with you.&#8221;')
], at(45, 'Taking things one day'), nx(46) - 0.10, y=280)
phrase([
    ('a md', '&#8220;Things have been lovely&#8212;what has been<br>the highlight of your week?&#8221;')
], at(46, 'Things have been lovely'), at(46, 'instantly makes you') - 0.15, y=330)
quote('Be the <i>breath of fresh air</i>', at(46, 'instantly makes you'), en(46) + 0.30, "in someone else&#8217;s day", at(46, 'breath of fresh air') + 0.35)


# ==============================================================================
# SECTION 6: MID-VIDEO PROMOTION BRIDGE (Lines 47-49)
# Placed cleanly after Point 4, followed immediately by White Card #5
# ==============================================================================
# Line 47: And speaking of carrying yourself with effortless confidence, there is a secret many elegant women quietly invest in: they don't leave their personal style and presence to guesswork.
canvas_full(C('woolcoat46', 0.0, 7.8), nx(47), en(47) + 0.25)

# Line 48: If you want to discover your exact body shape, find the colors and silhouettes that flatter you best, and build a timeless wardrobe that makes you feel confident every single day, check out our Personal Stylist Guide and our complete collection of Classy Lady Guides linked in the description box below.
# Line 49: Everything is sent straight to your email the moment you order so you can start your transformation right away.
row(
    [C('proportion3', 8.0, 13.0), C('midivneck9', 3.3, 8.8), C('navyblazer4', 0.0, 5.8)],
    [at(48, 'exact body shape'), at(48, 'colors and silhouettes'), at(48, 'timeless wardrobe')],
    at(48, 'check out our Personal') - 0.10,
    labels=['body shape', 'your colors', 'timeless wardrobe']
)
full([
    (C('fabriclight16', 1.0, 7.2), at(48, 'check out our Personal') - 0.15),
    (C('mk43250', 0.3, 6.0), nx(49)),
], en(49) + 0.35)
guide_haze(at(48, 'check out our Personal'), en(49) + 0.30)


# ==============================================================================
# SECTION 7: NUMBER 5 — CORRECTING SMALL DETAILS IN PUBLIC (Lines 50-57)
# ==============================================================================
# Line 50: Number five: jumping in to publicly correct small, unimportant details when someone else is speaking.
card('5. Correcting Small Details in Public', 50, style='font-size:96px')

# Line 51: Picture this scenario: you are at dinner with friends or colleagues, and someone is excitedly telling a story. Midway through, they say, "So when we went to that restaurant on Wednesday..." and someone at the table immediately cuts in with, "Actually, that wasn't Wednesday, it was Tuesday, and it wasn't that restaurant, it was the one down the street."
# Line 52: Or in a group discussion, someone shares an opinion and another person immediately responds with a sharp, "Actually, you're wrong about that."
full([(C('scent_woman_dinner', 0.4, 5.8), en(50) + 0.20)], at(51, 'and someone at the table') + 0.10)
framed([
    (C('dinner_interrupt_cut', 0.4, 6.8), at(51, 'and someone at the table')),
    (C('mk12123', 0.5, 6.5), nx(52)),
], en(52) + 0.35)
phrase([
    ('b', '&#8220;Actually, that wasn&#8217;t Wednesday,<br>it was Tuesday&#8230;&#8221;')
], at(51, 'Actually, that'), nx(52) - 0.10, y=330)
phrase([
    ('b', '&#8220;Actually, you&#8217;re wrong<br>about that.&#8221;')
], at(52, 'Actually, you'), en(52) + 0.30, y=330)

# Line 53: When we correct tiny factual details that don't change the heart of someone's story, we might feel like we are just being accurate. But to everyone around the table, it interrupts the storyteller's momentum and quietly puts them on the spot for no real reason.
full([
    (C('storyteller_pauses_awkward', 0.4, 5.5), nx(53)),
    (C('dinner_guests_uncomfortable', 0.4, 5.5), at(53, 'But to everyone')),
], en(53) + 0.25)

# Line 54: An elegant woman always asks herself a quiet question before correcting someone in public: does this detail actually matter, or am I just interrupting the warmth of the moment to be right?
quote('Does this detail actually matter&#8212;or am I', st(54) + 0.15, en(54) + 0.30, 'interrupting the <i>warmth</i> to be right?', at(54, 'interrupting the warmth'))

# Line 55: When a detail is harmless—like whether a trip happened in May or June—she simply lets it pass and allows the other person to enjoy telling their story.
full([(C('charade', 154.0, 161.2), nx(55))], en(55) + 0.25)                      # Audrey Hepburn listening with a warm, indulgent smile

# Line 56: And when she does need to offer a different perspective in a real discussion, or even respond to someone who has just made a sharp or passive-aggressive remark toward her, she never matches sharpness with sharpness. Instead of saying, "Actually, you're wrong," she bridges with grace and says, "I see what you mean—here is how I look at it."
# Line 57: And if someone says something genuinely rude or pointed in a group setting, rather than snapping back and losing her composure, she pauses briefly and says in a calm, even voice, "I'm not sure that was meant to come across that way, let's try that again," or simply, "I value peace much more than arguing, so I'll leave that there." That quiet self-control commands more respect than raising your voice ever could.
framed([
    (C('white_sofa_interview_two', 0.4, 7.2), nx(56)),                            # Exact parallel to RUDXBR8nyHw 3:23 ("I see what you mean, here's how I see it")
    (C('mk12120', 1.5, 7.2), at(56, 'Instead of saying')),
    (C('cate_blanchett_calm_pause', 0.4, 7.0), nx(57)),
    (C('cream_blazer_tea_nod', 0.4, 6.8), at(57, 'I value peace')),
], at(57, 'That quiet self-control') - 0.10)
phrase([
    ('b', '&#8220;Actually, you&#8217;re wrong.&#8221;'),
    ('a', '&#8220;I see what you mean&#8212;<br>here is how I look at it.&#8221;')
], at(56, 'Instead of saying'), nx(57) - 0.10, y=280)
phrase([
    ('a md', '&#8220;I&#8217;m not sure that was meant to come<br>across that way, let&#8217;s try that again.&#8221;')
], at(57, "I'm not sure that"), at(57, 'I value peace') - 0.10, y=320)
phrase([
    ('a md', '&#8220;I value peace much more than arguing,<br>so I&#8217;ll leave that there.&#8221;')
], at(57, 'I value peace'), at(57, 'That quiet self-control') - 0.15, y=320)
quote('Quiet <i>self-control</i> commands', at(57, 'That quiet self-control'), en(57) + 0.30, 'more respect than volume', at(57, 'more respect'))


# ==============================================================================
# SECTION 8: NUMBER 6 — MAKING MONEY THE CENTER OF CONVERSATION (Lines 58-65)
# ==============================================================================
# Line 58: Number six: making money and price tags the center of casual conversation—either by bragging about how expensive something is, or by putting yourself down about your budget.
card('6. Talking About Price Tags', 58, style='font-size:100px')

# Line 59: We have probably all heard both sides of this. On one hand, there is the person who cannot mention a handbag, a hotel, or a dinner without working the exact price tag or designer label into the sentence so everyone knows how much they spent.
row(
    [C('logo_handbag_street', 0.4, 6.5), C('luxury_hotel_balcony', 0.4, 6.5), C('fine_dining_champagne', 0.4, 6.5)],
    [at(59, 'a handbag'), at(59, 'a hotel'), at(59, 'or a dinner')],
    en(59) + 0.25,
    labels=['the handbag', 'the hotel', 'the dinner']
)

# Line 60: As the old saying goes, money talks, but wealth whispers—and needing to announce the cost of your lifestyle only reveals a need for validation.
quote('Money talks,', st(60) + 0.15, en(60) + 0.30, 'but wealth <i>whispers</i>', at(60, 'wealth whispers'))

# Line 61: But there is another side to this that many kind, well-meaning women fall into without realizing it, and that is loud financial self-deprecation. It sounds like saying, "I'm so broke right now, I can't afford anything," in the middle of a casual group chat, or when someone compliments your bag, immediately blurting out, "Oh, it's fake, it's just a cheap knockoff I found online!"
framed([
    (C('cafe_group_chatting', 0.4, 6.5), nx(61)),
    (C('leather_bag_wave_off', 0.4, 6.8), at(61, 'compliments your bag')),
], en(61) + 0.35)
phrase([
    ('b', '&#8220;I&#8217;m so broke right now,<br>I can&#8217;t afford anything.&#8221;')
], at(61, "I'm so broke"), en(61) + 0.30, y=290)
phrase([
    ('b', '&#8220;Oh, it&#8217;s fake, it&#8217;s just a<br>cheap knockoff I found online!&#8221;')
], at(61, "Oh, it's fake"), en(61) + 0.30, y=510)

# Line 62: Whether you are building your savings from scratch or living very comfortably, your bank account is private, and treating your finances with quiet dignity is a hallmark of true class.
full([(C('michelle_obama_stage_suit', 0.4, 7.2), nx(62))], en(62) + 0.25)         # Michelle Obama on stage (Never Share 5:14 callback)

# Line 63: When someone asks where you got something or hints at how much it cost, you never need to announce a price tag or apologize for a bargain. Simply smile and say, "Thank you! It was such a wonderful find and I've loved wearing it—I'd be happy to send you the link if you'd like."
# Line 64: And if friends invite you to an expensive dinner or trip that doesn't align with your financial priorities right now, you never need to say, "I'm too broke for that." Instead, say with complete confidence, "I'm going to sit this dinner out, but I would love to grab coffee with you next week," or "That is outside what I'm prioritizing right now, so let's plan a lunch together soon instead."
framed([
    (C('over60chic0', 3.0, 9.0), nx(63)),
    (C('mk41810', 4.8, 9.1), nx(64)),
    (C('px8922355', 5.0, 10.5), at(64, 'That is outside')),
], en(64) + 0.35)
phrase([
    ('b', '&#8220;It was super cheap / It cost a fortune.&#8221;'),
    ('a md', '&#8220;Thank you! It was such a wonderful<br>find and I&#8217;ve loved wearing it.&#8221;')
], at(63, 'Thank you! It was'), nx(64) - 0.10, y=280)
phrase([
    ('b', '&#8220;I&#8217;m too broke for that.&#8221;'),
    ('a sm', '&#8220;I&#8217;m going to sit this dinner out, but I&#8217;d<br>love to grab coffee with you next week.&#8221;')
], at(64, "I'm going to sit"), at(64, 'That is outside') - 0.10, y=280)
phrase([
    ('b', '&#8220;I can&#8217;t afford that right now.&#8221;'),
    ('a sm', '&#8220;That is outside what I&#8217;m prioritizing right<br>now&#8212;let&#8217;s plan a lunch together soon.&#8221;')
], at(64, 'That is outside'), en(64) + 0.30, y=280)

# Line 65: There is nothing more sophisticated than a woman who lives within her means gracefully and without embarrassment.
quote('Living within your means', st(65) + 0.15, en(65) + 0.30, '<i>gracefully</i> and without embarrassment', at(65, 'gracefully'))


# ==============================================================================
# SECTION 9: NUMBER 7 — GOSSIP STARTERS DISGUISED AS CONCERN (Lines 66-73)
# ==============================================================================
# Line 66: Number seven: gossip starters disguised as concern.
card('7. Gossip Disguised as Concern', 66, style='font-size:100px')

# Line 67: You know the exact phrases I am talking about. They almost always begin in a hushed voice with, "Don't tell anyone I told you this, but..." or "I feel so bad saying this, I'm only bringing it up because I'm worried about her, but did you hear what happened?"
framed([(C('whispering_table_two', 0.4, 9.8), en(66) + 0.20)], en(67) + 0.35)
phrase([
    ('b', '&#8220;Don&#8217;t tell anyone I told<br>you this, but&#8230;&#8221;')
], at(67, "Don't tell anyone"), en(67) + 0.30, y=290)
phrase([
    ('b', '&#8220;I&#8217;m only bringing it up because<br>I&#8217;m worried about her, but&#8230;&#8221;')
], at(67, "I'm only bringing"), en(67) + 0.30, y=510)

# Line 68: It is so easy to get pulled into these moments because in the short term, sharing a secret or talking about someone who isn't in the room can feel like instant bonding. Nobody wants to feel like the stiff, judgmental person in the group who lectures everyone else.
full([
    (C('mk42716', 0.5, 6.0), nx(68)),
    (C('terrace_woman_quiet_listen', 0.4, 6.0), at(68, 'Nobody wants to feel')),
], en(68) + 0.25)

# Line 69: Yet have you ever noticed what people think five minutes after a gossip session ends? Everyone secretly realizes that if a person will talk about a friend's private struggles the moment she leaves the table, she will do the exact same thing to you the moment you walk away.
quote('If she speaks of others when they leave,', st(69) + 0.20, en(69) + 0.30, 'she will speak of <i>you</i> when you walk away', at(69, 'she will do'))

# Line 70: An elegant woman protects her reputation as a safe, trustworthy person, and she knows how to step out of gossip warmly—without sounding preachy or making the other person feel scolded.
full([(C('jolie_thr_roundtable_nod', 0.4, 7.2), nx(70))], en(70) + 0.25)           # Angelina Jolie at THR Roundtable (RUDXBR8nyHw 2:23 callback)

# Line 71: When someone tries to pull you into speaking poorly about someone else, you don't need to make a big scene. You can gently neutralize the moment and redirect the conversation by saying, "I really don't know the full story, so I couldn't say—I just hope everything works out well for her."
# Line 72: Or, if someone presses you for private details you shouldn't share, say warmly, "That is really her story to tell whenever she feels ready."
# Line 73: And my favorite way to pivot a group conversation back to higher ground is simply saying, "All I know is she has always been lovely to me—by the way, I have been meaning to ask you about your trip!" People will instantly respect your discretion, and they will know deep down that their own name is safe with you too.
framed([
    (C('hijab_burgundy_speaking', 0.4, 8.5), nx(71)),                             # Burgundy hijabi model speaking softly (RUDXBR8nyHw 3:28 callback)
    (C('over60chic8', 1.8, 8.2), nx(72)),
    (C('mk12122', 6.8, 12.5), nx(73)),
], at(73, 'People will instantly') - 0.10)
phrase([
    ('b', '&#8220;Did you hear what happened to her?&#8221;'),
    ('a sm', '&#8220;I really don&#8217;t know the full story&#8212;<br>I just hope everything works out well for her.&#8221;')
], at(71, "I really don't know"), nx(72) - 0.10, y=280)
phrase([
    ('a md', '&#8220;That is really her story to tell<br>whenever she feels ready.&#8221;')
], at(72, 'That is really her'), nx(73) - 0.10, y=330)
phrase([
    ('a sm', '&#8220;All I know is she has always been lovely to me&#8212;<br>by the way, tell me about your trip!&#8221;')
], at(73, 'All I know is'), at(73, 'People will instantly') - 0.15, y=310)
quote('They will know their own name', at(73, 'People will instantly'), en(73) + 0.30, 'is <i>safe with you</i> too', at(73, 'safe with you'))


# ==============================================================================
# SECTION 10: NUMBER 8 — THE FIVE ONE-SECOND "ROUGH WORDS" (Lines 74-81)
# Includes authentic 4.4s real-voice insert (FILMAUDIO) after Line 75
# ==============================================================================
# Line 74: And finally, number eight: replacing the five automatic "rough words" that slip into our everyday speech when we are on autopilot.
card('8. The Five One-Second Swaps', 74, style='font-size:100px')

# Line 75: When you listen to timelessly graceful women—think of the way Audrey Hepburn or Princess Diana spoke in interviews—what stands out isn't that they used complicated, academic words. It is that their everyday responses were soft, unhurried, and considerate.
pair(
    [C('charade', 95.2, 102.5), C('diana_interview_soft', 0.2, 7.5)],
    [at(75, 'Audrey Hepburn'), at(75, 'Princess Diana')],
    en(75) + 0.20,
    labels=['Audrey Hepburn', 'Princess Diana']
)
# Authentic 4.4-second Real-Voice Demonstration Insert (during gaps.json["75"] = 4.95s pause, zero text clutter, matching RUDXBR8nyHw 0:32 & 1:44)
FS_AUDIO = en(75) + 0.25
full([(C('charade', 179.35, 183.75), FS_AUDIO)], FS_AUDIO + 4.45, xf=0.25)
FILMAUDIO.append(('charade', 179.35, 183.75, FS_AUDIO))

# Line 76: Most of us have a few automatic one-word replies that sound slightly blunt or dismissive even when our heart is warm. Let's walk through five quick swaps you can start using today.
quote('Soft, unhurried, and <i>considerate</i>', st(76) + 0.15, en(76) + 0.30, 'in everyday replies', at(76, 'five quick swaps'))

# Line 77: First, when you didn't quite hear what someone said, instead of a sharp "What?" or "Huh?", soften your tone and say, "Pardon?" or "Sorry, could you say that again?"
word_card('What?', st(77) - 0.05, at(77, 'soften your tone') - 0.10)              # Single-word card matching "Like" at 2:28 in RUDXBR8nyHw
# Continuous 5-Swap Cream Framed Sequence across Lines 77b-81a (matching RUDXBR8nyHw 3:08-3:38 peak!)
framed([
    (C('amal_stage_listening', 0.4, 6.8), at(77, 'soften your tone') - 0.05),     # Swap 1: Amal Clooney ("What?" -> "Say that again" at 6:31 in RUDXBR8nyHw)
    (C('px8922355', 10.8, 18.5), nx(78)),                                         # Swap 2: Two women at restaurant table choosing
    (C('mk41221', 0.3, 7.5), nx(79)),                                             # Swap 3: Warm thank-you exchange
    (C('cream_blouse_desk_nod', 0.4, 7.5), nx(80)),                               # Swap 4: Agreeing warmly ("Yeah, that's fine" -> "Sure, I'd be happy to")
    (C('px9520296', 8.0, 15.0), nx(81)),                                          # Swap 5: Smiling warmly before hanging up phone in camel coat
], at(81, 'Those tiny touches') - 0.10)
phrase([
    ('b', '&#8220;What? / Huh?&#8221;'),
    ('a', '&#8220;Pardon?&#8221;<br>&#8220;Could you say that again?&#8221;')
], at(77, 'Pardon'), nx(78) - 0.10, y=280)
phrase([
    ('b', '&#8220;Yeah, whatever, I don&#8217;t care.&#8221;'),
    ('a md', '&#8220;Both options sound lovely to me&#8212;<br>which one are you leaning toward?&#8221;')
], at(78, 'Both options'), nx(79) - 0.10, y=280)
phrase([
    ('b', '&#8220;No problem. / Yep.&#8221;'),
    ('a', '&#8220;Of course, my pleasure.&#8221;<br>&#8220;You are so welcome.&#8221;')
], at(79, 'Of course, my pleasure'), nx(80) - 0.10, y=280)
phrase([
    ('b', '&#8220;Yeah, that&#8217;s fine.&#8221;'),
    ('a md', '&#8220;Sure, I would be happy to do that.&#8221;<br>&#8220;Certainly, I can take care of that.&#8221;')
], at(80, 'Sure, I would'), nx(81) - 0.10, y=280)
phrase([
    ('b', '&#8220;Okay, bye.&#8221;'),
    ('a md', '&#8220;It was really lovely<br>speaking with you.&#8221;')
], at(81, 'It was really lovely'), at(81, 'Those tiny touches') - 0.15, y=300)
quote('Tiny touches of <i>warmth</i> linger', at(81, 'Those tiny touches'), en(81) + 0.30, 'long after the conversation ends', at(81, 'long after'))


# ==============================================================================
# SECTION 11: ENDING & CALL TO ACTION (Lines 82-85 + 4.2s White End Card)
# ==============================================================================
# Line 82: Remember, my loves, none of these eight shifts are about becoming stiff, overly formal, or pretending to be someone you are not. True elegance is simply where self-respect meets warmth toward others.
row(
    [C('over60chic23', 0.0, 6.0), C('curvychic17', 3.0, 8.87), C('over60chic2', 5.3, 11.5)],
    [st(82), st(82) + 0.45, st(82) + 0.90],
    at(82, 'True elegance is') - 0.10
)
quote('True elegance is where <i>self-respect</i>', at(82, 'True elegance is'), en(82) + 0.30, 'meets <i>warmth</i> toward others', at(82, 'meets warmth'))

# Line 83: Even choosing just one or two of these phrases to practice this week will quietly transform how confident you feel when you speak—and how naturally people lean in when they are around you.
full([(C('charade', 254.0, 258.9), nx(83))], en(83) + 0.25)

# Line 84: Now I would love to hear from you: which of these eight verbal swaps are you going to practice first this week? Let me know the number in the comments below—I read every single comment and I genuinely love hearing your stories and thoughts.
quote_side(
    C('over60chic8', 17.43, 22.6), st(84) - 0.05, en(84) + 0.30,
    'Which swap will you try <i>first</i>?', 'Tell us the number in the comments', at(84, 'Let me know the number')
)

# Line 85: If you enjoyed today's video, please give it a thumbs up, subscribe to Classy Academy if you haven't already, and don't forget to check out our Personal Stylist Guide and Classy Lady Guides linked in the description box below. Thank you so much for watching, and until next time. Bye, my loves.
canvas_full(C('camelwalk0', 0.0, 4.8), nx(85), at(85, 'Thank you so much') - 0.05, fin=0.5, fout=0.45)
canvas_full(C('woolcoat33', 7.47, 14.0), at(85, 'Thank you so much'), total - 2.8, fin=0.45, fout=0.6)
# Note: build.py automatically appends the crisp white end card (.endwhite + .endlogo `logo_ce_dark.png`) over the final 3.0 seconds as the solo piano fades out.
