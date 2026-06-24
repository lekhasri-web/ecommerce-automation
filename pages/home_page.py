
class HomePage:

    def __init__(self, page):
        self.page = page
    
    def open_url(self):
        self.page.goto("https://automationexercise.com/")

    def heading(self):
        return self.page.get_by_role("heading",name="Full-Fledged practice website for Automation Engineers")
    
    
    
