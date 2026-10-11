const {chromium}=require('C:/Users/ascen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const root=path.resolve(__dirname,'..'),assert=(v,m)=>{if(!v)throw Error(m)};
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true}),page=await browser.newPage({viewport:{width:1365,height:1000},reducedMotion:'reduce'}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));await page.goto(pathToFileURL(path.join(root,'index.html')).href);
 const manifest=await page.evaluate(()=>PAINTED_ART),catalog=await page.evaluate(()=>STORIES),ids=Object.keys(manifest.works);
 assert(ids.length>0,'Painted manifest');if(!process.argv.includes('--allow-incomplete'))assert(ids.length===catalog.length,'All works painted');
 let scenes=0;
 for(const id of ids){
  const s=catalog.find(s=>s.id===id),art=manifest.works[id];assert(s&&art.sceneKeys.length===12,'Twelve scenes '+id);
  assert(fs.existsSync(path.join(root,art.file)),'Local painting '+id);
  await page.locator('[data-story="'+id+'"]').click();
  assert(await page.evaluate(async file=>{const im=new Image();im.src=file;await im.decode();return im.naturalWidth>0},art.file),'Chrome image decode '+id);
  const panels=new Set();
  for(let i=0;i<12;i++){
   await page.locator('[data-scene="'+i+'"]').click();const svg=page.locator('#scene-art > svg'),im=svg.locator('image');
   assert(await svg.getAttribute('data-artwork')==='painted','Painted scene '+id);
   assert(await svg.getAttribute('data-scene-key')===s.scenes[i].key,'Stable scene identity');
   assert((await svg.getAttribute('aria-label')).includes(s.scenes[i].text),'Text alternative');
   assert(await im.getAttribute('href')===art.file,'Work-specific asset');
   panels.add((await im.getAttribute('x'))+','+(await im.getAttribute('y')));scenes++;
  }
  assert(panels.size===12,'Distinct panels '+id);
  await page.locator('#tab-cast').click();assert(await page.locator('.cast-card').count()===s.characters.length,'Complete cast');
  if(await page.locator('.cast-scene').count()){await page.locator('.cast-scene').first().click();assert(await page.locator('#panel-story').isVisible(),'Cast related scene link');}
  await page.locator('#close-reader').click();
 }
 for(const width of [1365,768,390,360,320]){
  await page.setViewportSize({width,height:900});await page.locator('[data-story="sultana-s-dream"]').click();
  assert(await page.locator('#reader').evaluate(el=>el.scrollWidth<=el.clientWidth),'Reader fits '+width);
  await page.screenshot({path:path.join(root,'qa/painted-illustrations/reader-'+width+'.png')});
  await page.locator('#tab-cast').click();assert(await page.locator('#reader').evaluate(el=>el.scrollWidth<=el.clientWidth),'Cast descriptions fit');
  await page.locator('#close-reader').click();
 }
 assert(!errors.length,errors.join('; '));const report={works:ids.length,scenes,totalWorks:catalog.length,errors};
 fs.writeFileSync(path.join(root,'qa/painted-illustrations/browser-report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
