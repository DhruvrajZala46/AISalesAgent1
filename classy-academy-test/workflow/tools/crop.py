import cv2,json,sys,os
from PIL import Image,ImageDraw
R='real'; K=json.load(open(R+'/keep.json'))
fc=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
pf=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_profileface.xml')
PW,PH=427,720
def face(path):
    im=cv2.imread(path); g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    fs=list(fc.detectMultiScale(g,1.08,5,minSize=(24,24)))+list(pf.detectMultiScale(g,1.08,5,minSize=(24,24)))
    if not fs: return None
    return max(fs,key=lambda r:r[2]*r[3])
def crop(k,fw=0.30,fy=0.22,manual=None):
    p=f'{R}/{k}.jpg'; im=Image.open(p).convert('RGB'); W,H=im.size
    f=manual or face(p)
    if f is None: return None,None
    x,y,w,h=f; s=(PW*fw)/w  # scale so the face is fw of panel width
    s=min(s, 1.7); s=max(s, max(PW/W,PH/H))
    cx,cy=(x+w/2)*s,(y+h/2)*s; im2=im.resize((round(W*s),round(H*s)),Image.LANCZOS)
    L=min(max(0,round(cx-PW/2)),im2.width-PW); T=min(max(0,round(cy-PH*fy)),im2.height-PH)
    return im2.crop((L,T,L+PW,T+PH)),s
if __name__=='__main__':
    ks=sys.argv[1:]; tiles=[]
    for k in ks:
        c,s=crop(k)
        if c is None: print('noface',k); continue
        tiles.append((c,f'{k} x{s:.2f}'))
    cols=8; sh=Image.new('RGB',(cols*(PW//2+4),((len(tiles)+cols-1)//cols)*(PH//2+18)),'white'); d=ImageDraw.Draw(sh)
    for i,(c,l) in enumerate(tiles):
        X,Y=(i%cols)*(PW//2+4),(i//cols)*(PH//2+18); sh.paste(c.resize((PW//2,PH//2)),(X,Y+16)); d.text((X+2,Y+2),l,fill='red')
    sh.save('crops.jpg',quality=88)
