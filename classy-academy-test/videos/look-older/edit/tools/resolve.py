# resolve.py ID [ID ...] : finds the public numeric Pinterest pin id of each pick (search results only give an 'e1_...' token,
# whose link sends a browser to Pinterest's Explore page). Walks the pin's board (else the uploader's pins) and matches the image
# signature; writes pin_url = https://www.pinterest.com/pin/<id>/ into picks/<ID>.json.
import json, sys, time, os, urllib.request, urllib.parse
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
H = {"User-Agent": UA, "X-Requested-With": "XMLHttpRequest", "Accept": "application/json"}
def get(res, opts, src, handler):
    u = f"https://www.pinterest.com/resource/{res}/get/?" + urllib.parse.urlencode({"source_url": src, "data": json.dumps({"options": opts, "context": {}})})
    r = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={**H, "X-Pinterest-PWS-Handler": handler}), timeout=40).read())["resource_response"]
    return r.get("data") or [], (r.get("bookmark") or None)
def walk(kind, key, src, sig, maxpages=20):
    bm = None
    for n in range(maxpages):
        if kind == 'board': opts, res, hd = {"board_id": key, "board_url": src, "page_size": 250, "field_set_key": "grid_item"}, "BoardFeedResource", "www/[username]/[slug].js"
        else: opts, res, hd = {"username": key, "page_size": 250, "field_set_key": "grid_item"}, "UserPinsResource", "www/[username].js"
        if bm: opts["bookmarks"] = [bm]
        data, bm = get(res, opts, src, hd)
        for x in data:
            if isinstance(x, dict) and x.get('image_signature') == sig and str(x.get('id', '')).isdigit(): return str(x['id'])
        if not bm or bm == '-end-' or not data: return None
        time.sleep(1.2)
    return None
for aid in sys.argv[1:]:
    f = f'{L}/picks/{aid}.json'; p = json.load(open(f))
    if str(p.get('pin_id', '')).isdigit(): p['pin_url'] = f"https://www.pinterest.com/pin/{p['pin_id']}/"; json.dump(p, open(f, 'w'), indent=1); print(aid, 'numeric already'); continue
    found = None
    try:
        if p.get('board_id') and p.get('board'): found = walk('board', p['board_id'], p['board'], p['sig'])
        if not found and p.get('pinner'): found = walk('user', p['pinner'], f"/{p['pinner']}/", p['sig'])
    except Exception as e: print(aid, 'error', e)
    if found: p['pin_url'] = f'https://www.pinterest.com/pin/{found}/'; p['pin_numeric'] = found
    else: p['pin_url_note'] = 'numeric pin id not found on the board or the uploader\'s pins'
    json.dump(p, open(f, 'w'), indent=1); print(aid, found, flush=True); time.sleep(1.5)
