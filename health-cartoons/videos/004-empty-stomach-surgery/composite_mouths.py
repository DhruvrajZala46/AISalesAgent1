# Paste only the mouth area of each AI mouth edit onto its base sprite (feathered ellipse), then key all variants with the BASE crop box.
import glob,os,json,numpy as np
from PIL import Image, ImageFilter, ImageDraw
from scipy import ndimage
import importlib.util
spec=importlib.util.spec_from_file_location('prep','prep_art.py')
def keyimg(img):  # same keying as prep_art.key but without cropping
    im=np.asarray(img.convert('RGB')).astype(np.float32); r,g,b=im[...,0],im[...,1],im[...,2]
    gn=g-np.maximum(r,b); a=np.clip(1-(gn-40)/80,0,1)
    g2=np.where((gn>15)|((g>np.maximum(r,b))&(a<1)),np.minimum(g,np.maximum(r,b)),g)
    o=Image.fromarray(np.dstack([r,g2,b,a*255]).astype(np.uint8),'RGBA')
    al=o.split()[3].filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.6)); o.putalpha(al); return o
def blob(base,edit):
    A=np.asarray(base).astype(np.int16); B=np.asarray(edit).astype(np.int16)
    d=np.abs(A-B).max(axis=2)>60; d=ndimage.binary_opening(d,iterations=2)
    lab,k=ndimage.label(ndimage.binary_dilation(d,iterations=6))
    if k==0: return None
    sizes=ndimage.sum(d,lab,range(1,k+1)); ys,xs=np.nonzero(lab==np.argmax(sizes)+1)
    return xs.min(),xs.max(),ys.min(),ys.max()
out={}
bases=sorted({os.path.basename(f)[:-7] for f in glob.glob('art/mouth/*_c.webp')})
for n in bases:
    base=Image.open(f'art/src/{n}.png').convert('RGB'); W,H=base.size
    eo=f'art/mouth/{n}_o.webp'; ec=f'art/mouth/{n}_c.webp'
    ref=Image.open(eo if os.path.exists(eo) else ec).convert('RGB')
    bx0,bx1,by0,by1=blob(base,ref); cx,cy=(bx0+bx1)/2,(by0+by1)/2; rx=(bx1-bx0)/2+W*.018; ry=(by1-by0)/2+W*.018
    if os.path.exists(eo):  # the closed mouth must sit inside the same area: grow to cover its blob if it is near
        bb=blob(base,Image.open(ec).convert('RGB'))
        if bb and abs((bb[0]+bb[1])/2-cx)<rx and abs((bb[2]+bb[3])/2-cy)<ry*1.5:
            rx=max(rx,(bb[1]-bb[0])/2+W*.018)
    OV={'burger_base':(115,95),'burger_scared':(115,100)}
    if n in OV: rx,ry=OV[n]
    mask=Image.new('L',(W,H),0); ImageDraw.Draw(mask).ellipse([cx-rx,cy-ry,cx+rx,cy+ry],fill=255); mask=mask.filter(ImageFilter.GaussianBlur(W*.006))
    kb=keyimg(base); box=kb.getbbox()
    for suf,src in (('c',ec),('o',eo)):
        if not os.path.exists(src): continue
        e=Image.open(src).convert('RGB'); comp=Image.composite(e,base,mask)
        keyimg(comp).crop(box).save(f'art/{n}_{suf}.png')
    out[n]={'patch':[round(cx),round(cy),round(rx),round(ry)],'box':box,'variants':[s for s,f in (('c',ec),('o',eo)) if os.path.exists(f)]}
    print(n,out[n])
json.dump(out,open('art/mouth/patches.json','w'),indent=1)

meta=json.load(open('art/meta.json'))
for n,v in out.items():
    if n in meta: meta[n]['variants']=v['variants']
json.dump(meta,open('art/meta.json','w'),indent=1); open('art/meta.js','w').write('window.ART='+json.dumps(meta)+';')
