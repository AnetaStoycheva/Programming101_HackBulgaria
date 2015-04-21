from sys import argv

for index in range(1, len(argv)):

    txt = open(argv[index], "r")
    content = txt.read()

    print(content)
    if index != len(argv) - 1:
        print()

    txt.close()
