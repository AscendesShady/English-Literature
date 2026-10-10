const {chromium}=require('C:/Users/ascen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const root=path.resolve(__dirname,'..'),site=pathToFileURL(path.join(root,'index.html')).href;
const assert=(v,m)=>{if(!v)throw Error(m)};
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const context=await browser.newContext({viewport:{width:1365,height:1000},reducedMotion:'reduce'}),page=await context.newPage(),errors=[];
 page.on('pageerror',e=>errors.push(e.message));await page.goto(site);
 const data=await page.evaluate(()=>STORIES);
 assert(data.length===158,'158 works');assert(data.filter(s=>typeof s.source==='string').length===133,'133 added works');
 assert(data.reduce((n,s)=>n+s.scenes.length,0)===1896,'1896 scenes');
 for(const s of data){
  assert(s.quotes.length===1&&s.quotes[0].context&&s.quotes[0].meaning,'One annotated quotation: '+s.id);
  await page.locator(`[data-story="${s.id}"]`).click();await page.locator('#tab-recall').click();await page.locator('#explore-quotes').click();
  assert(await page.locator('#panel-quotes').isVisible(),'Recall leads to quote');
  assert(await page.locator('.quote-card blockquote').textContent()===s.quotes[0].text,'Exact quotation rendered');
  assert(await page.locator('.quote-card a').getAttribute('href')===s.quotes[0].source,'Source reference rendered');
  await page.locator('#tab-quotes').focus();await page.keyboard.press('ArrowRight');assert(await page.locator('#panel-story').isVisible(),'Fourth tab wraps');await page.keyboard.press('End');assert(await page.locator('#panel-quotes').isVisible(),'End selects quote');
  await page.locator('#close-reader').click();
 }
 await page.evaluate(()=>localStorage.setItem('once-upon-timeline-v1',JSON.stringify({saved:['othello'],remembered:['macbeth'],positions:{othello:4,'to-his-coy-mistress':3}})));
 await page.reload();await page.locator('[data-story="othello"]').click();assert((await page.locator('#scene-number').textContent()).includes('12'),'Original fifth scene migrates to twelfth');await page.locator('#close-reader').click();
 await page.reload();await page.locator('[data-story="othello"]').click();assert((await page.locator('#scene-number').textContent()).includes('12'),'Migration runs only once');await page.locator('#close-reader').click();
 assert(await page.evaluate(()=>JSON.parse(localStorage.getItem('once-upon-timeline-v1')).remembered.includes('macbeth')),'Remembered preserved');
 await page.locator('#saved-button').click();assert(await page.locator('.story-card').count()===1,'Saved shelf preserved');await page.locator('#saved-button').click();
 await page.locator('[data-story="the-love-song-of-j-alfred-prufrock"]').click();await page.locator('#tab-quotes').click();await page.screenshot({path:path.join(root,'qa/quotes-desktop.png')});await page.locator('#close-reader').click();
 for(const width of [360,390,768]){
  await page.setViewportSize({width,height:844});await page.locator('[data-story="pride-and-prejudice"]').click();await page.locator('#tab-quotes').click();
  assert(await page.locator('#reader').evaluate(el=>el.scrollWidth<=el.clientWidth),'Quote layout fits '+width);
  assert(await page.locator('#tab-quotes').evaluate(el=>{const a=el.getBoundingClientRect(),b=el.closest('dialog').getBoundingClientRect();return a.right<=b.right&&a.left>=b.left}),'Four tabs fit '+width);
  await page.screenshot({path:path.join(root,`qa/quotes-${width}.png`)});await page.locator('#close-reader').click();
 }
 assert(!errors.length,errors.join('; '));const report={works:158,added:133,new:60,scenes:1896,quotes:158,checks:['quote panel for every work','exact quote and source rendering','recall-to-quote navigation','four-tab keyboard navigation','legacy reading position migration and reload','saved and remembered preservation','quote layout at 360/390/768'],errors};
 fs.writeFileSync(path.join(root,'qa/expansion-report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
