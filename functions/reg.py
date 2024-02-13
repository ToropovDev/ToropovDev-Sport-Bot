from aiogram import F
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram import Router
from config.bot_conf import *
from keyboards import keyboards as kb
from functions.states import RegStatesGroup
from db_functions.users import add_user

reg_router = Router()


@dp.callback_query(F.data == "start_reg")
async def start_registration(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(f"Сначала нам нужно познакомиться! Поделись своим контактом", reply_markup=kb['contact'])
    await call.answer()
    await state.set_state(RegStatesGroup.waiting_for_contact)


@reg_router.message(RegStatesGroup.waiting_for_contact)
async def process_contact(message: types.Message, state: FSMContext):
    contact = message.contact
    await state.set_data({"user_id": contact.user_id,
                          "first_name": contact.first_name,
                          "last_name": contact.last_name,
                          "phone_number": contact.phone_number})
    await state.set_state(RegStatesGroup.waiting_for_age)
    await message.answer("Введите свой возраст", reply_markup=types.ReplyKeyboardRemove())


@reg_router.message(RegStatesGroup.waiting_for_age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data({'age': message.text})
    await state.set_state(RegStatesGroup.waiting_for_height)
    await message.answer("Введите свой рост")


@reg_router.message(RegStatesGroup.waiting_for_height)
async def process_height(message: types.Message, state: FSMContext):
    await state.update_data({'height': message.text})
    await state.set_state(RegStatesGroup.waiting_for_weight)
    await message.answer("Введите свой вес")


@reg_router.message(RegStatesGroup.waiting_for_weight)
async def process_weight(message: types.Message, state: FSMContext):
    await state.update_data({'weight': message.text})
    await state.set_state(RegStatesGroup.waiting_for_goal)
    await message.answer("Выберите цель тренировок", reply_markup=kb['goal'])


@reg_router.callback_query(F.data == "gain")
async def process_gain_weight(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({'goal': 'gain'})
    await call.message.edit_text("Отлично! Все данные заполнены", reply_markup=kb["to_main_menu"])
    await call.answer()
    data = await state.get_data()
    add_user(data)
    await state.clear()


@reg_router.callback_query(F.data == "lose")
async def process_lose_weight(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({'goal': 'lose'})
    await call.message.edit_text("Отлично! Все данные заполнены", reply_markup=kb["to_main_menu"])
    await call.answer()
    data = await state.get_data()
    add_user(data)
    await state.clear()


@reg_router.callback_query(F.data == "save")
async def process_save_weight(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({'goal': 'save'})
    await call.message.edit_text("Отлично! Все данные заполнены", reply_markup=kb["to_main_menu"])
    await call.answer()
    data = await state.get_data()
    add_user(data)
    await state.clear()



