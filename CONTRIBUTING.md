# Contributing to Video Downloader

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Be respectful and constructive in all interactions.

## Getting Started

### 1. Fork the Repository

```bash
git clone https://github.com/yourusername/video_downloader_prod.git
cd video_downloader_prod
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
make install-dev
```

## Development Workflow

### 1. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

- Write clean, readable code
- Add type hints
- Add docstrings
- Follow existing code style

### 3. Run Tests

```bash
make test
```

### 4. Check Code Quality

```bash
make lint
```

### 5. Format Code

```bash
make format
```

### 6. Commit Changes

```bash
git add .
git commit -m "Description of changes"
```

### 7. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Coding Standards

### Style Guide

- Follow PEP 8
- Use black for formatting
- Use pylint for linting
- Use mypy for type checking

### Code Structure

```python
"""
Module docstring describing purpose
"""

from typing import Optional, List
from pathlib import Path


class MyClass:
    """Class docstring"""
    
    def __init__(self, param: str) -> None:
        """Initialize with param"""
        self.param = param
    
    def method(self, value: int) -> bool:
        """
        Method docstring with description
        
        Args:
            value: Description
        
        Returns:
            Description
        
        Raises:
            ValueError: When value is invalid
        """
        if value < 0:
            raise ValueError("Value must be positive")
        return True
```

### Type Hints

Always use type hints:

```python
# Good
def download(url: str, timeout: int = 30) -> bool:
    pass

# Avoid
def download(url, timeout=30):
    pass
```

### Docstrings

Use docstrings for modules, classes, and functions:

```python
"""Module for downloading video segments"""

class Downloader:
    """Download video segments from URL"""
    
    def download(self, url: str) -> Path:
        """
        Download a segment
        
        Args:
            url: Segment URL
        
        Returns:
            Path to downloaded file
        
        Raises:
            RequestException: If download fails
        """
        pass
```

## Testing

### Write Tests

```python
def test_feature():
    """Test description"""
    assert result == expected
```

### Run Tests

```bash
# Run all tests
make test

# Run specific test
python -m pytest tests/test_file.py::test_function -v

# With coverage
pytest --cov=src tests/
```

## Commit Messages

Use clear, descriptive commit messages:

```
Good:
  Add retry logic to segment downloader
  Fix 404 detection on merge failure
  Refactor logger to use proper levels

Avoid:
  fix bug
  update code
  changes
```

## Pull Request Process

1. Update README if needed
2. Add/update tests
3. Ensure all tests pass
4. Run linter and formatter
5. Write clear PR description
6. Link related issues

## Reporting Issues

### Bug Report

```
Title: [BUG] Short description

Description:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment (Python version, OS, etc.)
- Logs/errors
```

### Feature Request

```
Title: [FEATURE] Short description

Description:
- Use case
- Proposed solution
- Alternative solutions
```

## Questions?

- Open a GitHub discussion
- Check existing issues
- Review documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🚀
