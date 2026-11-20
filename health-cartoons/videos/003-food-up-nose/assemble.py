# Builds scene.html for 003 from the 001 engine (helpers, eyes, mouths, clinic, visemes) plus this video's parts.
L=open('../001-earwax-cotton-buds/scene.html').read().split('\n')
head='\n'.join(L[0:69]); labelbox=L[140]; clinic='\n'.join(L[144:257]); viseme='\n'.join(L[310:322])+'\n'+L[416]
def rep(s,a,b):
    assert s.count(a)==1,(s.count(a),a[:80]); return s.replace(a,b)
pc=open('parts_clinic.js').read(); mk=pc.split('//__CODE__')[0].replace('//__MARKUP__',''); code=pc.split('//__CODE__')[1]
i=clinic.index('function earPoster(){'); j=clinic.index('</g>`;}',i)+len('</g>`;}'); clinic=clinic[:i]+clinic[j:]
clinic=rep(clinic,'${earPoster()}','${nosePoster()}')
k=clinic.index('<g transform="translate(66,316) rotate(-30)">'); k2=clinic.index('</g>',clinic.index('L2 -44 L-2 -44',k) if 'L2 -44 L-2 -44' in clinic else clinic.index('<path d="M-4,-26 L4,-26',k))+4
clinic=clinic[:k]+clinic[k2:]
clinic=rep(clinic,'<circle cx="-60" cy="118" r="13" fill="#fff" ${LN2}/><circle cx="-48" cy="146" r="8" fill="#fff" ${LN2}/>','')
clinic=rep(clinic,'<use href="#world" transform="scale(.82) translate(-395,-648)"/>','<use href="#world" transform="scale(.47) translate(-315,-470)"/>')
a=clinic.index(" ${labelBox('lbImp'"); b=clinic.index('</g>`;',a)
clinic=clinic[:a]+''' ${labelBox('lbReg','NASAL REGURGITATION',360,64,26)}
 <g id="lbTip" opacity="0" transform="translate(360,64)"><rect x="-200" y="-24" width="400" height="48" fill="#fff" ${LN}/><circle cx="-170" cy="0" r="15" fill="#f0a020" ${LN2}/><path d="M-170,-8 v9 M-170,7 v1" stroke="#fff" stroke-width="4" stroke-linecap="round"/><text class="lbl" style="font-size:20px" x="26" y="8" text-anchor="middle">HAPPENS OFTEN? GET CHECKED</text></g>
'''+clinic[b:]
clinic=rep(clinic,"  ${mouthEl('pat_m',-4,138)}","  ${mouthEl('pat_m',-4,138)}\n  <g id=\"patBlush\" opacity=\"0\"><ellipse cx=\"-38\" cy=\"124\" rx=\"10\" ry=\"6\" fill=\"#ef8f86\"/><ellipse cx=\"32\" cy=\"124\" rx=\"10\" ry=\"6\" fill=\"#ef8f86\"/></g>\n  <path id=\"pnO\" fill=\"none\" stroke=\"${INK}\" stroke-width=\"10\" stroke-linecap=\"round\"/><path id=\"pnF\" fill=\"none\" stroke=\"#f6d27a\" stroke-width=\"6.5\" stroke-linecap=\"round\"/>")
pw=open('parts_world.js').read()
pt=open('parts_timing.js').read().replace('//__VISEME__',viseme).replace('//__CLINIC__',code).replace('//__STING__','')
assemble='''// =============== assemble ===============
const svg=$('S');
const body=S1+S2+SG+`<rect id="indark" width="720" height="1280" fill="#1e1012" opacity="0"/><g id="capg"><text id="cap" class="cap" x="360" y="1110" text-anchor="middle"></text></g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter><filter id="soft2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="10"/></filter><filter id="soft3" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
 ${DEFS}</defs>`+body;
'''
out=head+'\n'+labelbox+'\n'+pw+'\n'+clinic+'\n'+mk+'\n'+assemble+'\n'+pt+'\n</script></body></html>\n'
open('scene.html','w').write(out); print('ok',len(out))
