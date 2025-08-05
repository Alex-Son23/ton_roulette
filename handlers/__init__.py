from aiogram import Dispatcher

from .commands.__routers__ import commands_routers
from .error.__routers__ import error_routers


def register_all_handlers(dp: Dispatcher):
    dp.include_routers(commands_routers)
    dp.include_router(error_routers)
