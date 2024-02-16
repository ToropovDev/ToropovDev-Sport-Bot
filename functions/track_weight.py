import os
from aiogram import F
from aiogram import types
from config.bot_conf import *
from keyboards import keyboards as kb
from db_functions.weights import *
import matplotlib.pyplot as plt
from aiogram.fsm.context import FSMContext
from functions.states import AddWeightStatesGroup
from aiogram import Router
from scipy.interpolate import make_interp_spline
import numpy as np

add_weight_router = Router()


@dp.callback_query(F.data == "track_weight")
async def weight_tracking_menu(call: types.CallbackQuery):
    await call.message.answer("<b>Трекинг веса</b>", reply_markup=kb['track_weight'])
    await call.answer()


def generate_graph(user_id):
    weights = get_user_weights(user_id)
    dates = get_dates()
    dates = dates[len(dates) - len(weights):]
    w = "white"
    gray = "#231F20"
    plt.figure(figsize=(16, 9), facecolor=gray).patch.set_facecolor(gray)
    plt.xticks(rotation=0, fontsize=12, horizontalalignment='center', alpha=.7)
    plt.yticks(fontsize=12, alpha=.7)
    plt.ylabel("Вес", color=w, fontsize=14)
    plt.xlabel("Дата", color=w, fontsize=14)
    ax = plt.gca()
    plt.grid(axis="both", alpha=0.2)
    spines = ax.spines
    spines['top'].set_color(w)
    spines["top"].set_alpha(0.0)
    spines['bottom'].set_color(w)
    spines["bottom"].set_alpha(0.3)
    spines['right'].set_color(w)
    spines["right"].set_alpha(0.0)
    spines['left'].set_color(w)
    spines["left"].set_alpha(0.3)
    plt.gca().set_facecolor(gray)
    plt.yticks(color=w, alpha=0.7, fontsize=12)
    plt.xticks(color=w, alpha=0.7, fontsize=10, rotation=45)
    idx = range(len(dates))
    dates_new = np.linspace(min(idx), max(idx), 300)
    spl = make_interp_spline(idx, weights, k=3)
    smooth = spl(dates_new)
    plt.plot(dates_new, smooth, color="#00CF91", marker='', linewidth=3)
    plt.scatter(idx, weights, color="#00CF91", marker='o', s=300)
    plt.xticks(idx, dates)
    plt.savefig(f"files/{user_id}.png")
    plot = types.FSInputFile(f"files/{user_id}.png")
    return plot


@dp.callback_query(F.data == "check_graph")
async def weight_graph(call: types.CallbackQuery):
    user_id = call.from_user.id
    plot = generate_graph(user_id)
    await bot.send_photo(chat_id=user_id, photo=plot, caption="График вашего веса")
    os.remove(f"files/{user_id}.png")
    await call.answer()


@dp.callback_query(F.data == "add_today_weight")
async def add_today_weight_start(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введи свой актуальный вес")
    await call.answer()
    await state.set_state(AddWeightStatesGroup.waiting_for_weight)


@add_weight_router.message(AddWeightStatesGroup.waiting_for_weight)
async def process_new_weight(message: types.Message, state: FSMContext):
    weight = message.text
    user_id = message.from_user.id
    add_weight(user_id, weight)
    await message.answer("Отлично! Твой актуальный вес добавлен, теперь ты можешь посмотреть свой прогресс.\n\n"
                         "Возвращайся завтра чтобы внести новые измерения")
    await state.clear()
