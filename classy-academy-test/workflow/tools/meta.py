# meta.py OUTDIR id ... : public watch-page data via InnerTube "next" (no login): title, date, views, likes, comment count,
# description, chapters, owner subs, top comments (up to 4 pages). One video per call, caller paces requests.
import json,sys,urllib.request,os,re,time
CTX={"client":{"clientName":"WEB","clientVersion":"2.20250101.00.00","hl":"en","gl":"US"}}
def post(body):
    req=urllib.request.Request("https://www.youtube.com/youtubei/v1/next?prettyPrint=false",data=json.dumps(dict(context=CTX,**body)).encode(),
        headers={"Content-Type":"application/json","User-Agent":"Mozilla/5.0"})
    return json.load(urllib.request.urlopen(req,timeout=30))
def walk(x,key):
    if isinstance(x,dict):
        for k,v in x.items():
            if k==key: yield v
            yield from walk(v,key)
    elif isinstance(x,list):
        for v in x: yield from walk(v,key)
def txt(r):
    if not r: return ''
    if 'simpleText' in r: return r['simpleText']
    return ''.join(x.get('text','') for x in r.get('runs',[]))
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
for vid in sys.argv[2:]:
    f=os.path.join(out,vid+'.json')
    if os.path.exists(f): continue
    try:
        d=post({"videoId":vid}); info={'id':vid}
        for p in walk(d,'videoPrimaryInfoRenderer'):
            info['title']=txt(p.get('title')); info['date']=txt(p.get('dateText'))
            info['views']=txt(((p.get('viewCount') or {}).get('videoViewCountRenderer') or {}).get('viewCount')); break
        dj=json.dumps(d)
        m=re.search(r'along with ([\d,]+) other people',dj); info['likes']=int(m.group(1).replace(',','')) if m else None
        m=re.search(r'"contextualInfo":\s*\{"runs":\s*\[\{"text":\s*"([^"]+)"',dj); info['comment_count']=m.group(1) if m else None
        for o in walk(d,'videoOwnerRenderer'): info['channel']=txt(o.get('title')); info['subs']=txt(o.get('subscriberCountText')); break
        for desc in walk(d,'attributedDescription'): info['description']=desc.get('content',''); break
        ch=[]
        for mm in walk(d,'macroMarkersListItemRenderer'):
            c=(mm.get('timeDescription',{}).get('simpleText'),txt(mm.get('title')))
            if c not in ch: ch.append(c)
        info['chapters']=ch
        tok=None
        for s in walk(d,'itemSectionRenderer'):
            if s.get('sectionIdentifier')=='comment-item-section':
                for c in walk(s,'continuationCommand'): tok=c['token']; break
            if tok: break
        comments=[]; pages=0
        while tok and pages<4:
            time.sleep(3); c=post({"continuation":tok}); pages+=1; tok=None
            for m2 in walk(c,'mutations'):
                for mu in m2:
                    p=mu.get('payload',{}).get('commentEntityPayload')
                    if p: comments.append(dict(id=p['properties']['commentId'],text=p['properties']['content']['content'],likes=p['toolbar'].get('likeCountNotliked',''),replies=p['toolbar'].get('replyCount',''),author=p['author']['displayName']))
            for cc in walk(c,'continuationItemRenderer'):
                for t in walk(cc,'continuationCommand'): tok=t['token']; break
                if tok: break
        seen=set(); info['comments']=[x for x in comments if not (x['id'] in seen or seen.add(x['id']))]
        json.dump(info,open(f,'w'))
        print(vid,info.get('date'),info.get('views'),info.get('likes'),info.get('comment_count'),len(info['chapters']),len(info['comments']),flush=True)
    except Exception as e: print(vid,'ERR',e,flush=True)
