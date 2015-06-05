import sqlite3
from Client import Client
import create_database
import hashlib
import smtplib
import uuid
import os

EMAIL_USER = os.environ['EMAIL_USER']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']


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

    def register(self, username, email, password):
        insert_sql = """
            INSERT INTO Clients (username, email, password)
            VALUES (?, ?, ?)
        """

        if self.is_password_safe(username, password):
            cursor = self.__conn.cursor()

            cursor.execute(insert_sql, (username, email, self.hash_password(password)))
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
                AND (failed_logins < 5
                    OR last_failed_login < datetime(CURRENT_TIMESTAMP, "-30 seconds")
                )
            LIMIT 1
        """

        cursor = self.__conn.cursor()

        cursor.execute(select_query, (username, self.hash_password(password)))
        user = cursor.fetchone()

        if user:
            reset_counter_login_sql = """
                UPDATE Clients
                SET failed_logins = 0
                WHERE client_id = ?
            """

            cursor = self.__conn.cursor()

            cursor.execute(reset_counter_login_sql, (user[0], ))
            self.__conn.commit()

            return Client(user[0], user[1], user[2], user[3])

        else:
            increment_counter_login_sql = """
                UPDATE Clients
                SET failed_logins = failed_logins + 1,
                    last_failed_login = CURRENT_TIMESTAMP
                WHERE username = ?
            """

            cursor = self.__conn.cursor()

            cursor.execute(increment_counter_login_sql, (username, ))
            self.__conn.commit()

            return False

    def send_mail(self, username):
        select_query = """
            SELECT email
            FROM Clients
            WHERE username = ?
        """

        cursor = self.__conn.cursor()
        cursor.execute(select_query, (username, ))
        email = cursor.fetchone()[0]

        hashed = str(uuid.uuid4().hex)

        save_query = """
            UPDATE Clients
            SET hash = ?
            WHERE username = ?
        """

        cursor = self.__conn.cursor()
        cursor.execute(save_query, (hashed, username))
        self.__conn.commit()

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_USER, EMAIL_PASSWORD)
        message = """From: {}
To: {}
Subject: Password reset

You can reset your password using this UUID: {}
        """.format(EMAIL_USER, email, hashed)

        smtp.sendmail(EMAIL_USER, email, message)
