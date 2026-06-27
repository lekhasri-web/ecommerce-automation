# Ecommerce Automation Framework

An end-to-end test automation framework built with Playwright and Python, 
testing core user flows on automationexercise.com.

## Tech stack
- Playwright (Python)
- Pytest
- Page Object Model (POM)
- GitHub Actions (CI/CD) — coming Week 2

## Project structure
ecommerce-automation/
├── pages/         # Page Object Model classes
├── tests/
│   └── ui/        # UI test files
├── utils/         # Helper functions
├── config.py      # Base URL and config
├── conftest.py    # Pytest fixtures
└── pytest.ini     # Pytest configuration

## Test coverage
- Homepage load validation
- Login — valid, invalid, blank credentials
- Signup - new user full registration, existing email error

## How to run
pip install -r requirements.txt 
playwright install
pytest tests/ -v

## Run only smoke tests
pytest -m smoke -v