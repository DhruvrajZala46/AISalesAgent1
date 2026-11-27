import sys,subprocess
from PIL import Image,ImageDraw
src=sys.argv[1]; out=sys.argv[2]; wins=[tuple(map(float,w.split(':'))) for w in sys.argv[3:]]
tw,th=200,112; cols=10; fr=[]
for a,b,st in wins:
    t=a
    while t<=b:
        im=subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.2f}','-i',src,'-frames:v','1','-vf',f'scale={tw}:{th}','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
        if len(im)==tw*th*3: fr.append((t,Image.frombytes('RGB',(tw,th),im)))
        t+=st
rows=(len(fr)+cols-1)//cols; sh=Image.new('RGB',(cols*tw,rows*(th+12)),'black'); d=ImageDraw.Draw(sh)
for i,(t,im) in enumerate(fr):
    x=(i%cols)*tw; y=(i//cols)*(th+12); sh.paste(im,(x,y+12)); d.text((x+2,y),f"{int(t//60)}:{t%60:04.1f}",fill='yellow')
sh.save(out,quality=80)
