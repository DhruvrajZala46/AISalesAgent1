// =============== 015: "Where does the extra fat go?" Five scenes in the reference's order; our characters and words. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${liverScene()}</g>`, S2=`<g id="s2"><g transform="translate(0,930) scale(1.1) translate(0,-930)">${corridor()}</g>${labelBox('lbLiv','INSIDE THE LIVER',150,150,22)}</g>`, S4=`<g id="s4">${bodyScene()}</g>`, S5=`<g id="s5">${clinic15()}</g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+S2+S4+S5+`<text id="wm" x="360" y="64" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".6">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);setMouthV(id+'_m',talk,mw,mood,T,seed);}
const drop=(x,y,o,c='#bfe9ff')=>`<path transform="translate(${x.toFixed(1)},${y.toFixed(1)}) scale(1.5)" d="M0,-9 C5,-2 7,3 5,7 C3,11 -4,11 -5,7 C-7,3 -4,-2 0,-9Z" fill="${c}" stroke="${INK}" stroke-width="1.8" opacity="${o.toFixed(2)}"/>`;

// ---------- scene 1: the liver lifts, complains, and gives up ----------
function renderLiver(T){
  const tired=T>=E.drop,ph=(T%1.0)/1.0,rep=tired?0:.5-.5*Math.cos(ph*Math.PI*2),strain=tired?0:Math.pow(1-rep,2);
  const fall=tired?Math.min(1,(T-E.drop)/.14):0,land=tired?Math.exp(-(T-E.drop-.14)*9)*Math.cos((T-E.drop-.14)*26)*(T>E.drop+.14?1:0):0;
  const by=tired?lerp(760,905,fall*fall)-land*14:780-150*rep, lt=speak('liver',T);
  $('livB').setAttribute('transform',`translate(0,${(-rep*10+(tired?14:0)+Math.sin(T*2)*2).toFixed(1)}) scale(1,${(1+rep*.012).toFixed(4)})`);
  $('bar').setAttribute('transform',`translate(0,${by.toFixed(1)}) rotate(${(tired?0:Math.sin(T*6.28)*1.2).toFixed(2)},350,0)`);
  const arm=(sx,hx,o)=>{const hy=tired?lerp(700,660,fall):by,ex=sx+(hx-sx)*.5+o*(tired?30:46*(1-rep)),ey=(560+hy)/2+(tired?30:0);return `M${sx},540 Q${ex.toFixed(1)},${ey.toFixed(1)} ${tired?sx+o*-8:hx},${hy.toFixed(1)}`;};
  const dL=arm(200,230,-1),dR=arm(500,470,1);['armLo','armL'].forEach(i=>$(i).setAttribute('d',dL));['armRo','armR'].forEach(i=>$(i).setAttribute('d',dR));
  let f={dx:0,dy:18,lid:.05,bA:16-rep*6,arch:3,mood:-.6,small:false};
  if(T>4.2&&!tired)f={dx:10,dy:-30,lid:.1,bA:18,arch:2,mood:-.7,small:false};          // glaring up at "the guy upstairs"
  if(tired)f={dx:0,dy:22,lid:.55,bA:-12,arch:2,mood:-.8,small:false};
  face('lv',34,{...f,blink:blinkK(T,.9),bx:52,by:-54-(tired?0:strain*4),bw:40,talk:lt,mw:22,T,seed:3});
  let dr='';[0,1].forEach(j=>{const p=((T*.55+j*.5)%1),x=j?520:250;dr+=`<g transform="translate(${x},${(318+p*p*250).toFixed(1)})"><ellipse rx="11" ry="${(13+p*8).toFixed(1)}" fill="${C_FAT}" ${OLW2} opacity="${(p<.85?1:(1-p)/.15).toFixed(2)}"/></g>`;});
  $('drips').innerHTML=dr;
  let sw='';const k=tired?1:.6;[[110,330,0],[610,300,1],[640,380,2]].forEach(([x,y,j])=>{const p=((T*(tired?1.5:1)+j*.37)%1);sw+=drop(x+(j?10:-10)*p,y+p*46,(1-p)*k);});
  $('lsweat').innerHTML=sw;
}
// ---------- scene 2: insulin pushes the fat from door to door ----------
const segs=[[E.cor,E.a,150,XA-270],[E.w2,E.b,XA-270,XB-270],[E.w3,E.c,XB-270,XC-270],[E.w4,E.d,XC-270,XD-430]];
function i1x(T){let x=150;for(const [t0,t1,a,b] of segs){if(T<t0)break;x=lerp(a,b,eio(P(T,t0,t1)));}return x;}
function renderCorridor(T){
  const x=i1x(T),v=Math.abs(x-i1x(T-.04))>.4,bob=v?Math.abs(Math.sin(T*10.5))*10:0,camX=x-170+80*eio(P(T,E.in2-.2,E.in2+.8));show('lbLiv',1);
  $('corW').setAttribute('transform',`translate(${(-camX).toFixed(1)},0)`);
  $('i1w').setAttribute('transform',`translate(${x.toFixed(1)},${(FLOOR+70-bob).toFixed(1)}) rotate(${v?4:0})`);
  // the wheelbarrow, and tipping it into BODY FAT STORAGE
  const tip=eio(P(T,E.d+.45,E.d+.9))*(1-eio(P(T,E.d+1.45,E.d+1.75))),slide=eio(P(T,E.d+.7,E.d+1.3));
  $('barrow').setAttribute('transform',`translate(${(x+200).toFixed(1)},${(FLOOR+86+(v?Math.sin(T*21)*1.5:0)).toFixed(1)}) scale(1.25) rotate(${(tip*30).toFixed(1)},62,2)`);
  $('fatPile').setAttribute('transform',`translate(${(slide*210).toFixed(1)},${(slide*18).toFixed(1)}) scale(${(1-.35*slide).toFixed(3)})`);show('fatPile',slide<1?1:0);
  show('dD_open',T>=E.d+.15&&T<E.d+1.75?1:0);
  // knocks and the STORAGE FULL signs
  let fx='',kn=0,lookDoor=false;[['a',XA,'dA'],['b',XB,'dB'],['c',XC,'dC']].forEach(([k,X,id])=>{const t0=E[k];
    if(T>=t0+.02&&T<t0+.5){kn=Math.abs(Math.sin((T-t0-.02)*Math.PI/.24));lookDoor=true;
      if(kn>.75)fx+=`<path transform="translate(${X-60},640)" d="M0,-34 L9,-10 L34,-10 L14,6 L22,32 L0,16 L-22,32 L-14,6 L-34,-10 L-9,-10 Z" fill="#ffd23a" ${OLW2}/>`;}
    const on=T>=t0+.55;show(id+'_full',on?1:0);if(on)$(id+'_full').setAttribute('transform',`translate(${X},545) scale(${eob(P(T,t0+.55,t0+.8)).toFixed(3)}) translate(${-X},-545)`);
    if(T>=t0&&T<t0+1.2)lookDoor=true;});
  $('fxk').innerHTML=fx;
  $('i1_arm').setAttribute('transform',`rotate(${(-kn*62-(tip>0?20*tip:0)).toFixed(1)},44,-40)`);
  // the second insulin
  const in2=T>=E.in2,x2=in2?(T<E.w4?lerp(camX+900,x+400,eo(P(T,E.in2,E.in2+.8))):x+400):camX+1000;
  const v2=in2&&(T<E.in2+.8||(T>=E.w4&&T<E.d)),bob2=v2?Math.abs(Math.sin(T*10.5+1))*10:0;
  $('i2w').setAttribute('transform',`translate(${x2.toFixed(1)},${(FLOOR+70-bob2).toFixed(1)})`);show('i2w',in2?1:0);
  const t1=speak('ins',T),t2=speak('ins2',T),both=T>=E.in2+.6;
  let f1={dx:18,dy:6,lid:.08,bA:-12,arch:6,mood:-.4};
  if(lookDoor)f1={dx:24,dy:-20,lid:.05,bA:-10,arch:7,mood:-.4};
  if(inL('06_ins',T))f1={dx:-6,dy:12,lid:.2,bA:-16,arch:3,mood:-.7};
  if(both)f1={dx:26,dy:-6,lid:.08,bA:inL('10_ins',T)?-14:-8,arch:6,mood:inL('08_ins',T)?-.7:-.2};
  if(T>=E.w4)f1={dx:22,dy:4,lid:.1,bA:2,arch:5,mood:.2};
  face('i1',15,{...f1,blink:blinkK(T,.5),bx:19,by:-26,bw:20,talk:t1,mw:9,T,seed:1});
  $('i1_s').setAttribute('transform',`scale(${(1+(t1>.4?.02:0)-Math.sin(T*3.1)*.012).toFixed(3)},${(1-bob*.004+Math.sin(T*3.1)*.018).toFixed(3)})`);$('i2_s').setAttribute('transform',`scale(${(1-Math.sin(T*2.7+1)*.012).toFixed(3)},${(1+Math.sin(T*2.7+1)*.018).toFixed(3)})`);
  const calm=T>=ST['09_ins2']-.1;
  face('i2',15,{dx:calm&&!inL('09_ins2',T)?22:18,dy:calm?4:-4,lid:calm?.25:.05,blink:blinkK(T,2.2),bx:19,by:-26-(inL('09_ins2',T,0,-3.5)?5:0),bw:20,bA:calm?4:-8,arch:calm?6:8,talk:t2,mw:9,mood:calm?.6:.1,T,seed:2});
}
// ---------- scene 4: the body fat grows ----------
function renderBody(T){const t=T-E.body;
  [['f1',.0],['f2',.25],['f3',.5],['f4',.8],['f5',1.1]].forEach(([id,d],i)=>{const k=eob(P(t,d,d+.55)),g=.35+.65*k+.25*P(t,d+.55,2.8)+Math.sin(T*5+i)*.015;
    const e=$(id),base=e.getAttribute('data-b')||e.getAttribute('transform');e.setAttribute('data-b',base);e.setAttribute('transform',`${base} scale(${(k>0?g:0).toFixed(3)})`);});
  $('belly').setAttribute('transform',`translate(360,640) scale(${(1+.05*P(t,.3,2.8)).toFixed(4)},1) translate(-360,-640)`);}
// ---------- scene 5: the clinic ----------
function renderClinic(T){
  const dT=speak('doctor',T),pT=speak('patient',T),d0=ST['13_doctor'],sad=T>=ST['14_patient']-.2,hope=T>=ST['15_doctor'];
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,3+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,hope?.7:.2,T,5);setHEye('dEyeL',4,blinkK(T,.7));setHEye('dEyeR',4,blinkK(T,.7));
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
  let pr=-3+Math.sin(T*.8)*1;if(pT>.2)pr+=Math.sin(T*7)*2;if(sad&&!hope)pr+=5;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2+(sad&&!hope?4:0),1,1,pr);
  $('pBrows').setAttribute('d',T<d0?'M-36,70 Q-24,62 -10,64 M8,64 Q22,62 34,70':'M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66');
  setMouthV('pat_m',pT,10,T<d0?.5:(hope?.2:-.6),T,6);setHEye('pEyeL',-4,blinkK(T,2.1));setHEye('pEyeR',-4,blinkK(T,2.1));
  show('patBlush',sad?.5:.2);show('pSweat',0);
  const sh=[-84,234],el=[-108,356],wr=[-100,470];const d=limbD([sh,el,wr],[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1]+8,10,1.2,PSK);
  const n=Math.round(lerp(0,214,eo(P(T,E.clinic+.1,E.clinic+.9))));$('scaleTxt').textContent=n;
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,998) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,-998)`);}
window.render=function(T){
  const sc=T<E.cor?1:(T<E.body?2:(T<E.clinic?4:5));
  [1,2,4,5].forEach(i=>$('s'+i).setAttribute('display',sc===i?'inline':'none'));
  if(sc===1)renderLiver(T);if(sc===2)renderCorridor(T);if(sc===4)renderBody(T);if(sc===5)renderClinic(T);
  caption(T);};
window.render(0);
