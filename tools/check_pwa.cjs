const {chromium}=require('C:/Users/ascen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve(__dirname,'..'),assert=(v,m)=>{if(!v)throw Error(m)};
const prefix='/literature-test/';let testUpdate=false;
const server=http.createServer((req,res)=>{
 const parsed=new URL(req.url,'http://localhost');if(!parsed.pathname.startsWith(prefix)){res.writeHead(404);return res.end();}
 const name=decodeURIComponent(parsed.pathname.slice(prefix.length))||'index.html',target=path.resolve(root,name);
 if(!target.startsWith(root+path.sep)||name.startsWith('qa/')||name.startsWith('tools/')){res.writeHead(403);return res.end();}
 try{let data=fs.readFileSync(target);if(name==='sw.js'&&testUpdate)data=Buffer.from(data.toString().replace('v3-20261009','v4-test'));
 const mime={'.html':'text/html','.js':'application/javascript','.json':'application/json','.css':'text/css','.svg':'image/svg+xml','.png':'image/png','.docx':'application/vnd.openxmlformats-officedocument.wordprocessingml.document'};
 res.writeHead(200,{'Content-Type':(mime[path.extname(name)]||'application/octet-stream')+(['.html','.js','.json','.css','.svg'].includes(path.extname(name))?'; charset=utf-8':''),'Cache-Control':'no-store'});res.end(data);
 }catch{res.writeHead(404);res.end();}
});
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const site=`http://127.0.0.1:${server.address().port}${prefix}index.html`;
 const profile=fs.mkdtempSync(path.join(root,'qa/pwa-profile-'));
 const context=await chromium.launchPersistentContext(profile,{channel:'chrome',headless:true,viewport:{width:1365,height:1000},reducedMotion:'reduce'}),page=await context.newPage(),errors=[];
 page.on('pageerror',e=>errors.push(e.message));await page.goto(site);await page.waitForFunction(()=>navigator.serviceWorker.controller,{timeout:30000});
 await page.waitForFunction(()=>document.getElementById('offline-status').textContent.includes('ready offline'));
 assert(await page.locator('.story-card').count()===98,'Hosted catalogue');
 const client=await context.newCDPSession(page),manifestInfo=await client.send('Page.getAppManifest');assert(manifestInfo.errors.length===0,'Manifest has no errors');const manifest=JSON.parse(manifestInfo.data);assert(manifest.display==='standalone','Standalone display');assert(manifest.scope==='./'&&manifest.id==='./','Repository-relative scope and identity');
 const installability=await client.send('Page.getInstallabilityErrors');assert(!installability.installabilityErrors.length,JSON.stringify(installability.installabilityErrors));
 const cached=await page.evaluate(async()=>{const names=await caches.keys(),name=names.find(n=>n.includes('v3-20261009'));return (await (await caches.open(name)).keys()).map(r=>r.url);});assert(cached.length===14,'All 14 shell/document assets precached');
 await page.locator('[data-story="othello"]').click();await page.screenshot({path:path.join(root,'qa/character-othello.png')});await page.locator('#close-reader').click();
 await page.locator('[data-story="animal-farm"]').click();await page.locator('[data-scene="10"]').click();assert(await page.locator('#scene-art .story-person').count()>0,'Illustrated animal cast');await page.screenshot({path:path.join(root,'qa/character-animal-farm.png')});await page.locator('#close-reader').click();
 await page.locator('[data-save="animal-farm"]').click();
 await context.setOffline(true);await page.goto(site+'#story/animal-farm/12');assert((await page.locator('#scene-number').textContent()).includes('12'),'Offline direct link');await page.locator('#tab-quotes').click();assert(await page.locator('.quote-card').isVisible(),'Offline quotations');
 const docBytes=await page.evaluate(async()=>{const r=await fetch('literature%20by%20codex.docx');return r.ok?(await r.arrayBuffer()).byteLength:0});assert(docBytes>10000,'Companion document cached offline');await page.locator('#close-reader').click();await page.reload();assert(await page.locator('.story-card').count()===98,'Offline reload all 98');assert((await page.locator('#offline-status').textContent()).includes('offline'),'Offline status');
 const stories=await page.evaluate(()=>STORIES.map(s=>s.id));let quotes=0;
 for(const id of stories){await page.locator(`[data-story="${id}"]`).click();await page.locator('#tab-recall').click();await page.locator('#explore-quotes').click();assert(await page.locator('.quote-card blockquote').isVisible(),'Offline quote '+id);quotes++;await page.locator('#close-reader').click();}
 await context.setOffline(false);await page.evaluate(async()=>{await caches.open('unrelated-app-keep');await caches.open('once-upon-timeline:http://other-scope/:v0');});testUpdate=true;await page.evaluate(async()=>{await (await navigator.serviceWorker.getRegistration()).update()});await page.waitForFunction(()=>!document.getElementById('update-app').hidden);assert(await page.evaluate(async()=>!!(await navigator.serviceWorker.getRegistration()).waiting),'Update waits for reader');
 await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.locator('#update-app').click()]);await page.waitForFunction(async()=>{const keys=await caches.keys();return keys.some(k=>k.endsWith('v4-test'))&&!keys.some(k=>k.endsWith('v3-20261009'))});const names=await page.evaluate(()=>caches.keys());assert(names.includes('unrelated-app-keep')&&names.includes('once-upon-timeline:http://other-scope/:v0'),'Other application caches preserved');
 await page.locator('#saved-button').click();assert(await page.locator('.story-card').count()===1,'Saved shelf persists through update');await page.locator('#saved-button').click();
 for(const width of [360,390,768]){await page.setViewportSize({width,height:844});await page.locator('[data-story="a-christmas-carol"]').click();await page.locator('[data-scene="11"]').click();assert(await page.locator('#reader').evaluate(el=>el.scrollWidth<=el.clientWidth),'12-scene mobile layout '+width);await page.screenshot({path:path.join(root,`qa/storybook-${width}.png`)});await page.locator('#close-reader').click();}
 assert(!errors.length,errors.join('; '));const report={works:98,scenes:1176,offlineQuotes:quotes,cacheAssets:cached.length,manifestErrors:manifestInfo.errors,installabilityErrors:installability.installabilityErrors,checks:['real service-worker registration on localhost','GitHub-style subdirectory','manifest/icon installability','offline reload and direct story link','all 98 quote panels offline','offline companion document','user-controlled update','cache isolation and cleanup','saved shelf after update','mobile 12-scene controls'],errors};fs.writeFileSync(path.join(root,'qa/pwa-report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));await context.close();await new Promise(r=>server.close(r));
})().catch(e=>{console.error(e);server.close();process.exit(1)});
