import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID'))
    API_HASH = str(getenv('API_HASH'))
    BOT_TOKEN = str(getenv('BOT_TOKEN'))
    name = str(getenv('SESSION_NAME', 'File-To-Link'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '-1'))
    WORKERS = int(getenv('WORKERS', '4'))
    LOG_CHANNEL = int(getenv('LOG_CHANNEL'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "604152966").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Nanthakps'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    YOUR_IP = str(getenv('YOUR_IP', BIND_ADRESS)) if not ON_HEROKU or getenv('YOUR_IP') else APP_NAME+'.herokuapp.com'
    SSL=bool(getenv('SSL',False))
    if SSL:
        URL = "https://{}/".format(YOUR_IP)
    else:
        URL = "http://{}/".format(YOUR_IP)
    DATABASE_URL = str(getenv('DATABASE_URL'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split())) 
