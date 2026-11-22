# Builds scene.html for 007: the 001 engine helpers + code-drawn characters (chars.js) + the scene (parts_v7.js). No image model.
L=open('../001-earwax-cotton-buds/scene.html').read().split('\n')
head='\n'.join(L[0:69]).replace('<script src="data.js"></script>','<script src="data.js"></script><script src="art/meta.js"></script>')
labelbox=L[140]; viseme='\n'.join(L[310:322])+'\n'+L[416]
pt=open('parts_v7.js').read().replace('//__VISEME__',viseme)
open('scene.html','w').write(head+'\n'+labelbox+'\n'+open('chars.js').read()+'\n'+open('plate_skin.js').read()+'\n'+pt+'\n</script></body></html>\n'); print('ok')
