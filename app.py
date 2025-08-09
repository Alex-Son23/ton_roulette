import os, sys, django
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DJANGO_ROOT = BASE_DIR / "utils" / "web_admin"   # тут лежат draw_view, log_view и пакет web_admin
sys.path.insert(0, str(DJANGO_ROOT))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_admin.settings")
django.setup()

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN, OPENAI_TOKEN
from handlers import register_all_handlers
from ton_api import api_ton
from utils.database_api import init_db
from openai import AsyncOpenAI


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
openai_client = AsyncOpenAI(api_key=OPENAI_TOKEN)


async def scheduled_task(bot: Bot):
    try:
        await api_ton(bot, openai_client)
    except Exception as e:
        logger.error(f"Ошибка в scheduled_task: {e}")


async def scheduler(bot: Bot):

    while True:
        try:
            await scheduled_task(bot)
        except Exception as e:
            logger.error(f"Исключение в задаче: {e}")
        await asyncio.sleep(60)


async def main():
    await init_db()
    logger.info("База данных инициализирована")

    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    logger.info("Бот создан")

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    register_all_handlers(dp)

    asyncio.create_task(scheduler(bot))

    logger.info("Запуск polling...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот остановлен вручную")
