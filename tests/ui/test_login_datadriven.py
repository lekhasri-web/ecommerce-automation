from playwright.sync_api import expect
from pages.login_page import LoginPage
import pytest
import json

def load_json(path):
    with open(path) as f:
        return [(d["email"],d["password"],d["expected"])
                for d in json.load(f)]

@pytest.mark.parametrize("email,password,expected",load_json("tests/data/login_data.json"))
@pytest.mark.regression
def test_login_datadriven(page,email,password,expected):
    loginpage = LoginPage(page)
    loginpage.navigate()
    expect(loginpage.validate_Login_page()).to_be_visible()
    loginpage.enter_credentials(email,password)
    assert loginpage.get_error_message() == expected

