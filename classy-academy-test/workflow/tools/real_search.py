# Pinterest photo search that drops likely-AI images before a human looks:
#  - AI generator output sizes (1024x1536, 1536x1024, 896x1152, 832x1216, 1024x1024, 1152x896, 768x1344, 1344x768, 1080x1920 from AI video stills is NOT used)
#  - AI words in title/description/hashtags
#  - too small for a 427x720 panel (orig height < 900)
import json, sys, os, re, time, urllib.request, urllib.parse
from PIL import Image, ImageDraw
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
O = os.path.join(os.getcwd(), 'real'); os.makedirs(O, exist_ok=True)
AI_SIZES = {(1024, 1536), (1536, 1024), (896, 1152), (832, 1216), (1024, 1024), (1152, 896), (768, 1344), (1344, 768), (1023, 1537), (1024, 1792), (1792, 1024), (928, 1232), (864, 1184)}
AI_WORDS = re.compile(r'\bai\b|aigenerated|ai[- ]generated|ai art|midjourney|dall-?e|stable diffusion|photorealistic|generated|leonardo|firefly|sora|gemini|chatgpt|prompt|render', re.I)
def get(u, h={}): return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA, **h}), timeout=30).read()
def search(q, n=50):
    d = {"options": {"query": q, "scope": "pins", "page_size": n}, "context": {}}
    url = "https://www.pinterest.com/resource/BaseSearchResource/get/?" + urllib.parse.urlencode({"source_url": f"/search/pins/?q={q}", "data": json.dumps(d)})
    return json.loads(get(url, {"X-Pinterest-PWS-Handler": "www/search/[scope].js"}))["resource_response"]["data"]["results"]
keep = json.load(open(O + '/keep.json')) if os.path.exists(O + '/keep.json') else {}
for arg in sys.argv[1:]:
    tag, q = arg.split('=', 1); res = search(q); kept = 0; why = {'size': 0, 'words': 0, 'small': 0, 'video': 0}
    for p in res:
        im = (p.get('images') or {}).get('orig') or {}; w, h = im.get('width') or 0, im.get('height') or 0
        txt = ' '.join(str(p.get(k) or '') for k in ('description', 'grid_title', 'title', 'auto_alt_text'))
        if p.get('videos') or p.get('story_pin_data'): why['video'] += 1; continue
        if (w, h) in AI_SIZES: why['size'] += 1; continue
        if AI_WORDS.search(txt): why['words'] += 1; continue
        if h < 900 or w < 500: why['small'] += 1; continue
        pid = str(p.get('id')); nc = p.get('native_creator') or {}; pn = p.get('pinner') or {}
        keep[f'{tag}{kept}'] = dict(id=pid, url=f'https://www.pinterest.com/pin/{pid}/', orig=im['url'], w=w, h=h, link=p.get('link') or '',
                                    domain=p.get('domain') or '', creator=nc.get('full_name') or pn.get('full_name') or '', user=nc.get('username') or pn.get('username') or '',
                                    text=txt[:200])
        kept += 1
    print(tag, len(res), 'results -> kept', kept, 'dropped', why, flush=True); time.sleep(2)
json.dump(keep, open(O + '/keep.json', 'w'), indent=0)
# contact sheet of kept images (thumb from orig, resized)
tags = [a.split('=', 1)[0] for a in sys.argv[1:]]
ks = [k for k in keep if any(re.fullmatch(re.escape(t) + r'\d+', k) for t in tags)]
W, Hh = 200, 300; cols = 8
sh = Image.new('RGB', (cols * W, ((len(ks) + cols - 1) // cols) * (Hh + 26)), 'white'); dr = ImageDraw.Draw(sh)
for i, k in enumerate(ks):
    f = f'{O}/{k}.jpg'
    try:
        if not os.path.exists(f): open(f, 'wb').write(get(keep[k]['orig']))
        im = Image.open(f).convert('RGB'); im.thumbnail((W, Hh))
    except Exception: continue
    x, y = (i % cols) * W, (i // cols) * (Hh + 26); sh.paste(im, (x, y + 26))
    dr.text((x + 2, y + 1), f"{k} {keep[k]['w']}x{keep[k]['h']}", fill='red'); dr.text((x + 2, y + 13), (keep[k]['domain'] + ' ' + keep[k]['user'])[:30], fill='black')
sh.save(f'{O}/sheet_{"_".join(tags)}.jpg', quality=85); print('sheet', len(ks))
