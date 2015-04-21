from sys import argv


def sum_numbers(input_file):

    result = [int(x) for x in input_file.read().split(" ")]
    return sum(result)


def main():

    file_name = argv[1]

    with open(file_name, 'r') as f:
        print(sum_numbers(f))


if __name__ == '__main__':
    main()
