/* Local neural narration and audio-timed card progression. */
(()=>{
 'use strict';
 const $=id=>document.getElementById(id),bridge=globalThis.readerNarration;
 const play=$('narration-play'),stopButton=$('narration-stop'),replay=$('narration-replay'),voice=$('narration-voice'),speed=$('narration-speed'),auto=$('narration-auto'),status=$('narration-status');
 let state='idle',token=0,timer=null,worker=null,serial=0,loading=null,ready=false,context=null,gain=null,source=null,buffer=null,offset=0,startedAt=0,chain=Promise.resolve();
 const pending=new Map(),audioCache=new Map();
 try{const prefs=JSON.parse(localStorage.getItem('once-upon-narration-v1'));if(prefs){if(['af_heart','bm_fable'].includes(prefs.voice))voice.value=prefs.voice;if(['0.85','0.92','1','1.1'].includes(String(prefs.speed)))speed.value=prefs.speed;if(typeof prefs.auto==='boolean')auto.checked=prefs.auto;}}catch{}
 function save(){try{localStorage.setItem('once-upon-narration-v1',JSON.stringify({voice:voice.value,speed:speed.value,auto:auto.checked}));}catch{}}
 function update(message){
  if(message)status.textContent=message;
  const running=['loading','playing','gap'].includes(state);
  play.textContent=running?'Pause ❚❚':state==='paused'?'Resume ▶':'Listen ▶';
  play.setAttribute('aria-label',running?'Pause story narration':state==='paused'?'Resume story narration':'Listen to the story from this card');
  play.setAttribute('aria-pressed',String(running));
  stopButton.disabled=state==='idle'||state==='ended';replay.disabled=!bridge.getFrame();
 }
 function hush(){clearTimeout(timer);timer=null;if(source){source.onended=null;try{source.stop();}catch{}source.disconnect();source=null;}}
 function stop(message='Narration stopped. Listen starts from this card.'){token++;hush();offset=0;buffer=null;state='idle';update(message);}
 function pause(message='Paused. Resume when you’re ready.'){
  if(state==='playing'&&source)offset=Math.min(buffer.duration,offset+(context.currentTime-startedAt)*source.playbackRate.value);
  token++;hush();state='paused';update(message);
 }
 async function unlock(){
  if(!context){context=new (globalThis.AudioContext||globalThis.webkitAudioContext)();gain=context.createGain();gain.gain.value=0.8;gain.connect(context.destination);}
  await context.resume();
 }
 function call(type,data={}){const id=++serial;return new Promise((resolve,reject)=>{pending.set(id,{resolve,reject});worker.postMessage({id,type,...data});});}
 async function engine(){
  if(ready)return;
  if(!loading)loading=(async()=>{
   if(location.protocol==='file:')throw new Error('hosted');
   worker=new Worker('./narration-worker.js',{type:'module'});
   worker.addEventListener('message',event=>{
    const data=event.data;
    if(data.type==='progress'&&state==='loading')update(data.file?.endsWith('.onnx')?`Downloading the neural voice… ${Math.round(data.progress||0)}%. This happens once.`:'Preparing the neural voice…');
    if(data.type==='ready'){ready=true;return;}
    const job=pending.get(data.id);if(!job)return;pending.delete(data.id);
    if(data.type==='error')job.reject(new Error(data.message));else job.resolve(data);
   });
   worker.addEventListener('error',()=>{for(const job of pending.values())job.reject(new Error('runtime'));pending.clear();ready=false;loading=null;worker.terminate();worker=null;});
   await call('prepare');
  })().catch(error=>{loading=null;if(worker&&!ready){worker.terminate();worker=null;}throw error;});
  return loading;
 }
 const key=(frame,v,pace)=>`${frame.storyId}:${frame.key}:${v}:${pace}`;
 function pcm(frame,v){
  const pace=Number(speed.value),id=key(frame,v,pace);if(audioCache.has(id))return audioCache.get(id);
  const task=chain.catch(()=>{}).then(async()=>{
   const current=bridge.getFrame();
   if(!current||voice.value!==v||Number(speed.value)!==pace||frame.storyId!==current.storyId||![current.index,current.index+1].includes(frame.index))return null;
   await engine();return call('generate',{text:frame.text,voice:v,speed:pace});
  });
  chain=task;audioCache.set(id,task);while(audioCache.size>3)audioCache.delete(audioCache.keys().next().value);
  task.then(result=>{if(!result)audioCache.delete(id)},()=>audioCache.delete(id));return task;
 }
 function finish(t){
  if(t!==token||state!=='playing')return;source=null;offset=0;buffer=null;
  const frame=bridge.getFrame();
  if(auto.checked&&frame&&frame.index<frame.total-1){state='gap';update('A little breath, then the next card…');timer=setTimeout(()=>{if(t===token&&state==='gap')bridge.advance();},950);}
  else{state='ended';update(frame?.index===frame?.total-1?'The story has finished. Try the recall when you’re ready.':'Card finished. Swipe onward, or listen again.');}
 }
 function sound(t){
  if(t!==token||!buffer)return;
  source=context.createBufferSource();source.buffer=buffer;
  source.connect(gain);startedAt=context.currentTime;source.onended=()=>finish(t);state='playing';source.start(0,offset);
  update(`Listening · card ${bridge.getFrame().index+1} of ${bridge.getFrame().total}`);
  const next=bridge.nextFrame();if(next&&auto.checked)pcm(next,voice.value).catch(()=>{});
 }
 async function listen(resume=false){
  const frame=bridge.getFrame();if(!frame)return;
  const t=++token;hush();if(!resume){offset=0;buffer=null;}
  state='loading';update(ready?'Preparing this card’s narration…':'Preparing the neural voice… First use downloads about 115 MB.');
  try{
   await unlock();
   if(!buffer){const audio=await pcm(frame,voice.value);if(t!==token||!audio)return;buffer=context.createBuffer(1,audio.samples.length,audio.sampleRate);buffer.copyToChannel(audio.samples,0);}
   if(t!==token)return;sound(t);
  }catch(error){if(t!==token)return;state='idle';offset=0;buffer=null;update(error.message==='hosted'?'Open the hosted library to use local neural narration.':'The voice could not be prepared. Reconnect and try Listen again.');$('narration-hosted').hidden=error.message!=='hosted';$('narration-hosted').href=`https://ascendesshady.github.io/English-Literature/#story/${frame.storyId}/${frame.index+1}`;}
 }
 play.addEventListener('click',()=>{if(['loading','playing','gap'].includes(state)){pause();return;}bridge.showStory();listen(state==='paused');});
 stopButton.addEventListener('click',()=>stop());replay.addEventListener('click',()=>{bridge.showStory();listen(false);});
 voice.addEventListener('change',()=>{save();audioCache.clear();stop('Voice changed. Press Listen when you’re ready.');});
 speed.addEventListener('change',()=>{save();audioCache.clear();stop('Pace changed. Listen restarts this card with the new pace.');});
 auto.addEventListener('change',()=>{save();if(!auto.checked&&state==='gap'){hush();state='ended';update('Auto turn is off. Swipe to choose your next card.');}});
 document.addEventListener('visibilitychange',()=>{if(document.hidden&&['playing','loading','gap'].includes(state))pause('Paused while the library is in the background.');});
 window.addEventListener('pagehide',()=>stop());
 globalThis.StoryNarrator={stop,changed(){const keepGoing=['playing','loading','gap'].includes(state);token++;hush();offset=0;buffer=null;if(keepGoing)listen();else{state='idle';update('Listen from this card, or swipe to choose a starting point.');}},tabChanged(tab){if(tab!=='story'&&['playing','loading','gap'].includes(state))pause('Paused while you explore this section.');}};
 $('narration-hosted').href='https://ascendesshady.github.io/English-Literature/'+location.hash;
 if(!globalThis.Worker||!(globalThis.AudioContext||globalThis.webkitAudioContext)){play.disabled=true;replay.disabled=true;status.textContent='Neural narration is unavailable in this browser. Open the library in Chrome.';}else update('A gentle voice, one card at a time.');
})();
