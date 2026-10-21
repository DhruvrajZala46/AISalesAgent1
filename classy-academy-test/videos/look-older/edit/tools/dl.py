# dl.py ID TAG INDEX [--image]  : download pin INDEX of pin/TAG.json as the asset ID -> raw/ID.mp4 (or .jpg) + picks/ID.json
# The pin's video (720p mp4 or HLS) is fetched; with --image (or a pin without video) the original image is fetched instead.
import sys, os, json, subprocess, urllib.request
sys.path.insert(0, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools')
from pin_dl import dl, get
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
aid, tag, idx = sys.argv[1], sys.argv[2], int(sys.argv[3]); img = '--image' in sys.argv
p = json.load(open(f'{L}/pin/{tag}.json'))[idx]
os.makedirs(f'{L}/raw', exist_ok=True); os.makedirs(f'{L}/picks', exist_ok=True)
for old in [f'{L}/raw/{aid}.mp4', f'{L}/raw/{aid}.jpg']:
    if os.path.exists(old): os.remove(old)
if p['videos'] and not img:
    out = f'{L}/raw/{aid}.mp4'; dl(p['videos'][0], out); media = p['videos'][0]
else:
    out = f'{L}/raw/{aid}.jpg'; media = p['orig'] or p['thumb']; open(out, 'wb').write(get(media))
pr = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate:format=duration',
                                '-of', 'json', out], capture_output=True, text=True).stdout or '{}')
st = (pr.get('streams') or [{}])[0]; fps = st.get('r_frame_rate', '0/1'); a, b = (fps.split('/') + ['1'])[:2]
rec = dict(id=aid, pin_id=p['id'], pin_url=p['url'], creator=p['creator'], creator_user=p['creator_user'], src_link=p['src_link'],
           pin_title=p['title'], media_url=media, file=os.path.relpath(out, L), w=st.get('width'), h=st.get('height'),
           fps=round(float(a) / float(b or 1), 2) if b != '0' else None, dur=round(float((pr.get('format') or {}).get('duration') or 0), 2),
           search_tag=tag, search_index=idx, desc=p.get('desc',''), sig=p.get('sig'), pinner=p.get('pinner',''), board=p.get('board',''), board_id=p.get('board_id',''), dom=p.get('dom',''))
old = json.load(open(f'{L}/picks/{aid}.json')) if os.path.exists(f'{L}/picks/{aid}.json') else {}
old.update(rec); json.dump(old, open(f'{L}/picks/{aid}.json', 'w'), indent=1)
print(json.dumps(rec))
