#!/usr/bin/env python3
"""rank.py - rank collected.json with yt-viral's multiple-over-own-median, then cut it the way that found
the winter video and the 'Winter 2026 Trends' idea.

    python3 rank.py OUT_DIR [--today 2026-10-11] [--own "Classy Academy,TheClassyElegance"]

Prints four tables and writes OUT_DIR/ranked.json + OUT_DIR/outlier_thumbs.jpg:
  A. RIGHT NOW  - our lane, published in the last 6 months, >= 2x
  B. SEASON     - our lane, published in the same 3-month window LAST year (what this season rewards)
  C. OUR AUDIENCE - the user's own channel(s), all videos by multiple
  D. ALL-TIME   - our lane, >= 10x, any date (evergreen formats)
"""
import json, os, re, sys, subprocess, datetime, urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
SWIPE = os.path.join(HERE, '..', '..', 'yt-viral', 'swipe.py')
out_dir = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else '.'
arg = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
today = datetime.date.fromisoformat(arg('--today', datetime.date.today().isoformat()))
own = [s.strip().lower() for s in arg('--own', 'Classy Academy,TheClassyElegance,The Classy Elegance').split(',')]

coll = os.path.join(out_dir, 'collected.json')
r = subprocess.run([sys.executable, '-I', SWIPE, coll, '--min', '0', '--json'], capture_output=True, text=True, check=True)
rows = json.loads(r.stdout)['outliers']
date = {v['url']: v.get('date', '') for v in json.load(open(coll))}
for x in rows: x['date'] = date.get(x['url'], '')

# our lane: elegance / classy / style / fashion for women (keep beauty-only and mindset-only out)
LANE = re.compile(r"eleg|class|old money|quiet lux|expensive|chic|wardrobe|outfit|style|dress|wear|lady|ladies|feminin|"
                  r"polish|luxur|rich|french|capsule|winter|fall|autumn|spring|summer|holiday|christmas|fashion|"
                  r"put together|look (better|good|older|younger|cheap)", re.I)
lane = [x for x in rows if LANE.search(x['title'] or '')]
iso = lambda d: d.isoformat()
six_ago = today - datetime.timedelta(days=183)
s0 = today.replace(year=today.year - 1) - datetime.timedelta(days=10)
s1 = s0 + datetime.timedelta(days=100)

def show(name, xs, n):
    print(f'\n== {name}')
    for x in xs[:n]:
        print(f"  {x['multiple']:6.1f}x {x['views']//1000:>6}k {x['date']} {x['channel'][:20]:<20} {x['title'][:72]}  [{x['formula']}]")
    return xs[:n]

A = show(f'A. RIGHT NOW (lane, since {iso(six_ago)}, >=2x)',
         sorted([x for x in lane if x['date'] >= iso(six_ago) and x['multiple'] >= 2], key=lambda x: -x['multiple']), 20)
B = show(f'B. SEASON (lane, {iso(s0)}..{iso(s1)}, >=2x)',
         sorted([x for x in lane if iso(s0) <= x['date'] <= iso(s1) and x['multiple'] >= 2], key=lambda x: -x['multiple']), 20)
C = show('C. OUR AUDIENCE (own channel)',
         sorted([x for x in rows if any(o in x['channel'].lower() for o in own)], key=lambda x: -x['multiple']), 15)
D = show('D. ALL-TIME EVERGREEN (lane, >=10x)', sorted([x for x in lane if x['multiple'] >= 10], key=lambda x: -x['multiple']), 15)
json.dump(dict(A=A, B=B, C=C, D=D, today=iso(today)), open(os.path.join(out_dir, 'ranked.json'), 'w'), indent=1)

# thumbnail sheet of A+B so the winners can be SEEN, not just read
try:
    from PIL import Image, ImageDraw
    pick = (A + B)[:24]; os.makedirs(os.path.join(out_dir, 'thumbs'), exist_ok=True)
    def get(x):
        vid = x['url'].rsplit('/', 1)[-1]; f = os.path.join(out_dir, 'thumbs', vid + '.jpg')
        if not os.path.exists(f):
            for q in ('maxresdefault', 'hqdefault'):
                try: open(f, 'wb').write(urllib.request.urlopen(f'https://i.ytimg.com/vi/{vid}/{q}.jpg', timeout=20).read()); break
                except Exception: pass
        return f
    with ThreadPoolExecutor(8) as ex: files = list(ex.map(get, pick))
    W, H, C_ = 400, 225, 4; sh = Image.new('RGB', (C_ * W, ((len(pick) + 3) // 4) * (H + 30)), 'white'); d = ImageDraw.Draw(sh)
    for k, (x, f) in enumerate(zip(pick, files)):
        X, Y = (k % C_) * W, (k // C_) * (H + 30)
        try: sh.paste(Image.open(f).convert('RGB').resize((W, H)), (X, Y + 30))
        except Exception: pass
        d.text((X + 2, Y + 2), f"x{x['multiple']:.0f} {x['views']//1000}k {x['channel'][:24]}", fill='red'); d.text((X + 2, Y + 15), x['title'][:62], fill='black')
    sh.save(os.path.join(out_dir, 'outlier_thumbs.jpg'), quality=85); print('\nthumbnail sheet:', os.path.join(out_dir, 'outlier_thumbs.jpg'))
except Exception as e:
    print('thumbnail sheet skipped:', e)
