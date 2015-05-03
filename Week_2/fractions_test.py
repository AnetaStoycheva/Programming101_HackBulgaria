from fractions import Fraction
import unittest


class FractionTest(unittest.TestCase):
    def setUp(self):
        self.a = Fraction(3, 2)
        self.b = Fraction(6, 4)
        self.c = Fraction(3, 5)

    def test_equal_fractions(self):

        self.assertEqual(self.a, self.b)
        self.assertEqual(self.a, self.a)

    def test_not_equal_fractions(self):
        self.assertNotEqual(self.a, self.c)

    def test_add_fractions(self):
        self.assertEqual((self.a + self.b), Fraction(6, 2))
        self.assertEqual((self.a + self.c), Fraction(42, 20))

    def test_multiply_fractions(self):
        self.assertEqual((self.a * self.b), Fraction(9, 4))

    def test_subtract_fractions(self):
        self.assertEqual((self.a - self.b), Fraction(0, 9))
        self.assertEqual((self.c - self.a), Fraction(9, -10))

if __name__ == '__main__':
    unittest.main()
