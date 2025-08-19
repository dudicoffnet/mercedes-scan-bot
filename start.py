from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio, logging, os

API_TOKEN = os.getenv("API_TOKEN", "YOUR_API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Заполнить анкету")],
        [KeyboardButton(text="Найти рядом", request_location=True)],
        [KeyboardButton(text="Помочь проекту")],
        [KeyboardButton(text="Настройки")]
    ],
    resize_keyboard=True
)

@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Привет! Это бот «Сейчас». Выбирай действие:", reply_markup=main_menu)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
