import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN
from handlers import register_all_handlers
from ton_api import api_ton
from utils.database_api import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def scheduled_task(bot: Bot):
    try:
        await api_ton(bot)
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
