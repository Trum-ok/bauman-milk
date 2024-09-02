import os
import asyncio
import logging

from cassandra.cluster import Session, Cluster
from dotenv import load_dotenv


load_dotenv(override=True)

ENV = os.getenv("ENVIRONMENT", "dev")

# LOG_HOST = os.getenv("LOG_HOST")
# LOG_PORT = int(os.getenv("LOG_PORT"))
TG_TOKEN = os.getenv("TG_TOKEN") if ENV == 'prod' else os.getenv("TG_TOKEN_DEV")
BOT_NAME = "BaumanCoin_bot" if ENV == 'prod' else "BaumanCoin_test_bot"
BOT_URL = f"https://t.me/{BOT_NAME}"
# PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT"))
SC_USER = os.getenv("SC_USER")
SC_PASS = os.getenv("SC_PASSWORD")
SC_HOST = os.getenv("SC_HOST")
SC_PORT = os.getenv("SC_PORT")
SC_NODES: list = os.getenv("SC_NODES").split(',')
SC_DB = os.getenv("SC_DBNAME")
SC_KEY = os.getenv("SC_KEY")
OWNER_IDS = os.getenv("OWNERS_IDS").split(",")
BASE_WEB_URL = os.getenv("BASE_WEB_URL")
WEB_APP_URL = os.getenv("WEB_APP_URL")


def get_sc_session() -> Session:
    cluster = Cluster(SC_NODES)  # Add your ScyllaDB nodes here
    session = cluster.connect(SC_KEY)
    return session
