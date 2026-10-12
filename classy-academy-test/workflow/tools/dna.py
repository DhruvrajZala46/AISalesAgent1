"""dna.py - does this script TEACH the way The Classy Elegance teaches?

Measured from the channel's own transcripts (.claude/skills/content-idea/audience/transcripts).
The French script (Oct 2026) failed this the first time: it reported what other people say
("Ines says...", "one French woman shared...") and listed items, while the channel teaches from
its own voice: elegant women do this -> here is WHY it changes how you look and feel -> here is
HOW you do it -> here is how it makes you feel.

    python3 dna.py script.md          # a script written in the [ON SCREEN] format (bold spoken lines)
    python3 dna.py script.txt         # plain spoken text

Two checks:
 1. Teaching voice, per 1,000 words, against the channel's wardrobe videos (25th-75th percentile).
 2. Every numbered point must carry the channel's teaching anatomy:
    validate -> why (effect on her) -> principle line -> what elegant women do -> swap -> how-to -> inner payoff.
    Hard rule per point: WHY and SWAP are always there, and at least 3 of the 4 checked steps
    (the channel's own #1 video passes this on every point).
"""
import re, sys, os, glob, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
TR = os.path.join(HERE, '..', '..', '..', '.claude', 'skills', 'content-idea', 'audience', 'transcripts')

M = {
    'you / your (talks TO her)': (r"\byou\b|\byour\b|\byou're\b|\byourself\b", re.I, 'min'),
    'why / effect on her (because, creates, makes, feels, looks)': (r"\bbecause\b|\bcreates?\b|\bmakes? (it|you|the|an|a|your)\b|\bit can\b|\bfeels?\b|\blooks?\b", re.I, 'min'),
    'inner world (confidence, intention, grace, ease, respect, polish)': (r"\bconfiden\w*|\bintention\w*|\bpresence\b|\brespect\w*|\bgrace\w*|\bease\b|\bcalm\b|\bpolish\w*", re.I, 'min'),
    'how-to steps (Try / Start / Add / Pick / Choose / Keep / Let...)': (r"(?:^|[.!?]\s+)(Try|Start|Add|Pick|Choose|Keep|Let|Take|Opt|Swap|Look for|Invest|Focus|Remember|Avoid|Think|Instead)\b", 0, 'min'),
    'quotes an outside source (says, book, explains, shared)': (r"\bsays\b|\bsaid\b|according to|\bbook\b|\bexplains\b|\bshared her\b|\bputs it\b|\bhas said\b|\bgives (one|two)", re.I, 'cap:1.5'),
    'named person': (r"\b(In[eè]s|Fressange|Marilyn|Audrey|Hepburn|Grace Kelly|Kate|Jackie|Diana|Coco|Birkin|Meghan|Victoria)\b", 0, 'cap:2.5'),
    'reporting a culture (Paris, French, France)': (r"\bparis\b|\bfrench\b|\bfrance\b|\bparisian\b|\bitalian\b|\bitaly\b", re.I, 'cap:4'),
    'named pieces / colours / materials': (r"\b(blazer|loafers?|ballet flats?|trousers|jeans|knit|cashmere|linen|silk|wool|leather|beige|ivory|navy|camel|cream|chocolate|tote|scarf|hoops|studs|watch|belt|midi|trench|coat|shirt|blouse|sage|rose)\b", re.I, 'max'),
}
ANATOMY = [
    # "it's not you / your body, it's the detail" = absolution, the most-liked framing in the Oct 2026 study (9,900 + 5,700 likes)
    ('validate', r"\bwe get it\b|\bwe'?ve all (been there|had)\b|can (absolutely|feel|be)\b|\bis great\b|\bare wonderful\b|\bit'?s (easy|tempting|normal)\b|\bthere'?s nothing wrong\b|\bbeautiful\b|\blovely\b|\bit'?s not (you|your)\b|\bif you love\b"),
    ('why (effect on her)', r"\bbecause\b|\bcreates?\b|\bmakes? (it|you|the|an|a|your)\b|\bit can\b|\btakes? away\b|\bshift\w*\b|\bdraws?\b|\boverwhelm\w*\b|\bcompete\b|\blooks? (less|more|cheap|rushed|messy|tired)\b|\bfeel\w*\b"),
    ('swap or how-to', r"\binstead\b|\btry\b|\bswap\b|\bopt for\b|\breach for\b|\bchoose\b|\bpick\b|\bstart with\b|\badd an?\b|\bstick to\b|\blook for\b|\bgo for\b|\baim for\b|\bkeep (it|them|your)\b|\blet (one|it|your)\b|\btake (one|a)\b|\bbefore (heading|you)\b"),
    ('inner payoff', r"\bconfiden\w*|\bintention\w*|\bpresence\b|\brespect\w*|\bgrace\w*|\bease\b|\bcalm\b|\bpolish\w*|\byourself\b"),
]
WORDNUM = 'one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve'

def spoken(path):
    t = open(path, encoding='utf-8').read()
    if path.endswith('.md'):
        t = re.split(r'^#+\s*(How the channel|Proof|Final check|Sources)', t, flags=re.M)[0]
        return ' '.join(re.findall(r'^\*\*(.+?)\*\*\s*$', t, re.M))
    return re.sub(r'^#.*\n', '', t, flags=re.M)

def rates(txt):
    w = max(1, len(txt.split()))
    return {k: len(re.findall(p, txt, fl)) / w * 1000 for k, (p, fl, _) in M.items()}

def baseline():
    vids = []
    ward = re.compile(r'wear|dress|look|outfit|colou?r|jeans|shoes|jewel|wardrobe|luxury|expensive|essentials|avoid', re.I)
    for f in glob.glob(os.path.join(TR, '*.txt')):
        raw = open(f, encoding='utf-8').read(); title = raw.splitlines()[0]
        if ward.search(title) and not re.search(r'hair|pose|sound', title, re.I):
            vids.append(rates(re.sub(r'^#.*\n', '', raw, flags=re.M)))
    q = lambda k, p: st.quantiles([v[k] for v in vids], n=4)[p]
    return {k: (q(k, 0), st.median(v[k] for v in vids), q(k, 2)) for k in M}, len(vids)

def points(txt):
    parts = re.split(rf'(?=\bNumber ({WORDNUM})\b)', txt)
    out = []
    for p in parts:
        m = re.match(rf'Number ({WORDNUM})\b', p)
        if m: out.append((m.group(1), p))
    return out

def main(path):
    txt = spoken(path); r = rates(txt); B, n = baseline(); fixes = []
    print(f'TEACHING DNA - {os.path.basename(path)} ({len(txt.split())} spoken words) vs {n} channel wardrobe videos\n')
    print(f"  {'per 1,000 words':66} {'channel (p25-p75)':>18} {'script':>8}")
    for k, (p, fl, rule) in M.items():
        lo, med, hi = B[k]; v = r[k]; flag = ''
        if rule == 'min' and v < lo * 0.85: flag = '  << too little: the channel does this more'
        if rule == 'max' and v > hi * 1.3: flag = '  << listing, not teaching'
        if rule.startswith('cap') and v > float(rule.split(':')[1]): flag = '  << the channel never does this'
        if flag: fixes.append(k)
        print(f'  {k:66} {lo:6.1f} - {hi:6.1f}    {v:6.1f}{flag}')
    pts = points(txt)
    print(f'\n  Teaching anatomy per point ({len(pts)} points found)')
    print('  ' + 'point'.ljust(8) + ''.join(a[:20].ljust(22) for a, _ in ANATOMY))
    for num, body in pts:
        hit = {a: bool(re.search(pat, body, re.I)) for a, pat in ANATOMY}
        print('  ' + num.ljust(8) + ''.join(('ok' if hit[a] else 'missing').ljust(22) for a, _ in ANATOMY))
        # the channel's own points always explain WHY and give a SWAP; validate / inner payoff can be skipped on one point
        need = [a for a in ('why (effect on her)', 'swap or how-to') if not hit[a]]
        if sum(hit.values()) < 3: need.append(f'only {sum(hit.values())} of 4 teaching steps')
        for a in need: fixes.append(f'point {num}: {a}')
    print('\n  VERDICT: ' + ('TEACHES LIKE THE CHANNEL' if not fixes else f'{len(fixes)} thing(s) to fix:'))
    for f in fixes: print('   - ' + f)
    return 0 if not fixes else 1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
