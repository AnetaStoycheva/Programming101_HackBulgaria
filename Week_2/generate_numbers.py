from sys import argv
from random import randint


def generate_numbers(n):  # priema 2ri argument filename pri puskaneto v Py
    return [randint(1, 1000) for i in range(n)]


def main():

    numbs = [str(numb) for numb in generate_numbers(int(argv[2]))]

    with open(argv[1], 'w') as f:
        f.write(" ".join(numbs))
        f.write("\n")

if __name__ == '__main__':
    main()
