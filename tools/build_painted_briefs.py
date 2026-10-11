"""Build stable, one-work illustration commissions from existing scene keys.

One original painted sheet contains a work's twelve ordered panels. The browser
shows the matching panel, never a random stock photograph or another scene.
"""
import json
from pathlib import Path
from build_art_dossiers import source_text

ROOT = Path(__file__).resolve().parents[1]

STYLE = '''Create ONE original detailed painted book illustration sheet, EXACTLY twelve equal LANDSCAPE panels arranged in a strict 3-column by 4-row grid, reading left to right top to bottom. Each panel 7:4; overall ratio 21:16. Highest practical image resolution. No text, labels, numbers, speech balloons, gutters or framing. Natural human anatomy and individually expressive faces, rich watercolor/gouache texture, atmospheric light, carefully observed period architecture and useful narrative detail. This is literature illustration, not a movie poster, cartoon, collage of photographs or twelve portraits posing in front of the same background. Vary camera angle and composition as actions change. A person has the SAME recognisable face, body proportions, eye/hair/skin colours through a work unless the narrative explicitly changes appearance, ages them, gives a disguise or transforms them. Stage the action described in each panel: use the accompanying cast list as an identity guide, not an instruction that every listed person must always be visible. Show only people who actually attend the chosen moment. Do not insert an absent character, make a dead character physically present later, relocate a death or arrest, or turn a remembered event into a literal encounter. If a paragraph spans several times or places, choose one stated moment and keep only the people present there. Keep exactly twelve panels: no extra subdivisions or four-column final row. Show concrete settings, objects, gestures and consequences. Some cards explain poetry or argument: illustrate the precise imagery being discussed rather than inventing extra plot. Collections can change cast and setting between separate tales. Portray violence, death and sexual coercion indirectly and without gore or sexualised minors. All people clothed or safely draped. No racial caricatures or class-based change of complexion. Never copy an actor, film design or contemporary cover art. Unspecified physical attributes and historical clothing are artistic interpretations, not author-supplied facts. Do not assign exact heights, ages, hair/eye/skin colours or modern race labels merely because a name, nationality or era suggests them. Distinguish human skin, animal fur and supernatural anatomy. Source-based traits listed below take precedence over familiar screen adaptations.'''

def main():
    catalog = json.loads((ROOT/'content/catalog.json').read_text(encoding='utf-8'))
    designs = json.loads((ROOT/'content/character-designs.json').read_text(encoding='utf-8'))
    directions=json.loads((ROOT/'content/scene-art-directions.json').read_text(encoding='utf-8'))
    briefs=[]; verified=0
    for story in catalog:
        primary, text = source_text(story)
        reviewed=designs['traits'].get(story['id'], {})
        names={c['name'] for c in story['characters']}
        assert set(reviewed).issubset(names), (story['id'], set(reviewed)-names)
        for name,profile in reviewed.items():
            for anchor in profile['anchors']:
                assert anchor.casefold() in text.casefold(), (story['id'], name, anchor)
            verified+=1
        cast='\n'.join(c['name']+': '+c['role']+'. '+reviewed.get(c['name'],{}).get('description','Additional physical appearance is artistic interpretation; preserve a consistent design suitable to this story and role.') for c in story['characters'])
        visual=directions.get(story['id'],[f['text'] for f in story['scenes']])
        assert len(visual)==len(story['scenes']),story['id']
        panels='\n'.join(f"Panel {i}: {f['title']}. {direction}" for i,(f,direction) in enumerate(zip(story['scenes'],visual),1))
        prompt=STYLE+f"\nWORK: {story['title']} by {story['author']}.\nSETTING: {story['setting']}. Publication date {story['date']} is NOT necessarily the time of the action.\nEDITORIAL NOTE: {story['note']}\nCAST: \n{cast}\nTWELVE PANELS IN EXACT ORDER:\n{panels}\nCheck that the result contains twelve separate complete scenes in a 3x4 grid, with unchanged named character identities, each panel illustrating its own action."
        briefs.append(dict(id=story['id'],title=story['title'],source=primary,
                           sceneKeys=[f['key'] for f in story['scenes']],
                           reviewedTraits=reviewed,prompt=prompt))
    out=ROOT/'content/painted-briefs.json'
    out.write_text(json.dumps(briefs,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(briefs)} complete commissions covering {sum(len(b["sceneKeys"]) for b in briefs)} scenes; {verified} reviewed physical profiles with primary-text anchors.')

if __name__=='__main__':
    main()
