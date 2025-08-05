from aiogram import Router, types, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
router_start = Router()


@router_start.message(Command(commands='start'))
async def main_command_start_handler(message: types.Message, state: FSMContext,bot: Bot):
    await state.set_state(state=None)
    await message.answer(f'👋 {message.chat.full_name}, добро пожаловать')
