from playwright.sync_api import Page

def wait_for_element_page(page,selector,timeout=5000,index = 0):
    locator = page.locator(selector)
    locator.nth(index).wait_for(state="visible",timeout=timeout)
    return locator

def scroll_to_element(page,selector,index = 0):
    locator = page.locator(selector)
    locator.nth(index).scroll_into_view_if_needed()
    return locator

def get_element_text(page,selector,index=0):
    locator = page.locator(selector)
    locator = locator.nth(index).inner_text()
    return locator


    
