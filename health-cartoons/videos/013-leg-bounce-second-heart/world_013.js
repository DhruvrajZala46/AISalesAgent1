// =============== 013: "the elevator in your leg". Our own set, all code in the 012 / 001 style ===============
// Set A: a cut-away of the lower leg (toes to the left). The vein is the elevator shaft, the blood cells are the passengers,
// the calf muscle (right, with a sweatband) is the lift, the valve is a one-way door with a guard's cap. A teal sneaker taps
// the floor when the leg bounces. Set B: Dr. Mira's clinic (as in 012).
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_SKIN='#f1c7a3', C_IN='#fbe9d2', C_BONE='#f7eed6', C_BONE_D='#e4d2a4', C_MUS='#e15a66', C_MUS_S='#c23f4f', C_VEIN='#8ea4ef', C_VEIN_W='#5a70d2', C_ART='#e2474b', C_CELL='#d9404a', C_GATE='#0f7d79', C_TEAL='#14a3a0', C_CORAL='#ff7a66';
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
const VX=y=>420-18*(y+60)/910;                           // centre line of the vein
const SKIN_D='M236,-460 L236,-80 C230,120 232,300 246,520 C254,640 268,760 282,870 L486,870 C500,780 548,640 604,430 C628,320 624,120 604,-80 L604,-460 Z';
const INNER_D='M250,-460 L250,-80 C244,120 246,300 260,520 C268,640 280,760 294,870 L474,870 C488,780 534,640 590,430 C612,320 610,120 590,-80 L590,-460 Z';
const BONE_D='M256,-460 L256,-80 C250,200 262,520 292,870 L328,870 C312,520 306,200 316,-80 L316,-460 Z';
const MUS_D='M476,-460 L476,-80 C474,120 470,300 466,520 C466,620 474,690 486,728 C500,700 524,650 532,632 C560,560 584,470 586,420 C606,320 604,120 584,-80 L584,-460 Z';
function cellSVG(id,r,face){const k=r/20;
  return `<g id="${id}"><g id="${id}_b"><ellipse rx="${r}" ry="${(r*.93).toFixed(1)}" fill="${C_CELL}" ${OLW2}/><ellipse cx="${(-r*.08).toFixed(1)}" cy="${(r*.1).toFixed(1)}" rx="${(r*.6).toFixed(1)}" ry="${(r*.5).toFixed(1)}" fill="#bf303b" opacity=".5"/>
   <path d="M${(-r*.62).toFixed(1)},${(-r*.46).toFixed(1)} C${(-r*.3).toFixed(1)},${(-r*.8).toFixed(1)} ${(r*.2).toFixed(1)},${(-r*.84).toFixed(1)} ${(r*.46).toFixed(1)},${(-r*.64).toFixed(1)}" fill="none" stroke="#ff9ea4" stroke-width="${(3*k).toFixed(1)}" stroke-linecap="round"/>
   ${face?`<g transform="translate(${(-r*.36).toFixed(1)},${(-r*.14).toFixed(1)})">${oEye(id+'_eL',r*.3,C_CELL)}</g><g transform="translate(${(r*.36).toFixed(1)},${(-r*.14).toFixed(1)})">${oEye(id+'_eR',r*.3,C_CELL)}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',0,r*.44)}`:''}</g></g>`;}
function smallCell(x,y,r,rot){return `<g transform="translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${rot.toFixed(0)})"><ellipse rx="${r}" ry="${(r*.9).toFixed(1)}" fill="${C_CELL}" ${OLW2}/><ellipse cx="-1.5" cy="2" rx="${(r*.56).toFixed(1)}" ry="${(r*.44).toFixed(1)}" fill="#bf303b" opacity=".55"/><path d="M${(-r*.55).toFixed(1)},${(-r*.45).toFixed(1)} C${(-r*.2).toFixed(1)},${(-r*.78).toFixed(1)} ${(r*.25).toFixed(1)},${(-r*.78).toFixed(1)} ${(r*.5).toFixed(1)},${(-r*.55).toFixed(1)}" fill="none" stroke="#ff9ea4" stroke-width="3" stroke-linecap="round"/></g>`;}
const SHOE_IN=`<path d="M262,930 C330,912 450,912 512,928 C548,950 548,1040 540,1082 L44,1082 C26,1060 34,1018 70,1004 C130,984 200,966 262,930 Z" fill="${C_TEAL}" ${OLW}/>
    <path d="M40,1076 H544 C548,1092 544,1108 530,1114 H56 C36,1108 30,1090 40,1076 Z" fill="#fbfaf6" ${OLW}/>
    <path d="M44,1082 C26,1060 34,1018 70,1004 C96,996 112,1010 116,1036 C120,1058 110,1076 96,1082 Z" fill="#fbfaf6" ${OLW}/>
    <path d="M300,1080 C360,1040 430,1000 520,972" fill="none" stroke="${C_CORAL}" stroke-width="16" stroke-linecap="round"/>
    ${[[178,984],[206,972],[234,958]].map(([x,y])=>`<path d="M${x},${y} l22,26" stroke="#fbfaf6" stroke-width="7" stroke-linecap="round"/>`).join('')}
    <path d="M268,936 C330,922 448,922 506,934" fill="none" stroke="#0b6e6b" stroke-width="5" stroke-linecap="round"/>`;
function legWorld(){
  DEFS+=`<clipPath id="lumClip"><path id="lumClipP"/></clipPath><clipPath id="musClip"><path d="${MUS_D}"/></clipPath><clipPath id="legClip"><path d="${INNER_D}"/></clipPath>`;
  let s=`<g id="wLeg"><rect x="-200" y="-300" width="1120" height="1900" fill="#e3f4f0"/>
   ${[[90,160,60],[640,420,44],[120,620,36],[610,90,30],[70,940,40]].map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="#d3ece7"/>`).join('')}
   <g id="couch"><path d="M660,-300 L920,-300 L920,1040 L660,1040 C646,700 646,300 660,-300 Z" fill="#5f70a3" ${OLW}/><path d="M682,-300 C672,300 672,700 682,1010" fill="none" stroke="#8494c2" stroke-width="10" stroke-linecap="round" opacity=".8"/>
    <path d="M666,1040 L920,1040 L920,1074 L666,1074 Z" fill="#48577f" ${OLW}/><rect x="684" y="1074" width="30" height="42" fill="#a8734a" ${OLW}/></g>
   <rect x="-200" y="1086" width="1120" height="30" fill="#f6fbfa" ${OLW}/>
   <rect x="-200" y="1114" width="1120" height="500" fill="#d9a66b"/><path d="M-200,1114 H920" fill="none" ${OLW}/>
   ${[1180,1262,1360].map((y,i)=>`<path d="M-200,${y} H920" stroke="#bf8a52" stroke-width="3"/>`+[0,1,2,3].map(k=>`<path d="M${(k*260+i*120)%1000-140},${y-(i?82:66)} V${y}" stroke="#bf8a52" stroke-width="3"/>`).join('')).join('')}
   <ellipse id="shadow" cx="300" cy="1120" rx="290" ry="13" fill="#000" opacity=".14"/>`;
  // ---- the leg (moves up and down with the bounce) ----
  s+=`<g id="legG"><path d="${SKIN_D}" fill="${C_SKIN}" ${OLW}/><path d="${INNER_D}" fill="${C_IN}"/>
   <g clip-path="url(#legClip)">${[[300,120],[352,330],[330,560],[350,760],[452,790],[470,640]].map(([x,y],i)=>`<path d="M${x},${y} q${6+i%3*4},${22} ${-2},${46}" fill="none" stroke="#efd3b3" stroke-width="4" stroke-linecap="round"/>`).join('')}</g>
   <path d="${BONE_D}" fill="${C_BONE}" ${OLW}/><path d="M270,-460 L270,-60 C266,200 276,520 304,850" fill="none" stroke="#fffaf0" stroke-width="9" stroke-linecap="round" opacity=".9"/>
   ${[[296,40,3.5],[286,210,3],[300,400,3.5],[296,600,3],[312,760,3]].map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${C_BONE_D}"/>`).join('')}
   <path d="M342,-460 L342,-80 C344,200 346,520 344,870" fill="none" stroke="${INK}" stroke-width="16" stroke-linecap="round"/><path d="M342,-460 L342,-80 C344,200 346,520 344,870" fill="none" stroke="${C_ART}" stroke-width="10.5" stroke-linecap="round"/><path d="M340,-460 L340,-80 C342,200 344,520 342,870" fill="none" stroke="#ff8f92" stroke-width="3" stroke-linecap="round"/>
   <path d="M486,720 C482,770 474,820 470,870" fill="none" stroke="${INK}" stroke-width="24" stroke-linecap="round"/><path d="M486,720 C482,770 474,820 470,870" fill="none" stroke="#f6e7c8" stroke-width="18" stroke-linecap="round"/>`;
  // the calf muscle: a spindle with fibres, a teal sweatband and a face
  s+=`<g id="calfG">${shaded(MUS_D,C_MUS,C_MUS_S,20)}
    <g clip-path="url(#musClip)">${[490,508,528,548,566,582].map((x,i)=>`<path d="M${x},-460 L${x},-80 C${x+2},200 ${lerp(x,486,.45).toFixed(0)},520 ${lerp(x,486,.92).toFixed(0)},716" fill="none" stroke="#c9444f" stroke-width="2.6" opacity=".75"/>`).join('')}
     <path d="M462,196 C500,182 560,182 612,198 L612,226 C560,210 500,210 462,224 Z" fill="${C_TEAL}" ${OLW2}/><path d="M470,204 C510,192 560,192 604,206" fill="none" stroke="#6fd3cf" stroke-width="4" stroke-linecap="round"/></g>
    <path d="${MUS_D}" fill="none" ${OLW}/>
    <g id="calfFace"><g transform="translate(508,276)">${oEye('cEyeL',25,C_MUS)}</g><g transform="translate(562,276)">${oEye('cEyeR',25,C_MUS)}</g>${brow('cBrL')}${brow('cBrR')}${mouthEl('calf_m',536,332)}</g>
    <g id="sparks"></g></g>`;
  // the vein = the elevator shaft (drawn every frame: it bulges where cells pile up and narrows when the calf squeezes)
  s+=`<path id="veinO" fill="none" stroke="${INK}" stroke-width="14" stroke-linejoin="round"/><path id="veinW" fill="none" stroke="${C_VEIN_W}" stroke-width="8.5" stroke-linejoin="round"/><path id="veinL" fill="${C_VEIN}"/>
   <g clip-path="url(#lumClip)"><path id="veinShine" fill="none" stroke="#b9c7fb" stroke-width="7" stroke-linecap="round" opacity=".8"/>
    <g id="panel"><rect x="361" y="566" width="30" height="64" rx="7" fill="#e3e7ee" ${OLW2}/><path d="M376,574 l-8,12 h16 Z" fill="#7d8697"/><circle id="btn" cx="376" cy="610" r="9.5" fill="#f2b340" ${OLW2}/></g>
    <g id="cellsG"></g>${cellSVG('hA',30,true)}${cellSVG('hB',30,true)}</g>
   <path id="uvL" fill="#f5f7ff" ${OLW2}/><path id="uvR" fill="#f5f7ff" ${OLW2}/>
   <path id="gvL" fill="#f5f7ff" ${OLW2}/><path id="gvR" fill="#f5f7ff" ${OLW2}/>
   <g id="gateG"><rect x="354" y="410" width="112" height="66" rx="14" fill="${C_GATE}" ${OLW}/><path d="M366,422 H454" stroke="#3fb5b0" stroke-width="5" stroke-linecap="round"/>
    <g id="gateCap"><path d="M386,410 C386,388 434,388 434,410 Z" fill="#26346b" ${OLW2}/><path d="M378,410 H442" stroke="${INK}" stroke-width="8" stroke-linecap="round"/><path d="M378,410 H442" stroke="#1a2247" stroke-width="4.5" stroke-linecap="round"/><path d="M405,396 l5,-5 l5,5 l-5,6 Z" fill="#f2c74a" ${OLW2}/></g>
    <g transform="translate(392,442)">${oEye('gEyeL',13,C_GATE)}</g><g transform="translate(428,442)">${oEye('gEyeR',13,C_GATE)}</g>${brow('gBrL')}${brow('gBrR')}${mouthEl('gate_m',410,464)}</g>
   <g id="sock"><path d="M258,838 C320,826 440,826 504,838 L508,960 L262,960 Z" fill="#fbfaf6" ${OLW}/><path d="M262,862 C330,852 436,852 504,862 M263,882 C330,872 436,872 505,882" fill="none" stroke="${C_TEAL}" stroke-width="7"/></g></g>`;
  // ---- the sneaker (turns about its toes when the heel lifts) ----
  s+=`<g id="shoeG">${SHOE_IN}</g>
   <g id="impact"></g></g>`;
  return s;}

// a small copy of the leg for the study card (the same sneaker; the leg comes down from the top of its window)
function miniLeg(id,cx,floorY,x0,y0,ww,hh){
  DEFS+=`<clipPath id="${id}_c"><rect x="${x0}" y="${y0}" width="${ww}" height="${hh}" rx="16"/></clipPath>`;
  return `<rect x="${x0}" y="${y0}" width="${ww}" height="${hh}" rx="16" fill="#e3f4f0"/>
   <g clip-path="url(#${id}_c)"><circle cx="${x0+46}" cy="${y0+70}" r="26" fill="#d3ece7"/><rect x="${x0}" y="${floorY}" width="${ww}" height="60" fill="#d9a66b"/><path d="M${x0},${floorY} h${ww}" stroke="${INK}" stroke-width="3"/>
    <g transform="translate(${cx},${floorY}) scale(.36) translate(-289,-1114)"><ellipse cx="300" cy="1120" rx="290" ry="13" fill="#000" opacity=".14"/>
     <g id="${id}_leg"><path d="M262,-200 C258,300 262,640 270,860 L498,860 C512,760 560,560 592,300 C600,200 600,0 596,-200 Z" fill="#3d4f86" ${OLW}/><path d="M266,792 C330,782 440,782 506,794 L500,842 C440,832 330,832 268,842 Z" fill="#2f3e6b" ${OLW}/>
      <path d="M258,838 C320,826 440,826 504,838 L508,960 L262,960 Z" fill="#fbfaf6" ${OLW}/><path d="M262,862 C330,852 436,852 504,862 M263,882 C330,872 436,872 505,882" fill="none" stroke="${C_TEAL}" stroke-width="7"/></g>
     <g id="${id}_shoe">${SHOE_IN}</g><g id="${id}_imp"></g></g></g>
   <rect x="${x0}" y="${y0}" width="${ww}" height="${hh}" rx="16" fill="none" ${OLW}/>`;}
const ARROW_D='M0,-70 L40,-18 L17,-18 L17,70 L-17,70 L-17,-18 L-40,-18 Z';
function studyCard(){
  DEFS+=`<clipPath id="cardC"><rect x="70" y="60" width="580" height="482" rx="26"/></clipPath>`;
  return `<g id="card" opacity="0"><rect x="78" y="70" width="580" height="482" rx="26" fill="#000" opacity=".13"/>
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

// ---------------- Dr. Mira's clinic (the 012 room) ----------------
function clinicRoom13(){
  return `<rect x="-60" y="-60" width="840" height="1400" fill="#e8f7f5"/>
   <rect x="640" y="-60" width="140" height="1400" fill="#f7fdfc" ${OLW}/>
   <g transform="translate(262,52)"><rect x="0" y="0" width="304" height="192" fill="#2b3b3b" ${OLW}/>${[0,1,2,3].map(i=>`<rect x="10" y="${10+i*45}" width="284" height="36" fill="#c6d4d2"/><rect x="10" y="${36+i*45}" width="284" height="8" fill="#8b9b99"/>`).join('')}</g>
   <rect x="-10" y="432" width="82" height="900" fill="#14a3a0" ${OLW}/><rect x="16" y="462" width="56" height="880" fill="#cfe3e1" ${OLW}/>
   <g transform="translate(520,330)"><rect x="-70" y="-90" width="140" height="180" rx="10" fill="#fff" ${OLW}/><path d="M-12,-40 h24 v28 h28 v24 h-28 v28 h-24 v-28 h-28 v-24 h28 Z" fill="#14a3a0"/>
    <text x="0" y="70" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:20px" fill="#0b6e6b">DR. MIRA</text></g>`;}
