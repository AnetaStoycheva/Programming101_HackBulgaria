import sqlite3
from Client import Client
import create_database


class SqlManager:
    def __init__(self, conn):
        self.__conn = conn

    def change_message(self, new_message, logged_user):
        update_sql = """
            UPDATE Clients
            SET message = ?
            WHERE client_id = ?
        """

        cursor = self.__conn.cursor()

        cursor.execute(update_sql, (new_message, logged_user.get_client_id()))
        self.__conn.commit()
        logged_user.set_message(new_message)

    def change_pass(self, new_pass, logged_user):
        update_sql = """
            UPDATE Clients
            SET password = ?
            WHERE client_id = ?
        """

        cursor = self.__conn.cursor()

        cursor.execute(update_sql, (new_pass, logged_user.get_client_id()))
        self.__conn.commit()

    def register(self, username, password):
        insert_sql = """
            INSERT INTO Clients (username, password)
            VALUES (?, ?)
        """
        # try:

        # except CannotUseThis:
        #     raise

# Da ne pravi registraciq, ako imeto ve4e e zaeto!!!

        cursor = self.__conn.cursor()

        cursor.execute(insert_sql, (username, password))
        self.__conn.commit()

    def login(self, username, password):
        select_query = """
            SELECT client_id, username, balance, message
            FROM Clients
            WHERE username = ? AND password = ?
            LIMIT 1
        """

        cursor = self.__conn.cursor()

        cursor.execute(select_query, (username, password))
        user = cursor.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3])
        else:
            return False


class CannotUseThis(Exception):
    pass
