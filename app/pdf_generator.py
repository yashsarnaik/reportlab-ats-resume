import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
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
        fontSize=18,
        spaceAfter=6,
        alignment=TA_CENTER
    )
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        spaceAfter=12,
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
        fontSize=14,
        spaceAfter=6,
        spaceBefore=12,
        bottomPadding=0,
        alignment=TA_LEFT
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        spaceAfter=6
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leftIndent=15,
        spaceAfter=3
    )
    
    story = []
    
    # Header: Name, Title, Contact Info
    story.append(Paragraph(data.name.upper(), name_style))
    story.append(Paragraph(data.title, title_style))
    
    contact_parts = []
    if data.email: contact_parts.append(data.email)
    if data.phone: contact_parts.append(data.phone)
    if data.linkedin: contact_parts.append(data.linkedin)
    if data.github: contact_parts.append(data.github)
    if data.website: contact_parts.append(data.website)
    
    if contact_parts:
        contact_str = " | ".join(contact_parts)
        story.append(Paragraph(contact_str, contact_style))
        
    story.append(Spacer(1, 12))
    
    # Summary
    if data.summary:
        story.append(Paragraph("SUMMARY", heading_style))
        story.append(Paragraph(data.summary, body_style))
        
    # Skills
    if data.skills:
        story.append(Paragraph("SKILLS", heading_style))
        skills_str = ", ".join(data.skills)
        story.append(Paragraph(skills_str, body_style))
        
    # Experience
    if data.experience:
        story.append(Paragraph("EXPERIENCE", heading_style))
        for exp in data.experience:
            exp_header = f"<b>{exp.company}</b> - <i>{exp.role}</i> ({exp.duration})"
            story.append(Paragraph(exp_header, body_style))
            
            for point in exp.points:
                story.append(Paragraph(f"• {point}", bullet_style))
            story.append(Spacer(1, 6))
            
    # Projects
    if data.projects:
        story.append(Paragraph("PROJECTS", heading_style))
        for proj in data.projects:
            proj_header = f"<b>{proj.name}</b>"
            story.append(Paragraph(proj_header, body_style))
            
            for point in proj.points:
                story.append(Paragraph(f"• {point}", bullet_style))
            story.append(Spacer(1, 6))
            
    # Education
    if data.education:
        story.append(Paragraph("EDUCATION", heading_style))
        for edu in data.education:
            edu_str = f"<b>{edu.institution}</b> - {edu.degree} ({edu.year})"
            story.append(Paragraph(edu_str, body_style))
            story.append(Spacer(1, 6))
            
    doc.build(story)
    
    buffer.seek(0)
    return buffer
