import sys
import unittest
import os
import sqlite3

sys.path.append('..')

from sql_manager import SqlManager
import create_database


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect('test.db')
        create_database.create_clients_table(self.connection)
        self.sql_manager = SqlManager(self.connection)
        self.sql_manager.register('Tester', '123')

    def tearDown(self):
        cursor = self.connection.cursor()
        cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove('test.db')

    def test_register(self):
        self.sql_manager.register('Dinko', '123123')
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM Clients
            WHERE username = (?) AND password = (?)
        """, ('Dinko', '123123'))
        users_count = cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = self.sql_manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = self.sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = self.sql_manager.login('Tester', '123')
        new_message = "podaivinototam"
        self.sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = self.sql_manager.login('Tester', '123')
        new_password = "12345"
        self.sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = self.sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    def test_login_with_sql_injection(self):
        logged_user = self.sql_manager.login("' OR 1 = 1 --", '1234')
        self.assertFalse(logged_user)

if __name__ == '__main__':
    unittest.main()
