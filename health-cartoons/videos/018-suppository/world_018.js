// =============== 018: how a suppository fixes constipation. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_STEEL='#c3cad3', C_TEAL='#14a3a0', C_GLOVE='#2f8fe0', C_GLOVE_S='#1c6cba';
const OUT_D='M226,330 C226,150 300,56 430,56 L800,56 L800,334 L504,334 L504,560 C504,700 446,760 424,830 L404,905 L316,905 L296,830 C274,760 226,700 226,560 Z';
const LUM_D='M256,330 C256,172 322,86 430,86 L800,86 L800,304 L474,304 L474,560 C474,690 422,750 398,830 L386,905 L334,905 L322,830 C298,750 256,690 256,560 Z';
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
// a stool lump: a bumpy blob; hard = dark, cracked; soft = lighter, glossy
function lump(id,r,face){const n=9,pts=Array.from({length:n},(_,i)=>{const a=i/n*6.283,rr=r*(.82+rnd(i+r)*.3);return [Math.cos(a)*rr*1.15,Math.sin(a)*rr*.9];});
  let d='M'+pts.map((p,i)=>{const q=pts[(i+1)%n];return `${((p[0]+q[0])/2).toFixed(1)},${((p[1]+q[1])/2).toFixed(1)} Q${q[0].toFixed(1)},${q[1].toFixed(1)}`;}).join(' ');
  const q0=pts[0],q1=pts[1];d=`M${((q0[0]+q1[0])/2).toFixed(1)},${((q0[1]+q1[1])/2).toFixed(1)} `+pts.map((_,i)=>{const p=pts[(i+1)%n],q=pts[(i+2)%n];return `Q${p[0].toFixed(1)},${p[1].toFixed(1)} ${((p[0]+q[0])/2).toFixed(1)},${((p[1]+q[1])/2).toFixed(1)}`;}).join(' ')+'Z';
  return `<g id="${id}"><g id="${id}_s"><path id="${id}_p" d="${d}" fill="#6b3a1c" ${OLW}/><path d="M${-r*.6},${r*.3} q${r*.5},${r*.4} ${r*1.1},${r*.1}" fill="none" stroke="#3f200d" stroke-width="7" stroke-linecap="round" opacity=".5"/>
    <g id="${id}_cr"><path d="M${-r*.5},${-r*.5} l${r*.25},${r*.3} l${-r*.1},${r*.3} M${r*.4},${-r*.4} l${-r*.2},${r*.3} l${r*.15},${r*.25} M${r*.1},${r*.45} l${r*.2},${-r*.2}" fill="none" stroke="#2c1608" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>
    <g id="${id}_gl" opacity="0"><ellipse cx="${-r*.35}" cy="${-r*.4}" rx="${r*.28}" ry="${r*.13}" fill="#fff" opacity=".55"/><circle cx="${r*.45}" cy="${-r*.3}" r="${r*.08}" fill="#fff" opacity=".5"/></g>
    ${face?`<g transform="translate(0,${-r*.05})"><g transform="translate(${-r*.3},0)">${oEye(id+'_eL',r*.27,'#6b3a1c')}</g><g transform="translate(${r*.3},0)">${oEye(id+'_eR',r*.27,'#6b3a1c')}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',0,r*.5)}</g>`:''}</g></g>`;}
function bodyWorld(){
  DEFS+=`<clipPath id="lumC"><path d="${LUM_D}"/></clipPath>`;
  return `<g id="bw"><rect x="-40" y="-40" width="800" height="1360" fill="#f3cfa6"/>
   ${[[110,640,60,16],[200,660,26,9],[590,650,70,16],[650,690,24,8],[120,300,40,12]].map(([x,y,a,b])=>`<ellipse cx="${x}" cy="${y}" rx="${a}" ry="${b}" fill="#f8dcbb"/>`).join('')}
   <path d="M-40,900 C100,880 250,930 318,905 L402,905 C470,930 620,880 760,900 L760,1320 L-40,1320 Z" fill="#a9d6f7"/><path d="M-40,900 C100,880 250,930 318,905 M402,905 C470,930 620,880 760,900" fill="none" ${OLW}/>
   <path d="${OUT_D}" fill="#f6a3ad" ${OLW}/><path d="${LUM_D}" fill="#d9505f" ${OLW2}/>
   <g clip-path="url(#lumC)"><path d="M300,330 C300,220 350,130 430,126 L800,126" fill="none" stroke="#ef7f8a" stroke-width="16" stroke-linecap="round" opacity=".7"/><path d="M360,560 v200" stroke="#c23f50" stroke-width="10" stroke-linecap="round" opacity=".5"/>
    <g id="wet"></g><g id="melt" opacity="0"><path d="M0,-44 C30,-50 44,-20 40,6 C52,30 20,50 -4,44 C-34,52 -52,22 -42,-6 C-48,-34 -22,-50 0,-44Z" fill="#fde8ea" ${OLW2}/></g></g>
   ${[[300,812,1],[420,812,-1],[310,858,1],[410,858,-1]].map(([x,y,s])=>`<path d="M${x},${y} q${s*16},14 0,30" fill="#f6a3ad" ${OLW2}/>`).join('')}
   <g id="rface" transform="translate(365,520)"><g transform="translate(-34,0)">${oEye('rc_eL',32,'#d9505f')}</g><g transform="translate(34,0)">${oEye('rc_eR',32,'#d9505f')}</g>${brow('rc_bL')}${brow('rc_bR')}${mouthEl('rc_m',0,74)}</g>
   <g id="lumps">${lump('L4',62,false)}${lump('L3',70,false)}${lump('L2',58,false)}${lump('L1',64,false)}${lump('L0',76,true)}</g>
   <g id="drops"></g>
   <g id="supp"><path d="M-17,34 L-17,-20 C-17,-48 17,-48 17,-20 L17,34 C10,42 -10,42 -17,34 Z" fill="#fbfbf6" ${OLW}/><path d="M-8,-22 v40" stroke="#dcdccf" stroke-width="5" stroke-linecap="round"/></g>
   <g id="glove"><path d="M-70,300 L-70,150 C-110,110 -112,40 -78,10 C-70,-10 -50,-10 -44,10 L-36,60 L-30,-70 C-28,-96 2,-96 4,-70 L8,30 L16,-80 C18,-106 48,-106 50,-80 L50,40 C70,20 92,30 88,56 C84,110 84,130 70,160 L70,300 Z" fill="${C_GLOVE}" ${OLW}/>
     <path d="M-56,170 C-88,130 -92,70 -70,40" fill="none" stroke="#6db7f5" stroke-width="9" stroke-linecap="round"/><path d="M-70,236 h140 M-70,262 h140" stroke="${C_GLOVE_S}" stroke-width="6"/>
     <g transform="translate(4,128)"><g transform="translate(-27,0)">${oEye('gv_eL',26,C_GLOVE)}</g><g transform="translate(27,0)">${oEye('gv_eR',26,C_GLOVE)}</g>${brow('gv_bL')}${brow('gv_bR')}${mouthEl('gv_m',0,54)}</g></g>
   <g id="fx"></g></g>`;}
function board(){const row=(id,y,col,txt)=>`<g id="${id}" opacity="0"><rect x="70" y="${y}" width="580" height="74" rx="16" fill="${col}" stroke="#1d2a44" stroke-width="4"/><text x="360" y="${y+50}" text-anchor="middle" style="font-family:LG,sans-serif;font-size:35px;letter-spacing:1px" fill="#fff">${txt}</text></g>`;
  return `<g id="brd"><rect x="46" y="40" width="644" height="470" rx="24" fill="#000" opacity=".12"/><rect x="38" y="30" width="644" height="470" rx="24" fill="#fff" stroke="#1d2a44" stroke-width="5"/>
   <text x="360" y="104" text-anchor="middle" style="font-family:LG,sans-serif;font-size:54px;letter-spacing:2px" fill="#1d2a44">HOW IT WORKS</text>
   ${row('b0',132,'#2f8fe0','1. MELTS INSIDE')}${row('b1',218,'#14a3a0','2. PULLS WATER TO THE STOOL')}${row('b2',304,'#e8873f','3. TRIGGERS THE URGE')}${row('b3',390,'#2fae62','WORKS IN 15-60 MINUTES')}</g>`;}
// ---- the hospital room: our patient in bed, our doctor beside him ----
function ward(){
  DEFS+=`<clipPath id="bedC"><rect x="-300" y="-100" width="600" height="700"/></clipPath>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#cfe0e6"/><rect x="430" y="-40" width="26" height="700" fill="#eef7fa"/><rect x="456" y="-40" width="8" height="700" fill="#b9cdd4"/>
   <rect x="-40" y="560" width="800" height="14" fill="#b9cdd4"/>
   <g transform="translate(360,640) scale(1.3) translate(-372,-560)"><g transform="translate(176,330) scale(1.22)">${doctorSVG()}</g>
   <path d="M440,560 C440,500 700,500 700,560 L720,900 L420,900 Z" fill="#fff" ${OLW}/><path d="M470,590 q90,-40 200,0" fill="none" stroke="#d5dde2" stroke-width="6" stroke-linecap="round"/>
   <g id="patWrap"><g transform="translate(545,470) scale(1.3)"><g clip-path="url(#bedC)">${patientSVG()}</g></g></g></g><g transform="translate(0,84)">
   <path d="M-40,1000 C60,930 180,880 300,930 C380,880 520,850 640,880 C700,892 740,900 760,910 L760,1320 L-40,1320 Z" fill="#fff" ${OLW}/>
   <path d="M60,1010 C160,960 240,950 300,1000 C330,1040 330,1120 300,1200 M360,960 C460,910 580,910 700,950 M420,1040 C500,1010 600,1010 700,1060 M120,1120 C180,1100 230,1110 260,1150" fill="none" stroke="#cfd6db" stroke-width="7" stroke-linecap="round"/></g>`;}
