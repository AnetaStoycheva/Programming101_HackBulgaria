from settings_money_in_bank import DB_NAME, DB_SQL_FILE
import sqlite3

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

with open(DB_SQL_FILE, "r") as f:
    cursor.executescript(f.read())

conn.close()
