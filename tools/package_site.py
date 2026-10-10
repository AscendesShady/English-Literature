from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json

root=Path(__file__).resolve().parents[1]
files=['index.html','styles.css','app.js','stories.js','illustrations.js','pwa.js','sw.js','manifest.json','literature by codex.docx','README.md','.nojekyll','assets/favicon.svg','assets/app-icon.svg','assets/icons/icon-192.png','assets/icons/icon-512.png','assets/icons/icon-maskable-512.png','assets/icons/apple-touch-icon.png','content/catalog.json','tools/build_content.py','tools/build_document.py','tools/additions_50.py','tools/additions_romantic.py','tools/additions_modern.py','tools/expand_originals.py','tools/quotations.py','tools/additions_20.py','tools/additions_20_poems.py','tools/twelve_scenes.py','tools/package_site.py','tools/build_icons.cjs']
out=root/'website-github-ready.zip'
files += ['tools/narrative_rewrite.py','tools/narrative_cards.txt']
files += ['tools/pdf_expansion.py','tools/pdf_story_cards.txt','tools/pdf_reference_map.json','content/pdf-additions.md']
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
