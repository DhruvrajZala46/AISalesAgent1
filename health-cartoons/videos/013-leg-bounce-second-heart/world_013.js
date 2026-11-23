// =============== 013 v2: "the bouncing leg". Our own set, all code in the 012 / 001 style ===============
// A bright cut-away of the lower leg (toes to the left): shin bone, a front muscle, a wide vein full of blood cells with faces,
// a big calf muscle with a sweatband and a face, and a small valve guard on the vein wall. A coral sneaker taps the floor.
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_SKIN='#f6c9a2', C_IN='#fde6cc', C_BONE='#fbf3dc', C_BONE_D='#e4d2a4', C_MUS='#ef5464', C_MUS_S='#c9374a', C_MUS2='#f58a86', C_MUS2_S='#dc6a6c',
  C_VEIN='#7f9cf5', C_VEIN_W='#4f68d8', C_CELL='#e23a48', C_GATE='#12928d', C_TEAL='#14a3a0', C_CORAL='#ff7a55', C_WALL='#bfe8f4', C_WALL2='#a6dcee';
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
const VX=y=>400-14*(y+60)/910;                           // centre line of the vein
const VW=60;                                             // half width of the vein
const V_LO=600, V_UP=230;                                // the two valves (hinge heights)
const SKIN_D='M150,-460 L150,-80 C146,200 170,520 236,760 C250,810 258,840 262,870 L500,870 C512,790 606,620 654,400 C676,300 672,100 654,-80 L654,-460 Z';
const INNER_D='M163,-460 L163,-80 C159,200 183,520 248,760 C261,810 269,840 273,870 L489,870 C501,790 594,620 641,400 C662,300 659,100 641,-80 L641,-460 Z';
const BONE_D='M178,-460 L178,-80 C176,200 204,520 276,870 L312,870 C262,520 240,200 240,-80 L240,-460 Z';
const MUS2_D='M254,-460 L254,-80 C252,150 262,420 296,640 C304,690 310,725 316,752 C324,700 328,560 326,420 C324,200 322,0 322,-80 L322,-460 Z';
const MUS_D='M474,-460 L474,-80 C472,120 468,300 464,520 C464,640 470,720 482,774 C500,730 544,650 564,600 C612,500 640,400 644,300 C652,180 648,40 640,-80 L640,-460 Z';
// a blood cell with a full face (the two speaking cells)
function cellSVG(id,r,face){const k=r/20;
  return `<g id="${id}"><g id="${id}_b"><ellipse rx="${r}" ry="${(r*.93).toFixed(1)}" fill="${C_CELL}" ${OLW2}/><ellipse cx="${(-r*.08).toFixed(1)}" cy="${(r*.1).toFixed(1)}" rx="${(r*.6).toFixed(1)}" ry="${(r*.5).toFixed(1)}" fill="#c22d3b" opacity=".5"/>
   <path d="M${(-r*.62).toFixed(1)},${(-r*.46).toFixed(1)} C${(-r*.3).toFixed(1)},${(-r*.8).toFixed(1)} ${(r*.2).toFixed(1)},${(-r*.84).toFixed(1)} ${(r*.46).toFixed(1)},${(-r*.64).toFixed(1)}" fill="none" stroke="#ff9ea4" stroke-width="${(3*k).toFixed(1)}" stroke-linecap="round"/>
   ${face?`<g transform="translate(${(-r*.36).toFixed(1)},${(-r*.14).toFixed(1)})">${oEye(id+'_eL',r*.32,C_CELL)}</g><g transform="translate(${(r*.36).toFixed(1)},${(-r*.14).toFixed(1)})">${oEye(id+'_eR',r*.32,C_CELL)}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',0,r*.46)}`:''}</g></g>`;}
// every other cell: drawn each frame with a small face. mood: 1 happy, 0 calm, -1 scared, -2 squashed and grumpy
function smallCell(x,y,r,rot,mood,lx,ly,bl){const sx=mood<=-2?1.1:1,sy=mood<=-2?.9:1;
  const eye=(ex)=>bl?`<path d="M${ex-5},-3 h10" stroke="${INK}" stroke-width="2.4" stroke-linecap="round"/>`:`<circle cx="${ex}" cy="-3.5" r="6" fill="#fff" stroke="${INK}" stroke-width="1.8"/><circle cx="${(ex+lx*2.6).toFixed(1)}" cy="${(-3.5+ly*2.6).toFixed(1)}" r="${mood===-1?2.1:2.9}" fill="${INK}"/>`;
  const m=mood>=1?`<path d="M-5.5,6.5 Q0,13 5.5,6.5 Z" fill="#5e1a20" stroke="${INK}" stroke-width="1.8" stroke-linejoin="round"/>`:mood===-1?`<ellipse cx="0" cy="9.5" rx="3.4" ry="4.4" fill="#5e1a20" stroke="${INK}" stroke-width="1.8"/>`:mood<=-2?`<path d="M-5,10.5 Q0,6.5 5,10.5" fill="none" stroke="${INK}" stroke-width="2.2" stroke-linecap="round"/>`:`<path d="M-4.5,9 H4.5" stroke="${INK}" stroke-width="2.2" stroke-linecap="round"/>`;
  const br=mood===-1?`<path d="M-11,-13 L-3,-11 M11,-13 L3,-11" stroke="${INK}" stroke-width="2" stroke-linecap="round"/>`:mood<=-2?`<path d="M-11,-11.5 L-3,-9.5 M11,-11.5 L3,-9.5" stroke="${INK}" stroke-width="2" stroke-linecap="round"/>`:'';
  return `<g transform="translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${rot.toFixed(0)}) scale(${sx},${sy})"><ellipse rx="${r}" ry="${(r*.93).toFixed(1)}" fill="${C_CELL}" ${OLW2}/><path d="M${(-r*.6).toFixed(1)},${(-r*.5).toFixed(1)} C${(-r*.25).toFixed(1)},${(-r*.84).toFixed(1)} ${(r*.25).toFixed(1)},${(-r*.84).toFixed(1)} ${(r*.52).toFixed(1)},${(-r*.6).toFixed(1)}" fill="none" stroke="#ff9ea4" stroke-width="3" stroke-linecap="round"/>${eye(-7.2)}${eye(7.2)}${br}${m}</g>`;}
const SHOE_IN=`<path d="M262,930 C330,912 450,912 512,928 C548,950 548,1040 540,1082 L44,1082 C26,1060 34,1018 70,1004 C130,984 200,966 262,930 Z" fill="${C_CORAL}" ${OLW}/>
    <path d="M40,1076 H544 C548,1092 544,1108 530,1114 H56 C36,1108 30,1090 40,1076 Z" fill="#fffdf8" ${OLW}/>
    <path d="M44,1082 C26,1060 34,1018 70,1004 C96,996 112,1010 116,1036 C120,1058 110,1076 96,1082 Z" fill="#fffdf8" ${OLW}/>
    <path d="M300,1080 C360,1040 430,1000 520,972" fill="none" stroke="${C_TEAL}" stroke-width="16" stroke-linecap="round"/>
    ${[[178,984],[206,972],[234,958]].map(([x,y])=>`<path d="M${x},${y} l22,26" stroke="#fffdf8" stroke-width="7" stroke-linecap="round"/>`).join('')}
    <path d="M268,936 C330,922 448,922 506,934" fill="none" stroke="#d9562f" stroke-width="5" stroke-linecap="round"/>`;
// the valve guard: a small round fellow on the vein wall, right at the hinge of his valve
function guardSVG(id,x,y){return `<g id="${id}" transform="translate(${x},${y})"><circle r="31" fill="${C_GATE}" ${OLW}/><path d="M-20,-14 C-12,-24 12,-24 20,-14" fill="none" stroke="#49c2bc" stroke-width="5" stroke-linecap="round"/>
   <g id="${id}_cap"><path d="M-22,-25 C-22,-50 22,-50 22,-25 Z" fill="#26346b" ${OLW2}/><path d="M-30,-25 H30" stroke="${INK}" stroke-width="9" stroke-linecap="round"/><path d="M-30,-25 H30" stroke="#1a2247" stroke-width="5" stroke-linecap="round"/><path d="M-5,-38 l5,-5 l5,5 l-5,6 Z" fill="#f2c74a" ${OLW2}/></g>
   <g transform="translate(-11,-3)">${oEye(id+'_eL',10.5,C_GATE)}</g><g transform="translate(11,-3)">${oEye(id+'_eR',10.5,C_GATE)}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',0,16)}</g>`;}
function legWorld(){
  DEFS+=`<clipPath id="lumClip"><path id="lumClipP"/></clipPath><clipPath id="musClip"><path d="${MUS_D}"/></clipPath><clipPath id="mus2Clip"><path d="${MUS2_D}"/></clipPath><clipPath id="legClip"><path d="${INNER_D}"/></clipPath>`;
  let s=`<g id="wLeg"><rect x="-900" y="-600" width="2500" height="2400" fill="${C_WALL}"/>
   ${[[70,150,70],[690,470,50],[60,640,44],[660,60,36],[40,960,48],[-200,400,80],[-330,820,60]].map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${C_WALL2}"/>`).join('')}
   <g id="couch"><path d="M704,-600 L1600,-600 L1600,1040 L704,1040 C690,700 690,300 704,-600 Z" fill="#f6c14f" ${OLW}/><path d="M728,-600 C718,300 718,700 728,1010" fill="none" stroke="#ffdf8f" stroke-width="12" stroke-linecap="round" opacity=".9"/>
    <path d="M710,1040 L1600,1040 L1600,1074 L710,1074 Z" fill="#d99a2b" ${OLW}/><rect x="728" y="1074" width="30" height="42" fill="#8a5a36" ${OLW}/></g>
   <rect x="-900" y="1086" width="2500" height="30" fill="#fffdf8" ${OLW}/>
   <rect x="-900" y="1114" width="2500" height="700" fill="#e2a868"/><path d="M-900,1114 H1600" fill="none" ${OLW}/>
   ${[1180,1262,1360].map((y,i)=>`<path d="M-900,${y} H1600" stroke="#c88a4c" stroke-width="3"/>`+[-3,-2,-1,0,1,2,3,4].map(k=>`<path d="M${k*260+i*120-140},${y-(i?82:66)} V${y}" stroke="#c88a4c" stroke-width="3"/>`).join('')).join('')}
   <g id="walkG"><ellipse id="shadow" cx="300" cy="1120" rx="290" ry="13" fill="#000" opacity=".16"/>`;
  // ---- the leg (moves up and down with the bounce) ----
  s+=`<g id="legG"><path d="${SKIN_D}" fill="${C_SKIN}" ${OLW}/><path d="${INNER_D}" fill="${C_IN}"/>
   <path d="${BONE_D}" fill="${C_BONE}" ${OLW}/><path d="M194,-460 L194,-60 C192,200 216,520 280,850" fill="none" stroke="#fffdf4" stroke-width="9" stroke-linecap="round" opacity=".95"/>
   ${[[214,40,3.5],[212,250,3],[232,440,3.5],[252,620,3],[282,780,3]].map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${C_BONE_D}"/>`).join('')}
   ${shaded(MUS2_D,C_MUS2,C_MUS2_S,16)}<g clip-path="url(#mus2Clip)">${[272,290,306].map(x=>`<path d="M${x},-460 L${x},-80 C${x+2},200 ${lerp(x,312,.5).toFixed(0)},480 ${lerp(x,314,.94).toFixed(0)},730" fill="none" stroke="#e0706f" stroke-width="2.6" opacity=".8"/>`).join('')}</g><path d="${MUS2_D}" fill="none" ${OLW}/>
   <path d="M482,768 C480,800 474,836 470,870" fill="none" stroke="${INK}" stroke-width="24" stroke-linecap="round"/><path d="M482,768 C480,800 474,836 470,870" fill="none" stroke="#fbeccd" stroke-width="18" stroke-linecap="round"/>`;
  // the calf muscle: big, with fibres, a teal sweatband and a face
  s+=`<g id="calfG">${shaded(MUS_D,C_MUS,C_MUS_S,22)}
    <g clip-path="url(#musClip)">${[492,512,534,556,578,600,620].map((x,i)=>`<path d="M${x},-460 L${x},-80 C${x+2},200 ${lerp(x,484,.45).toFixed(0)},520 ${lerp(x,484,.93).toFixed(0)},760" fill="none" stroke="#cf3e50" stroke-width="2.6" opacity=".7"/>`).join('')}
     <path d="M458,176 C510,160 590,160 660,178 L660,214 C590,196 510,196 458,212 Z" fill="${C_TEAL}" ${OLW2}/><path d="M468,186 C516,172 590,172 650,188" fill="none" stroke="#6fd3cf" stroke-width="5" stroke-linecap="round"/></g>
    <path d="${MUS_D}" fill="none" ${OLW}/>
    <g id="calfFace"><g transform="translate(521,292)">${oEye('cEyeL',33,C_MUS)}</g><g transform="translate(593,292)">${oEye('cEyeR',33,C_MUS)}</g>${brow('cBrL')}${brow('cBrR')}${mouthEl('calf_m',557,366)}</g>
    <g id="sqz"></g><g id="sparks"></g></g>`;
  // the vein (drawn every frame: it bulges where cells pile up and narrows when the calf squeezes)
  s+=`<path id="veinO" fill="none" stroke="${INK}" stroke-width="15" stroke-linejoin="round"/><path id="veinW" fill="none" stroke="${C_VEIN_W}" stroke-width="9" stroke-linejoin="round"/><path id="veinL" fill="${C_VEIN}"/>
   <g clip-path="url(#lumClip)"><path id="veinShine" fill="none" stroke="#b3c4fb" stroke-width="8" stroke-linecap="round" opacity=".85"/>
    <g id="cellsG"></g>${cellSVG('hA',26,true)}${cellSVG('hB',26,true)}<g id="sweat"></g></g>
   <path id="uvL" fill="#fbfcff" ${OLW2}/><path id="uvR" fill="#fbfcff" ${OLW2}/>
   <path id="gvL" fill="#fbfcff" ${OLW2}/><path id="gvR" fill="#fbfcff" ${OLW2}/>
   ${guardSVG('gd',VX(V_LO)-VW-20,V_LO-14)}
   <g id="sock"><path d="M254,838 C320,826 440,826 508,838 L512,960 L258,960 Z" fill="#fffdf8" ${OLW}/><path d="M258,862 C330,852 436,852 508,862 M259,882 C330,872 436,872 509,882" fill="none" stroke="${C_TEAL}" stroke-width="7"/></g></g>`;
  // ---- the sneaker (turns about its toes when the heel lifts) ----
  s+=`<g id="shoeG">${SHOE_IN}</g></g>
   <g id="impact"></g></g>`;
  return s;}
// a small copy of the leg for the study card (the same sneaker; the leg comes down from the top of its window)
function miniLeg(id,cx,floorY,x0,y0,ww,hh){
  DEFS+=`<clipPath id="${id}_c"><rect x="${x0}" y="${y0}" width="${ww}" height="${hh}" rx="16"/></clipPath>`;
  return `<rect x="${x0}" y="${y0}" width="${ww}" height="${hh}" rx="16" fill="${C_WALL}"/>
   <g clip-path="url(#${id}_c)"><circle cx="${x0+46}" cy="${y0+70}" r="26" fill="${C_WALL2}"/><rect x="${x0}" y="${floorY}" width="${ww}" height="60" fill="#e2a868"/><path d="M${x0},${floorY} h${ww}" stroke="${INK}" stroke-width="3"/>
    <g transform="translate(${cx},${floorY}) scale(.36) translate(-289,-1114)"><ellipse cx="300" cy="1120" rx="290" ry="13" fill="#000" opacity=".14"/>
     <g id="${id}_leg"><path d="M262,-200 C258,300 262,640 270,860 L498,860 C512,760 560,560 592,300 C600,200 600,0 596,-200 Z" fill="#3d4f86" ${OLW}/><path d="M266,792 C330,782 440,782 506,794 L500,842 C440,832 330,832 268,842 Z" fill="#2f3e6b" ${OLW}/>
      <path d="M258,838 C320,826 440,826 504,838 L508,960 L262,960 Z" fill="#fffdf8" ${OLW}/><path d="M262,862 C330,852 436,852 504,862 M263,882 C330,872 436,872 505,882" fill="none" stroke="${C_TEAL}" stroke-width="7"/></g>
     <g id="${id}_shoe">${SHOE_IN}</g><g id="${id}_imp"></g></g></g>
   <rect x="${x0}" y="${y0}" width="${ww}" height="${hh}" rx="16" fill="none" ${OLW}/>`;}
const ARROW_D='M0,-70 L40,-18 L17,-18 L17,70 L-17,70 L-17,-18 L-40,-18 Z';
function studyCard(){
  DEFS+=`<clipPath id="cardC"><rect x="70" y="60" width="580" height="482" rx="26"/></clipPath>`;
  return `<g id="card" opacity="0"><rect x="78" y="70" width="580" height="482" rx="26" fill="#000" opacity=".16"/>
   <rect x="70" y="60" width="580" height="482" rx="26" fill="#fff"/><g clip-path="url(#cardC)"><rect x="70" y="60" width="580" height="74" fill="${C_TEAL}"/><path d="M70,134 h580" stroke="${INK}" stroke-width="3.4"/></g>
   <rect x="70" y="60" width="580" height="482" rx="26" fill="none" stroke="${INK}" stroke-width="4"/>
   <g transform="translate(124,97)"><circle r="23" fill="#fff" ${OLW2}/><path d="M0,-13 V0 L10,7" fill="none" stroke="${INK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>
   <text x="392" y="110" text-anchor="middle" style="font-family:LG,sans-serif;font-size:35px;letter-spacing:1px" fill="#fff" stroke="${INK}" stroke-width="5" paint-order="stroke" stroke-linejoin="round">AFTER 3 HOURS SITTING</text>
   ${miniLeg('mlS',176,416,90,152,254,292)}${miniLeg('mlF',466,416,376,152,254,292)}
   <g id="arrD" opacity="0"><g transform="rotate(180)"><path d="${ARROW_D}" fill="#3f73e6" ${OLW}/></g></g>
   <g id="arrU" opacity="0"><path d="${ARROW_D}" fill="#2fbf5f" ${OLW}/></g>
   <text class="lbl" x="217" y="482" text-anchor="middle" style="font-size:25px">STILL LEG</text><text class="lbl" x="503" y="482" text-anchor="middle" style="font-size:25px">FIDGETING LEG</text>
   <text id="tD" opacity="0" class="lbl" x="217" y="518" text-anchor="middle" style="font-size:21px;fill:#2f5fd0">BLOOD FLOW DOWN</text><text id="tU" opacity="0" class="lbl" x="503" y="518" text-anchor="middle" style="font-size:21px;fill:#1f9d4b">BLOOD FLOW UP</text></g>`;}
function heartIcon(id){return `<g id="${id}" opacity="0"><path d="M0,40 C-70,-8 -54,-74 0,-36 C54,-74 70,-8 0,40 Z" fill="#e2474b" ${OLW}/><path d="M-32,-36 C-42,-28 -44,-16 -39,-6" fill="none" stroke="#ff9ea4" stroke-width="7" stroke-linecap="round"/></g>`;}
// Dr. Mira in a round bubble (she explains over the leg; no cut away from the action)
function docBubble(){
  DEFS+=`<clipPath id="dbC"><circle r="92"/></clipPath>`;
  return `<g id="docB" opacity="0"><circle r="100" cx="5" cy="7" fill="#000" opacity=".16"/><circle r="92" fill="#e8f7f5"/><g clip-path="url(#dbC)"><g transform="translate(0,-92) scale(1.02)">${doctorSVG()}</g></g>
   <circle r="92" fill="none" stroke="${C_TEAL}" stroke-width="10"/><circle r="97" fill="none" stroke="${INK}" stroke-width="3.4"/><circle r="87" fill="none" stroke="${INK}" stroke-width="2.4"/>
   <g transform="translate(0,104)"><rect x="-72" y="-17" width="144" height="34" rx="17" fill="#fff" ${OLW2}/><text y="8" text-anchor="middle" style="font-family:LG,sans-serif;font-size:21px;letter-spacing:.5px" fill="#0b6e6b">GIGGLEMD</text></g></g>`;}
