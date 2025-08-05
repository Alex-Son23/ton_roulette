from aiogram import Router

# from filters.chat_type import InBotChatFilter
from .start import router_start

commands_routers = Router()
commands_routers.include_routers(router_start)

# commands_routers.message.filter(InBotChatFilter())
