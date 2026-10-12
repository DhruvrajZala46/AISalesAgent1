# per clip: detect shots, save segments, make a sheet with one frame per shot (mid-shot) + range
import os,sys,json,subprocess,io,re
from PIL import Image,ImageDraw
F=os.getcwd(); R=F+'/raw'; meta=json.load(open(R+'/meta.json'))
SJ=F+'/shots.json'; S=json.load(open(SJ)) if os.path.exists(SJ) else {}
def probe(f):
    pr=json.loads(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height,color_transfer:format=duration','-of','json',f],capture_output=True,text=True).stdout)
    return float(pr['format']['duration']),pr['streams'][0]['width'],pr['streams'][0]['height'],pr['streams'][0].get('color_transfer','')
def shots(f,d):
    o=subprocess.run(['ffmpeg','-nostdin','-i',f,'-vf',"scale=160:-2,select='gt(scene,0.32)',showinfo",'-an','-f','null','-'],capture_output=True,text=True).stderr
    cuts=[float(x) for x in re.findall(r'pts_time:([\d.]+)',o)]
    b=[0]+[c for c in cuts if 0.4<c<d-0.4]+[d]; seg=[]
    for a,c in zip(b,b[1:]):
        if c-a>=0.5: seg.append([round(a,2),round(c,2)])
    return seg
keys=sys.argv[2:] if len(sys.argv)>2 else sorted(k for k in meta if os.path.exists(f'{R}/{k}.mp4'))
for k in keys:
    f=f'{R}/{k}.mp4'
    if k in S or not os.path.exists(f): continue
    d,w,h,tr=probe(f); S[k]=dict(d=round(d,2),w=w,h=h,hdr=tr in ('arib-std-b67','smpte2084'),seg=shots(f,d))
json.dump(S,open(SJ,'w'),indent=0)
out=sys.argv[1]; rows=[]
for k in keys:
    if k not in S: continue
    fr=[]
    for a,c in S[k]['seg'][:9]:
        b=subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',str((a+c)/2),'-i',f'{R}/{k}.mp4','-frames:v','1','-vf','scale=-2:240','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
        try: fr.append((Image.open(io.BytesIO(b)).convert('RGB'),a,c))
        except Exception: pass
    rows.append((k,fr))
W=1500
for pg in range(0,len(rows),6):
  sh=Image.new('RGB',(W,6*272),'white'); dr=ImageDraw.Draw(sh); y=0
  for k,fr in rows[pg:pg+6]:
    s=S[k]; m=meta.get(k,{'creator':'?','user':'?'}); x=0
    flag=(' LOWRES' if min(s['w'],s['h'])<500 else '')+(' HDR' if s['hdr'] else '')
    dr.text((4,y+2),f"{k} {s['d']}s {s['w']}x{s['h']}{flag}  by {m['creator']} (@{m['user']})",fill='red')
    for im,a,c in fr:
        if x+im.width>W: break
        sh.paste(im,(x,y+16)); dr.text((x+3,y+258),f'{a}-{c}',fill='blue'); x+=im.width+3
    y+=272
  sh.save(f'{out}_{pg//6}.jpg',quality=78)
print(len(rows))
