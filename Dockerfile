FROM python:3.11-slim

RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY backend/ backend/
COPY frontend/ frontend/
COPY run.py .

EXPOSE 8000

CMD ["uv", "run", "python", "run.py"]
