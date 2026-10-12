'use strict';
(()=>{
 const status=document.getElementById('offline-status'),install=document.getElementById('install-app'),topInstall=document.getElementById('install-top'),update=document.getElementById('update-app'),guide=document.getElementById('install-guide');
 const installButtons=[topInstall,install];
 const appScope=new URL('./',location.href).href,disabledKey='once-upon-offline-disabled:'+appScope;
 let offlineDisabled=false;
 try{offlineDisabled=localStorage.getItem(disabledKey)==='1';}catch{}
 let prompt=null,registration=null,readyOffline=false,reloading=false,installing=false,installedHere=false;
 const standalone=()=>matchMedia('(display-mode: standalone)').matches||navigator.standalone===true;
 function showStatus(){if(offlineDisabled){status.textContent='Offline downloads cleared. Use Download audio → Save website offline to save this library again.';return;}status.textContent=!navigator.onLine?(readyOffline?'You’re offline. Your whole library is ready to read!':'You’re offline. Open the hosted library online once to save it.') :readyOffline?`All ${window.STORIES.length} stories, illustrations and quotes are ready offline!`:'Saving your library for days without a signal…';}
 function changed(){window.dispatchEvent(new Event('offline-downloads-changed'));}
 function setDisabled(value){offlineDisabled=value;try{if(value)localStorage.setItem(disabledKey,'1');else localStorage.removeItem(disabledKey);}catch{}showStatus();changed();}
 async function disableWorker(worker){
  if(!worker)return;
  await new Promise(resolve=>{const channel=new MessageChannel(),timer=setTimeout(()=>{channel.port1.close();resolve();},1200);channel.port1.onmessage=()=>{clearTimeout(timer);channel.port1.close();resolve();};try{worker.postMessage({type:'DISABLE_DOWNLOADS'},[channel.port2]);}catch{clearTimeout(timer);channel.port1.close();resolve();}});
 }
 async function clearDeviceCache(){
  setDisabled(true);readyOffline=false;update.hidden=true;update.disabled=false;
  // An empty preference marker also survives service-worker restarts.
  await caches.open(disabledKey);
  await globalThis.StoryNarrator?.releaseDownloads?.();
  if('serviceWorker' in navigator){
   const registrations=(await navigator.serviceWorker.getRegistrations()).filter(reg=>reg.scope===appScope);
   for(const reg of registrations){await Promise.all([reg.active,reg.waiting,reg.installing].filter(Boolean).map(disableWorker));await reg.unregister();}
   registration=null;
  }
  const prefixes=['once-upon-timeline:'+appScope+':','once-upon-narration:'+appScope+':'];
  const owned=(await caches.keys()).filter(name=>prefixes.some(prefix=>name.startsWith(prefix)));
  await Promise.all(owned.map(name=>caches.delete(name)));showStatus();changed();
 }
 async function enableOffline(){
  if(location.protocol==='file:'||!('serviceWorker' in navigator)||!isSecureContext)throw new Error('hosted');
  await caches.delete(disabledKey);
  setDisabled(false);await registerLibrary();
  if(navigator.serviceWorker.controller!==registration.active)await new Promise((resolve,reject)=>{const timer=setTimeout(()=>{navigator.serviceWorker.removeEventListener('controllerchange',check);reject(new Error('offline-setup'));},15000);function check(){if(navigator.serviceWorker.controller!==registration.active)return;clearTimeout(timer);navigator.serviceWorker.removeEventListener('controllerchange',check);resolve();}navigator.serviceWorker.addEventListener('controllerchange',check);check();});
 }
 globalThis.OfflineLibrary={clearDeviceCache,enable:enableOffline,disabled:()=>offlineDisabled};
 window.addEventListener('storage',event=>{if(event.key===disabledKey){offlineDisabled=event.newValue==='1';if(offlineDisabled){readyOffline=false;update.hidden=true;globalThis.StoryNarrator?.releaseDownloads?.().catch(()=>{});}showStatus();changed();}});
 document.getElementById('install-help').addEventListener('click',()=>guide.showModal());document.getElementById('close-install-guide').addEventListener('click',()=>guide.close());
 function syncInstallButtons(){const installed=installedHere||standalone();topInstall.hidden=installed;install.hidden=installed||!prompt;for(const button of installButtons)button.disabled=installing;}
 window.addEventListener('beforeinstallprompt',event=>{event.preventDefault();if(installedHere||standalone())return;prompt=event;syncInstallButtons();});
 async function requestInstall(){
  if(installing)return;
  if(!prompt){if(!guide.open)guide.showModal();return;}
  const pending=prompt;prompt=null;installing=true;syncInstallButtons();
  try{await pending.prompt();const choice=await pending.userChoice;if(!installedHere)status.textContent=choice.outcome==='dismissed'?'You can install later from Chrome’s menu. Your reading place is kept.':'Installation requested. Follow Chrome’s confirmation.';}
  catch{status.textContent='Chrome could not open the install prompt. See the installation options to try again.';if(!guide.open)guide.showModal();}
  finally{installing=false;syncInstallButtons();}
 }
 for(const button of installButtons)button.addEventListener('click',requestInstall);
 window.addEventListener('appinstalled',()=>{installedHere=true;prompt=null;syncInstallButtons();status.textContent='Installed! Your library now has its own home.';});
 syncInstallButtons();
 update.addEventListener('click',()=>{update.disabled=true;registration?.waiting?.postMessage({type:'SKIP_WAITING'});});
 if(location.protocol==='file:'){status.textContent='Local preview. Use the hosted site to install and save the offline app.';return;}
 if(!('serviceWorker' in navigator)||!window.isSecureContext){status.textContent='Read online here. Installation and offline saving need the HTTPS site address.';return;}
 navigator.serviceWorker.addEventListener('controllerchange',()=>{if(update.disabled&&!reloading){reloading=true;location.reload();}});
 function offerUpdate(){if(registration.waiting){update.hidden=false;update.disabled=false;}}
 async function registerLibrary(){try{const reg=await navigator.serviceWorker.register('./sw.js',{updateViaCache:'none'});
  registration=reg;offerUpdate();reg.addEventListener('updatefound',()=>{const worker=reg.installing;if(worker)worker.addEventListener('statechange',()=>{if(worker.state==='installed'){if(navigator.serviceWorker.controller)setTimeout(offerUpdate,0);}if(worker.state==='redundant'&&!readyOffline)status.textContent='Offline saving did not finish. Reopen the hosted library online to try again.';});});
  await navigator.serviceWorker.ready;if(offlineDisabled)return;readyOffline=true;showStatus();
 }catch(error){status.textContent='The library is open online. Offline saving could not finish; reopen when connected to try again.';throw error;}}
 if(offlineDisabled)showStatus();else registerLibrary().catch(()=>{});
 window.addEventListener('online',showStatus);window.addEventListener('offline',showStatus);
})();
