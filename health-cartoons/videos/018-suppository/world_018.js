// =============== 018: how a suppository fixes constipation. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_STEEL='#c3cad3', C_TEAL='#14a3a0', C_GLOVE='#2f8fe0', C_GLOVE_S='#1c6cba';
const OUT_D='M226,330 C226,150 300,56 430,56 L800,56 L800,334 L504,334 L504,560 C504,700 446,760 424,830 L404,905 L316,905 L296,830 C274,760 226,700 226,560 Z';
const LUM_D='M256,330 C256,172 322,86 430,86 L800,86 L800,304 L474,304 L474,560 C474,690 422,750 398,830 L386,905 L334,905 L322,830 C298,750 256,690 256,560 Z';
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
// a poop lump: lumpy, shaded, with bumps. hard = dark, dry and cracked; soft = lighter, wet and glossy
function lump(id,r,face){const n=8,pts=Array.from({length:n},(_,i)=>{const a=i/n*6.283,rr=r*(.74+rnd(i*3+r)*.46);return [Math.cos(a)*rr*1.18,Math.sin(a)*rr*.88];});
  const q0=pts[0],q1=pts[1];const d=`M${((q0[0]+q1[0])/2).toFixed(1)},${((q0[1]+q1[1])/2).toFixed(1)} `+pts.map((_,i)=>{const p=pts[(i+1)%n],q=pts[(i+2)%n];return `Q${p[0].toFixed(1)},${p[1].toFixed(1)} ${((p[0]+q[0])/2).toFixed(1)},${((p[1]+q[1])/2).toFixed(1)}`;}).join(' ')+'Z';
  DEFS+=`<clipPath id="${id}_c"><path d="${d}"/></clipPath>`;
  return `<g id="${id}"><g id="${id}_s"><path id="${id}_p" d="${d}" fill="#6b3a1c" ${OLW}/>
    <g clip-path="url(#${id}_c)"><path d="M${-r*1.3},${r*.2} Q0,${r*.75} ${r*1.3},${r*.2} L${r*1.3},${r*1.2} L${-r*1.3},${r*1.2} Z" fill="#000" opacity=".22"/>
     <path d="M${-r*.9},${-r*.1} q${r*.35},${-r*.3} ${r*.7},0 M${r*.1},${-r*.45} q${r*.35},${-r*.25} ${r*.7},${r*.05} M${-r*.5},${r*.45} q${r*.4},${-r*.22} ${r*.8},0" fill="none" stroke="#3a1d0b" stroke-width="5" stroke-linecap="round" opacity=".55"/></g>
    <g id="${id}_cr"><path d="M${-r*.85},${-r*.35} l${r*.16},${r*.14} l${-r*.06},${r*.18} M${r*.8},${r*.05} l${-r*.18},${r*.1} l${r*.06},${r*.16} M${-r*.1},${-r*.78} l${r*.06},${r*.2}" fill="none" stroke="#24120a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>
    <g id="${id}_gl" opacity="0"><ellipse cx="${-r*.4}" cy="${-r*.45}" rx="${r*.3}" ry="${r*.12}" fill="#fff" opacity=".6" transform="rotate(-18,${-r*.4},${-r*.45})"/><circle cx="${r*.5}" cy="${-r*.35}" r="${r*.08}" fill="#fff" opacity=".55"/></g>
    ${face?`<g transform="translate(0,${-r*.05})"><g transform="translate(${-r*.32},0)">${oEye(id+'_eL',r*.29,'#6b3a1c')}</g><g transform="translate(${r*.32},0)">${oEye(id+'_eR',r*.29,'#6b3a1c')}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',0,r*.52)}</g>`:''}</g></g>`;}
function bodyWorld(){
  DEFS+=`<clipPath id="lumC"><path d="${LUM_D}"/></clipPath>`;
  return `<g id="bw"><rect x="-40" y="-40" width="800" height="1360" fill="#f3cfa6"/>
   ${[[110,640,60,16],[200,660,26,9],[590,650,70,16],[650,690,24,8],[120,300,40,12]].map(([x,y,a,b])=>`<ellipse cx="${x}" cy="${y}" rx="${a}" ry="${b}" fill="#f8dcbb"/>`).join('')}
   <path d="M-40,930 C40,1040 270,1030 318,905 L402,905 C450,1030 680,1040 760,930 L760,1320 L-40,1320 Z" fill="#a9d6f7"/><path d="M-40,930 C40,1040 270,1030 318,905 M402,905 C450,1030 680,1040 760,930" fill="none" ${OLW}/><path d="M60,950 q60,40 130,34 M660,950 q-60,40 -130,34" fill="none" stroke="#e2b98c" stroke-width="7" stroke-linecap="round"/>
   <path d="M520,62 q46,-40 92,0 q46,-40 92,0 q46,-40 92,0 L796,62 Z M520,328 q46,40 92,0 q46,40 92,0 q46,40 92,0 Z" fill="#f6a3ad" ${OLW}/>
   <path d="${OUT_D}" fill="#f6a3ad" ${OLW}/><path d="${LUM_D}" fill="#d9505f" ${OLW2}/>
   <g clip-path="url(#lumC)"><path d="M300,330 C300,220 350,130 430,126 L800,126" fill="none" stroke="#ef7f8a" stroke-width="16" stroke-linecap="round" opacity=".7"/><path d="M360,560 v200" stroke="#c23f50" stroke-width="10" stroke-linecap="round" opacity=".5"/>
    <rect id="wetR" x="230" y="900" width="600" height="900" fill="#9fd4fb" opacity="0"/><g id="wet"></g><g id="melt" opacity="0"><path d="M0,-44 C30,-50 44,-20 40,6 C52,30 20,50 -4,44 C-34,52 -52,22 -42,-6 C-48,-34 -22,-50 0,-44Z" fill="#fde8ea" ${OLW2}/></g></g>
   ${[[300,812,1],[420,812,-1],[310,858,1],[410,858,-1]].map(([x,y,s])=>`<path d="M${x},${y} q${s*16},14 0,30" fill="#f6a3ad" ${OLW2}/>`).join('')}
   <g id="rface" transform="translate(365,520)"><g transform="translate(-34,0)">${oEye('rc_eL',32,'#d9505f')}</g><g transform="translate(34,0)">${oEye('rc_eR',32,'#d9505f')}</g>${brow('rc_bL')}${brow('rc_bR')}${mouthEl('rc_m',0,74)}</g>
   <g id="lumps">${lump('L4',62,false)}${lump('L3',70,false)}${lump('L2',58,false)}${lump('L1',64,false)}${lump('L0',76,true)}</g>
   <g id="drops"></g>
   <g id="supp"><path d="M-17,34 L-17,-20 C-17,-48 17,-48 17,-20 L17,34 C10,42 -10,42 -17,34 Z" fill="#fbfbf6" ${OLW}/><path d="M-8,-22 v40" stroke="#dcdccf" stroke-width="5" stroke-linecap="round"/></g>
   <g id="toilet"><path d="M-196,10 C-186,170 -110,230 0,230 C110,230 186,170 196,10 Z" fill="#fbfbf8" ${OLW}/><ellipse rx="206" ry="48" fill="#fbfbf8" ${OLW}/><ellipse cy="2" rx="170" ry="33" fill="#31475c" ${OLW2}/><ellipse cy="10" rx="150" ry="22" fill="#8fd0fb"/><path d="M-110,8 q40,-10 80,0" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"/><g id="splash"></g></g>
   <g id="glove"><rect x="-74" y="252" width="148" height="110" rx="14" fill="#62b2f5" ${OLW}/><path d="M-74,286 h148 M-74,314 h148" stroke="${C_GLOVE_S}" stroke-width="5"/>
     <path d="M-80,262 C-98,200 -94,128 -72,100 L62,100 C88,128 94,200 80,262 Z" fill="${C_GLOVE}" ${OLW}/>
     ${[[-56,104],[-26,96],[4,100]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="26" fill="${C_GLOVE}" ${OLW}/><path d="M${x-12},${y+6} q12,10 24,0" fill="none" stroke="${C_GLOVE_S}" stroke-width="4" stroke-linecap="round"/>`).join('')}
     <path d="M72,186 Q98,70 20,6" fill="none" stroke="${INK}" stroke-width="47" stroke-linecap="round"/><path d="M72,186 Q98,70 20,6" fill="none" stroke="${C_GLOVE}" stroke-width="40" stroke-linecap="round"/>
     <path d="M26,112 L-14,2" fill="none" stroke="${INK}" stroke-width="45" stroke-linecap="round"/><path d="M26,112 L-14,2" fill="none" stroke="${C_GLOVE}" stroke-width="38" stroke-linecap="round"/>
     <path d="M-60,236 C-82,200 -84,150 -70,124" fill="none" stroke="#6db7f5" stroke-width="9" stroke-linecap="round"/>
     <g transform="translate(-6,184)"><g transform="translate(-26,0)">${oEye('gv_eL',25,C_GLOVE)}</g><g transform="translate(26,0)">${oEye('gv_eR',25,C_GLOVE)}</g>${brow('gv_bL')}${brow('gv_bR')}${mouthEl('gv_m',0,50)}</g></g>
   <g id="inset"><rect x="16" y="150" width="196" height="352" rx="18" fill="#fff" ${OLW}/><circle cx="114" cy="204" r="27" fill="#f6c9a2" ${OLW2}/><path d="M80,240 h68 q10,0 10,10 v112 h-88 v-112 q0,-10 10,-10 Z" fill="#7fb6e8" ${OLW2}/><rect x="72" y="362" width="38" height="92" rx="10" fill="#f6c9a2" ${OLW2}/><rect x="118" y="362" width="38" height="92" rx="10" fill="#f6c9a2" ${OLW2}/>
     <path d="M92,262 h44 v18 h-40 v18 h40 v18 h-40 v18 h18 v22" fill="none" stroke="#e8667a" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><circle id="ring" cx="114" cy="366" r="20" fill="none" stroke="#e02626" stroke-width="6"/>
     <text x="114" y="488" text-anchor="middle" style="font-family:LG,sans-serif;font-size:21px" fill="#1d2a44">INSIDE HERE</text><path d="M134,366 L236,470" stroke="#e02626" stroke-width="5" stroke-dasharray="10 9" stroke-linecap="round"/></g>
   <g id="fx"></g></g>`;}
function board(){const row=(id,y,col,txt)=>`<g id="${id}" opacity="0"><rect x="70" y="${y}" width="580" height="74" rx="16" fill="${col}" stroke="#1d2a44" stroke-width="4"/><text x="360" y="${y+50}" text-anchor="middle" style="font-family:LG,sans-serif;font-size:35px;letter-spacing:1px" fill="#fff">${txt}</text></g>`;
  return `<g id="brd"><rect x="46" y="40" width="644" height="470" rx="24" fill="#000" opacity=".12"/><rect x="38" y="30" width="644" height="470" rx="24" fill="#fff" stroke="#1d2a44" stroke-width="5"/>
   <text x="360" y="104" text-anchor="middle" style="font-family:LG,sans-serif;font-size:54px;letter-spacing:2px" fill="#1d2a44">HOW IT WORKS</text>
   ${row('b0',132,'#2f8fe0','1. MELTS INSIDE')}${row('b1',218,'#14a3a0','2. PULLS WATER INTO THE POOP')}${row('b2',304,'#e8873f','3. TRIGGERS THE URGE')}${row('b3',390,'#2fae62','WORKS IN 15-60 MINUTES')}</g>`;}
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
