import os,sys,subprocess,json
from PIL import Image,ImageDraw
D,out=sys.argv[1],sys.argv[2]; fs=sorted(f for f in os.listdir(D) if f.endswith('.mp4'))
W,H,K=90,160,10; meta={}
rows=[]
for f in fs:
    d=float(subprocess.run(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {D}/{f}",shell=True,capture_output=True,text=True).stdout or 0)
    meta[f]=d; row=Image.new('RGB',(W*K+150,H),'white'); dr=ImageDraw.Draw(row); dr.text((2,2),f[:-4],fill='red'); dr.text((2,16),f'{d:.1f}s',fill='black')
    for k in range(K):
        t=d*(k+0.5)/K
        subprocess.run(f"ffmpeg -nostdin -v error -y -ss {t:.2f} -i {D}/{f} -frames:v 1 -vf scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H} {D}/_t.jpg",shell=True)
        try: row.paste(Image.open(f'{D}/_t.jpg'),(150+k*W,0)); dr.text((150+k*W+2,H-12),f'{t:.1f}',fill='yellow')
        except Exception: pass
    rows.append(row)
json.dump(meta,open(f'{D}/meta.json','w'))
for p in range(0,len(rows),13):
    sub=rows[p:p+13]; sh=Image.new('RGB',(W*K+150,len(sub)*(H+4)),'white')
    for j,r in enumerate(sub): sh.paste(r,(0,j*(H+4)))
    sh.save(f'{out}_{p//13}.jpg',quality=78)
