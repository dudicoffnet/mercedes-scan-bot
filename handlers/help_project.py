from aiogram import types, Router

router = Router()

@router.message(lambda m: m.text == "Помочь проекту")
async def help_project(message: types.Message):
    await message.answer("Спасибо за поддержку! (Тут будет QR-код)")
