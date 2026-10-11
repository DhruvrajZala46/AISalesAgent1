#!/usr/bin/env python3
"""fit.py - audience fit: does an idea or a script match what THIS channel's viewers know it for?

The multiple (rank.py) says a topic is wanted in the niche. It does not say the tips inside belong to
this channel. A hot topic told the wrong way ("runway news", "quiet luxury is over", "bright colours
are not elegant") is how a channel upsets the audience that built it. fit.py measures that.

    python3 fit.py build [transcripts_dir] [comments.json]   # rebuild audience/dna.json
    python3 fit.py profile                                    # print the channel's content DNA
    python3 fit.py idea "Title one" "Title two" ...           # topic fit for candidate ideas
    python3 fit.py check script.md [--expect trend]           # tip-type fit for a script

The baseline is the channel's OWN words: audience/transcripts/*.txt (one per video, with views in
the header) plus comment themes. In a .md script only the **bold** spoken lines are measured, so
[ON SCREEN] notes don't count as speech, but they are checked for red lines.
"""
import json, os, re, sys, glob, statistics

HERE = os.path.dirname(os.path.abspath(__file__)); AUD = os.path.join(HERE, '..', 'audience')
DNA = os.path.join(AUD, 'dna.json')

# What kind of tip is being taught. kind: risk = more than the channel is a warning sign,
# core = keep near the channel's level, wanted = the audience asks for it, more is fine.
PROBES = {
    'runway / fashion week / designers': ('risk', r'runway|fashion week|\bdesigners?\b|\bcollections?\b'),
    'luxury brand names': ('risk', r'\b(chanel|dior|celine|herm[eè]s|gucci|prada|the row|tom ford|ysl|saint laurent|loewe|burberry|chlo[eé]|bottega|valentino|fendi|balenciaga|louis vuitton)\b'),
    'trend / trendy': ('risk', r'\btrend'),
    'hype words': ('risk', r'\b(insane|crazy|game.?changer|obsessed|must.?have|viral)\b'),
    'statistics / studies': ('risk', r'\d+\s?%|percent|stud(y|ies) (show|found)|scientists'),
    'timeless / classic': ('core', r'timeless|classic'),
    'swap: instead / try': ('core', r'\binstead\b|\btry\b|\bswap'),
    'elegant women tend to / often': ('core', r'elegant women (tend|often|choose|know|don)'),
    'colour names': ('core', r'\b(cream|ivory|camel|beige|navy|chocolate|burgundy|oatmeal|olive|charcoal)\b'),
    'budget / not about cost': ('wanted', r'budget|afford|cost|don.?t need (a|to buy)|without (buying|spending)'),
    'you may already own it': ('wanted', r'already (own|have)|in your (closet|wardrobe)'),
    'any age / every woman': ('wanted', r'any age|every age|at every|every woman|all ages'),
}
# Things that contradict what the channel stands for or what its viewers pushed back on.
RED_LINES = [
    (r"(quiet luxury|elegance)[^.]{0,30}\b(is over|is dead|has ended)|end of quiet luxury|death of quiet luxury",
     'Says quiet luxury/elegance is over: contradicts "How to Dress Quiet Luxury" and the channel stance.'),
    (r"(colou?rs?|neon|bright|purple|red|pink|yellow|orange|green|violet)[^.\n]{0,40}(are|is|look)n?'?t? (not )?(elegant|classy)[^.\n]{0,5}(never|not)|(never|not) (elegant|classy)[^.\n]{0,25}(colou?r|bright)",
     'Bans a colour: viewers pushed back hard (667- and 424-like replies). Refine, never ban.'),
    (r"✕[^\n]{0,60}\b(bright|violet|neon|red|pink|yellow|orange)\b|\b(bright|violet|neon)\b[^\n]{0,30}✕",
     'A ✕ on a bright colour on screen: the same pushback, visually.'),
    (r"\b(ugly|tacky|frumpy|trashy|basic girls?|rich people|poor people)\b", 'Shaming or rich-vs-poor language: not the channel voice.'),
    (r"(?<!n't )(?<!not )(?<!never )(?<!no need to )\b(chase|follow) (every|all the) trends?\b", 'Tells viewers to chase trends: the channel teaches the opposite.'),
]
# What the channel has said about trends, in its own words (shown when an idea touches trends).
STANCE = r"[^.?!]*\btrends?\b[^.?!]*[.?!]"

def spoken(path):
    t = open(path, encoding='utf-8').read()
    t = re.split(r'^#+\s*Sources', t, flags=re.M)[0]          # quoted sources are not our words
    if path.endswith('.md'):
        lines = re.findall(r'^\*\*(.+?)\*\*\s*$', t, re.M)
        hooks = re.findall(r'^>\s*(.+)$', t, re.M)
        return ' '.join(hooks[:1] + lines), t
    return t, t

def rate(text, pat): return len(re.findall(pat, text, re.I)) / max(1, len(text.split())) * 1000

def build(tdir=None, comments=None):
    tdir = tdir or os.path.join(AUD, 'transcripts')
    vids = []
    for f in sorted(glob.glob(os.path.join(tdir, '*.txt'))):
        raw = open(f, encoding='utf-8').read(); m = re.search(r'^# (.+)\n# views=(\d+)', raw)
        if not m: continue
        vids.append(dict(title=m.group(1), views=int(m.group(2)), text=re.sub(r'^#.*\n', '', raw, flags=re.M).lower()))
    allt = ' '.join(v['text'] for v in vids); med = statistics.median(v['views'] for v in vids)
    dna = dict(videos=[dict(title=v['title'], views=v['views'], multiple=round(v['views'] / med, 2)) for v in vids],
               median_views=med, words=len(allt.split()),
               rates={k: round(rate(allt, p), 3) for k, (_, p) in PROBES.items()},
               stance=sorted({s.strip() for v in vids for s in re.findall(STANCE, v['text']) if len(s) < 200})[:12])
    old = json.load(open(DNA)) if os.path.exists(DNA) else {}
    dna['comments'] = old.get('comments', {})
    if comments and os.path.exists(comments):
        c = json.load(open(comments))
        themes = {'calm voice': r'voice|calm|sooth|relax|peaceful', 'asks for part 2 / more': r'part 2|part two|more videos|next video',
                  'timeless / classic': r'timeless|classic|never go(es)? out', 'shares it (daughter, friend)': r'shar|send(ing)? (this|it) to|my daughter|my friend',
                  'budget / money': r'budget|money|afford|cheap|thrift|second.?hand', 'age 40-70+': r'\b(40|50|60|70)s?\b|older|my age|grandm|mature',
                  'bright colour pushback': r'(bright|colou?r)[^.]{0,60}(can be|are|is) (elegant|classy|beautiful|stunning)|disagree[^.]{0,40}colou?r',
                  'anti-logo / understated': r'logo|flashy|understated'}
        dna['comments'] = dict(total=len(c), themes={k: dict(comments=sum(1 for x in c if re.search(p, x['text'], re.I)),
                               likes=sum(x['likes'] for x in c if re.search(p, x['text'], re.I))) for k, p in themes.items()})
    json.dump(dna, open(DNA, 'w'), indent=1); print(f'dna.json: {len(vids)} videos, {dna["words"]:,} words, comments: {dna["comments"].get("total", "kept")}')

def profile():
    d = json.load(open(DNA))
    print(f"\nCONTENT DNA - {len(d['videos'])} of the channel's own videos ({d['words']:,} words), median {d['median_views']:,.0f} views")
    print('\n  What the channel teaches (mentions per 1,000 spoken words):')
    for k, v in d['rates'].items(): print(f'    {k:<34} {v:5.2f}   [{PROBES[k][0]}]')
    if d.get('comments', {}).get('themes'):
        print(f"\n  What viewers say ({d['comments']['total']:,} comments):")
        for k, v in sorted(d['comments']['themes'].items(), key=lambda x: -x[1]['likes']): print(f"    {k:<30} {v['comments']:>4} comments {v['likes']:>6} likes")
    print('\n  The channel in its own words on trends:'); [print('    "' + s + '"') for s in d['stance'][:8]]
    print('\n  Best videos:'); [print(f"    {v['multiple']:4.1f}x  {v['title']}") for v in sorted(d['videos'], key=lambda v: -v['multiple'])[:6]]

# words that mean the same topic to a viewer: seasons, clothes, colour, habits
GROUPS = {'season': r'winter|fall|autumn|summer|spring|holiday|christmas|season', 'wardrobe': r'wear|dress|outfits?|wardrobe|coats?|clothes|clothing|jeans|shoes|knit\w*|trends?|essentials',
          'colour': r'colou?rs?|combos?', 'habits': r'habits?|behavio\w*|signs?|gestures?|presence|respect|public|share|room',
          'hair': r'hair\w*|haircuts?', 'expensive': r'expensive|luxury|old money|classy|budget'}
def toks(s, stop):
    w = set(re.findall(r"[a-z]+", s.lower())) - stop
    return w | {g for g, p in GROUPS.items() if re.search(r'\b(' + p + r')\b', s, re.I)}

def idea(titles):
    d = json.load(open(DNA)); STOP = set('the a an of for to in on and or is are with your you my i this that it how what why things never wear that make look elegant ladies women'.split())
    for t in titles:
        tw = toks(t, STOP)
        # ALL own videos that share a topic group or 2+ words: never just the closest few (that flatters)
        near = [v for v in d['videos'] if len(tw & set(GROUPS) & toks(v['title'], STOP)) >= 1 or len((tw - set(GROUPS)) & toks(v['title'], STOP)) >= 2]
        print(f'\n  "{t}"')
        if near:
            ms = sorted((v['multiple'] for v in near), reverse=True)
            print(f'    your audience on this topic: {len(near)} of your videos, median {statistics.median(ms):.1f}x your usual views  [all: {", ".join(f"{m:.1f}" for m in ms)}]')
            for v in sorted(near, key=lambda v: -v['multiple'])[:3]: print(f"      {v['multiple']:4.1f}x  {v['title']}")
        else: print('    none of your videos are close: new ground. Check it against the channel stance before committing.')
        if re.search(r'trend|runway|2026|2027|new|latest', t, re.I):
            print('    stance: you teach "don\'t chase every trend, choose what works for you". Tell this idea through that lens.')
        if any(re.search(p, t, re.I) for p, _ in RED_LINES): print('    RED LINE in the title itself.')

def check(path, expect=()):
    d = json.load(open(DNA)); text, full = spoken(path); n = len(text.split()); bad = 0
    print(f'\nAUDIENCE FIT - {os.path.basename(path)} ({n:,} spoken words) vs the channel ({d["words"]:,} words)\n')
    print(f'  {"tip type":<34} {"channel":>8} {"script":>8}')
    for k, (kind, p) in PROBES.items():
        a, b = d['rates'][k], rate(text, p); note = ''
        if kind == 'risk' and b > max(1.0, 3 * a):
            exp = any(e in k for e in expect); note = '  (topic word, expected)' if exp else '  !! much more than the channel'; bad += not exp
        elif kind == 'core' and a > 0.5 and b < 0.5 * a: note = '  !! less than the channel'; bad += 1
        elif kind == 'wanted' and b > 0: note = '  ok, viewers ask for this'
        print(f'  {k:<34} {a:8.2f} {b:8.2f}{note}')
    print('\n  Red lines (whole file, on-screen notes included):'); hits = 0
    for p, why in RED_LINES:
        for m in re.finditer(p, full, re.I):
            hits += 1; s = full[max(0, m.start() - 40):m.end() + 40].replace('\n', ' '); print(f'    !! {why}\n       ...{s}...')
    if not hits: print('    none')
    for k in ('budget / not about cost', 'you may already own it'):
        if rate(text, PROBES[k][1]) == 0: print(f'  tip: nothing for "{k}" - viewers reward it (budget comments, "use what you have").'); bad += 1
    print(f'\n  VERDICT: {"FITS THE CHANNEL" if bad + hits == 0 else f"{bad + hits} thing(s) to fix before this goes out"}')

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(1)
    cmd = a[0]
    if cmd == 'build': build(a[1] if len(a) > 1 else None, a[2] if len(a) > 2 else None)
    elif cmd == 'profile': profile()
    elif cmd == 'idea': idea(a[1:])
    elif cmd == 'check':
        ex = [a[a.index('--expect') + 1]] if '--expect' in a else []; check(a[1], ex)
    else: print(__doc__)
