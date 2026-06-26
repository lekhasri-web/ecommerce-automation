from config import BASE_URL

class SignupPage():

    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto(BASE_URL+"/login")
    
    def enter_name_email(self,name,email):
        self.page.locator('input[data-qa="signup-name"]').fill(name)
        self.page.locator('input[data-qa="signup-email"]').fill(email)
        self.page.locator('button[data-qa="signup-button"]').click()

    def enter_signup_details(self,password,day,month,year,firstname,lastname,Company,address,country,state,city,zipcode,mobilenumber):
        self.page.locator('[data-qa="login"][id="uniform-id_gender2"]')
        self.page.locator('input[data-qa="password"]').fill(password)
        self.page.locator('[data-qa="days"]').select_option(value=str(day))
        self.page.locator('[data-qa="months"]').select_option(value=month)
        self.page.locator('[data-qa="years"]').select_option(value=str(year))
        self.page.locator("#newsletter").check()
        self.page.locator("#optin").check()
        self.page.locator('[data-qa="first_name"]').fill(firstname)
        self.page.locator('[data-qa="last_name"]').fill(lastname)
        self.page.locator('[data-qa="company"]').fill(Company)
        self.page.locator('[data-qa="address"]').fill(address)
        self.page.locator('[data-qa="country"]').select_option(value=country)
        self.page.locator('[data-qa="state"]').fill(state)
        self.page.locator('[data-qa="city"]').fill(city)
        self.page.locator('[data-qa="zipcode"]').fill(str(zipcode))
        self.page.locator('[data-qa="mobile_number"]').fill(mobilenumber)
        self.page.locator('button[data-qa="create-account"]').click()
        #locator = account-created



        

