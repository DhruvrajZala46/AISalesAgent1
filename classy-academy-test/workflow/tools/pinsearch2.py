# pinsearch2.py - deeper Pinterest search for the owner's kind of footage (EDIT-RULES.md section 6).
# usage (inside the work folder): python3 pinsearch2.py [--pages 3] [--videos] [--landscape] [--images] tag="query" tag2="..."
#   --videos      search Pinterest's real "Videos" tab (scope=videos, the grid a person sees there), AI-generated pins filtered out
#   --pages N     follow Pinterest's bookmarks N pages deep (25-50 pins a page) instead of only the first page
#   --landscape   keep only video pins wider than tall (full-screen footage; vertical reels are never blown up)
#   --images      keep image pins too (product photos for cut-outs)
# Writes pin/<tag>.json (same fields as pin_search.py, plus vw/vh/dur of the video) and pin/sheet_<tag>.jpg.
# Pins whose video or image was already downloaded for ANY video (raw/meta.json here + pin/_seen.txt) are dropped,
# so every search brings new footage.
import json, sys, os, time, urllib.request, urllib.parse
from PIL import Image, ImageDraw
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
A = sys.argv[1:]; PAGES = 3; LAND = IMG = VID = False; Q = []
i = 0
while i < len(A):
    if A[i] == '--pages': PAGES = int(A[i + 1]); i += 2; continue
    if A[i] == '--landscape': LAND = True
    elif A[i] == '--images': IMG = True
    elif A[i] == '--videos': VID = True
    else: Q.append(A[i].split('=', 1))
    i += 1
O = os.path.join(os.getcwd(), 'pin'); os.makedirs(O, exist_ok=True)
SEEN = set()
if os.path.exists(f'{O}/_seen.txt'): SEEN |= {l.strip() for l in open(f'{O}/_seen.txt') if l.strip()}
if os.path.exists('raw/meta.json'):
    for v in json.load(open('raw/meta.json')).values():
        for k in ('video', 'pin_id'):
            if v.get(k): SEEN.add(v[k])
def get(url, headers={}):
    r = urllib.request.Request(url, headers={"User-Agent": UA, **headers}); return urllib.request.urlopen(r, timeout=30).read()
def vids(p):
    out = []
    lists = [((p.get('videos') or {}).get('video_list') or {})]
    for pg in ((p.get('story_pin_data') or {}).get('pages') or []):
        for b in pg.get('blocks', []) or []: lists.append(((b.get('video') or {}).get('video_list') or {}))
    for vl in lists:
        for k in ('V_720P', 'V_EXP7', 'V_EXP6', 'V_EXP5', 'V_HLSV4'):
            if k in vl:
                v = vl[k]; out.append(dict(url=v['url'], w=v.get('width'), h=v.get('height'), dur=(v.get('duration') or 0) / 1000)); break
    return out
for tag, q in Q:
    pins, bm, seen_ids = [], None, set()
    for page in range(PAGES):
        opt = {"query": q, "scope": "videos" if VID else "pins", "page_size": 25 if VID else 50, "filter_genai": True}
        if bm: opt["bookmarks"] = [bm]
        d = {"options": opt, "context": {}}
        url = "https://www.pinterest.com/resource/BaseSearchResource/get/?" + urllib.parse.urlencode({"source_url": f"/search/{'videos' if VID else 'pins'}/?q={q}", "data": json.dumps(d)})
        try: rr = json.loads(get(url, {"X-Pinterest-PWS-Handler": "www/search/[scope].js"}))["resource_response"]
        except Exception as e: print(tag, 'page', page, 'failed', e); break
        res = (rr.get("data") or {}).get("results") or []
        for p in res:
            pid = str(p.get('id') or '')
            if not pid or pid in seen_ids: continue
            seen_ids.add(pid)
            im = (p.get('images') or {}); thumb = (im.get('474x') or im.get('236x') or {}).get('url'); orig = (im.get('orig') or {}).get('url')
            if not thumb: continue
            vv = vids(p)
            if not vv and not IMG: continue
            if vv and LAND and not ((vv[0]['w'] or 0) > (vv[0]['h'] or 1)): continue
            if (vv and vv[0]['url'] in SEEN) or pid in SEEN or (not vv and orig in SEEN): continue
            pn = (p.get('pinner') or {}); nc = (p.get('native_creator') or {})
            pins.append(dict(id=pid, url=(f'https://www.pinterest.com/pin/{pid}/' if pid.isdigit() else ''),
                             creator=(nc.get('full_name') or nc.get('username') or pn.get('full_name') or pn.get('username') or ''),
                             creator_user=(nc.get('username') or pn.get('username') or ''), src_link=p.get('link') or '',
                             orig=orig, thumb=thumb, videos=[v['url'] for v in vv], title=(p.get('grid_title') or p.get('title') or '')[:80],
                             vw=vv[0]['w'] if vv else None, vh=vv[0]['h'] if vv else None, dur=round(vv[0]['dur'], 1) if vv else None,
                             w=(im.get('orig') or {}).get('width'), h=(im.get('orig') or {}).get('height')))
        bm = rr.get('bookmark')
        if not bm or bm == '-end-': break
        time.sleep(1.5)
    json.dump(pins, open(f"{O}/{tag}.json", "w"), indent=0)
    W, H = 200, 300; cols = 10; rows = max(1, (len(pins) + cols - 1) // cols)
    sh = Image.new('RGB', (W * cols, (H + 18) * rows), 'white'); dr = ImageDraw.Draw(sh)
    for k, p in enumerate(pins):
        f = f"{O}/{tag}_{k}.jpg"
        try:
            open(f, 'wb').write(get(p['thumb'])); im = Image.open(f).convert('RGB')
            sc = min(W / im.width, H / im.height); im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))))
        except Exception: continue
        x, y = (k % cols) * W, (k // cols) * (H + 18); sh.paste(im, (x + (W - im.width) // 2, y + 18))
        lab = f"{tag}{k}" + (f" {p['vw']}x{p['vh']} {p['dur']}s" if p['videos'] else " IMG")
        dr.text((x + 3, y + 3), lab, fill='red' if p['videos'] else 'blue')
    sh.save(f"{O}/sheet_{tag}.jpg", quality=80)
    print(tag, len(pins), 'new pins', sum(1 for p in pins if p['videos']), 'video', flush=True)
    time.sleep(2)
