FROM python:3.11-slim

# Install uv
RUN pip install uv

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Use uv to install dependencies
RUN uv sync --frozen --no-dev

COPY backend/ backend/
COPY frontend/ frontend/
COPY run.py .

EXPOSE 8000

CMD ["uv", "run", "python", "run.py"]
