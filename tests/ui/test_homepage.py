from playwright.sync_api import expect
from pages.home_page import HomePage
import pytest


@pytest.mark.smoke
def test_homepage_loads_successfully(page):
    home_page = HomePage(page)
    home_page.open_url()
    expect(home_page.heading()).to_be_visible()
    expect(home_page.page).to_have_title("Automation Exercise")



