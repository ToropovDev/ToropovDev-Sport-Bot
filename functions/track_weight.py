from aiogram import F
from aiogram import types
from config.bot_conf import *
from keyboards import keyboards as kb
from db_functions.weights import get_user_weights
import matplotlib.pyplot as plt
import pandas as pd


@dp.callback_query(F.data == "track_weight")
async def weight_tracking_menu(call: types.CallbackQuery):
    await call.message.answer("<b>Трекинг веса</b>", reply_markup=kb['track_weight'])
    await call.answer()


@dp.callback_query(F.data == "check_graph")
async def weight_graph(call: types.CallbackQuery):
    user_id = call.from_user.id
    weights = get_user_weights(user_id)
    plt.plot(weights[1:])
    plt.savefig(f"files/{user_id}.png")
    plot = types.FSInputFile(f"files/{user_id}.png")
    await bot.send_photo(chat_id=user_id, photo=plot, caption="График вашего веса")
    await call.answer()

