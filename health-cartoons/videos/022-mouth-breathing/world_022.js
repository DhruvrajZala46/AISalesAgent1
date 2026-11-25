// =============== 022: mouth breathing and the face. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_SK='#f7e8d8', C_SK_S='#e9cfb6', C_CAV='#d9605c', C_CAV_D='#b3423f', C_TON='#f2938f', C_PAL='#f3d873', C_ADE='#f59a94', C_BG='#a8736c';
const lim=(d,wd,col)=>`<path d="${d}" fill="none" stroke="${INK}" stroke-width="${wd+7}" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}" fill="none" stroke="${col}" stroke-width="${wd}" stroke-linecap="round" stroke-linejoin="round"/>`;
// the head from the side, facing left: skin, the nose passage on top, the mouth below, the throat going down
const HEAD_D='M344,-140 C300,60 240,200 176,304 C130,380 70,440 34,490 C12,520 20,542 50,550 L98,566 C72,588 50,610 54,638 C56,666 76,684 106,700 L160,716 L430,1000 L392,1500 L900,1500 L900,-140 Z';
const CAV_D='M112,580 C98,470 190,332 330,322 C476,312 606,352 628,474 L648,1500 L474,1500 L470,1000 L160,716 L112,694 Z';
const palD=(k)=>`M108,604 C230,${590-k*70} 410,${596-k*90} 520,${672-k*30} C538,${700-k*20} 512,${712-k*20} 500,${694-k*20} C416,${640-k*90} 236,${636-k*70} 108,642 Z`;
function headScene(){
  DEFS+=`<clipPath id="cavC"><path d="${CAV_D}"/></clipPath>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="${C_BG}"/><g id="hd">
   <path d="${HEAD_D}" fill="${C_SK}" ${OLW}/><path d="M60,548 q14,-22 34,-6" fill="none" ${OLW2}/>
   <path d="M690,300 V1500" stroke="${C_SK_S}" stroke-width="50"/>${[420,560,700,840,980,1120,1260,1400].map(y=>`<ellipse cx="690" cy="${y}" rx="26" ry="40" fill="#f4dc7a" ${OLW2}/>`).join('')}
   <path d="${CAV_D}" fill="${C_CAV}" ${OLW}/>
   <g clip-path="url(#cavC)"><path d="M100,470 C200,340 520,330 640,470" fill="none" stroke="${C_CAV_D}" stroke-width="44"/><path d="M632,560 L668,1500" stroke="${C_CAV_D}" stroke-width="40"/>
    <path d="M596,700 L612,1500" stroke="#c9534f" stroke-width="40"/><path d="M520,800 L548,1500" stroke="#f2a09a" stroke-width="56"/><path d="M492,800 L520,1500 M548,800 L576,1500" stroke="${INK}" stroke-width="2.6" fill="none"/>${[900,1010,1120,1230,1340,1450].map(y=>`<ellipse cx="${530+(y-900)*.05}" cy="${y}" rx="11" ry="34" fill="#fbd3cf"/>`).join('')}</g>
   <path d="M180,520 C260,470 420,470 500,560 C440,520 280,512 180,520 Z" fill="#ec8d86" ${OLW2}/>
   <g id="airB"></g>
   <g id="adeW" transform="translate(556,476)"><path d="M-62,10 C-70,-60 -10,-96 34,-70 C74,-46 74,40 40,74 C10,100 -54,70 -62,10 Z" fill="${C_ADE}" ${OLW}/><path d="M-30,-50 q24,-20 50,-6" fill="none" stroke="#fbc4bf" stroke-width="9" stroke-linecap="round"/>
     <g id="aFace" transform="translate(-10,-4)"><g transform="translate(-26,0)">${oEye('ad_eL',24,C_ADE)}</g><g transform="translate(26,0)">${oEye('ad_eR',24,C_ADE)}</g>${brow('ad_bL')}${brow('ad_bR')}<g transform="translate(0,40) scale(1.5)">${mouthEl('ad_m',0,0)}</g>
      <g id="shades"><path d="M-56,-14 H56 V2 C56,22 6,22 4,2 H-4 C-6,22 -56,22 -56,2 Z" fill="#17171a" ${OLW2}/><path d="M-44,-6 l12,10 M12,-6 l12,10" stroke="#fff" stroke-width="4" stroke-linecap="round"/></g></g></g>
   <path d="M112,650 h24 q8,0 8,10 v34 q0,8 -8,8 h-18 Z" fill="#fff" ${OLW2}/>
   <g id="jaw"><path d="M106,706 C78,716 60,736 66,758 C70,774 86,782 98,788 C86,832 92,892 114,932 C138,974 192,1002 262,1018 C332,1032 392,1012 424,982 L474,1044 L506,884 C404,904 254,894 172,852 C142,822 132,772 156,722 Z" fill="${C_SK}" ${OLW}/>
    <path d="M118,722 h22 q8,0 8,10 v30 h-30 Z" fill="#fff" ${OLW2}/><path d="M200,900 q80,40 190,30 M230,940 q70,26 150,16" fill="none" stroke="${C_SK_S}" stroke-width="6" stroke-linecap="round"/>
    <path id="tongue" d="M152,776 C140,744 168,716 204,720 C250,668 380,650 480,696 C560,734 566,820 500,846 C400,878 250,872 186,836 C160,822 152,800 152,776 Z" fill="${C_TON}" ${OLW}/><path d="M214,734 q70,-36 150,-30" fill="none" stroke="#fbc4bf" stroke-width="10" stroke-linecap="round"/><circle cx="186" cy="760" r="5" fill="#d9605c"/><circle cx="204" cy="776" r="4" fill="#d9605c"/>
    <g id="tFace" transform="translate(320,742)" opacity="0"><g transform="translate(-38,0)">${oEye('tg_eL',30,C_TON)}</g><g transform="translate(38,0)">${oEye('tg_eR',30,C_TON)}</g>${brow('tg_bL')}${brow('tg_bR')}<g transform="translate(0,52) scale(1.6)">${mouthEl('tg_m',0,0)}</g></g>
    <g id="ropeT"></g></g>
   <path id="pal" d="${palD(0)}" fill="${C_PAL}" ${OLW}/>
   <g id="pFace" transform="translate(300,596)" opacity="0"><g transform="translate(-38,-22)">${oEye('pl_eL',30,C_PAL)}</g><g transform="translate(38,-22)">${oEye('pl_eR',30,C_PAL)}</g>${brow('pl_bL')}${brow('pl_bR')}<g transform="translate(0,26) scale(1.5)">${mouthEl('pl_m',0,0)}</g></g>
   <g id="ropeP"></g>
   <g id="airF"></g>
   <g id="xmark" opacity="0" transform="translate(470,470)"><circle r="46" fill="#e8473f" stroke="#1d2a44" stroke-width="5"/><path d="M-20,-20 L20,20 M20,-20 L-20,20" stroke="#fff" stroke-width="12" stroke-linecap="round"/></g></g>${headCard()}`;}
function headCard(){return `<g id="inset"><rect x="14" y="1010" width="196" height="256" rx="18" fill="#fff" ${OLW}/>
   <path d="M70,1200 C60,1160 52,1120 60,1090 C70,1050 110,1030 146,1040 C180,1050 190,1090 184,1130 C180,1160 170,1190 172,1214 L96,1214 C92,1206 84,1204 70,1200 Z" fill="${PSK}" ${OLW2}/><path d="M62,1090 C70,1040 150,1020 184,1070 C190,1090 190,1110 184,1126 C170,1090 130,1070 96,1076 C80,1080 68,1084 62,1090 Z" fill="#1f1d24" ${OLW2}/>
   <path d="M60,1124 l-14,22 l16,6 M78,1118 q8,6 16,0" fill="none" ${OLW2}/><path d="M56,1166 q10,6 20,2" fill="none" ${OLW2}/>
   <rect id="ring" x="40" y="1108" width="84" height="80" rx="12" fill="#e02626" fill-opacity=".18" stroke="#e02626" stroke-width="6"/>
   <text x="112" y="1250" text-anchor="middle" style="font-family:LG,sans-serif;font-size:19px" fill="#1d2a44">INSIDE THE HEAD</text></g>`;}
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
