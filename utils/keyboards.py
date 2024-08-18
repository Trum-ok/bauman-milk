from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from config import BASE_WEB_URL

# website_keyboard = InlineKeyboardBuilder()
# website_keyboard.add(types.InlineKeyboardButton(
#     text='Сайт', url=BASE_WEB_URL
# ))

start_kb = InlineKeyboardBuilder()
start_kb.add(types.InlineKeyboardButton(
    text='Начать', 
    callback_data='start'
))
