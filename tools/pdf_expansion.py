"""Original twelve-card adaptations of works identified in the two PDFs.

The references identify the reading list; linked primary editions supply the
stories and quotation wording. Source PDFs remain local reference material.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read_entries():
    entries = []
    current = None
    for line in (HERE / 'pdf_story_cards.txt').read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        if line.startswith('@'):
            fields = line[1:].split('|')
            if len(fields) != 9:
                raise ValueError(f'Expected nine header fields: {line}')
            current = dict(zip(['title', 'author', 'year', 'era', 'genre', 'setting', 'hook', 'cast', 'source'], fields))
            current.update(scenes=[], note='')
            entries.append(current)
        elif current is None:
            raise ValueError('Card before work header')
        elif line.startswith('?'):
            current['question'], current['answer'] = line[1:].split('|')
        elif line.startswith('!'):
            quote, context, meaning = line[1:].split('|')
            current['quote'] = dict(text=quote, context=context, meaning=meaning)
        elif line.startswith('%'):
            current['note'] = line[1:]
        else:
            fields = line.split('|')
            if len(fields) != 4:
                raise ValueError(f'Expected four card fields: {line}')
            current['scenes'].append(fields)
    titles = [entry['title'] for entry in entries]
    if len(titles) != len(set(titles)):
        raise ValueError('Duplicate PDF addition')
    for entry in entries:
        if len(entry['scenes']) != 12 or not all(k in entry for k in ['quote', 'question', 'answer']):
            raise ValueError(f'Incomplete twelve-card entry: {entry["title"]}')
    return entries


def register(add):
    references = json.loads((HERE / 'pdf_reference_map.json').read_text(encoding='utf-8'))
    for entry in read_entries():
        source = entry['source']
        url = f'https://www.gutenberg.org/ebooks/{source}' if source.isdigit() else source
        frames = '\n'.join('~'.join([title, text, cast, motif, title.upper()]) for title, text, cast, motif in entry['scenes'])
        year = int(entry['year'])
        date = str(year) if year > 1000 else f'c. {year} manuscript; composition uncertain'
        add(entry['title'], entry['author'], year, date, entry['era'], entry['genre'], entry['setting'], entry['hook'], entry['cast'].replace(';', '|'), frames, entry['question'], entry['answer'], source=url, note=entry['note'])
        story = add.last
        story['quotes'] = [dict(**entry['quote'], source=url)]
        story['spoken'] = True
        story['pdfReferences'] = references[story['id']]
        additional_editions = {
            'le-morte-darthur': ['https://www.gutenberg.org/ebooks/1251'],
            'joseph-andrews': ['https://www.gutenberg.org/ebooks/9609'],
            'nineteen-eighty-four': ['https://www.orwellfoundation.com/the-orwell-foundation/orwell/articles/ben-pimlott-introduction-to-nineteen-eighty-four/'],
        }
        if story['id'] in additional_editions:
            story['additionalReferences'] = additional_editions[story['id']]
        if year == 970:
            story['additionalReferences'] = ['https://www.exeter-cathedral.org.uk/learning-collections/explore-the-collections/the-exeter-book/']
        if not story['pdfReferences']:
            raise ValueError(f'No PDF provenance: {story["id"]}')
