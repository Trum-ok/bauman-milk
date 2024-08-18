from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from config import BASE_WEB_URL
from config import WEB_APP_URL

# website_keyboard = InlineKeyboardBuilder()
# website_keyboard.add(types.InlineKeyboardButton(
#     text='Сайт', url=BASE_WEB_URL
# ))

start_kb = InlineKeyboardBuilder()
start_kb.add(types.InlineKeyboardButton(
    text='Начать', 
    web_app=types.WebAppInfo(url=WEB_APP_URL)
))
