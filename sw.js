'use strict';
importScripts('./painted-assets.js','./authors.js','./narration-assets.js');
const PREFIX='once-upon-timeline:'+self.registration.scope+':';
const VERSION=PREFIX+'v7-painted-c8f4048d3b71';
const SHELL=['./','./index.html','./styles.css','./stories.js','./authors.js','./painted-assets.js','./illustrations.js','./app.js','./pwa.js','./manifest.json','./assets/favicon.svg','./assets/icons/icon-192.png','./assets/icons/icon-512.png','./assets/icons/icon-maskable-512.png','./assets/icons/apple-touch-icon.png',...Object.values(self.PAINTED_ART.works).map(art=>'./'+art.file),...Object.values(self.AUTHOR_LIBRARY.profiles).filter(author=>author.portrait).map(author=>'./'+author.portrait)];
const urls=SHELL.map(path=>new URL(path,self.registration.scope).href);
urls.push(...['narration.js','narration-assets.js','narration-store.js','narration-downloads.js'].map(file=>new URL(file,self.registration.scope).href));
const neuralUrls=self.NARRATION_ASSETS.files.map(path=>new URL(path,self.registration.scope).href);
const neuralPrefix='once-upon-narration:'+self.registration.scope+':assets-';
const neuralCache=neuralPrefix+self.NARRATION_ASSETS.version;
self.addEventListener('install',event=>event.waitUntil((async()=>{
 await (await caches.open(VERSION)).addAll(urls);
 // Readers who already prepared narration retain it across app updates.
 const prior=(await caches.keys()).filter(name=>name.startsWith(neuralPrefix)&&name!==neuralCache);
 if(!prior.length)return;
 const target=await caches.open(neuralCache);
 for(const file of self.NARRATION_ASSETS.files){
  const url=new URL(file,self.registration.scope).href;
  if(await target.match(url))continue;
  let reused=false;
  for(const name of prior){
   const response=await (await caches.open(name)).match(url);if(!response)continue;
   const digest=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',await response.clone().arrayBuffer()))).map(n=>n.toString(16).padStart(2,'0')).join('');
   if(digest===self.NARRATION_ASSETS.hashes[file]){await target.put(url,response);reused=true;break;}
  }
  if(!reused){const response=await fetch(url);if(!response.ok)throw new Error('Narration update did not finish');await target.put(url,response);}
 }
})()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{
 const names=await caches.keys();await Promise.all(names.filter(n=>n.startsWith(PREFIX)&&n!==VERSION).map(n=>caches.delete(n)));
 if(names.includes(neuralCache))await Promise.all(names.filter(n=>n.startsWith(neuralPrefix)&&n!==neuralCache).map(n=>caches.delete(n)));
 await self.clients.claim();
})()));
self.addEventListener('message',event=>{if(event.data?.type==='SKIP_WAITING')self.skipWaiting();});
self.addEventListener('fetch',event=>{
 const request=event.request,url=new URL(request.url);
 if(request.method!=='GET'||url.origin!==self.location.origin||!url.href.startsWith(self.registration.scope))return;
 // Cache only this app's declared resources. Source websites are left to the network.
 const canonical=new URL(url.href);canonical.search='';canonical.hash='';
 const navigation=request.mode==='navigate';
 const optional=neuralUrls.includes(canonical.href);
 if(!navigation&&!urls.includes(canonical.href)&&!optional)return;
 event.respondWith((async()=>{
  const cache=await caches.open(optional?neuralCache:VERSION);
  if(navigation){const shell=await cache.match(new URL('./index.html',self.registration.scope).href);return shell||fetch(request);}
  const cached=await cache.match(canonical.href);if(cached)return cached;
  const response=await fetch(request);
  if(optional&&response.ok)try{await cache.put(canonical.href,response.clone());}catch{}
  return response;
 })());
});
