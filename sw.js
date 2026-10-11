'use strict';
importScripts('./painted-assets.js');
const PREFIX='once-upon-timeline:'+self.registration.scope+':';
const VERSION=PREFIX+'v7-painted-40ead279f039';
const SHELL=['./','./index.html','./styles.css','./stories.js','./painted-assets.js','./illustrations.js','./app.js','./pwa.js','./manifest.json','./assets/favicon.svg','./assets/icons/icon-192.png','./assets/icons/icon-512.png','./assets/icons/icon-maskable-512.png','./assets/icons/apple-touch-icon.png',...Object.values(self.PAINTED_ART.works).map(art=>'./'+art.file)];
const urls=SHELL.map(path=>new URL(path,self.registration.scope).href);
self.addEventListener('install',event=>event.waitUntil(caches.open(VERSION).then(cache=>cache.addAll(urls))));
self.addEventListener('activate',event=>event.waitUntil((async()=>{
 const names=await caches.keys();await Promise.all(names.filter(n=>n.startsWith(PREFIX)&&n!==VERSION).map(n=>caches.delete(n)));
 await self.clients.claim();
})()));
self.addEventListener('message',event=>{if(event.data?.type==='SKIP_WAITING')self.skipWaiting();});
self.addEventListener('fetch',event=>{
 const request=event.request,url=new URL(request.url);
 if(request.method!=='GET'||url.origin!==self.location.origin||!url.href.startsWith(self.registration.scope))return;
 // Cache only this app's declared resources. Source websites are left to the network.
 const canonical=new URL(url.href);canonical.search='';canonical.hash='';
 const navigation=request.mode==='navigate';
 if(!navigation&&!urls.includes(canonical.href))return;
 event.respondWith((async()=>{
  const cache=await caches.open(VERSION);
  if(navigation){const shell=await cache.match(new URL('./index.html',self.registration.scope).href);return shell||fetch(request);}
  const cached=await cache.match(canonical.href);if(cached)return cached;
  return fetch(request);
 })());
});
