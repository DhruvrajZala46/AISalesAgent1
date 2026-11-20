# Builds brand.html (channel DP + banner) from the 001 engine (helpers, doctor) and the 003 brain drawing.
import re
L=open('../videos/001-earwax-cotton-buds/scene.html').read().split('\n')
i0=[i for i,l in enumerate(L) if '=============== helpers' in l][0]
helpers='\n'.join(L[i0:69]); labelbox=L[140]
clinic='\n'.join(L[144:257])
a=clinic.index('function doctorSVG(){'); b=clinic.index('const PSK=')
doc=clinic[a:b]
# brand pose: right arm raised in a wave instead of holding the otoscope
k=doc.index('<g id="docArmR">'); k2=doc.index('</g>\n</g>`;}',k)
doc=doc[:k]+'''<g id="docArmR">${shaded(limbD([[86,226],[134,170],[128,86]],[40,34,30]),'#f8f8f6','#d4d9dd',10)}${hand(128,74,170,1.25,DSK)}'''+doc[k2:]
hum='\n'.join(L[145:156])
pw=open('../videos/003-food-up-nose/parts_world.js').read()
brain=pw[pw.index('function brainD('):pw.index("let W=`<g id=\"world\">")]
html=open('brand_tpl.html').read().replace('//__ENGINE__',helpers+'\n'+labelbox+'\n'+hum+'\n'+doc+'\n'+brain)
open('brand.html','w').write(html); print('ok',len(html))
