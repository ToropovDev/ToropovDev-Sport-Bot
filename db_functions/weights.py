from db_functions.create_tables import cur, conn
from datetime import date


def get_user_weights(user_id):
    cur.execute("SELECT * FROM weights;")
    fetch_all = cur.fetchall()
    weights = []
    for user in fetch_all:
        if user[0] == user_id:
            weights = user
    weights = [w for w in weights if w is not None][2:]
    return weights


def add_weight(user_id, new_weight):
    today = str(date.today()).replace('-', '_')
    cur.execute(f"UPDATE weights SET day_{today}={new_weight} WHERE user_id={user_id};")
    cur.execute(f"UPDATE weights SET actual_weight={new_weight} WHERE user_id={user_id};")
    conn.commit()


def get_dates():
    local_cur = conn.execute("SELECT * FROM weights;")
    dates = [d[0][4:].split("_") for d in local_cur.description][2:]
    dates = [".".join([d[2], d[1], d[0]]) for d in dates]
    return dates





