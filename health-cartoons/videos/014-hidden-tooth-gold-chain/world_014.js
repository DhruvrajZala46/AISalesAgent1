// =============== 014: "the hidden tooth and the gold chain". Our own set, all code (013 v2 look) ===============
// Inside a mouth with braces. A canine tooth is asleep in a pocket in the upper gum, above the gap where it should be.
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_GUM='#ff9db3', C_GUM_L='#ffc2cf', C_GUM_D='#ee7f99', C_CAV='#8f2440', C_TOOTH='#ffffff', C_TOOTH_S='#d7e3ee', C_GOLD='#f6c12d', C_GOLD_D='#c98c11', C_STEEL='#b9c3cf', C_TEAL='#14a3a0';
const UPX=[55,205,515,665], GAP=360, UTOP=455, WIRE=633;       // upper teeth centres, the empty seat, where they leave the gum, the wire
const TOOTH_D='M-68,0 L68,0 C76,90 72,172 54,206 C32,232 -32,232 -54,206 C-72,172 -76,90 -68,0Z';
const CAN_D='M-56,-70 C-62,-118 62,-118 56,-70 L50,22 C44,62 14,94 0,104 C-14,94 -44,62 -50,22 Z';
const bracket=(x,y)=>`<g transform="translate(${x},${y})"><rect x="-19" y="-15" width="38" height="30" rx="6" fill="${C_STEEL}" ${OLW2}/><rect x="-10" y="-7" width="20" height="14" rx="3" fill="#8793a3" stroke="${INK}" stroke-width="1.6"/></g>`;
function toothSVG(id,x,face){
  return `<g id="${id}" transform="translate(${x},${UTOP})">${shaded(TOOTH_D,C_TOOTH,C_TOOTH_S,16)}
   ${face?`<g transform="translate(-27,80)">${oEye(id+'_eL',22,'#fff')}</g><g transform="translate(27,80)">${oEye(id+'_eR',22,'#fff')}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',0,134)}`
     :`<circle cx="-24" cy="84" r="15" fill="#fff" ${OLW2}/><circle cx="24" cy="84" r="15" fill="#fff" ${OLW2}/><circle id="${id}_pL" cx="-24" cy="78" r="6.5" fill="${INK}"/><circle id="${id}_pR" cx="24" cy="78" r="6.5" fill="${INK}"/><path d="M-10,128 Q0,134 10,128" fill="none" ${OLW2}/>`}
   ${bracket(0,WIRE-UTOP)}</g>`;}
function mouthWorld(){
  DEFS+=`<clipPath id="pocketC"><ellipse cx="${GAP}" cy="250" rx="100" ry="118"/></clipPath>`;
  let s=`<g id="wMouth"><rect x="-400" y="-500" width="1520" height="2400" fill="${C_CAV}"/>
   <ellipse cx="360" cy="1010" rx="470" ry="250" fill="#f26f86" ${OLW}/><path d="M360,800 C352,900 356,1000 360,1100" fill="none" stroke="#d9546e" stroke-width="6" stroke-linecap="round"/>
   <ellipse cx="200" cy="900" rx="90" ry="40" fill="#f88ea1" opacity=".7"/>`;
  // lower teeth and gum
  s+=`<g id="lowT">${[30,180,330,480,630,780].map((x,i)=>`<g transform="translate(${x},1075) scale(1,-1)">${shaded('M-70,0 L70,0 C76,80 72,150 56,178 C34,198 -34,198 -56,178 C-72,150 -76,80 -70,0Z',C_TOOTH,C_TOOTH_S,14)}</g>${bracket(x,985)}`).join('')}
    <path d="M-400,985 H1120" stroke="${INK}" stroke-width="7"/><path d="M-400,985 H1120" stroke="${C_STEEL}" stroke-width="3.5"/></g>
   <path d="M-400,1500 L-400,1062 ${[-45,105,255,405,555,705,855].map(x=>`Q${x-37},1088 ${x},1040 Q${x+37},1088 ${x+75},1062`).join(' ')} L1120,1062 L1120,1500 Z" fill="${C_GUM}" ${OLW}/>`;
  // upper gum, the pocket in it
  s+=`<rect x="-400" y="-500" width="1520" height="980" fill="${C_GUM}"/><ellipse cx="150" cy="120" rx="260" ry="120" fill="${C_GUM_L}" opacity=".55"/><ellipse cx="640" cy="330" rx="150" ry="70" fill="${C_GUM_L}" opacity=".4"/>
   ${UPX.map(x=>toothSVG('t'+x,x,x===205||x===515)).join('')}
   <path id="wire" d="M-400,${WIRE} H1120" stroke="${INK}" stroke-width="7"/><path d="M-400,${WIRE} H1120" stroke="${C_STEEL}" stroke-width="3.5"/>
   <path d="M-400,-500 L-400,486 L-88,486 ${[55,205].map(x=>`Q${x-70},508 ${x},462 Q${x+70},508 ${x+75},486`).join(' ')} L440,486 ${[515,665].map(x=>`Q${x-70},508 ${x},462 Q${x+70},508 ${x+75},486`).join(' ')} L1120,486 L1120,-500 Z" fill="${C_GUM}"/>
   <path d="M-400,486 L-88,486 ${[55,205].map(x=>`Q${x-70},508 ${x},462 Q${x+70},508 ${x+75},486`).join(' ')} L440,486 ${[515,665].map(x=>`Q${x-70},508 ${x},462 Q${x+70},508 ${x+75},486`).join(' ')} L1120,486" fill="none" ${OLW}/>
   <g id="sign" opacity="0"><path d="M-36,-34 V-6 M36,-34 V-6" stroke="${INK}" stroke-width="3"/><rect x="-62" y="-8" width="124" height="40" rx="7" fill="#fff7d6" ${OLW2}/><text y="19" text-anchor="middle" style="font-family:LG,sans-serif;font-size:21px;letter-spacing:.5px" fill="#d9562f">RESERVED</text></g>
   <g id="pocket" opacity="0"><ellipse cx="${GAP}" cy="250" rx="100" ry="118" fill="#c9506d" ${OLW}/><ellipse cx="${GAP}" cy="250" rx="90" ry="108" fill="none" stroke="#f6e3bf" stroke-width="10" stroke-dasharray="26 12" opacity=".9"/><ellipse cx="${GAP}" cy="262" rx="78" ry="92" fill="#a93655" opacity=".55"/></g>
   <g id="can">${shaded(CAN_D,C_TOOTH,C_TOOTH_S,16)}<g transform="translate(-22,-44)">${oEye('c_eL',19,'#fff')}</g><g transform="translate(22,-44)">${oEye('c_eR',19,'#fff')}</g>${brow('c_bL')}${brow('c_bR')}${mouthEl('c_m',0,2)}
     <g id="cBrk" opacity="0">${bracket(0,58)}</g><g id="btn" opacity="0"><circle cx="0" cy="60" r="14" fill="${C_GOLD}" ${OLW2}/><circle cx="0" cy="60" r="5.5" fill="${C_GOLD_D}"/></g></g>
   <path id="chO" fill="none" stroke="${INK}" stroke-width="12" stroke-linecap="round" stroke-dasharray="15 7"/><path id="chG" fill="none" stroke="${C_GOLD}" stroke-width="7.5" stroke-linecap="round" stroke-dasharray="15 7"/><path id="chH" fill="none" stroke="#fff3b0" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="6 16"/>
   <g id="flap"><ellipse cx="${GAP}" cy="250" rx="102" ry="120" fill="${C_GUM_L}" ${OLW}/><ellipse cx="${GAP-26}" cy="210" rx="34" ry="46" fill="#fff" opacity=".35"/></g>
   <g id="glow"></g><g id="zz"></g><g id="fx"></g>
   <g id="scalpel"><path d="M0,0 L20,-58 L34,-54 L16,-4 Z" fill="#e9eef4" ${OLW2}/><path d="M22,-56 L74,-196 L94,-188 L40,-50 Z" fill="${C_STEEL}" ${OLW2}/><path d="M40,-92 L60,-146" stroke="#8793a3" stroke-width="5" stroke-linecap="round"/></g>
   <g id="tweez" opacity="0"><path d="M0,0 L120,-170 L132,-160 L10,6 Z" fill="${C_STEEL}" ${OLW2}/><path d="M6,8 L140,-150 L150,-138 L12,14 Z" fill="#d9e0e8" ${OLW2}/></g></g>`;
  return s;}
function docBubble(){
  DEFS+=`<clipPath id="dbC"><circle r="92"/></clipPath>`;
  return `<g id="docB" opacity="0"><circle r="100" cx="5" cy="7" fill="#000" opacity=".16"/><circle r="92" fill="#e8f7f5"/><g clip-path="url(#dbC)"><g transform="translate(0,-92) scale(1.02)">${doctorSVG()}</g></g>
   <circle r="92" fill="none" stroke="${C_TEAL}" stroke-width="10"/><circle r="97" fill="none" stroke="${INK}" stroke-width="3.4"/><circle r="87" fill="none" stroke="${INK}" stroke-width="2.4"/>
   <g transform="translate(0,104)"><rect x="-72" y="-17" width="144" height="34" rx="17" fill="#fff" ${OLW2}/><text y="8" text-anchor="middle" style="font-family:LG,sans-serif;font-size:21px;letter-spacing:.5px" fill="#0b6e6b">GIGGLEMD</text></g></g>`;}
