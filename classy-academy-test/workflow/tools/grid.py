import os,sys,json,subprocess,io
from PIL import Image,ImageDraw
F=os.getcwd(); R=F+'/raw'; S=json.load(open(F+'/shots.json'))
keys=sys.argv[2:] if len(sys.argv)>2 else sorted(S)
tiles=[]
for k in keys:
    s=S[k]
    for j,(a,c) in enumerate(s['seg'][:6]):
        b=subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',str(a+(c-a)*0.4),'-i',f'{R}/{k}.mp4','-frames:v','1','-vf','scale=150:266:force_original_aspect_ratio=decrease,pad=150:266:(ow-iw)/2:(oh-ih)/2','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
        try: im=Image.open(io.BytesIO(b)).convert('RGB')
        except Exception: continue
        flag=('L' if min(s['w'],s['h'])<500 else '')+('H' if s['hdr'] else '')
        tiles.append((im,f'{k}{flag}',f'#{j} {a}-{c}'))
cols,rows=12,5; per=cols*rows
for p in range(0,len(tiles),per):
    sh=Image.new('RGB',(cols*152,rows*296),'white'); d=ImageDraw.Draw(sh)
    for i,(im,l1,l2) in enumerate(tiles[p:p+per]):
        x,y=(i%cols)*152,(i//cols)*296; sh.paste(im,(x,y+14)); d.text((x+2,y+1),l1,fill='red'); d.text((x+2,y+281),l2,fill='blue')
    sh.save(f'{sys.argv[1]}_{p//per}.jpg',quality=80)
print(len(tiles),'tiles',(len(tiles)+per-1)//per,'pages')
