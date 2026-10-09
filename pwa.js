'use strict';
(()=>{
 const status=document.getElementById('offline-status'),install=document.getElementById('install-app'),update=document.getElementById('update-app'),guide=document.getElementById('install-guide');
 let prompt=null,registration=null,readyOffline=false,reloading=false;
 const standalone=()=>matchMedia('(display-mode: standalone)').matches||navigator.standalone===true;
 function showStatus(){status.textContent=!navigator.onLine?(readyOffline?'You’re offline. Your whole library is ready to read!':'You’re offline. Open the hosted library online once to save it.') :readyOffline?'All 98 stories, illustrations and quotes are ready offline!':'Saving your library for days without a signal…';}
 document.getElementById('install-help').addEventListener('click',()=>guide.showModal());document.getElementById('close-install-guide').addEventListener('click',()=>guide.close());
 window.addEventListener('beforeinstallprompt',event=>{event.preventDefault();prompt=event;if(!standalone())install.hidden=false;});
 install.addEventListener('click',async()=>{if(!prompt)return;const pending=prompt;prompt=null;install.hidden=true;await pending.prompt();const choice=await pending.userChoice;if(choice.outcome==='dismissed')status.textContent='You can install later from Chrome’s menu. Your reading place is kept.';});
 window.addEventListener('appinstalled',()=>{install.hidden=true;prompt=null;status.textContent='Installed! Your library now has its own home.';});
 update.addEventListener('click',()=>{update.disabled=true;registration?.waiting?.postMessage({type:'SKIP_WAITING'});});
 if(location.protocol==='file:'){status.textContent='Local preview. Use the hosted site to install and save the offline app.';return;}
 if(!('serviceWorker' in navigator)||!window.isSecureContext){status.textContent='Read online here. Installation and offline saving need the HTTPS site address.';return;}
 navigator.serviceWorker.addEventListener('controllerchange',()=>{if(update.disabled&&!reloading){reloading=true;location.reload();}});
 function offerUpdate(){if(registration.waiting){update.hidden=false;update.disabled=false;}}
 navigator.serviceWorker.register('./sw.js',{updateViaCache:'none'}).then(async reg=>{
  registration=reg;offerUpdate();reg.addEventListener('updatefound',()=>{const worker=reg.installing;if(worker)worker.addEventListener('statechange',()=>{if(worker.state==='installed'){if(navigator.serviceWorker.controller)setTimeout(offerUpdate,0);}if(worker.state==='redundant'&&!readyOffline)status.textContent='Offline saving did not finish. Reopen the hosted library online to try again.';});});
  await navigator.serviceWorker.ready;readyOffline=true;showStatus();
 }).catch(()=>{status.textContent='The library is open online. Offline saving could not finish; reopen when connected to try again.';});
 window.addEventListener('online',showStatus);window.addEventListener('offline',showStatus);
})();
