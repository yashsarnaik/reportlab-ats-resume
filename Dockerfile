FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install uv inside container
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependencies list
COPY requirements.txt .

# Use uv to install dependencies into the system environment
RUN uv pip install --system -r requirements.txt

# Copy project files
COPY app/ ./app/

# Expose port 8000
EXPOSE 8000

# Run FastAPI via uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
