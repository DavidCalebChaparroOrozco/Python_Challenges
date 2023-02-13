from ResourceManager import *
# with open('test.txt', 'r', encoding='utf8') as file:
with ResourceManager('test.txt') as file:
    print(file.read())