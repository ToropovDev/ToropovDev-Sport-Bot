from aiogram import F
from aiogram import types
from config.bot_conf import *
from keyboards import keyboards as kb


@dp.callback_query(F.data == "track_weight")
async def track_weight_menu(call: types.CallbackQuery):
    await call.message.edit_text(f"<b>Weight tracking</b>")
    await call.answer()
