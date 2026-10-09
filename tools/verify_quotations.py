"""Read-only source comparison for the short Gutenberg excerpts."""
import concurrent.futures,html,json,re,unicodedata,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
cache=ROOT/'qa/quote-sources';cache.mkdir(parents=True,exist_ok=True)
def norm(s):
    return ' '.join(re.findall(r'\w+',unicodedata.normalize('NFKD',s.replace('_','')).lower()))
def check(s):
    q=s['quotes'][0];m=re.fullmatch(r'https://www.gutenberg.org/ebooks/(\d+)',q['source'])
    if not m:return dict(id=s['id'],status='separate-reference',source=q['source'])
    number=m[1];target=cache/(number+'.txt')
    try:
        if target.exists():text=target.read_text(encoding='utf-8')
        else:
            url=f'https://www.gutenberg.org/cache/epub/{number}/pg{number}.txt'
            text=urllib.request.urlopen(url,timeout=45).read().decode('utf-8-sig')
            target.write_text(text,encoding='utf-8')
        ok=norm(q['text']) in norm(text)
        words=re.findall(r'\w+',q['text']);needle=' '.join(words[:3])
        matches=list(re.finditer(r'\s+'.join(re.escape(w) for w in words[:3]),text,re.I))
        snippets=[text[max(0,m.start()-50):m.end()+180].replace('\n',' ') for m in matches[:3]]
        return dict(id=s['id'],status='matched' if ok else 'REVIEW',quote=q['text'],source=q['source'],snippets=snippets)
    except Exception as e:return dict(id=s['id'],status='ERROR',error=str(e))
stories=json.loads((ROOT/'content/catalog.json').read_text(encoding='utf-8'))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(check,stories))
(ROOT/'qa/quotation-verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
for r in results:
    if r['status'] in ['REVIEW','ERROR']: print(json.dumps(r,ensure_ascii=False))
print({status:sum(r['status']==status for r in results) for status in sorted({r['status'] for r in results})})
