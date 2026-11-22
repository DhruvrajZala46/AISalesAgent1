// =============== 012: why we snore. Three sets, all code in the 001 / 003-v1 style, laid out like the reference ===============
// Set A: a side cut of the throat (the reference's locked shot: skull bone top right, the nose airway, the soft palate, the big
// tongue with its face, the throat tube on the right, the spine at the right edge). Set B: the bedroom slap. Set C: Dr. Mira's clinic.
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const TIS='#b94b58', TIS_D='#a33f4c', AIRC='#74202d', AIRC_D='#5a1823', BONE='#f4e4a6', BONE_D='#e2c77a', TONG='#f08a95', TONG_S='#d76878', PALC='#e8848f', PALC_S='#c9606e', WALL='#c95c69';
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
function vert(y){return `<g transform="translate(0,${y})"><path d="M664,0 C690,-6 740,-6 790,0 L790,70 C740,76 690,76 664,70 C656,48 656,22 664,0 Z" fill="${BONE}" ${OLW}/>
 <circle cx="700" cy="22" r="4" fill="${BONE_D}"/><circle cx="738" cy="44" r="3" fill="${BONE_D}"/><circle cx="716" cy="56" r="3" fill="${BONE_D}"/>
 <path d="M662,74 C690,82 740,82 790,76 L790,88 C740,92 690,92 662,86 Z" fill="#f8efe1" ${OLW}/></g>`;}
// the soft palate: a band from the hard palate to the uvula; droop (0..1) and flap (radians) bend its tail
function palPts(droop,flap){const base=[[206,440],[276,446],[338,466],[388,502],[422,546],[444,592]];
  return base.map(([x,y],i)=>{const k=i/(base.length-1), a=flap*k*k, dx=(x-222), dy=(y-430);
    const cx=222+dx*Math.cos(a)-dy*Math.sin(a), cy=430+dx*Math.sin(a)+dy*Math.cos(a)+droop*k*k*26; return [cx,cy];});}
function bandD(pts,w0,w1){const L=[],R=[];for(let i=0;i<pts.length;i++){const a=pts[Math.max(0,i-1)],b=pts[Math.min(pts.length-1,i+1)];let dx=b[0]-a[0],dy=b[1]-a[1];const d=Math.hypot(dx,dy)||1;dx/=d;dy/=d;
  const w=(w0+(w1-w0)*i/(pts.length-1))/2;L.push([pts[i][0]-dy*w,pts[i][1]+dx*w]);R.push([pts[i][0]+dy*w,pts[i][1]-dx*w]);}
  const e=pts[pts.length-1], r=w1/2; return smooth(L)+` A${r},${r} 0 0 0 ${R[R.length-1][0].toFixed(1)},${R[R.length-1][1].toFixed(1)} `+smooth(R.slice().reverse()).replace(/^M[^C]*/,'')+'Z';}
// an air puff: a small cloud with a face
function puffSVG(id,c1,c2){const bl=[[-30,6,22],[-10,-14,24],[16,-12,22],[32,6,20],[6,14,24],[-18,16,18]];
  return `<g id="${id}"><g id="${id}_b">${bl.map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${c1}" ${OLW}/>`).join('')}${bl.map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r-3.4}" fill="${c1}"/>`).join('')}
  <path d="M-34,10 C-20,26 20,26 36,10" fill="none" stroke="${c2}" stroke-width="6" stroke-linecap="round" opacity=".8"/><path d="M-14,-24 C-4,-30 10,-30 18,-24" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
  <g transform="translate(-10,-2)">${oEye(id+'_eL',10,c1)}</g><g transform="translate(12,-2)">${oEye(id+'_eR',10,c1)}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',1,14)}</g></g>`;}
function throatWorld(){
  let s=`<g id="wThroat"><rect x="-80" y="-80" width="880" height="1440" fill="${TIS}"/>
   ${[[60,150,140],[120,250,120],[40,720,90],[90,1150,120],[600,1180,80]].map(([x,y,w])=>`<path d="M${x},${y} c${w/3},-14 ${w*2/3},10 ${w},-4" fill="none" stroke="${TIS_D}" stroke-width="5" stroke-linecap="round" opacity=".7"/>`).join('')}
   <path d="M576,300 C590,500 584,900 588,1340 L680,1340 L680,300 Z" fill="${WALL}"/><path d="M576,300 C590,500 584,900 588,1340" fill="none" ${OLW}/>
   ${[360,452,544,636,728,820,912,1004,1096,1188,1280].map(vert).join('')}
   <path d="M210,-60 C236,110 330,214 482,246 C594,270 690,300 800,366 L800,-60 Z" fill="${BONE}" ${OLW}/>
   <path d="M236,-60 C262,96 350,192 488,222 C596,244 690,276 800,334" fill="none" stroke="${BONE_D}" stroke-width="8" opacity=".6"/>
   <ellipse cx="460" cy="96" rx="124" ry="70" fill="#9c3a47" ${OLW}/><path d="M360,92 C400,60 500,52 560,82" fill="none" stroke="#b9525e" stroke-width="8" stroke-linecap="round" opacity=".8"/>
   ${[[300,30,3],[610,40,4],[690,150,3],[560,200,3],[260,140,3]].map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${BONE_D}"/>`).join('')}`;
  // the air spaces: the nose passage, the back of the nose, the throat tube; and the gap of the mouth
  const AIRW='M150,372 C230,362 300,356 360,352 C440,346 506,354 538,394 C560,432 564,520 560,640 C556,820 552,1000 546,1340';
  s+=`${[[20,352,150],[40,300,170],[60,250,150]].map(([x,y,wd])=>`<path d="M${x},${y} C${x+wd*.3},${y-26} ${x+wd*.75},${y-20} ${x+wd},${y-4}" fill="none" stroke="#9d3846" stroke-width="16" stroke-linecap="round" opacity=".55"/>`).join('')}
   <path d="${AIRW}" fill="none" stroke="${INK}" stroke-width="64" stroke-linecap="round"/><path d="${AIRW}" fill="none" stroke="${AIRC}" stroke-width="57" stroke-linecap="round"/>
   <path d="${AIRW}" fill="none" stroke="${AIRC_D}" stroke-width="22" stroke-linecap="round" opacity=".6"/>
   <path d="M-80,452 C120,452 300,460 400,486 C460,506 500,560 520,640 L520,700 C470,640 380,606 250,596 C120,588 30,596 -80,604 Z" fill="${AIRC}"/>
   <path d="M-80,400 C60,394 160,396 240,410 L238,474 C150,466 60,462 -80,466 Z" fill="${PALC}" ${OLW}/><path d="M-80,414 C60,408 160,410 236,420 L236,436 C150,428 60,426 -80,430 Z" fill="${BONE}" opacity=".9"/>
   
   ${[[60,350,120],[150,344,110]].map(([x,y,w])=>`<path d="M${x},${y} c${w/3},-12 ${w*2/3},-12 ${w},0" fill="none" stroke="#9d3846" stroke-width="5" stroke-linecap="round" opacity=".8"/>`).join('')}`;
  // floor of the mouth, the jaw bone and the hyoid (bottom left), the epiglottis at the tongue's root
  s+=`<path d="M-80,1060 C80,1040 230,1050 320,1100 C352,1150 320,1206 220,1218 C110,1230 0,1224 -80,1220 Z" fill="${BONE}" ${OLW}/>
   <path d="M-60,1100 C80,1088 210,1096 286,1130 C296,1160 270,1186 210,1190 C110,1198 10,1194 -60,1190 Z" fill="#ead08a"/>
   <path d="M-80,1236 L760,1236 L760,1340 L-80,1340 Z" fill="#8f4a46"/>
   <ellipse cx="392" cy="1102" rx="40" ry="20" fill="${BONE}" ${OLW}/>
   <path d="M486,968 C500,940 520,900 528,870 C532,856 546,858 544,874 C540,912 526,952 506,984 Z" fill="#ee9aa2" ${OLW}/>`;
  // the tongue: big, relaxed and fallen back against the throat (the snoring position)
  const TD='M-80,606 C80,584 220,580 330,598 C430,614 500,664 518,744 C532,822 520,900 488,962 C452,1018 384,1040 300,1042 C200,1044 60,1032 -80,1022 Z';
  s+=`<g id="tongueG">${shaded(TD,TONG,TONG_S,22)}<path d="M-40,640 C100,618 260,622 400,664" fill="none" stroke="#f7aab2" stroke-width="7" stroke-linecap="round" opacity=".8"/>
   <path d="M150,860 C220,900 300,900 360,870" fill="none" stroke="${TONG_S}" stroke-width="4" stroke-linecap="round" opacity=".6"/>
   <g id="tFace"><g id="tOpen"><g transform="translate(312,708)">${oEye('tEyeL',34,TONG)}</g><g transform="translate(402,708)">${oEye('tEyeR',34,TONG)}</g></g><path id="tShut" d="M284,712 Q312,734 340,712 M374,712 Q402,734 430,712" fill="none" stroke="${INK}" stroke-width="5" stroke-linecap="round" opacity="0"/>${brow('tBrL')}${brow('tBrR')}${mouthEl('tongue_m',358,792)}</g>
   <g id="zzz"></g></g>`;
  // the soft palate (drawn each frame) with its face
  s+=`<g id="palG"><path id="palBody" fill="${PALC}" ${OLW}/><path id="palHi" fill="none" stroke="#f6aab3" stroke-width="5" stroke-linecap="round" opacity=".8"/>
   <g id="palFace"><g id="paOpen"><g transform="translate(272,446)">${oEye('paEyeL',14,PALC)}</g><g transform="translate(310,454)">${oEye('paEyeR',14,PALC)}</g></g><path id="paShut" d="M260,448 Q272,458 284,448 M298,456 Q310,466 322,456" fill="none" stroke="${INK}" stroke-width="3.4" stroke-linecap="round"/>${brow('paBrL')}${brow('paBrR')}${mouthEl('palate_m',294,476)}</g></g>`;
  s+=`<g id="flow"></g>${puffSVG('pf1','#f3fbff','#b8def2')}${puffSVG('pf2','#e8f4ff','#a9c9ef')}<g id="vibes"></g></g>`;
  return s;}

// ---------------- SET B: the bedroom (the reference's last shot: his face on the pillow, the partner's slap) ----------------
function bedroomWorld(pat){
  return `<g id="wBed"><rect x="-60" y="-60" width="840" height="1400" fill="#fbf4ec"/>
   ${[110,180].map(y=>`<path d="M-60,${y} C200,${y-8} 500,${y+6} 780,${y-4}" fill="none" stroke="#efe2d2" stroke-width="5"/>`).join('')}
   <path d="M-30,250 C40,200 680,196 750,246 C786,330 790,690 754,770 C680,812 40,816 -30,772 C-70,690 -70,330 -30,250 Z" fill="#c9a27a" ${OLW}/>
   <path d="M10,300 C200,262 520,262 710,300" fill="none" stroke="#dcbb94" stroke-width="10" stroke-linecap="round" opacity=".7"/>
   ${[[60,420,40],[650,460,-30],[90,640,20],[640,660,-20]].map(([x,y,r])=>`<path d="M${x},${y} q${r},18 ${r*1.6},44" fill="none" stroke="#a88160" stroke-width="4" stroke-linecap="round"/>`).join('')}
   <g transform="translate(372,240) scale(3)">${pat}</g>
   <path d="M-60,1000 C140,950 420,968 780,1004 L780,1340 L-60,1340 Z" fill="#f1d9bf" ${OLW}/>
   <path d="M60,1060 C200,1040 360,1050 470,1080 M380,1150 C500,1130 620,1140 720,1170" fill="none" stroke="#dcbc9b" stroke-width="6" stroke-linecap="round"/>
   <g id="snoreW"></g>
   <g id="slapArm" opacity="0"><path id="saO" fill="none" stroke="${INK}" stroke-width="86" stroke-linecap="round" stroke-linejoin="round"/><path id="saS" fill="none" stroke="#d96f9c" stroke-width="78" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="saK" fill="none" stroke="${INK}" stroke-width="62" stroke-linecap="round"/><path id="saKi" fill="none" stroke="#f0c19c" stroke-width="55" stroke-linecap="round"/><g id="saH"></g></g>
   <g id="impact"></g></g>`;}
function slapHand(x,y,rot,s){return `<g transform="translate(${x},${y}) rotate(${rot}) scale(${s})"><path d="M-30,-10 C-34,-40 -20,-56 0,-56 C22,-56 34,-40 30,-10 L30,26 C30,44 14,54 0,54 C-14,54 -30,44 -30,26 Z" fill="#f0c19c" ${OLW}/>
  ${[[-22,-50,-8],[-7,-62,-3],[8,-62,3],[22,-52,8]].map(([fx,fy,r])=>`<rect x="${fx-7}" y="${fy-30}" width="14" height="40" rx="7" fill="#f0c19c" transform="rotate(${r},${fx},${fy})" ${OLW}/>`).join('')}
  <rect x="-40" y="-4" width="16" height="36" rx="8" fill="#f0c19c" transform="rotate(-30,-32,12)" ${OLW}/></g>`;}
// the handprint the slap leaves on his cheek (local coordinates of the 001 patient head)
const HANDPRINT=`<g id="pHandprint" opacity="0" transform="translate(-30,112) rotate(-14)"><path d="M-12,-4 C-14,-16 -8,-22 0,-22 C9,-22 14,-16 12,-4 L12,10 C12,17 6,21 0,21 C-6,21 -12,17 -12,10 Z" fill="#f08d97" opacity=".85"/>
  ${[[-9,-20],[-3,-25],[3,-25],[9,-21]].map(([x,y])=>`<rect x="${x-2.6}" y="${y-13}" width="5.2" height="15" rx="2.6" fill="#f08d97" opacity=".85"/>`).join('')}</g>`;

// ---------------- SET C: Dr. Mira's clinic (the reference's plain room, in our teal and mint) ----------------
function clinicRoom12(){
  return `<rect x="-60" y="-60" width="840" height="1400" fill="#e8f7f5"/>
   <rect x="640" y="-60" width="140" height="1400" fill="#f7fdfc" ${OLW}/>
   <g transform="translate(262,52)"><rect x="0" y="0" width="304" height="192" fill="#2b3b3b" ${OLW}/>${[0,1,2,3].map(i=>`<rect x="10" y="${10+i*45}" width="284" height="36" fill="#c6d4d2"/><rect x="10" y="${36+i*45}" width="284" height="8" fill="#8b9b99"/>`).join('')}</g>
   <rect x="-10" y="432" width="82" height="900" fill="#14a3a0" ${OLW}/><rect x="16" y="462" width="56" height="880" fill="#cfe3e1" ${OLW}/>
   <g transform="translate(520,330)"><rect x="-70" y="-90" width="140" height="180" rx="10" fill="#fff" ${OLW}/><path d="M-12,-40 h24 v28 h28 v24 h-28 v28 h-24 v-28 h-28 v-24 h28 Z" fill="#14a3a0"/>
    <text x="0" y="70" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:20px" fill="#0b6e6b">DR. MIRA</text></g>`;}
