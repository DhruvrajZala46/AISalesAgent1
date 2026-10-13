# aieye.py - three full-size frames per clip for the AI check by eye (waxy skin, morphing hair, objects that change).
# usage (inside the work folder): python3 aieye.py OUT.jpg key1 key2 ...
import sys,subprocess,io
from PIL import Image,ImageDraw
out=sys.argv[1]; keys=sys.argv[2:]; H=420; rows=[]
for k in keys:
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'raw/{k}.mp4'],capture_output=True,text=True).stdout)
    ims=[]
    for f in (0.15,0.5,0.85):
        b=subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',f'{d*f:.2f}','-i',f'raw/{k}.mp4','-frames:v','1','-vf',f'scale=-2:{H}','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
        ims.append(Image.open(io.BytesIO(b)).convert('RGB'))
    rows.append((k,ims))
cols=2; per=max(sum(i.width for i in ims) for k,ims in rows)
sh=Image.new('RGB',(cols*(per+10),((len(rows)+1)//2)*(H+20)),'white'); dr=ImageDraw.Draw(sh)
for n,(k,ims) in enumerate(rows):
    x=(n%cols)*(per+10); y=(n//cols)*(H+20); dr.text((x+2,y+2),k,fill='red')
    for im in ims: sh.paste(im,(x,y+18)); x+=im.width
sh.save(out,quality=85); print(out)
