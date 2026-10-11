import json,sys
from PIL import Image,ImageDraw
S,out,tags=sys.argv[1],sys.argv[2],sys.argv[3:]
W,H=96,150; C=16; blocks=[]
for t in tags:
    d=json.load(open(f'{S}/pin/{t}.json')); idx=[i for i,p in enumerate(d) if p.get('videos')]
    r=max(1,(len(idx)+C-1)//C); im=Image.new('RGB',(W*C,(H+13)*r),'white'); dr=ImageDraw.Draw(im)
    for j,i in enumerate(idx):
        try: th=Image.open(f'{S}/pin/{t}_{i}.jpg').convert('RGB')
        except Exception: continue
        th=th.resize((W,int(th.height*W/th.width))).crop((0,0,W,H)); x,y=(j%C)*W,(j//C)*(H+13)
        im.paste(th,(x,y+13)); dr.text((x+2,y+1),f'{t} {i}',fill='red')
    blocks.append(im)
sh=Image.new('RGB',(W*C,sum(b.height for b in blocks)),'white'); y=0
for b in blocks: sh.paste(b,(0,y)); y+=b.height
sh.save(out,quality=80); print(sh.size)
