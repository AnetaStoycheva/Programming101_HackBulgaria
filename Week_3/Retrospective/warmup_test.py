import unittest
import warmup


class TestWarmUp(unittest.TestCase):
    def test_factorial_ok(self):
        self.assertEqual(warmup.factorial(0), 1)
        self.assertEqual(warmup.factorial(1), 1)
        self.assertEqual(warmup.factorial(5), 120)

    def test_fibonacci_ok(self):
        self.assertEqual(warmup.fibonacci(1), [1])
        self.assertEqual(warmup.fibonacci(2), [1, 1])
        self.assertEqual(warmup.fibonacci(9), [1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_sum_all_digits_of_a_number(self):
        self.assertEqual(warmup.sum_of_digits(1325132435356), 43)
        self.assertEqual(warmup.sum_of_digits(123), 6)
        self.assertEqual(warmup.sum_of_digits(-10), 1)

    def test_factorial_digits(self):
        self.assertEqual(warmup.fact_digits(111), 3)
        self.assertEqual(warmup.fact_digits(145), 145)
        self.assertEqual(warmup.fact_digits2(999), 1088640)

    def test_is_something_a_palindrome(self):
        self.assertEqual(warmup.palindrome(121), True)
        self.assertTrue(warmup.palindrome('kapak'))

    def test_something_isnt_a_palindrome(self):
        self.assertFalse(warmup.palindrome('baba'))

    def test_integer_to_a_list_of_its_digits(self):
        self.assertEqual(warmup.to_digits_comprehension(123), [1, 2, 3])
        self.assertEqual(warmup.to_digits(99999), [9, 9, 9, 9, 9])
        self.assertEqual(warmup.to_digits(123023), [1, 2, 3, 0, 2, 3])

    def test_turning_a_list_of_digits_into_a_number(self):
        self.assertEqual(warmup.to_number([1, 2, 3]), 123)
        self.assertEqual(warmup.to_number([9, 9, 9, 9, 9]), 99999)
        self.assertEqual(warmup.to_number([1, 2, 3, 0, 2, 3]), 123023)

    def test_fib_number_with_concatenating_fist_n_fibs(self):
        self.assertEqual(warmup.fib_number(10), 11235813213455)
        self.assertEqual(warmup.fibonacci_number(3), 112)

    def test_count_vowels(self):
        self.assertEqual(warmup.count_vowels('Python'), 2)
        self.assertEqual(warmup.count_vowels('Theistareykjarbunga'), 8)
        self.assertEqual(warmup.count_vowels('grrrgh!'), 0)
        self.assertEqual(warmup.count_vowels('A nice day to code!'), 8)

    def test_count_consonants(self):
        self.assertEqual(warmup.count_consonants('Python'), 4)
        self.assertEqual(warmup.count_consonants('Theistareykjarbunga'), 11)
        self.assertEqual(warmup.count_consonants('grrrgh!'), 6)

    def test_char_histogram(self):
        self.assertEqual(warmup.char_histogram('AAAAaaa!!!'), {'A': 4, '!': 3, 'a': 3})
        self.assertEqual(warmup.char_histogram("Python!"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})

    def test_palindrome_score(self):
        self.assertEqual(warmup.p_score(121), 1)
        self.assertEqual(warmup.p_score(48), 3)
        self.assertEqual(warmup.p_score(198), 6)

    def test_if_given_sequence_is_monotonously_increasing(self):
        self.assertEqual(warmup.is_increasing([1, 2, 3, 4, 5]), True)
        self.assertTrue(warmup.is_increasing([1]))
        self.assertFalse(warmup.is_increasing([5, 6, -10]))
        self.assertEqual(warmup.is_increasing([1, 1, 1, 1]), False)

    def test_if_given_sequence_is_monotonously_decreasing(self):
        self.assertEqual(warmup.is_decreasing([5, 4, 3, 2, 1]), True)
        self.assertEqual(warmup.is_decreasing([1, 2, 3]), False)
        self.assertEqual(warmup.is_decreasing([1, 1, 1, 1]), False)

    def test_next_hach_number(self):
        self.assertEqual(warmup.next_hack(0), 1)
        self.assertEqual(warmup.next_hack(10), 21)
        self.assertEqual(warmup.next_hack(8031), 8191)


if __name__ == '__main__':
    unittest.main()
