from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--preview',action='store_true',help='Package only approved paintings with existing drawings for pending works; explicit preview release.')
args=parser.parse_args()

root=Path(__file__).resolve().parents[1]
files=['index.html','styles.css','app.js','stories.js','illustrations.js','pwa.js','sw.js','manifest.json','literature by codex.docx','README.md','.nojekyll','assets/favicon.svg','assets/app-icon.svg','assets/icons/icon-192.png','assets/icons/icon-512.png','assets/icons/icon-maskable-512.png','assets/icons/apple-touch-icon.png','content/catalog.json','tools/build_content.py','tools/build_document.py','tools/additions_50.py','tools/additions_romantic.py','tools/additions_modern.py','tools/expand_originals.py','tools/quotations.py','tools/additions_20.py','tools/additions_20_poems.py','tools/twelve_scenes.py','tools/package_site.py','tools/build_icons.cjs']
out=root/'website-github-ready.zip'
files += ['tools/narrative_rewrite.py','tools/narrative_cards.txt']
files += ['tools/pdf_expansion.py','tools/pdf_story_cards.txt','tools/pdf_reference_map.json','content/pdf-additions.md']
painted=json.loads((root/'content/painted-assets.json').read_text(encoding='utf-8'))
catalog=json.loads((root/'content/catalog.json').read_text(encoding='utf-8'))
assert set(painted['works'])<={s['id'] for s in catalog},'Unknown painted work.'
if not args.preview:
    assert set(painted['works'])=={s['id'] for s in catalog},'Full release requires paintings for every work. Use --preview only for an explicitly requested preview release.'
files += ['painted-assets.js','content/painted-assets.json','content/character-designs.json','content/scene-art-directions.json','content/painted-briefs.json','tools/build_art_dossiers.py','tools/build_painted_briefs.py','tools/import_painted_sheet.py','tools/build_painted_assets.py','tools/check_painted_art.cjs']
files += [record['file'] for record in painted['works'].values()]
files += ['content/reviewed-painting-prompts.json','tools/audit_narration.py','tools/checkpoint_painted_work.py']
files += ['tools/sync_site_package.py','tools/check_site.cjs','tools/check_expansion.cjs','tools/check_extras.cjs','tools/check_pwa.cjs','tools/check_install.cjs','tools/check_pdf_expansion.cjs']
assert len(files)==len(set(files))
with ZipFile(out,'w',ZIP_DEFLATED) as z:
    for name in files:
        assert (root/name).is_file(),name
        z.write(root/name,name)
with ZipFile(out) as z:
    assert z.testzip() is None
    assert all(n in z.namelist() for n in files)
catalog=json.loads((root/'content/catalog.json').read_text(encoding='utf-8'))
assert len({s['id'] for s in catalog})==158
assert len([s for s in catalog if isinstance(s['source'],str)])==133
assert all(len(s['scenes'])==12 for s in catalog)
assert sum(len(s['scenes']) for s in catalog)==1896
assert all(len(s['quotes'])==1 and all(s['quotes'][0][key] for key in ['text','context','meaning','source']) for s in catalog)
assert all(all(name in {c['name'] for c in s['characters']} for name in f['cast']) for s in catalog for f in s['scenes'])
assert all(len({f['key'] for f in s['scenes']})==12 for s in catalog)
manifest=json.loads((root/'manifest.json').read_text(encoding='utf-8'))
assert manifest['display']=='standalone' and manifest['scope']=='./'
assert all(i['src'] in files for i in manifest['icons'])
print(f'Validated {len(files)} packaged files, {len(catalog)} works, {sum(len(s["scenes"]) for s in catalog)} scenes, {len(catalog)} quotations and PWA assets. ZIP size: {out.stat().st_size:,} bytes.')
