# ATS-Friendly Resume Builder

A FastAPI service to dynamically generate ATS-friendly resume PDFs from structured JSON data.

## Requirements

*   [uv](https://github.com/astral-sh/uv) (for dependency management)
*   Python 3.11+
*   Docker (for containerized deployment)

## Setup Locally

1. Create a virtual environment using `uv`:
   ```bash
   uv venv
   ```

2. Activate the virtual environment:
   ```bash
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

4. Run the server locally:
   ```bash
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

## Docker Deployment

Build the Docker image:
```bash
docker build -t resume-builder .
```

Run the container:
```bash
docker run -p 8000:8000 resume-builder
```

## Usage

Send a POST request to `/generate-resume` to generate a PDF.

### Sample `curl` Request

```bash
curl -X POST http://127.0.0.1:8000/generate-resume \
-H "Content-Type: application/json" \
-d '{
  "name": "Jane Doe",
  "title": "Senior Backend Engineer",
  "email": "jane@example.com",
  "phone": "+1-555-555-5555",
  "website": "janedoe.com",
  "linkedin": "linkedin.com/in/janedoe",
  "github": "github.com/janedoe",
  "summary": "Experienced backend engineer with a strong track record of designing scalable systems and driving team success. Passionate about Python, cloud architecture, and building data-driven products.",
  "skills": [
    "Python", "FastAPI", "Docker", "PostgreSQL", "AWS"
  ],
  "experience": [
    {
      "company": "Tech Corp",
      "role": "Senior Engineer",
      "duration": "2020 - Present",
      "points": [
        "Architected scalable microservices.",
        "Improved system performance by 40%."
      ]
    }
  ],
  "projects": [
    {
      "name": "Open Source Tooling",
      "points": [
        "Created an open-source library used by thousands of developers.",
        "Maintained CI/CD pipelines and unit test coverage above 90%."
      ]
    }
  ],
  "education": [
    {
      "institution": "State University",
      "degree": "B.S. in Computer Science",
      "year": "2016"
    }
  ]
}' -o resume.pdf
```
