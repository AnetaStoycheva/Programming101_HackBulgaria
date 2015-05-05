import unittest
import final_round


class TestFinalRound(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(final_round.count_words(["apple", "banana", "apple", "pie"]), {'apple': 2, 'pie': 1, 'banana': 1})
        self.assertEqual(final_round.count_words(["python", "python", "python", "ruby"]), {'ruby': 1, 'python': 3})

    def test_the_number_of_different_words_given(self):
        self.assertEqual(final_round.unique_words_count(["apple", "banana", "apple", "pie"]), 3)
        self.assertEqual(final_round.unique_words_count(["python", "python", "python", "ruby"]), 2)
        self.assertEqual(final_round.unique_words_count(["HELLO!"] * 10), 1)

    def test_nan_expand(self):
        self.assertEqual(final_round.nan_expand(0), '')
        self.assertEqual(final_round.nan_expand(1), 'Not a NaN')
        self.assertEqual(final_round.nan_expand(2), 'Not a Not a NaN')
        self.assertEqual(final_round.nan_expand(3), 'Not a Not a Not a NaN')

    def test_iterations_of_nan_expand(self):
        self.assertEqual(final_round.iterations_of_nan_expand(''), 0)
        self.assertEqual(final_round.iterations_of_nan_expand('Not a NaN'), 1)
        self.assertEqual(final_round.iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'), 10)
        self.assertEqual(final_round.iterations_of_nan_expand('Show these people!'), False)

    def test_integer_prime_factorization(self):
        self.assertEqual(final_round.prime_factorization(10), [(2, 1), (5, 1)])
        self.assertEqual(final_round.prime_factorization(89), [(89, 1)])
        self.assertEqual(final_round.prime_factorization(356), [(2, 2), (89, 1)])
        self.assertEqual(final_round.prime_factorization(1000), [(2, 3), (5, 3)])

    def test_the_group_function(self):
        self.assertEqual(final_round.group([1, 1, 1, 2, 3, 1, 1]), [[1, 1, 1], [2], [3], [1, 1]])
        self.assertEqual(final_round.group([1, 2, 1, 2, 3, 3]), [[1], [2], [1], [2], [3, 3]])

    def test_max_consecutive(self):
        self.assertEqual(final_round.max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]), 4)
        self.assertEqual(final_round.max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]), 3)

    def test_group_by(self):
        self.assertEqual(final_round.groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]), {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]})
        self.assertEqual(final_round.groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]), {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]})
        self.assertEqual(final_round.groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]), {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]})

    def test_prepare_meal(self):
        self.assertEqual(final_round.prepare_meal(5), 'eggs')
        self.assertEqual(final_round.prepare_meal(3), 'spam')
        self.assertEqual(final_round.prepare_meal(27), 'spam spam spam')
        self.assertEqual(final_round.prepare_meal(15), 'spam and eggs')
        self.assertEqual(final_round.prepare_meal(7), '')

    def test_reduce_file_path(self):
        self.assertEqual(final_round.reduce_file_path('/'), '/')
        self.assertEqual(final_round.reduce_file_path('/srv/../'), '/')
        self.assertEqual(final_round.reduce_file_path('/srv/www/htdocs/wtf'), '/srv/www/htdocs/wtf')
        self.assertEqual(final_round.reduce_file_path('/srv/./././././'), '/srv')
        self.assertEqual(final_round.reduce_file_path('/etc/../etc/../etc/../'), '/')
        self.assertEqual(final_round.reduce_file_path('//////////////'), '/')
        self.assertEqual(final_round.reduce_file_path('/../'), '/')

    def test_if_word_is_from_an_bn_language(self):
        self.assertEqual(final_round.is_an_bn(''), True)
        self.assertEqual(final_round.is_an_bn('rado'), False)
        self.assertEqual(final_round.is_an_bn('aaabb'), False)
        self.assertEqual(final_round.is_an_bn('aaabbb'), True)
        self.assertEqual(final_round.is_an_bn('aabbaabb'), False)
        self.assertEqual(final_round.is_an_bn('bbbaaa'), False)
        self.assertEqual(final_round.is_an_bn('aaaaabbbbb'), True)
        self.assertEqual(final_round.is_an_bn('  '), False)

    def test_is_credit_card_valid(self):
        self.assertEqual(final_round.is_credit_card_valid(79927398713), True)
        self.assertEqual(final_round.is_credit_card_valid(79927398715), False)

    def test_goldbach_conjecture(self):
        self.assertEqual(final_round.goldbach(4), [(2, 2)])
        self.assertEqual(final_round.goldbach(8), [(3, 5)])
        self.assertEqual(final_round.goldbach(10), [(3, 7), (5, 5)])
        self.assertEqual(final_round.goldbach(100), [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)])

    def test_magic_square(self):
        self.assertEqual(final_round.magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), False)
        self.assertEqual(final_round.magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]), True)
        self.assertEqual(final_round.magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

    def test_friday_years(self):
        self.assertEqual(final_round.friday_years(1000, 2000), 178)
        self.assertEqual(final_round.friday_years(1753, 2000), 44)
        self.assertEqual(final_round.friday_years(1990, 2015), 4)


if __name__ == '__main__':
    unittest.main()
