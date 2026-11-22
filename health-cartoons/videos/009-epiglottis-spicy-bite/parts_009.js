// =============== 009 v2: the reference's staging shot for shot (exact script), our code characters ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
function popK(T,t0){const k=P(T,t0,t0+.18);return k<1?Math.sin(k*Math.PI):0;}
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const T_MAN=E.man;
let SA=`<g id="sA"><g id="camA">${throatWorld()}</g>${throatLabels()}</g>`;
let SB=`<g id="sB"><g id="camB">${dinnerWorld()}</g></g>`;
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}${GDEF}</defs>`
 +SA+SB+`<g id="capg"><text id="cap" x="370" y="1004" text-anchor="middle" style="font-family:'DejaVu Serif',serif;font-weight:700;font-size:50px;paint-order:stroke;stroke:#111;stroke-width:8px;stroke-linejoin:round" fill="#fff"></text></g>`;

// ---------- the epiglottis flap: one tapered shape that bends from "open" (up) to "shut" (lying over the airway) ----------
const FLAP_UP=[[150,620],[205,500],[262,412],[318,350],[346,326]], FLAP_DN=[[150,620],[214,598],[290,592],[370,598],[424,604]], FLAP_W=[170,112,80,54,30];
function setFlap(k){const pts=FLAP_UP.map((p,i)=>[lerp(p[0],FLAP_DN[i][0],k),lerp(p[1],FLAP_DN[i][1],k)]);
  $('flapO').setAttribute('d',limbD(pts,FLAP_W)); const st=smooth(pts.slice(1)); $('flapS1').setAttribute('d',st); $('flapS2').setAttribute('d',st);}
// ---------- food chunks: fall down the middle of the throat into the top of the food pipe ----------
function dropChunk(id,t0,T,dur=.9){const q=(T-t0)/dur; if(q<0||q>1.3){show(id,0);return null;} show(id,1);
  let x=lerp(456,412,eio(Math.min(q,1))), y=lerp(-130,640,Math.min(q,1)*Math.min(q,1)), sx=1, sy=1, op=1;
  if(q>1){const u=(q-1)/.3; y=640+u*70; sx=1-u*.45; sy=1-u*.6; op=1-u;}
  $(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${(Math.sin(q*5)*8).toFixed(1)}) scale(${sx.toFixed(3)},${sy.toFixed(3)})`); $(id).setAttribute('opacity',op.toFixed(2));
  return [x,y];}
function renderThroat(T){
  const tT=speak('trachea',T), eT=speak('epiglottis',T);
  const f1=dropChunk('food1',E.food1,T), f2=dropChunk('food2',E.food2,T);
  // the third chunk: lands on the closing flap by the food pipe, the windpipe grabs it and eats it
  let f3=null;
  if(T>=E.food3&&T<E.spicy-.05){show('food3',1); let x,y,sc=1;
    if(T<E.close+.1){const q=P(T,E.food3,E.close+.1); x=lerp(462,436,q); y=lerp(-130,600,q*q);}
    else if(T<E.grab+.05){x=436+Math.sin(T*30)*2; y=600;}
    else {const k=eio(P(T,E.grab+.05,E.grab+.5)); x=lerp(436,300,k); y=lerp(600,1004,k); sc=lerp(1,.55,k);
      sc*=T>=ST['05_epiglottis']+1.5?.7:(T>=ST['05_epiglottis']+.9?.85:1);}
    f3=[x,y]; $('food3').setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${(T<E.close?Math.sin(T*6)*8:-16).toFixed(1)}) scale(${sc.toFixed(3)})`);}
  else show('food3',0);
  const fp=f1||f2||(T<E.close+.1?f3:null);
  // epiglottis
  const shut=eob(P(T,E.close-.05,E.close+.22))*(1-eio(P(T,E.grab+.25,E.grab+.55)));
  setFlap(clamp(shut,0,1.08));
  const e0=ST['02_epiglottis'], e4=ST['04_epiglottis'], e5=ST['05_epiglottis'], e7=ST['07_epiglottis'];
  const mood=shut>.2?'shock':(T>=e7?'worried':(T>=e5?'angry':(T>=e4?'firm':(T>=e0?'annoyed':'calm'))));
  const el=fp&&shut<.2?[26,-38]:(mood==='shock'?[34,-6]:(T>=ST['01_trachea']?[16,38]:[18,30])), ebl=blinkK(T,.4);
  const lid={calm:.1,annoyed:.32,firm:.3,angry:.45,worried:.12,shock:0}[mood];
  setOEye('eEyeL',40,{dx:el[0],dy:el[1],lid,blink:mood==='shock'?0:ebl}); setOEye('eEyeR',40,{dx:el[0],dy:el[1],lid,blink:mood==='shock'?0:ebl});
  const bb={calm:[0,0,6],annoyed:[14,-14,2],firm:[16,-16,0],angry:[24,-24,0],worried:[-16,16,8],shock:[-20,20,10]}[mood];
  $('eBrowL').setAttribute('d',`M80,${538-bb[2]} Q105,${524-bb[2]} 132,${538-bb[2]}`); $('eBrowL').setAttribute('transform',`rotate(${bb[0]},105,534)`);
  $('eBrowR').setAttribute('d',`M166,${532-bb[2]} Q192,${518-bb[2]} 218,${532-bb[2]}`); $('eBrowR').setAttribute('transform',`rotate(${bb[1]},192,528)`);
  show('grit',mood==='shock'?1:0); show('epi_m',mood==='shock'?0:1);
  setMouthV('epi_m',eT,18,{calm:.2,annoyed:-.5,firm:-.6,angry:-1,worried:-.8,shock:0}[mood],T,2);
  $('epiG').setAttribute('transform',`translate(150,700) rotate(${(eT>.1?Math.sin(T*9)*1.6*eT:Math.sin(T*1.4)*.8).toFixed(2)}) translate(-150,-700)`);
  // the windpipe
  const t3=ST['03_trachea'], red=T>=E.fire-.3, eating=T>=E.grab+.3&&T<E.spicy-.05;
  const tl=fp&&shut<.2?[16,-40]:(T>=E.grab-.3&&T<E.grab+.3&&f3?[20,-40]:(eating?[-6,10]:[-14,-38])), tb=blinkK(T,1.9);
  const tlid=T>=t3&&T<e4?0:.08;
  setOEye('tEyeL',42,{dx:tl[0],dy:tl[1],lid:tlid,blink:tb}); setOEye('tEyeR',42,{dx:tl[0],dy:tl[1],lid:tlid,blink:tb});
  show('redEyes',red?1:0);
  const plead=T>=t3&&T<e4+.5, tbr=red?[-18,18,12]:(plead?[-16,16,10]:[-6,6,6]);
  $('tBrowL').setAttribute('d',`M218,${890-tbr[2]} Q246,${876-tbr[2]} 274,${890-tbr[2]}`); $('tBrowL').setAttribute('transform',`rotate(${tbr[0]},246,886)`);
  $('tBrowR').setAttribute('d',`M304,${890-tbr[2]} Q332,${876-tbr[2]} 360,${890-tbr[2]}`); $('tBrowR').setAttribute('transform',`rotate(${tbr[1]},332,886)`);
  const chew=eating?(.35+.3*Math.abs(Math.sin(T*9))):0;
  setMouthV('tra_m',Math.max(tT,chew),20,red?-1:(plead?.6:-.3),T,5);
  const sh=red?Math.sin(T*34)*3:0; $('traFace').setAttribute('transform',`translate(${sh.toFixed(1)},${(Math.sin(T*2.2)*3).toFixed(1)})`);
  let tears='';if(red){for(let i=0;i<4;i++){const u=((T*1.4)+i/4)%1,x=i%2?332:246;tears+=`<path d="M${x-12},${(1000+u*120).toFixed(1)} c6,8 8,15 0,19 c-8,-4 -6,-11 0,-19z" fill="#7fc8ef" ${OLW} opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;}} $('tTears').innerHTML=tears;
  const armsOn=T>=E.close-.25; show('tArmL',armsOn?1:0); show('tArmR',armsOn?1:0);
  if(armsOn){const w=Math.sin(T*14)*14;
    if(T<E.grab+.08){const g=f3||[436,600], k=eob(P(T,E.close-.25,E.close+.1));
      setHose('tArmL',[[212,980],[lerp(190,300,k),lerp(1040,800,k)],[lerp(170,g[0]-34,k),lerp(1080,g[1]+60,k)]],lerp(20,170,k),.9);
      setHose('tArmR',[[378,980],[lerp(420,450,k),lerp(1040,800,k)],[lerp(430,g[0]+30,k),lerp(1080,g[1]+66,k)]],lerp(-20,-170,k),.9);}
    else if(!red){const g=f3||[300,1004];
      setHose('tArmL',[[212,980],[176,1040],[184,1100]],10,.9); setHose('tArmR',[[378,980],[400,1040],[g[0]+34,g[1]+30]],-120,.9);}
    else {setHose('tArmL',[[212,980],[150,1030],[150+w*.4,1100]],30,.9); setHose('tArmR',[[378,980],[440,1030],[440-w*.4,1100]],-30,.9);}}
  // labels as in the reference (always on, pop in at the start)
  [['lbEpi',.1],['lbTra',.2],['lbEso',.3]].forEach(([id,t0])=>{const k=eob(P(T,t0,t0+.3)),e=$(id); if(!e.getAttribute('data-b'))e.setAttribute('data-b',e.getAttribute('transform')); e.setAttribute('transform',e.getAttribute('data-b')+` scale(${k.toFixed(3)})`);});
}
// ---------- the man at the table ----------
function renderDinner(T){
  const mT=speak('man',T), m0=ST['08_man'], hit=T>=m0-.1;
  const hy=Math.sin(T*1.5)*1.5+(hit?Math.abs(Math.sin(T*15))*4*(1-P(T,m0,m0+1.2)):0), hr=hit?-4+Math.sin(T*8)*2.5:Math.sin(T*1.2)*1;
  tr('patHead',0,hy,1,1,hr);
  $('pBrows').setAttribute('d',hit?'M-36,62 Q-24,54 -10,62 M8,62 Q22,54 34,62':'M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70');
  const chew=!hit?.3+.3*Math.abs(Math.sin(T*8)):0;
  setMouthV('pat_m',Math.max(mT,chew,hit&&T<m0+.5?.6:0),11,hit?-.8:.2,T,6);
  const shut=hit?.15:.92; setHEye('pEyeL',0,Math.min(.95,shut+blinkK(T,.8))); setHEye('pEyeR',0,Math.min(.95,shut+blinkK(T,.8)));
  show('patBlush',hit?1:0); show('pSweat',hit?1:0); $('pSweat').setAttribute('transform',`translate(46,${(70+((T*14)%24)).toFixed(1)})`);
  const d=limbD([[-84,234],[-132,300],[-112,356]],[44,38,32]); $('patArmLD').setAttribute('d',d); $('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(-112,360,-10,1.2,PSK);
  let s='';if(hit){s=`<g transform="translate(390,206) scale(1.9)"><g transform="translate(0,${hy.toFixed(2)}) rotate(${hr.toFixed(2)})">
    <ellipse cx="-22" cy="88" rx="11" ry="6" fill="#e3242c" opacity=".7"/><ellipse cx="18" cy="88" rx="11" ry="6" fill="#e3242c" opacity=".7"/>
    <ellipse cx="-4" cy="${(142+mT*3).toFixed(1)}" rx="${(10+mT*3).toFixed(1)}" ry="${(6+mT*5).toFixed(1)}" fill="#e3242c" stroke="${INK}" stroke-width="1.6"/>`;
    for(let i=0;i<2;i++){const u=((T*1.1)+i*.5)%1;[-30,26].forEach(x=>{s+=`<path d="M${x},${(98+u*44).toFixed(1)} c4,5 5,10 0,12 c-5,-2 -4,-7 0,-12z" fill="#7fc8ef" stroke="${INK}" stroke-width="1.2" opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;});}
    s+=`</g></g>`;}
  $('manFx').innerHTML=s;
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  const c=$('cap'); c.textContent=w==='I'?'I':w.toLowerCase();
  const k=eo(P(T,ws,ws+.08)); c.setAttribute('transform',`translate(370,1004) scale(${lerp(1.12,1,k)}) translate(-370,-1004)`);}
window.render=function(T){
  const sc=T<T_MAN?1:2; $('sA').setAttribute('display',sc===1?'inline':'none'); $('sB').setAttribute('display',sc===2?'inline':'none');
  if(sc===1){renderThroat(T);
    const pin=eio(P(T,E.close-.2,E.close+.1))*(1-eio(P(T,E.grab+.55,E.grab+.95)));
    const z=1+.13*pin, cx=lerp(360,300,pin), cy=lerp(640,690,pin);
    $('camA').setAttribute('transform',`translate(360,640) scale(${z.toFixed(4)}) translate(${(-cx).toFixed(1)},${(-cy).toFixed(1)})`);}
  else {renderDinner(T); const z=1+.04*eio(P(T,T_MAN,END)); $('camB').setAttribute('transform',`translate(360,600) scale(${z.toFixed(4)}) translate(-360,-600)`);}
  caption(T);
};
window.render(0);
