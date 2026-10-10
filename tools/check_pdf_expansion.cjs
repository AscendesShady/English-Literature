const {chromium}=require('C:/Users/ascen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const root=path.resolve(__dirname,'..'),assert=(v,m)=>{if(!v)throw Error(m)};
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 try{
  const page=await browser.newPage({viewport:{width:1365,height:1000},reducedMotion:'reduce'}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));await page.goto(pathToFileURL(path.join(root,'index.html')).href);
  const added=await page.evaluate(()=>STORIES.filter(s=>s.pdfReferences));assert(added.length===60,'Sixty PDF additions');
  const creatures={'the-jungle-book':{Baloo:'bear',Bagheera:'panther',Kaa:'python','Shere Khan':'tiger','Rikki-tikki-tavi':'mongoose',Kotick:'seal'},'the-metamorphosis':{Gregor:'vermin'},'the-war-of-the-worlds':{'The Martians':'martian'}};
  for(const s of added){
   await page.locator(`[data-story="${s.id}"]`).click();assert(await page.locator('#scene-text').textContent()===s.scenes[0].text,'Opening narration '+s.id);
   for(const ref of s.pdfReferences){assert((await page.locator('#source-info').textContent()).includes(ref.document),'PDF provenance '+s.id);}
   await page.locator('#tab-cast').click();
   for(const [name,kind] of Object.entries(creatures[s.id]||{})){assert(await page.locator(`#cast-grid [data-character="${name}"][data-creature="${kind}"]`).count()===1,'Creature portrait '+name);}
   await page.locator('#tab-story').click();await page.locator('[data-scene="11"]').click();assert(await page.locator('#scene-text').textContent()===s.scenes[11].text,'Final narration '+s.id);
   await page.locator('#close-reader').click();
  }
  for(const [id,scene] of [['sultana-s-dream',0],['the-jungle-book',5],['the-metamorphosis',0],['troilus-and-criseyde',0]]){
   for(const width of [1365,360]){
    await page.setViewportSize({width,height:width===360?844:1000});await page.locator(`[data-story="${id}"]`).click();await page.locator(`[data-scene="${scene}"]`).click();
    assert(await page.locator('#reader').evaluate(el=>el.scrollWidth<=el.clientWidth),'No overflow '+id+' '+width);
    await page.screenshot({path:path.join(root,`qa/pdf-expansion/${id}-${width}.png`)});await page.locator('#close-reader').click();
   }
  }
  await page.setViewportSize({width:1365,height:1000});await page.locator('#search').fill('Rokeya');assert(await page.locator('.story-card').count()===1,'Rokeya author search');
  await page.locator('[data-save="sultana-s-dream"]').click();await page.locator('#search').fill('');await page.locator('#saved-button').click();assert(await page.locator('.story-card').count()===1,'Save PDF addition');await page.reload();await page.locator('#saved-button').click();assert(await page.locator('.story-card').count()===1,'New favourite survives reload');
  assert(!errors.length,errors.join('; '));const report={pdfWorks:60,checks:['all new opening and final cards','source PDF labels for all additions','distinct animal and alien portraits','new author search','new favourite persistence','desktop and mobile reader layout'],errors};fs.writeFileSync(path.join(root,'qa/pdf-expansion/browser-report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
