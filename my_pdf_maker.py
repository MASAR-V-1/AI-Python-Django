import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display

def create_pdf_report(report_text, output_filename="AI_Report.pdf"):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    story = []
    
    # نظام التنسيقات
    styles = getSampleStyleSheet()
    
    # إذا كنت تستخدم نصوصاً إنجليزية فقط حالياً:
    style = styles['Normal']
    clean_text = report_text
    
    # (ملاحظة لدعم العربية مستقبلاً: تحتاج لتسجيل خط كـ TTFont وتمرير النص عبر reshaper و bidi)
    
    story.append(Paragraph(clean_text, style))
    doc.build(story)
    
    return output_filename