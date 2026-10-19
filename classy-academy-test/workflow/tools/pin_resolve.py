# find the public numeric pin id of each used pin: walk the uploader's board (or all their pins) and match the image signature
#   python3 -I pin_resolve.py <workdir> <out.json> A13_p0.mp4 ...   (needs <workdir>/raw/meta_pin.json, gap/*.json, credits/pin_full.json)
import json, sys, time, glob, os, urllib.request, urllib.parse
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
H = {"User-Agent": UA, "X-Requested-With": "XMLHttpRequest", "Accept": "application/json"}
def get(res, opts, src, handler):
    u = f"https://www.pinterest.com/resource/{res}/get/?" + urllib.parse.urlencode({"source_url": src, "data": json.dumps({"options": opts, "context": {}})})
    r = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={**H, "X-Pinterest-PWS-Handler": handler}), timeout=40).read())["resource_response"]
    return r.get("data") or [], (r.get("bookmark") or None)
def walk(kind, key, src, sig, maxpages=60):
    bm = None
    for n in range(maxpages):
        if kind == 'board':
            opts = {"board_id": key, "board_url": src, "page_size": 250, "field_set_key": "grid_item"}
            res, handler = "BoardFeedResource", "www/[username]/[slug].js"
        else:
            opts = {"username": key, "page_size": 250, "field_set_key": "grid_item"}
            res, handler = "UserPinsResource", "www/[username].js"
        if bm: opts["bookmarks"] = [bm]
        data, bm = get(res, opts, src, handler)
        for x in data:
            if isinstance(x, dict) and x.get('image_signature') == sig and str(x.get('id', '')).isdigit(): return x.get('id'), n
        if not bm or bm == '-end-' or not data: return None, n
        time.sleep(1)
    return None, maxpages
wd, out = sys.argv[1], sys.argv[2]
pins = json.load(open(f'{wd}/raw/meta_pin.json')); full = json.load(open(f'{wd}/credits/pin_full.json'))
sigs = {}
for f in glob.glob(f'{wd}/gap/*.json'):
    for c in json.load(open(f)):
        if isinstance(c, dict) and 'pin_id' in c: sigs[c['pin_id']] = os.path.basename(c['thumb']).rsplit('.', 1)[0]
res = json.load(open(out)) if os.path.exists(out) else {}
for f in sys.argv[3:]:
    if res.get(f, {}).get('id'): continue
    pid = pins[f]['pin'].rstrip('/').rsplit('/', 1)[1]; sig = sigs.get(pid); who = pins[f]['pinner']
    r = {'e1': pid, 'sig': sig, 'pinner': who}
    try:
        b = (full.get(f) or {}).get('board')
        if b:
            r['id'], r['pages'] = walk('board', b['id'], b['url'], sig); r['via'] = 'board ' + b['url']
        if not r.get('id'):
            r['id'], r['pages'] = walk('user', who, f'/{who}/', sig); r['via'] = f'all pins of {who}'
    except Exception as e: r['err'] = str(e)[:200]
    if r.get('id'): r['url'] = f"https://www.pinterest.com/pin/{r['id']}/"
    res[f] = r; print(f, json.dumps(r)); json.dump(res, open(out, 'w'), indent=1)
