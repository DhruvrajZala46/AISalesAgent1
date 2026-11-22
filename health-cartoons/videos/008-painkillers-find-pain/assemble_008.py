# 008: ALL code in the 001 / 003-v1 style (the user's references). 001 engine + 001 code clinic + chars.js + world_008.js + parts_008.js.
L=open('../001-earwax-cotton-buds/scene.html').read().split('\n')
head='\n'.join(L[0:69]); labelbox=L[140]; clinic='\n'.join(L[144:257]); viseme='\n'.join(L[310:322])+'\n'+L[416]
def rep(s,a,b):
    assert s.count(a)==1,(s.count(a),a[:80]); return s.replace(a,b)
i=clinic.index('function earPoster(){'); j=clinic.index('</g>`;}',i)+len('</g>`;}'); clinic=clinic[:i]+clinic[j:]
clinic=rep(clinic,'${earPoster()}','${painPoster()}')
k=clinic.index('<g transform="translate(66,316) rotate(-30)">'); k2=clinic.index('</g>',clinic.index('<path d="M-4,-26 L4,-26',k))+4
clinic=clinic[:k]+clinic[k2:]                                   # no otoscope
clinic=rep(clinic,'<circle cx="-60" cy="118" r="13" fill="#fff" ${LN2}/><circle cx="-48" cy="146" r="8" fill="#fff" ${LN2}/>','')
clinic=rep(clinic,'<use href="#world" transform="scale(.82) translate(-395,-648)"/>',
  '<use id="bubA" href="#wCut" transform="scale(.42) translate(-440,-820)"/><use id="bubB" href="#wFork" transform="scale(.36) translate(-360,-760)"/>')
clinic=rep(clinic,'let S2=`<g id="s2"><g id="ccam">','let S5=`<g id="s5"><g id="ccam">')
a=clinic.index(" ${labelBox('lbImp'"); b=clinic.index('</g>`;',a)
clinic=clinic[:a]+''' ${labelBox('lbPro','PROSTAGLANDINS',360,64,26)}
 <g id="lbTip" opacity="0" transform="translate(360,84)"><rect x="-300" y="-44" width="600" height="88" fill="#fff" ${LN}/><circle cx="-264" cy="-14" r="15" fill="#2fa36b" ${LN2}/><path d="M-272,-14 l6,6 l11,-12" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  <text class="lbl" style="font-size:22px" x="20" y="-6" text-anchor="middle">PAINKILLERS DON'T HEAL THE WOUND</text><text class="lbl" style="font-size:22px" x="0" y="28" text-anchor="middle" fill="#e0454f">THEY TURN THE PAIN SIGNAL DOWN</text></g>
'''+clinic[b:]
clinic=rep(clinic,"  ${mouthEl('pat_m',-4,138)}","  ${mouthEl('pat_m',-4,138)}\n  <g id=\"patBlush\" opacity=\"0\"><ellipse cx=\"-38\" cy=\"124\" rx=\"10\" ry=\"6\" fill=\"#ef8f86\"/><ellipse cx=\"32\" cy=\"124\" rx=\"10\" ry=\"6\" fill=\"#ef8f86\"/></g>\n  <path id=\"pSweat\" d=\"M0,-9 C5,-2 7,3 5,7 C3,11 -4,11 -5,7 C-7,3 -4,-2 0,-9Z\" fill=\"#9fd8f5\" ${LN2}/>")
# the hurt foot: a bandage wrapped over his right shoe
clinic=rep(clinic,'<path d="M8,766 h58" ${TH(\'#9aa0a6\')}/>','<path d="M8,766 h58" ${TH(\'#9aa0a6\')}/><path d="M4,742 C16,724 64,726 72,744 L74,774 L4,774Z" fill="#fbf7ef" ${LN2}/><path d="M10,736 l60,14 M6,752 l66,10 M8,766 l64,4" ${TH(\'#d9cfc4\')} stroke-width="2.6"/><circle cx="56" cy="748" r="4" fill="#d6404a" opacity=".5"/>')
pt=open('parts_008.js').read().replace('//__VISEME__',viseme)
out=head+'\n'+labelbox+'\n'+open('chars.js').read()+'\n'+open('world_008.js').read()+'\n'+clinic+'\n'+pt+'\n</script></body></html>\n'
open('scene.html','w').write(out); print('ok',len(out))
