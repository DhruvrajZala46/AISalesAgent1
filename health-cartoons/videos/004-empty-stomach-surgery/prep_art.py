# Key every green-screen sprite to a trimmed transparent PNG and detect the eye whites (for blinks) -> art/meta.json
import json,glob,os,numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
def key(src):
    im=np.asarray(Image.open(src).convert('RGB')).astype(np.float32); r,g,b=im[...,0],im[...,1],im[...,2]
    gn=g-np.maximum(r,b); a=np.clip(1-(gn-40)/80,0,1)
    g2=np.where((gn>15)|((g>np.maximum(r,b))&(a<1)),np.minimum(g,np.maximum(r,b)),g)
    img=Image.fromarray(np.dstack([r,g2,b,a*255]).astype(np.uint8),'RGBA')
    al=img.split()[3].filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.6)); img.putalpha(al)
    return img.crop(img.getbbox())
def eyes(img):
    A=np.asarray(img).astype(np.float32); rgb=A[...,:3]; al=A[...,3]
    white=(rgb.min(axis=2)>225)&(al>200)
    lab,n=ndimage.label(white); C=[]; H,W=white.shape
    for i,sl in enumerate(ndimage.find_objects(lab),1):
        h=sl[0].stop-sl[0].start; w=sl[1].stop-sl[1].start
        if (lab[sl]==i).sum()<W*H*0.001 or not (0.5<h/w<2.0): continue
        # the white region plus its interior holes = the eye; its centre must hold a dark pupil
        filled=ndimage.binary_fill_holes(lab[sl]==i); ys,xs=np.nonzero(filled)
        cy,cx=ys.mean(),xs.mean(); ry,rx=h/2,w/2
        yy,xx=np.mgrid[0:h,0:w]; inner=((yy-cy)/ry)**2+((xx-cx)/rx)**2<0.35
        dark=(rgb[sl].max(axis=2)<80)[inner&filled].mean() if (inner&filled).any() else 0
        if dark<0.12: continue
        C.append({'cx':sl[1].start+w/2,'cy':sl[0].start+h/2,'rx':rx,'ry':ry,'dark':round(float(dark),2)})
    best=None
    for i in range(len(C)):
        for j in range(i+1,len(C)):
            a,b=C[i],C[j]; s=abs(a['cy']-b['cy'])/max(a['ry'],b['ry'])+abs(a['rx']-b['rx'])/max(a['rx'],b['rx'])-0.002*(a['rx']+b['rx'])
            if abs(a['cy']-b['cy'])<1.2*max(a['ry'],b['ry']) and (best is None or s<best[0]): best=(s,[a,b])
    out=sorted(best[1],key=lambda e:e['cx']) if best else C[:1]
    lid=None
    if out:
        e=out[0]; y0=int(max(0,e['cy']-e['ry']*2.0)); y1=int(max(1,e['cy']-e['ry']*1.2)); x0=int(e['cx']-e['rx']); x1=int(e['cx']+e['rx'])
        p=rgb[y0:y1,x0:x1].reshape(-1,3); m=al[y0:y1,x0:x1].reshape(-1)>200; p=p[m]; p=p[(p.min(axis=1)<225)&(p.max(axis=1)>120)]
        if len(p): lid='#%02x%02x%02x'%tuple(int(v) for v in np.median(p,axis=0))
    return out,lid
meta={}
for f in sorted(glob.glob('art/*.webp')):
    n=os.path.basename(f)[:-5]
    if n.startswith('plate_') or n in ('bg_throat',):
        im=Image.open(f).convert('RGB'); im.save(f'art/{n}.jpg',quality=92); meta[n]={'w':im.size[0],'h':im.size[1]}; continue
    img=key(f); img.save(f'art/{n}.png'); e,lid=eyes(img)
    meta[n]={'w':img.size[0],'h':img.size[1],'eyes':e,'lid':lid}
    print(n,img.size,[(round(x['cx']),round(x['cy']),round(x['rx']),round(x['ry'])) for x in e],lid)
json.dump(meta,open('art/meta.json','w'),indent=1)

json.dump(meta,open('art/meta.json','w'),indent=1); open('art/meta.js','w').write('window.ART='+json.dumps(meta)+';')
