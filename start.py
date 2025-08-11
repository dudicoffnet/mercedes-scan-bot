print("Рестарт бота через Railway")
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = "8058008956:AAGtm2NhagRqwSHzTANVGrWM7XNITnmIMlM"

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

dp = Dispatcher()

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer("Привет! Бот запущен и работает 24/7. Команда: /ping")

@dp.message(F.text == "/ping")
async def cmd_ping(message: Message):
    await message.answer(hbold("pong"))

async def main():
    if not BOT_TOKEN:
        raise RuntimeError("Переменная окружения BOT_TOKEN не задана.")
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
