// =============== 021: how cutting your toenails can cause an ingrown toenail. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_SK='#f3dccb', C_SK_S='#e6b9a6', C_NAIL='#f9e6da', C_RED='#e2504a', C_MET='#d9dde2', C_MET_D='#b4bac2';
const BIG_D='M-40,1330 L-40,650 C-40,520 60,446 200,446 C340,446 436,530 436,664 C436,800 384,900 344,1040 C322,1120 318,1220 322,1330 Z';
const SEC_D='M440,1330 C428,1100 418,900 424,704 C426,600 482,536 572,536 C662,536 718,600 718,704 C718,900 704,1100 694,1330 Z';
// the big toe's nail: top edge y, corner radius r, half-width grows with w
function nailD(top,r,w=0){const x0=48-w,x1=402+w;return `M${x0},780 L${x0},${top+r} Q${x0},${top} ${x0+r},${top} L${x1-r},${top} Q${x1},${top} ${x1},${top+r} L${x1},780 Q${x1},842 ${x1-62},842 L${x0+62},842 Q${x0},842 ${x0},780 Z`;}
const arcsD=(n=3)=>Array.from({length:n},(_,j)=>`<path d="M${-34-j*4},${-j*24} q${34+j*4},-26 ${68+j*8},0" fill="none" stroke="${INK}" stroke-width="19" stroke-linecap="round"/><path d="M${-34-j*4},${-j*24} q${34+j*4},-26 ${68+j*8},0" fill="none" stroke="#ffe81a" stroke-width="12" stroke-linecap="round"/>`).join('');
function clipperSVG(){return `<g id="clip"><path d="M-66,-150 L66,-150 L92,124 L-92,124 Z" fill="${C_MET}" ${OLW}/><path d="M-98,124 L98,124 L104,168 L-104,168 Z" fill="${C_MET_D}" ${OLW}/><path d="M-98,140 H98" ${OLW2}/>
   <path d="M-44,-196 L44,-196 L58,70 L-58,70 Z" fill="#f1f3f6" ${OLW}/><path d="M-30,-180 L-40,50" stroke="#fff" stroke-width="8" stroke-linecap="round"/>
   <rect id="cmouth" x="-17" y="-70" width="34" height="70" rx="15" fill="#2a2326" ${OLW2}/><ellipse id="ctong" cx="0" cy="-20" rx="10" ry="8" fill="#e8474f" opacity="0"/>
   <circle cx="0" cy="44" r="17" fill="#8c939c" ${OLW2}/>
   <g id="carms" opacity="0"><path d="M-70,-40 C-120,-80 -110,-140 -44,-128 M70,-40 C120,-80 110,-140 44,-128" fill="none" stroke="${INK}" stroke-width="13" stroke-linecap="round"/><path d="M-70,-40 C-120,-80 -110,-140 -44,-128 M70,-40 C120,-80 110,-140 44,-128" fill="none" stroke="${C_MET}" stroke-width="7" stroke-linecap="round"/><circle cx="-38" cy="-124" r="13" fill="#fff" ${OLW2}/><circle cx="38" cy="-124" r="13" fill="#fff" ${OLW2}/></g>
   <g transform="translate(0,-176)"><g transform="translate(-36,0)">${oEye('cl_eL',34,'#f1f3f6')}</g><g transform="translate(36,0)">${oEye('cl_eR',34,'#f1f3f6')}</g>${brow('cl_bL')}${brow('cl_bR')}</g></g>`;}
function footCard(){return `<g id="inset"><rect x="500" y="170" width="204" height="300" rx="18" fill="#fff" ${OLW}/>
   <path d="M560,430 C540,380 548,300 566,260 C584,228 650,228 660,268 C672,320 664,390 650,430 C630,450 580,450 560,430 Z" fill="${C_SK}" ${OLW2}/>
   ${[[574,232,20,26],[608,226,15,20],[632,232,13,18],[652,244,12,16],[668,260,11,14]].map(([x,y,a,b])=>`<ellipse cx="${x}" cy="${y}" rx="${a}" ry="${b}" fill="${C_SK}" ${OLW2}/>`).join('')}
   <path d="M562,222 q12,-12 24,0 v14 h-24 Z" fill="#fff" ${OLW2}/><circle id="ring" cx="574" cy="230" r="30" fill="none" stroke="#e02626" stroke-width="6"/>
   <text x="602" y="456" text-anchor="middle" style="font-family:LG,sans-serif;font-size:21px" fill="#1d2a44">BIG TOE NAIL</text></g>`;}
// ---- scene 1: two toes and the clipper ----
function toesScene(){
  DEFS+=`<clipPath id="bigC"><path d="${BIG_D}"/></clipPath><clipPath id="secC"><path d="${SEC_D}"/></clipPath><clipPath id="nailC"><path id="nailCP" d="${nailD(430,40)}"/></clipPath><filter id="soft2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="16"/></filter>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#d8e9f6"/><rect x="-40" y="90" width="800" height="110" fill="#b7cfe2" filter="url(#soft2)"/>
   <g id="stink"></g>
   <path d="${SEC_D}" fill="${C_SK}" ${OLW}/><g clip-path="url(#secC)"><path d="${SEC_D}" fill="none" stroke="${C_SK_S}" stroke-width="26" opacity=".7"/></g><path d="${SEC_D}" fill="none" ${OLW}/>
   <path d="M462,640 Q462,566 530,566 L622,566 Q690,566 690,640 L690,720 Q690,764 646,764 L506,764 Q462,764 462,720 Z" fill="${C_NAIL}" ${OLW}/><path d="M476,596 Q486,572 530,572 L622,572 Q668,572 678,596" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round"/>
   <g id="tface" transform="translate(576,660)"><g transform="translate(-42,0)">${oEye('t2_eL',36,C_NAIL)}</g><g transform="translate(42,0)">${oEye('t2_eR',36,C_NAIL)}</g>${brow('t2_bL')}${brow('t2_bR')}<g transform="translate(0,62) scale(1.6)">${mouthEl('t2_m',0,0)}</g></g>
   <path d="${BIG_D}" fill="${C_SK}" ${OLW}/><g clip-path="url(#bigC)"><path d="${BIG_D}" fill="none" stroke="${C_SK_S}" stroke-width="34" opacity=".75"/><g id="swell"></g></g><path d="${BIG_D}" fill="none" ${OLW}/>
   <path d="M60,1070 q60,-14 110,6 M40,1100 q70,-10 120,10 M90,1130 q40,-6 80,6" fill="none" ${OLW2}/>
   <path id="nail" d="${nailD(430,40)}" fill="${C_NAIL}" ${OLW}/><g clip-path="url(#nailC)"><rect id="free" x="0" y="400" width="460" height="70" fill="#fff"/><path id="freeL" d="M0,500 H460" stroke="${INK}" stroke-width="2.4"/></g><path id="nailO" d="${nailD(430,40)}" fill="none" ${OLW}/>
   <g id="swell2"></g><path id="dash" d="" fill="none" stroke="#2fd24a" stroke-width="10" stroke-dasharray="26 16" stroke-linecap="round" opacity="0"/>
   <g id="bface" transform="translate(225,650)"><g id="bOpen"><g transform="translate(-68,0)">${oEye('bt_eL',40,C_NAIL)}</g><g transform="translate(68,0)">${oEye('bt_eR',40,C_NAIL)}</g></g>
     <g id="bShut" opacity="0">${[-68,68].map(x=>`<g transform="translate(${x},0) scale(1.4)"><ellipse rx="37" ry="40" fill="#fff" ${OLW2}/><path d="M${x<0?-16:16},-16 L${x<0?12:-12},0 L${x<0?-16:16},16" fill="none" stroke="${INK}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></g>`).join('')}</g>
     ${brow('bt_bL')}${brow('bt_bR')}<g transform="translate(0,104) scale(2.3)">${mouthEl('bt_m',0,0)}</g></g>
   <g id="chip" opacity="0"><path d="M-70,10 C-40,-30 40,-30 70,10 C40,-6 -40,-6 -70,10 Z" fill="#fff" ${OLW2}/></g>
   <g id="spark"></g>
   ${footCard()}
   <g id="clipW">${clipperSVG()}</g>`;}
// ---- the clinic ----
function miniToe(id,x,y,bad){const top=bad?-70:-96,r=bad?70:22;
  return `<g id="${id}" opacity="0"><g transform="translate(${x},${y})"><path d="M-104,150 L-104,-40 C-104,-120 104,-120 104,-40 L104,150 Z" fill="${C_SK}" ${OLW}/>
   ${bad?`<ellipse cx="-80" cy="-10" rx="30" ry="60" fill="${C_RED}" opacity=".85" filter="url(#soft)"/><ellipse cx="80" cy="-10" rx="30" ry="60" fill="${C_RED}" opacity=".85" filter="url(#soft)"/>`:''}
   <path d="M-74,70 L-74,${top+r} Q-74,${top} ${-74+r},${top} L${74-r},${top} Q74,${top} 74,${top+r} L74,70 Q74,100 44,100 L-44,100 Q-74,100 -74,70 Z" fill="${C_NAIL}" ${OLW}/>
   <path d="M${-74+r*.5},${top+10} Q0,${top-(bad?6:0)} ${74-r*.5},${top+10}" fill="none" stroke="${bad?'#e02626':'#22b04a'}" stroke-width="9" stroke-dasharray="18 12" stroke-linecap="round"/>
   <circle cx="96" cy="-104" r="38" fill="${bad?'#e8473f':'#2fae62'}" stroke="#1d2a44" stroke-width="4"/>${bad?`<path d="M80,-120 L112,-88 M112,-120 L80,-88" stroke="#fff" stroke-width="10" stroke-linecap="round"/>`:`<path d="M78,-104 L92,-88 L116,-120" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>`}
   <rect x="-124" y="168" width="248" height="56" rx="12" fill="${bad?'#e8473f':'#2fae62'}" stroke="#1d2a44" stroke-width="4"/><text x="0" y="207" text-anchor="middle" style="font-family:LG,sans-serif;font-size:26px" fill="#fff">${bad?'ROUND CORNERS':'STRAIGHT ACROSS'}</text></g></g>`;}
function clinic21(){
  return `<rect x="-60" y="-60" width="840" height="1400" fill="#b9c6cc"/><path d="M-60,560 H780 M240,-60 V1000 M520,-60 V1000" stroke="#a3b1b8" stroke-width="6"/>
   <path d="M-60,1010 H780 V1400 H-60 Z" fill="#8f8d8a"/><path d="M-60,1010 H780 M-60,1120 H780 M140,1010 L60,1340 M400,1010 L390,1340 M640,1010 L720,1340" stroke="#74726f" stroke-width="3" fill="none"/>
   <g id="brd"><rect x="38" y="46" width="660" height="470" rx="26" fill="#000" opacity=".12"/><rect x="30" y="36" width="660" height="470" rx="26" fill="#fff" stroke="#1d2a44" stroke-width="5"/>
    ${miniToe('m0',196,200,true)}${miniToe('m1',524,200,false)}
    <g id="m2" opacity="0"><text x="360" y="486" text-anchor="middle" style="font-family:LG,sans-serif;font-size:30px" fill="#1d2a44">NAIL GROWS OUT, NOT INTO THE SKIN</text></g></g>
   <g transform="translate(176,540) scale(.8)">${doctorSVG()}</g>
   <g transform="translate(274,806) rotate(160) scale(.27)"><path d="M-66,-150 L66,-150 L92,124 L-92,124 Z" fill="${C_MET}" ${OLW}/><path d="M-98,124 L98,124 L104,168 L-104,168 Z" fill="${C_MET_D}" ${OLW}/><path d="M-44,-196 L44,-196 L58,70 L-58,70 Z" fill="#f1f3f6" ${OLW}/></g>
   <path d="M-60,950 H330 V990 H-60 Z" fill="#8a7a6c" ${OLW}/><path d="M150,990 H310 V1200 H150 Z" fill="#7d6e62" ${OLW}/>
   <g id="patWrap"><path d="M660,700 H730 V960 H660 Z" fill="#5a95d0" ${OLW}/>
    <g transform="translate(560,540) scale(.8)">${patientSVG()}</g>
    <path d="M410,925 H730 V1010 H410 Z" fill="#6aa5e0" ${OLW}/><path d="M440,1010 H730 V1200 H440 Z" fill="#c9cdd2" ${OLW}/><path d="M440,1040 H730" ${OLW2}/>
    <path d="M520,960 L440,1030" stroke="${INK}" stroke-width="5" stroke-dasharray="10 9" stroke-linecap="round"/>
    <g id="pfoot" transform="translate(400,1110)"><circle r="122" fill="#fff" ${OLW}/><circle r="122" fill="none" stroke="#e02626" stroke-width="7" stroke-dasharray="16 10"/>
     <path d="M-66,110 L-66,-20 C-66,-90 66,-90 66,-20 L66,110 Z" fill="${PSK}" ${OLW}/><ellipse cx="-54" cy="6" rx="22" ry="48" fill="${C_RED}" opacity=".9" filter="url(#soft)"/><ellipse cx="54" cy="6" rx="22" ry="48" fill="${C_RED}" opacity=".9" filter="url(#soft)"/>
     <path d="M-44,60 L-44,-10 Q-44,-52 0,-52 Q44,-52 44,-10 L44,60 Q44,80 24,80 L-24,80 Q-44,80 -44,60 Z" fill="${C_NAIL}" ${OLW}/><g id="pain"></g></g></g>`;}
