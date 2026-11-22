# 009: ALL code, our 001 / 003-v1 style: 001 engine (helpers, eyes, mouths, the patient), chars.js (gloves), world_009.js, parts_009.js.
L=open('../001-earwax-cotton-buds/scene.html').read().split('\n')
head='\n'.join(L[0:69]).replace('@font-face{font-family:LG;src:url(../../assets/fonts/LuckiestGuy.woff2)}','@font-face{font-family:LG;src:url(../../assets/fonts/LuckiestGuy.woff2)}@font-face{font-family:ComicNeue;font-weight:700;src:url(../../assets/fonts/comic-neue-latin-700-normal.woff2)}@font-face{font-family:Merri;font-weight:900;src:url(../../assets/fonts/merriweather-latin-900-normal.woff2)}'); labelbox=L[140]; clinic='\n'.join(L[144:257]); viseme='\n'.join(L[310:322])+'\n'+L[416]
def rep(s,a,b):
    assert s.count(a)==1,(s.count(a),a[:80]); return s.replace(a,b)
clinic=rep(clinic,"  ${mouthEl('pat_m',-4,138)}","  ${mouthEl('pat_m',-4,138)}\n  <g id=\"patBlush\" opacity=\"0\"><ellipse cx=\"-38\" cy=\"124\" rx=\"12\" ry=\"7\" fill=\"#ef6f66\"/><ellipse cx=\"32\" cy=\"124\" rx=\"12\" ry=\"7\" fill=\"#ef6f66\"/></g>\n  <path id=\"pSweat\" d=\"M0,-9 C5,-2 7,3 5,7 C3,11 -4,11 -5,7 C-7,3 -4,-2 0,-9Z\" fill=\"#9fd8f5\" ${LN2}/>")
clinic=rep(clinic,'let S2=`<g id="s2"><g id="ccam">','let S_CLINIC_UNUSED=`<g id="s2x"><g id="ccamx">')
pt=open('parts_009.js').read().replace('//__VISEME__',viseme)
out=head+'\n'+labelbox+'\n'+open('chars.js').read()+'\n'+open('world_009.js').read()+'\n'+clinic+'\n'+pt+'\n</script></body></html>\n'
open('scene.html','w').write(out); print('ok',len(out))
