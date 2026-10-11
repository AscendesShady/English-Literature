"""Save the exact remaining work without marking incomplete artwork finished."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/'content/catalog.json').read_text(encoding='utf-8'))
imports=ROOT/'qa/painted-illustrations/imports'
approved=[]; corrections=[]; missing=[]; unreviewed=[]
for story in catalog:
    file=imports/(story['id']+'.json')
    if not file.exists():
        missing.append(story['id']);continue
    record=json.loads(file.read_text(encoding='utf-8'))
    if record.get('needsCorrection'):
        corrections.append({'id':story['id'],'sourceImage':record['sourceImage'],'file':record['file'],'note':record.get('reviewNote','See pending-corrections.json for exact prompt.')})
    elif record['visuallyReviewed']:
        approved.append(story['id'])
    else:
        unreviewed.append(story['id'])
report={'style':'Detailed painted book illustrations with consistent characters','totalWorks':len(catalog),'approvedWorks':approved,'approvedScenes':len(approved)*12,'corrections':corrections,'missingWorks':missing,'unreviewedWorks':unreviewed,'imageGenerationBlockedBy':'Daily built-in image generation limit','retryAfterUtc':'2026-10-11T13:35:01Z','publication':'User subsequently requested commit and push now: publish only the approved preview, clearly labelled incomplete. Full illustrations and final narration engagement review remain pending.','nextSteps':['Correct flagged existing sheets and verify source-specific appearances','Generate remaining work commissions without repeatedly retrying a usage-limit error','Visually review twelve panels and the named people in every sheet','Build full reviewed manifest, browser/offline checks and final package','Complete human narration review and synchronize any changed companion-document paragraphs','Commit, push and verify remote/live assets']}
folder=ROOT/'qa/painted-illustrations'
(folder/'progress.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'approvedWorks':len(approved),'approvedScenes':report['approvedScenes'],'correctionSheets':len(corrections),'missingSheets':len(missing),'unreviewedSheets':len(unreviewed)}))
