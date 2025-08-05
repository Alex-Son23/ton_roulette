import pytz
from environs import Env
# from aioredis.client import Redis

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")

POSTGRES_USER = env.str("POSTGRES_USER")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
POSTGRES_DB = env.str("POSTGRES_DB")
POSTGRES_HOST = env.str("POSTGRES_HOST")
POSTGRES_PORT = env.int("POSTGRES_PORT")
POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

REDIS_HOST = env.str("REDIS_HOST")
REDIS_PORT = env.str("REDIS_PORT")
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
USE_REDIS = env.bool('USE_REDIS')

# redis_client = Redis.from_url(REDIS_URL)

TELEGRAM_CHAT_ID = env.str("TELEGRAM_CHAT_ID")
TON_RECEIVE_WALLET = env.str("TON_RECEIVE_WALLET")
TIME_ZONE = pytz.timezone(env.str("TIME_ZONE"))
