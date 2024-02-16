from db_functions.create_tables import cur, conn
from datetime import date
from bg_workers.db_worker import *


def add_user(user_data: dict[str, any]) -> None:
    cur.execute("SELECT * FROM users;")
    fetch_all = cur.fetchall()
    for user in fetch_all:
        if user[0] == user_data['user_id']:
            return
    cur.execute("INSERT INTO users VALUES(:user_id,"
                " :first_name,"
                " :last_name,"
                " :phone_number,"
                " :age,"
                " :height,"
                " :weight,"
                " :goal)",
                user_data)
    today = str(date.today()).replace('-', '_')
    cur.execute(f"INSERT INTO weights (user_id, actual_weight, day_{today}) VALUES({user_data['user_id']},"
                f"{user_data['weight']}, {user_data['weight']});")
    conn.commit()


def check_exist_user(user_id: int) -> bool:
    cur.execute("SELECT * FROM users;")
    fetch_all = cur.fetchall()
    for user in fetch_all:
        if user[0] == user_id:
            return True
    return False

