import os
from sys import argv


file_triples = os.walk(argv[1])

result = 0

for item in file_triples:
    for element in item[-1]:
        a = os.path.join(item[0], element)
        try:
            result += os.path.getsize(a)
        except (FileNotFoundError, OSError) as error:
            print(error)

print("{0:.2f}".format(result / 1024) + ' KB')
