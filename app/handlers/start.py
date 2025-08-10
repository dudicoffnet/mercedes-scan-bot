from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from app.keyboards.main import kb_main

router = Router()

@router.message(CommandStart())
async def start_cmd(msg: Message):
    # send banner then menu text
    banner = FSInputFile('assets/banner.png')
    await msg.answer_photo(banner, caption=(
        '<b>Оригинальная диагностика Mercedes</b>\n'
        'XENTRY / DAS — <b>от 30 рублей</b>\n\n'
        'Выберите действие кнопкой ниже:'
    ))
    await msg.answer('Меню:', reply_markup=kb_main)
