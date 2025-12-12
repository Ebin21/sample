from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

with open('MSC_CA_Exam_All_Questions.md', 'r', encoding='utf-8') as f:
    content = f.read()

doc = SimpleDocTemplate('Research-Methodology.pdf', pagesize=A4,
                       rightMargin=0.75*inch, leftMargin=0.75*inch)

styles = getSampleStyleSheet()
story = []

for line in content.split('\n'):
    if not line.strip():
        story.append(Spacer(1, 0.08*inch))
    elif line.startswith('# '):
        story.append(Paragraph(line.replace('# ', ''), styles['Heading1']))
    elif line.startswith('## '):
        story.append(Paragraph(line.replace('## ', ''), styles['Heading2']))
    elif line.strip():
        story.append(Paragraph(line, styles['Normal']))

doc.build(story)
print("✓ PDF Created: Research-Methodology.pdf")
