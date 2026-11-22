// =============== 009: the epiglottis and the trachea (exact script of the user's reference), ALL code, 001 / 003-v1 style ===============
const E=D.ev, ST=D.start, END=D.end;
const KEY=/^(BLOCKING|BREATHING|FOOD|GAME|OVER|BITE|DANGEROUS|SPICY|FIRE|BREATHE|CHOKING|BLACK)$/;
//__VISEME__
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
function popK(T,t0){const k=P(T,t0,t0+.18);return k<1?Math.sin(k*Math.PI):0;}
function along(pts,s){s=clamp(s)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;return [lerp(pts[i][0],pts[i+1][0],f),lerp(pts[i][1],pts[i+1][1],f)];}
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const T_MAN=E.man;
let SA=`<g id="sA"><g id="camA">${throatWorld()}</g>${throatLabels()}</g>`;
let SB=`<g id="sB"><g id="camB">${dinnerWorld()}</g></g>`;
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}${GDEF}</defs>`
 +SA+SB+`<rect id="indark" width="720" height="1280" fill="#1e1012" opacity="0"/><g id="capg"><text id="cap" class="cap" x="360" y="1110" text-anchor="middle"></text></g>`;

// ---------- the throat ----------
function dropFood(id,t0,T){const q=(T-t0)/1.1; if(q<0||q>1.25){show(id,0);return null;} show(id,1);
  const p=q<1?[lerp(450,424,eio(q)),lerp(-90,700,q*q)]:[424,700+(q-1)*240];
  $(id).setAttribute('transform',`translate(${p[0].toFixed(1)},${p[1].toFixed(1)}) rotate(${(q*200).toFixed(1)})`); $(id).setAttribute('opacity',q<1?1:Math.max(0,1-(q-1)*4)); return p;}
function renderThroat(T){
  const tT=speak('trachea',T), eT=speak('epiglottis',T);
  const f1=dropFood('food1',E.food1,T), f2=dropFood('food2',E.food2,T), fp=f1||f2;
  // the epiglottis folds back over the windpipe while the spicy crumb goes by, then springs up again
  const shut=eob(P(T,E.close,E.close+.25))*(1-eio(P(T,E.grab+.1,E.grab+.42)));
  const e0=ST['02_epiglottis'], e4=ST['04_epiglottis'], e5=ST['05_epiglottis'], e7=ST['07_epiglottis'];
  const mood=T>=e7?'worried':(T>=e5?'angry':(T>=e4?'firm':(T>=e0?'annoyed':'calm')));
  const rot=shut*72+(eT>.1?Math.sin(T*9)*2*eT:Math.sin(T*1.4)*1.2)-popK(T,e5)*4;
  $('epi').setAttribute('transform',`rotate(${rot.toFixed(2)},186,742)`);
  const elook=fp?[22,-24]:(mood==='calm'?[16,26]:[18,34]), ebl=blinkK(T,.4);
  setOEye('eEyeL',28,{dx:elook[0],dy:elook[1],lid:mood==='angry'?.38:(mood==='annoyed'||mood==='firm'?.25:.08),blink:ebl,small:mood==='worried'&&shut<.1});
  setOEye('eEyeR',28,{dx:elook[0],dy:elook[1],lid:mood==='angry'?.38:(mood==='annoyed'||mood==='firm'?.25:.08),blink:ebl,small:mood==='worried'&&shut<.1});
  const eb={calm:[4,-4,4],annoyed:[16,-16,2],firm:[18,-18,0],angry:[26,-26,0],worried:[-18,18,8]}[mood];
  setBrow('eBrowL',166,560,36,eb[0],eb[2]); setBrow('eBrowR',230,552,36,eb[1],eb[2]);
  setMouthV('epi_m',eT,16,{calm:.2,annoyed:-.5,firm:-.6,angry:-1,worried:-.8}[mood],T,2);
  const ew=Math.sin(T*3.4)*6;
  const EA={calm:[[250,650],[300,690],[316,742+ew]],annoyed:[[250,650],[300,700],[310,780+ew]],firm:[[250,650],[320,620],[372,600+ew]],
            angry:[[250,650],[318,686],[352,760+ew]],worried:[[250,650],[290,720],[290,820+ew]]}[mood];
  setHose('eArm',EA,mood==='firm'?-80:150,.8); show('eArm',shut>.3?0:1);
  // the crumb: falls on the shut flap, slides off; the trachea snatches it and eats it
  const cq=P(T,E.close-.55,E.close+.12); let cp=null;
  if(T>=E.close-.55&&T<E.eat+.15){
    if(T<E.close+.12) cp=[lerp(470,486,cq),lerp(-60,706,cq*cq)];
    else if(T<E.grab) cp=[lerp(486,420,P(T,E.close+.12,E.grab)),lerp(706,770,P(T,E.close+.12,E.grab))];
    else {const k=eio(P(T,E.grab+.15,E.eat)); cp=[lerp(420,244,k),lerp(770,1010,k)];}
    show('crumb',1); $('crumb').setAttribute('transform',`translate(${cp[0].toFixed(1)},${cp[1].toFixed(1)}) rotate(${(T*260).toFixed(1)})`);
  } else show('crumb',0);
  // the trachea: whines, pleads, snatches, then the spice hits
  const t1=ST['01_trachea'], t3=ST['03_trachea'], spicy=T>=E.spicy, ate=T>=E.eat;
  const tlook=fp?[26,-34]:(cp?[(cp[0]-244)/4,(cp[1]-960)/4]:(T>=e0&&T<t3||T>=e4&&T<E.close?[-12,-36]:[0,4])), tbl=blinkK(T,1.9);
  setOEye('tEyeL',30,{dx:tlook[0],dy:tlook[1],lid:T>=t3&&T<e4?.0:.1,blink:tbl}); setOEye('tEyeR',30,{dx:tlook[0],dy:tlook[1],lid:T>=t3&&T<e4?.0:.1,blink:tbl});
  show('redEyes',spicy?1:0); show('traBlush',spicy?.9:(ate?.4:0));
  const tb=spicy?[-20,20,10]:(T>=t3&&T<e4?[-14,14,8]:(T<t3?[-8,8,6]:[4,-4,4]));
  setBrow('tBrowL',212,918,40,tb[0],tb[2]); setBrow('tBrowR',276,918,40,tb[1],tb[2]);
  setMouthV('tra_m',tT,spicy?20:15,spicy?-1:(T>=t3&&T<e4?.6:-.3),T,5);
  const shake=spicy?Math.sin(T*40)*4:0, puff=ate&&!spicy?Math.sin(P(T,E.eat,E.eat+.4)*Math.PI)*.06:0;
  $('tra').setAttribute('transform',`translate(${shake.toFixed(1)},0) translate(243,1100) scale(${(1+puff).toFixed(3)},${(1-puff*.5+tT*.012).toFixed(3)}) translate(-243,-1100)`);
  const armsOn=T>=E.close-.25; show('tArmL',armsOn?1:0); show('tArmR',armsOn?1:0);
  if(armsOn){const aw=Math.sin(T*14)*18;
    if(spicy){setHose('tArmL',[[150,1000],[100,950],[150+aw*.6,880]],60,.85); setHose('tArmR',[[336,1000],[390,950],[336-aw*.6,880]],-60,.85);}
    else{const g=cp&&T>=E.grab-.2?cp:[392,1040];setHose('tArmL',[[150,1000],[110,1050],[124,1110]],10,.85);
      setHose('tArmR',[[336,1000],[lerp(390,(g[0]+336)/2+40,cp?1:0),lerp(1040,(g[1]+1000)/2,cp?1:0)],[g[0]+8,g[1]+10]],cp?-150:-10,.85);}}
  // tears, steam, flames
  let tr2='';if(spicy){for(let i=0;i<4;i++){const u=((T*1.3)+i/4)%1, x=i%2?300:188;tr2+=`<path d="M${x},${(980+u*120).toFixed(1)} c5,7 7,13 0,16 c-7,-3 -5,-9 0,-16z" fill="#8fd3f4" ${LN2} opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;}}
  $('tears').innerHTML=tr2;
  let st='';if(spicy){for(let i=0;i<5;i++){const u=((T*.9)+i/5)%1;st+=`<circle cx="${(200+i*22+Math.sin(T*3+i)*14).toFixed(1)}" cy="${(760-u*240).toFixed(1)}" r="${(16+u*26).toFixed(1)}" fill="#fff" opacity="${(.75*Math.sin(u*Math.PI)).toFixed(2)}" ${LN2}/>`;}}
  $('steam').innerHTML=st;
  const fk=P(T,E.fire-.1,E.fire+1.6); let fl='';if(fk>0&&fk<1){for(let i=0;i<3;i++){const s=(.7+.3*Math.sin(T*18+i))*(1-Math.max(0,fk-.8)*5);
    fl+=`<g transform="translate(${190+i*54},${760}) scale(${s.toFixed(2)})"><path d="M0,0 C-26,-10 -24,-44 -6,-70 C-4,-48 10,-44 12,-60 C30,-36 30,-8 0,0Z" fill="#ffb21f" ${LN2}/><path d="M0,-6 C-12,-12 -10,-30 -2,-42 C2,-30 10,-28 10,-38 C18,-24 16,-10 0,-6Z" fill="#ff5a1f"/></g>`;}}
  $('flames').innerHTML=fl;
  [['lbEpi',.15],['lbTra',.25],['lbEso',.35]].forEach(([id,t0])=>{const k=eob(P(T,t0,t0+.3));const e=$(id);if(id==='lbEpi'){e.setAttribute('transform',`translate(52,690) rotate(-90) scale(${k.toFixed(3)})`);}else{show(id,1);e.setAttribute('transform',`translate(${id==='lbTra'?246:560},${id==='lbTra'?852:800}) scale(${k.toFixed(3)})`);}});
}
// ---------- the man at the table ----------
function renderDinner(T){
  const mT=speak('man',T), t0=E.man;
  const cough=Math.max(0,1-P(T,t0+.1,t0+1.1))*Math.abs(Math.sin(T*16));
  tr('patHead',0,Math.sin(T*1.5)*1.5+cough*6,1,1,-4+Math.sin(T*9)*2*cough+(mT>.1?Math.sin(T*6)*1.5:0));
  $('pBrows').setAttribute('d','M-36,62 Q-24,56 -10,62 M8,62 Q22,56 34,62');
  setMouthV('pat_m',Math.max(mT,cough*.7),11,-.8,T,6);
  const sq=.45+.3*cough; setHEye('pEyeL',0,Math.min(.9,sq+blinkK(T,.8))); setHEye('pEyeR',0,Math.min(.9,sq+blinkK(T,.8)));
  show('patBlush',1); show('pSweat',1); $('pSweat').setAttribute('transform',`translate(46,${(70+((T*14)%24)).toFixed(1)})`);
  // hand up at his mouth / throat while he coughs
  const up=eio(P(T,t0,t0+.4)); const sh=[-84,234], el=[lerp(-102,-128,up),lerp(370,330,up)], wr=[lerp(-90,-30,up),lerp(470,190,up)];
  const d=limbD([sh,el,wr],[44,38,32]); $('patArmLD').setAttribute('d',d); $('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1],lerp(-8,140,up),1.2,PSK);
  // red spicy lips, tears and heat lines (drawn over him in scene coords)
  let s=`<g transform="translate(360,430) scale(1.32)"><g transform="translate(0,${(Math.sin(T*1.5)*1.5+cough*6).toFixed(1)}) rotate(${(-4+Math.sin(T*9)*2*cough).toFixed(1)})"><ellipse cx="-4" cy="140" rx="17" ry="9" fill="none" stroke="#e0262c" stroke-width="4" opacity=".8"/>`;
  for(let i=0;i<2;i++){const u=((T*1.2)+i*.5)%1;[-22,18].forEach(x=>{s+=`<path d="M${x},${(100+u*60).toFixed(1)} c4,6 6,11 0,14 c-6,-3 -4,-8 0,-14z" fill="#8fd3f4" ${LN2} opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;});}
  s+=`</g></g>`; for(let i=0;i<4;i++){const u=((T*.8)+i/4)%1;s+=`<path d="M${(120+i*130).toFixed(0)},${(940-u*90).toFixed(1)} q12,-14 0,-28 q-12,-14 0,-28" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity="${(.8*Math.sin(u*Math.PI)).toFixed(2)}"/>`;}
  $('spicyFace').innerHTML=s; show('spicyFace',1);
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  const c=$('cap'),big=KEY.test(w.replace(/[^A-Z'\-]/g,'')); c.textContent=w; c.style.fontSize=big?'56px':'44px'; c.style.fill=big?'#ffd21f':'#fff';
  const k=eo(P(T,ws,ws+.09)); c.setAttribute('transform',`translate(360,1110) scale(${lerp(1.2,1,k)}) translate(-360,-1110)`);}
window.render=function(T){
  const sc=T<T_MAN?1:2; $('sA').setAttribute('display',sc===1?'inline':'none'); $('sB').setAttribute('display',sc===2?'inline':'none');
  const dark=Math.max(P(T,T_MAN-.12,T_MAN)*(T<T_MAN?1:0),T>=T_MAN?1-P(T,T_MAN,T_MAN+.12):0);
  if(sc===1){renderThroat(T); const sh=T>=E.spicy?Math.sin(T*60)*3:0, z=1+.03*P(T,0,T_MAN)+(T>=E.close&&T<E.close+.3?.02*Math.sin(P(T,E.close,E.close+.3)*Math.PI):0);
    $('camA').setAttribute('transform',`translate(${(360+sh).toFixed(1)},640) scale(${z.toFixed(4)}) translate(-360,-660)`);}
  else {renderDinner(T); const z=1.1+.06*eio(P(T,T_MAN,END)); $('camB').setAttribute('transform',`translate(360,600) scale(${z.toFixed(4)}) translate(-360,-575)`);}
  show('indark',dark*.9);
  caption(T);
};
window.render(0);
