import calendar


def count_words(arr):

    result = {}

    for element in arr:
        if element not in result:
            result[element] = 1
        else:
            result[element] += 1

    return result


def count_words2(arr):
    return {key: arr.count(key) for key in arr}


def unique_words_count(arr):

    result = 0
    dictionary = {}

    for element in arr:
        if element not in dictionary:
            dictionary[element] = 1
        else:
            dictionary[element] += 1

    for key in dictionary:
        result += 1

    return result


def unique_words(arr):
    return len([key for key in count_words2(arr)])


def unique_words2(arr):
    return len(set(arr))


def nan_expand(times):

    result = 'Not a '

    if times > 0:
        return result * times + 'NaN'
    else:
        return ''


def is_nan_expand(string):

    n = len(string) // len('Not a ')
    result = 'Not a ' * n + 'NaN'

    if string == result:
        return True
    elif string == '':
        return True
    else:
        return False


def iterations_of_nan_expand(expanded):

    if is_nan_expand(expanded):
        n = len(expanded) // len('Not a ')

        return n

    return False


# 6te vyrne spisyk bez povtarq6ti se elementi, kojto 6te e podreden spored
# na4alno zadadeniq, a set() vry6ta razbyrkano (no e 1 red :D)
def dedup(items):  # de-duplication

    found = set()
    result = []

    for item in items:
        if item not in found:
            result.append(item)
            found.add(item)

    return result


def is_prime(n):

    if n <= 1:
        return False

    for a in range(2, n):
        if n % a == 0:
            return False

    return True


def next_prime(n):

    n += 1  # uveli4avame go otsega, za da vzemem sledva6toto

    while not is_prime(n):
        n += 1

    return n


# ZA DOLNATA: ? pyti moje da razdelim 40/2 celo4isleno
# 40/2 = 1 pyt; 20/2 = 2ri pyt; 10/2 - 3ti pyt
def divide_count(n, k):

    times = 0

    while n != 1 and n % k == 0:
        times += 1
        n = n // k

    return times


def prime_factorization(n):

    result = []
    current_prime = 2

    while n > 1:
        times = divide_count(n, current_prime)

        if times != 0:
            result.append((current_prime, times))
            n = n // current_prime ** times

        current_prime = next_prime(current_prime)

    return result


def counter_of_dividers(n, prime_number):

    divider_counter = 0

    while n % prime_number == 0:
        divider_counter += 1
        n /= prime_number

    return divider_counter


def prime_factorization2(n):

    primes = [x for x in range(2, n + 1) if is_prime(x)]

    return [(num, counter_of_dividers(n, num)) for num in primes
            if counter_of_dividers(n, num) != 0]


# def take_first(a_list):

#     result = []

#     for a in range(0, len(a_list) - 1):
#         if a_list[a] == a_list[a + 1]:
#             result = a_list[a]
#             result += a_list[a]

#     return result


def take_same(items):

    first_item = items[0]
    index = 1
    result = [first_item]

    while index < len(items) and items[index] == first_item:
        result.append(items[index])
        index += 1

    return result


def group(items):

    result = []

    while len(items) > 0:
        current_group = take_same(items)
        result.append(current_group)

        items = items[len(current_group):]

    return result


def max_consecutive(items):
    return max([len(g) for g in group(items)])


def groupby(func, seq):

    result = {}

    for element in seq:
        if func(element) in result:
            result[func(element)].append(element)
        else:
            result[func(element)] = [element]

    return result


def prepare_meal(number):

    result = ''

    while number % 3 == 0 and number != 0:
        result += "spam "
        number = number / 3
    result = result[0:-1]

    if number % 5 == 0 and number != 0:
        if len(result) == 0:
            result += "eggs"
        else:
            result += " and eggs"

    return result


def reduce_file_path(path):
    # mahame '/' i ' '
    # pravim go na spisyk, posle 6te go prevyrnem obratno v string
    # split-vame po '/'
    result = []
    parts = [part for part in path.split("/") if part not in [".", ""]]

    while len(parts) != 0:
        part = parts.pop()  # maha posledniq element

        if part == "..":
            if len(parts) != 0:
                parts.pop()
        else:
            result.insert(0, part)

    return "/" + "/".join(result)


# def same_letters(letter, string):

#     result = []

#     for a in string:
#         if a == letter:
#             result.append('True')
#         else:
#             result.append('False')

#     return result


def same_characters(string):  # T ot F
    return all([string[0] == ch for ch in string])


def is_an_bn(word):

    if len(word) % 2 == 0:
        a = word[:int(len(word) / 2)]
        print(a)
        b = word[int(len(word) / 2):]
        print(b)

        return same_characters(a) and same_characters(b)

    return False


def to_digits(number):

    result = []

    while number > 0:
        result.append(number % 10)
        number = number // 10

    return result


# def sum_digits(number):
#     return sum(to_digits(number))


def count_digits(number):

    counter = 0

    for n in str(number):
        counter += 1

    return counter


def is_credit_card_valid(number):

    result = 0
    list_numbers = to_digits(number)

    if count_digits(number) % 2 != 0:

        for index in range(0, len(str(number))):

            if index % 2 != 0:
                result += sum(to_digits(list_numbers[index] * 2))
            else:
                result += list_numbers[index]

        return result % 10 == 0

    return False


def goldbach(n):

    result = []
    primes = [x for x in range(2, n + 1) if is_prime(x)]

    for a in primes:
        if a <= n / 2:
            result.append([(a, b) for b in primes if a + b == n])

    return [res[0] for res in result if res != []]


def magic_square(matrix):

    s = []

    for row in matrix:
        s.append(sum(row))

    for column_index in range(0, len(matrix)):
        s.append(sum([row[column_index] for row in matrix]))

    s.append(sum([matrix[i][i] for i in range(0, len(matrix))]))

    s.append(sum([matrix[j][len(matrix) - j - 1] for j in range(0, len(matrix))]))

    return all([s[0] == s[i] for i in range(0, len(s))])


def friday_years(start, end):

    result = 0

    for year in range(start, end + 1):
        fridays_in_year = 0
        for month in range(1, 13):
            weeks = calendar.monthcalendar(year, month)
            for row in weeks:
                if row[4] != 0:
                    fridays_in_year += 1

        if fridays_in_year == 53:
            result += 1

    return result


def main():
    # print(count_words(["apple", "banana", "apple", "pie"]))
    # print(count_words(["python", "python", "python", "ruby"]))
    # print(count_words2(["apple", "banana", "apple", "pie"]))
    # print(count_words2(["python", "python", "python", "ruby"]))
    # print(unique_words_count(["apple", "banana", "apple", "pie"]))
    # print(unique_words_count(["python", "python", "python", "ruby"]))
    # print(unique_words_count(["HELLO!"] * 10))
    # print(unique_words(["apple", "banana", "apple", "pie"]))
    # print(unique_words(["HELLO!"] * 10))
    # print(unique_words2(["apple", "banana", "apple", "pie"]))
    # print(unique_words2(["HELLO!"] * 10))
    # print(dedup(['Aaa', "sdasf", 'Aaa', '23324d']))  # vry6ta set ot tqh
    # print(nan_expand(0))
    # print(nan_expand(1))
    # print(nan_expand(2))
    # print(nan_expand(3))
    # print((is_nan_expand('')))
    # print((is_nan_expand("Not a NaN")))  # True
    # print((is_nan_expand("Show these people!")))
    # print(iterations_of_nan_expand(""))
    # print(iterations_of_nan_expand("Not a NaN"))
    # print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
    # print(iterations_of_nan_expand("Show these people!"))
    # print(is_prime(22))
    # print(is_prime(0))
    # print(next_prime(9))
    # print(divide_count(2, 40))
    # print(divide_count(40, 2))
    # print(divide_count(20, 5))
    # print(prime_factorization(10))
    # print(prime_factorization(14))
    # print(prime_factorization(356))
    # print(prime_factorization(1000))
    # print(counter_of_dividers(7, 3))  # 0
    # print(counter_of_dividers(100, 3))  # 0
    # print(counter_of_dividers(9, 3))  # 2
    # print(take_first([1, 2, 3, 4]))  # vry6ta [], za6toto nikoj el ne e = sledv
    # print(take_first([3, 3, 3, 8, 11]))  # ?
    # print(take_first([1, 1, 2, 1, 4, 5]))
    # print(take_same([5, 5, 5, 7, 6, 7]))
    # print(take_same([5, 5, 4, 1, 1]))
    # print(group([1, 1, 1, 2, 3, 1, 1]))
    # print(group([1, 2, 1, 2, 3, 3]))
    # print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
    # print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
    # print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
    # print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
    # print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))
    # print(prepare_meal(5))  # "eggs"
    # print(prepare_meal(3))  # "spam"
    # print(prepare_meal(27))  # "spam spam spam"
    # print(prepare_meal(15))  # "spam and eggs"
    # print(prepare_meal(45))  # "spam spam and eggs"
    # print(prepare_meal(7))  # ""
    # print(reduce_file_path("/"))
    # print(reduce_file_path("/srv/../"))
    # print(reduce_file_path("/srv/www/htdocs/wtf/"))
    # print(reduce_file_path("/srv/www/htdocs/wtf"))
    # print(reduce_file_path("/srv/./././././"))
    # print(reduce_file_path("/etc//wtf/"))
    # print(reduce_file_path("/etc/../etc/../etc/../"))
    # print(reduce_file_path("//////////////"))
    # print(reduce_file_path("/../"))
    # print(same_letters('a', 'aaaab'))
    # print(same_letters(0, '000'))
    # print(same_characters('aaa'))
    # print(is_an_bn(''))
    # print(is_an_bn("aaabb"))
    # print(is_an_bn('bbbaaa'))
    # print(is_an_bn('rado'))
    # print(is_an_bn("aabbaabb"))
    # print(is_an_bn("aaaaabbbbb"))
    # print(to_digits(245656))
    # print(sum_digits(245656))
    # print(count_digits(245656))
    # print(is_credit_card_valid(79927398713))
    # print(is_credit_card_valid(79927398715))
    # print(is_credit_card_valid(7992739871))
    # print(goldbach(4))
    # print(goldbach(6))
    # print(goldbach(8))
    # print(goldbach(10))
    # print(goldbach(100))
    # print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    # print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(magic_square([[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]))
    print(friday_years(1000, 2000))
    print(friday_years(1753, 2000))
    print(friday_years(1990, 2015))


if __name__ == '__main__':
    main()
