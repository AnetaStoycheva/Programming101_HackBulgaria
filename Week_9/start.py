import sql_manager
from cli_interface import CliInterface


def main():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    sql_manager = SqlManager(conn)
    interface = CliInterface(sql_manager)

    interface.start()


if __name__ == "__main__":
    main()
