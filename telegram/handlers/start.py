import os

from aiogram import Router, types
from aiogram.filters import Command, CommandStart, CommandObject

from utils.text import START
from utils.keyboards import start_kb
from db.main import Database
from cassandra import AlreadyExists

router = Router()


@router.message(CommandStart(deep_link=True))
async def start_(message: types.Message, command: CommandObject,  db: Database):
    arg = command.args
    if arg == "milk":
        # секретный гифт
        pass
    # рефералы
    else:
        await start_foo(message, db)


@router.message(Command('start'))
async def start(message: types.Message,  db: Database):
    await start_foo(message, db)


async def start_foo(message: types.Message,  db: Database):
    try:
        id = message.from_user.id
        db.users.insert(id)
        db.energy.first(id, 1200)
        db.upgrades.insert(id)
    except AlreadyExists:
        pass
    await message.answer_photo(
        photo=types.FSInputFile(path="telegram/props/not.jpg"),
        caption=START.format(name=message.from_user.username),
        reply_markup=start_kb.as_markup()
    )


def register_start_handlers(dp: Router):
    dp.include_router(router)
