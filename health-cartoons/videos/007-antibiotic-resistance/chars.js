// 007: code-drawn characters in the style of our AI art (thick dark-brown outline, soft gradients, highlights, googly eyes, white gloves).
// No image model is used (user rule, 22 Nov 2026).
const OL='#4a2a24', OW=5;
const STK=`stroke="${OL}" stroke-width="${OW}" stroke-linejoin="round" stroke-linecap="round"`;
const STK2=`stroke="${OL}" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"`;
let GDEF='';
function grad(id,c1,c2,radial=true,fx='35%',fy='30%'){GDEF+=radial?`<radialGradient id="${id}" cx="40%" cy="35%" r="75%" fx="${fx}" fy="${fy}"><stop offset="0" stop-color="${c1}"/><stop offset="1" stop-color="${c2}"/></radialGradient>`:
  `<linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${c1}"/><stop offset="1" stop-color="${c2}"/></linearGradient>`;return `url(#${id})`;}
// googly eye with lid + brow, drawn bigger than the 001 ones to match the AI art
function gEye(id,r){const c='ce'+(UID++);DEFS+=`<clipPath id="${c}"><ellipse rx="${r*.9}" ry="${r}"/></clipPath>`;
  return `<g id="${id}"><ellipse rx="${r*.9}" ry="${r}" fill="#fff"/><g clip-path="url(#${c})"><circle id="${id}_p" r="${r*.5}" fill="#231a18"/><circle id="${id}_h" r="${r*.17}" fill="#fff"/>
  <g id="${id}_lid"><rect x="${-r*2}" y="${-r*3}" width="${r*4}" height="${r*2}" fill="#000" opacity="0"/><path d="M${-r*2},${-r} L${r*2},${-r}" ${STK2}/></g></g><ellipse rx="${r*.9}" ry="${r}" fill="none" ${STK2}/></g>`;}
function setGEye(id,r,{dx=0,dy=0,lid=0,lidCol='#000',blink=0}={}){const d=Math.hypot(dx,dy)||1,m=r*.4,k=Math.min(1,d/40);const px=dx/d*m*k,py=dy/d*m*k;
  $(id+'_p').setAttribute('cx',px);$(id+'_p').setAttribute('cy',py);$(id+'_h').setAttribute('cx',px-r*.15);$(id+'_h').setAttribute('cy',py-r*.18);
  const L=Math.max(lid,blink);const g=$(id+'_lid');g.setAttribute('transform',`translate(0,${L*2*r})`);g.firstElementChild.setAttribute('fill',lidCol);g.firstElementChild.setAttribute('opacity',L>0.01?1:0);g.lastElementChild.setAttribute('opacity',L>0.01?1:0);}
function gBrow(id){return `<path id="${id}" fill="none" stroke="${OL}" stroke-width="6" stroke-linecap="round"/>`;}
// mouth: dark maroon with pink tongue, like the AI mouths
function gMouth(id){return `<g id="${id}"><path id="${id}_o" fill="#6a1f22" ${STK2}/><ellipse id="${id}_t" rx="1" ry="1" fill="#e88a8f"/></g>`;}
function setGMouth(id,o,w,mood=0){const e=$(id+'_o'),t=$(id+'_t');o=clamp(o);
  if(o<.1){e.setAttribute('d',`M${-w*.6},0 Q0,${mood*w*.5} ${w*.6},0`);e.setAttribute('fill','none');t.setAttribute('opacity',0);return;}
  const h=4+o*w*1.1;e.setAttribute('d',`M${-w*.62},0 Q0,${-3+mood*3} ${w*.62},0 Q${w*.55},${h} 0,${h+2} Q${-w*.55},${h} ${-w*.62},0Z`);e.setAttribute('fill','#6a1f22');
  t.setAttribute('opacity',o>.3?1:0);t.setAttribute('cx',0);t.setAttribute('cy',h*.72);t.setAttribute('rx',w*.32);t.setAttribute('ry',h*.22);}
// white rubber-hose arm with a cartoon glove at the end
function glove(x,y,rot,s=1){return `<g transform="translate(${x},${y}) rotate(${rot}) scale(${s})"><path d="M-14,-10 C-22,-6 -24,8 -16,16 C-10,22 8,22 16,14 C22,8 22,-4 16,-10 C14,-20 4,-22 0,-14 C-4,-22 -12,-18 -14,-10Z" fill="#fff" ${STK2}/><path d="M-8,4 L6,4 M-6,10 L8,10" fill="none" stroke="#c9c2bf" stroke-width="2.5" stroke-linecap="round"/></g>`;}
function arm(id){return `<g id="${id}"><path id="${id}_a" fill="none" stroke="${OL}" stroke-width="15" stroke-linecap="round"/><path id="${id}_b" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round"/><g id="${id}_g"></g></g>`;}
function setArm(id,x0,y0,x1,y1,bend,rot,s=1){const mx=(x0+x1)/2+bend,my=(y0+y1)/2-Math.abs(bend)*.3;const d=`M${x0},${y0} Q${mx},${my} ${x1},${y1}`;
  $(id+'_a').setAttribute('d',d);$(id+'_b').setAttribute('d',d);$(id+'_g').innerHTML=glove(x1,y1,rot,s);}
function leg(x,y,len,ang){const ex=x+Math.sin(ang*Math.PI/180)*len,ey=y+Math.cos(ang*Math.PI/180)*len;
  return `<path d="M${x},${y} L${ex},${ey}" stroke="${OL}" stroke-width="15" stroke-linecap="round"/><path d="M${x},${y} L${ex},${ey}" stroke="#fff" stroke-width="9" stroke-linecap="round"/>
   <path d="M${ex-16},${ey+10} C${ex-18},${ey-6} ${ex+8},${ey-8} ${ex+22},${ey+2} C${ex+28},${ey+8} ${ex+24},${ey+16} ${ex+12},${ey+16} L${ex-12},${ey+16} C${ex-18},${ey+16} ${ex-18},${ey+12} ${ex-16},${ey+10}Z" fill="#fff" ${STK2}/>`;}

// ---------- the skin-cell GUARD (police cap, STOP sign) ----------
function guardSVG(id){return `<g id="${id}"><g id="${id}_body">
  ${leg(-34,100,46,4)}${leg(34,100,46,-4)}
  <path d="M-95,-30 C-100,-95 -60,-128 0,-128 C60,-128 100,-95 95,-30 C100,40 80,108 0,112 C-80,108 -100,40 -95,-30Z" fill="${grad(id+'g1','#ffe0c4','#e8a87f')}" ${STK}/>
  <path d="M-70,-90 C-50,-112 -10,-118 20,-112" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".55"/>
  <circle cx="-62" cy="40" r="5" fill="#d98b66" opacity=".7"/><circle cx="58" cy="58" r="6" fill="#d98b66" opacity=".7"/><circle cx="40" cy="80" r="4" fill="#d98b66" opacity=".7"/>
  <path d="M-58,-40 C-40,-8 40,-8 58,-40" fill="none" stroke="#e8a87f" stroke-width="3" opacity=".0"/>
  <g transform="translate(0,-118)"><path d="M-92,22 C-90,-6 -60,-30 0,-32 C60,-30 90,-6 92,22 Z" fill="${grad(id+'g2','#3d4f86','#1f2a52')}" ${STK}/>
   <path d="M-104,22 C-60,40 60,40 104,22 C96,36 60,46 0,46 C-60,46 -96,36 -104,22Z" fill="#1a1f38" ${STK2}/>
   <path d="M-12,-16 L12,-16 L14,4 L0,12 L-14,4Z" fill="#f2c74a" ${STK2}/></g>
  <g transform="translate(-30,-40)">${gEye(id+'_eL',24)}</g><g transform="translate(30,-40)">${gEye(id+'_eR',24)}</g>${gBrow(id+'_bL')}${gBrow(id+'_bR')}
  <path d="M-34,6 C-22,-6 -6,0 0,4 C6,0 22,-6 34,6 C24,12 10,10 0,8 C-10,10 -24,12 -34,6Z" fill="#6b3b22" ${STK2}/>
  <g transform="translate(0,26)">${gMouth(id+'_m')}</g>
  <path d="M-30,78 L30,78" stroke="#1f2a52" stroke-width="0"/>
  </g>${arm(id+'_aL')}${arm(id+'_aR')}
  <g id="${id}_sign"><path d="M0,0 L0,150" stroke="${OL}" stroke-width="12" stroke-linecap="round"/><path d="M0,0 L0,150" stroke="#9b9b9b" stroke-width="6" stroke-linecap="round"/>
   <path d="M-23,-56 L23,-56 L56,-23 L56,23 L23,56 L-23,56 L-56,23 L-56,-23Z" transform="translate(0,-40)" fill="#e0392f" ${STK}/>
   <path d="M-19,-46 L19,-46 L46,-19 L46,19 L19,46 L-19,46 L-46,19 L-46,-19Z" transform="translate(0,-40)" fill="none" stroke="#fff" stroke-width="4"/>
   <text x="0" y="-31" text-anchor="middle" style="font-family:LG,sans-serif;font-size:27px" fill="#fff">STOP</text></g>
  <g id="${id}_phone" opacity="0"><rect x="-14" y="-28" width="28" height="56" rx="7" fill="#2b2b33" ${STK2}/><rect x="-9" y="-21" width="18" height="38" rx="3" fill="#7fd0ff"/></g></g>`;}
function setGuard(id,x,y,s,{talk=0,T=0,pose='stop',rot=0,look=0,mood=0,brows=0}={}){
  $(id).setAttribute('transform',`translate(${x},${y}) rotate(${rot}) scale(${s})`);
  const bl=blinkK(T,.4); [['_eL',-1],['_eR',1]].forEach(([e,sg])=>setGEye(id+e,24,{dx:look*40,dy:pose==='fallen'?10:2,blink:bl,lidCol:'#f3c6a2',lid:pose==='phone'?.2:0}));
  const by=-74-brows*6;$(id+'_bL').setAttribute('d',`M-50,${by+brows*8} Q-32,${by-10} -14,${by-brows*6}`);$(id+'_bR').setAttribute('d',`M14,${by-brows*6} Q32,${by-10} 50,${by+brows*8}`);
  setGMouth(id+'_m',talk,26,mood);
  const sw=Math.sin(T*3)*4;
  if(pose==='stop'){setArm(id+'_aL',-90,0,-128,50+sw,-10,20);setArm(id+'_aR',90,-10,132,-10+sw,10,-30);$(id+'_sign').setAttribute('transform',`translate(142,${-38+sw}) rotate(8)`);show(id+'_sign',1);show(id+'_phone',0);}
  else if(pose==='phone'){setArm(id+'_aL',-90,0,-120,60,-10,20);setArm(id+'_aR',88,-10,88,-58,30,-60);$(id+'_phone').setAttribute('transform',`translate(86,-70) rotate(-12)`);show(id+'_phone',1);
     $(id+'_sign').setAttribute('transform',`translate(-150,40) rotate(-70)`);show(id+'_sign',1);}
  else {setArm(id+'_aL',-90,0,-140,-40,-20,40);setArm(id+'_aR',90,0,140,-40,20,-40);show(id+'_sign',0);show(id+'_phone',0);}
}
// ---------- BACTERIA (green rod, little hairs) ----------
function bactSVG(id,col1='#a8e86a',col2='#5fae3a'){let hairs='';for(let i=0;i<14;i++){const a=i/14*Math.PI*2,x=Math.cos(a)*112,y=Math.sin(a)*70;hairs+=`<path d="M${x.toFixed(0)},${y.toFixed(0)} q${(Math.cos(a)*18).toFixed(0)},${(Math.sin(a)*18-10).toFixed(0)} ${(Math.cos(a)*30).toFixed(0)},${(Math.sin(a)*30).toFixed(0)}" fill="none" stroke="${OL}" stroke-width="4" stroke-linecap="round"/>`;}
  return `<g id="${id}"><g id="${id}_hair">${hairs}</g>
  <path d="M-110,0 C-110,-60 -70,-74 0,-74 C70,-74 110,-60 110,0 C110,60 70,74 0,74 C-70,74 -110,60 -110,0Z" fill="${grad(id+'g',col1,col2)}" ${STK}/>
  <path d="M-80,-44 C-50,-62 10,-64 50,-56" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".5"/>
  <circle cx="-70" cy="30" r="9" fill="${col2}" opacity=".6"/><circle cx="74" cy="34" r="7" fill="${col2}" opacity=".6"/><circle cx="50" cy="-20" r="6" fill="${col2}" opacity=".5"/>
  <g transform="translate(-26,-16)">${gEye(id+'_eL',22)}</g><g transform="translate(26,-16)">${gEye(id+'_eR',22)}</g>${gBrow(id+'_bL')}${gBrow(id+'_bR')}
  <g transform="translate(0,26)">${gMouth(id+'_m')}</g>${arm(id+'_aL')}${arm(id+'_aR')}<g id="${id}_shield" opacity="0"></g></g>`;}
function setBact(id,x,y,s,{talk=0,T=0,smug=.5,rot=0,look=0,arms='hips',mood=.4,seed=0}={}){
  $(id).setAttribute('transform',`translate(${x},${y}) rotate(${rot}) scale(${s})`);
  $(id+'_hair').setAttribute('transform',`rotate(${Math.sin(T*6+seed)*4})`);
  const bl=blinkK(T,seed);['_eL','_eR'].forEach(e=>setGEye(id+e,22,{dx:look*40,dy:2,lid:smug*.45,lidCol:'#7cc94e',blink:bl}));
  $(id+'_bL').setAttribute('d',`M-46,${-44+smug*6} Q-28,${-50} -10,${-40-smug*4}`);$(id+'_bR').setAttribute('d',`M10,${-40-smug*4} Q28,-50 46,${-44+smug*6}`);
  setGMouth(id+'_m',talk,24,mood);
  const w=Math.sin(T*4+seed)*5;
  if(arms==='hips'){setArm(id+'_aL',-104,14,-126,52+w,-18,30,.9);setArm(id+'_aR',104,14,126,52-w,18,-30,.9);}
  else if(arms==='push'){setArm(id+'_aL',-100,0,-170,-6+w,-10,90,.9);setArm(id+'_aR',100,0,40,-90,40,0,.0001);}
  else {setArm(id+'_aL',-104,0,-150,-60+w,-20,40,.9);setArm(id+'_aR',104,0,150,-60-w,20,-40,.9);}
}
// ---------- WHITE BLOOD CELL (bumpy round cell, boxing gloves) ----------
function wbcSVG(id){let d='';const n=16;for(let i=0;i<=n;i++){const a=i/n*Math.PI*2,r=118+(i%2?8:-4);d+=(i?' ':'M')+(Math.cos(a)*r).toFixed(1)+','+(Math.sin(a)*r).toFixed(1);}
  return `<g id="${id}"><path d="${smooth(Array.from({length:n},(_,i)=>{const a=i/n*Math.PI*2,r=118+(i%2?9:-5);return [Math.cos(a)*r,Math.sin(a)*r];}).concat([[Math.cos(0)*113,0]]))}Z" fill="${grad(id+'g','#ffffff','#d9d4ef')}" ${STK}/>
  <path d="M-40,40 C-60,20 -30,0 -10,20 C0,0 40,0 30,30 C50,40 30,70 10,60 C-10,80 -40,70 -40,40Z" fill="#c8b8ec" opacity=".55"/>
  <path d="M-70,-70 C-40,-96 10,-100 40,-92" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round" opacity=".9"/>
  <g transform="translate(-30,-26)">${gEye(id+'_eL',24)}</g><g transform="translate(30,-26)">${gEye(id+'_eR',24)}</g>${gBrow(id+'_bL')}${gBrow(id+'_bR')}
  <g transform="translate(0,22)">${gMouth(id+'_m')}</g>${arm(id+'_aL')}${arm(id+'_aR')}</g>`;}
function setWbc(id,x,y,s,{talk=0,T=0,rot=0,look=0,mood=0,angry=1,punch=0}={}){
  $(id).setAttribute('transform',`translate(${x},${y}) rotate(${rot}) scale(${s})`);
  const bl=blinkK(T,1.3);['_eL','_eR'].forEach(e=>setGEye(id+e,24,{dx:look*40,dy:2,blink:bl,lidCol:'#efecf8'}));
  $(id+'_bL').setAttribute('d',`M-56,${-56-angry*2} Q-36,${-66+angry*6} -12,${-50+angry*10}`);$(id+'_bR').setAttribute('d',`M12,${-50+angry*10} Q36,${-66+angry*6} 56,${-56-angry*2}`);
  setGMouth(id+'_m',talk,26,mood);
  const j=Math.sin(T*8)*6;setArm(id+'_aL',-110,10,-150+punch*-40,0+j,-10,80,1.15);setArm(id+'_aR',110,10,150,-10-j,10,-80,1.15);
}
// ---------- ANTIBIOTIC (capsule soldier with a helmet and a spear) ----------
function abSVG(id){return `<g id="${id}">${leg(-26,96,40,4)}${leg(26,96,40,-4)}
  <path d="M-72,-10 L-72,-60 C-72,-110 72,-110 72,-60 L72,-10Z" fill="${grad(id+'g1','#ff8a7a','#d8362f')}" ${STK}/>
  <path d="M-72,-10 L-72,50 C-72,110 72,110 72,50 L72,-10Z" fill="${grad(id+'g2','#ffffff','#dcdfe6')}" ${STK}/>
  <path d="M-50,-80 C-30,-96 10,-98 30,-92" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".6"/>
  <g transform="translate(0,-92)"><path d="M-84,14 C-84,-34 84,-34 84,14Z" fill="${grad(id+'g3','#6f8d47','#3f5a24')}" ${STK}/><path d="M-96,14 L96,14" stroke="${OL}" stroke-width="10" stroke-linecap="round"/><path d="M-96,14 L96,14" stroke="#4f6c2e" stroke-width="5" stroke-linecap="round"/></g>
  <g transform="translate(-26,-34)">${gEye(id+'_eL',22)}</g><g transform="translate(26,-34)">${gEye(id+'_eR',22)}</g>${gBrow(id+'_bL')}${gBrow(id+'_bR')}
  <g transform="translate(0,16)">${gMouth(id+'_m')}</g>${arm(id+'_aL')}${arm(id+'_aR')}
  <g id="${id}_spear"><path d="M0,-140 L0,120" stroke="${OL}" stroke-width="11" stroke-linecap="round"/><path d="M0,-140 L0,120" stroke="#b07a46" stroke-width="5" stroke-linecap="round"/><path d="M0,-190 L16,-140 L-16,-140Z" fill="#cfd6de" ${STK2}/></g></g>`;}
function setAb(id,x,y,s,{talk=0,T=0,rot=0,look=0,mood=0,poke=0,shock=0}={}){
  $(id).setAttribute('transform',`translate(${x},${y}) rotate(${rot}) scale(${s})`);
  const bl=blinkK(T,2.2);['_eL','_eR'].forEach(e=>setGEye(id+e,22,{dx:look*40,dy:2,blink:bl}));
  $(id+'_bL').setAttribute('d',`M-48,${-62+shock*-8} Q-30,${-74+(1-shock)*6} -10,${-58+(1-shock)*8}`);$(id+'_bR').setAttribute('d',`M10,${-58+(1-shock)*8} Q30,${-74+(1-shock)*6} 48,${-62+shock*-8}`);
  setGMouth(id+'_m',talk,24,mood);
  setArm(id+'_aL',-70,10,-110,40,-10,20,.9);setArm(id+'_aR',70,10,112-poke*60,44,10,-60,.9);
  $(id+'_spear').setAttribute('transform',`translate(${(118-poke*60).toFixed(1)},44) rotate(-92)`);
}
// ---------- the tissue background (skin on top, the cut, dermis) ----------
function tissueSVG(){return `<g id="tissue"><rect width="720" height="1280" fill="${grad('tg0','#f6b3a8','#d97f78',false)}"/>
  ${Array.from({length:22},(_,i)=>{const x=20+i*33+rnd(i)*14;return `<path d="M${x},230 C${x+20},${380+rnd(i+3)*80} ${x-24},${560+rnd(i+5)*60} ${x+6},${760+rnd(i+7)*60}" fill="none" stroke="#c9625d" stroke-width="${2+rnd(i+9)*2}" opacity=".55"/>`;}).join('')}
  <path d="M0,180 C120,170 240,196 360,186 C480,176 600,196 720,184 L720,0 L0,0Z" fill="${grad('tg1','#ffe2c8','#eeb994',false)}" ${STK}/>
  <path d="M0,200 C120,190 240,216 360,206 C480,196 600,216 720,204" fill="none" stroke="#d98f73" stroke-width="10" opacity=".6"/>
  <path d="M0,880 C140,860 260,900 380,884 C520,866 620,896 720,882 L720,1280 L0,1280Z" fill="${grad('tg2','#e78b82','#b9534f',false)}" ${STK}/>
  ${Array.from({length:9},(_,i)=>`<ellipse cx="${40+i*80}" cy="${950+rnd(i)*40}" rx="${26+rnd(i+2)*14}" ry="10" fill="#f2a59a" opacity=".55"/>`).join('')}
  ${Array.from({length:11},(_,i)=>`<ellipse cx="${30+i*66}" cy="${120+rnd(i+40)*30}" rx="${26+rnd(i+41)*8}" ry="${16+rnd(i+42)*6}" fill="#f9d2b4" stroke="#d9a27f" stroke-width="3"/>`).join('')}
  <path d="M-20,640 C160,600 300,690 470,650 C590,622 680,660 740,640" fill="none" stroke="${OL}" stroke-width="44" stroke-linecap="round"/>
  <path d="M-20,640 C160,600 300,690 470,650 C590,622 680,660 740,640" fill="none" stroke="#d5434a" stroke-width="34" stroke-linecap="round"/>
  <path d="M-20,632 C160,592 300,682 470,642 C590,614 680,652 740,632" fill="none" stroke="#f07a7d" stroke-width="7" stroke-linecap="round" opacity=".8"/>
  ${Array.from({length:5},(_,i)=>`<ellipse cx="${80+i*140}" cy="${640+Math.sin(i)*14}" rx="13" ry="8" fill="#ff8f8f" stroke="#a8282e" stroke-width="2"/>`).join('')}
  <g id="cut"><path d="M300,170 C318,260 330,360 352,470 C364,360 382,260 410,166 Z" fill="${grad('tg3','#7a0f14','#c4232c')}" ${STK}/>
   <path d="M330,200 C342,280 348,360 356,430" fill="none" stroke="#ff6b6b" stroke-width="6" stroke-linecap="round" opacity=".7"/></g></g>`;}
