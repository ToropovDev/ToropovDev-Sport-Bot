import asyncio
from aiogram.filters.command import CommandStart, Command
from aiogram import types

from config.bot_conf import *
from keyboards import keyboards as kb
from functions.reg import *
from db_functions.create_tables import create_tables
from functions.menu import *

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    if check_exist_user(message.from_user.id):
        await message.answer(f"""Привет, {message.from_user.first_name}!""", reply_markup=kb['to_main_menu'])
        return
    await message.reply(f"""Привет, {message.from_user.first_name}!""", reply_markup=kb['start'])


async def bot_start():
    create_tables()
    dp.include_router(reg_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(bot_start())
