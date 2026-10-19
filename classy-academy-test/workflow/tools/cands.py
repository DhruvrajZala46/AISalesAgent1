# Candidate finder (discovery layer = Pinterest video pins, as in the channel's past clips).
#   python3 -I cands.py <tag> "query 1" "query 2" ...
# Writes cand/<tag>.json (every video pin: pin id, pinner, outbound link, @handles/credits in the text, thumb)
# and cand/<tag>_sheetN.jpg (numbered thumbnails with pinner and link domain) for review by eye.
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pins import search
from revsearch import fetch
from PIL import Image, ImageDraw
tag, qs = sys.argv[1], sys.argv[2:]
os.makedirs('cand/th', exist_ok=True)
out, seen = [], set()
for q in qs:
    try: res, _ = search(q)
    except Exception as e: print('ERR', q, e); continue
    for p in res:
        if not (p.get('videos') or p.get('story_pin_data')): continue
        sig = p.get('image_signature') or p['id']
        if sig in seen: continue
        seen.add(sig)
        im = p.get('images') or {}; u = (im.get('236x') or im.get('474x') or {}).get('url')
        if not u: continue
        th = f'cand/th/{sig}.jpg'
        if not os.path.exists(th) and not fetch(u, th): continue
        text = ' '.join(str(p.get(k) or '') for k in ('grid_title', 'title', 'description')).replace('\n', ' ')
        handles = sorted(set(re.findall(r'@([A-Za-z0-9_.]{3,30})', text)))
        out.append({'n': len(out), 'q': q, 'pin_id': p['id'], 'pin_url': f"https://www.pinterest.com/pin/{p['id']}/",
                    'pinner': (p.get('pinner') or {}).get('username'), 'board': ((p.get('board') or {}).get('name')),
                    'link': p.get('link'), 'created': p.get('created_at'), 'handles': handles,
                    'credit_text': bool(re.search(r'credit|cr:|via|tiktok|@', text, re.I)), 'text': text[:300], 'thumb': th})
json.dump(out, open(f'cand/{tag}.json', 'w'), indent=1, ensure_ascii=False)
W, H, C = 200, 300, 8
for s in range(0, len(out), 32):
    part = out[s:s + 32]; rows = (len(part) + C - 1) // C
    sh = Image.new('RGB', (W * C, rows * (H + 40)), 'white'); d = ImageDraw.Draw(sh)
    for k, c in enumerate(part):
        x, y = (k % C) * W, (k // C) * (H + 40)
        t = Image.open(c['thumb']).convert('RGB'); t.thumbnail((W - 4, H)); sh.paste(t, (x + 2, y + 38))
        dom = re.sub(r'https?://(www\.)?', '', c['link'] or '-')[:22]
        d.text((x + 2, y + 2), f"#{c['n']} {(c['pinner'] or '')[:20]}", fill='red'); d.text((x + 2, y + 16), dom, fill='blue')
    sh.save(f'cand/{tag}_sheet{s // 32}.jpg', quality=82)
print(tag, len(out), 'video pins;', sum(1 for c in out if c['link'] and re.search('tiktok|instagram|youtube', c['link'])), 'link to an original post')
