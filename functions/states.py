from aiogram.fsm.state import StatesGroup, State


class RegStatesGroup(StatesGroup):
    waiting_for_contact = State()
    waiting_for_age = State()
    waiting_for_height = State()
    waiting_for_weight = State()
    waiting_for_goal = State()
    ending = State()

