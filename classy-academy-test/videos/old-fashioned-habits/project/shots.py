import sys,subprocess,json,os,numpy as np
from PIL import Image,ImageDraw
src,out=sys.argv[1],sys.argv[2]; key=os.path.basename(src)[:-4]
W,H=96,72
p=subprocess.run(['ffmpeg','-v','error','-i',src,'-vf',f'fps=5,scale={W}:{H}','-pix_fmt','gray','-f','rawvideo','-'],capture_output=True).stdout
a=np.frombuffer(p,np.uint8).reshape(-1,H,W).astype(np.float32)
d=np.abs(np.diff(a,axis=0)).mean((1,2))
cuts=[0]+[i+1 for i in range(len(d)) if d[i]>14 and d[i]>3*np.median(d[max(0,i-10):i+10])]
shots=[]
for i,c in enumerate(cuts):
    e=cuts[i+1] if i+1<len(cuts) else len(a)
    if (e-c)/5>=1.2: shots.append((c/5,e/5))
json.dump(shots,open(f'{out}/{key}.json','w'))
# sheet: frame from middle of each shot
tw,th=240,180; cols=8
frames=[]
for s,e in shots:
    t=(s+e)/2
    im=subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.2f}','-i',src,'-frames:v','1','-vf',f'scale={tw}:{th}','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    if len(im)==tw*th*3: frames.append((s,e,Image.frombytes('RGB',(tw,th),im)))
per=48
for p0 in range(0,len(frames),per):
    chunk=frames[p0:p0+per]; rows=(len(chunk)+cols-1)//cols
    sh=Image.new('RGB',(cols*tw,rows*(th+14)),'black'); dr=ImageDraw.Draw(sh)
    for i,(s,e,im) in enumerate(chunk):
        x=(i%cols)*tw; y=(i//cols)*(th+14); sh.paste(im,(x,y+14)); dr.text((x+2,y+1),f"{int(s//60)}:{s%60:04.1f}-{int(e//60)}:{e%60:04.1f}",fill='yellow')
    sh.save(f'{out}/{key}_{p0//per}.jpg',quality=80)
print(key,len(shots),'shots')
