"""Prepare an editorial review queue; heuristics are not engagement scores."""
import json
import re
import statistics
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/'content/catalog.json').read_text(encoding='utf-8'))
stop=set('a an the of to in on at for and or but if as is are was were be been has have had he she they it his her their that this these those with from into by not no one another'.split())
sentences=defaultdict(list)
lengths=[]
adjacent=[]
long=[]
abstract=[]
for story in catalog:
    previous=None
    for i,frame in enumerate(story['scenes']):
        words=re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?",frame['text'])
        lengths.append(len(words))
        terms={w.lower() for w in words if w.lower() not in stop}
        if previous:
            overlap=len(terms&previous)/max(1,len(terms|previous))
            if overlap>=.4:
                adjacent.append({'work':story['id'],'scenes':[i,i+1],'overlap':round(overlap,3),'keys':[story['scenes'][i-1]['key'],frame['key']]})
        previous=terms
        if len(words)>65:
            long.append({'work':story['id'],'scene':i+1,'key':frame['key'],'words':len(words)})
        if sum(w.lower() in {'argument','speaker','poem','voice','meaning','belief','understanding','experience','recognition'} for w in words)>=4:
            abstract.append({'work':story['id'],'scene':i+1,'key':frame['key'],'text':frame['text']})
        for sentence in re.split(r'(?<=[.!?])\s+',frame['text']):
            if len(sentence.split())>=7:
                sentences[sentence].append({'work':story['id'],'key':frame['key']})

duplicates=[{'sentence':s,'occurrences':refs} for s,refs in sentences.items() if len({r['work'] for r in refs})>1]
report={'stage':'Editorial triage prepared; human engagement review remains pending until the illustrations are complete.',
        'works':len(catalog),'scenes':len(lengths),'cardWords':{'minimum':min(lengths),'median':statistics.median(lengths),'maximum':max(lengths)},
        'repeatedSentencesAcrossWorks':duplicates,'adjacentCardsToReview':adjacent,
        'longCardsToReview':long,'abstractCardsToReview':abstract,
        'manualFindings':[{'work':'hamlet','scenes':[9,10],'issue':'The funeral is introduced before the Yorick conversation; clarify the chronology while preserving scene keys and matching the final paintings.'},
                          {'work':'a-midsummer-night-s-dream','scenes':[10,12],'issue':'Make Bottom restoration to human form explicit before the wedding performance; the current short account restores the lovers but omits this transition.'}],
        'checklist':['Opening establishes who, place and stakes','Each card advances an action, image or argument','Unfamiliar concepts receive plain explanations','Transitions connect causes to consequences','Hooks come from the work rather than repeated generic questions','Poems and collections retain separate voices','Ending is faithful and leads into recall']}
out=ROOT/'qa/narration-review'
out.mkdir(exist_ok=True)
(out/'editorial-queue.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'works':report['works'],'scenes':report['scenes'],'words':report['cardWords'],'repeatedSentences':len(duplicates),'adjacentPairs':len(adjacent),'longCards':len(long),'abstractCards':len(abstract),'stage':report['stage']}))
