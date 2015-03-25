def factorial(n):
    result = 1

    for a in range(1, n + 1):
        result = result * a

    return result


def fibonacci(n):
    result = [1, 1]

    if n == 1:
        return [1]

    for a in range(2, n):
        result.append(result[-1] + result[-2])

    return result


def series(series_name, n):
    if series_name == "fibonacci":
        a = 1
        b = 1
    elif series_name == "lucas":  # redicata na Lucas
        a = 2
        b = 1
    else:
        a = 0
        b = 0

    result = []

    while len(result) != n:

        result.append(a)

        next_fib = a + b
        a = b  # razmenqme mestata na a i b (i na dolniq red)
        b = next_fib

    return result


# moje i sys sum/ moje i da go napravim na string a = '...'
# i sled tova [x for x in a] (list comprehension)
# ili re6enie na 1 red -> return sum(to_digits(n))

def sum_of_digits(n):

    result = 0

    if n < 0:
        n = n * (-1)  # ili abs(n)/ ili n = -n

    while n > 0:

        last_digit = n % 10
        result += last_digit
        n = n // 10

    return result


def fact_digits(n):
    result = 0
    digits_of_n = []

    while n > 0:
        digit = n % 10
        digits_of_n.append(digit)
        n = n // 10

    for item in digits_of_n:
        result += factorial(item)

    return result


def fact_digits2(n):
    return sum([factorial(x) for x in to_digits(n)])  # s 2 dr f-cii


def palindrome(obj):
    obj = str(obj)
    obj_reversed = obj[-1:: -1]

    return obj == obj_reversed


def to_digits(n):
    result = []

    while n > 0:
        digit = n % 10
        result.append(digit)
        n = n // 10

    return result[-1:: -1]


def to_digits_compehension(n):
    return [int(x) for x in str(n)]


def count_digits(n):  # 6te ni trqbva za dolnata f-ciq
    return sum([1 for x in to_digits_compehension(n)])


def to_number(digits):
    result = 0

    for digit in digits:
        broj_cifri = count_digits(digit)  # taka znaem kolko 0-li da osvobodim
        result = result * (10 ** broj_cifri) + digit  # osvobojdavame si 0-li

    return result


def fib_number(n):

    result = ''
    list_fibs = fibonacci(n)

    for a in list_fibs:
        result += str(a)

    return result


# vyzmojno e, za6toto modificirehme to_number(digits): / da osvobojdava nuli
def fibonacci_number(n):
    return to_number(fibonacci(n))


def count_vowels(string):

    vowels = "aeiouyAEIOUY"
    result = 0

    for item in string:
        if item in vowels:
            result += 1

    return result


def count_consonants(string):

    counter = 0
    cons = "bcdfghjklmnpqrstvwxz"
    cons2 = cons.upper()
    consonants = cons + cons2

    for item in string:
        if item in consonants:
            counter += 1

    return counter


def char_histogram(string):  # ili s .count() i dict comprehension

    dictionary = {}

    for a in string:
        if a not in dictionary:  # proverqvame za klu4
            dictionary[a] = 1
        else:
            dictionary[a] += 1

    return dictionary


def p_score(n):
    result = 0

    if palindrome(n):  # == True
        result += 1

        return result

    else:
        # prevr 4isloto n v spisyk ot cifrite mu i sys slising obry6tam spisyka
        reversed_n = to_digits(n)[-1:: -1]

        # obyrnatiq spisyk go pravim na 4islo i go polzvame s pyrvoto 4islo
        n_reverse = to_number(reversed_n)
        suma = n + n_reverse
        result = 1 + p_score(suma)

        return result


def is_increasing(seq):

    for a in range(0, len(seq) - 1):  # za da vzema do predposledniq element
        if seq[a] < seq[a + 1]:
            pass
        else:
            return False

    return True


def is_decreasing(seq):

    for index in range(0, len(seq) - 1):
        if seq[index] > seq[index + 1]:
            pass
        else:
            return False

    return True


def sum_digits_binary(bin_n):

    total = 0

    while bin_n > 0:

        last_digit = bin_n % 2  # delim na 2, za6toto sme v 2-na brojna sistema
        total += last_digit
        bin_n = bin_n // 2

    return total


def next_hack(n):

    current_n = n + 1

    while True:

        # bin vry6ta 0b101 primerno (zatova vzimame ot 3tiq element)
        if palindrome(bin(current_n)[2:]):

            if sum_digits_binary(current_n) % 2 == 1:
                return current_n  # taka e po uslovie
            else:
                pass  # taka e po uslovie

        current_n += 1  # za da ne zaciklim ili da sprem sled 2to 4islo palindr


def main():

    # print(factorial(0))
    # print(factorial(1))
    # print(factorial(5))
    # print(fibonacci(1))
    # print(fibonacci(2))
    # print(fibonacci(3))
    # print(fibonacci(10))
    # print(series("fibonacci", 3))
    # print(series("lucas", 5))
    # print(sum_of_digits(1325132435356))
    # print(sum_of_digits(123))
    # print(sum_of_digits(6))
    # print(sum_of_digits(-10))
    # print(fact_digits(111))
    # print(fact_digits(100))
    # print(fact_digits(145))
    # print(fact_digits(999))
    # print(fact_digits2(111))
    # print(fact_digits2(100))
    # print(fact_digits2(145))
    # print(fact_digits2(999))
    # print(palindrome(121))
    # print(palindrome("kapak"))
    # print(palindrome('baba'))
    # print(to_digits(123))
    # print(to_digits(99999))
    # print(to_digits(123023))
    # print(to_digits_compehension(123))
    # print(to_digits_compehension(99999))
    # print(to_digits_compehension(123023))
    # print(count_digits(123))
    # print(count_digits(9999))
    # print(to_number([1, 2, 3]))
    # print(to_number([9, 9, 9, 9]))
    # print(to_number([1, 2, 3, 0, 2, 3]))
    # print(fib_number(3))
    # print(fib_number(10))
    # print(fibonacci_number(3))
    # print(fibonacci_number(10))
    # print(count_vowels("Python"))
    # print(count_vowels("Theistareykjarbunga"))
    # print(count_vowels("grrrrgh!"))
    # print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    # print(count_vowels("A nice day to code!"))
    # print(count_consonants("Python"))
    # print(count_consonants("Theistareykjarbunga"))
    # print(count_consonants("grrrrgh!"))
    # print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
    # print(count_consonants("A nice day to code!"))
    # print(char_histogram("Python!"))
    # print(char_histogram('AAAAaaa!!!'))
    # print(p_score(121))
    # print(p_score(48))
    # print(p_score(198))
    # print(is_increasing([1, 2, 3, 4, 5]))
    # print(is_increasing([1]))
    # print(is_increasing([5, 6, -10]))
    # print(is_increasing([1, 1, 1, 1]))
    # print(is_decreasing([5, 4, 3, 2, 1]))
    # print(is_decreasing([1, 2, 3]))
    # print(is_decreasing([100, 50, 20]))
    # print(is_decreasing([1, 1, 1, 1]))
    print(sum_digits_binary(10))
    print(sum_digits_binary(100))
    print(sum_digits_binary(101))
    # print(next_hack(0))
    # print(next_hack(6))
    # print(next_hack(10))
    # print(next_hack(8031))


if __name__ == '__main__':
    main()
