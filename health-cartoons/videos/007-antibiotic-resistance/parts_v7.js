// =============== 007: antibiotic resistance - remake of the 17M reference. Library art + code-drawn characters (no image model) ===============
const A=window.ART, E=D.ev, ST=D.start, END=D.end;
const KEY=/^(ANTIBIOTICS|ANTIBIOTIC|HEADACHE|BURNS|STOP|CUT|WAY|SKIN|BACTERIA|WHITE|BLOOD|CELLS|CELL|MESS|BACKUP|FAST|ANOTHER|INTRUDER|MATCH|RESIST|WEAPONS|INFECTION|RESISTANCE|MISUSED|ADAPT|STRONGER|UH-OH)$/;
//__VISEME__
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
function actorSVG(id){return `<g id="${id}"><image id="${id}_img" preserveAspectRatio="none"/></g>`;}
const lastPose={};
function placeActor(id,pose,fx,fy,H,o={}){
  const m=A[pose], w=H*m.w/m.h; let file=pose; const V=m.variants||[];
  if(V.length){const env=o.env||0, f=Math.floor((o.T||0)*15)+(o.seed||0); let open=env>0.12; if(open&&env<0.45&&f%3===0) open=false; file=pose+'_'+(open&&V.includes('o')?'o':'c');}
  const im=$(id+'_img'); if(lastPose[id]!==file){im.setAttribute('href','art/'+file+'.png');lastPose[id]=file;}
  im.setAttribute('x',(-w/2).toFixed(1)); im.setAttribute('y',(-H).toFixed(1)); im.setAttribute('width',w.toFixed(1)); im.setAttribute('height',H.toFixed(1));
  $(id).setAttribute('transform',`translate(${fx.toFixed(1)},${fy.toFixed(1)}) rotate(${(o.rot||0).toFixed(2)}) scale(${(o.sx||1).toFixed(4)},${(o.sy||1).toFixed(4)})`);
}
function poseAt(T,segs,def){let p=def,t0=0;for(const [a,b,q] of segs) if(T>=a&&T<b){p=q;t0=a;} return [p,t0];}
function popK(T,t0){const k=P(T,t0,t0+.18);return k<1?Math.sin(k*Math.PI):0;}
function along(pts,s){s=clamp(s)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;return [lerp(pts[i][0],pts[i+1][0],f),lerp(pts[i][1],pts[i+1][1],f)];}
const IMG=(f)=>`<image href="art/${f}" x="-5.5" y="0" width="731" height="1280" preserveAspectRatio="none"/>`;
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
// capsule (red + white), drawn like the antibiotic soldier but tiny and faceless
function capsule(id){return `<g id="${id}"><rect x="-16" y="-34" width="32" height="68" rx="16" fill="#fff" ${STK2}/><path d="M-16,0 L-16,-18 A16,16 0 0 1 16,-18 L16,0Z" fill="#e0392f" ${STK2}/><path d="M-9,-22 L-9,-6" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".7"/></g>`;}
// ---------- geometry ----------
const STO=[382,1052,690], BUD=[138,1012,165];
const PIPE=[[180,350],[184,385],[218,436],[251,498],[262,600],[262,741],[280,793],[313,850],[352,905]];
// ---------- SCENE 1: the stomach ----------
let S1=`<g id="s1"><g id="cam1"><g id="wStomach">${IMG('plate_abdomen.jpg')}${actorSVG('sto')}${actorSVG('bud')}
  <g id="caps">${capsule('cp0')}${capsule('cp1')}${capsule('cp2')}</g><g id="steam1"></g><g id="burnGlow" opacity="0"><ellipse cx="380" cy="900" rx="170" ry="60" fill="#ff5a2a" filter="url(#soft)"/></g></g></g>
 ${labelBox('lbSto','STOMACH',560,300,24)}${labelBox('lbAb','ANTIBIOTIC',540,900,22)}
</g>`;
// ---------- SCENE 2: the skin (all code) ----------
let S2=`<g id="s2"><g id="cam2"><g id="wSkin">${tissueSVG()}
  ${bactSVG('cl1','#b7ee84','#6fb846')}${bactSVG('cl2','#b7ee84','#6fb846')}
  ${guardSVG('gd')}${wbcSVG('wb')}${bactSVG('bc')}<g id="shield" opacity="0"><ellipse rx="150" ry="112" fill="#9be86a" opacity=".25" stroke="#5fae3a" stroke-width="6"/><path d="M-90,-60 C-50,-96 40,-98 80,-70" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".7"/></g>
  ${abSVG('ab')}${abSVG('ab2')}<g id="drops"></g><g id="dust"></g><g id="stars"></g></g></g>
 ${labelBox('lbSkin','SKIN',120,90,26)}${labelBox('lbCut','CUT',470,330,24)}${labelBox('lbBac','BACTERIA',560,600,24)}${labelBox('lbWbc','WHITE BLOOD CELL',520,560,22)}${labelBox('lbAb2','ANTIBIOTIC',540,520,22)}
</g>`;
// ---------- SCENE 3: the hospital ----------
let S3=`<g id="s3"><g id="ccam">${IMG('plate_hospital.jpg')}${actorSVG('pat')}${actorSVG('doc')}
 <g id="bandage"><rect x="-26" y="-10" width="52" height="20" rx="6" fill="#fff" ${STK2}/><path d="M-14,-10 L-14,10 M0,-10 L0,10 M14,-10 L14,10" stroke="#d9cfc9" stroke-width="2"/><circle cx="0" cy="0" r="5" fill="#e0392f" opacity=".6"/></g>
 <g id="bub" opacity="0"><g transform="translate(360,250)"><ellipse rx="300" ry="196" fill="#fff" ${LN}/><clipPath id="bubClip"><ellipse rx="290" ry="186"/></clipPath>
   <g clip-path="url(#bubClip)"><use id="bubA" href="#wStomach" transform="scale(.62) translate(-345,-790)"/><use id="bubB" href="#wSkin" transform="scale(.62) translate(-370,-760)"/></g>
   <ellipse rx="300" ry="196" fill="none" ${LN}/></g></g></g>
 ${labelBox('lbRes','ANTIBIOTIC RESISTANCE',360,74,30)}
 <g id="lbTip" opacity="0" transform="translate(360,124)"><rect x="-322" y="-66" width="644" height="132" rx="14" fill="#fff" ${LN}/>
  <circle cx="-282" cy="-22" r="22" fill="#2fa36b" ${LN2}/><path d="M-293,-22 l8,8 l15,-16" fill="none" stroke="#fff" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
  <text class="lbl" style="font-size:26px" x="26" y="-12" text-anchor="middle">ANTIBIOTICS ONLY WHEN PRESCRIBED</text><text class="lbl" style="font-size:28px" x="0" y="40" text-anchor="middle" fill="#e0454f">TAKE THEM EXACTLY AS TOLD</text></g>
</g>`;
let CTA=`<g id="cta" opacity="0"><g id="cta_i"><rect x="-250" y="-62" width="500" height="132" rx="26" fill="#fff" ${LN}/>
  <text class="cta" text-anchor="middle" y="6" style="font-size:66px;stroke-width:9px" fill="#ffd21f">FOLLOW</text>
  <text class="cta" text-anchor="middle" y="52" style="font-size:30px;stroke-width:6px" fill="#fff">FOR MORE BODY SECRETS</text></g></g>`;
// =============== assemble ===============
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="9"/></filter>${DEFS}${GDEF}</defs>`
 +S1+S2+S3+CTA+`<rect id="indark" width="720" height="1280" fill="#1e1012" opacity="0"/><g id="capg"><text id="cap" class="cap" x="360" y="1110" text-anchor="middle"></text></g>`;
// gold helmet for the stronger antibiotic (stinger)
document.querySelectorAll('#ab2 path').forEach(p=>{const f=p.getAttribute('fill')||'';if(f.includes('ab2g3'))p.setAttribute('fill','#f2c233');});
// =============== timing ===============
const T_SKIN=E.skin, T_ST2=E.stom2, T_SKIN2=E.skin2, T_CLIN=E.clinic, T_STING=E.sting;
function renderStomach(T,second){
  const [sp,s0]=poseAt(T,[[ST['02_stomach']-.1,ST['03_stomach']-.1,'stomach_point'],[ST['03_stomach']-.1,ST['04_buddy'],'stomach_shout'],[ST['05_stomach']-.1,ST['06_buddy'],'stomach_point'],
     [ST['07_stomach']-.1,T_SKIN,'stomach_smug'],[ST['20_stomach']-.3,1e9,'stomach_panic']],'stomach_base');
  const se=speak('stomach',T), pk=popK(T,s0);
  placeActor('sto',sp,STO[0],STO[1],STO[2],{sy:1+Math.sin(T*3)*.01+se*.02-pk*.04,sx:1+pk*.05,rot:sp==='stomach_shout'?Math.sin(T*24)*.8:0,env:se,T,seed:3});
  const be=speak('buddy',T); placeActor('bud','buddy_base',BUD[0],BUD[1],BUD[2],{sy:1+Math.sin(T*2.4)*.02+be*.03,env:be,T,seed:9});
  // capsules: 2 at the start, 1 more at drop2; they slide down the food pipe and land in the juice, then fizz
  const drops=[[E.drop,0],[E.drop+.18,1],[E.drop2,2]];
  drops.forEach(([t0,i])=>{const el=$('cp'+i),k=(T-t0)/.75; if(k<0||(i===2&&T<E.stom2-.1)){el.setAttribute('opacity',0);return;}
    el.setAttribute('opacity',1); const p=k<1?along(PIPE,k):[352+(i-1)*44,912+Math.sin(T*2+i)*4];
    el.setAttribute('transform',`translate(${p[0].toFixed(1)},${p[1].toFixed(1)}) rotate(${(k<1?k*400:70+i*30+Math.sin(T*2+i)*6).toFixed(1)}) scale(.85)`);});
  const bk=clamp(P(T,E.burn-.2,E.burn+.4))*(1-P(T,T_SKIN-.4,T_SKIN)); show('burnGlow',bk*(.4+.15*Math.sin(T*8)));
  let st='';if(bk>0||(T>E.drop+1&&T<T_SKIN))for(let i=0;i<4;i++){const u=((T*.7)+i/4)%1;st+=`<path d="M${(300+i*40).toFixed(0)},${(890-u*110).toFixed(1)} q10,-14 0,-28 q-10,-14 0,-28" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity="${((.25+bk*.6)*Math.sin(u*Math.PI)).toFixed(2)}"/>`;}
  $('steam1').innerHTML=st;
}
function renderSkin(T){
  const stinger=T>=T_STING, sk2=T>=T_SKIN2;
  // the bacterium: slips down through the cut, argues, shoves, fights, multiplies; shield later
  const bTalk=speak('bacteria',T);
  let bx=510,by=760,bs=1.05,brot=0,barms='hips',bsmug=.6,bmood=.5;
  const sn=P(T,E.sneak,E.stop-.1); if(T<E.stop){const p=along([[355,200],[360,380],[420,560],[510,760]],eio(sn));bx=p[0];by=p[1];brot=lerp(-30,0,sn);bs=lerp(.5,1.05,sn);}
  if(T>=E.shove-.3&&T<E.radio){const k=eob(P(T,E.shove-.3,E.shove+.1));bx=lerp(510,360,k);barms='push';}
  if(T>=E.radio){bx=370;by=765;bs=1.0;}
  if(T>=E.fight-.1&&T<E.clones){bx=440+Math.sin(T*30)*12;}
  if(sk2){bx=330;by=770;bs=1.0;}
  if(stinger){bx=280;by=780;bs=1.0;bsmug=0;bmood=-1;barms='up';brot=Math.sin(T*30)*2;}
  const inFight=T>=E.fight&&T<E.clones-.1;
  show('bc',inFight?0:1);
  setBact('bc',bx,by+Math.sin(T*2.2)*6,bs,{talk:bTalk,T,smug:bsmug,mood:bmood,rot:brot,arms:barms,look:stinger?1:(T<E.radio?-1:1),seed:0});
  // clones appear after the fight
  const ck=eob(P(T,E.clones,E.clones+.35)); show('cl1',T>=E.clones?1:0); show('cl2',T>=E.clones+.15?1:0);
  if(T>=E.clones){setBact('cl1',sk2?170:230,(sk2?630:660)+Math.sin(T*2.6)*8,.64*ck,{T,smug:stinger?0:.7,mood:stinger?-1:.6,seed:2,look:stinger?1:-1,arms:stinger?'up':'hips'});
    setBact('cl2',sk2?490:560,(sk2?600:620)+Math.sin(T*2.3+1)*8,.58*eob(P(T,E.clones+.15,E.clones+.5)),{T,smug:stinger?0:.7,mood:stinger?-1:.6,seed:4,look:stinger?1:-1,arms:stinger?'up':'hips'});}
  // the guard
  const gTalk=speak('guard',T), gOn=!sk2; show('gd',gOn?1:0);
  if(gOn){let gx=200,gy=710,gs=1.08,pose='stop',grot=0,gmood=-.6,brows=1;
    if(T>=E.shove){const k=eio(P(T,E.shove,E.shove+.35)),up=eio(P(T,E.radio-.3,E.radio+.2));gx=lerp(200,150,k)-up*40;gy=lerp(710,830,k)-up*50;grot=lerp(0,-78,k)*(1-up);pose=up>.5?'phone':'fallen';gs=lerp(1.08,.85,up);}
    if(T>=E.radio){pose='phone';gx=110;gy=780;gs=.85;gmood=-1;brows=-1;}
    setGuard('gd',gx,gy+(pose==='stop'?Math.sin(T*2)*3:0),gs,{talk:gTalk,T,pose,rot:grot,look:1,mood:gmood,brows});}
  // the white blood cell rolls in, fights, gets knocked away
  const wOn=T>=E.wbc&&T<E.wbcGone+.6; show('wb',wOn?1:0);
  if(wOn){const rin=eio(P(T,E.wbc,E.wbc+.7)); let wx=lerp(860,600,rin),wy=755,wr=(1-rin)*-360,ws=.98;
    if(T>=E.wbcGone){const k=P(T,E.wbcGone,E.wbcGone+.6);wx=600+k*260;wy=755-k*500;wr=k*720;ws=.98*(1-k*.5);}
    setWbc('wb',wx,wy+Math.sin(T*3)*5,ws,{talk:speak('wbc',T),T,rot:wr,look:-1,angry:1,punch:T>=ST['17_wbc']?Math.abs(Math.sin(T*10)):0});}
  // the fight dust cloud
  const fk=P(T,E.fight,E.clones); if(fk>0&&fk<1){let h='';for(let i=0;i<12;i++){const a=i/12*6.283+T*3,r=90+Math.sin(T*9+i)*20;
      h+=`<circle cx="${(500+Math.cos(a)*r).toFixed(1)}" cy="${(730+Math.sin(a)*r*.7).toFixed(1)}" r="${(60+rnd(i)*30+Math.sin(T*12+i)*8).toFixed(1)}" fill="#fff" stroke="${OL}" stroke-width="4"/>`;}
    h+=`<circle cx="500" cy="730" r="110" fill="#fff"/>`; $('dust').innerHTML=h;
    let s='';for(let i=0;i<5;i++){const k=((T*2.2)+i/5)%1;s+=`<path transform="translate(${(500+Math.cos(i*1.3)*k*200).toFixed(1)},${(700+Math.sin(i*1.9)*k*160).toFixed(1)}) scale(${(.6+k).toFixed(2)})" d="M0,-16 L5,-5 L16,-5 L7,2 L10,14 L0,7 L-10,14 L-7,2 L-16,-5 L-5,-5Z" fill="#ffd21f" stroke="${OL}" stroke-width="2.5" opacity="${(1-k).toFixed(2)}"/>`;}
    $('stars').innerHTML=s;} else {$('dust').innerHTML='';$('stars').innerHTML='';}
  // the antibiotic soldier: marches in, pokes, the spear bounces off a shield
  const aOn=sk2&&!stinger; show('ab',aOn?1:0);
  if(aOn){const k=eio(P(T,E.ab,E.ab+1.0)); let ax=lerp(860,590,k),ay=735+Math.abs(Math.sin(T*8))*(k<1?10:0),poke=0,shock=0,arot=0;
    if(T>=E.poke-.1){poke=Math.sin(clamp(P(T,E.poke-.1,E.poke+.25))*Math.PI);}
    if(T>=E.bounce){const b=P(T,E.bounce,E.bounce+.5);ax+=Math.sin(b*Math.PI)*60;arot=Math.sin(b*Math.PI)*12;shock=1;}
    setAb('ab',ax,ay,.98,{talk:speak('antibiotic',T),T,poke,shock,rot:arot,look:-1});}
  const shK=T>=E.bounce-.15&&T<T_CLIN?eob(P(T,E.bounce-.15,E.bounce+.15)):0; show('shield',shK>0?Math.min(1,shK)*(.75+.25*Math.sin(T*6)):0);
  if(shK>0) $('shield').setAttribute('transform',`translate(330,770) scale(${(1.0*shK).toFixed(3)})`);
  // stinger: a bigger antibiotic with a gold helmet slides in
  const a2=stinger; show('ab2',a2?1:0); if(a2){const k=eob(P(T,E.big,E.big+.8));setAb('ab2',lerp(900,560,k),690,1.3,{T,look:-1,mood:.6,poke:0});}
  let dr='';for(let i=0;i<3;i++){const u=((T*.45)+i/3)%1;dr+=`<path d="M${(352+i*4).toFixed(0)},${(430+u*300).toFixed(1)} c7,9 9,17 0,21 c-9,-4 -7,-12 0,-21z" fill="#c4232c" stroke="${OL}" stroke-width="2.5" opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;}$('drops').innerHTML=dr;
  // labels
  popLabel('lbSkin',T,T_SKIN+.2,T_SKIN+2.4,120,90); popLabel('lbCut',T,T_SKIN+.4,T_SKIN+2.4,470,330);
  popLabel('lbBac',T,ST['10_bacteria']-.1,ST['10_bacteria']+2.2,560,600); popLabel('lbWbc',T,E.wbc+.5,E.wbc+2.8,520,560);
  popLabel('lbAb2',T,E.ab+.6,E.ab+2.8,560,520);
}
function renderClinic(T){
  const dT=speak('doctor',T), pT=speak('patient',T), d0=ST['25_doctor'], p0=ST['24_patient'];
  const dpose=T>=E.stronger-.2?'doc_point':(T>=E.misused-.15?'doc_explain':'doc_base');
  placeActor('pat','pat_bed',474,1250,770,{sy:1+Math.sin(T*1.4)*.006+pT*.01,rot:T<d0&&pT>.2?Math.sin(T*7)*.4:0,env:pT,T,seed:6});
  placeActor('doc',dpose,168,1236,740,{rot:dT>.15?Math.sin(T*6.5)*.6*dT:0,sy:1+Math.sin(T*1.3)*.006+dT*.012,env:dT,T,seed:5});
  $('bandage').setAttribute('transform',`translate(468,${(790+Math.sin(T*1.4)*1.5).toFixed(1)}) rotate(-24) scale(.72)`);
  const pq=eio(P(T,p0,p0+1.5))*(1-eio(P(T,d0-.2,d0+.4)));
  let z=1+.035*P(T,d0,T_STING)+.08*pq, cx=lerp(360,470,pq), cy=lerp(640,600,pq);
  const pk=eio(P(T,E.resist-.15,E.resist+.15))*(1-eio(P(T,E.misused-.45,E.misused-.1)));
  z=lerp(z,1.45,pk); cx=lerp(cx,215,pk); cy=lerp(cy,640,pk);
  const ty=lerp(640,600,pk); cx=clamp(cx,360/z,720-360/z); cy=clamp(cy,ty/z,1280-(1280-ty)/z);
  $('ccam').setAttribute('transform',`translate(360,${ty}) scale(${z}) translate(${-cx},${-cy})`);
  // bubble replays cut on the doctor's words: misused -> the capsules for a headache; adapt -> the shield
  const sA=E.misused-.15, sB=E.adapt-.15, sE=E.stronger-.25, bOn=T>=sA&&T<sE;
  $('bub').setAttribute('opacity',bOn?1:0);
  if(bOn){const seg=T<sB?0:1, t0=[sA,sB][seg], t1=[sB,sE][seg], u=P(T,t0,t1);
    const pop=seg===0?eob(P(T,sA,sA+.3)):1+.06*Math.sin(clamp(P(T,t0,t0+.25))*Math.PI);
    $('bub').setAttribute('transform',`translate(360,250) scale(${pop.toFixed(3)}) translate(-360,-250)`);
    show('bubA',seg===0?1:0); show('bubB',seg===1?1:0);
    if(seg===0) renderStomach(lerp(E.drop,ST['03_stomach']+1.5,u)); else renderSkin(lerp(E.poke-.3,ST['23_bacteria'],u));}
  popLabel('lbRes',T,E.resist-.05,E.misused-.2,360,74);
  popLabel('lbTip',T,E.stronger-.1,T_STING,360,124);
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  const c=$('cap'),big=KEY.test(w.replace(/[^A-Z'\-]/g,'')); c.textContent=w; c.style.fontSize=big?'56px':'44px'; c.style.fill=big?'#ffd21f':'#fff';
  const k=eo(P(T,ws,ws+.09)); c.setAttribute('transform',`translate(360,1110) scale(${lerp(1.2,1,k)}) translate(-360,-1110)`);}
// skin-scene camera: punch in on whoever talks, go wide on the silent action beats; averaged over the last 0.6 s (deterministic per T)
function camTarget(t){
  const L=D.lines.find(l=>t>=l.t0-.15&&t<l.t0+l.dur+.25&&['guard','bacteria','wbc','antibiotic'].includes(l.who));
  if(!L) return [360,1.0];
  if(t>=T_STING) return [470,1.06];   // stinger: keep the big new antibiotic fully in frame
  const x=L.who==='guard'?(t<E.radio?200:120):L.who==='bacteria'?(t>=T_STING?280:t>=T_SKIN2?330:t>=E.radio?370:510):L.who==='wbc'?600:590;
  return [x,1.14];}
function skinCam(T){let sx=0,sz=0,n=0;for(let i=0;i<=12;i++){const [x,z]=camTarget(T-.6+i*.05);sx+=x;sz+=z;n++;}return [sx/n,sz/n];}
window.render=function(T){
  const sc=T<T_SKIN?1:T<T_ST2?2:T<T_SKIN2?1:T<T_CLIN?2:T<T_STING?3:2;
  ['s1','s2','s3'].forEach((id,i)=>$(id).setAttribute('display',sc===i+1?'inline':'none'));
  let dark=0;
  const bounds=[[0,T_SKIN],[T_SKIN,T_ST2],[T_ST2,T_SKIN2],[T_SKIN2,T_CLIN],[T_CLIN,T_STING],[T_STING,END]];
  const seg=bounds.find(([a,b])=>T>=a&&T<b)||bounds[5];
  dark=Math.max(seg[0]>0?1-P(T,seg[0],seg[0]+.16):0, seg[1]<END?P(T,seg[1]-.16,seg[1]):0);
  if(sc===1){renderStomach(T); const c=1.05+.02*Math.sin(T*.3); $('cam1').setAttribute('transform',`translate(360,640) scale(${c}) translate(-366,-660)`);
    popLabel('lbSto',T,1.6,3.4,560,300); popLabel('lbAb',T,E.drop+.9,E.drop+3.0,540,900);}
  if(sc===2){renderSkin(T); const shake=(Math.sin(clamp(P(T,E.shove,E.shove+.3))*Math.PI)+Math.sin(clamp(P(T,E.bounce,E.bounce+.3))*Math.PI)+(T>=E.fight&&T<E.clones?.5:0))*Math.sin(T*70)*7;
    const [tx,tz]=skinCam(T); const z=tz+.02*Math.sin(T*.25), cx=clamp(360+(tx-360)*.6,360/z,720-360/z), cy=clamp(lerp(640,700,(tz-1)/.14),640/z,1280-640/z);
    $('cam2').setAttribute('transform',`translate(${(360+shake).toFixed(1)},640) scale(${z.toFixed(4)}) translate(${(-cx).toFixed(1)},${(-cy).toFixed(1)})`);}
  if(sc===3) renderClinic(T);
  const ck=P(T,E.cta,E.cta+.35); show('cta',T>=E.cta?1:0); $('cta').setAttribute('transform',`translate(360,${250+Math.sin(T*3)*4}) rotate(${Math.sin(T*2.2)*2})`); $('cta_i').setAttribute('transform',`scale(${eob(ck)})`);
  show('indark',dark*.9);
  caption(T);
};
window.render(0);
