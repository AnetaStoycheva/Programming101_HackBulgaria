from bank import BankAccount
import unittest


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount('Annie', 2000, 'BGN')
        self.account2 = BankAccount('Gosho', 350, 'grosh')
        self.account3 = BankAccount('Stef4o', 45, 'grosh')

    def test_can_create_bank_account(self):
        self.assertTrue(isinstance(self.account, BankAccount))
        self.assertTrue(isinstance(self.account2, BankAccount))

    def test_deposit(self):
        self.account.deposit(300)
        self.assertEqual(self.account.balance(), 2300)

    def test_can_withdraw(self):
        self.assertTrue(self.account.withdraw(800))
        self.assertEqual(self.account.balance(), 1200)

    def test_cannot_withdraw(self):
        self.assertFalse(self.account.withdraw(4500))
        self.assertEqual(self.account.balance(), 2000)

    def test_can_withdraw_till_the_end(self):
        self.assertTrue(self.account.withdraw(2000))
        self.assertEqual(self.account.balance(), 0)

    def test_str(self):
        self.assertEqual(str(self.account), 'Bank account for Annie with balance of 2000BGN')

    def test_int(self):
        self.assertEqual(int(self.account), 2000)

    def test_cannot_transfer_with_different_currencies(self):
        self.assertFalse(self.account.transfer_to(self.account2, 900))

    def test_can_transfer_to(self):
        self.assertTrue(self.account2.transfer_to(self.account3, 55))
        self.assertEqual(self.account2.balance(), 295)
        self.assertEqual(self.account3.balance(), 100)

    def test_cannot_transfer_to(self):
        self.assertFalse(self.account2.transfer_to(self.account3, 400))
        self.assertEqual(self.account2.balance(), 350)
        self.assertEqual(self.account3.balance(), 45)

    def test_history(self):
        self.account.deposit(1000)
        self.account.balance()
        self.assertEqual(self.account.history(), ['Account was created',\
            'Deposited 1000BGN', 'Balance check -> 3000BGN'])

    def test_is_balance_int(self):
        pass

    def test_is_balance_bigger_than0(self):
        pass

if __name__ == '__main__':
    unittest.main()
