// =============== 009 v3: the reference's staging, studied at 5 fps (exact script), our code characters ===============
// Every food drop: the epiglottis strains (teeth gritted, eyes up), folds shut over the airway, the chunk slides over it into the food pipe
// and travels down INSIDE the pipe. Drop 3: the windpipe snatches a small bite, holds it at its mouth, eats it, the spice hits.
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const T_MAN=E.man, DROPS=[E.land1,E.land2,E.land3];
const KEYW=/^(blocking|over|bite|dangerous|spicy|fire|can't|breathe|choking|black)$/;
let SA=`<g id="sA"><g id="camA">${throatWorld()}</g>${throatLabels()}</g>`;
let SB=`<g id="sB"><g id="camB">${dinnerWorld()}</g></g>`;
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}${GDEF}</defs>`
 +SA+SB+`<rect id="endBlack" x="-10" y="-10" width="740" height="1300" fill="#000" opacity="0"/><g id="capg"><text id="cap" x="330" y="990" text-anchor="middle" style="font-family:'Merri',serif;font-weight:900;font-size:40px;paint-order:stroke;stroke:#111;stroke-width:8px;stroke-linejoin:round" fill="#fff"></text></g>`;
$('esoFood').innerHTML=chunkSVG('tube1')+chunkSVG('tube2')+chunkSVG('tube3');

// ---------- epiglottis flap ----------
const FLAP_UP=[[150,620],[205,500],[262,412],[318,350],[346,326]], FLAP_DN=[[150,620],[214,598],[290,592],[370,598],[424,604]], FLAP_W=[170,112,80,54,30];
function setFlap(k){const pts=FLAP_UP.map((p,i)=>[lerp(p[0],FLAP_DN[i][0],k),lerp(p[1],FLAP_DN[i][1],k)]);
  $('flapO').setAttribute('d',limbD(pts,FLAP_W));
  // the light band runs along the back edge of the flap
  const band=pts.slice(1).map((p,i,a)=>{const q=a[Math.min(i+1,a.length-1)],o=a[Math.max(i-1,0)];let dx=q[0]-o[0],dy=q[1]-o[1];const L=Math.hypot(dx,dy)||1;const off=FLAP_W[i+1]*.2;return [p[0]-dy/L*off,p[1]+dx/L*off];});
  const st=smooth(band); $('flapS1').setAttribute('d',st); $('flapS2').setAttribute('d',st);}
function shutAt(T){let s=0;DROPS.forEach((L,i)=>{const hold=i===2?.32:.25;s=Math.max(s,eo(P(T,L-.2,L))*(1-eio(P(T,L+hold,L+hold+.3))));});return s;}
// ---------- a food drop: falls -> slides over the shut flap -> down inside the food pipe ----------
const TUBE=[[412,700],[420,800],[434,900],[452,1000],[474,1100],[492,1200],[508,1360]];
function along(pts,s){s=clamp(s)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;return [lerp(pts[i][0],pts[i+1][0],f),lerp(pts[i][1],pts[i+1][1],f)];}
function drop(i,T){const L=DROPS[i], free=$('food'+(i+1)), tube=$('tube'+(i+1));
  if(T<L-1.0||T>L+1.0){show('food'+(i+1),0);show('tube'+(i+1),0);return null;}
  if(T<L+.2){show('food'+(i+1),1);show('tube'+(i+1),0);let x,y,r;
    if(T<L){const q=P(T,L-1.0,L);x=lerp(462,436,eio(q));y=lerp(-140,548,q*q);r=Math.sin(q*5)*8;}
    else{const q=P(T,L,L+.2);x=lerp(436,414,q);y=lerp(548,668,q);r=lerp(0,-12,q);}
    free.setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(1)})`);return [x,y];}
  show('food'+(i+1),0);show('tube'+(i+1),1);const p=along(TUBE,P(T,L+.2,L+1.0));
  tube.setAttribute('transform',`translate(${p[0].toFixed(1)},${p[1].toFixed(1)}) rotate(-14) scale(.5,.62)`);return null;}
function renderThroat(T){
  const tT=speak('trachea',T), eT=speak('epiglottis',T);
  const fps=[0,1,2].map(i=>drop(i,T)); const falling=fps.find(Boolean);
  const shut=shutAt(T); setFlap(clamp(shut+.025*Math.sin(T*2.6),0,1.06)); $('epiFace').setAttribute('transform',`translate(0,${(Math.sin(T*2.6)*2.5).toFixed(1)})`);
  $('hyoid').setAttribute('transform',`translate(${(shut*10).toFixed(1)},${(-shut*10).toFixed(1)}) translate(86,490) scale(${(1+shut*.08).toFixed(3)},${(1-shut*.14).toFixed(3)}) translate(-86,-490)`);
  // epiglottis mood
  const e0=ST['02_epiglottis'], e4=ST['04_epiglottis'], e5=ST['05_epiglottis'], e7=ST['07_epiglottis'];
  const strain=DROPS.some((L,i)=>T>=L-.6&&T<L+(i===2?.45:.35));
  const mood=strain?'strain':(T>=e7?'worried':(T>=e5?'angry':(T>=e4?'firm':(T>=e0?'annoyed':'calm'))));
  const el=strain?[10,-40]:(T>=ST['01_trachea']?[16,38]:[18,30]), ebl=blinkK(T,.4);
  const lid={calm:.08,annoyed:.36,firm:.32,angry:.45,worried:.1,strain:0}[mood];
  setCEye('eEyeL',40,{dx:el[0],dy:el[1],lid,blink:strain?0:ebl}); setCEye('eEyeR',40,{dx:el[0],dy:el[1],lid,blink:strain?0:ebl});
  const bb={calm:[0,0,6],annoyed:[14,-14,0],firm:[16,-16,0],angry:[22,-22,-2],worried:[-16,16,8],strain:[-14,14,12]}[mood];
  $('eBrowL').setAttribute('d',`M82,${538-bb[2]} Q105,${528-bb[2]} 128,${538-bb[2]}`); $('eBrowL').setAttribute('transform',`rotate(${bb[0]},105,534)`);
  $('eBrowR').setAttribute('d',`M169,${532-bb[2]} Q192,${522-bb[2]} 215,${532-bb[2]}`); $('eBrowR').setAttribute('transform',`rotate(${bb[1]},192,528)`);
  show('grit',strain?1:0); show('epi_m',strain?0:1); show('epi_m_l',strain?0:1);
  if(!strain) setCMouth('epi_m',eT,16,{calm:.1,annoyed:-.4,firm:-.5,angry:-.8,worried:-.7}[mood]);
  // the windpipe
  const t3=ST['03_trachea'], L3=DROPS[2], red=T>=E.fire-.3;
  const biting=T>=E.grab&&T<E.eat+.15, chewing=T>=E.eat&&T<E.spicy;
  let tl=[-14,-38]; if(falling&&!red) tl=[16,-40]; if(T>=L3-.3&&T<E.grab+.4) tl=[24,-40]; if(biting) tl=[-10,-30];
  const tb=blinkK(T,1.9), plead=T>=t3&&T<e4+.6;
  setCEye('tEyeL',42,{dx:tl[0],dy:tl[1],lid:red?.15:0,blink:tb}); setCEye('tEyeR',42,{dx:tl[0],dy:tl[1],lid:red?.15:0,blink:tb});
  show('redEyes',red?1:0);
  const tbr=red?[-16,16,12]:(plead?[-16,16,10]:[-4,4,6]);
  $('tBrowL').setAttribute('d',`M222,${890-tbr[2]} Q246,${880-tbr[2]} 270,${890-tbr[2]}`); $('tBrowL').setAttribute('transform',`rotate(${tbr[0]},246,886)`);
  $('tBrowR').setAttribute('d',`M308,${890-tbr[2]} Q332,${880-tbr[2]} 356,${890-tbr[2]}`); $('tBrowR').setAttribute('transform',`rotate(${tbr[1]},332,886)`);
  const chew=chewing?.25+.25*Math.abs(Math.sin(T*10)):0;
  setCMouth('tra_m',Math.max(tT,chew),20,red?-.8:(plead?.5:-.2),red&&tT>.08?'#c8222b':'#4d2e2b');
  $('traFace').setAttribute('transform',`translate(0,${(Math.sin(T*2.2)*3).toFixed(1)}) translate(290,960) scale(${(1+.015*Math.sin(T*2.2+1)).toFixed(4)}) translate(-290,-960)`);
  let tears='';if(red){[246,332].forEach((x,i)=>{const s=1+.12*Math.sin(T*3+i);tears+=`<path transform="translate(${x},${992}) scale(${s.toFixed(2)})" d="M-26,-6 C-30,14 -16,26 -8,12 C0,28 16,24 14,6 C24,18 34,8 28,-8" fill="#7fc8ef" ${OLW}/>`;});} $('tTears').innerHTML=tears;
  // arms: out at drop 3; the right hand snatches a small bite from the chunk on the flap, holds it at the mouth, then both hang
  const armsOn=T>=L3-.15; show('tArmL',armsOn?1:0); show('tArmR',armsOn?1:0);
  let bite=null;
  if(armsOn){
    setHose('tArmL',[[214,968],[176,1036],[188,1104]],10,.9);
    if(T<E.grab){const k=eob(P(T,L3-.15,E.grab)); setHose('tArmR',[[378,968],[lerp(410,446,k),lerp(1030,800,k)],[lerp(404,438,k),lerp(1100,604,k)]],lerp(-10,-170,k),.9);}
    else if(T<E.eat+.15){const k=eio(P(T,E.grab,E.grab+.4)), hx=lerp(438,326,k), hy=lerp(604,1018,k);
      setHose('tArmR',[[378,968],[lerp(446,420,k),lerp(800,1060,k)],[hx,hy]],lerp(-170,-130,k),.9); bite=[hx-16,hy-14];}
    else setHose('tArmR',[[378,968],[412,1036],[402,1104]],-10,.9);}
  show('bite',bite?1:0); if(bite){const s=T>=E.eat?.32*(1-P(T,E.eat,E.eat+.15)):.32; $('bite').setAttribute('transform',`translate(${bite[0].toFixed(1)},${bite[1].toFixed(1)}) rotate(-20) scale(${Math.max(.001,s).toFixed(3)})`);}
  [['lbEpi',.05],['lbTra',.1],['lbEso',.15]].forEach(([id,t0])=>{const k=eob(P(T,t0,t0+.25)),e=$(id); if(!e.getAttribute('data-b'))e.setAttribute('data-b',e.getAttribute('transform')); e.setAttribute('transform',e.getAttribute('data-b')+` scale(${k.toFixed(3)})`);});
}
// ---------- the man at the table: eyes open -> coughing fit -> red eyes, red mouth, tears ----------
function renderDinner(T){
  const mT=speak('man',T), m0=ST['08_man'], cough=T>=m0+.15&&T<m0+1.15, after=T>=m0+1.15;
  const jerk=cough?Math.abs(Math.sin((T-m0)*15)):0;
  const hy=Math.sin(T*1.5)*1.5+jerk*7, hr=cough?-5+jerk*4:(after?-3+Math.sin(T*3)*1:0);
  tr('patHead',0,hy,1,1,hr);
  $('pBrows').setAttribute('d',(cough||after)?'M-36,62 Q-24,54 -10,62 M8,62 Q22,54 34,62':'M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70');
  const open=cough?.45+.5*jerk:mT, hurt=cough||after;
  setMouthV('pat_m',hurt?0:open,11,hurt?-.6:0,T,6); ['pat_m','pat_m_w','pat_m_t'].forEach(id=>{const e=$(id);if(e)e.setAttribute('display',hurt?'none':'inline');});
  const lidV=cough?.95:(after?.3:0); setHEye('pEyeL',0,Math.min(.95,lidV+blinkK(T,.8))); setHEye('pEyeR',0,Math.min(.95,lidV+blinkK(T,.8)));
  ['pEyeL','pEyeR'].forEach(id=>{const w=document.querySelector('#'+id+' path');if(w){w.setAttribute('fill',after?'#ffc2c2':'#fff');}});
  show('patBlush',(cough||after)?1:0); show('pSweat',after?1:0); $('pSweat').setAttribute('transform',`translate(46,${(70+((T*14)%24)).toFixed(1)})`);
  const d=limbD([[-84,234],[-132,300],[-112,356]],[44,38,32]); $('patArmLD').setAttribute('d',d); $('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(-112,360,-10,1.2,PSK);
  let s='';if(hurt){const ry=3+open*9;s=`<g transform="translate(390,206) scale(1.9)"><g transform="translate(0,${hy.toFixed(2)}) rotate(${hr.toFixed(2)})">
    <ellipse cx="-4" cy="${(138+ry*.5).toFixed(1)}" rx="${(6+open*3).toFixed(1)}" ry="${ry.toFixed(1)}" fill="#d8262c" stroke="${INK}" stroke-width="1.6"/></g></g>`;}
  if(after){s+=`<g transform="translate(390,206) scale(1.9)"><g transform="translate(0,${hy.toFixed(2)}) rotate(${hr.toFixed(2)})">
    <path d="M-34,88 Q-22,76 -10,88 M6,88 Q18,76 30,88" fill="none" stroke="#e3242c" stroke-width="2.2"/>
    <path d="M-30,96 c-3,6 -1,11 3,11 c4,0 6,-5 3,-11 M24,96 c-3,6 -1,11 3,11 c4,0 6,-5 3,-11" fill="#7fc8ef" stroke="${INK}" stroke-width="1.2"/></g></g>`;}
  $('manFx').innerHTML=s;
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  const c=$('cap'), t=w==='I'?'I':w.toLowerCase(); c.textContent=t; const key=KEYW.test(t);
  c.style.fontSize=key?'54px':'40px';
  const man=T>=T_MAN, cx=man?360:330, cy=man?1070:990;
  c.setAttribute('x',cx); c.setAttribute('y',cy);
  const k=eob(P(T,ws,ws+.14)); c.setAttribute('transform',`translate(${cx},${cy}) scale(${lerp(.6,1,k).toFixed(3)}) translate(${-cx},${-cy})`);}
window.render=function(T){
  const sc=T<T_MAN?1:2; $('sA').setAttribute('display',sc===1?'inline':'none'); $('sB').setAttribute('display',sc===2?'inline':'none');
  if(sc===1){renderThroat(T); const z=1+.025*P(T,0,T_MAN)+.004*Math.sin(T*1.3); $('camA').setAttribute('transform',`translate(360,640) scale(${z.toFixed(4)}) translate(-360,-640)`);}
  else {renderDinner(T); const z=1+.03*P(T,T_MAN,END)+.004*Math.sin(T*1.3); $('camB').setAttribute('transform',`translate(360,560) scale(${z.toFixed(4)}) translate(-360,-560)`);}
  show('endBlack',T>=END-.15?1:0);
  caption(T);
};
window.render(0);
