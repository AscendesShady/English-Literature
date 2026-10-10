'use strict';
(()=>{
 const status=document.getElementById('offline-status'),install=document.getElementById('install-app'),topInstall=document.getElementById('install-top'),update=document.getElementById('update-app'),guide=document.getElementById('install-guide');
 const installButtons=[topInstall,install];
 let prompt=null,registration=null,readyOffline=false,reloading=false,installing=false,installedHere=false;
 const standalone=()=>matchMedia('(display-mode: standalone)').matches||navigator.standalone===true;
 function showStatus(){status.textContent=!navigator.onLine?(readyOffline?'You’re offline. Your whole library is ready to read!':'You’re offline. Open the hosted library online once to save it.') :readyOffline?`All ${window.STORIES.length} stories, illustrations and quotes are ready offline!`:'Saving your library for days without a signal…';}
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
 navigator.serviceWorker.register('./sw.js',{updateViaCache:'none'}).then(async reg=>{
  registration=reg;offerUpdate();reg.addEventListener('updatefound',()=>{const worker=reg.installing;if(worker)worker.addEventListener('statechange',()=>{if(worker.state==='installed'){if(navigator.serviceWorker.controller)setTimeout(offerUpdate,0);}if(worker.state==='redundant'&&!readyOffline)status.textContent='Offline saving did not finish. Reopen the hosted library online to try again.';});});
  await navigator.serviceWorker.ready;readyOffline=true;showStatus();
 }).catch(()=>{status.textContent='The library is open online. Offline saving could not finish; reopen when connected to try again.';});
 window.addEventListener('online',showStatus);window.addEventListener('offline',showStatus);
})();
