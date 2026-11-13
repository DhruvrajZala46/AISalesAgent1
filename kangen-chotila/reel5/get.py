import json, sys, os
sys.path.insert(0, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools')
from pin_dl import dl
meta = json.load(open('raw/pinmeta.json')) if os.path.exists('raw/pinmeta.json') else {}
for a in sys.argv[1:]:
    tag, i = a.rsplit(':', 1); p = json.load(open(f'pin/{tag}.json'))[int(i)]; name = f'{tag}{i}'
    out = f'raw/{name}.mp4'
    if os.path.exists(out): continue
    try:
        dl(p['videos'][0], out); meta[name] = dict(pin=p['url'], creator=p['creator'], user=p['creator_user'], src=p['src_link'], title=p['title'])
        print('ok', name, flush=True)
    except Exception as e: print('fail', name, e, flush=True)
json.dump(meta, open('raw/pinmeta.json', 'w'), ensure_ascii=False, indent=0)
