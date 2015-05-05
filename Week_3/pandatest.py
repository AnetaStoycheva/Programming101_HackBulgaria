import unittest
from panda import Panda
from panda import PandaSocialNetwork
from panda import PandaAlreadyThere
from panda import PandasAlreadyFriends


class PandaTest(unittest.TestCase):
    def setUp(self):
        self.account = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_constructor(self):
        self.assertEqual(self.account.get_name(), "Ivo")
        self.assertEqual(self.account.get_email(), "ivo@pandamail.com")
        self.assertEqual(self.account.get_gender(), "male")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            account_new = Panda("Maria", "maria@pandamail", "female")

    def test_is_name_valid_type(self):
        with self.assertRaises(TypeError) as context:
            Panda(1, "ivo@pandamail.com", "male")
        self.assertEqual(str(context.exception), "1 is not a valid name.")

    def test_is_email_valid_type(self):
        with self.assertRaises(TypeError) as context:
            Panda("Ivo", 10, "male")
        self.assertEqual(str(context.exception), "10 is not a string.")

    def test_create_panda_account_class(self):
        self.assertTrue(isinstance(self.account, Panda))

    def test_panda_str(self):
        expected = "Panda account for Ivo with email ivo@pandamail.com and gender male."
        self.assertEqual(str(self.account), expected)

    def test_when_pandas_are_not_equal(self):
        p1 = Panda("Ivo", "ivo@pandamail.com", "male")
        p2 = Panda("Ivo2", "ivo2@pandamail.com", "male")

        self.assertFalse(p1 == p2)

    def test_when_pandas_are_equal(self):
        p1 = Panda("Ivo", "ivo@pandamail.com", "male")
        p2 = Panda("Ivo", "ivo@pandamail.com", "male")

        self.assertTrue(p1 == p2)

    def test_can_put_panda_in_hash_table(self):
        dictionary = {}
        dictionary[self.account] = 1  # davam mu prosto nqkakva stojnost
        self.assertTrue(self.account in dictionary)


class TestPandaSocialNetwork(unittest.TestCase):
    def setUp(self):
        self.panda1 = Panda("Ivo", "ivo@pandamail.com", "male")
        self.panda2 = Panda("Rado", "rado@pandamail.com", "male")
        self.panda3 = Panda("Maria", "maria@pandamail.com", "female")
        self.panda4 = Panda("Kiko", "kiko@mail.bg", "female")
        self.panda5 = Panda("Kikomir", "kikomir@mail.bg", "male")
        self.panda6 = Panda("Kikimor4o", "kikimor4o@mail.bg", "male")
        self.panda_network = PandaSocialNetwork()

    def test_is_panda_network_valid(self):
        self.assertTrue(isinstance(self.panda_network, PandaSocialNetwork))

    def test_is_panda_added_in_network(self):
        self.panda_network.add_panda(self.panda1)
        self.assertTrue(self.panda_network.has_panda(self.panda1))

    def test_is_panda_already_in_network(self):
        self.panda_network.add_panda(self.panda1)
        with self.assertRaises(PandaAlreadyThere):
            self.panda_network.add_panda(self.panda1)

    def test_if_make_friends_adds_to_network(self):
        self.panda_network.make_friends(self.panda1, self.panda2)
        self.assertTrue(self.panda_network.has_panda(self.panda1) and self.panda_network.has_panda(self.panda2))

    def test_are_pandas_already_friends(self):
        self.panda_network.make_friends(self.panda1, self.panda2)
        with self.assertRaises(PandasAlreadyFriends):
            self.panda_network.make_friends(self.panda1, self.panda2)

    def test_panda_make_friends_and_friends_of(self):
        self.panda_network.make_friends(self.panda1, self.panda2)
        self.assertEqual(self.panda_network.friends_of(self.panda1), [self.panda2])

    def test_connection_level(self):
        self.panda_network.make_friends(self.panda1, self.panda2)
        self.panda_network.make_friends(self.panda1, self.panda3)
        self.panda_network.make_friends(self.panda2, self.panda4)

        self.panda_network.add_panda(self.panda6)

        self.assertEqual(self.panda_network.connection_level(self.panda1, self.panda2), 1)
        self.assertEqual(self.panda_network.connection_level(self.panda2, self.panda3), 2)
        self.assertEqual(self.panda_network.connection_level(self.panda3, self.panda4), 3)
        self.assertEqual(self.panda_network.connection_level(self.panda3, self.panda5), False)
        self.assertEqual(self.panda_network.connection_level(self.panda3, self.panda6), -1)

    def test_are_connected(self):
        self.panda_network.make_friends(self.panda1, self.panda2)
        self.panda_network.make_friends(self.panda1, self.panda3)
        self.panda_network.make_friends(self.panda2, self.panda4)

        self.panda_network.add_panda(self.panda6)

        self.assertEqual(self.panda_network.are_connected(self.panda1, self.panda2), True)
        self.assertEqual(self.panda_network.are_connected(self.panda2, self.panda3), True)
        self.assertEqual(self.panda_network.are_connected(self.panda3, self.panda5), False)
        self.assertEqual(self.panda_network.are_connected(self.panda3, self.panda6), False)

    def test_how_many_genders(self):
        self.panda_network.make_friends(self.panda1, self.panda2)
        self.panda_network.make_friends(self.panda1, self.panda3)
        self.panda_network.make_friends(self.panda3, self.panda4)
        self.panda_network.make_friends(self.panda2, self.panda4)

        self.assertEqual(self.panda_network.how_many_gender_in_network(1, self.panda1, "female"), 1)
        self.assertEqual(self.panda_network.how_many_gender_in_network(2, self.panda1, "female"), 2)
        self.assertEqual(self.panda_network.how_many_gender_in_network(1, self.panda1, "male"), 1)

    def test_save_and_load_with_pickle(self):
        self.panda_network.make_friends(self.panda1, self.panda2)
        self.panda_network.make_friends(self.panda1, self.panda3)

        self.panda_network.save('panda_book.bin')

        panda_new_network = PandaSocialNetwork()

        panda_new_network.load('panda_book.bin')

        self.assertEqual(panda_new_network.are_friends(self.panda1, self.panda2), True)
        self.assertEqual(panda_new_network.are_friends(self.panda2, self.panda3), False)


if __name__ == '__main__':
    unittest.main()
