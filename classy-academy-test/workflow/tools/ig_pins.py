# Pinterest search that keeps ONLY photo pins linking to an Instagram post (a creator's own original) at >= 1080 px high
#   python3 -I ig_pins.py <outdir> "search words" ...   -> <outdir>/keep.json + one jpg per pin (check each author with igcheck.js)
import json, sys, os, re, time, urllib.request, urllib.parse
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
def get(u, h={}): return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA, **h}), timeout=30).read()
def search(q):
    d = {"options": {"query": q, "scope": "pins", "page_size": 50}, "context": {}}
    url = "https://www.pinterest.com/resource/BaseSearchResource/get/?" + urllib.parse.urlencode({"source_url": f"/search/pins/?q={q}", "data": json.dumps(d)})
    return json.loads(get(url, {"X-Pinterest-PWS-Handler": "www/search/[scope].js"}))["resource_response"]["data"]["results"]
O = sys.argv[1]; os.makedirs(O, exist_ok=True)
keep = json.load(open(f'{O}/keep.json')) if os.path.exists(f'{O}/keep.json') else {}
seen = {v['ig'] for v in keep.values()}
for q in sys.argv[2:]:
    try: res = search(q)
    except Exception as e: print('ERR', q, e); continue
    n = 0
    for p in res:
        link = p.get('link') or ''; m = re.match(r'https?://(www\.)?instagram\.com/(p|reel)/([A-Za-z0-9_-]+)', link)
        im = (p.get('images') or {}).get('orig') or {}
        if not m or m.group(2) != 'p' or p.get('videos') or (im.get('height') or 0) < 1080: continue
        ig = f'https://www.instagram.com/p/{m.group(3)}/'
        if ig in seen: continue
        seen.add(ig); k = f'i{len(keep)}'
        try: open(f'{O}/{k}.jpg', 'wb').write(get(im['url']))
        except Exception: continue
        keep[k] = dict(ig=ig, orig=im['url'], w=im['width'], h=im['height'], pinner=(p.get('pinner') or {}).get('username'), sig=p.get('image_signature'),
                       text=' '.join(str(p.get(x) or '') for x in ('title', 'description'))[:160].replace('\n', ' '), q=q)
        n += 1
    print(q, '->', n, flush=True); time.sleep(2)
json.dump(keep, open(f'{O}/keep.json', 'w'), indent=0)
