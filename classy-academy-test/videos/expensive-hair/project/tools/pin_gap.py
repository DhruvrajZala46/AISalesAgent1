# pin_gap.py - Pinterest video-pin search for the shots that still need a clip (the channel's own route: video pins)
#   python3 -I pin_gap.py A09="frizzy dry hair ends video|damaged hair back view video" A43w="..."  [--images]
# -> gap/<asset>.json (every pin with its video url, pinner, link, credit text) + gap/<asset>_sheet.jpg (numbered)
import sys, os, json, re, time, urllib.request, urllib.parse
from PIL import Image, ImageDraw
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
IMAGES = '--images' in sys.argv
def get(u, h={}): return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA, **h}), timeout=40).read()
def search(q):
    d = {"options": {"query": q, "scope": "pins", "page_size": 50}, "context": {}}
    u = "https://www.pinterest.com/resource/BaseSearchResource/get/?" + urllib.parse.urlencode({"source_url": f"/search/pins/?q={q}", "data": json.dumps(d)})
    return json.loads(get(u, {"X-Pinterest-PWS-Handler": "www/search/[scope].js"}))["resource_response"]["data"]["results"]
def video_url(p):
    vl = (p.get('videos') or {}).get('video_list') or {}
    for k in ('V_720P', 'V_EXP7', 'V_EXP6', 'V_EXP5', 'V_HLSV4'):
        if k in vl: return vl[k]['url'], vl[k].get('width'), vl[k].get('height'), vl[k].get('duration')
    for pg in ((p.get('story_pin_data') or {}).get('pages') or []):
        for b in pg.get('blocks') or []:
            v = (b.get('video') or {}).get('video_list') or {}
            for k in ('V_EXP7', 'V_720P', 'V_EXP6', 'V_EXP5', 'V_HLSV4'):
                if k in v: return v[k]['url'], v[k].get('width'), v[k].get('height'), v[k].get('duration')
    return None
os.makedirs('gap/th', exist_ok=True)
for arg in [a for a in sys.argv[1:] if '=' in a]:
    aid, qs = arg.split('=', 1); out, seen = [], set()
    for q in qs.split('|'):
        try: res = search(q)
        except Exception as e: print('ERR', q, e); continue
        for p in res:
            vu = video_url(p)
            if not IMAGES and not vu: continue
            sig = p.get('image_signature') or p['id']
            if sig in seen: continue
            seen.add(sig)
            im = p.get('images') or {}; th = (im.get('236x') or {}).get('url'); orig = (im.get('orig') or {})
            if not th: continue
            f = f'gap/th/{sig}.jpg'
            if not os.path.exists(f):
                try: open(f, 'wb').write(get(th))
                except Exception: continue
            text = ' '.join(str(p.get(k) or '') for k in ('grid_title', 'title', 'description')).replace('\n', ' ')
            out.append(dict(n=len(out), q=q, pin_id=p['id'], pinner=(p.get('pinner') or {}).get('username'), link=p.get('link'),
                            video=vu[0] if vu else None, vw=vu[1] if vu else orig.get('width'), vh=vu[2] if vu else orig.get('height'),
                            vdur=round(vu[3] / 1000, 1) if vu and vu[3] else None, image=orig.get('url'),
                            handles=sorted(set(re.findall(r'@([A-Za-z0-9_.]{3,30})', text))), text=text[:240], thumb=f))
        time.sleep(2)
    json.dump(out, open(f'gap/{aid}.json', 'w'), indent=0)
    C, TW, TH = 8, 200, 300; rows = (len(out) + C - 1) // C
    sh = Image.new('RGB', (C * TW, max(1, rows) * (TH + 30)), 'white'); dr = ImageDraw.Draw(sh)
    for k, c in enumerate(out):
        x, y = (k % C) * TW, (k // C) * (TH + 30)
        t = Image.open(c['thumb']).convert('RGB'); t.thumbnail((TW - 4, TH)); sh.paste(t, (x + 2, y + 28))
        dr.text((x + 2, y + 2), f"#{k} {(c['pinner'] or '')[:18]}", fill='red')
        dr.text((x + 2, y + 15), f"{c['vw']}x{c['vh']} {c['vdur'] or ''}s", fill='blue')
    sh.save(f'gap/{aid}_sheet.jpg', quality=80)
    print(aid, len(out), 'pins')
