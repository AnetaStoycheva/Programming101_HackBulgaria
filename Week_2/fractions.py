class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return '{} / {}'.format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.numerator * other.denominator ==\
            self.denominator * other.numerator

    def __add__(self, other):
        return Fraction((self.numerator * other.denominator + other.numerator *
            self.denominator), (self.denominator * other.denominator))

    def __mul__(self, other):
        return Fraction((self.numerator * other.numerator), (self.denominator * other.denominator))

    def __sub__(self, other):
        return Fraction((self.numerator * other.denominator) - (other.numerator
            * self.denominator), (self.denominator * other.denominator))
