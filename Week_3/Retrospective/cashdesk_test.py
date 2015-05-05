import unittest
from cashdesk import Bill, BatchBill, CashDesk


class TestBill(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(10, '$')
        self.bill2 = Bill(20, '$')
        self.bill3 = Bill(10, '$')

    def test_can_make_bill(self):
        self.assertTrue(isinstance(self.bill, Bill))

    def test_is_amount_valid_type(self):
        with self.assertRaises(TypeError) as context:
            Bill('10', '$')
        self.assertEqual(str(context.exception), 'The amount of this bill is not an integer.')

    def test_int(self):
        self.assertEqual(int(self.bill), 10)
        self.assertEqual(int(self.bill2), 20)

    def test_str(self):
        self.assertEqual(str(self.bill), '10$')

    def test_are_equal(self):
        self.assertEqual(self.bill, self.bill3)

    def test_are_not_equal(self):
        self.assertNotEqual(self.bill, self.bill2)

    def test_can_put_bill_in_a_dictionary(self):
        dictionary = {}
        dictionary[self.bill] = 1
        self.assertTrue(self.bill in dictionary)


class TestBatchBill(unittest.TestCase):
    def setUp(self):
        self.bills = BatchBill([Bill(10, '$'), Bill(20, '$'), Bill(10, '$'), Bill(30, '$')])

    def test_str(self):
        self.assertEqual([str(bill) for bill in self.bills], ['10$', '20$', '10$', '30$'])

    def test_len(self):
        self.assertEqual(len(self.bills), 4)

    def test_getitem(self):
        index = 2
        index2 = -1
        self.assertEqual(self.bills[index], Bill(10, '$'))
        self.assertNotEqual(self.bills[index2], Bill(33, '$'))

    def test_total(self):
        self.assertEqual(self.bills.total(), 70)


class TestCashDesk(unittest.TestCase):
    def setUp(self):
        self.cash_desk = CashDesk()
        self.bill = Bill(10, '$')
        self.bills = BatchBill([Bill(10, '$'), Bill(20, '$'), Bill(10, '$'), Bill(30, '$')])

    def test_take_bill(self):
        self.cash_desk.take_money(self.bill)
        self.assertEqual(self.cash_desk.total(), 10)

    def test_take_batch_bill(self):
        self.cash_desk.take_money(self.bills)
        self.assertEqual(self.cash_desk.total(), 70)

# if we write inspect method in cashdesk.py with 'return' we can test it
    def test_inspect(self):
        pass


if __name__ == '__main__':
    unittest.main()
