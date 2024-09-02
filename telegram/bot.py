import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from config import TG_TOKEN, OWNER_IDS, ENV, get_sc_session
from handlers import register_handlers
# from prometheus_client import start_http_server
from db.main import Database

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG if ENV == 'dev' else logging.INFO,
)

async def main():
    bot = Bot(
        token=TG_TOKEN, 
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
            )
        )
    await bot.delete_webhook(drop_pending_updates=True)
    dp = Dispatcher(storage=MemoryStorage())
    dp['started_at'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    register_handlers(dp)
    
    s = get_sc_session()
    if s is None:
        raise ValueError("Failed to get ScyllaDB session.")
    
    db = Database(s)
    if db is None:
        raise ValueError("Failed to initialize Database.")

    dp['db'] = db
    db.create()

    await bot.set_my_commands([
        BotCommand(command="start", description="Начало приключения 🚀"),
        BotCommand(command="help", description="Где я? 🗺️")
    ])

    # start_http_server(PROMETHEUS_PORT)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
