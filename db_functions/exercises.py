from db_functions.create_tables import cur, conn
import pandas as pd


def check_empty_table():
    cur.execute("SELECT EXISTS (SELECT 1 FROM exercises);")
    return cur.fetchall()[0][0]


def add_exercises():
    if not (check_empty_table()):
        exercises = pd.read_excel("files/exercises.xlsx")
        exercises = exercises.values.tolist()
        for exercise in exercises:
            cur.execute("INSERT INTO exercises VALUES (?, ?, ?, ?, ?, ?, ?)", exercise)
        conn.commit()
