from aiogram import F
from aiogram import types
from config.bot_conf import *
from keyboards import keyboards as kb


@dp.callback_query(F.data == "to_main_menu")
async def main_menu(call: types.CallbackQuery):
    await call.message.edit_text("<b>Главное меню</b>"
                                 "\n\n"
                                 "Выберите нужный раздел",
                                 reply_markup=kb['main_menu'])
    await call.answer()
