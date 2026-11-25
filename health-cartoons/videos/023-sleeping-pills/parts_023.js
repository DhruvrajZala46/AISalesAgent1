// =============== 023: "How do sleeping pills actually work?" The stomach, the brain's worry centre, the bedroom. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${stomachScene()}</g>`, S2=`<g id="s2">${amygScene()}</g>`, S3=`<g id="s3">${bedroomScene().replace('<g id="wifeW"></g><g id="husW"></g>',`<g id="wifeW"><g transform="translate(230,880) scale(1.35)">${wifeSVG()}</g></g><g id="husW"><g id="husI" transform="translate(545,300) scale(1.25)">${patientSVG()}</g></g>`)}</g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +`<g id="cam">`+S1+S2+S3+`</g>`+`<text id="wm" x="360" y="58" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".7">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:8px;font-size:58px"></text></g>`;
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);if($(id+'_m'))setMouthV(id+'_m',talk,mw,mood,T,seed);}
const mv=(id,x,y,r=0,s=1)=>$(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(1)}) scale(${s})`);
const lab=(id,T,a,b,x,y)=>{const on=T>=a&&T<b;show(id,on?1:0);if(on)$(id).setAttribute('transform',`translate(${x},${y}) scale(${(T<.02?1:Math.max(.01,eob(P(T,a-.01,a+.28)))).toFixed(3)})`);};
const ACID=742;
// ---------- scene 1 ----------
function renderStomach(T){
  // the acid pool, sloshing
  const slosh=T>=ST['06_stomach']&&T<E.melt+1.4?1:0;let d=`M-60,${ACID}`;for(let x=-60;x<=820;x+=40)d+=` L${x},${(ACID+Math.sin(x*.02+T*(slosh?7:2.2))*(slosh?16:6)).toFixed(1)}`;d+=' L820,1100 L-60,1100 Z';
  $('acid').innerHTML=`<path d="${d}" fill="${C_ACID}" opacity=".9"/><path d="M-60,${ACID+30} ${Array.from({length:12},(_,k)=>`q36,${k%2?-10:10} 72,0`).join(' ')}" fill="none" stroke="#f6c49c" stroke-width="7" opacity=".7"/>`;
  // two pills fall down the food pipe and splash into the acid
  [[.0,'p1',-26],[.18,'p2',30]].forEach(([dl,id,ox])=>{const t=T-E.drop-dl,k=P(t,0,.8);let x=lerp(282,320+ox,k),y=lerp(120,ACID+70,k*k);
    if(t>.8){x=320+ox+Math.sin(T*2+dl*9)*4;y=ACID+70+eo(P(t,.8,1.6))*60+Math.sin(T*2.4+dl*7)*4;}
    const melt=clamp(P(T,E.melt,E.melt+1.2));mv(id,x,y,t*200*(t<.8)+Math.sin(T*2)*8,(t>.8?1.15:1.3)*(1-melt*.9));});
  let fz='';if(T>=E.melt&&T<E.melt+1.6){for(let j=0;j<10;j++){const q=((T*1.3+j/10)%1);fz+=`<circle cx="${(300+Math.sin(j*2.1)*60).toFixed(0)}" cy="${(ACID+130-q*160).toFixed(0)}" r="${(6+j%3*4)}" fill="#fff" opacity="${(1-q).toFixed(2)}"/>`;}}
  $('fizz').innerHTML=fz;
  // the brain in a thought bubble
  const bOn=T>=E.brain&&T<E.melt,bk=eob(P(T,E.brain,E.brain+.3));show('bub',bOn?1:0);if(bOn)$('bub').setAttribute('transform',`translate(190,222) scale(${bk.toFixed(3)}) translate(-190,-222)`);
  const brT=speak('brain',T);face('br',26,{dx:-14,dy:26,lid:.3,blink:blinkK(T,.9),bx:30,by:-36,bw:26,bA:-12,arch:6,talk:brT,mw:10,mood:-.8,T,seed:3});
  $('brainW').setAttribute('transform',`translate(190,${(224+Math.sin(T*2)*3).toFixed(1)}) rotate(${(brT>.3?Math.sin(T*8)*2:0).toFixed(1)})`);
  // the stomach's face
  const sT=speak('stomach',T);let f={dx:-18,dy:34,lid:.1,bA:16,arch:3,mood:-.6,small:false};
  if(T<ST['02_stomach']){const k=P(T,0,.8),px=lerp(282,320,k),py=lerp(120,ACID+70,k*k);f={dx:(px-540)*.25,dy:(py-390)*.25,lid:.08,bA:22,arch:2,mood:-.9,small:false};}
  if(inL('02_stomach',T))f={dx:-30,dy:-38,lid:0,bA:-4,arch:7,mood:-.2,small:false};
  if(T>=E.brain&&T<E.melt)f={dx:-36,dy:-34,lid:.08,bA:inL('06_stomach',T)?18:-10,arch:inL('06_stomach',T)?2:7,mood:-.7,small:false};
  if(T>=E.melt)f={dx:-20,dy:40,lid:.2,bA:14,arch:3,mood:-.6,small:false};
  face('st',60,{...f,blink:T<1.2?0:blinkK(T,1.4),bx:68,by:-74,bw:64,talk:sT,mw:sT>.05?13:18,T,seed:1});['st_bL','st_bR'].forEach(b=>$(b).setAttribute('stroke-width','9'));
  $('sface').setAttribute('transform',`translate(540,${(390+Math.sin(T*2.1)*4).toFixed(1)})`);
  }
// ---------- scene 2 ----------
const BL=[['bG','bg',470,860,90],['bB','bb',615,920,86],['bY','by',530,1050,96]];
function heat(T){if(T<E.amyg+.2)return 1;if(T<ST['07_officer']+1.8)return 1;if(T<E.flare)return 1-eio(P(T,ST['07_officer']+1.8,ST['07_officer']+2.8))*.75;if(T<E.calm)return Math.min(1.25,.25+eob(P(T,E.flare,E.flare+.5)));
  return 1.2-clamp(P(T,E.q1,E.q1+.4))*.4-clamp(P(T,E.q2,E.q2+.4))*.4-clamp(P(T,E.q3,E.q3+.4))*.4;}
function flame(w,h,T,seed){let s='';for(let j=0;j<7;j++){const a=(-165+j*25)*Math.PI/180,bx=Math.cos(a)*w*.82,by=Math.sin(a)*w*.75,hh=h*(.55+.45*Math.abs(Math.sin(T*5+seed+j*1.9)))*(1-Math.abs(j-3)*.1),sw=Math.sin(T*7+j*2+seed)*w*.2;
  const tg=(k,f,st)=>`<path d="M${(bx-w*.22*k).toFixed(1)},${by.toFixed(1)} C${(bx-w*.3*k).toFixed(1)},${(by-hh*.45*k).toFixed(1)} ${(bx+sw-w*.1*k).toFixed(1)},${(by-hh*.75*k).toFixed(1)} ${(bx+sw).toFixed(1)},${(by-hh*k).toFixed(1)} C${(bx+sw+w*.08*k).toFixed(1)},${(by-hh*.7*k).toFixed(1)} ${(bx+w*.32*k).toFixed(1)},${(by-hh*.45*k).toFixed(1)} ${(bx+w*.22*k).toFixed(1)},${by.toFixed(1)} Z" fill="${f}" ${st}/>`;
  s+=tg(1,'#f3921c','stroke="#c9561a" stroke-width="3"')+tg(.55,'#fcd94a','');}return s;}
function renderAmyg(T){
  const h=heat(T),blast=T>=E.blast&&T<E.blast+1.4,beaten=T>=E.blast+1.1;
  BL.forEach(([g,id,x,y,w],i)=>{const sh=h>.5?Math.sin(T*(30+i*6))*4*h:0;mv(g,x+sh,y+Math.sin(T*2+i)*4,0,1);
    $(g).querySelector('.fl').innerHTML=h>.08?`<g transform="scale(${Math.min(1,h).toFixed(2)})">${flame(w,w*1.7,T,i*3)}</g>`:'';$(g).querySelector('.mark').setAttribute('opacity',h>.4?'1':'0');
    const calm=h<.4;face(id,w*.24,{dx:calm?0:-14,dy:calm?4:-2,lid:calm?.4:0,blink:calm?blinkK(T,i):0,small:false,bx:w*.34,by:-w*.58,bw:w*.34,bA:calm?-4:30,arch:calm?6:1,talk:0,mw:12,mood:calm?.8:-1,T,seed:i});
    ['_eL','_eR'].forEach(s=>{const e=$(id+s+'_p');if(e){e.setAttribute('fill',calm?'#1b1717':'#d81e1e');e.setAttribute('r',(w*.24*(calm?.46:.36)).toFixed(1));}});});
  $('firePool').innerHTML=h>.3?`<path d="M420,1140 ${Array.from({length:6},(_,k)=>`q${15},${-(18+Math.abs(Math.sin(T*6+k))*22).toFixed(0)} 30,0`).join(' ')} q-60,26 -180,0 Z" fill="#fcd94a" stroke="#e39a1a" stroke-width="4" opacity="${Math.min(1,h).toFixed(2)}"/>`:'';
  // the cop: walks in, waves his arms, gets caught in the brawl
  const cT=speak('officer',T),ik=eo(P(T,E.amyg,E.amyg+.6));let cx=lerp(-160,190,ik);
  mv('copW',cx+(beaten?0:Math.sin(T*1.6)*3),700+(cT>.2?-Math.abs(Math.sin(T*10))*5:0),0,.86);
  $('copArmR').setAttribute('transform',`rotate(${(cT>.25&&!beaten?-60+Math.sin(T*8)*25:0).toFixed(1)},78,180)`);$('copArmL').setAttribute('transform',`rotate(${(cT>.25&&!beaten?40+Math.sin(T*8+1)*20:0).toFixed(1)},-78,180)`);
  show('bruise',beaten?1:0);
  const mad=inL('08_officer',T)||inL('11_officer',T);
  face('cp',14,{dx:14,dy:beaten&&T<E.pillin?18:0,lid:beaten?.45:.1,blink:blinkK(T,.6),bx:22,by:-20,bw:22,bA:mad||beaten?18:2,arch:3,talk:cT,mw:12,mood:T>=ST['13_officer']?.6:-.5,T,seed:4});
  // the smoke cloud of the brawl
  show('smoke',blast?1:0);if(blast){let s='';for(let j=0;j<9;j++){const a=j*.7+T*3,r=110+Math.sin(T*9+j)*20;s+=`<circle cx="${(440+Math.cos(a)*120).toFixed(0)}" cy="${(790+Math.sin(a)*90).toFixed(0)}" r="${r.toFixed(0)}" fill="#f4f4f2" ${OLW2}/>`;}
    for(let j=0;j<5;j++){const a=T*7+j*1.3;s+=`<path transform="translate(${(440+Math.cos(a)*190).toFixed(0)},${(780+Math.sin(a)*150).toFixed(0)}) rotate(${(a*60).toFixed(0)})" d="M-16,0 l12,-4 l4,-12 l4,12 l12,4 l-12,4 l-4,12 l-4,-12 Z" fill="#ffe81a" stroke="${INK}" stroke-width="2"/>`;}$('smoke').innerHTML=s;}
  // the sleeping pill walks in from the bottom left
  const pk=eo(P(T,E.pillin,E.pillin+.7)),pT=speak('pill',T),pOn=T>=E.pillin;show('spW',pOn?1:0);
  if(pOn){const walk=T<E.pillin+.7?Math.abs(Math.sin(T*14))*-10:0;mv('spW',lerp(-120,150,pk),1196+walk+(pT>.2?-Math.abs(Math.sin(T*9))*4:0),Math.sin(T*2)*3,.75);
    face('sp',18,{dx:16,dy:-8,lid:0,blink:blinkK(T,1.8),bx:22,by:-28,bw:18,bA:-6,arch:6,talk:pT,mw:9,mood:.8,T,seed:5});}}
// ---------- scene 3 ----------
function renderBed(T){const hT=speak('husband',T);
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,-4+(hT>.2?Math.sin(T*7)*1.5:0));$('pBrows').setAttribute('d','M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70');
  setMouthV('pat_m',hT,10,.6,T,6);setHEye('pEyeL',-4,blinkK(T,2.1));setHEye('pEyeR',-4,blinkK(T,2.1));show('patBlush',0);show('pSweat',0);
  const P3=[[-84,234],[-100,370],[-92,468]],dd=limbD(P3,[44,38,32]);$('patArmLD').setAttribute('d',dd);$('patArmLO').setAttribute('d',dd);$('patHandL').innerHTML=hand(-92,480,-8,1.2,PSK);
  setHEye('wEyeL',4,blinkK(T,1.6));setHEye('wEyeR',4,blinkK(T,1.6));$('wifeMouth').setAttribute('ry',(4+Math.abs(Math.sin(T*.8))*1).toFixed(1));$('wifeMouth').setAttribute('rx','13');
  $('wifeHead').setAttribute('transform',`rotate(${(Math.sin(T*1.2)*1.5+4).toFixed(2)},-8,-230)`);}
function caption(T,sc){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const y0={1:1020,2:1020,3:1020}[sc],x0=360;c.setAttribute('x',x0);c.setAttribute('y',y0+17);const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(${x0},${y0}) scale(${lerp(1.4,1,k).toFixed(3)}) translate(${-x0},${-y0})`);}
window.render=function(T){
  const sc=T<E.amyg?1:(T<E.home?2:3);[1,2,3].forEach(i=>$('s'+i).setAttribute('display',sc===i?'inline':'none'));
  if(sc===1)renderStomach(T);if(sc===2)renderAmyg(T);if(sc===3)renderBed(T);
  
  $('cam').setAttribute('transform',`translate(360,640) scale(${(1.012+Math.sin(T*1.4)*.012).toFixed(4)}) translate(-360,-640)`);
  caption(T,sc);};
window.render(0);
