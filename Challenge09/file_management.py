# open: Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised.
# See Reading and Writing Files for more examples of how to use this function.
# https://docs.python.org/3/library/functions.html#open
try:
    file = open('test.txt', 'w', encoding='utf8') # w: write / enconding
    file.write('Add information to the file \n') # \n: Line break
    file.write('Bye')
except Exception as e:
    print(e)
finally:
    file.close()
    print('End to the file')