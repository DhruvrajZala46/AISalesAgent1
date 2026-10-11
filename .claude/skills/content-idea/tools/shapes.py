#!/usr/bin/env python3
"""shapes.py - group the niche winners into video SHAPES (topic + format) and score each on three things:
  niche proof (lane videos, last 12 months, how many beat their channel 5x+, from how many channels),
  our audience (ALL of our videos with that shape, median multiple), and our comments (mentions, requests).

    python3 shapes.py OUT_DIR [comments.json]      # OUT_DIR from collect.py; run swipe.py first:
    python3 swipe.py OUT_DIR/collected.json --min 0 --json > OUT_DIR/all.json

Add or edit SHAPES below as the niche changes. A shape needs winners from SEVERAL channels to count:
one channel at 50x is that channel, five channels at 10x+ is a shape."""
import json,re,statistics,sys
W=sys.argv[1]; COM=sys.argv[2] if len(sys.argv)>2 else None
rows=json.load(open(W+'/all.json'))['outliers']; date={v['url']:v['date'] for v in json.load(open(W+'/collected.json'))}
for r in rows: r['date']=date.get(r['url'],'')
import os; dna=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','audience','dna.json')))
own=dna['videos']; com=json.load(open(COM)) if COM else []
LANE=re.compile(r"eleg|class|old money|quiet lux|expensive|chic|wardrobe|outfit|style|dress|wear|lady|ladies|feminin|polish|luxur|french|capsule|winter|fall|autumn|holiday|fashion|put together|habit|shoes|over (40|50|60)",re.I)
OFF=re.compile(r'\b(men|man|guy|masculine|hair care|skin|hygiene|shave|bra\b|makeup|discipline|mindset|neuroplastic)',re.I)
yr=[r for r in rows if r['date']>='2025-10-11' and LANE.search(r['title']) and not OFF.search(r['title'])]
SHAPES={
 'Never wear / remove from wardrobe': r'never wear|should (never|not) wear|remove from|stop wearing|avoid wearing|don.?t flatter|do not look elegant|cheapen|look(s)? cheap|outfit mistakes|fashion mistakes',
 'Habits / traits of an elegant woman': r'habits?|traits|signs (you|of)|behavio|never do|put together|polished',
 'French women / French chic': r'french|paris|parisian',
 'Look expensive / rich (any budget)': r'expensive|look rich|luxur|old money',
 'Shoes': r'shoes|heels|boots|loafers|flats|footwear',
 'Season trends / in & out': r'trend|in & out|in and out|what.?s in|lookbook',
 'Ageless style (over 40/50/60, with age)': r'over (40|50|60)|50\+|60\+|at (50|60)|with age|ageless|older|younger',
 'Essentials / pieces to own': r'essentials|capsule|pieces|should own|must own|staples',
 'Colours / colour combos': r'colou?rs?|combos?',
}
REQ=re.compile(r'(video|episode|part 2|part two)[^.]{0,40}(on|about)|please (do|make)|can you (do|make)|would love (a|to see)|next video',re.I)
res=[]
for name,p in SHAPES.items():
    rx=re.compile(p,re.I); n=[r for r in yr if rx.search(r['title'])]; big=[r for r in n if r['multiple']>=5]
    ow=[v for v in own if rx.search(v['title'])]; ment=[c for c in com if rx.search(c['text'])]; req=[c for c in ment if REQ.search(c['text'])]
    res.append(dict(name=name,n=n,big=big,ow=ow,ment=ment,req=req))
for x in sorted(res,key=lambda x:-len(x['big'])):
    n,big,ow=x['n'],x['big'],x['ow']
    print(f"\n## {x['name']}")
    print(f"   NICHE last 12 months: {len(n)} videos, median {statistics.median([r['multiple'] for r in n]) if n else 0:.1f}x, {len(big)} at 5x+ from {len(set(r['channel'] for r in big))} channels")
    for r in sorted(big,key=lambda r:-r['multiple'])[:5]: print(f"      {r['multiple']:5.1f}x {r['views']//1000:>5}k {r['date'][:7]} {r['channel'][:20]:<20} {r['title'][:72]}")
    if ow:
        ms=sorted((v['multiple'] for v in ow),reverse=True)
        print(f"   YOUR AUDIENCE: {len(ow)} videos, median {statistics.median(ms):.1f}x  [all: {', '.join(f'{m:.1f}' for m in ms)}]")
        for v in sorted(ow,key=lambda v:-v['multiple'])[:3]: print(f"      {v['multiple']:.1f}x {v['title'][:70]}")
    else: print("   YOUR AUDIENCE: no videos yet")
    print(f"   YOUR COMMENTS: {len(x['ment'])} mention it ({sum(c['likes'] for c in x['ment'])} likes); {len(x['req'])} request a video on it")
