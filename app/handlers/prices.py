from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(F.text == '💰 Цены')
@router.message(Command('prices'))
async def prices(msg: Message):
    await msg.answer(
        '<b>Прайс (от 30 руб.)</b>\n'
        '— Комп. диагностика: от 30 BYN\n'
        '— Чтение/сброс ошибок: от 20 BYN\n'
        '— Предпродажная проверка: от 50 BYN\n\n'
        'Точно назову после первичного осмотра.'
    )
