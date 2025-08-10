from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📅 Записаться')],
        [KeyboardButton(text='💰 Цены')],
        [KeyboardButton(text='📲 Связаться с мастером')]
    ],
    resize_keyboard=True
)
