const fs=require('fs'),path=require('path');
const sharp=require('C:/Users/ascen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=path.resolve(__dirname,'..'),dir=path.join(root,'assets/icons');fs.mkdirSync(dir,{recursive:true});
(async()=>{
 const src=fs.readFileSync(path.join(root,'assets/app-icon.svg'));
 for(const [name,size] of [['icon-192.png',192],['icon-512.png',512],['apple-touch-icon.png',180]])await sharp(src).resize(size,size).png().toFile(path.join(dir,name));
 const mark=await sharp(src).resize(384,384).png().toBuffer();
 await sharp({create:{width:512,height:512,channels:4,background:'#334d40'}}).composite([{input:mark,left:64,top:64}]).png().toFile(path.join(dir,'icon-maskable-512.png'));
 console.log('Built 192px, 512px, maskable and Apple icons from the storybook mark.');
})().catch(e=>{console.error(e);process.exit(1)});
