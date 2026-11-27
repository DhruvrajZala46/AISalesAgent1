import json,csv,re
from PIL import Image,ImageDraw
C={f"{c['tag']}{c['i']}":c for c in json.load(open('cands.json'))}
B={b['k']:b for b in json.load(open('../ofh/beats.json'))['beats']}
fmt=lambda t:f"{int(t//60)}:{t%60:04.1f}"
SHOTS=[
('S01','H1','Hook: a woman in a camel coat walking a city street',['camelwalk39','camelwalk46','camelwalk48']),
('S02','H1b','Hook: same white shirt + camel coat, worn well',['whiteshirt19','whiteshirt41','whiteshirt20','whiteshirt17']),
('S03','H2','Coat details: hands on the belt / buttons of a wool coat',['coatbutton28','coatbutton11','coatbutton37']),
('S04','H3','A woman pressing clothes at home (the old lessons, modern)',['ironing0','ironing20']),
('S05','H4','Three panels: press a blouse / sew a hem / care for shoes',['steamer13','hem26','shoepolish4']),
('S06','H5','Polished women walking, outfits that look considered',['posture11','posture18','polished21']),
('S07','H6','Title background: elegant coat moment',['navycoat15','camelwalk46']),
('S08','A2','Wrinkled shirt',['steamer20','ironing12']),
('S09','A3','Crisp pressed shirt',['steamer36','ironing48']),
('S10','A4','Handheld steamer on a blouse',['steamer5','steamer8','steamer43']),
('S11','A4b','Delicate fabric (silk/satin) steamed gently',['steamer37']),
('S12','A5','Collar / cuffs / front pressed (three panels)',['ironing38','ironing20','ironing48']),
('S13','A5b','Hang it straight away',['hanger16','hanger14']),
('S14','A6','Result: a pressed white shirt outfit',['whiteshirt40','whiteshirt25']),
('S15','B2','Clothes left on a chair',['chairpile5','chairpile1','chairpile43']),
('S16','B3','Coat on a shaped wooden hanger',['hanger2','hanger33','hanger49']),
('S17','B4','Knitwear folded, not hung',['foldsweater21','foldsweater46','foldsweater43']),
('S18','B4b','Hangers in a wardrobe (wire vs good hangers)',['hanger32','hanger21']),
('S19','B5','Clothes airing / calm bedroom by a window',['morning24','morning29']),
('S20','B6','An orderly neutral wardrobe',['wardrobe19','wardrobe37','wardrobe42']),
('S21','C2','Loose button / fallen hem (panels)',['sewing17','sewing5','hem2','hem28']),
('S22','C4','Small sewing box, repair done in the evening',['sewing26','sewing33']),
('S23','C5','Needle, thread and spare buttons',['sewing20','sewing22']),
('S24','C6','Tailor fitting a jacket',['tailor45','tailor39','tailor34','tailor9']),
('S25','D2','A dark wool coat outfit',['navycoat11','navycoat24','navycoat1']),
('S26','D3','Brushing a wool coat with a clothes brush',['clothesbrush36','clothesbrush40']),
('S27','D4','A rich, deep coat colour (after)',['coatbutton29','coatbutton31']),
('S28','D5','Lint roller at the door',['lintroller1','lintroller9','lintroller48']),
('S29','E2','Shoes: the first thing that gives an outfit away',['loafers23','loafers20','loafers28']),
('S30','E3','Wiping / polishing leather',['shoepolish0','shoepolish13','shoepolish4']),
('S31','E4','Shoe trees in loafers / shoes kept in shape',['shoetree26','shoetree7','shoetree13']),
('S32','E4b','A pair resting / shoe rotation',['shoetree33','shoetree0']),
('S33','E5','A cobbler replacing a heel',['cobbler4','cobbler41','cobbler42']),
('S34','E6','Cared-for shoes with a simple outfit',['loafers35','loafers45']),
('S35','F3','Night before: outfit chosen and laid out',['outfitlaid40','outfitlaid32']),
('S36','F3','Nails tidied (neutral manicure)',['nails14','nails28','nails35']),
('S37','F5','Loose braid / silk scarf for the night',['silkscarf46','silkscarf15']),
('S38','F6','Calm morning, getting ready',['morning13','morning29','morning46']),
('S39','G2','Full-length mirror check',['mirror12','mirror29','mirror30']),
('S40','G3','Last details: lint, a strap, a tag',['lintroller48','tailor33']),
('S41','G6','Standing tall, walking with ease',['posture9','posture11','camelwalk48']),
('S42','Z3','Ending: elegant women, cared-for clothes',['wardrobe42','coatbutton37','camelwalk46']),
]
rows=[]; pick=[]
for sid,bk,desc,keys in SHOTS:
    for r,k in enumerate(keys):
        c=C[k]; rows.append({'shot':sid,'priority':'first choice' if r==0 else f'alternative {r}','video_time':f"{fmt(B[bk]['s'])}",'narration':B[bk]['text'][:90],'needed_visual':desc,
          'candidate':k,'original_post':c['src_link'],'pinterest_pinner':f"{c['creator']} (@{c['creator_user']})",'pin_title':c['title'],'pin_video_size':f"{c['w']}x{c['h']}",
          'permission_status':'NOT REQUESTED','creator_reply':'','file_received':'','notes':''})
        pick.append((sid,r,k))
with open('PERMISSION-SHORTLIST.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(SHOTS),'shots',len(rows),'candidates',len(set(r['original_post'] for r in rows)),'unique posts')
W,H=150,230; cols=12; n=(len(pick)+cols-1)//cols
sh=Image.new('RGB',(W*cols,(H+18)*n),'white'); d=ImageDraw.Draw(sh)
for j,(sid,r,k) in enumerate(pick):
    c=C[k]; im=Image.open(f"pin/{c['tag']}_{c['i']}.jpg").convert('RGB'); im=im.resize((W,int(im.height*W/im.width))).crop((0,0,W,H))
    X=(j%cols)*W; Y=(j//cols)*(H+18); sh.paste(im,(X,Y+18)); d.text((X+2,Y+3),f"{sid} {'*' if r==0 else r} {k}",fill='red' if r==0 else 'black')
sh.save('PERMISSION-SHORTLIST.jpg',quality=82)
