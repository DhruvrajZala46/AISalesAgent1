// =============== 024: why you should never take a pill without water. All code, in the decoded reference style ===============
const OLW=`stroke="${INK}" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_LIN='#f4aaa0', C_FOLD='#e48f86', C_WALL='#d9666a', C_BG='#6b2a30';
// smooth line through points (Catmull-Rom)
const cr=(pts,mv=true)=>{let d=(mv?'M':'L')+`${pts[0][0].toFixed(1)},${pts[0][1].toFixed(1)}`;for(let i=0;i<pts.length-1;i++){const p0=pts[Math.max(0,i-1)],p1=pts[i],p2=pts[i+1],p3=pts[Math.min(pts.length-1,i+2)];
  d+=` C${(p1[0]+(p2[0]-p0[0])/6).toFixed(1)},${(p1[1]+(p2[1]-p0[1])/6).toFixed(1)} ${(p2[0]-(p3[0]-p1[0])/6).toFixed(1)},${(p2[1]-(p3[1]-p1[1])/6).toFixed(1)} ${p2[0].toFixed(1)},${p2[1].toFixed(1)}`;}return d;};
const edge=(x0,a,f,ph,y0,y1,st)=>{const p=[];for(let y=y0;y<=y1;y+=st)p.push([x0+Math.sin(y*f+ph)*a,y]);return p;};
function tube(xl,xr,xil,xir,y0,y1,st,id){            // a length of food pipe: muscle wall, then the pink lining with long folds
  const L=edge(xl,12,.006,0,y0,y1,st),R=edge(xr,12,.006,1.3,y0,y1,st),IL=edge(xil,10,.007,.4,y0,y1,st),IR=edge(xir,10,.007,2,y0,y1,st);
  const wall=cr(L)+' '+cr(R.slice().reverse(),false)+' Z',lum=cr(IL)+' '+cr(IR.slice().reverse(),false)+' Z';
  const rings=[];for(let y=y0+50;y<y1;y+=st*.9){const a=xl+Math.sin(y*.006)*12,b=xil+Math.sin(y*.007+.4)*10,c=xir+Math.sin(y*.007+2)*10,e=xr+Math.sin(y*.006+1.3)*12;
    rings.push(`M${(a+6).toFixed(0)},${y} Q${((a+b)/2).toFixed(0)},${y+12} ${(b-6).toFixed(0)},${y} M${(c+6).toFixed(0)},${y} Q${((c+e)/2).toFixed(0)},${y+12} ${(e-6).toFixed(0)},${y}`);}
  const w=xir-xil,folds=[.22,.5,.78].map((k,i)=>cr(edge(xil+w*k,14,.011,i*1.7,y0,y1,st))).join(' ');
  return `<path d="${wall}" fill="${C_WALL}" ${OLW}/><path d="${rings.join(' ')}" fill="none" stroke="#bf5357" stroke-width="4" stroke-linecap="round"/>
   <path ${id?`id="${id}"`:''} d="${lum}" fill="${C_LIN}" ${OLW}/><path d="${folds}" fill="none" stroke="${C_FOLD}" stroke-width="7" stroke-linecap="round" opacity=".85"/>
   <path d="${cr(edge(xil+16,10,.007,.4,y0,y1,st))}" fill="none" stroke="#fbd0c9" stroke-width="10" stroke-linecap="round" opacity=".8"/>`;}
function capsule(id){return `<g id="${id}"><ellipse cx="0" cy="54" rx="120" ry="12" fill="#000" opacity=".12"/>
   <path d="M0,-46 H-104 A46,46 0 0 0 -104,46 H0 Z" fill="#fff" ${OLW}/><path d="M0,-46 H104 A46,46 0 0 1 104,46 H0 Z" fill="#e8473f" ${OLW}/>
   <path d="M-112,-26 H-20 M20,-26 H100" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".55"/>
   <g transform="translate(-52,-6)"><g transform="translate(-24,0)">${oEye(id+'_eL',17,'#fff')}</g><g transform="translate(24,0)">${oEye(id+'_eR',17,'#fff')}</g>${brow(id+'_bL')}${brow(id+'_bR')}</g>
   <g transform="translate(-52,26) scale(1.05)">${mouthEl(id+'_m',0,0)}</g></g>`;}
function brainSVG(p){return `<path d="M-130,24 C-142,-46 -92,-104 -20,-106 C44,-124 116,-98 132,-36 C150,14 128,64 80,72 C60,96 8,94 -12,82 C-62,96 -112,80 -130,24 Z" fill="#c46a5f" ${OLW}/>
   <path d="M-104,-20 q14,-26 40,-14 q10,-30 40,-20 M-30,-80 q20,10 14,36 q20,6 22,30 M30,-92 q-4,30 22,36 M70,-70 q-10,26 16,40 q24,0 26,26 M-112,30 q24,-20 50,0 q20,-20 46,0 M-40,10 q10,24 40,18 M20,-10 q30,-6 40,20 M-60,60 q20,-14 40,4 M30,50 q20,-18 46,-6" fill="none" stroke="#7a3a33" stroke-width="5.5" stroke-linecap="round"/>
   <g transform="translate(10,0)"><g transform="translate(-34,0)">${oEye(p+'_eL',28,'#c46a5f')}</g><g transform="translate(34,0)">${oEye(p+'_eR',28,'#c46a5f')}</g>${brow(p+'_bL')}${brow(p+'_bR')}<g transform="translate(0,48) scale(1.35)">${mouthEl(p+'_m',0,0)}</g></g>`;}
// ---- scene 1: inside the food pipe ----
function esoScene(){
  DEFS+=`<radialGradient id="burnG"><stop offset="0" stop-color="#ff2f1c" stop-opacity=".9"/><stop offset=".55" stop-color="#ff4a22" stop-opacity=".45"/><stop offset="1" stop-color="#ff4a22" stop-opacity="0"/></radialGradient>
    <clipPath id="bubC"><circle cx="540" cy="215" r="150"/></clipPath>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="${C_BG}"/>
   <path d="${Array.from({length:9},(_,i)=>`M${-20+i*90},-40 C${10+i*90},300 ${-40+i*90},800 ${-10+i*90},1320`).join(' ')}" fill="none" stroke="#5a2228" stroke-width="10" opacity=".7"/>
   ${tube(150,570,222,498,-80,1360,100,'lumen')}
   <g id="burn"></g><g id="sore"></g>
   <g id="eface" transform="translate(360,770)"><g transform="translate(-64,0)">${oEye('es_eL',52,C_LIN)}</g><g transform="translate(64,0)">${oEye('es_eR',52,C_LIN)}</g>${brow('es_bL')}${brow('es_bR')}
    <g id="esSweat" opacity="0"><path d="M118,-70 C128,-52 132,-40 126,-30 C120,-20 106,-22 104,-32 C102,-44 110,-56 118,-70 Z" fill="#9fd8f5" ${OLW2}/></g>
    <g id="esTears" opacity="0"></g><g id="esPain" opacity="0"><path d="M-170,-40 l18,10 l-14,12 l20,8 M170,-40 l-18,10 l14,12 l-20,8" fill="none" stroke="#e02626" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>
    <g transform="translate(0,98) scale(2.3)">${mouthEl('es_m',0,0)}</g></g>
   <g id="pillW">${capsule('pl')}</g><g id="fz"></g><g id="smk"></g>
   <g transform="translate(24,70)"><rect x="0" y="0" width="346" height="50" fill="#fff" stroke="#1d2a44" stroke-width="3"/><text x="173" y="34" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:27px" fill="#1d2a44">Food Pipe (Esophagus)</text></g>
   <g id="bub" opacity="0"><path d="M440,330 L486,352 L392,452 Z" fill="#fff" ${OLW}/><circle cx="540" cy="215" r="150" fill="#fff" ${OLW}/><path d="M446,338 L482,354" stroke="#fff" stroke-width="12"/>
    <g clip-path="url(#bubC)"><rect x="390" y="300" width="300" height="80" fill="#b98a66"/><path d="M390,300 H690" ${OLW2}/>
     <ellipse cx="548" cy="236" rx="96" ry="34" fill="#fff" ${OLW2}/>
     <g id="brW"><g transform="scale(.6)">${brainSVG('br')}</g></g>
     <path d="M396,266 C470,250 640,250 700,266 L700,380 L396,380 Z" fill="#7fa6dd" ${OLW}/><path d="M440,296 q40,16 80,0 q40,16 80,0" fill="none" stroke="#5f86bd" stroke-width="5" stroke-linecap="round"/>
     <g id="zz" opacity="0" style="font-family:LG,sans-serif" fill="#1d2a44"><text id="z1" x="590" y="150" font-size="34">Z</text><text id="z2" x="618" y="120" font-size="26">z</text></g></g>
    <circle cx="540" cy="215" r="150" fill="none" ${OLW}/></g>`;}
// ---- the time card ----
function cardScene(){return `<rect x="-40" y="-40" width="800" height="1360" fill="#000"/><text x="360" y="660" text-anchor="middle" style="font-family:'DejaVu Sans',Arial,sans-serif;font-weight:700;font-size:58px;letter-spacing:2px" fill="#fff">NEXT MORNING</text>`;}
// ---- scene 2: the clinic ----
function clinicRoom(){DEFS+='<clipPath id="dbC"><ellipse cx="380" cy="232" rx="290" ry="184"/></clipPath>';return `<rect x="-40" y="-40" width="800" height="1360" fill="#c3ccd3"/><path d="M-40,996 H760 V1044 H-40 Z" fill="#9aa6ae" ${OLW2}/>
   <path d="M-40,1044 H760 V1330 H-40 Z" fill="#a2663e"/><path d="M-40,1044 H760 M-40,1120 H760 M-40,1210 H760 M90,1044 V1120 M330,1044 V1120 M570,1044 V1120 M210,1120 V1210 M450,1120 V1210 M690,1120 V1210 M90,1210 V1330 M330,1210 V1330 M570,1210 V1330" stroke="#7d4b2c" stroke-width="3" fill="none"/>
   <path d="M-40,1044 H760" ${OLW2}/>
   <g id="chart"><rect x="250" y="104" width="220" height="330" rx="6" fill="#8a6a4c" ${OLW}/><rect x="264" y="118" width="192" height="302" fill="#fff" ${OLW2}/>
    <circle cx="360" cy="176" r="34" fill="#f3d9c4" ${OLW2}/><path d="M346,206 L346,226 C318,230 296,240 292,262 L292,388 L428,388 L428,262 C424,240 402,230 374,226 L374,206 Z" fill="#f3d9c4" ${OLW2}/>
    <path d="M360,190 C361,230 362,280 364,326" fill="none" stroke="${INK}" stroke-width="13" stroke-linecap="round"/><path d="M360,190 C361,230 362,280 364,326" fill="none" stroke="#e8473f" stroke-width="8" stroke-linecap="round"/>
    <path d="M362,322 C384,314 410,326 408,348 C406,370 376,374 362,360 C352,350 352,330 362,322 Z" fill="#f7a29c" ${OLW2}/>
    <circle id="chartRing" cx="362" cy="268" r="24" fill="none" stroke="#e02626" stroke-width="6" opacity="0"/>
    <text x="360" y="412" text-anchor="middle" style="font-family:LG,sans-serif;font-size:21px" fill="#1d2a44">FOOD PIPE</text></g>
   <g id="docW"><g transform="translate(150,470) scale(.9)">${doctorSVG()}</g></g>
   <g id="patW"><g transform="translate(560,470) scale(.9)">${patientSVG()}</g></g>
   <g id="dbub" opacity="0"><circle cx="160" cy="508" r="8" fill="#fff" ${OLW2}/><circle cx="182" cy="474" r="12" fill="#fff" ${OLW2}/><circle cx="214" cy="436" r="17" fill="#fff" ${OLW2}/>
    <ellipse cx="380" cy="232" rx="292" ry="186" fill="#fff" ${OLW}/>
    <g clip-path="url(#dbC)"><g id="miniT"><rect x="80" y="40" width="600" height="400" fill="#f3e3df"/>${tube(300,460,322,438,0,470,60)}</g>
     <g id="mSore"><ellipse cx="380" cy="236" rx="56" ry="22" transform="rotate(-24,380,236)" fill="#b8282d"/><circle cx="380" cy="236" r="84" fill="url(#burnG)" opacity=".8"/></g>
     <g id="mWater"></g><g id="mPill"><g transform="scale(.5)">${capsule('mp')}</g></g>
     <g id="glass" opacity="0"><path d="M-34,-60 L34,-60 L26,60 L-26,60 Z" fill="#e9f6fd" ${OLW}/><path id="glassW" d="M-30,-10 L30,-10 L26,60 L-26,60 Z" fill="#7cc6f2"/><path d="M-34,-60 L34,-60 L26,60 L-26,60 Z" fill="none" ${OLW}/><path d="M-22,-44 L-18,44" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".8"/></g>
     <g id="clock" opacity="0" transform="translate(575,236)"><circle r="62" fill="#fff" stroke="#1d2a44" stroke-width="6"/><path d="M0,-40 V0 L26,14" fill="none" stroke="#1d2a44" stroke-width="7" stroke-linecap="round"/>
      <rect x="-62" y="72" width="124" height="44" rx="8" fill="#2fae62" stroke="#1d2a44" stroke-width="3"/><text x="0" y="104" text-anchor="middle" style="font-family:LG,sans-serif;font-size:28px" fill="#fff">30 MIN</text></g></g>
    <ellipse cx="380" cy="232" rx="292" ry="186" fill="none" ${OLW}/></g>`;}
