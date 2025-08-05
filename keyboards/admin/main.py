from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def main_admin_keyboard():
    key = InlineKeyboardBuilder()
    key.row(
        InlineKeyboardButton(text='📣 Рассылка', callback_data='admin_sending'),
        InlineKeyboardButton(text='📊 Статистика', callback_data='admin_statistics'),
        width=1
    )
    return key.as_markup()


async def admin_statistics_keyboard():
    key = InlineKeyboardBuilder()
    key.row(
        InlineKeyboardButton(text='⬅️ Назад', callback_data='admin_main_menu')
    )
    return key.as_markup()
