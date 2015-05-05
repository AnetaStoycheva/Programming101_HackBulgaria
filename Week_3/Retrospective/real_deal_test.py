import unittest
import real_deal


class TestRealDeal(unittest.TestCase):
    def test_sum_of_all_divisors(self):
        self.assertEqual(real_deal.sum_of_divisors(8), 15)
        self.assertEqual(real_deal.sum_of_divisors(1), 1)
        self.assertEqual(real_deal.sum_of_divisors(1000), 2340)

    def test_is_prime(self):
        self.assertEqual(real_deal.is_prime(1), False)
        self.assertTrue(real_deal.is_prime(2))
        self.assertFalse(real_deal.is_prime(8))
        self.assertFalse(real_deal.is_prime(-10))

    def test_prime_number_of_divisors(self):
        self.assertEqual(real_deal.prime_number_of_divisors(7), True)
        self.assertFalse(real_deal.prime_number_of_divisors(8))
        self.assertTrue(real_deal.prime_number_of_divisors(9))

    def test_if_digit_is_in_the_given_number(self):
        self.assertEqual(real_deal.contains_digit(123, 4), False)
        self.assertEqual(real_deal.contains_digit(42, 2), True)
        self.assertEqual(real_deal.contains_digit(1000, 0), True)

    def test_if_number_contains_all_given_digits(self):
        self.assertEqual(real_deal.contains_digits(402123, [0, 3, 4]), True)
        self.assertEqual(real_deal.contains_digits(666, [6, 4]), False)
        self.assertEqual(real_deal.contains_digits(456, []), True)

    def test_is_number_balanced(self):
        self.assertEqual(real_deal.is_number_balanced(9), True)
        self.assertEqual(real_deal.is_number_balanced(11), True)
        self.assertEqual(real_deal.is_number_balanced(13), False)
        self.assertEqual(real_deal.is_number_balanced(4518), True)
        self.assertEqual(real_deal.is_number_balanced(28471), False)

    def test_counting_substrings(self):
        self.assertEqual(real_deal.count_substrings('This is a test string', 'is'), 2)
        self.assertEqual(real_deal.count_substrings('babababa', 'baba'), 2)
        self.assertEqual(real_deal.count_substrings('We have nothing in common!', 'really?'), 0)

    def test_zero_insertion(self):
        self.assertEqual(real_deal.zero_insert(116457), 10160457)
        self.assertEqual(real_deal.zero_insert(55555), 505050505)
        self.assertEqual(real_deal.zero_insert(1), 1)
        self.assertEqual(real_deal.zero_insert(6446), 6040406)

    def test_sum_all_numbers_in_matrix(self):
        self.assertEqual(real_deal.sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)
        self.assertEqual(real_deal.sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)

    def test_matrix_bombing_plan(self):
        result = {(0, 0): 42, (0, 1): 36, (0, 2): 37, (1, 0): 30, (1, 1): 15,\
                  (1, 2): 23, (2, 0): 29, (2, 1): 15, (2, 2): 26}
        self.assertEqual(real_deal.matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), result)


if __name__ == '__main__':
    unittest.main()
