from math import sqrt


def fill_tetrahedron(num):

    return ((num ** 3) / (6 * sqrt(2))) / 1000


def main():
    print(fill_tetrahedron(100))
    print("{0:.2f}".format(fill_tetrahedron(100)))

    print(fill_tetrahedron(200))
    print(fill_tetrahedron(160))
    print(fill_tetrahedron(110))

if __name__ == '__main__':
    main()
