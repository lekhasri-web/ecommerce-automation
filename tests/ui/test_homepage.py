from playwright.sync_api import Page,expect
from pages.home_page import HomePage

def test_homepage_search_bar(human_page_fixture):
    home_page = HomePage(human_page_fixture)
    home_page. open_url()
    expect(home_page.heading()).to_be_visible(timeout=5000)
    expect(home_page.page).to_have_title("Automation Exercise")
