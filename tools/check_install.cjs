const {chromium}=require('C:/Users/ascen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const root=path.resolve(__dirname,'..'),site=pathToFileURL(path.join(root,'index.html')).href;
const assert=(value,message)=>{if(!value)throw Error(message)};
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 try{
  const context=await browser.newContext({viewport:{width:1365,height:900},reducedMotion:'reduce'}),page=await context.newPage(),errors=[];
  page.on('pageerror',e=>errors.push(e.message));await page.goto(site);
  assert(await page.locator('#install-top').isVisible(),'Top install visible in local preview');
  await page.locator('#install-top').click();assert(await page.locator('#install-guide').evaluate(el=>el.open),'No native event opens guidance');
  assert(await page.locator('#installation-origin-note a').getAttribute('href')==='https://ascendesshady.github.io/English-Literature/','Guide links to hosted library');
  await page.keyboard.press('Escape');assert(await page.locator('#install-top').evaluate(el=>el===document.activeElement),'Focus restored to install button');
  for(const width of [1365,768,390,360,320]){
   await page.setViewportSize({width,height:900});await page.evaluate(()=>scrollTo(0,0));
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Header fits at '+width);
   const bounds=await page.locator('#install-top').boundingBox();assert(bounds&&bounds.y>=0&&bounds.y+bounds.height<200,'Install above fold at '+width);
   await page.screenshot({path:path.join(root,`qa/install-header-${width}.png`)});
  }
  // Exercise the browser event contract without installing an app on the host.
  async function offer(fails=false){await page.evaluate(fails=>{
   window.installCalls=0;window.installChoice=new Promise(resolve=>window.resolveInstall=resolve);
   const event=new Event('beforeinstallprompt',{cancelable:true});event.prompt=async()=>{window.installCalls++;if(fails)throw Error('Prompt unavailable')};event.userChoice=window.installChoice;window.dispatchEvent(event);
  },fails)}
  await offer();assert(await page.locator('#install-app').isVisible(),'Lower button shares native availability');
  await page.locator('#install-top').click();assert(await page.locator('#install-top').isDisabled(),'Pending prompt disables top control');
  assert(await page.locator('#install-app').isDisabled(),'Pending prompt disables lower control');
  await page.evaluate(()=>document.getElementById('install-top').click());assert(await page.evaluate(()=>installCalls)===1,'Prompt used once even with repeated clicks');
  await page.evaluate(()=>resolveInstall({outcome:'dismissed'}));await page.waitForFunction(()=>!document.getElementById('install-top').disabled);
  assert(await page.locator('#install-top').isVisible(),'Dismissal retains accessible installation options');assert(await page.locator('#install-app').isHidden(),'Consumed native event not reused');
  await page.locator('#install-top').click();assert(await page.locator('#install-guide').evaluate(el=>el.open),'Consumed event falls back to guide');await page.keyboard.press('Escape');
  await offer(true);await page.locator('#install-top').click();await page.waitForFunction(()=>document.getElementById('install-guide').open);
  assert(!await page.locator('#install-top').isDisabled(),'Failed prompt restores usable control');await page.keyboard.press('Escape');
  await offer();await page.locator('#install-app').click();assert(await page.evaluate(()=>installCalls)===1,'Lower button calls same prompt handler');
  await page.evaluate(()=>{window.dispatchEvent(new Event('appinstalled'));resolveInstall({outcome:'accepted'})});
  await page.waitForFunction(()=>!document.getElementById('install-top').disabled);
  assert(await page.locator('#install-top').isHidden()&&await page.locator('#install-app').isHidden(),'Both controls hide after installed event');
  assert((await page.locator('#offline-status').textContent()).startsWith('Installed!'),'Installed state survives prompt resolution');
  const installed=await browser.newContext();await installed.addInitScript(()=>{const nativeMatch=window.matchMedia.bind(window);window.matchMedia=query=>query==='(display-mode: standalone)'?{matches:true}:nativeMatch(query)});
  const app=await installed.newPage();await app.goto(site);assert(await app.locator('#install-top').isHidden(),'Standalone app hides top installer');await installed.close();
  assert(!errors.length,errors.join('; '));const report={checks:['visible top installer','hosted guidance when native prompt absent','keyboard focus restoration','320/360/390/768/1365 header layouts','shared prompt and repeat-click protection','dismissed and failed prompts remain usable','installed and standalone states'],promptTesting:'Synthetic beforeinstallprompt/appinstalled events in real Chrome; no host app installed',errors};
  fs.writeFileSync(path.join(root,'qa/install-report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));await context.close();
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
