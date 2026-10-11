import json,sys
from PIL import Image,ImageDraw
S,out,tags=sys.argv[1],sys.argv[2],sys.argv[3:]
W,H=80,100; C=16; blocks=[]
for t in tags:
    n=min(16,len(json.load(open(f'{S}/pin/{t}.json'))))
    im=Image.new('RGB',(W*C,H+12),'white'); d=ImageDraw.Draw(im)
    for i in range(n):
        try: th=Image.open(f'{S}/pin/{t}_{i}.jpg').convert('RGB')
        except Exception: continue
        th.thumbnail((W,H)); im.paste(th,(i*W,12)); d.text((i*W+2,0),f'{t[3:]} {i}',fill='red')
    blocks.append(im)
sh=Image.new('RGB',(W*C,len(blocks)*(H+12)),'white')
for k,b in enumerate(blocks): sh.paste(b,(0,k*(H+12)))
sh.save(out,quality=80)
