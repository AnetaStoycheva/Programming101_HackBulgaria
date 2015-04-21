from sys import argv  # argv e spisyk s promenlivite mi


# vzimame tozi element ot spisyka argv i kazvame, 4e toj e na6iqt tekstov fail
# ne vzimame 0-iq element, za6toto tova e imeto na faila ni -> cat.py
filename = argv[1]

txt = open(filename, "r")
content = txt.read()

print(content)

txt.close()
