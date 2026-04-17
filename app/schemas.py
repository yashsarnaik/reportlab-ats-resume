from pydantic import BaseModel, Field
from typing import List, Optional

class Experience(BaseModel):
    company: str = Field(description="Name of the company", example="Google")
    role: str = Field(description="Job title/role", example="Senior Software Engineer")
    duration: str = Field(description="Duration of employment (e.g., '2020 - Present' or 'Jan 2018 - Dec 2019')", example="2020 - Present")
    points: List[str] = Field(description="List of achievements or responsibilities as bullet points", example=["Improved performance by 20%", "Led a backend team"])

class Project(BaseModel):
    name: str = Field(description="Name of the project", example="Resume Builder API")
    points: List[str] = Field(description="List of key features or achievements in the project", example=["Developed a self-hosted API", "Integrated with ReportLab"])

class Education(BaseModel):
    institution: str = Field(description="Name of the university or institution", example="Stanford University")
    degree: str = Field(description="Degree obtained", example="B.S. in Computer Science")
    year: str = Field(description="Graduation year", example="2022")

class ResumeData(BaseModel):
    name: str = Field(description="Full name of the candidate", example="Jane Doe")
    title: str = Field(description="Professional title", example="Backend Engineer")
    email: str = Field(description="Email address", example="jane@example.com")
    phone: str = Field(description="Phone number", example="+1-555-555-5555")
    website: Optional[str] = Field(default=None, description="Personal website URL (optional)", example="janedoe.com")
    linkedin: Optional[str] = Field(default=None, description="LinkedIn profile URL (optional)", example="linkedin.com/in/janedoe")
    github: Optional[str] = Field(default=None, description="GitHub profile URL (optional)", example="github.com/janedoe")
    summary: str = Field(description="A brief professional summary or objective", example="Passionate backend engineer with 5 years of experience in Python and APIs.")
    skills: List[str] = Field(description="List of technical or professional skills", example=["Python", "FastAPI", "Docker", "ReportLab"])
    experience: List[Experience] = Field(default_factory=list, description="List of past work experience")
    projects: List[Project] = Field(default_factory=list, description="List of personal or professional projects")
    education: List[Education] = Field(default_factory=list, description="List of educational qualifications")

