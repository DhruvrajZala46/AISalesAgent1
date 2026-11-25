// =============== 022: mouth breathing and the face. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_SK='#f7e8d8', C_SK_S='#e9cfb6', C_CAV='#d9605c', C_CAV_D='#b3423f', C_TON='#f2938f', C_PAL='#f3d873', C_ADE='#f59a94', C_BG='#a8736c';
const lim=(d,wd,col)=>`<path d="${d}" fill="none" stroke="${INK}" stroke-width="${wd+7}" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}" fill="none" stroke="${col}" stroke-width="${wd}" stroke-linecap="round" stroke-linejoin="round"/>`;
// the head from the side, facing left: skin, the nose passage on top, the mouth below, the throat going down
const HEAD_D='M300,-140 C262,140 170,330 70,480 C30,530 14,566 40,584 L96,604 C74,622 62,648 82,668 L130,690 L420,960 L410,1500 L900,1500 L900,-140 Z';
const CAV_D='M104,612 C92,480 200,364 380,356 C520,350 612,410 618,520 L650,1500 L486,1500 L470,950 L130,690 Z';
const palD=(k)=>`M100,600 C220,${588-k*70} 400,${592-k*90} 512,${664-k*30} C530,${690-k*20} 506,${702-k*20} 494,${686-k*20} C410,${636-k*90} 230,${632-k*70} 100,638 Z`;
function headScene(){
  DEFS+=`<clipPath id="cavC"><path d="${CAV_D}"/></clipPath>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="${C_BG}"/><g id="hd" transform="translate(64,-52) scale(1.02)">
   <path d="${HEAD_D}" fill="${C_SK}" ${OLW}/><path d="M176,300 q46,-34 100,-10" fill="none" stroke="#3a2a22" stroke-width="15" stroke-linecap="round"/><path d="M204,346 q30,20 62,2" fill="none" stroke="#17171a" stroke-width="7" stroke-linecap="round"/><path d="M52,560 q10,14 28,10" fill="none" ${OLW2}/>
   <path d="M690,300 V1500" stroke="${C_SK_S}" stroke-width="50"/>${[420,560,700,840,980,1120,1260,1400].map(y=>`<ellipse cx="690" cy="${y}" rx="26" ry="40" fill="#f4dc7a" ${OLW2}/>`).join('')}
   <path d="${CAV_D}" fill="${C_CAV}" ${OLW}/>
   <g clip-path="url(#cavC)"><path d="M100,470 C200,340 520,330 640,470" fill="none" stroke="${C_CAV_D}" stroke-width="44"/><path d="M632,560 L668,1500" stroke="${C_CAV_D}" stroke-width="40"/>
    <path d="M520,760 L556,1500" stroke="#f2a09a" stroke-width="54"/>${[900,1010,1120,1230,1340,1450].map(y=>`<ellipse cx="${530+(y-900)*.05}" cy="${y}" rx="11" ry="34" fill="#fbd3cf"/>`).join('')}</g>
   <path d="M180,520 C260,470 420,470 500,560 C440,520 280,512 180,520 Z" fill="#ec8d86" ${OLW2}/>
   <g id="airB"></g>
   <g id="adeW" transform="translate(556,476)"><path d="M-62,10 C-70,-60 -10,-96 34,-70 C74,-46 74,40 40,74 C10,100 -54,70 -62,10 Z" fill="${C_ADE}" ${OLW}/><path d="M-30,-50 q24,-20 50,-6" fill="none" stroke="#fbc4bf" stroke-width="9" stroke-linecap="round"/>
     <g id="aFace" transform="translate(-10,-4)"><g transform="translate(-26,0)">${oEye('ad_eL',24,C_ADE)}</g><g transform="translate(26,0)">${oEye('ad_eR',24,C_ADE)}</g>${brow('ad_bL')}${brow('ad_bR')}<g transform="translate(0,40) scale(1.5)">${mouthEl('ad_m',0,0)}</g>
      <g id="shades"><path d="M-56,-14 H56 V2 C56,22 6,22 4,2 H-4 C-6,22 -56,22 -56,2 Z" fill="#17171a" ${OLW2}/><path d="M-44,-6 l12,10 M12,-6 l12,10" stroke="#fff" stroke-width="4" stroke-linecap="round"/></g></g></g>
   <g id="jaw"><path d="M82,668 C62,690 66,716 92,728 C84,790 96,862 130,902 C190,956 320,972 424,956 L470,1010 L474,860 C380,880 220,880 150,832 L118,720 Z" fill="${C_SK}" ${OLW}/>
    <path id="tongue" d="M134,736 C190,664 380,650 474,706 C536,744 530,826 472,846 C360,880 206,872 152,828 C122,800 118,766 134,736 Z" fill="${C_TON}" ${OLW}/><path d="M176,726 q60,-30 130,-26" fill="none" stroke="#fbc4bf" stroke-width="10" stroke-linecap="round"/>
    <g id="tFace" transform="translate(320,742)" opacity="0"><g transform="translate(-38,0)">${oEye('tg_eL',30,C_TON)}</g><g transform="translate(38,0)">${oEye('tg_eR',30,C_TON)}</g>${brow('tg_bL')}${brow('tg_bR')}<g transform="translate(0,52) scale(1.6)">${mouthEl('tg_m',0,0)}</g></g>
    <g id="ropeT"></g></g>
   <path id="pal" d="${palD(0)}" fill="${C_PAL}" ${OLW}/>
   <g id="pFace" transform="translate(300,596)" opacity="0"><g transform="translate(-38,-22)">${oEye('pl_eL',30,C_PAL)}</g><g transform="translate(38,-22)">${oEye('pl_eR',30,C_PAL)}</g>${brow('pl_bL')}${brow('pl_bR')}<g transform="translate(0,26) scale(1.5)">${mouthEl('pl_m',0,0)}</g></g>
   <g id="ropeP"></g>
   <g id="airF"></g>
   <g id="xmark" opacity="0" transform="translate(470,470)"><circle r="46" fill="#e8473f" stroke="#1d2a44" stroke-width="5"/><path d="M-20,-20 L20,20 M20,-20 L-20,20" stroke="#fff" stroke-width="12" stroke-linecap="round"/></g></g>`;}
// one air bubble with a face
function bubbleSVG(id){return `<g id="${id}"><circle r="46" fill="#fff" opacity=".55" ${OLW2}/><circle r="46" fill="none" ${OLW2}/><path d="M-28,-22 q10,-14 24,-14" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>
   <g transform="translate(-17,-4)">${oEye(id+'_eL',17,'#fff')}</g><g transform="translate(17,-4)">${oEye(id+'_eR',17,'#fff')}</g>${brow(id+'_bL')}${brow(id+'_bR')}<g transform="translate(0,24) scale(1.2)">${mouthEl(id+'_m',0,0)}</g></g>`;}
// ---- the end: the mirror, then the doctor ----
function mirrorScene(){const row=(id,y,col,txt)=>`<g id="${id}" opacity="0"><rect x="60" y="${y}" width="600" height="66" rx="14" fill="${col}" stroke="#1d2a44" stroke-width="4"/><text x="360" y="${y+46}" text-anchor="middle" style="font-family:LG,sans-serif;font-size:31px;letter-spacing:.5px" fill="#fff">${txt}</text></g>`;
  return `<rect x="-60" y="-60" width="840" height="1400" fill="#dfeaf0"/><path d="M-60,1040 H780 V1400 H-60 Z" fill="#a9a5a8"/><path d="M-60,1040 H780 M-60,1150 H780 M180,1040 L120,1340 M420,1040 L420,1340 M640,1040 L700,1340" stroke="#8c888c" stroke-width="3" fill="none"/>
   <g id="brd" opacity="0"><rect x="36" y="46" width="660" height="424" rx="24" fill="#000" opacity=".12"/><rect x="28" y="36" width="660" height="424" rx="24" fill="#fff" stroke="#1d2a44" stroke-width="5"/>
   <text x="360" y="104" text-anchor="middle" style="font-family:LG,sans-serif;font-size:42px;letter-spacing:1px" fill="#1d2a44">YEARS OF MOUTH BREATHING</text>
   ${row('b0',128,'#e8473f','1. LONG FACE')}${row('b1',206,'#8a5bd1','2. NARROW JAW')}${row('b2',284,'#2f8fe0','3. CROWDED TEETH')}${row('b3',362,'#2fae62','NOSE ALWAYS BLOCKED? GET IT CHECKED')}</g>
   <g id="docW"><g transform="translate(150,470) scale(.9)">${doctorSVG()}</g></g>
   <g id="patW"><g transform="translate(560,470) scale(.9)">${patientSVG()}</g>
    <g id="mirror"><path d="M0,60 L24,300" stroke="${INK}" stroke-width="34" stroke-linecap="round"/><path d="M0,60 L24,300" stroke="#6b452c" stroke-width="26" stroke-linecap="round"/><ellipse cx="-10" cy="-60" rx="110" ry="132" fill="#6b452c" ${OLW}/><ellipse cx="-10" cy="-60" rx="88" ry="110" fill="#5a3823"/></g></g>`;}
