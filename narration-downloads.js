/* Resumable preparation of finished narration, without changing story progress. */
(()=>{
 'use strict';
 const $=id=>document.getElementById(id),dialog=$('audio-downloads'),scope=$('audio-scope'),voice=$('audio-voice'),pace=$('audio-pace'),versions=$('audio-versions'),start=$('audio-start'),pause=$('audio-pause'),status=$('audio-status'),bar=$('audio-progress'),count=$('audio-count');
 let running=false,pausing=false,refreshId=0,selectedStory=null,lastSettings=null;
 const bytes=n=>n>=1e9?(n/1e9).toFixed(1)+' GB':(n/1e6).toFixed(1)+' MB';
 const frames=()=>STORIES.filter(story=>scope.value==='all'||story.id===selectedStory).flatMap(story=>story.scenes.map((frame,index)=>({storyId:story.id,title:story.title,key:frame.key,text:frame.text,index,total:story.scenes.length})));
 const combinations=()=>{
  if(versions.value!=='all')return [{voice:voice.value,pace:Number(pace.value)}];
  const current=StoryNarrator.settings(),matrix=['af_heart','bm_fable'].flatMap(v=>[0.85,0.92,1,1.1].map(p=>({voice:v,pace:p})));
  return matrix.sort((a,b)=>Number(b.voice===current.voice&&b.pace===current.pace)-Number(a.voice===current.voice&&a.pace===current.pace));
 };
 async function inventory(items,variants){const result={ready:[],missing:[],bytes:0};for(const variant of variants){const saved=await NarrationStore.inventory(items,variant.voice,variant.pace);result.ready.push(...saved.ready.map(frame=>({...frame,...variant})));result.missing.push(...saved.missing.map(frame=>({...frame,...variant})));result.bytes+=saved.bytes;}
  const order=new Map(items.map((frame,index)=>[frame.storyId+'|'+frame.key,index]));
  result.missing.sort((a,b)=>order.get(a.storyId+'|'+a.key)-order.get(b.storyId+'|'+b.key));return result;
 }
 function controls(){start.disabled=running||!NarrationStore.enabled||!frames().length;pause.disabled=!running||pausing;$('audio-clear').disabled=running||!NarrationStore.enabled;for(const el of [scope,versions])el.disabled=running;voice.disabled=pace.disabled=running||versions.value==='all';}
 function progress(done,total,size){bar.max=total||1;bar.value=done;count.textContent=`${done.toLocaleString()} / ${total.toLocaleString()} recordings saved · ${bytes(size)}`;$('audio-top').textContent=running?`Audio ${done}/${total}`:'Audio ↓';}
 function prefs(){lastSettings={voice:voice.value,pace:pace.value,versions:versions.value,scope:scope.value,story:selectedStory};try{localStorage.setItem('once-upon-audio-downloads-v1',JSON.stringify(lastSettings));}catch{}}
 async function refresh(){
  if(running)return;const id=++refreshId,items=frames(),variants=combinations(),total=items.length*variants.length;controls();start.disabled=true;
  const words=items.reduce((sum,frame)=>sum+frame.text.trim().split(/\s+/).length,0),estimate=variants.reduce((sum,variant)=>sum+words*60/(150*variant.pace)*48000,0);
  $('audio-size').textContent=`Estimated finished audio: ${bytes(estimate)} for ${variants.length===8?'all 2 voices and 4 paces (8 versions)':'the selected voice and pace'}, plus the voice model. Completed versions play without speech generation.`;
  if(!NarrationStore.enabled){status.textContent='Open the hosted library to save narration in your browser.';$('audio-open-hosted').hidden=false;progress(0,total,0);return;}
  bar.max=total||1;bar.value=0;count.textContent=`Checking ${total.toLocaleString()} recordings…`;status.textContent='Checking saved recordings…';
  try{const saved=await inventory(items,variants);if(id!==refreshId)return;progress(saved.ready.length,total,saved.bytes);start.textContent=saved.missing.length?(saved.ready.length?'Resume download':'Download narration'):'All selected narration is ready';controls();if(!saved.missing.length)start.disabled=true;status.textContent=saved.missing.length?'Finished recordings stay saved if you pause or close the browser. Resume skips those recordings.':'Ready to listen without preparing each card again.';}
  catch{if(id!==refreshId)return;controls();status.textContent='Audio storage could not be opened. Try reopening the hosted library.';}
 }
 function open(kind='all'){
  if(!running){const current=readerNarration.getFrame();selectedStory=kind==='story'?current?.storyId||selectedStory:lastSettings?.story||current?.storyId||selectedStory;const option=scope.querySelector('[value="story"]');option.disabled=!selectedStory;option.textContent=selectedStory?`This story: ${STORIES.find(s=>s.id===selectedStory).title} (12 cards)`:'This story (open a story first)';scope.value=(kind==='story'||lastSettings?.scope==='story')&&selectedStory?'story':'all';const config=kind==='story'||!lastSettings?StoryNarrator.settings():lastSettings;voice.value=config.voice;pace.value=String(config.pace);versions.value=lastSettings?.versions||'all';refresh();}
  if(!dialog.open)dialog.showModal();
 }
 async function download(){
  if(running)return;const items=frames(),variants=combinations(),total=items.length*variants.length;running=true;pausing=false;refreshId++;controls();prefs();if(variants.length===1)StoryNarrator.useSettings(variants[0].voice,variants[0].pace);
  let saved,done=0,size=0;const timings=[];
  try{
   saved=await inventory(items,variants);done=saved.ready.length;size=saved.bytes;progress(done,total,size);
   navigator.storage?.persist?.().catch(()=>{});
   const estimate=await navigator.storage?.estimate?.().catch(()=>null);
   if(estimate?.quota&&estimate.quota-estimate.usage<48000*5&&saved.missing.length)throw new DOMException('Storage full','QuotaExceededError');
   for(const frame of saved.missing){
    if(pausing)break;
    status.textContent=`Preparing ${frame.title}, card ${frame.index+1} · ${frame.voice==='af_heart'?'American':'British'}, pace ${frame.pace}…`;
    const began=performance.now(),audio=await StoryNarrator.prepare(frame,frame.voice,frame.pace,()=>!pausing);
    if(!audio)break;
    done++;size+=audio.storedBytes||44+audio.samples.length*2;timings.push(performance.now()-began);if(timings.length>8)timings.shift();progress(done,total,size);
    if(timings.length>=3){const minutes=Math.ceil(timings.reduce((a,b)=>a+b,0)/timings.length*(total-done)/60000);status.textContent=`Saved ${frame.title}, card ${frame.index+1}. About ${minutes.toLocaleString()} minutes remaining at this device’s current speed.`;}
    // Allow input and playback requests to run before queuing the next card.
    await new Promise(resolve=>setTimeout(resolve,40));
   }
   status.textContent=done===total?'All selected narration is saved. Cards are ready for immediate offline listening.':'Paused. Finished recordings are saved; Resume picks up the rest.';
  }catch(error){status.textContent=error.name==='QuotaExceededError'?'Paused because browser storage is full. Finished cards are saved; free space or prepare fewer stories.':'Preparation stopped. Finished cards are saved. Reconnect if the voice model is still downloading, then Resume.';}
  finally{running=false;pausing=false;controls();start.textContent=done===total?'All selected narration is ready':'Resume download';if(done===total)start.disabled=true;progress(done,total,size);}
 }
 $('audio-top').addEventListener('click',()=>open());$('audio-install').addEventListener('click',()=>open());$('audio-story').addEventListener('click',()=>open('story'));
 $('audio-close').addEventListener('click',()=>dialog.close());start.addEventListener('click',download);
 pause.addEventListener('click',()=>{pausing=true;controls();status.textContent='Pausing after the current card is saved…';});
 $('audio-clear').addEventListener('click',async()=>{if(running||!confirm('Remove all downloaded card narration? Your saved shelf, reading progress and voice model will remain.'))return;await NarrationStore.clear();refresh();});
 for(const el of [scope,voice,pace,versions])el.addEventListener('change',()=>{prefs();refresh();});
 globalThis.addEventListener('narration-model-progress',event=>{if(running&&!pausing)status.textContent=`Preparing the voice model… ${Math.round(event.detail.progress||0)}%. Finished card audio will be saved next.`;});
 try{const p=JSON.parse(localStorage.getItem('once-upon-audio-downloads-v1'));if(p&&['af_heart','bm_fable'].includes(p.voice)&&['0.85','0.92','1','1.1'].includes(String(p.pace))){lastSettings=p;if(STORIES.some(s=>s.id===p.story))selectedStory=p.story;else lastSettings.story=null;}}catch{}
 controls();
})();
