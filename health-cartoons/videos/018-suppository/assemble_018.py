# 018: 001 engine (helpers, eyes, mouths, visemes, the code doctor = Dr. Mira and the patient) + world_018.js + parts_018.js
L=open('../001-earwax-cotton-buds/scene.html').read().split('\n')
head='\n'.join(L[0:69]).replace('@font-face{font-family:LG;src:url(../../assets/fonts/LuckiestGuy.woff2)}','@font-face{font-family:LG;src:url(../../assets/fonts/LuckiestGuy.woff2)}@font-face{font-family:ComicNeue;font-weight:700;src:url(../../assets/fonts/comic-neue-latin-700-normal.woff2)}')
assert 'ComicNeue' in head
labelbox=L[140]; clinic='\n'.join(L[144:257]); viseme='\n'.join(L[310:322])+'\n'+L[416]
def rep(s,a,b):
    assert s.count(a)==1,(s.count(a),a[:80]); return s.replace(a,b)
clinic=clinic[:clinic.index('function earPoster(){')]
k=clinic.index('<g transform="translate(66,316) rotate(-30)">'); k2=clinic.index('</g>',clinic.index('<path d="M-4,-26 L4,-26',k))+4
clinic=clinic[:k]+clinic[k2:]                                   # no otoscope
clinic=rep(clinic,"${shaded(limbD([[-86,226],[-104,350],[-72,440]],[40,34,30]),'#f8f8f6','#d4d9dd',10)}\n <g transform=\"translate(-58,450) rotate(-12)\">",
  "${shaded(limbD([[-86,226],[-74,336],[-6,352]],[40,34,30]),'#f8f8f6','#d4d9dd',10)}\n <g transform=\"translate(8,316) rotate(-8)\">")   # clipboard at the chest
clinic=rep(clinic,"${hand(-60,452,-20,1.15,DSK)}","${hand(-2,356,-70,1.15,DSK)}")
clinic=rep(clinic,"<g id=\"docArmR\">${shaded(limbD([[86,226],[108,350],[72,330]],[40,34,30]),'#f8f8f6','#d4d9dd',10)}","<g id=\"docArmR\">${shaded(limbD([[86,226],[110,318],[96,346]],[40,34,30]),'#f8f8f6','#d4d9dd',10)}")
clinic=rep(clinic,"${hand(68,330,-30,1.15,DSK)}","${hand(98,350,-60,1.15,DSK)}")
clinic=rep(clinic,"  ${mouthEl('pat_m',-4,138)}","  ${mouthEl('pat_m',-4,138)}\n  <g id=\"patBlush\" opacity=\"0\"><ellipse cx=\"-38\" cy=\"124\" rx=\"10\" ry=\"6\" fill=\"#ef8f86\"/><ellipse cx=\"32\" cy=\"124\" rx=\"10\" ry=\"6\" fill=\"#ef8f86\"/></g>\n  <path id=\"pSweat\" d=\"M0,-9 C5,-2 7,3 5,7 C3,11 -4,11 -5,7 C-7,3 -4,-2 0,-9Z\" fill=\"#9fd8f5\" ${LN2}/>")
pt=open('parts_018.js').read().replace('//__VISEME__',viseme)
out=head+'\n'+labelbox+'\n'+open('world_018.js').read()+'\n'+clinic+'\n'+pt+'\n</script></body></html>\n'
open('scene.html','w').write(out); print('ok',len(out))
