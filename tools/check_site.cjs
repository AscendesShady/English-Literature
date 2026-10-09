const { chromium }=require('C:/Users/ascen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const root=path.resolve(__dirname,'..'),qa=path.join(root,'qa');fs.mkdirSync(qa,{recursive:true});
const assert=(value,message)=>{if(!value)throw Error(message);};
(async()=>{
 const browser=await chromium.launch({headless:true,channel:'chrome'});
 const context=await browser.newContext({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
 const page=await context.newPage(),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(pathToFileURL(path.join(root,'index.html')).href);await page.waitForSelector('.story-card');await page.screenshot({path:path.join(qa,'desktop.png')});
 assert(await page.locator('.story-card').count()===98,'All 98 cards');
 const stories=await page.evaluate(()=>STORIES.map(s=>({id:s.id,count:s.scenes.length,title:s.title,era:s.era})));
 let scenes=0;
 for(const story of stories){
   await page.locator(`[data-story="${story.id}"]`).click();assert(await page.locator('#reader').evaluate(el=>el.open),'Reader opens');assert(await page.locator('#reader-title').textContent()===story.title,'Correct title');
   for(let i=0;i<story.count;i++){
     await page.locator(`[data-scene="${i}"]`).click();assert((await page.locator('#scene-number').textContent()).includes(String(i+1).padStart(2,'0')),'Correct scene');
     assert((await page.locator('#scene-text').textContent()).length>40,'Narrative present');assert(await page.locator('#scene-art svg').count()===1,'Scene artwork');scenes++;
   }
   await page.locator('#next').click();assert(await page.locator('#panel-recall').isVisible(),'End opens recall');
   await page.locator('#reveal-answer').click();assert(await page.locator('#recall-answer').isVisible(),'Recall answer revealed');
   await page.locator('#mark-read').click();await page.locator('#tab-cast').click();assert(await page.locator('.cast-card').count()>1,'Cast guide');
   await page.locator('#close-reader').click();
 }
 for(const era of [...new Set(stories.map(s=>s.era))]){await page.locator(`[data-era="${era}"]`).click();assert(await page.locator('.story-card').count()===stories.filter(s=>s.era===era).length,'Era filter '+era);}
 await page.locator('[data-era="all"]').click();await page.locator('#search').fill('Wiglaf');assert(await page.locator('.story-card').count()===1,'Character search');await page.locator('#search').fill('nonsense-no-results');assert(await page.locator('#empty').isVisible(),'Empty search');await page.locator('#clear-filter').click();
 await page.locator('[data-save="macbeth"]').click();await page.locator('#saved-button').click();assert(await page.locator('.story-card').count()===1,'Saved shelf');await page.reload();await page.locator('#saved-button').click();assert(await page.locator('.story-card').count()===1,'Saved persistence');
 await page.locator('[data-story="macbeth"]').click();assert((await page.locator('#scene-number').textContent()).includes('12'),'Scene persistence');await page.locator('#tab-story').focus();await page.keyboard.press('ArrowRight');assert(await page.locator('#panel-cast').isVisible(),'Keyboard tab navigation');await page.keyboard.press('Escape');assert(!(await page.locator('#reader').evaluate(el=>el.open)),'Escape closes');
 await page.goto(pathToFileURL(path.join(root,'index.html')).href+'#story/the-odyssey/3');await page.waitForFunction(()=>document.getElementById('reader-title').textContent==='The Odyssey'&&document.getElementById('scene-number').textContent.includes('03'));assert((await page.locator('#scene-number').textContent()).includes('03'),'Direct scene link');await page.locator('#previous').click();assert((await page.locator('#scene-number').textContent()).includes('02'),'Previous scene');await page.keyboard.press('ArrowRight');assert((await page.locator('#scene-number').textContent()).includes('03'),'Keyboard next scene');await page.screenshot({path:path.join(qa,'reader-desktop.png')});await page.locator('#close-reader').click();
 for(const width of [360,390,768]){
   await page.setViewportSize({width,height:844});await page.evaluate(()=>scrollTo(0,0));
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'No overflow at '+width);await page.screenshot({path:path.join(qa,`mobile-${width}.png`),fullPage:true});
   await page.locator('[data-story="macbeth"]').click();assert(await page.locator('#next').isVisible(),'Mobile reader controls');assert(await page.locator('#reader').evaluate(el=>el.scrollWidth<=el.clientWidth),'No reader overflow');await page.screenshot({path:path.join(qa,`reader-${width}.png`)});await page.locator('#close-reader').click();
 }
 const offline=await browser.newContext({viewport:{width:1280,height:900},offline:true});const offlinePage=await offline.newPage();await offlinePage.goto(pathToFileURL(path.join(root,'index.html')).href);assert(await offlinePage.locator('.story-card').count()===98,'Offline functionality');await offline.close();
 assert(errors.length===0,'No JavaScript exceptions: '+errors.join('; '));
 const report={stories:stories.length,scenes,eras:8,checks:['every scene and cast','recall and completion','era filters','character search','empty search','saved shelf persistence','reading position persistence','keyboard tabs and page navigation','direct scene links','360/390/768 responsive overflow','offline local file'],errors};fs.writeFileSync(path.join(qa,'site-report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
