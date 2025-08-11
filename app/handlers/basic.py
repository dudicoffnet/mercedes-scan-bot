from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Записаться")],
        [KeyboardButton(text="💰 Цены")],
        [KeyboardButton(text="📲 Связаться с мастером")],
    ],
    resize_keyboard=True
)

@router.message(CommandStart())
async def cmd_start(m: Message):
    await m.answer("Привет! Я онлайн на Railway ✅", reply_markup=kb_main)

@router.message(F.text)
async def echo(m: Message):
    await m.answer(f"Эхо: {m.text}")