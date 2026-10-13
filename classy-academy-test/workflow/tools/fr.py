# fr.py - full frames of clips (720x1280 space) with a 160 px grid, to measure where to draw on her.
# usage (inside the work folder): python3 fr.py OUT.jpg key:t key:t ...
# fr.py OUT key:t key:t ... -> frames at 270x480 (from the 720x1280 cover crop) with a grid every 160 px (labels in 720-space)
import sys,subprocess,io
from PIL import Image,ImageDraw
out=sys.argv[1]; items=sys.argv[2:]; FW,FH=270,480; cols=8
sh=Image.new('RGB',(cols*(FW+4),((len(items)+cols-1)//cols)*(FH+18)),'white'); d=ImageDraw.Draw(sh)
for n,it in enumerate(items):
    k,t=it.rsplit(':',1)
    b=subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',t,'-i',f'raw/{k}.mp4','-frames:v','1','-vf','scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,scale=270:480','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
    x,y=(n%cols)*(FW+4),(n//cols)*(FH+18)
    try: im=Image.open(io.BytesIO(b)).convert('RGB')
    except Exception: continue
    g=ImageDraw.Draw(im)
    for v in range(160,720,160): g.line([(v*FW/720,0),(v*FW/720,FH)],fill=(255,0,0),width=1); g.text((v*FW/720+2,2),str(v),fill=(255,0,0))
    for v in range(160,1280,160): g.line([(0,v*FH/1280),(FW,v*FH/1280)],fill=(255,0,0),width=1); g.text((2,v*FH/1280+2),str(v),fill=(255,0,0))
    sh.paste(im,(x,y+16)); d.text((x+2,y+2),it,fill='blue')
sh.save(out,quality=85); print(out)
