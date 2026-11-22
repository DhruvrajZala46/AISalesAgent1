# Channel art for the new channel (avatar 800x800, banner 2560x1440), drawn in code with 001's female doctor.
# Usage: python3 make_brand.py && node render_brand.js   -> avatar.png, banner.png (media: not committed)
L=open('../videos/001-earwax-cotton-buds/scene.html').read().split('\n')
head='\n'.join(L[0:69]).replace('@font-face{font-family:LG;src:url(../../assets/fonts/LuckiestGuy.woff2)}',
  '@font-face{font-family:LG;src:url(../assets/fonts/LuckiestGuy.woff2)}@font-face{font-family:ComicNeue;font-weight:700;src:url(../assets/fonts/comic-neue-latin-700-normal.woff2)}')
clinic='\n'.join(L[144:257]); clinic=clinic[:clinic.index('function earPoster(){')]
k=clinic.index('<g transform="translate(66,316) rotate(-30)">'); k2=clinic.index('</g>',clinic.index('<path d="M-4,-26 L4,-26',k))+4
clinic=clinic[:k]+clinic[k2:]                                    # no otoscope
viseme='\n'.join(L[310:322])+'\n'+L[416]
art=r'''
const TEAL='#14a3a0', TEAL_D='#0b6e6b', MINT='#e8f7f5', CORAL='#ff7a66';
function plusPattern(w,h,n){let s='';for(let i=0;i<n;i++){const x=(i*397)%w, y=(i*211)%h, r=10+(i%4)*6;
  s+=`<path d="M${x-r},${y-r/3} h${r*2/3} v-${r*2/3} h${r*2/3} v${r*2/3} h${r*2/3} v${r*2/3} h-${r*2/3} v${r*2/3} h-${r*2/3} v-${r*2/3} h-${r*2/3}Z" fill="#fff" opacity=".10"/>`;}return s;}
window.drawAvatar=function(){const S=$('S');S.setAttribute('width',800);S.setAttribute('height',800);S.setAttribute('viewBox','0 0 800 800');
  DEFS='';const doc=doctorSVG();
  S.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}
   <radialGradient id="bgA" cx="50%" cy="40%" r="70%"><stop offset="0" stop-color="#3cc7c2"/><stop offset="1" stop-color="${TEAL_D}"/></radialGradient><clipPath id="circ"><circle cx="400" cy="400" r="400"/></clipPath></defs>
   <g><rect width="800" height="800" fill="url(#bgA)"/>${plusPattern(800,800,28)}
   <g transform="translate(400,120) scale(2.75)">${doc}</g></g>`;
  setMouthV('doc_m',0,10,.8,0,5); setHEye('dEyeL',3,0); setHEye('dEyeR',3,0);};
window.drawBanner=function(){const S=$('S');S.setAttribute('width',2560);S.setAttribute('height',1440);S.setAttribute('viewBox','0 0 2560 1440');
  DEFS='';const doc=doctorSVG();
  S.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}
   <linearGradient id="bgB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2bbdb8"/><stop offset="1" stop-color="${TEAL_D}"/></linearGradient>
   <clipPath id="safe"><rect x="0" y="508" width="2560" height="423"/></clipPath></defs>
   <rect width="2560" height="1440" fill="url(#bgB)"/>${plusPattern(2560,1440,90)}
   <text x="640" y="705" style="font-family:LG,sans-serif;font-size:118px;paint-order:stroke;stroke:#0a3f3d;stroke-width:16px;stroke-linejoin:round" fill="#fff">HI, I'M DR. MIRA!</text>
   <text x="646" y="800" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:58px" fill="${MINT}">Your body, explained in 60 funny seconds.</text>
   <rect x="646" y="836" width="430" height="64" rx="32" fill="${CORAL}"/><text x="861" y="880" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:38px" fill="#fff">New Shorts every day</text>
   <g clip-path="url(#safe)"><g transform="translate(1900,520) scale(1.38)">${doc}</g></g>
   <rect x="0" y="928" width="2560" height="6" fill="#fff" opacity=".0"/>`;
  setMouthV('doc_m',0,10,.8,0,5); setHEye('dEyeL',3,0); setHEye('dEyeR',3,0);};
'''
out=head+'\n'+clinic+'\n'+viseme+'\n'+art+'\n</script></body></html>\n'
open('brand.html','w').write(out); print('ok',len(out))
