import os
from aiogram import F
from aiogram import types
from config.bot_conf import *
from keyboards import keyboards as kb
from db_functions.weights import get_user_weights, add_weight
import matplotlib.pyplot as plt
from aiogram.fsm.context import FSMContext
from functions.states import AddWeightStatesGroup
from aiogram import Router

add_weight_router = Router()


@dp.callback_query(F.data == "track_weight")
async def weight_tracking_menu(call: types.CallbackQuery):
    await call.message.answer("<b>Трекинг веса</b>", reply_markup=kb['track_weight'])
    await call.answer()


@dp.callback_query(F.data == "check_graph")
async def weight_graph(call: types.CallbackQuery):
    user_id = call.from_user.id
    weights = get_user_weights(user_id)
    plt.plot(weights[2:])
    plt.savefig(f"files/{user_id}.png")
    plot = types.FSInputFile(f"files/{user_id}.png")
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
