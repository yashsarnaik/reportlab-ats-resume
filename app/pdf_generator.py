import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib import colors
from .schemas import ResumeData

def generate_resume_pdf(data: ResumeData) -> io.BytesIO:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        spaceAfter=8,
        alignment=TA_CENTER
    )
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        spaceAfter=4,
        alignment=TA_CENTER
    )
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        spaceAfter=12,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'HeadingStyle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        spaceAfter=2,
        spaceBefore=10,
        bottomPadding=0,
        alignment=TA_LEFT,
        textTransform='uppercase'
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        spaceAfter=2,
        spaceBefore=2
    )

    right_body_style = ParagraphStyle(
        'RightBodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        spaceAfter=2,
        spaceBefore=2,
        alignment=TA_RIGHT
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leftIndent=12,
        spaceAfter=2,
        spaceBefore=2
    )
    
    story = []
    
    # Header: Name, Title, Contact Info
    story.append(Paragraph(data.name.upper(), name_style))
    story.append(Paragraph(data.title, title_style))
    
    contact_parts = []
    if data.email: contact_parts.append(data.email)
    if data.phone: contact_parts.append(data.phone)
    if data.linkedin: contact_parts.append(data.linkedin)
    if data.website: contact_parts.append(data.website)
    
    if contact_parts:
        contact_str = " | ".join(contact_parts)
        story.append(Paragraph(contact_str, contact_style))
        
    def add_section_heading(title):
        story.append(Paragraph(title, heading_style))
        line = Table([['']], colWidths=[540], style=[
            ('LINEABOVE', (0,0), (-1,0), 1, colors.black),
            ('TOPPADDING', (0,0), (-1,0), 0),
            ('BOTTOMPADDING', (0,0), (-1,0), 0)
        ])
        story.append(line)
        story.append(Spacer(1, 4))
    
    # Summary
    if data.summary:
        add_section_heading("PROFESSIONAL SUMMARY")
        story.append(Paragraph(data.summary, body_style))
        story.append(Spacer(1, 6))
        
    # Experience
    if data.experience:
        add_section_heading("WORK EXPERIENCE")
        for exp in data.experience:
            story.append(Paragraph(f"<b>{exp.role}</b>", body_style))
            
            t = Table(
                [[Paragraph(exp.company, body_style), Paragraph(exp.duration, right_body_style)]],
                colWidths=[400, 140],
                style=[
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('TOPPADDING', (0, 0), (-1, -1), 0),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                    ('LEFTPADDING', (0, 0), (-1, -1), 0),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ]
            )
            story.append(t)
            
            for point in exp.points:
                story.append(Paragraph(f"• {point}", bullet_style))
            story.append(Spacer(1, 8))
            
    # Education
    if data.education:
        add_section_heading("EDUCATION")
        for edu in data.education:
            story.append(Paragraph(f"<b>{edu.degree}</b>", body_style))
            
            t = Table(
                [[Paragraph(edu.institution, body_style), Paragraph(edu.year, right_body_style)]],
                colWidths=[400, 140],
                style=[
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('TOPPADDING', (0, 0), (-1, -1), 0),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                    ('LEFTPADDING', (0, 0), (-1, -1), 0),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ]
            )
            story.append(t)
            story.append(Spacer(1, 8))
            
    # Skills
    if data.skills:
        add_section_heading("SKILLS")
        for skill in data.skills:
            story.append(Paragraph(f"• {skill}", bullet_style))
        story.append(Spacer(1, 8))
        
    # Certifications
    if data.certifications:
        add_section_heading("CERTIFICATIONS")
        for cert in data.certifications:
            story.append(Paragraph(f"• {cert}", bullet_style))
        story.append(Spacer(1, 8))
            
    doc.build(story)
    
    buffer.seek(0)
    return buffer
