import os 
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://automationexercise.com"
TEST_EMAIL = os.getenv("TEST_EMAIL", "")
TEST_PASSWORD = os.getenv("TEST_PASSWORD", "")
