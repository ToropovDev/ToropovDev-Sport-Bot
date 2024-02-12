from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

start_login_btn = InlineKeyboardButton(text="Начать путь", callback_data="start_reg")
start_kb = InlineKeyboardMarkup(inline_keyboard=[[start_login_btn]])

contact_btn = KeyboardButton(text="Отправить номер телефона", request_contact=True)
contact_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[contact_btn]])

gain_btn = InlineKeyboardButton(text="Набрать вес", callback_data="gain")
save_btn = InlineKeyboardButton(text="Удерживать вес", callback_data="save")
lose_btn = InlineKeyboardButton(text="Сбросить вес", callback_data="lose")
goal_kb = InlineKeyboardMarkup(inline_keyboard=[[gain_btn, lose_btn],
                                                [save_btn]])

to_main_menu_btn = InlineKeyboardButton(text="В главное меню", callback_data="to_main_menu")
to_main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[[to_main_menu_btn]])

track_weight_btn = InlineKeyboardButton(text="Трекинг веса", callback_data="track_weight")
edit_user_btn = InlineKeyboardButton(text="Изменить данные", callback_data="edit_user")
calculs_btn = InlineKeyboardButton(text="Расчёты", callback_data="calculs")
workouts_btn = InlineKeyboardButton(text="Тренировки", callback_data="workouts")
measurements_btn = InlineKeyboardButton(text="Замеры", callback_data="measurements")
main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[[workouts_btn],
                                                     [track_weight_btn],
                                                     [calculs_btn, measurements_btn],
                                                     [edit_user_btn]])

add_today_weight_btn = InlineKeyboardButton(text="Добавить измерение", callback_data="add_today_weight")
check_graph_btn = InlineKeyboardButton(text="Посмотреть прогресс", callback_data="check_graph")
track_weight_kb = InlineKeyboardMarkup(inline_keyboard=[[add_today_weight_btn], [check_graph_btn]])

keyboards = {"start": start_kb,
             "contact": contact_kb,
             "goal": goal_kb,
             "to_main_menu": to_main_menu_kb,
             "main_menu": main_menu_kb,
             "track_weight": track_weight_kb}

