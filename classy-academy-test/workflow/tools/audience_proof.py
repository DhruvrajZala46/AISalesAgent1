# audience_proof.py - what OUR viewers really value, measured from their own likes and comments.
# usage: python3 audience_proof.py <data dir with videos.json + comments.json>                 -> videos ranked by love
#        python3 audience_proof.py <data dir> --video "Sound More Elegant"                      -> the tips viewers quoted, thanked, pushed back on
#        python3 audience_proof.py <data dir> --ask "speak|manners|etiquette|disrespect"        -> what they ask us to make (with likes)
# Views say what gets clicked. Like rate, "thank you" comments, shares and "best tip" comments say what was worth it.
# A tip goes into a script only with proof: viewers quoted or thanked it here, and/or the niche winners teach it (proof map).
import json, re, sys, os
D = sys.argv[1]; args = sys.argv[2:]
V = json.load(open(os.path.join(D, 'videos.json'))); C = json.load(open(os.path.join(D, 'comments.json')))
THANK = re.compile(r'thank|helpful|useful|learn|so true|great tips|needed this|changed|best tip|life.?saver', re.I)
SHARE = re.compile(r'daughter|friend|sister|\bmom\b|mother|niece|shar(e|ing) (this|it)|sent this|send this|granddaughter', re.I)
MORE = re.compile(r'part 2|part two|more (videos|tips|of this)|another video|please (do|make)|video (on|about)', re.I)
TIP = re.compile(r'best tip|i (started|tried|now|stopped|began)|i\'m going to|changed (my|the)|game|^\s*1[.)]', re.I | re.M)
PUSH = re.compile(r'\b(but|disagree|not true|feels? (rude|demanding|cold)|i (just|would rather)|instead i)\b', re.I)
NARR = re.compile(r"(your|her|the) (beautiful |lovely |soothing |calm |calming |soft )?voice|love (the|your|her) voice", re.I)
def com(vid): return [k for k in C if k['vid'] == vid]
if not args:
    print(f"{'like%':>6} {'thanks':>6} {'shares':>6} {'more':>5} {'tips':>5} {'views':>9}  title")
    rows = []
    for x in V:
        cs = com(x['id'])
        rows.append((x['likes'] / max(1, x['views']) * 100, sum(bool(THANK.search(k['text'])) for k in cs), sum(bool(SHARE.search(k['text'])) for k in cs),
                     sum(bool(MORE.search(k['text'])) for k in cs), sum(bool(TIP.search(k['text'])) for k in cs), x['views'], x['title'][:68]))
    for r in sorted(rows, key=lambda r: -r[0]): print(f"{r[0]:6.2f} {r[1]:6} {r[2]:6} {r[3]:5} {r[4]:5} {r[5]:9}  {r[6]}")
elif args[0] == '--video':
    x = [v for v in V if args[1].lower() in v['title'].lower()][0]; cs = sorted(com(x['id']), key=lambda k: -k['likes'])
    print(x['title'], x['views'], 'views', f"{x['likes'] / x['views'] * 100:.2f}% liked", len(cs), 'comments\n')
    for name, rx in (('TIPS QUOTED / TRIED', TIP), ('THANKS', THANK), ('ASKS FOR MORE', MORE), ('PUSHBACK', PUSH)):
        print('==', name)
        for k in [k for k in cs if rx.search(k['text']) and not (name == 'THANKS' and NARR.search(k['text']))][:8]:
            print(f"  {k['likes']:4} | {k['text'][:170]}".replace('\n', ' '))
elif args[0] == '--ask':
    rx = re.compile(args[1], re.I)
    xs = sorted([k for k in C if rx.search(NARR.sub('', k['text'])) and MORE.search(k['text']) or (rx.search(NARR.sub('', k['text'])) and re.search(r'please|could you|can you', k['text'], re.I))], key=lambda k: -k['likes'])
    print(len(xs), 'requests,', sum(k['likes'] for k in xs), 'likes')
    for k in xs[:20]: print(f"  {k['likes']:4} | {k['title'][:30]} | {k['text'][:150]}".replace('\n', ' '))
