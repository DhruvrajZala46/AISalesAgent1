# usage (in the work folder): python3 phsearch.py queries.txt   (lines tag=search words)
# Pinterest PHOTO search for product shots / stills (drops AI sizes, AI words, videos, tiny images); writes ph/<tag>.json + ph/sheet_<tag>.jpg
import json, sys, os, re, time, urllib.request, urllib.parse
from PIL import Image, ImageDraw
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
O = 'ph'
AI_SIZES = {(1024, 1536), (1536, 1024), (896, 1152), (832, 1216), (1024, 1024), (1152, 896), (768, 1344), (1344, 768), (1023, 1537), (1024, 1792), (1792, 1024), (928, 1232), (864, 1184)}
AI_WORDS = re.compile(r'\bai\b|aigenerated|ai[- ]generated|ai art|midjourney|dall-?e|stable diffusion|photorealistic|generated|leonardo|firefly|sora|gemini|chatgpt|prompt|render', re.I)
def get(u, h={}): return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA, **h}), timeout=30).read()
lines = [l.strip() for l in open(sys.argv[1]) if '=' in l]
for line in lines:
    tag, q = line.split('=', 1)
    try:
        d = {"options": {"query": q, "scope": "pins", "page_size": 50}, "context": {}}
        url = "https://www.pinterest.com/resource/BaseSearchResource/get/?" + urllib.parse.urlencode({"source_url": f"/search/pins/?q={q}", "data": json.dumps(d)})
        res = json.loads(get(url, {"X-Pinterest-PWS-Handler": "www/search/[scope].js"}))["resource_response"]["data"]["results"]
    except Exception as e: print(tag, 'ERR', e, flush=True); time.sleep(5); continue
    pins = []
    for p in res:
        im = (p.get('images') or {}).get('orig') or {}; w, h = im.get('width') or 0, im.get('height') or 0
        txt = ' '.join(str(p.get(k) or '') for k in ('description', 'grid_title', 'title', 'auto_alt_text'))
        if p.get('videos') or p.get('story_pin_data'): continue
        if (w, h) in AI_SIZES or AI_WORDS.search(txt) or h < 700 or w < 450: continue
        pid = str(p.get('id')); nc = p.get('native_creator') or {}; pn = p.get('pinner') or {}
        t = ((p.get('images') or {}).get('474x') or {}).get('url')
        if not t: continue
        pins.append(dict(id=pid, url=f'https://www.pinterest.com/pin/{pid}/', orig=im['url'], thumb=t, w=w, h=h, link=p.get('link') or '',
                         domain=p.get('domain') or '', creator=nc.get('full_name') or pn.get('full_name') or '', user=nc.get('username') or pn.get('username') or '', text=txt[:200]))
    json.dump(pins, open(f'{O}/{tag}.json', 'w'), indent=0)
    W, H = 200, 260; cols = 8; rows = max(1, (len(pins) + cols - 1) // cols)
    sh = Image.new('RGB', (W * cols, (H + 16) * rows), 'white'); dr = ImageDraw.Draw(sh)
    for k, p in enumerate(pins):
        try:
            b = get(p['thumb']); f = f'{O}/{tag}_{k}.jpg'; open(f, 'wb').write(b)
            im = Image.open(f).convert('RGB'); im.thumbnail((W, H))
        except Exception: continue
        x, y = (k % cols) * W, (k // cols) * (H + 16); sh.paste(im, (x + (W - im.width) // 2, y + 16)); dr.text((x + 3, y + 2), f'{tag} {k} {p["domain"][:18]}', fill='black')
    sh.save(f'{O}/sheet_{tag}.jpg', quality=75); print(tag, len(pins), flush=True); time.sleep(2)
print('PHDONE', flush=True)
