# Build the screened dataset: every video with its channel median, multiple (views / channel median of latest <=60 long uploads),
# approximate date, age, views/day (lifetime average) and topic tags. Long-form (>=3 min) only; Shorts are counted separately.
import json, glob, re, statistics as st, datetime as dt, os
TODAY = dt.date(2026, 10, 20)
ch = {}
for f in glob.glob('track/ch/*.json') + glob.glob('xch/*.json'):
    try: d = json.load(open(f))
    except Exception: continue
    cid = os.path.basename(f)[:-5]
    vids = []
    for e in d.get('entries') or []:
        if not e or e.get('view_count') is None: continue
        ts = e.get('timestamp'); date = dt.datetime.fromtimestamp(ts, dt.UTC).date() if ts else None
        vids.append(dict(id=e['id'], title=e.get('title') or '', views=e['view_count'], duration=e.get('duration') or 0, date=date))
    long = [v for v in vids if v['duration'] >= 180]
    ch[cid] = dict(name=d.get('channel') or d.get('uploader') or cid, subs=d.get('channel_follower_count'), tracked=f.startswith('track'),
                   median=st.median(v['views'] for v in long) if len(long) >= 4 else None, n_long=len(long), vids=long)
sw = json.load(open('sweep.json'))
V = {}
for cid, c in ch.items():
    for v in c['vids']:
        V[v['id']] = dict(v, channel=c['name'], channel_id=cid, src='channel list')
nshort = 0
for k, b in sw.items():
    for r in b['rows']:
        if (r.get('duration') or 0) < 180:
            nshort += (r.get('duration') or 0) > 0; continue
        x = V.setdefault(r['id'], dict(id=r['id'], title=r.get('title') or '', views=r.get('views'), duration=r.get('duration'), date=None, channel=r.get('channel'), channel_id=r.get('channel_id'), src='search'))
        x.setdefault('queries', []).append(k)
        if b['mode'] == 'year': x['within_year'] = True
OFF = re.compile(r"\bmen'?s\b|for men|\bmale\b|masculine|\bguys?\b|gentleman|\bboyfriend|mukbang|recipe|workout|minecraft|fortnite|\bnfl\b|crypto|stock market", re.I)
T = {
 'never wear / stop wearing': r"never wear|stop wearing|avoid wearing|don.?t wear|not to wear|wouldn.?t be caught|never buy|stop buying|should stop wearing|should never wear",
 'what to wear instead': r"wear(ing)? instead|what to wear instead|\binstead\b",
 'mistakes / cheapen / look cheap': r"mistake|cheapen|look(s|ing)? cheap|\btacky\b|unflattering|ruin(ing|s)? your|aging you|ageing you|make(s)? you look older|look frumpy|frumpy",
 'look expensive / rich / classy': r"look(s|ing)? (more |so |instantly |always )?(expensive|rich|wealthy|luxurious|high.?end|classy|elegant|chic|sophisticated)|expensive.?looking",
 'old money / quiet luxury': r"old money|quiet luxury|stealth wealth|understated",
 'capsule / essentials / basics': r"capsule|essentials|staples|\bbasics\b|must.?haves?|wardrobe pieces|investment pieces",
 'colour combos / colours': r"colou?r combo|colou?r combination|\bcolou?rs\b|colou?r palette|neutrals",
 'colour analysis / season': r"colou?r analysis|undertone|colou?r season|seasonal colou?r|deep winter|soft summer|true autumn|soft autumn",
 'body shape / proportions': r"body (shape|type)|proportion|petite|\btall women|curvy|plus.?size|apple shape|\bpear\b|hourglass|look (taller|slimmer|thinner)|tummy|\bbelly\b",
 'look younger / age well': r"younger|anti.?ag(e|ing)|age (well|gracefully)|aging gracefully|ageless|with age|beautiful (at|after) (40|50|60|70)",
 'over 40/50/60/70 audience': r"over (40|50|60|70)|\b(40|50|60|70)s?\+|after (40|50|60|70)|in your (40|50|60|70)s|at (5|6|7)\d\b|mature women|older women|women of a certain age",
 'hair': r"\bhair|haircut|hairstyle|\bbob\b|updo|\bbun\b|ponytail|\bbangs\b|pixie",
 'makeup': r"make.?up|lipstick|\bblush\b|mascara|eyeliner|concealer|\bbrows?\b",
 'skin / skincare': r"\bskin\b|skincare|wrinkle|retinol|sunscreen|facial|\bglowing skin",
 'nails / hands': r"\bnails?\b|manicure|pedicure|\bhands\b",
 'scent / perfume': r"perfume|fragrance|\bscent|smell (good|amazing|expensive|rich)",
 'jewellery': r"jewel|earring|necklace|pearls?\b|\brings?\b|bracelet|\bgold\b|\bwatch(es)?\b",
 'bags': r"\bbags?\b|handbag|purse|\btote\b",
 'shoes': r"\bshoes\b|\bheels\b|\bboots\b|loafers|\bflats\b|sneakers|sandals|ballet flats",
 'coats / outerwear': r"\bcoats?\b|outerwear|trench|blazer|jacket",
 'seasonal (fall/winter/spring/summer/holiday)': r"\b(fall|autumn|winter|spring|summer|holiday|christmas|new year)\b",
 'trends / in & out / outdated': r"trend|in (and|&) out|outdated|\bdated\b|out of style|old.?fashioned",
 'French / Parisian / Italian / European': r"french|paris|parisian|italian|europe|british|scandinavian|spanish|\bswiss\b",
 'icons / royals / celebrities': r"audrey|grace kelly|jackie|kennedy|bessette|princess|kate middleton|diana|royal|queen|duchess|meghan|sophia loren|celebrit|actress|hollywood|bellucci|aniston|grece ghanem|helen mirren",
 'habits / routines': r"habit|routine|ritual|\bdaily\b",
 'signs / traits': r"\bsigns?\b|traits|qualities|red flags",
 'etiquette / manners': r"etiquette|manners|\btable\b|\bdinner\b|\bguests?\b|\bhost(ing|ess)?\b|\bpolite|\brude\b|faux pas|\bgrace\b",
 'speech / voice / conversation': r"\bspeak|\bvoice\b|conversation|\btalk|\bsay\b|phrases|\bwords\b|small talk|texting",
 'body language / posture / walk': r"body language|posture|\bwalk|\bsit\b|sitting|\bstand\b|\bpose\b|posing|gestures|hip sway",
 'magnetic / attractive / aura': r"magnetic|attractive|\baura\b|charisma|charming|captivating|irresistible|unforgettable|mysterious",
 'confidence / respect / presence': r"confiden|presence|respect|intimidat|command|unbothered",
 'feminine / femininity': r"feminin|ladylike|lady.?like|soft girl|womanly",
 'high value / dating': r"high.?value|dating|relationship|husband|marry|marriage",
 'transformation / makeover / glow-up': r"transform|makeover|before (and|&) after|glow.?up|level up",
 'visual comparison (vs / this or that)': r"\bvs\.?\b|versus|before (and|&) after|this or that|same outfit|\bor\b.{0,20}\?",
 'polished / put together': r"put.?together|polished|pulled together|effortless",
 'home / lifestyle / hosting': r"\bhome\b|\bhouse\b|hosting|entertain|decor|kitchen|bedroom",
 'travel': r"travel|airport|vacation|packing|suitcase",
 'workwear': r"\bwork\b|office|workwear|interview|business casual|corporate",
 'denim / jeans': r"\bjeans\b|denim",
 'fabric / quality': r"fabric|quality|cashmere|\bwool\b|\bsilk\b|\blinen\b|cotton",
 'budget / shopping / dupes': r"budget|afford|thrift|\bzara\b|h&m|uniqlo|\bcos\b|amazon|\bsale\b|\bhaul\b|\bdupes?\b|worth (it|buying)",
 'luxury brands': r"chanel|herm[eè]s|dior|louis vuitton|gucci|prada|cartier|birkin|rolex|loro piana|the row",
}
T = {k: re.compile(v, re.I) for k, v in T.items()}
rows = []
for v in V.values():
    if OFF.search(v['title']): continue
    c = ch.get(v.get('channel_id'))
    med = c['median'] if c else None
    d = v.get('date'); age = (TODAY - d).days if d else None
    rows.append(dict(id=v['id'], url='https://youtu.be/' + v['id'], title=v['title'], channel=v['channel'], channel_id=v.get('channel_id'),
                     subs=c['subs'] if c else None, channel_median=med, views=v['views'], duration=v['duration'],
                     date=d.isoformat() if d else None, date_precision='approximate (month)' if d else None, age_days=age,
                     within_year=v.get('within_year', bool(age is not None and age <= 365)),
                     views_per_day_lifetime=round(v['views'] / max(age, 1)) if (age and v['views']) else None,
                     multiple=round(v['views'] / med, 2) if (med and v['views'] is not None) else None,
                     subs_ratio=round(v['views'] / c['subs'], 2) if (c and c['subs'] and v['views'] is not None) else None,
                     topics=[k for k, rx in T.items() if rx.search(v['title'])], src=v['src'], queries=v.get('queries', [])))
json.dump(dict(built=TODAY.isoformat(), n_channels_listed=len(ch), n_channels_with_median=sum(1 for c in ch.values() if c['median']),
               n_shorts_in_search=nshort, rows=rows,
               channels={k: dict(name=c['name'], subs=c['subs'], median=c['median'], n_long=c['n_long'], tracked=c['tracked']) for k, c in ch.items()}),
          open('dataset.json', 'w'), ensure_ascii=False)
print(len(rows), 'long-form videos;', sum(r['multiple'] is not None for r in rows), 'with a multiple;', len(ch), 'channels listed;', sum(1 for c in ch.values() if c['median']), 'with median;', nshort, 'shorts seen in search')
