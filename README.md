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
  "name": "Michael Harris",
  "title": "Digital Marketing | SEO | SEM | Content Marketing",
  "email": "michael.harris@email.com",
  "phone": "+61 412 345 678",
  "linkedin": "linkedin.com/in/michaelharris",
  "website": "michaelharris.com",
  "summary": "Results-oriented marketing professional with over 5 years of experience in digital marketing, brand strategy, and content creation. Proven ability to drive brand growth, increase online engagement, and deliver data-driven results. Expert in utilizing digital tools and analytics to optimize marketing campaigns and achieve business objectives.",
  "skills": [
    "Digital Marketing Strategy, SEO & SEM, Google Analytics & SEMrush",
    "Social Media Marketing, Content Creation & Copywriting, Budget Management, Data Analysis"
  ],
  "experience": [
    {
      "role": "Marketing Manager",
      "company": "XYZ Corporation, Sydney, NSW",
      "duration": "January 2022 – Present",
      "points": [
        "Lead a team of 5 in creating and executing digital marketing strategies across multiple platforms, including social media, SEO, and email campaigns.",
        "Achieved a 35% increase in website traffic and 50% boost in social media engagement within the first year.",
        "Managed a marketing budget of $200,000, ensuring maximum ROI through cost-effective advertising strategies."
      ]
    },
    {
      "role": "Digital Marketing Specialist",
      "company": "ABC Solutions, Melbourne, VIC",
      "duration": "June 2018 – December 2021",
      "points": [
        "Developed and executed SEO and SEM strategies that increased organic search traffic by 25%.",
        "Created and managed Google Ads and Facebook Ads campaigns, resulting in a 20% increase in qualified leads.",
        "Produced engaging content for blogs, newsletters, and social media platforms to attract target audiences."
      ]
    }
  ],
  "education": [
    {
      "degree": "Bachelor of Marketing",
      "institution": "University of Sydney, Sydney, NSW",
      "year": "Graduated: 2018"
    }
  ],
  "certifications": [
    "Google Analytics Certified",
    "Facebook Blueprint Certification",
    "HubSpot Inbound Marketing Certification"
  ]
}' -o resume.pdf
```
