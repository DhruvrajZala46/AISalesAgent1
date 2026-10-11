# Storyboard frame (~every 5s) next to the words spoken during it: what the viewer SEES for what they HEAR
import re,sys,os
from PIL import Image,ImageDraw
vtt,fdir,dur,out=sys.argv[1],sys.argv[2],float(sys.argv[3]),sys.argv[4]
fs=sorted(os.listdir(fdir)); N=len(fs); step=dur/N
ts=lambda s:sum(float(x)*m for x,m in zip(s.split(':'),[3600,60,1]))
words=[]
for a,b,body in re.findall(r'(\d+:\d+:\d+\.\d+) --> (\d+:\d+:\d+\.\d+)[^\n]*\n(.*?)(?:\n\n|\Z)',open(vtt,encoding='utf-8').read(),re.S):
    if '<c>' not in body: continue
    line=body.strip().split('\n')[-1]
    parts=re.split(r'<(\d+:\d+:\d+\.\d+)><c>',line); t=ts(a)
    first=re.sub(r'<[^>]+>','',parts[0]).strip()
    if first: words.append((t,first))
    for k in range(1,len(parts),2): words.append((ts(parts[k]),re.sub(r'<[^>]+>','',parts[k+1]).strip()))
C=5; W,H=320,180; rows=(N+C-1)//C
sh=Image.new('RGB',(C*W,rows*(H+44)),'white'); d=ImageDraw.Draw(sh)
for i,f in enumerate(fs):
    t0=i*step; t1=t0+step; x,y=(i%C)*W,(i//C)*(H+44)
    sh.paste(Image.open(f'{fdir}/{f}'),(x,y+44))
    txt=' '.join(w for t,w in words if t0<=t<t1)
    d.text((x+3,y+2),f"{int(t0//60)}:{int(t0%60):02d}",fill='red')
    d.text((x+40,y+2),txt[:52],fill='black'); d.text((x+3,y+15),txt[52:110],fill='black'); d.text((x+3,y+28),txt[110:168],fill='black')
half=(rows+1)//2
sh.crop((0,0,C*W,half*(H+44))).save(out+'_a.jpg',quality=80)
sh.crop((0,half*(H+44),C*W,rows*(H+44))).save(out+'_b.jpg',quality=80)
