# Framework Design Decisions

## 1. Playwright over Selenium
I chose Playwright because it has built-in auto-waiting — tests only execute  after the page is fully loaded, which reduced flaky tests in my framework. Playwright runs all 26 tests in under 3 minutes which is significantly faster 
than Selenium. I also needed API testing support in the same tool, which Playwright provides natively. Selenium requires separate setup for WebDriver and does not support API testing.

## 2. Python over Java or TypeScript
I chose Python because I needed one language for both UI tests using Playwright and API tests using the requests library. Switching between two languages for different test types would slow down development and increase complexity. Python also has clean syntax which makes test code readable for non-technical 
stakeholders.

## 3. Page Object Model
I chose POM because when a locator breaks, I only need to update one file the page class — instead of every test that uses that locator. Tests contain only test logic and assertions. Pages contain all locators and actions. This 
separation made maintenance significantly easier when automationexercise.com updated their UI.

## 4. Separate API test folder
I separated API tests into tests/api/ because I can run them independently without markers — just pytest tests/api/ -v. In CI/CD I run UI smoke tests and API tests as separate pipeline steps, which gives faster feedback on which 
layer broke. Mixing API and UI tests in one folder would make selective execution harder.

## 5. GitHub Actions for CI/CD
I chose GitHub Actions because it is built into GitHub — no separate tool setup needed. When I pushed code with bugs in my first CI run, the pipeline caught failures I hadn't noticed locally. This gave me confidence that every 
push to main is automatically validated against the full test suite.