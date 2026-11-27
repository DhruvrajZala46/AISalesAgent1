import json,glob,os,re
from PIL import Image,ImageDraw
rows=[]
for f in sorted(glob.glob('pin/*.json')):
    tag=os.path.basename(f)[:-5]
    for i,x in enumerate(json.load(open(f))):
        s=x['src_link'] or ''
        if x['videos'] and re.search(r'instagram\.com/(reel|p)/|tiktok\.com/',s):
            rows.append((tag,i,x))
seen=set(); R=[]
for t,i,x in rows:
    if x['src_link'] in seen: continue
    seen.add(x['src_link']); R.append((t,i,x))
print(len(rows),'with IG/TikTok source;',len(R),'unique')
json.dump([dict(tag=t,i=i,**x) for t,i,x in R],open('cands.json','w'),indent=0)
W,H=170,260; cols=10
from collections import defaultdict
by=defaultdict(list)
for t,i,x in R: by[t].append((i,x))
tags=sorted(by); 
for g in range(0,len(tags),5):
    grp=tags[g:g+5]; n=sum((len(by[t])+cols-1)//cols for t in grp)
    sh=Image.new('RGB',(W*cols,(H+16)*n),'white'); d=ImageDraw.Draw(sh); r=0
    for t in grp:
        for k,(i,x) in enumerate(by[t]):
            if k and k%cols==0: r+=1
            try: im=Image.open(f'pin/{t}_{i}.jpg').convert('RGB'); im=im.resize((W,int(im.height*W/im.width))).crop((0,0,W,H))
            except Exception: continue
            X=(k%cols)*W; Y=r*(H+16); sh.paste(im,(X,Y+16)); d.text((X+2,Y+2),f'{t}{i}',fill='red')
        r+=1
    sh.save(f'fsheet_{g//5}.jpg',quality=80)
print(len(tags),'tags', [ (t,len(by[t])) for t in tags])
