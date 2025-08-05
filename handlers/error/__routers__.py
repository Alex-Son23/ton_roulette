from aiogram import Router

from .main import router_main_error

error_routers = Router()
error_routers.include_routers(router_main_error)
