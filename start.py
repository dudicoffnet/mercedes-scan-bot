import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer("Бот запущен ✅\nКоманда: /ping — проверить статус")

@dp.message(F.text == "/ping")
async def cmd_ping(message: Message):
    await message.answer("pong 🟢")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
