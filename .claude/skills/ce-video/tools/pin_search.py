import json,sys,os,time,urllib.request,urllib.parse
from PIL import Image,ImageDraw
# results go to $PIN_OUT (default ./pin): <tag>.json (creator + pin URL for credits), thumbnails, sheet_<tag>.jpg
O=os.environ.get("PIN_OUT") or os.path.join(os.getcwd(),"pin"); os.makedirs(O,exist_ok=True)
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
def get(url,headers={}):
    r=urllib.request.Request(url,headers={"User-Agent":UA,**headers}); return urllib.request.urlopen(r,timeout=30).read()
def videos_of(p):
    out=[]
    vl=(p.get('videos') or {}).get('video_list') or {}
    for k in ('V_720P','V_EXP7','V_EXP6','V_EXP5','V_HLSV4'):
        if k in vl: out.append(vl[k]['url']); break
    sp=p.get('story_pin_data') or {}
    for pg in sp.get('pages',[]) or []:
        for b in pg.get('blocks',[]) or []:
            v=((b.get('video') or {}).get('video_list') or {})
            for k in ('V_EXP7','V_720P','V_EXP6','V_EXP5','V_HLSV4'):
                if k in v: out.append(v[k]['url']); break
    return out
for tag,q in [a.split('=',1) for a in sys.argv[1:]]:
    d={"options":{"query":q,"scope":"pins","page_size":25},"context":{}}
    url="https://www.pinterest.com/resource/BaseSearchResource/get/?"+urllib.parse.urlencode({"source_url":f"/search/pins/?q={q}","data":json.dumps(d)})
    res=json.loads(get(url,{"X-Pinterest-PWS-Handler":"www/search/[scope].js"}))["resource_response"]["data"]["results"]
    pins=[]
    for p in res:
        im=(p.get('images') or {}); orig=(im.get('orig') or {}).get('url'); thumb=(im.get('474x') or im.get('236x') or {}).get('url')
        if not thumb: continue
        pn=(p.get('pinner') or {}); nc=(p.get('native_creator') or {}); pid=str(p.get('id') or '')
        pins.append(dict(id=pid,url=(f'https://www.pinterest.com/pin/{pid}/' if pid.isdigit() else ''),creator=(nc.get('full_name') or nc.get('username') or pn.get('full_name') or pn.get('username') or ''),creator_user=(nc.get('username') or pn.get('username') or ''),src_link=p.get('link') or '',orig=orig,thumb=thumb,videos=videos_of(p),title=(p.get('grid_title') or p.get('title') or '')[:80],
                         w=(im.get('orig') or {}).get('width'),h=(im.get('orig') or {}).get('height')))
    json.dump(pins,open(f"{O}/{tag}.json","w"),indent=0)
    W,H=180,280; cols=8; rows=(len(pins)+cols-1)//cols
    sh=Image.new('RGB',(W*cols,(H+16)*rows),'white'); dr=ImageDraw.Draw(sh)
    for i,p in enumerate(pins):
        f=f"{O}/{tag}_{i}.jpg"
        try:
            open(f,'wb').write(get(p['thumb'])); im=Image.open(f).convert('RGB'); im=im.resize((W,int(im.height*W/im.width))).crop((0,0,W,H))
        except Exception: continue
        x,y=(i%cols)*W,(i//cols)*(H+16); sh.paste(im,(x,y+16)); dr.text((x+3,y+2),f"{tag} {i}"+(" VIDEO" if p['videos'] else ""),fill='red' if p['videos'] else 'black')
    sh.save(f"{O}/sheet_{tag}.jpg",quality=78); print(tag,len(pins),'pins,',sum(1 for p in pins if p['videos']),'video')
    time.sleep(2.5)
