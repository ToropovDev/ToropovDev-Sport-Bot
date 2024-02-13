from db_functions.create_tables import cur, conn
import pandas as pd
from datetime import date


def get_user_weights(user_id):
    cur.execute("SELECT * FROM weights;")
    fetch_all = cur.fetchall()
    weights = pd.Series()
    for user in fetch_all:
        if user[0] == user_id:
            weights = pd.Series(user)
    return weights


def add_weight(user_id, new_weight):
    today = str(date.today()).replace('-', '_')
    cur.execute(f"UPDATE weights SET day_{today}={new_weight} WHERE user_id={user_id};")
    cur.execute(f"UPDATE weights SET actual_weight={new_weight} WHERE user_id={user_id};")
    conn.commit()





