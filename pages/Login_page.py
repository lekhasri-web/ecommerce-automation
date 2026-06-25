from config import BASE_URL

class LoginPage:
    
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(BASE_URL + "/login")

    def validate_Login_page(self):
        return self.page.get_by_role("heading", name="Login to your account")

    def enter_credentials(self, email, password):
        self.page.locator('input[data-qa="login-email"]').fill(email)
        self.page.locator('input[data-qa="login-password"]').fill(password)
        self.page.locator('button[data-qa="login-button"]').click()
