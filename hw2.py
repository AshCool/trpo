from re import *

"""
Вывести все имена классов, у которых есть публичные атрибуты или методы
"""

#  search for all classes
class_pattern = \
    compile(r"<packagedElement.*?name=\"([a-zA-Z0-9]*?)\"[^>]*?xmi:type=\"uml:Class\".*?>(.*?)</packagedElement>", S)
#  search for public attributes/operations
inner_pattern = \
    compile(r".*?((<ownedAttribute[^>]*?visibility=\"public\".*?/>)"
            r"|(<ownedOperation[^>]*?visibility=\"public\".*?/>)).*?", S)

#  trying to open file
while True:

    file_name = input("Введите имя файла: ")

    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print("File not found.\n")
        continue

    break

#  matching file content against regexp for classes
contents = file.read()
public_classes = finditer(class_pattern, contents)

#  if any classes found - search for public attributes/operation within their contents
result = list()
for match in public_classes:
    #  for some reason, [0] is class content and [1] is it's name
    if search(inner_pattern, match[0]):
        #  if regular class content has smt public - add it's name to the result list
        result.append(match[1])

for name in result:
    print(name)

result.clear()
