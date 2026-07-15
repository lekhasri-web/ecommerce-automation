from config import BASE_URL

class ProductsPage:

        def __init__(self,page):
                self.page = page
        
        def navigate(self):
            self.page.goto(BASE_URL + "/products",timeout = 60000)
    
        
