/* Prepared card audio, scoped to this library and its exact text/voice/pace. */
(()=>{
 'use strict';
 const scope=new URL('./',location.href).href,name=`once-upon-narration:${scope}:cards-v1`;
 const enabled=location.protocol!=='file:'&&!!globalThis.caches&&!!globalThis.crypto?.subtle;
 const cache=()=>caches.open(name);
 async function url(frame,voice,pace){
  const bytes=new TextEncoder().encode('kokoro-1.2.1-1939ad2a-q8:'+frame.text);
  const digest=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))).map(n=>n.toString(16).padStart(2,'0')).join('');
  return new URL(`_prepared-narration/${voice}/${pace}/${encodeURIComponent(frame.storyId)}/${encodeURIComponent(frame.key)}-${digest}.wav`,scope).href;
 }
 async function get(frame,voice,pace){
  if(!enabled)return null;
  if(!await caches.has(name))return null;
  const response=await (await cache()).match(await url(frame,voice,pace));if(!response)return null;
  const bytes=await response.arrayBuffer(),view=new DataView(bytes);
  if(bytes.byteLength<44||view.getUint32(0)!==0x52494646||view.getUint16(22,true)!==1||view.getUint16(34,true)!==16)return null;
  const count=view.getUint32(40,true)/2;if(44+count*2!==bytes.byteLength)return null;
  const samples=new Float32Array(count);for(let i=0;i<count;i++)samples[i]=view.getInt16(44+i*2,true)/32768;
  return {samples,sampleRate:view.getUint32(24,true),cached:true};
 }
 async function put(frame,voice,pace,audio){
  if(!enabled)throw new Error('storage-unavailable');
  const bytes=new ArrayBuffer(44+audio.samples.length*2),view=new DataView(bytes);
  const chars=(offset,text)=>{for(let i=0;i<text.length;i++)view.setUint8(offset+i,text.charCodeAt(i));};
  chars(0,'RIFF');view.setUint32(4,bytes.byteLength-8,true);chars(8,'WAVE');chars(12,'fmt ');view.setUint32(16,16,true);view.setUint16(20,1,true);view.setUint16(22,1,true);view.setUint32(24,audio.sampleRate,true);view.setUint32(28,audio.sampleRate*2,true);view.setUint16(32,2,true);view.setUint16(34,16,true);chars(36,'data');view.setUint32(40,audio.samples.length*2,true);
  for(let i=0;i<audio.samples.length;i++){const sample=Math.max(-1,Math.min(1,audio.samples[i]));view.setInt16(44+i*2,Math.round(sample*(sample<0?32768:32767)),true);}
  await (await cache()).put(await url(frame,voice,pace),new Response(bytes,{headers:{'Content-Type':'audio/wav','X-Audio-Bytes':String(bytes.byteLength)}}));
  return bytes.byteLength;
 }
 async function inventory(frames,voice,pace){
  if(!enabled||!await caches.has(name))return {ready:[],missing:frames,bytes:0};
  const saved=await cache(),keys=new Set((await saved.keys()).map(request=>request.url));
  const paths=await Promise.all(frames.map(frame=>url(frame,voice,pace))),ready=[],missing=[];
  let bytes=0;
  for(let i=0;i<frames.length;i++){
   if(keys.has(paths[i])){ready.push(frames[i]);bytes+=Number((await saved.match(paths[i])).headers.get('X-Audio-Bytes')||0);}else missing.push(frames[i]);
  }
  return {ready,missing,bytes};
 }
 globalThis.NarrationStore={enabled,get,put,inventory,clear:async()=>{if(enabled)await caches.delete(name);}};
})();
