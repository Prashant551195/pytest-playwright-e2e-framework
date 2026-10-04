# Pytest Playwright E2E Framework

UI and end-to-end test automation framework built with **Playwright (Python)** and **Pytest**, using the Page Object Model.

**Application under test:** [SauceDemo](https://www.saucedemo.com) (e-commerce demo app)

## Tech stack
- Python 3.14
- Playwright (Python)
- Pytest, pytest-playwright
- pytest-xdist (parallel runs), pytest-rerunfailures (retries)
- Faker (dynamic test data)
- python-dotenv (config)
- Allure (reporting, planned)

## Project structure
```
├── config/          # settings loaded from .env
├── data/            # test data (users.json)
├── pages/           # Page Objects (login, inventory, cart, checkout)
├── components/      # reusable UI components
├── api/             # API clients (planned)
├── utils/           # helpers
├── tests/
│   ├── ui/          # login and cart tests
│   ├── api/         # API tests (planned)
│   └── e2e/         # full business flows
├── conftest.py      # shared fixtures
└── pytest.ini       # markers and settings
```

## Features
- Page Object Model: locators and actions kept in one place per page
- Pytest fixtures for page objects and test data
- Data-driven tests with a JSON user file
- Random checkout data generated with Faker
- Config in environment variables, no hardcoded credentials
- Test markers: `smoke`, `regression`, `e2e`, `api`

## Test coverage
| Area | Tests |
|------|-------|
| Login | valid login, invalid login, locked-out user |
| Cart | add item, add two items, remove item |
| E2E | login, add to cart, checkout, order confirmation |

## Setup
```bash
git clone https://github.com/Prashant551195/pytest-playwright-e2e-framework.git
cd pytest-playwright-e2e-framework
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

Create a `.env` file in the project root:
```
BASE_URL=https://www.saucedemo.com
SAUCE_USER=standard_user
SAUCE_PASSWORD=secret_sauce
```

## Run tests
```bash
pytest                      # all tests
pytest -m smoke             # smoke tests only
pytest -m e2e               # end-to-end flow
pytest --headed --slowmo 500   # watch the browser
```

## Roadmap
- [x] Framework setup and Page Object Model
- [x] UI and E2E tests with test data
- [ ] API tests (Restful-Booker) and hybrid UI + API tests
- [ ] Allure reports, screenshots, traces, auto-created GitHub issues
- [ ] Cross-browser and parallel runs, Docker
- [ ] CI/CD with GitHub Actions
- [ ] Visual and accessibility checks