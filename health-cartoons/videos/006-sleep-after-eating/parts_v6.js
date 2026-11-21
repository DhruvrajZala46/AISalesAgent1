// =============== 006: sleep right after eating - remake of the 26M reference, our AI art + our engine ===============
const A=window.ART, E=D.ev, ST=D.start, END=D.end;
const KEY=/^(FOOD|MORE|FULL|ROOM|BED|BRAIN|NO|MEAL|SLEEPS|EATING|TOMORROW|EXHAUSTED|DIGEST|TIRED|HABIT|NIGHT|EASY|SURE|POSITIVE|SMELL|HYDROGEN|SULFIDE|ROTTEN|EGG|EGGS|LESSON|BURP|BURPING|YAAAWN)$/;
//__VISEME__
function actorSVG(id){return `<g id="${id}"><image id="${id}_img" preserveAspectRatio="none"/><g id="${id}_mg">${mouthEl(id+'_m',0,0)}</g></g>`;}
const lastPose={};
function placeActor(id,pose,fx,fy,H,o={}){
  const m=A[pose], w=H*m.w/m.h, x0=-w/2, y0=-H; let file=pose; const V=m.variants||[];
  if(V.length){const env=o.env||0, f=Math.floor((o.T||0)*15)+(o.seed||0); let open=env>0.12; if(open&&env<0.45&&f%3===0) open=false; file=pose+'_'+(open&&V.includes('o')?'o':'c');}
  const im=$(id+'_img'); if(lastPose[id]!==file){im.setAttribute('href','art/'+file+'.png');lastPose[id]=file;}
  im.setAttribute('x',x0.toFixed(1)); im.setAttribute('y',y0.toFixed(1)); im.setAttribute('width',w.toFixed(1)); im.setAttribute('height',H.toFixed(1));
  $(id).setAttribute('transform',`translate(${fx.toFixed(1)},${fy.toFixed(1)}) rotate(${(o.rot||0).toFixed(2)}) scale(${(o.sx||1).toFixed(4)},${(o.sy||1).toFixed(4)})`);
  $(id+'_mg').setAttribute('opacity',0);
}
function poseAt(T,segs,def){let p=def,t0=0;for(const [a,b,q] of segs) if(T>=a&&T<b){p=q;t0=a;} return [p,t0];}
function popK(T,t0){const k=P(T,t0,t0+.18);return k<1?Math.sin(k*Math.PI):0;}
function along(pts,s){s=clamp(s)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;return [lerp(pts[i][0],pts[i+1][0],f),lerp(pts[i][1],pts[i+1][1],f)];}
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
const IMG=(f)=>`<image href="art/${f}" x="-5.5" y="0" width="731" height="1280" preserveAspectRatio="none"/>`;
const SPR=(id)=>`<image id="${id}" preserveAspectRatio="none"/>`;
function placeImg(id,f,cx,by,H,o={}){const m=A[f],w=H*m.w/m.h,el=$(id);if(el.dataset.f!==f){el.setAttribute('href','art/'+f+'.png');el.dataset.f=f;}
  el.setAttribute('x',(-w/2).toFixed(1));el.setAttribute('y',(-H).toFixed(1));el.setAttribute('width',w.toFixed(1));el.setAttribute('height',H.toFixed(1));
  el.setAttribute('transform',`translate(${cx.toFixed(1)},${by.toFixed(1)}) rotate(${(o.rot||0).toFixed(1)}) scale(${(o.s||1).toFixed(3)})`);el.setAttribute('opacity',o.op===undefined?1:o.op);}
function gasPuffs(n,cx,cy,rx,ry,T,k,seed){let h='';for(let i=0;i<n;i++){const a=rnd(i+seed)*6.283,r=Math.sqrt(rnd(i+seed+50)),x=cx+Math.cos(a)*rx*r+Math.sin(T*.8+i)*12,y=cy+Math.sin(a)*ry*r+Math.cos(T*.7+i)*10;
  h+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${(38+rnd(i+seed+9)*46).toFixed(1)}" fill="#8fb84a" opacity="${(.22*k).toFixed(3)}"/>`;}return h;}
// ---------- geometry ----------
const STO=[382,1052,690], HEAP=[355,948,140], BUD=[138,1012,165];
const PIPE=[[180,350],[184,385],[218,436],[251,498],[262,600],[262,741],[280,793],[313,850],[352,900]];
const FOODS=['food_burger','food_drum','food_egg','food_fries'];
// ---------- SCENE 1: the stomach ----------
let S1=`<g id="s1"><g id="cam1"><g id="wStomach">${IMG('plate_abdomen.jpg')}
  ${actorSVG('sto')}${SPR('heap')}<g id="items">${Array.from({length:8},(_,i)=>SPR('it'+i)).join('')}</g>
  ${actorSVG('bud')}<g id="zzz1"></g><g id="gas1" filter="url(#soft)"></g></g></g>
 <rect id="night1" width="720" height="1280" fill="#142050" opacity="0"/>
 ${labelBox('lbSto','STOMACH',560,300,24)}${labelBox('lbBud','SMALL INTESTINE',170,815,22)}${labelBox('lbGas','HYDROGEN SULFIDE GAS',360,150,26)}
</g>`;
// ---------- SCENE 2: the brain on its brain stem ----------
let S2=`<g id="s2"><g id="cam2"><g id="wBrain"><defs><radialGradient id="bgB" cx="50%" cy="45%" r="70%"><stop offset="0" stop-color="#fbe1da"/><stop offset=".55" stop-color="#e9a59b"/><stop offset="1" stop-color="#b85f5a"/></radialGradient></defs>
  <rect width="720" height="1280" fill="url(#bgB)"/>
  <path d="M282,700 C300,900 282,1100 270,1300 L450,1300 C438,1100 420,900 438,700 Z" fill="#c95b5f" stroke="#4a2a24" stroke-width="5"/>
  <path d="M318,760 C330,940 316,1120 306,1300" fill="none" stroke="#e48789" stroke-width="12" stroke-linecap="round" opacity=".8"/><path d="M402,760 C396,940 408,1120 414,1300" fill="none" stroke="#a9474c" stroke-width="8" stroke-linecap="round" opacity=".6"/>
  ${actorSVG('brn')}<g id="zzz2"></g></g></g>
 <g id="waves" opacity="0"></g>
 <g id="sInset" opacity="0"><circle r="122" fill="none" ${LN}/><circle r="117" fill="#fff"/><clipPath id="sClip"><circle r="110"/></clipPath>
  <g clip-path="url(#sClip)"><circle r="110" fill="#f6d5cf"/>${actorSVG('sto2')}</g><circle r="110" fill="none" ${LN2}/></g>
 ${labelBox('lbBrain','BRAIN',360,170,26)}
</g>`;
// ---------- black card ----------
let CARD=`<g id="card" opacity="0"><rect width="720" height="1280" fill="#0b0b10"/>
 <text class="cta" x="360" y="640" text-anchor="middle" style="font-size:58px;stroke-width:8px" fill="#fff">A FEW HOURS LATER...</text>
 <g id="clk" transform="translate(360,500)"><circle r="54" fill="#fff" stroke="#888" stroke-width="5"/><path id="clkH" d="M0,0 L0,-30" stroke="#222" stroke-width="7" stroke-linecap="round"/><path id="clkM" d="M0,0 L0,-44" stroke="#e0454f" stroke-width="5" stroke-linecap="round"/></g></g>`;
// ---------- SCENE 3: the bedroom ----------
let S3=`<g id="s3"><g id="cam3"><g id="wBed">${IMG('plate_bedroom.jpg')}${actorSVG('man')}<g id="burps" filter="url(#soft)"></g><g id="stink"></g></g></g>
 <g id="lbTip" opacity="0" transform="translate(360,130)"><rect x="-300" y="-64" width="600" height="128" rx="14" fill="#fff" ${LN}/>
  <circle cx="-258" cy="-22" r="24" fill="#2fa36b" ${LN2}/><path d="M-270,-22 l8,8 l16,-17" fill="none" stroke="#fff" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
  <text class="lbl" style="font-size:34px" x="24" y="-8" text-anchor="middle">WAIT 3 HOURS AFTER EATING</text><text class="lbl" style="font-size:30px" x="0" y="40" text-anchor="middle" fill="#e0454f">BEFORE YOU LIE DOWN</text></g>
 <g id="cta" opacity="0"><g id="cta_i"><rect x="-250" y="-62" width="500" height="132" rx="26" fill="#fff" ${LN}/>
  <text class="cta" text-anchor="middle" y="6" style="font-size:66px;stroke-width:9px" fill="#ffd21f">FOLLOW</text>
  <text class="cta" text-anchor="middle" y="52" style="font-size:30px;stroke-width:6px" fill="#fff">FOR MORE BODY SECRETS</text></g></g>
</g>`;
// =============== assemble ===============
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="9"/></filter>${DEFS}</defs>`
 +S1+S2+S3+CARD+`<rect id="indark" width="720" height="1280" fill="#1e1012" opacity="0"/><g id="capg"><text id="cap" class="cap" x="360" y="1110" text-anchor="middle"></text></g>`;
// =============== timing ===============
const T_BRAIN=E.brain, T_BACK=E.back, T_CARD=E.card, T_GAS=E.card+1.7, T_BED=E.bed;
const ITEM=[...Array(8)].map((_,i)=>({f:FOODS[i%4],t0:E.drop+i*.07,dur:.5+rnd(i)*.12,x:300+rnd(i+20)*110,y:905+rnd(i+40)*24,h:60+rnd(i+60)*20,r:rnd(i+80)*360}));
function zzz(id,x,y,T,on){let h='';if(on)for(let i=0;i<3;i++){const u=((T*.5)+i/3)%1;h+=`<text class="cap" x="${(x+u*40+i*6).toFixed(1)}" y="${(y-u*90).toFixed(1)}" style="font-size:${(26+u*20).toFixed(0)}px" opacity="${Math.sin(u*Math.PI).toFixed(2)}">Z</text>`;}$(id).innerHTML=h;}
function renderStomach(T){
  const asleep=T>=E.masks&&T<E.wake, s12=ST['12_stomach'], s16=ST['16_stomach'], s21=ST['21_stomach'];
  const [sp,s0]=poseAt(T,[[E.drop+.35,ST['05_stomach']-.1,'stomach_panic'],[ST['05_stomach']-.1,T_BRAIN,'stomach_fork'],
     [T_BACK,s16-.1,'stomach_point'],[s16-.1,E.masks,'stomach_smug'],[E.masks,E.wake+.3,'stomach_asleep'],[E.wake+.3,1e9,'stomach_sniff']],'stomach_fork');
  const se=speak('stomach',T), pk=popK(T,s0), chew=sp==='stomach_fork'&&T<E.drop?Math.abs(Math.sin(T*5))*.02:0;
  const breathe=sp==='stomach_asleep'?Math.sin(T*2.2)*.025:Math.sin(T*3)*.01, land=Math.sin(clamp(P(T,E.drop+.5,E.drop+.9))*Math.PI);
  placeActor('sto',sp,STO[0],STO[1],STO[2],{sy:1+breathe+se*.02-pk*.04-land*.04-chew,sx:1+pk*.05+land*.03+chew*.5,rot:sp==='stomach_panic'?Math.sin(T*26)*.8:0,env:se,T,seed:3});
  // food: a heap from the start, more food drops down the pipe at E.drop
  let landed=0; ITEM.forEach((it,i)=>{const k=(T-it.t0)/it.dur; if(k<=0||k>=1.25){$('it'+i).setAttribute('opacity',0); if(k>=1) landed++; return;} if(k>=1) landed++;
    const p=k<1?along(PIPE,k):[it.x,it.y]; placeImg('it'+i,it.f,k<1?p[0]:it.x,(k<1?p[1]:it.y)+it.h*.5,it.h,{rot:it.r+k*300,op:k<1?1:1-(k-1)/.25});});
  placeImg('heap','food_heap',HEAP[0],HEAP[1],HEAP[2],{s:.75+.25*eob(clamp(landed/8))+.02*Math.sin(T*2)});
  // the small-intestine buddy at the stomach's exit
  const bOn=T>=T_BACK-.2, be=speak('buddy',T), bp=T>=E.masks&&T<E.wake?'buddy_mask':(T>=E.wake&&T<ST['20_buddy']-.05?'buddy_sniff':(T>=lastEnd('20_buddy')&&T>=E.wake?'buddy_sniff':'buddy_base'));
  show('bud',bOn?1:0); if(bOn){const bpk=popK(T,T_BACK);placeActor('bud',bp,BUD[0],BUD[1],BUD[2],{sy:1+Math.sin(T*2.4)*.02+be*.03-bpk*.06,sx:1+bpk*.06,rot:bp==='buddy_mask'?Math.sin(T*1.5)*3:0,env:be,T,seed:9});}
  zzz('zzz1',470,420,T,asleep&&T>=E.masks+.4);
  // green gas fills the stomach while they sleep
  const gk=clamp(P(T,T_GAS,T_GAS+1.6))*(T>=T_GAS?1:0); $('gas1').innerHTML=gk>0?gasPuffs(26,400,720,260,330,T,gk,3):'';
  return asleep;
}
function lastEnd(id){const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;}
function renderBrain(T){
  const s07=ST['07_stomach'], s09=ST['09_brain'], be=speak('brain',T);
  const bp=T>=E.mask?'brain_mask':'brain_yawn', pk=popK(T,E.mask);
  placeActor('brn',bp,360,880,620,{sy:1+be*.025+Math.sin(T*2)*.015-pk*.05,sx:1+pk*.05,rot:bp==='brain_yawn'?Math.sin(T*1.2)*2:Math.sin(T*1.5)*2.5,env:be,T,seed:7});
  zzz('zzz2',520,330,T,T>=E.mask+.6);
  // the stomach shouts from below: an inset + yellow sound waves rising
  const iOn=T>=s07-.25&&T<s09-.1; show('sInset',iOn?1:0);
  if(iOn){const k=eob(P(T,s07-.25,s07+.05))*(1-eio(P(T,s09-.4,s09-.1)));$('sInset').setAttribute('transform',`translate(560,1010) scale(${k.toFixed(3)})`);
    const se=speak('stomach',T);placeActor('sto2','stomach_shout',0,150,300,{sy:1+se*.04,env:se,T,seed:3});}
  const wOn=T>=s07&&T<s09-.1; show('waves',wOn?1:0);
  if(wOn){let h='';for(let i=0;i<3;i++){const u=((T*1.6)+i/3)%1;h+=`<path d="M${(420).toFixed(1)},${(1080-u*230).toFixed(1)} q-60,-34 -120,0" fill="none" stroke="#ffd21f" stroke-width="${(12-u*5).toFixed(1)}" stroke-linecap="round" opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;}$('waves').innerHTML=h;}
}
function renderBed(T){
  const me=speak('man',T), b0=ST['23_man'];
  placeActor('man','man_bed',430,1270,880,{sy:1+Math.sin(T*1.4)*.006+me*.01,rot:me>.3?Math.sin(T*9)*.5:0,env:me,T,seed:6});
  // a green burp cloud on every *BURP*
  let h='';const L=D.lines.find(l=>l.id==='23_man');L.words.filter(w=>w[2]==='*BURP*').forEach((w,i)=>{const k=P(T,w[0],w[0]+1.4);if(k>0&&k<1)h+=`<ellipse cx="${(392+k*80+i*6).toFixed(1)}" cy="${(650-k*110).toFixed(1)}" rx="${(30+k*70).toFixed(1)}" ry="${(22+k*45).toFixed(1)}" fill="#8fb84a" opacity="${(.7*(1-k)).toFixed(2)}"/>`;});
  $('burps').innerHTML=h;
  let s='';if(T>=b0+.3)for(let i=0;i<3;i++){const u=((T*.7)+i/3)%1;s+=`<path d="M${(420+i*45).toFixed(1)},${(690-u*130).toFixed(1)} q12,-16 0,-32 q-12,-16 0,-32" fill="none" stroke="#7fa83a" stroke-width="6" stroke-linecap="round" opacity="${(.8*Math.sin(u*Math.PI)).toFixed(2)}"/>`;}
  $('stink').innerHTML=s;
  const z=1.02+.06*eio(P(T,T_BED,E.tip)); $('cam3').setAttribute('transform',`translate(360,640) scale(${z.toFixed(4)}) translate(-372,${-Math.min(700,1280-640/z).toFixed(1)})`);
  popLabel('lbTip',T,E.tip,END,360,130);
  const ck=P(T,E.cta,E.cta+.35); show('cta',T>=E.cta?1:0); $('cta').setAttribute('transform',`translate(360,${330+Math.sin(T*3)*4}) rotate(${Math.sin(T*2.2)*2})`); $('cta_i').setAttribute('transform',`scale(${eob(ck)})`);
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  const c=$('cap'),big=KEY.test(w.replace(/[^A-Z']/g,'')); c.textContent=w; c.style.fontSize=big?'56px':'44px'; c.style.fill=big?'#ffd21f':'#fff';
  const k=eo(P(T,ws,ws+.09)); c.setAttribute('transform',`translate(360,1110) scale(${lerp(1.2,1,k)}) translate(-360,-1110)`);}
window.render=function(T){
  const sc=T<T_BRAIN?1:T<T_BACK?2:T<T_BED?1:3;
  ['s1','s2','s3'].forEach((id,i)=>$(id).setAttribute('display',sc===i+1?'inline':'none'));
  let dark=0;
  if(sc===1){renderStomach(T); const c=1.05+.02*Math.sin(T*.3); $('cam1').setAttribute('transform',`translate(360,640) scale(${c}) translate(-366,-660)`);
    show('night1',.32*eio(P(T,E.masks,E.masks+.6))*(1-eio(P(T,E.wake-.2,E.wake+.4))));
    popLabel('lbSto',T,1.0,2.9,560,300); popLabel('lbBud',T,T_BACK+.2,T_BACK+2.6,170,815); popLabel('lbGas',T,E.hydrogen-.05,E.hydrogen+2.6,360,150);
    dark=T<T_BRAIN?P(T,T_BRAIN-.15,T_BRAIN):Math.max(1-P(T,T_BACK,T_BACK+.15),P(T,T_BED-.15,T_BED));}
  if(sc===2){renderBrain(T); popLabel('lbBrain',T,T_BRAIN+.3,T_BRAIN+2.4,360,170); $('cam2').setAttribute('transform',`translate(360,640) scale(${(1.0+.04*eio(P(T,T_BRAIN,T_BACK))).toFixed(4)}) translate(-360,-640)`);
    dark=Math.max(1-P(T,T_BRAIN,T_BRAIN+.15),P(T,T_BACK-.15,T_BACK));}
  if(sc===3){renderBed(T); dark=1-P(T,T_BED,T_BED+.15);}
  const cardOn=T>=T_CARD&&T<T_GAS; show('card',cardOn?1:0);
  if(cardOn){const u=P(T,T_CARD,T_GAS);$('clkH').setAttribute('transform',`rotate(${u*120})`);$('clkM').setAttribute('transform',`rotate(${u*1440})`);}
  show('indark',dark*.9);
  if(cardOn) $('cap').textContent=''; else caption(T);
};
window.render(0);
