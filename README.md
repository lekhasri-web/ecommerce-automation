[![CI/CD_demo](https://github.com/lekhasri-web/ecommerce-automation/actions/workflows/ci.yml/badge.svg)](https://github.com/lekhasri-web/ecommerce-automation/actions/workflows/ci.yml)

# Ecommerce Automation Framework

End-to-end test automation framework built with Playwright and Python,
testing core user flows on automationexercise.com.

## Tech stack
- Python 3.11
- Playwright
- Pytest
- Page Object Model (POM)
- GitHub Actions CI/CD — Week 2

## Project structure
ecommerce-automation/
├── pages/          # Page Object classes
├── tests/
│   └── ui/         # UI test files
├── utils/          # Helper functions
├── screenshots/    # Auto-captured on test failure
├── config.py       # Base URL, credentials via env vars
├── conftest.py     # Fixtures and hooks
└── pytest.ini      # Pytest configuration

## Test coverage (9 tests)
- Homepage — page load validation
- Login — valid credentials, invalid credentials, blank fields
- Signup — new user registration with dynamic email, existing email error
- Products — logged in view, logged out view, product count validation

## How to run locally
pip install -r requirements.txt
playwright install
pytest tests/ -v

## Run by marker
pytest -m smoke -v      # 4 critical path tests
pytest -m regression -v # 5 full coverage tests

## Features
- Page Object Model — locators separated from test logic
- Screenshot on failure — auto-captured in screenshots/ folder
- Environment variables — credentials never hardcoded
- Dynamic test data — uuid generated emails for signup tests

## CI/CD
- GitHub Actions runs on every push to main
- UI smoke tests + full API test suite
- Both pass in under 40 seconds