# Extract storyboard sprite sheets from an mhtml into individual frames + report interval
import email,sys,os,io
from PIL import Image
src,out=sys.argv[1],sys.argv[2]; os.makedirs(out,exist_ok=True)
msg=email.message_from_bytes(open(src,'rb').read())
sheets=[p.get_payload(decode=True) for p in msg.walk() if p.get_content_type().startswith('image/')]
n=0
for b in sheets:
    im=Image.open(io.BytesIO(b)).convert('RGB'); W,H=im.size
    cols,rows=W//320,H//180
    for r in range(rows):
        for c in range(cols):
            f=im.crop((c*320,r*180,c*320+320,r*180+180))
            if f.getextrema()[0][1]<8 and f.getextrema()[1][1]<8: continue   # trailing black filler
            f.save(f'{out}/{n:04d}.jpg',quality=88); n+=1
print(n,'frames from',len(sheets),'sheets')
