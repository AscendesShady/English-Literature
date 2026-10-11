"""Import an original generated twelve-panel sheet without cropping or retouching.

WebP conversion preserves the composition. Individual panels are clipped in the
browser, so one file supplies all twelve cards and is cached once for a work.
"""
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('identifier')
    parser.add_argument('source',type=Path)
    args=parser.parse_args()
    briefs=json.loads((ROOT/'content/painted-briefs.json').read_text(encoding='utf-8'))
    brief=next(b for b in briefs if b['id']==args.identifier)
    commission=ROOT/'qa/painted-illustrations/commissions'/f'{args.identifier}.json'
    if commission.exists():
        brief=json.loads(commission.read_text(encoding='utf-8'))
    source=args.source.absolute()
    image=Image.open(source).convert('RGB')
    assert image.width>=1200 and image.height>=900, image.size
    assert abs(image.width/image.height-21/16)<.06, image.size
    destination=ROOT/'assets/painted'/f'{args.identifier}.webp'
    destination.parent.mkdir(parents=True,exist_ok=True)
    image.save(destination,quality=84,method=6)
    record=dict(id=brief['id'],title=brief['title'],file=destination.relative_to(ROOT).as_posix(),
                width=image.width,height=image.height,columns=3,rows=4,sceneKeys=brief['sceneKeys'],
                source=brief['source'],reviewedTraits=brief['reviewedTraits'],
                sourceImage=str(source),bytes=destination.stat().st_size,
                sha256=hashlib.sha256(destination.read_bytes()).hexdigest(),
                generator='built-in image_gen',visuallyReviewed=False,prompt=brief['prompt'])
    ledger=ROOT/'qa/painted-illustrations/imports'
    ledger.mkdir(parents=True,exist_ok=True)
    (ledger/f'{args.identifier}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(id=brief['id'],file=record['file'],bytes=record['bytes'],size=image.size)))

if __name__=='__main__':
    main()
