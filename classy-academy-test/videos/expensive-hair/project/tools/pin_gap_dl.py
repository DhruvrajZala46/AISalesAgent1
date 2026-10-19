# pin_dl.py - download chosen Pinterest pins from gap/<set>.json into raw/<asset>_p<k>.<ext>, recording the source
#   python3 -I pin_dl.py A09=A09:4 A43=A54:7 A82=A82:7,A82:4 ...
import sys, os, json, subprocess, urllib.request
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
meta = json.load(open('raw/meta_pin.json')) if os.path.exists('raw/meta_pin.json') else {}
for arg in sys.argv[1:]:
    aid, picks = arg.split('=', 1)
    for k, p in enumerate(picks.split(',')):
        st, n = p.split(':'); c = json.load(open(f'gap/{st}.json'))[int(n)]
        if c.get('video'):
            out = f'raw/{aid}_p{k}.mp4'
            if not os.path.exists(out):
                if c['video'].endswith('.m3u8'):
                    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-user_agent', UA, '-i', c['video'], '-c', 'copy', out])
                else:
                    open(out, 'wb').write(urllib.request.urlopen(urllib.request.Request(c['video'], headers={'User-Agent': UA}), timeout=120).read())
        else:
            out = f'raw/{aid}_p{k}.jpg'
            if not os.path.exists(out):
                open(out, 'wb').write(urllib.request.urlopen(urllib.request.Request(c['image'], headers={'User-Agent': UA}), timeout=120).read())
        meta[os.path.basename(out)] = dict(asset=aid, pin=f"https://www.pinterest.com/pin/{c['pin_id']}/", pinner=c['pinner'], link=c['link'],
                                           handles=c['handles'], text=c['text'], w=c['vw'], h=c['vh'], dur=c['vdur'])
        print(out, os.path.getsize(out) if os.path.exists(out) else 'FAILED', c['pinner'], c['link'], flush=True)
json.dump(meta, open('raw/meta_pin.json', 'w'), indent=1)
