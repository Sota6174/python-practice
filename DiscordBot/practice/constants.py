import os

from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
PUBLIC_KYE = os.getenv('PUBLIC_KYE')
TOKEN = os.getenv('TOKEN')
TEXT_CHANNEL_ID = os.getenv('TEXT_CHANNEL_ID')

CORONA_URL = os.getenv('CORONA_URL')

GOOLAB_APP_ID = os.getenv('GOOLAB_APP_ID')
GOOLAB_URL = os.getenv('GOOLAB_URL')

GOOGLE_CGI_URL = os.getenv('GOOGLE_CGI_URL')
