# fam3.py: pool every search collected (20 Oct sweep + angle searches + dataset, 21 Oct concept/focused sweeps, 23 Oct new-family sweep)
# and count strict on-concept long videos per concept family: 1M+ and 500k+ videos, distinct channels, years.
import json, re, sys
pool = {}
def add(r, year=None, src=''):
    if not r.get('id') or not r.get('views'): return
    x = pool.setdefault(r['id'], dict(id=r['id'], title=r.get('title') or '', channel=r.get('channel'), channel_id=r.get('channel_id'), views=r['views'], duration=r.get('duration'), year_approx=year, src=set()))
    x['views'] = max(x['views'], r['views']); x['src'].add(src)
    if year and not x['year_approx']: x['year_approx'] = year
S = '/tmp/claude-0/-home-user-AISalesAgent1/73fc3aa5-807d-530d-b865-5c7bcc671679/scratchpad/'
for f in ('proven/csweep.json', 'proven/ksweep.json', 'p3/sweep3.json'):
    for b in json.load(open(S + f)).values():
        for r in b['rows']: add(r, r.get('year_approx'), f.split('/')[-1])
for b in json.load(open(S + 'deep/sweep.json')).values():
    for r in b['rows']: add(r, None, 'sweep20oct')
for v in json.load(open(S + 'deep/angle_search.json')).values():
    if v != 'ERR':
        for r in v: add(r, None, 'angle20oct')
for r in json.load(open(S + 'deep/dataset.json'))['rows']:
    add(dict(id=r['id'], title=r['title'], channel=r['channel'], channel_id=r['channel_id'], views=r['views'], duration=r['duration']), int(r['date'][:4]) if r.get('date') else None, 'dataset')
print(len(pool), 'unique videos in the pool')
MEN = re.compile(r"\bmen\b(?!.{0,15}(find|like|love|notice|want))|\bman\b|\bguys?\b|gentle(man|men)|masculine|beard|\bmale\b|for boys|\bboys?\b|\bhis\b", re.I)
JUNK = re.compile(r"minecraft|roblox|gta|fortnite|song|lyrics|playlist|movie|full episode|\bep\.? ?\d|kdrama|anime|prank|asmr|tiktok compilation|celebrit|before and after transformation|makeover show|plastic surgery", re.I)
K = {
 'K1 look older / younger (in production)': r"look(s|ing)? older|look(s|ing)? old\b|\bages? you\b|aging you|ageing you|\bage you\b|years older|instantly age|(look|dress|style|appear).{0,25}younger|years younger|youthful",
 'K2 look expensive / classy / rich (covered)': r"look(s|ing)? (more |so |always |instantly |extra )?(expensive|rich|wealthy|classy|elegant|luxurious|high.?end|sophisticated|like a million)|expensive.?looking|look like money",
 'K3 style mistakes, not age (covered: Cheapen 0.23x)': r"(fashion|style|styling|outfit|wardrobe|clothing|dressing|makeup|make-up|hair) mistakes?|mistakes? (in|with) (your )?(style|outfits?|fashion)",
 'K6 never wear / stop wearing (covered)': r"never wear|stop wearing|don.?t wear|should(n.?t| never) wear|what not to wear|not to wear",
 'N1 more attractive / prettier / glow up': r"more attractive|(look|looking|be|become|get) (more |so |extra )?(attractive|prettier|pretty|beautiful|gorgeous)\b|glow.?up|prettier|attractive (woman|women|girl|lady)|what makes (a )?(woman|women|girl) attractive|instantly attractive|naturally (pretty|beautiful|attractive)",
 'N2 unattractive (fear)': r"unattractive|less attractive|look(s|ing)? ugly|make(s)? you (look )?ugly|ruin(s|ing)? your (look|beauty|face)",
 'N3 smell good / perfume': r"smell(s|ing)? (good|amazing|expensive|great|nice|rich|luxurious|like)|perfume|fragrance|\bscent",
 'N4 look taller / slimmer': r"look(s|ing)? (taller|slimmer|thinner|leaner|skinnier|petite)|appear (taller|slimmer|thinner)|look (fat|bigger|wider|shorter|heavier)|longer legs|look \d+ ?(lbs|pounds|kg)",
 'N5 makeup (expensive / mistakes / elegant)': r"make.?up.{0,40}(mistake|expensive|elegant|classy|rich|natural|everyday|beginner|tips|secrets|look younger|older)|(mistake|expensive|elegant|classy).{0,30}make.?up",
 'N6 posture / walk / grace': r"posture|how to walk|walk (like|elegantly|gracefully|with confidence)|sit like a (lady|queen)|how to sit|graceful|gracefully",
 'N7 high value woman': r"high.?value",
 'N8 beauty secrets / tips / habits': r"beauty (secrets?|tips|hacks|habits|routine)|beautiful (women|woman|girls?) (do|habits|secrets)|habits of (beautiful|pretty|attractive)",
 'N9 always look stylish / dress better': r"look(s|ing)? (more )?stylish|always look (good|stylish|great|chic|amazing)|dress better|style tips|(be|look) (more )?fashionable|style hacks|fashion hacks|styling (tips|tricks|hacks)",
 'N10 trends in / out / outdated': r"trends? (that are|in and out|in & out|out|to stop|dying|over|ending|you should)|outdated|out of style|in and out|in & out|dated",
 'N11 old money / rich women': r"old money|rich (women|woman|girls?|ladies)|wealthy (women|woman)|(dress|look) (like )?(a )?(rich|wealthy|millionaire)|quiet luxury",
 'N12 confidence': r"confiden",
 'O1 colour analysis / colours that suit you': r"colou?r analysis|(seasonal|season) colou?r|colou?rs? (that|to) (suit|flatter|make you)|best colou?rs? for (you|your)|skin ?(tone|undertone)",
 'O2 body type / dress your shape': r"body (type|shape)|apple shape|pear shape|hourglass|inverted triangle|petite (women|girls|styling)|plus.?size styling",
 'O3 capsule / wardrobe essentials': r"capsule|minimalist wardrobe|wardrobe (essentials|staples|basics)|timeless wardrobe|pieces every woman",
 'O4 feminine / feminine energy': r"feminin",
 'O5 classy / elegant habits (covered)': r"habits?|how to be (elegant|classy|a lady|ladylike)|classy (women|woman|lady|ladies)|elegant (women|woman|lady|ladies)|things classy|signs (you|of)",
 'O6 etiquette (rejected)': r"etiquette|manners",
 'O7 hairstyles / haircuts (covered)': r"hairstyle|haircut|hair ?style|updo|\bbun\b",
}
res = {}
for k, rx in K.items():
    rxc = re.compile(rx, re.I)
    v = [r for r in pool.values() if rxc.search(r['title']) and not MEN.search(r['title']) and not JUNK.search(r['title']) and (r['duration'] or 0) >= 180]
    m1 = sorted([r for r in v if r['views'] >= 1e6], key=lambda r: -r['views']); m5 = [r for r in v if r['views'] >= 5e5]
    res[k] = dict(n=len(v), n1M=len(m1), ch1M=len({r['channel_id'] for r in m1}), n500k=len(m5), ch500k=len({r['channel_id'] for r in m5}),
                  years1M=sorted({r['year_approx'] for r in m1 if r['year_approx']}), top=[{**r, 'src': sorted(r['src'])} for r in sorted(m5, key=lambda r: -r['views'])])
print(f"{'family':52} {'n':>5} {'1M':>4} {'ch1M':>5} {'500k':>5} {'ch500k':>6}  years with 1M+")
for k, x in sorted(res.items(), key=lambda kv: -kv[1]['ch1M']):
    print(f"{k[:52]:52} {x['n']:5} {x['n1M']:4} {x['ch1M']:5} {x['n500k']:5} {x['ch500k']:6}  {x['years1M']}")
json.dump(res, open('fam3_res.json', 'w'), ensure_ascii=False, default=list)
json.dump({k: {**v, 'src': sorted(v['src'])} for k, v in pool.items()}, open('pool.json', 'w'), ensure_ascii=False)
