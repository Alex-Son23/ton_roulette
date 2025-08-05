# from typing import Union
#
# from aiogram import types
# from aiogram.filters import BaseFilter
#
# from config import ADMINS
#
#
# class IsAdmin(BaseFilter):
#     async def __call__(self, telegram_object: Union[types.Message, types.CallbackQuery]) -> bool:
#         if isinstance(telegram_object, types.CallbackQuery):
#             return str(telegram_object.message.chat.id) in ADMINS
#         else:
#             return str(telegram_object.chat.id) in ADMINS
