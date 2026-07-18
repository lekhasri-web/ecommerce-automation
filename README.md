[![CI/CD_demo](https://github.com/lekhasri-web/ecommerce-automation/actions/workflows/ci.yml/badge.svg)](https://github.com/lekhasri-web/ecommerce-automation/actions/workflows/ci.yml)

# Ecommerce Automation Framework

End-to-end test automation framework built with Playwright and Python,
testing core user flows on automationexercise.com.

## CI/CD
- GitHub Actions runs on every push to main and pull requests
- Runs UI smoke tests and full API test suite as separate steps
- Pipeline completes in under 4 minutes

## Overview
This framework tests core user flows on automationexercise.com — an e-commerce web application. It covers UI testing (login, signup, product browsing), API testing (products, brands, search endpoints), cross-layer API + UI validation, and performance baseline testing. Built with Playwright and Python, it demonstrates hands-on SDET skills including Page Object Model, data driven testing, parallel execution, structured logging, screenshot on failure, and CI/CD with GitHub Actions.

## Tech stack
- Python 3.11
- Playwright + pytest-playwright
- Pytest
- Requests (API testing)
- pytest-xdist (parallel execution)
- pytest-rerunfailures (retry logic)
- Page Object Model (POM)
- GitHub Actions (CI/CD)


## Project structure
```ecommerce-automation/

├── pages/          # Page Object classes
├── tests/
│   ├── api/        # API test files
│   ├── ui/         # UI test files
│   └── data/       # JSON test data files
├── utils/
│   ├── helpers.py    # Reusable helper functions
│   └── logger.py     # Structured logging
├── screenshots/    # Auto-captured on test failure
├── config.py       # Base URL, credentials via env vars
├── conftest.py     # Fixtures and hooks
└── pytest.ini      # Pytest configuration
└── requirements.txt   # requirements 
└── DECISIONS.md       # decisions explained
└── Test_PLAN.md       # requirements 
```



## Test coverage (32 tests)
- **UI tests (12)** — homepage load, login (valid/invalid/blank), signup (new user/existing email), products (logged in/logged out/count), performance baseline (homepage/login/products), data driven login (3 scenarios)
- **API tests (11)** — products list (status/schema/fields), brands list (status/fields), search product (results/keyword validation), login API (valid/invalid/blank/wrong method)
- **Cross-layer tests (2)** — first product from API verified in UI, first brand from API verified in UI
- **Performance tests (3)** — homepage, login page, products page load time assertions
- **Json schema validation tests (4)** - product response,individual product schema,brand response, individual brand schema


## Framework features
- **Page Object Model** — locators and actions separated from test logic, single place to update when UI changes
- **Screenshot on failure** — automatically captured in screenshots/ folder on any test failure
- **Environment variables** — credentials stored via os.getenv, never hardcoded in code
- **Dynamic test data** — uuid generated unique emails for signup tests, preventing data pollution
- **Data driven testing** — JSON file drives parametrized login tests, no code change needed to add scenarios
- **Structured logging** — every test action logged with timestamp for debugging CI failures
- **Parallel execution** — pytest-xdist runs tests concurrently, reducing suite time by 30%
- **Retry logic** — pytest-rerunfailures automatically retries failed tests up to 2 times
- **Helper utilities** — reusable wait, scroll, and text extraction functions following DRY principle
- **Performance baseline** — page load time assertions ensure pages load within acceptable thresholds

## How to install and run
pip install -r requirements.txt
playwright install chromium
pytest tests/ -v

## Run by category
pytest -m smoke -v              # UI critical path tests
pytest -m regression -v         # Full UI coverage
pytest tests/api/ -v            # API tests only
pytest tests/ui/ -v             # UI tests only
pytest tests/ -n 2 -v           # Parallel execution with 2 workers
pytest tests/ui/test_performance.py -v  # Performance tests only

## Design decisions
See [DECISIONS.md](DECISIONS.md) for framework architecture decisions.

## Demo
Loom walkthrough video — coming Day 23


