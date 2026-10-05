import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
SAUCE_USER = os.getenv("SAUCE_USER")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")
API_BASE_URL = os.getenv("API_BASE_URL")