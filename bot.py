
import logging
import asyncio


from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import  start_polling

from core import config
from core.handlers import main_handlers
from core.metric import  background_on_start


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):

    main_handlers(dp)
    asyncio.create_task(background_on_start())


def main():
    logging.basicConfig(level=logging.INFO)
    logging.warning('Запуск на пулинге')
    start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup)
