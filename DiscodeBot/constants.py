import os

from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
PUBLIC_KYE = os.getenv('PUBLIC_KYE')
TOKEN = os.getenv('TOKEN')
TEXT_CHANNEL_ID = os.getenv('TEXT_CHANNEL_ID')
