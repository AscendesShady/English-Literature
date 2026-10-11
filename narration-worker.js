import {KokoroTTS,modelEnvironment} from './assets/narration/kokoro.web.js';
const MODEL='onnx-community/Kokoro-82M-v1.0-ONNX';
const REVISION='1939ad2a8e416c0acfeecc08a694d14ef25f2231';
const scope=new URL('./',import.meta.url).href;
let engine,loading;
async function prepare(){
 if(engine)return engine;
 if(!loading)loading=(async()=>{
  modelEnvironment.allowLocalModels=false;
  modelEnvironment.remotePathTemplate=`{model}/resolve/${REVISION}/`;
  modelEnvironment.backends.onnx.wasm.wasmPaths=new URL('./assets/narration/',import.meta.url).href;
  modelEnvironment.backends.onnx.wasm.numThreads=1;
  modelEnvironment.backends.onnx.wasm.proxy=false;
  modelEnvironment.useBrowserCache=false;
  modelEnvironment.useCustomCache=true;
  modelEnvironment.customCache=await caches.open(`once-upon-narration:${scope}:model-${REVISION}`);
  await Promise.all(['af_heart','bm_fable'].map(async voice=>{
   const response=await fetch(new URL(`./assets/narration/voices/${voice}.bin`,import.meta.url));
   if(!response.ok)throw new Error('Voice style download did not finish');
   await response.arrayBuffer();
  }));
  engine=await KokoroTTS.from_pretrained(MODEL,{dtype:'q8',device:'wasm',progress_callback:progress=>{
   if(progress.status==='progress')self.postMessage({type:'progress',file:progress.file,progress:progress.progress});
  }});
  self.postMessage({type:'ready'});return engine;
 })().catch(error=>{loading=null;throw error;});
 return loading;
}
self.addEventListener('message',async event=>{
 const {id,type,text,voice,speed=0.92}=event.data;
 try{
  const tts=await prepare();
  if(type==='prepare'){self.postMessage({id,type:'prepared'});return;}
  if(type!=='generate')return;
  const audio=await tts.generate(text,{voice,speed});
  const samples=audio.audio instanceof Float32Array?audio.audio:new Float32Array(audio.audio);
  self.postMessage({id,type:'audio',samples,sampleRate:audio.sampling_rate||24000},[samples.buffer]);
 }catch(error){self.postMessage({id,type:'error',message:error.message||String(error)});}
});
