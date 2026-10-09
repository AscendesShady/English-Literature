from pathlib import Path
import json
from pdf2image import convert_from_path
from pypdf import PdfReader
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'qa/docx';pdf=out/'literature by codex.pdf'
reader=PdfReader(pdf)
assert len(reader.pages)==147,'Intro and two pages per added work'
assert all(len(p.extract_text())>500 for p in reader.pages),'No near-empty overflow pages'
pages=convert_from_path(pdf,dpi=85,output_folder=str(out),fmt='png',output_file='twelve-scenes',paths_only=True)
for batch in range(0,len(pages),6):
    images=[Image.open(p).convert('RGB') for p in pages[batch:batch+6]]
    w,h=images[0].size;sheet=Image.new('RGB',(w*2,h*3+36*3),'#e8e8e8');draw=ImageDraw.Draw(sheet)
    for j,im in enumerate(images):
        x=(j%2)*w;y=(j//2)*(h+36);draw.text((x+10,y+8),'Page '+str(batch+j+1),fill='black');sheet.paste(im,(x,y+36))
    sheet.save(out/f'review-{batch//6+1:02}.png')
(out/'layout-report.json').write_text(json.dumps({'pages':147,'works':73,'short_overflow_pages':0,'rendered_pages':len(pages),'review_sheets':25},indent=2),encoding='utf-8')
print('Rendered all 147 pages and 25 review sheets')
