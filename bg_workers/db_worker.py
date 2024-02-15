from db_functions.create_tables import cur, conn
from datetime import date


async def add_date():
    today = str(date.today()).replace('-', '_')
    cur.execute(f"ALTER TABLE weights ADD COLUMN day_{today};")
    conn.commit()


async def add_yesterday_weight():
    today = str(date.today()).replace('-', '_')
    cur.execute(f"UPDATE weights SET day_{today}=actual_weight WHERE day_{today} IS NULL;")
    conn.commit()
