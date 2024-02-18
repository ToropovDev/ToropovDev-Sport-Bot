import asyncio
from aiogram.filters.command import CommandStart, Command
from aiogram import types

from config.bot_conf import *
from keyboards import keyboards as kb
from db_functions.create_tables import create_tables
from db_functions.weights import *
from functions.reg import *
from functions.menu import *
from functions.track_weight import *
from bg_workers.db_worker import *
from db_functions.users import check_exist_user
from db_functions.exercises import *


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    # await add_date()
    if check_exist_user(message.from_user.id):
        await message.answer(f"Привет, {message.from_user.first_name}!",
                             reply_markup=kb['to_main_menu'])
        return
    await message.reply(f"Привет, {message.from_user.first_name}!",
                        reply_markup=kb['start'])


def sched_start():
    sched.start()
    sched.add_job(add_yesterday_weight, "cron", hour=23, minute=59)
    sched.add_job(add_date, "cron", hour=0, minute=1)


async def bot_start():
    create_tables()
    sched_start()
    dp.include_router(reg_router)
    dp.include_router(add_weight_router)
    add_exercises()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(bot_start())
