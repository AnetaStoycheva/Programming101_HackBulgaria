from settings_money_in_bank import DB_NAME, DB_SQL_FILE
import sqlite3


def create_clients_table(conn):
    cursor = conn.cursor()
    with open(DB_SQL_FILE, "r") as f:
        cursor.executescript(f.read())


def main():
    conn = sqlite3.connect(DB_NAME)
    create_clients_table(conn)

if __name__ == '__main__':
    main()
