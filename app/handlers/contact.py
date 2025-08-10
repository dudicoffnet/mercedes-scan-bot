from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from app.config import settings

router = Router()

@router.message(F.text.in_({'📲 Связаться с мастером'}))
@router.message(Command('contact'))
async def contact(msg: Message):
    if settings.MASTER_ID:
        await msg.answer('Передаю ваш запрос мастеру. Он свяжется с вами в Telegram.')
    elif settings.MASTER_USERNAME:
        await msg.answer(f'Напишите мастеру: @{settings.MASTER_USERNAME}')
    else:
        await msg.answer('Контакт мастера скоро появится. Попробуйте «📅 Записаться».')
