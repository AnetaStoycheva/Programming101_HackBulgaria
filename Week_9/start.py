from sql_manager import SqlManager
from cli_interface import CliInterface
import sqlite3
from settings_money_in_bank import DB_NAME


def main():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    sql_manager = SqlManager(conn)
    interface = CliInterface(sql_manager)

    interface.start()


if __name__ == "__main__":
    main()
