import sys,subprocess
from PIL import Image,ImageDraw
src,a,b,step,out=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),sys.argv[5]
tw,th=240,180; cols=8; fr=[]; t=a
while t<=b:
    im=subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.2f}','-i',src,'-frames:v','1','-vf',f'scale={tw}:{th}','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    if len(im)==tw*th*3: fr.append((t,Image.frombytes('RGB',(tw,th),im)))
    t+=step
rows=(len(fr)+cols-1)//cols; sh=Image.new('RGB',(cols*tw,rows*(th+14)),'black'); d=ImageDraw.Draw(sh)
for i,(t,im) in enumerate(fr):
    x=(i%cols)*tw; y=(i//cols)*(th+14); sh.paste(im,(x,y+14)); d.text((x+2,y+1),f"{int(t//60)}:{t%60:04.1f}",fill='yellow')
sh.save(out,quality=80)
