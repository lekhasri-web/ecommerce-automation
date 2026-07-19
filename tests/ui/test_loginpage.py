from playwright.sync_api import expect
from pages.login_page import LoginPage
import pytest
from config import TEST_EMAIL,TEST_PASSWORD

@pytest.mark.smoke
def test_loginpage_correct_credentials(page):
    loginpage = LoginPage(page)
    loginpage.navigate()
    expect(loginpage.validate_Login_page()).to_be_visible()
    loginpage.enter_credentials(TEST_EMAIL,TEST_PASSWORD)
    expect(page.get_by_text(" Logged in as")).to_be_visible()

@pytest.mark.regression
def test_loginpage_incorrect_credentials(page):
    loginpage = LoginPage(page)
    loginpage.navigate()
    expect(loginpage.validate_Login_page()).to_be_visible()
    loginpage.enter_credentials("Lekhaaa@gmail.com","2222")
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()

@pytest.mark.regression
def test_loginpage_blank_credentails(page):
    loginpage = LoginPage(page)
    loginpage.navigate()
    expect(loginpage.validate_Login_page()).to_be_visible()
    loginpage.enter_credentials("","")
    email_input = page.locator('input[data-qa="login-email"]')
    validation_message = email_input.evaluate("el => el.validationMessage")
    assert "fill out this field" in validation_message.lower()
