// =============== 017: blackheads, the peel-off mask and salicylic acid. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_OIL='#d6c35a', C_OIL_L='#e9dc8c', C_TEAL='#14a3a0', SURF=470;
const PORES={big:{cx:360,r:150},sL:{cx:112,r:70},sR:{cx:608,r:70}};
Object.values(PORES).forEach(p=>{p.n=p.r*.36;p.cy=SURF+p.r*1.75;p.bot=p.cy+p.r;
  p.d=`M${p.cx-p.n},${SURF-6} C${p.cx-p.n},${SURF+p.r*.55} ${p.cx-p.r},${SURF+p.r*.75} ${p.cx-p.r},${p.cy} A${p.r},${p.r} 0 0 0 ${p.cx+p.r},${p.cy} C${p.cx+p.r},${SURF+p.r*.75} ${p.cx+p.n},${SURF+p.r*.55} ${p.cx+p.n},${SURF-6} Z`;});
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
function poreSVG(id,er,mw){const p=PORES[id];
  DEFS+=`<clipPath id="${id}_c"><path d="${p.d}"/></clipPath><clipPath id="${id}_lc"><rect id="${id}_lr" x="${p.cx-p.r-10}" y="${SURF}" width="${p.r*2+20}" height="${p.r*3}"/></clipPath>`;
  const bub=Array.from({length:id==='big'?16:8},(_,i)=>{const a=rnd(i+p.r)*6.28,d=Math.sqrt(rnd(i*3+p.cx))*p.r*.82;return `<circle cx="${(p.cx+Math.cos(a)*d).toFixed(0)}" cy="${(p.cy+Math.sin(a)*d*.9).toFixed(0)}" r="${(p.r*(.08+rnd(i*7)*.13)).toFixed(0)}" fill="${C_OIL_L}" opacity=".85"/>`;}).join('');
  return `<path d="${p.d}" fill="#fbdcc0" stroke="${INK}" stroke-width="24" stroke-linejoin="round"/><path d="${p.d}" fill="#fbdcc0" stroke="#f6c9a6" stroke-width="17" stroke-linejoin="round"/>
   <g clip-path="url(#${id}_c)"><g clip-path="url(#${id}_lc)"><rect x="${p.cx-p.r-10}" y="${SURF-20}" width="${p.r*2+20}" height="${p.r*3.2}" fill="${C_OIL}"/>${bub}</g>
    <g id="${id}_dark"><rect x="${-p.r-10}" y="-30" width="${p.r*2+20}" height="${p.r*.42+30}" fill="#19130f"/><rect x="${-p.r-10}" y="${p.r*.42-1}" width="${p.r*2+20}" height="${p.r*.8}" fill="url(#darkG)"/></g>
    <path id="${id}_surf" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity="0"/></g>
   <g id="${id}_face"><g transform="translate(${-er*1.15},0)">${oEye(id+'_eL',er,C_OIL)}</g><g transform="translate(${er*1.15},0)">${oEye(id+'_eR',er,C_OIL)}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',0,er*1.9)}</g>`;}
function skinWorld(){
  DEFS+=`<linearGradient id="darkG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#19130f"/><stop offset="1" stop-color="#19130f" stop-opacity="0"/></linearGradient>`;
  const top='M-140,472 C80,462 200,476 330,468 C460,460 600,476 860,468';
  let s=`<g id="skin" transform="translate(360,500) scale(1.15) translate(-360,-470)"><rect x="-140" y="-540" width="1000" height="2100" fill="#cfe6f5"/>
   <path d="${top} L860,1420 L-140,1420 Z" fill="#fde3c6"/><path d="M-140,566 H860 V1420 H-140 Z" fill="#f7b7c7"/><path d="M-140,556 H860 V582 H-140 Z" fill="#f28d9f"/>
   <path d="M-40,1050 C80,1020 200,1070 330,1040 C460,1012 600,1066 760,1036 L760,1320 L-40,1320 Z" fill="#ec9fb6"/><path d="M-40,1190 C100,1170 260,1210 400,1184 C540,1160 660,1200 760,1180 L760,1320 L-40,1320 Z" fill="#e08ca8"/>
   ${[[230,500],[250,520],[470,496],[500,522],[560,506],[200,530],[690,520],[30,512]].map(([x,y],i)=>`<ellipse cx="${x}" cy="${y}" rx="${7+i%3*2}" ry="3.5" fill="#c9825f" opacity=".7"/>`).join('')}
   ${[[150,760],[560,820],[230,940],[620,980],[90,900],[470,960]].map(([x,y])=>`<ellipse cx="${x}" cy="${y}" rx="26" ry="8" fill="#f29db3" opacity=".7"/>`).join('')}
   <path d="${top}" fill="none" ${OLW}/>
   ${poreSVG('sL',19,8)}${poreSVG('sR',19,8)}${poreSVG('big',40,20)}
   <g id="drops"></g>
   <g id="mask"><path id="maskP" fill="#17171a" ${OLW}/><path id="maskHi" fill="none" stroke="#5a5a62" stroke-width="5" stroke-linecap="round"/><g id="maskDry" opacity="0">${Array.from({length:46},(_,i)=>`<circle cx="${(rnd(i)*760-20).toFixed(0)}" cy="${(392+rnd(i*5)*78).toFixed(0)}" r="${(1.6+rnd(i*9)*2).toFixed(1)}" fill="#8a8a92"/>`).join('')}
     <path d="M120,400 l14,28 l-10,26 M330,396 l-12,30 l14,28 M540,400 l12,26 l-12,28 M650,398 l-8,42" fill="none" stroke="#6b6b73" stroke-width="3" stroke-linecap="round"/></g>
    <g id="tops" opacity="0">${['sL','sR'].map(k=>{const p=PORES[k];return `<path d="M${p.cx-p.n+3},470 L${p.cx+p.n-3},470 L${p.cx+p.n*1.5},${470+p.r*.7} C${p.cx},${470+p.r*.95} ${p.cx},${470+p.r*.95} ${p.cx-p.n*1.5},${470+p.r*.7} Z" fill="#19130f" ${OLW2}/>`;}).join('')}</g></g>
   <g id="brush"><path d="M0,0 L150,-420" stroke="${INK}" stroke-width="30" stroke-linecap="round"/><path d="M0,0 L150,-420" stroke="#e7a85c" stroke-width="23" stroke-linecap="round"/><path d="M-34,34 C-44,6 -20,-22 10,-28 C40,-30 54,0 44,30 C30,52 -18,54 -34,34 Z" fill="#232326" ${OLW}/></g>
   <g id="bottle"><path d="M0,0 L-7,-46 L7,-46 Z" fill="#e8f6ff" ${OLW2}/><rect x="-24" y="-128" width="48" height="84" rx="8" fill="#232326" ${OLW}/><path d="M-24,-104 h48 M-24,-84 h48" stroke="#4a4a52" stroke-width="5"/>
     <rect x="-70" y="-336" width="140" height="212" rx="20" fill="#d8eefb" ${OLW}/><path d="M-52,-316 v170" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".8"/>
     <rect x="-58" y="-232" width="116" height="78" rx="6" fill="#fff" ${OLW2}/><text x="0" y="-200" text-anchor="middle" style="font-family:LG,sans-serif;font-size:24px" fill="#1d2a44">SALICYLIC</text><text x="0" y="-170" text-anchor="middle" style="font-family:LG,sans-serif;font-size:24px" fill="#1d2a44">ACID</text>
     <g transform="translate(0,-280)"><g transform="translate(-24,0)">${oEye('ac_eL',19,'#d8eefb')}</g><g transform="translate(24,0)">${oEye('ac_eR',19,'#d8eefb')}</g>${brow('ac_bL')}${brow('ac_bR')}${mouthEl('ac_m',0,30)}</g></g>
   <g id="fx"></g></g>`;
  return s;}
// ---- the clinic: a cheat sheet board over our doctor and patient ----
function clinic17(){
  const card=(x,ttl,sub,ok,col,l1,l2,foot,id)=>`<g id="${id}" opacity="0"><rect x="${x}" y="170" width="290" height="340" rx="18" fill="#fff" stroke="#1d2a44" stroke-width="4"/>
    <text x="${x+145}" y="214" text-anchor="middle" style="font-family:LG,sans-serif;font-size:27px" fill="#1d2a44">${ttl}</text><text x="${x+145}" y="246" text-anchor="middle" style="font-family:LG,sans-serif;font-size:${sub.length>12?19:27}px" fill="#1d2a44">${sub}</text>
    <path d="M${x+131},266 h28 l-14,18 Z" fill="#8a94a6"/>
    <rect x="${x+16}" y="300" width="258" height="112" rx="16" fill="${col}" stroke="#1d2a44" stroke-width="3.4"/><text x="${x+145}" y="346" text-anchor="middle" style="font-family:LG,sans-serif;font-size:25px" fill="#fff">${l1}</text><text x="${x+145}" y="384" text-anchor="middle" style="font-family:LG,sans-serif;font-size:25px" fill="#fff">${l2}</text>
    <text x="${x+145}" y="462" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:21px" fill="#1d2a44">${foot}</text>
    <g transform="translate(${x+268},180)"><circle r="27" fill="${ok?'#2fae62':'#e8473f'}" stroke="#1d2a44" stroke-width="3.4"/>${ok?'<path d="M-12,1 l8,9 l15,-17" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>':'<path d="M-10,-10 L10,10 M10,-10 L-10,10" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'}</g></g>`;
  return `<rect x="-60" y="-60" width="840" height="1400" fill="#dcefe9"/>
   <rect x="38" y="52" width="656" height="494" rx="24" fill="#000" opacity=".12"/><rect x="30" y="40" width="660" height="494" rx="24" fill="#fff" stroke="#1d2a44" stroke-width="5"/>
   <text x="360" y="118" text-anchor="middle" style="font-family:LG,sans-serif;font-size:60px;letter-spacing:2px" fill="#1d2a44">CHEAT SHEET</text>
   ${card(52,'PEEL-OFF','MASK',false,'#e8473f','ONLY PULLS','THE TOP OFF','the pore fills right back up','cd1')}${card(378,'SALICYLIC ACID','A FEW TIMES A WEEK',true,'#2fae62','DISSOLVES OIL','INSIDE THE PORE','cleanser or serum','cd2')}
   <g id="cd3" opacity="0"><rect x="110" y="556" width="500" height="64" rx="32" fill="#e8473f" stroke="#1d2a44" stroke-width="4"/><text x="360" y="601" text-anchor="middle" style="font-family:LG,sans-serif;font-size:35px;letter-spacing:1px" fill="#fff">DON'T SQUEEZE THEM</text></g>
   <g transform="translate(190,660) scale(1.5)">${doctorSVG()}</g><g id="patWrap"><g transform="translate(565,790) scale(1.6)">${patientSVG()}</g></g>`;}
