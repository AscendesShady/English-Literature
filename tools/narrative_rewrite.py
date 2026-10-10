"""Apply individually authored narration after the twelve-scene assembly.

The plain-text file is the editorial source: one @id|hook header followed by
exactly twelve paragraphs. Scene identities and illustration metadata stay in
the existing content pipeline, so saved reading positions remain stable.
"""
from pathlib import Path


def read_narratives():
    entries = {}
    current = None
    path = Path(__file__).with_name('narrative_cards.txt')
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        if line.startswith('@'):
            identifier, hook = line[1:].split('|', 1)
            if identifier in entries:
                raise ValueError(f'Duplicate narrative: {identifier}')
            current = {'hook': hook, 'scenes': []}
            entries[identifier] = current
        elif current is None:
            raise ValueError('Paragraph before narrative header')
        else:
            current['scenes'].append(line)
    for identifier, entry in entries.items():
        if len(entry['scenes']) != 12:
            raise ValueError(f'{identifier}: expected 12 paragraphs, got {len(entry["scenes"])}')
    return entries


def rewrite(stories):
    entries = read_narratives()
    identifiers = {s['id'] for s in stories}
    if identifiers != set(entries):
        raise ValueError(f'Narrative coverage differs: {identifiers ^ set(entries)}')
    for story in stories:
        entry = entries[story['id']]
        story['hook'] = entry['hook']
        for frame, paragraph in zip(story['scenes'], entry['scenes'], strict=True):
            frame['text'] = paragraph
        # Original document provenance and quotation editions are retained.
        # These are reading references, not claims of a fresh full-text audit.
        story['narrativeReference'] = story['source'] if isinstance(story['source'], str) else story['quotes'][0]['source']
        story['contentVersion'] = 4
