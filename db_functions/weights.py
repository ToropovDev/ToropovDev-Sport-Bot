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


async def add_date():
    today = str(date.today()).replace('-', '_')
    cur.execute(f"ALTER TABLE weights ADD COLUMN d_{today}")
    conn.commit()


