from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="Resume Builder API",
    description="API to generate ATS-friendly resumes using ReportLab",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Resume Builder API."}


