import asyncio
from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from handlers import basic_router
import logging
import sys
import os

load_dotenv()


bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()
dp.include_router(basic_router)


async def main():
    await bot.delete_webhook()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
