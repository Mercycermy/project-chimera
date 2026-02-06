# Project Chimera - Build Automation
.PHONY: setup test test-cov lint docker-build docker-test spec-check clean

# === SETUP ===
setup:
	@echo "Setting up development environment..."
	uv pip install --system fastapi "pydantic>=2.0" "pytest>=9.0.2" redis black flake8

# === TESTING ===
test:
	@echo "Running tests..."
	pytest tests/ -v --tb=short

test-cov:
	@echo "Running tests with coverage..."
	pytest tests/ -v --cov=skills --cov-report=html

# === LINTING ===
lint:
	@echo "Running linters..."
	black --check .
	flake8 .

format:
	@echo "Formatting code..."
	black .

# === DOCKER ===
docker-build:
	@echo "Building Docker image..."
	docker build -t project-chimera:latest .

docker-test:
	@echo "Running tests in Docker..."
	docker run --rm project-chimera:latest

# === SPEC CHECKING ===
spec-check:
	@echo "Checking spec alignment..."
	@test -d specs || (echo "ERROR: specs/ directory missing!" && exit 1)
	@test -f specs/_meta.md || (echo "ERROR: specs/_meta.md missing!" && exit 1)
	@test -f specs/functional.md || (echo "ERROR: specs/functional.md missing!" && exit 1)
	@test -f specs/technical.md || (echo "ERROR: specs/technical.md missing!" && exit 1)
	@echo "All required specs present!"

# === CLEANUP ===
clean:
	rm -rf __pycache__ .pytest_cache htmlcov .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true