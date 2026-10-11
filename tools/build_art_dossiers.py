"""Collect primary-text research for the painted illustration commissioning pass.

The nearby passages are research candidates, not verified character attributes.
They stay in qa; only an editorially reviewed design should enter public assets.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / 'qa/quote-sources'
OUT = ROOT / 'qa/painted-illustrations'
OUT.mkdir(parents=True, exist_ok=True)
APPEARANCE = re.compile(r'\b(tall|short|height|stature|complexion|skin|hair|eyes|beard|slender|broad|lame|scar|dress|coat|gown|fair|dark|pale|black|brown|yellow|white|red|golden|blue|green|grey|gray|handsome|beautiful|young|old|aged|years)\b', re.I)


def source_text(story):
    urls = [story.get('narrativeReference'), story.get('source'), story['quotes'][0]['source']]
    for url in urls:
        if not isinstance(url, str):
            continue
        match = re.search(r'gutenberg\.org/(?:ebooks/|files/|cache/epub/)(\d+)', url)
        target = CACHE / (match[1] + '.txt') if match else CACHE / (story['id'] + '.html')
        if not target.exists():
            continue
        text = target.read_text(encoding='utf-8')
        if target.suffix == '.html':
            text = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', text, flags=re.S | re.I)
            text = html.unescape(re.sub(r'<[^>]+>', ' ', text))
        if len(text) < 1000 or 'captcha' in text[:1000].lower():
            continue
        return url, ' '.join(text.split())
    return story.get('narrativeReference'), ''


def candidates(character, text):
    name = character['name']
    terms = [name]
    if len(name.split()) > 1 and not name.startswith('The '):
        terms.append(name.split()[-1])
    if name == 'The creature':
        terms = ['yellow skin', 'eight feet', 'lustrous black']
    if name.startswith('The ') and name not in ['The creature', 'The Queen']:
        return []
    found = []
    for term in terms:
        for match in re.finditer(r'\b' + re.escape(term) + r'\b', text, re.I):
            passage = text[max(0, match.start() - 140):match.end() + 330]
            score = len(APPEARANCE.findall(passage))
            if score >= 3:
                found.append((score, match.start(), passage))
    selected = []
    for score, offset, passage in sorted(found, reverse=True):
        if all(abs(offset - prior['offset']) > 300 for prior in selected):
            selected.append(dict(offset=offset, score=score, passage=passage))
        if len(selected) == 4:
            break
    return selected


def main():
    catalog = json.loads((ROOT / 'content/catalog.json').read_text(encoding='utf-8'))
    result = []
    for story in catalog:
        source, text = source_text(story)
        result.append(dict(id=story['id'], title=story['title'], source=source,
                           primaryTextAvailable=bool(text), setting=story['setting'],
                           characters=[dict(**c, candidates=candidates(c, text)) for c in story['characters']],
                           scenes=[dict(key=f['key'], title=f['title'], text=f['text'], cast=f['cast']) for f in story['scenes']]))
    (OUT / 'research-candidates.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = []
    for story in result:
        lines.append('\n@' + story['title'])
        for c in story['characters']:
            lines.append(c['name'] + ': ' + (c['candidates'][0]['passage'] if c['candidates'] else '[no shortlisted appearance passage]'))
    (OUT / 'research-candidates.txt').write_text('\n'.join(lines), encoding='utf-8')
    print(f"Research candidates: {len(result)} works, {sum(len(s['characters']) for s in result)} characters; {sum(s['primaryTextAvailable'] for s in result)} cached primary editions. No candidate is automatically treated as a verified trait.")


if __name__ == '__main__':
    main()
