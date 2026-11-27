import sys,subprocess,os
from PIL import Image,ImageDraw
src,out,step=sys.argv[1],sys.argv[2],float(sys.argv[3]); key=os.path.basename(src)[:-4]
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
tw,th=240,150; cols=8; per=64; fr=[]
t=step/2
while t<dur:
    im=subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.1f}','-i',src,'-frames:v','1','-vf',f'scale={tw}:{th}','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    if len(im)==tw*th*3: fr.append((t,Image.frombytes('RGB',(tw,th),im)))
    t+=step
for p0 in range(0,len(fr),per):
    ch=fr[p0:p0+per]; rows=(len(ch)+cols-1)//cols
    sh=Image.new('RGB',(cols*tw,rows*(th+14)),'black'); d=ImageDraw.Draw(sh)
    for i,(t,im) in enumerate(ch):
        x=(i%cols)*tw; y=(i//cols)*(th+14); sh.paste(im,(x,y+14)); d.text((x+2,y+1),f"{int(t//60)}:{t%60:04.1f}",fill='yellow')
    sh.save(f'{out}/S_{key}_{p0//per}.jpg',quality=80)
print(key,len(fr))
