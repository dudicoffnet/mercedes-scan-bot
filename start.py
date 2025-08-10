from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio, os

from app.config import settings
from app.handlers.start import router as start_router
from app.handlers.booking import router as booking_router
from app.handlers.prices import router as prices_router
from app.handlers.contact import router as contact_router

async def set_commands(bot: Bot):
    cmds = [
        BotCommand(command='start', description='Меню'),
        BotCommand(command='prices', description='Цены'),
        BotCommand(command='contact', description='Связаться с мастером'),
    ]
    await bot.set_my_commands(cmds)

async def main():
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start_router)
    dp.include_router(booking_router)
    dp.include_router(prices_router)
    dp.include_router(contact_router)

    await set_commands(bot)
    print('Bot started')
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
