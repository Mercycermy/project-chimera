FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    make \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml Readme.md ./
COPY skills ./skills
COPY specs ./specs
COPY tests ./tests

RUN pip install --no-cache-dir uv \
    && uv pip install --system fastapi "pydantic>=2.0" "pytest>=9.0.2" redis

CMD ["pytest", "-q"]
