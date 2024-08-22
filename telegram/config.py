import os
import asyncpg
import logging
from dotenv import load_dotenv

load_dotenv(override=True)

ENV = os.getenv("ENVIRONMENT", "dev")

# LOG_HOST = os.getenv("LOG_HOST")
# LOG_PORT = int(os.getenv("LOG_PORT"))
TG_TOKEN = os.getenv("TG_TOKEN") if ENV == 'prod' else os.getenv("TG_TOKEN_DEV")
BOT_NAME = "BaumanCoin_bot" if ENV == 'prod' else "BaumanCoin_test_bot"
BOT_URL = f"https://t.me/{BOT_NAME}"
# PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT"))
PD_USER = os.getenv("POSTGRESQL_USER")
PG_PASS = os.getenv("POSTGRESQL_PASSWORD")
PG_HOST = os.getenv("POSTGRESQL_HOST")
PG_PORT = os.getenv("POSTGRESQL_PORT")
PG_DB = os.getenv("POSTGRESQL_DBNAME")
OWNER_IDS = os.getenv("OWNERS_IDS").split(",")
BASE_WEB_URL = os.getenv("BASE_WEB_URL")
WEB_APP_URL = os.getenv("WEB_APP_URL")


async def get_pool() -> asyncpg.Pool:
    try:
        pool = await asyncpg.create_pool(
            host=PG_HOST,
            port=PG_PORT,
            user=PD_USER,
            password=PG_PASS,
            database=PG_DB,
        )
    except Exception as e:
        logging.error("Failed to connect to database", exc_info=e)
        return
    if not pool:
        raise AssertionError
    return pool
