import logging

from aiogram import Router
from aiogram.types import ErrorEvent

router_main_error = Router()


@router_main_error.error()
async def error_handler(event: ErrorEvent):
    logger = logging.getLogger(__name__)
    logger.critical("Critical error caused by %s", event.exception, exc_info=True)
