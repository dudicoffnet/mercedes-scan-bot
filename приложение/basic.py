from aiogram import F, Router
from aiogram.types import Message

router = Router()

@router.message(F.photo)
async def get_file_id(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"file_id этой картинки: `{file_id}`")
