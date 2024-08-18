from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, CommandObject

# from utils.text import EMAIL_FOR_REGISTER, PASSWORD_FOR_REGISTER, ALREADY_REGISTERED, INVALID_EMAIL, REGISTER_SUCCESS
# from utils import check
# from db.main import Database
from utils.text import START
from utils.keyboards import start_kb
# from utils.exceptions import UserNotFound

router = Router()


@router.message(CommandStart(deep_link=True))
async def start_(message: types.Message, command: CommandObject):
    arg = command.args
    if arg == "milk":
        # секретный гифт
        pass
    # рефералы
    else:
        # добавить фото
        await message.answer(
            text=START.format(name=message.from_user.username), 
            reply_markup=start_kb.as_markup()
        )


@router.message(Command('start'))
async def start(message: types.Message):
    # добавить фото
    await message.answer(
        text=START.format(name=message.from_user.username), 
        reply_markup=start_kb.as_markup()
    )


def register_start_handlers(dp: Router):
    dp.include_router(router)
