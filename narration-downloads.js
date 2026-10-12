/* Resumable preparation of finished narration, without changing story progress. */
(()=>{
 'use strict';
 const $=id=>document.getElementById(id),dialog=$('audio-downloads'),scope=$('audio-scope'),voice=$('audio-voice'),pace=$('audio-pace'),versions=$('audio-versions'),start=$('audio-start'),pause=$('audio-pause'),status=$('audio-status'),bar=$('audio-progress'),count=$('audio-count');
 const voiceChoices=[...dialog.querySelectorAll('[name="audio-save-voice"]')],paceChoices=[...dialog.querySelectorAll('[name="audio-save-pace"]')];
 const voices=['af_heart','bm_fable'],paces=[0.85,0.92,1,1.1];
 let running=false,pausing=false,clearing=false,refreshId=0,selectedStory=null,lastSettings=null;
 const bytes=n=>n>=1e9?(n/1e9).toFixed(1)+' GB':(n/1e6).toFixed(1)+' MB';
 const frames=()=>STORIES.filter(story=>scope.value==='all'||story.id===selectedStory).flatMap(story=>story.scenes.map((frame,index)=>({storyId:story.id,title:story.title,key:frame.key,text:frame.text,index,total:story.scenes.length})));
 const combinations=()=>{
  if(versions.value==='selected')return [{voice:voice.value,pace:Number(pace.value)}];
  const chosenVoices=versions.value==='custom'?voiceChoices.filter(el=>el.checked).map(el=>el.value):voices;
  const chosenPaces=versions.value==='custom'?paceChoices.filter(el=>el.checked).map(el=>Number(el.value)):paces;
  const current=StoryNarrator.settings(),matrix=chosenVoices.flatMap(v=>chosenPaces.map(p=>({voice:v,pace:p})));
  return matrix.sort((a,b)=>Number(b.voice===current.voice&&b.pace===current.pace)-Number(a.voice===current.voice&&a.pace===current.pace));
 };
 async function inventory(items,variants){const result={ready:[],missing:[],bytes:0};for(const variant of variants){const saved=await NarrationStore.inventory(items,variant.voice,variant.pace);result.ready.push(...saved.ready.map(frame=>({...frame,...variant})));result.missing.push(...saved.missing.map(frame=>({...frame,...variant})));result.bytes+=saved.bytes;}
  const order=new Map(items.map((frame,index)=>[frame.storyId+'|'+frame.key,index]));
  result.missing.sort((a,b)=>order.get(a.storyId+'|'+a.key)-order.get(b.storyId+'|'+b.key));return result;
 }
 function controls(){const busy=running||clearing;start.disabled=busy||!NarrationStore.enabled||!frames().length||!combinations().length;pause.disabled=!running||pausing;$('audio-clear').disabled=$('audio-clear-cache').disabled=busy||!NarrationStore.enabled;$('audio-cache-restore').hidden=!globalThis.OfflineLibrary?.disabled();$('audio-cache-restore').disabled=busy||!NarrationStore.enabled;for(const el of [scope,versions,...voiceChoices,...paceChoices])el.disabled=busy;voice.disabled=pace.disabled=busy||versions.value!=='selected';$('audio-custom').hidden=versions.value!=='custom';for(const id of ['audio-single-voice','audio-single-pace'])$(id).hidden=versions.value!=='selected';}
 function progress(done,total,size){
  const percent=total?Math.floor(done/total*100):0;
  bar.max=total||1;bar.value=done;$('audio-percent').textContent=`${percent}%`;
  count.textContent=`${done.toLocaleString()} / ${total.toLocaleString()} recordings saved · ${bytes(size)}`;
  $('audio-top').textContent=running?`Saving audio · ${percent}%`:'Download audio ↓';
  $('audio-story').textContent=running?`Saving audio · ${percent}%`:'Download story ↓';
  $('audio-top').title=`${done.toLocaleString()} of ${total.toLocaleString()} selected recordings saved on this device`;
 }
 function prefs(){lastSettings={voice:voice.value,pace:pace.value,versions:versions.value,scope:scope.value,story:selectedStory,voices:voiceChoices.filter(el=>el.checked).map(el=>el.value),paces:paceChoices.filter(el=>el.checked).map(el=>el.value)};try{localStorage.setItem('once-upon-audio-downloads-v1',JSON.stringify(lastSettings));}catch{}}
 async function refresh(){
  if(running||clearing)return;const id=++refreshId,items=frames(),variants=combinations(),total=items.length*variants.length;controls();start.disabled=true;
  const words=items.reduce((sum,frame)=>sum+frame.text.trim().split(/\s+/).length,0),estimate=variants.reduce((sum,variant)=>sum+words*60/(150*variant.pace)*48000,0);
  $('audio-size').textContent=`Estimated audio storage: ${bytes(estimate)} for ${variants.length===1?'one voice and pace':`${variants.length} voice/pace combinations`}, plus the voice model. Saved inside this browser or installed app on this device.`;
  if(!variants.length){progress(0,0,0);status.textContent='Choose at least one voice and one pace.';start.textContent='Download audio';start.disabled=true;return;}
  if(!NarrationStore.enabled){status.textContent='Open the hosted library to save narration in your browser.';$('audio-open-hosted').hidden=false;progress(0,total,0);return;}
  bar.max=total||1;bar.removeAttribute('value');$('audio-percent').textContent='Checking…';count.textContent=`Checking ${total.toLocaleString()} recordings…`;status.textContent='Checking saved recordings…';
  try{const saved=await inventory(items,variants);if(id!==refreshId)return;progress(saved.ready.length,total,saved.bytes);start.textContent=saved.missing.length?(saved.ready.length?'Resume download':'Download audio'):'All selected narration is ready';controls();if(!saved.missing.length)start.disabled=true;status.textContent=saved.missing.length?'Completed recordings stay saved if you pause or close the app. Resume skips those recordings.':'Ready to listen offline with your selected voices and paces.';}
  catch{if(id!==refreshId)return;controls();status.textContent='Audio storage could not be opened. Try reopening the hosted library.';}
 }
 function open(kind='all'){
  if(!running){const current=readerNarration.getFrame();selectedStory=kind==='story'?current?.storyId||selectedStory:lastSettings?.story||current?.storyId||selectedStory;const option=scope.querySelector('[value="story"]');option.disabled=!selectedStory;option.textContent=selectedStory?`This story: ${STORIES.find(s=>s.id===selectedStory).title} (12 cards)`:'This story (open a story first)';scope.value=(kind==='story'||lastSettings?.scope==='story')&&selectedStory?'story':'all';const config=kind==='story'||!lastSettings?StoryNarrator.settings():lastSettings;voice.value=config.voice;pace.value=String(config.pace);versions.value=['all','selected','custom'].includes(lastSettings?.versions)?lastSettings.versions:'selected';for(const el of voiceChoices)el.checked=Array.isArray(lastSettings?.voices)?lastSettings.voices.includes(el.value):el.value===config.voice;for(const el of paceChoices)el.checked=Array.isArray(lastSettings?.paces)?lastSettings.paces.map(String).includes(el.value):el.value===String(config.pace);$('audio-model-setup').hidden=true;refresh();}
  if(!dialog.open)dialog.showModal();
 }
 async function download(){
  if(running||clearing)return;const items=frames(),variants=combinations(),total=items.length*variants.length;if(!total)return;running=true;pausing=false;refreshId++;controls();prefs();if(variants.length===1)StoryNarrator.useSettings(variants[0].voice,variants[0].pace);
  let saved,done=0,size=0;const timings=[];
  try{
   if(globalThis.OfflineLibrary?.disabled()){status.textContent='Saving the website for offline listening…';await OfflineLibrary.enable();}
   saved=await inventory(items,variants);done=saved.ready.length;size=saved.bytes;progress(done,total,size);
   navigator.storage?.persist?.().catch(()=>{});
   const estimate=await navigator.storage?.estimate?.().catch(()=>null);
   if(estimate?.quota&&estimate.quota-estimate.usage<48000*5&&saved.missing.length)throw new DOMException('Storage full','QuotaExceededError');
   for(const frame of saved.missing){
    if(pausing)break;
    status.textContent=`Preparing ${frame.title}, card ${frame.index+1} · ${frame.voice==='af_heart'?'American':'British'}, pace ${frame.pace}…`;
    const began=performance.now(),audio=await StoryNarrator.prepare(frame,frame.voice,frame.pace,()=>!pausing);
    if(!audio)break;
    $('audio-model-setup').hidden=true;done++;size+=audio.storedBytes||44+audio.samples.length*2;timings.push(performance.now()-began);if(timings.length>8)timings.shift();progress(done,total,size);
    if(timings.length>=3){const minutes=Math.ceil(timings.reduce((a,b)=>a+b,0)/timings.length*(total-done)/60000);status.textContent=`Saved ${frame.title}, card ${frame.index+1}. About ${minutes.toLocaleString()} minutes remaining at this device’s current speed.`;}
    // Allow input and playback requests to run before queuing the next card.
    await new Promise(resolve=>setTimeout(resolve,40));
   }
   status.textContent=done===total?'All selected narration is saved. Cards are ready for immediate offline listening.':'Paused. Finished recordings are saved; Resume picks up the rest.';
  }catch(error){status.textContent=error.name==='QuotaExceededError'?'Paused because browser storage is full. Finished cards are saved; free space or prepare fewer stories.':'Preparation stopped. Finished cards are saved. Reconnect if the voice model is still downloading, then Resume.';}
  finally{running=false;pausing=false;$('audio-model-setup').hidden=true;controls();start.textContent=done===total?'All selected narration is ready':'Resume download';if(done===total)start.disabled=true;progress(done,total,size);}
 }
 $('audio-top').addEventListener('click',()=>open());$('audio-install').addEventListener('click',()=>open());$('audio-story').addEventListener('click',()=>open('story'));
 $('audio-close').addEventListener('click',()=>dialog.close());start.addEventListener('click',download);
 pause.addEventListener('click',()=>{pausing=true;controls();status.textContent='Pausing after the current card is saved…';});
 $('audio-clear').addEventListener('click',async()=>{if(running||clearing||!confirm('Remove all downloaded card narration? Your saved shelf, reading progress and voice model will remain.'))return;clearing=true;controls();try{await StoryNarrator.releaseDownloads();await NarrationStore.clear();clearing=false;await refresh();}catch{status.textContent='Saved audio could not be cleared. Try again.';}finally{clearing=false;controls();}});
 $('audio-clear-cache').addEventListener('click',async()=>{if(running||clearing||!confirm('Clear this app’s offline website, audio recordings and voice downloads from this device? Your saved shelf and reading progress will be kept.'))return;clearing=true;refreshId++;controls();status.textContent='Clearing offline files from this device…';try{await OfflineLibrary.clearDeviceCache();clearing=false;await refresh();status.textContent='Device cache cleared. Your shelf and reading progress are kept. Save the website offline or download audio again whenever you want.';}catch{status.textContent='Some offline files could not be cleared. Try again.';}finally{clearing=false;controls();}});
 $('audio-cache-restore').addEventListener('click',async()=>{if(running||clearing)return;clearing=true;controls();status.textContent='Saving the website for offline reading…';try{await OfflineLibrary.enable();clearing=false;await refresh();status.textContent='The website is saved offline. Choose Download audio to prepare your selected voices and paces.';}catch{status.textContent='Offline saving could not finish. Reconnect and try again.';}finally{clearing=false;controls();}});
 globalThis.addEventListener('offline-downloads-changed',()=>{controls();if(dialog.open&&!running&&!clearing)refresh();});
 globalThis.addEventListener('storage',event=>{if(event.key==='once-upon-offline-disabled:'+new URL('./',location.href).href&&event.newValue==='1'){pausing=true;controls();}});
 for(const el of [scope,voice,pace,versions,...voiceChoices,...paceChoices])el.addEventListener('change',()=>{prefs();refresh();});
 globalThis.addEventListener('narration-model-progress',event=>{if(running&&!pausing){const percent=Math.max(0,Math.min(100,Math.round(event.detail.progress||0)));$('audio-model-setup').hidden=false;$('audio-model-progress').value=percent;$('audio-model-percent').textContent=`${percent}%`;status.textContent='Downloading the voice setup. Your audio collection will be saved next.';}});
 try{const p=JSON.parse(localStorage.getItem('once-upon-audio-downloads-v1'));if(p&&['af_heart','bm_fable'].includes(p.voice)&&['0.85','0.92','1','1.1'].includes(String(p.pace))){lastSettings=p;if(STORIES.some(s=>s.id===p.story))selectedStory=p.story;else lastSettings.story=null;}}catch{}
 controls();
})();
