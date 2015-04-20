def caesar_encrypt(string, n):

    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_upper = letters.upper()
    letter_index = ''

    result = ''

    for index in range(0, len(string)):

        if string[index] in letters:
            letter_index = letters.index(string[index])
            result += letters[(letter_index + n) % len(letters)]

        elif string[index] in letters_upper:
            letter_index = letters_upper.index(string[index])
            result += letters_upper[(letter_index + n) % len(letters)]

        else:
            result += string[index]

    return result


def main():
    print(caesar_encrypt('fd', 4))
    print(caesar_encrypt('AaBb', 2))
    print(caesar_encrypt(';) a', 2))
    print(caesar_encrypt("abc", 1))
    print(caesar_encrypt("ABC", 1))
    print(caesar_encrypt("abc", 2))
    print(caesar_encrypt("aaa", 7))
    print(caesar_encrypt("xyz", 1))


if __name__ == '__main__':
    main()
