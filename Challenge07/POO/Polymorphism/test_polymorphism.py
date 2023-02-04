from Employee import *
from Manager import *

def print_details(object):
    # print(object)
    print(type(object))
    print(object.show_details())
    # isinstance: The isinstance() built-in function is recommended for testing the type of object,
    # because it takes subclasses into account
    # https://docs.python.org/3/library/functions.html#isinstance
    if isinstance(object, Manager):
        print(object.department)

manager1 = Manager('Montgomery Burns', 100000, 'CEO')
print_details(manager1)

employee1 = Employee('Homer J Simpson', 3000)
print_details(employee1)