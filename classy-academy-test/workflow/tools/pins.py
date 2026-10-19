# Pinterest search (public JSON used by the web app); prints pins: id, video?, pinner, native creator, title/desc
import json,sys,urllib.request,urllib.parse,re,os
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
def get(u,h={}): return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA,**h}),timeout=30).read()
def search(q,n=50,bookmark=None):
    o={"query":q,"scope":"pins","page_size":n}
    if bookmark: o["bookmarks"]=[bookmark]
    d={"options":o,"context":{}}
    url="https://www.pinterest.com/resource/BaseSearchResource/get/?"+urllib.parse.urlencode({"source_url":f"/search/pins/?q={q}","data":json.dumps(d)})
    r=json.loads(get(url,{"X-Pinterest-PWS-Handler":"www/search/[scope].js"}))["resource_response"]
    return r["data"]["results"], r.get("bookmark")
if __name__=="__main__":
    os.makedirs('pinjson',exist_ok=True)
    for q in sys.argv[1:]:
        res,_=search(q)
        json.dump(res,open('pinjson/'+re.sub(r'\W+','_',q)+'.json','w'))
        print('###',q,len(res))
        for i,p in enumerate(res):
            vid='V' if (p.get('videos') or p.get('story_pin_data')) else '-'
            pn=(p.get('pinner') or {}).get('username'); nc=(p.get('native_creator') or {}).get('username')
            t=' '.join(str(p.get(k) or '') for k in ('grid_title','title','description')).replace('\n',' ')
            print(f"{i:2d} {vid} {p.get('id')} pinner={pn} creator={nc} link={(p.get('link') or '')[:60]} | {t[:150]}")
