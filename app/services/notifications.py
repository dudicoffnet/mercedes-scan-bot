from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.config import settings

def make_card_buttons():
    buttons = []
    if settings.MASTER_USERNAME:
        buttons.append([InlineKeyboardButton(text='Связаться в Telegram', url=f'https://t.me/{settings.MASTER_USERNAME}')])
    # Пока без телефона, если дадите номер — добавим tel: ссылку
    if settings.CHANNEL_ID:
        buttons.append([InlineKeyboardButton(text='Открыть канал', url='https://t.me/+3kyBWqh-b1lkZDEy')])
    return InlineKeyboardMarkup(inline_keyboard=buttons) if buttons else None

async def notify_all(bot: Bot, text: str, reply_markup=None):
    ok = False
    # to personal master
    if settings.MASTER_ID:
        try:
            await bot.send_message(settings.MASTER_ID, text, reply_markup=reply_markup)
            ok = True
        except Exception:
            pass
    # to channel
    if settings.CHANNEL_ID:
        try:
            await bot.send_message(settings.CHANNEL_ID, text, reply_markup=reply_markup)
            ok = True
        except Exception:
            pass
    return ok
