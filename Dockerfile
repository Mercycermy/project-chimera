FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml Readme.md ./
COPY skills ./skills
COPY specs ./specs
COPY tests ./tests

RUN pip install --no-cache-dir fastapi "pydantic>=2.0" "pytest>=9.0.2" redis

CMD ["pytest", "-q"]
