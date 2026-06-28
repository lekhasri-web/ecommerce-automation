from playwright.sync_api import expect
from pages.signup_page import SignupPage
import uuid
import pytest

@pytest.mark.smoke
def test_signup(page):
    signpage = SignupPage(page)
    signpage.navigate()
    random_email = f"test_{uuid.uuid4().hex[:8]}@gmail.com"
    signpage.enter_name_email("Test1",random_email)
    #url = https://automationexercise.com/account_created
    expect(page).to_have_url("https://automationexercise.com/signup")
    signpage.enter_signup_details("Test@1234", 9, "September", 2000, "Test", "User", "TestCo", "123 Test St", "India", "Karnataka", "Bangalore", 560001, "9999999999")
    expect(page).to_have_url("https://automationexercise.com/account_created")
    
@pytest.mark.regression
def test_invalid_signup(page):
    signpage = SignupPage(page)
    signpage.navigate()
    signpage.enter_name_email("Dharani","Dharani99@gmail.com")
    expect(page.locator('p[style="color: red;"]')).to_be_visible()
    expect(page.locator('p[style="color: red;"]')).to_have_text("Email Address already exist!")