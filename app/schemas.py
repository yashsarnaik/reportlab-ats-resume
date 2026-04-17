from pydantic import BaseModel, Field
from typing import List, Optional

class Experience(BaseModel):
    role: str = Field(description="Job title/role", example="Marketing Manager")
    company: str = Field(description="Name and location of the company", example="XYZ Corporation, Sydney, NSW")
    duration: str = Field(description="Duration of employment", example="January 2022 - Present")
    points: List[str] = Field(description="List of achievements", example=["Achieved a 35% increase in website traffic..."])

class Education(BaseModel):
    degree: str = Field(description="Degree obtained", example="Bachelor of Marketing")
    institution: str = Field(description="Name and location of the university or institution", example="University of Sydney, Sydney, NSW")
    year: str = Field(description="Graduation year", example="Graduated: 2018")

class ResumeData(BaseModel):
    name: str = Field(description="Full name of the candidate", example="Michael Harris")
    title: str = Field(description="Professional title", example="Digital Marketing | SEO | SEM | Content Marketing")
    email: str = Field(description="Email address", example="michael.harris@email.com")
    phone: str = Field(description="Phone number", example="+61 412 345 678")
    website: Optional[str] = Field(default=None, description="Personal website URL (optional)", example="michaelharris.com")
    linkedin: Optional[str] = Field(default=None, description="LinkedIn profile URL (optional)", example="linkedin.com/in/michaelharris")
    summary: str = Field(description="A brief professional summary", example="Results-oriented marketing professional...")
    skills: List[str] = Field(description="List of technical or professional skills", example=["Digital Marketing Strategy", "SEO & SEM"])
    experience: List[Experience] = Field(default_factory=list, description="List of past work experience")
    education: List[Education] = Field(default_factory=list, description="List of educational qualifications")
    certifications: List[str] = Field(default_factory=list, description="List of certifications")

