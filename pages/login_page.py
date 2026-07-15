from config import BASE_URL
from utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage:
    
    def __init__(self, page):
        self.page = page

    def navigate(self):
        logger.info("Navigating to login page")
        self.page.goto(BASE_URL + "/login")

    #validating if we came on correct page
    def validate_Login_page(self):
        return self.page.get_by_role("heading",name="Login to your account")

    #entering email and password
    def enter_credentials(self,email,password):
        logger.info(f"Entering credentials for {email[:3]}***")
        self.page.locator('input[data-qa="login-email"]').fill(email)
        self.page.locator('input[data-qa="login-password"]').fill(password)
        self.page.locator('button[data-qa="login-button"]').click()
        logger.info("Login button is clicked")

    #getting error message
    def get_error_message(self):
        return self.page.locator('p').nth(0).inner_text()
    

    
