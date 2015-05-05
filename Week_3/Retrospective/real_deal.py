from warmup import to_digits, to_number, count_digits

import copy
import pprint


def sum_of_divisors(n):  # s n vklu4itelno

    result = 0

    for a in range(1, n + 1):
        if n % a == 0:
            result += a

    return result

# return sum([x for x in range(1, n + 1) if n % x == 0]) # 2ro re6enie :)


def is_prime(n):

    if n <= 1:
        return False

    for a in range(2, n):
        if n % a == 0:
            return False

    return True

# 2ro re6enie --> sumata na delitelite mu da e 1 + samoto 4islo
# t.e. -> return n + 1 == sum_of_divisors(n) / ot 2to re6enie na gornata f-ciq


def count_of_divisors(n):
    return sum([1 for x in range(1, n + 1) if n % x == 0])


# the divisors of 8 are 1, 2, 4 and 8, a total of 4. 4 is not a prime number.
# The divisors of 9 are 1, 3 and 9, a total of 3. 3 is a prime number.-> True
def prime_number_of_divisors(n):
    return is_prime(count_of_divisors(n))


def contains_digit(number, digit):

    number = str(number)
    digit = str(digit)

    return digit in number


def contains_digits(number, digits):

    result = []
    for a in digits:
        result.append(str(contains_digit(number, a)))

    if 'False' in result:
        return False
    else:
        return True

    # for digit in digits:
    #     if not contains_digit(number, digit):
    #         return False

    # return True


def is_number_balanced(n):

    numbers = to_digits(n)
    len_2 = len(numbers) // 2
    left_numbers = numbers[0: len_2]

    if len(numbers) % 2 == 0:
        right_numbers = numbers[len_2:]
    else:
        right_numbers = numbers[len_2 + 1:]

    return sum(left_numbers) == sum(right_numbers)


def count_substrings(haystack, needle):
    return haystack.count(needle)


def zero_insert(n):  # naj-dobre da go prevyrnem v spisyk ot cifri

    result = []
    digits = to_digits(n)

    start = 0  # tova 6te mi e pozicitq
    end = len(digits)

    while start < end - 1:
        x = digits[start]
        x_plus_1 = digits[start + 1]

        result.append(x)

        if (x + x_plus_1) % 10 == 0 or x == x_plus_1:
            result.append(0)  # slagame 0 mejdu 2te (ot uslovieto e taka)

        start += 1

    result.append(digits[start])

    return to_number(result)


def sum_matrix(m):

    result = 0

    for spisyk in m:
        result += sum(spisyk)

    return result


def sum_matrix2(matr):
    return sum([sum(row) for row in matr])


# za zada4ata s matrix_bombing_plan:

NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),  # Get to 1, 2 and 3
    (-1, 0), (1, 0),  # Get to 8 and 7
    (-1, 1), (0, 1), (1, 1)]  # Get to 9, 5 and 6


def within_bounds(m, at):  # matrica i tuple / vry6ta True/ false // garantiram si da ne izlqza ot matricata
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1  # dx = 0 i dy = 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            # This min() is not to go less than zero
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m   # vry6ta spisyk s novata matrica (sled udara na bombata)


def matrix_bombing_plan(m):

    result = {}

    for i in range(0, len(m)):  # broq na redovete
        for j in range(0, len(m[0])):  # broq na kolonite
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result


def main():
    # print(sum_of_divisors(8))
    # print(sum_of_divisors(1000))
    # print(is_prime(1))
    # print(is_prime(2))
    # print(is_prime(8))
    # print(is_prime(11))
    # print(is_prime(-7))
    # print(count_of_divisors(8))
    # print(count_of_divisors(7))
    # print(prime_number_of_divisors(7))
    # print(prime_number_of_divisors(8))
    # print(prime_number_of_divisors(9))
    # print(contains_digit(123, 4))
    # print(contains_digit(42, 2))
    # print(contains_digit(1000, 0))
    # print(contains_digit(12346789, 5))
    # print(contains_digits(402123, [0, 3, 4]))
    # print(contains_digits(666, [6, 4]))
    # print(contains_digits(123456789, [1, 2, 3, 0]))
    # print(contains_digits(456, []))
    # print(is_number_balanced(9))
    # print(is_number_balanced(11))
    # print(is_number_balanced(13))
    # print(is_number_balanced(121))
    # print(is_number_balanced(4518))
    # print(is_number_balanced(28471))
    # print(is_number_balanced(1238033))
    # print(count_substrings("This is a test string", "is"))
    # print(count_substrings("babababa", "baba"))
    # print(count_substrings("Python is an awesome language to program in!", "o"))
    # print(count_substrings("We have nothing in common!", "really?"))
    # print(count_substrings("This is this and that is this", "this"))
    # print(zero_insert(116457))
    # print(zero_insert(55555555))
    # print(zero_insert(1))
    # print(zero_insert(6446))
    # print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    # print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
    # print(sum_matrix2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(sum_matrix2([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    # print(sum_matrix2([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
    print(bomb([[1, 2, 3], [4, 5, 6], [7, 8, 9]], (0, 2)))  # [[1, 0, 3], [4, 2, 3], [7, 8, 9]]
    print(bomb([[1, 2, 3], [4, 5, 6], [7, 8, 9]], (2, 0)))  # [[1, 2, 3], [0, 0, 6], [7, 1, 9]]
    # print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    # m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # result = matrix_bombing_plan(m)

    # pp = pprint.PrettyPrinter()  # vry6ta gi podredeni
    # pp.pprint(result)


if __name__ == '__main__':
    main()


# ne6tata v main-a vry6tat:
# {(0, 0): 42,
#  (0, 1): 36,
#  (0, 2): 37,
#  (1, 0): 30,
#  (1, 1): 15,
#  (1, 2): 23,
#  (2, 0): 29,
#  (2, 1): 15,
#  (2, 2): 26}

# print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) - > vry6ta:
# {(0, 1): 36, (1, 2): 23, (0, 0): 42, (2, 0): 29, (1, 0): 30, (2, 2): 26, (0, 2): 37, (2, 1): 15, (1, 1): 15}
