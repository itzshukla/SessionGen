import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7293869890:AAFVop74BV2FY11djRiCAeOj32qB9ol4OWM").strip()
MONGO_URI = os.getenv("MONGO_URI", "").strip()
AUTH_CHANNEL = os.getenv("AUTH_CHANNEL", "").strip()
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "").strip()
BOT_USERNAME = os.getenv("BOT_USERNAME", "").strip()
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "").strip()
AUTH_USERS = os.getenv("AUTH_USERS", "").strip()
