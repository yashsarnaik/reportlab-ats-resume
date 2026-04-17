from fastapi import APIRouter, Response
from .schemas import ResumeData
from .pdf_generator import generate_resume_pdf

router = APIRouter()

@router.post(
    "/generate-resume",
    response_class=Response,
    summary="Generate ATS-Friendly Resume PDF",
    description="Accepts structured JSON containing resume details (experience, education, skills, projects) and returns a dynamically generated ATS-friendly PDF. Suitable for consumption by AI workflows or n8n nodes.",
    response_description="A binary PDF file download containing the formatted resume."
)
def generate_resume(data: ResumeData):
    pdf_buffer = generate_resume_pdf(data)
    pdf_bytes = pdf_buffer.getvalue()
    
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": 'attachment; filename="resume.pdf"'
        }
    )
