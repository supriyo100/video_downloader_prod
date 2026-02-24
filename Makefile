.PHONY: help install install-dev test lint format clean run

help:
	@echo "Available commands:"
	@echo "  make install         - Install dependencies"
	@echo "  make install-dev     - Install dev dependencies"
	@echo "  make test            - Run tests"
	@echo "  make lint            - Lint code"
	@echo "  make format          - Format code"
	@echo "  make clean           - Clean up generated files"
	@echo "  make run             - Run application"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install pytest black pylint mypy

test:
	python -m pytest tests/ -v

lint:
	pylint src/ main.py --disable=all --enable=E,F

format:
	black src/ main.py tests/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info/
	rm -rf video_segments/ video_temp/ *.ts concat.txt 2>/dev/null || true
	rm -f *.log

run:
	python main.py -h
