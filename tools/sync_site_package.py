"""Copy the validated package into the local release and publication checkout."""
from pathlib import Path
from zipfile import ZipFile
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
text_suffixes={'.js','.json','.py','.txt','.md','.html','.css','.svg','.cjs'}
with ZipFile(ROOT/'website-github-ready.zip') as archive:
    names=archive.namelist()
    assert archive.testzip() is None
    assert len(names)==len(set(names))
    assert 'index.html' in names and 'painted-assets.js' in names
    art=json.loads(archive.read('content/painted-assets.json'))
    expected={record['file'] for record in art['works'].values()}
    assert {name for name in names if name.startswith('assets/painted/')}==expected
    # Validate every destination before writing. No deletion or move is needed.
    destinations=[]
    for base in [ROOT/'website-github-ready',ROOT/'qa/github-publish']:
        resolved_base=base.resolve()
        assert resolved_base.is_relative_to(ROOT.resolve())
        for name in names:
            target=(base/name).resolve()
            assert target.is_relative_to(resolved_base),name
            assert '.git' not in Path(name).parts,name
            destinations.append((base,name,target))
    for base,name,target in destinations:
        data=archive.read(name)
        if base.name=='github-publish' and target.suffix in text_suffixes:
            data=data.decode('utf-8').replace('\r\n','\n').encode('utf-8')
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(data)
        assert target.read_bytes()==data,name
    receipt={'files':len(names),'paintedWorks':len(art['works']),
             'packageSha256':hashlib.sha256((ROOT/'website-github-ready.zip').read_bytes()).hexdigest(),
             'unreviewedPaintingsIncluded':False}
    (ROOT/'qa/package-sync-report.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
