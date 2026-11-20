# Builds scene.html for 002 from the 001 engine (helpers, eyes, mouths, clinic, visemes) plus this video's parts.
L=open('../001-earwax-cotton-buds/scene.html').read().split('\n')
head='\n'.join(L[0:69])
labelbox=L[140]
clinic='\n'.join(L[144:257])
viseme='\n'.join(L[310:322])+'\n'+L[416]
def rep(s,a,b):
    assert s.count(a)==1,(s.count(a),a[:80]); return s.replace(a,b)
i=clinic.index('function earPoster(){'); j=clinic.index('</g>`;}',i)+len('</g>`;}')
clinic=clinic[:i]+'''function stomachPoster(){return `<g transform="translate(560,250)"><rect x="-92" y="-118" width="184" height="236" fill="#fbfaf7" ${LN}/><rect x="-80" y="-106" width="160" height="182" fill="#f6ece8"/>
  <path d="M-36,-80 C-34,-60 -30,-50 -20,-46 C10,-60 50,-40 48,0 C46,40 10,64 -24,58 C-40,56 -50,50 -56,44 L-60,52 L-66,40 C-50,30 -36,20 -32,0 C-30,-20 -40,-40 -46,-80 Z" fill="#ec9aa0" ${LN2}/>
  <path d="M-10,-30 q20,10 10,30 q-10,20 10,30" fill="none" ${TH('#c45f69')}/>
  <rect x="-62" y="86" width="124" height="10" rx="3" fill="#d9a3a7"/><rect x="-44" y="100" width="88" height="8" rx="3" fill="#ecc8ca"/></g>`;}'''+clinic[j:]
clinic=rep(clinic,'${earPoster()}','${stomachPoster()}')
k=clinic.index('<g transform="translate(66,316) rotate(-30)">'); k2=clinic.index('</g>',clinic.index('L2 -44 L-2 -44',k) if 'L2 -44 L-2 -44' in clinic else clinic.index('<path d="M-4,-26 L4,-26',k))+4
clinic=clinic[:k]+clinic[k2:]
clinic=rep(clinic,'<use href="#world" transform="scale(.82) translate(-395,-648)"/>','<use href="#world" transform="scale(.6) translate(-370,-800)"/>')
a=clinic.index(" ${labelBox('lbImp'"); b=clinic.index('</g>`;',a)
clinic=clinic[:a]+''' ${labelBox('lbBez','BEZOAR',360,64,30)}
 <g id="lbMyth" opacity="0" transform="translate(360,64)"><rect x="-150" y="-26" width="300" height="52" fill="#fff" ${LN}/><circle cx="-118" cy="0" r="17" fill="#e0454f" ${LN2}/><path d="M-125,-7 L-111,7 M-111,-7 L-125,7" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><text class="lbl" style="font-size:27px" x="16" y="9" text-anchor="middle">7-YEAR MYTH</text></g>
'''+clinic[b:]
pw=open('parts_world.js').read(); pf=open('parts_face.js').read(); pt=open('parts_timing.js').read().replace('//__VISEME__',viseme)
assemble='''// =============== assemble ===============
const svg=$('S');
const body=S1+S3+SL+S2+SX+SG+`<rect id="indark" width="720" height="1280" fill="#2a1312" opacity="0"/><g id="capg"><text id="cap" class="cap" x="360" y="1110" text-anchor="middle"></text></g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter><filter id="soft2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="10"/></filter><filter id="soft3" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
 <linearGradient id="gSto" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f8cdcb"/><stop offset="1" stop-color="#eda3a7"/></linearGradient>
 <radialGradient id="gGum" cx=".38" cy=".32" r=".8"><stop offset="0" stop-color="#ffc4dc"/><stop offset=".55" stop-color="#f58fb9"/><stop offset="1" stop-color="#d9608f"/></radialGradient>
 <radialGradient id="gBub" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#ffd6e7"/><stop offset=".7" stop-color="#f7a1c4"/><stop offset="1" stop-color="#e57aa6"/></radialGradient>
 ${DEFS}</defs>`+body;
'''
out=head+'\n'+labelbox+'\n'+pw+'\n'+clinic+'\n'+pf+'\n'+assemble+'\n'+pt+'\n</script></body></html>\n'
open('scene.html','w').write(out); print('ok', len(out))
