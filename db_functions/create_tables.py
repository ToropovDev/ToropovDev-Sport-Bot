import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()


def create_table_users():
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT,
            phone_number TEXT NOT NULL,
            age INT NOT NULL,
            height INT NOT NULL,
            weight INT NOT NULL,
            goal INT NOT NULL,
            CONSTRAINT PK_users PRIMARY KEY (user_id));
        """)
    conn.commit()


def create_table_weights():
    cur.execute("""CREATE TABLE IF NOT EXISTS weights(
            user_id INT NOT NULL,
            actual_weight INT NOT NULL,
            day_08_02_24 INT,
            CONSTRAINT PK_weights PRIMARY KEY (user_id))""")
    conn.commit()


def create_tables():
    create_table_users()
    create_table_weights()