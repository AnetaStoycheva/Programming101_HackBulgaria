import sqlite3
from Client import Client
import create_database
import hashlib


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

        if self.is_password_safe(logged_user.get_username(), new_pass):
            cursor = self.__conn.cursor()

            cursor.execute(update_sql, (self.hash_password(new_pass), logged_user.get_client_id()))
            self.__conn.commit()
            return True

        else:
            return False

    def register(self, username, password):
        insert_sql = """
            INSERT INTO Clients (username, password)
            VALUES (?, ?)
        """

        if self.is_password_safe(username, password):
            cursor = self.__conn.cursor()

            cursor.execute(insert_sql, (username, self.hash_password(password)))
            self.__conn.commit()
            return True

        else:
            return False

    def is_password_safe(self, username, password):
        if len(password) < 9:
            return False

        if username in password:
            return False

        found_capital_letter = False
        found_number = False
        found_special_symbol = False

        for letter in password:
            if letter.isupper():
                found_capital_letter = True
            else:
                if letter.isdigit():
                    found_number = True
                else:
                    if letter in '!@#$%^&*()_+=\|]}[{";:><.,/?~`\'':
                        found_special_symbol = True

        if found_special_symbol and found_number and found_capital_letter:
            return True
        else:
            return False

    def hash_password(self, password):
        password_bytes = bytearray(password, 'utf-8')
        hash_object = hashlib.sha1(password_bytes)
        hex_dig = hash_object.hexdigest()

        return hex_dig

    def login(self, username, password):
        select_query = """
            SELECT client_id, username, balance, message
            FROM Clients
            WHERE username = ? AND password = ?
            LIMIT 1
        """

        cursor = self.__conn.cursor()

        cursor.execute(select_query, (username, self.hash_password(password)))
        user = cursor.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3])
        else:
            return False
