
class HomePage:

    def __init__(self, page):
        self.page = page
    
    def open_url(self, url: str):
        self.page.goto(url)

    def heading(self):
        return self.page.get_by_role("heading",name="Full-Fledged practice website for Automation Engineers")
    
    def page_title_validation(self):
        return self.page.title()
    
    
