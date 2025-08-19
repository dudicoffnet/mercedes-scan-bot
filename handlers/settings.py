from aiogram import types, Router

router = Router()

@router.message(lambda m: m.text == "Настройки")
async def settings_handler(message: types.Message):
    await message.answer("Здесь будут настройки профиля и видимости.")
