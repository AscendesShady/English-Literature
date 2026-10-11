"""Publish reviewed sheets and their exact, persistent scene-key mapping."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--allow-incomplete',action='store_true',help='Build a partial preview; full rollout requires all works.')
    args=parser.parse_args()
    catalog=json.loads((ROOT/'content/catalog.json').read_text(encoding='utf-8'))
    profiles=json.loads((ROOT/'content/character-designs.json').read_text(encoding='utf-8'))
    paintings={}; prompts=[]
    for story in catalog:
        path=ROOT/'qa/painted-illustrations/imports'/f"{story['id']}.json"
        if not path.exists():
            continue
        record=json.loads(path.read_text(encoding='utf-8'))
        if not record['visuallyReviewed'] or record.get('needsCorrection'):
            continue
        assert record['sceneKeys']==[f['key'] for f in story['scenes']],story['id']
        file=ROOT/record['file']
        assert Image.open(file).size==(record['width'],record['height'])
        assert hashlib.sha256(file.read_bytes()).hexdigest()==record['sha256'],f'Reviewed asset changed: {story["id"]}'
        paintings[story['id']]={key:record[key] for key in ['file','width','height','columns','rows','sceneKeys','source','bytes']}
        prompts.append(dict(id=record['id'],source=record['source'],sceneKeys=record['sceneKeys'],originalPrompt=record['prompt'],edits=[record['repairPrompt']] if record.get('repairPrompt') else [],documentedRepair=record.get('repair',''),reviewNote=record.get('reviewNote','')))
    if not args.allow_incomplete:
        assert len(paintings)==len(catalog), f'Only {len(paintings)}/{len(catalog)} sheets visually reviewed.'
    content=dict(schemaVersion=1,style='Original painted book illustrations',
                 policy=profiles['policy'],characters=profiles['traits'],works=paintings)
    (ROOT/'painted-assets.js').write_text('/* Original paintings; stable scene-key mappings. */\nself.PAINTED_ART = '+json.dumps(content,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
    (ROOT/'content/painted-assets.json').write_text(json.dumps(content,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'content/reviewed-painting-prompts.json').write_text(json.dumps(dict(mode='built-in image_gen',works=prompts),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # A changed painting or runtime file must install into a new complete cache.
    files=['index.html','styles.css','app.js','stories.js','painted-assets.js','illustrations.js','pwa.js','manifest.json','literature by codex.docx','assets/favicon.svg']
    files += [p.relative_to(ROOT).as_posix() for p in (ROOT/'assets/icons').glob('*.png')]
    files += [record['file'] for record in paintings.values()]
    digest=hashlib.sha256()
    for name in sorted(files):
        digest.update(name.encode('utf-8'));digest.update((ROOT/name).read_bytes())
    worker=ROOT/'sw.js'
    source=worker.read_text(encoding='utf-8')
    source,count=re.subn(r"const VERSION=PREFIX\+'[^']+';", "const VERSION=PREFIX+'v7-painted-"+digest.hexdigest()[:12]+"';",source)
    assert count==1,'Service worker release identifier'
    worker.write_text(source,encoding='utf-8')
    readme=ROOT/'README.md'
    overview=readme.read_text(encoding='utf-8')
    status=(f'All {len(catalog)} works and {len(catalog)*12} cards have reviewed painted illustrations.' if len(paintings)==len(catalog)
            else f'Painting preview release: {len(paintings)} of {len(catalog)} works, covering {len(paintings)*12} of {len(catalog)*12} cards. The remaining cards retain their symbolic drawings while their paintings are generated or corrected. The complete art rollout and final storytelling engagement review remain unfinished.')
    overview=re.sub(r'<!-- painted-coverage-start -->.*?<!-- painted-coverage-end -->','<!-- painted-coverage-start -->\n'+status+'\n<!-- painted-coverage-end -->',overview,flags=re.S)
    readme.write_text(overview,encoding='utf-8')
    print(f'{len(paintings)} reviewed sheets / {sum(len(p["sceneKeys"]) for p in paintings.values())} painted scenes; {sum(p["bytes"] for p in paintings.values())/1_000_000:.1f} MB.')

if __name__=='__main__':
    main()
