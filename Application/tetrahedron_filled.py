from math import sqrt


def fill_tetrahedron(num):

    return ((num ** 3) / (6 * sqrt(2))) / 1000


def tetrahedron_filled(tetrahedrons, water):

    counter = 0
    pyramids = sorted(tetrahedrons)

    for a in pyramids:

        obem = fill_tetrahedron(a)

        if obem < water:
            water -= obem
            counter += 1

        if water <= 0:
            break

    return counter


def main():

    print(tetrahedron_filled([100, 20, 30], 10))
    print(tetrahedron_filled([110, 160, 200], 1200))


if __name__ == '__main__':
    main()
