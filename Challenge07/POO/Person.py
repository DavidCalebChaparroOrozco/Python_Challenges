# Class: A template for creating user-defined objects. Class definitions normally contain method definitions which
# operate on instances of the class.

# Object: An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class
# with actual values. Objects are basically an encapsulation of data variables and methods acting on that data into a
# single entity.
# https://docs.python.org/3/glossary.html
class Person:
    # __init__: Allows to add attributes to classes and to initialize these attributes.
    # self: is a parameter for default, it is also a reference to the object itself.
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# Rick Sanchez 70
person1 = Person('Rick', 'Sanchez', 70)
# print(person1.first_name)
# print(person1.last_name)
# print(person1.age)
print(f'Object person 1: {person1.first_name} {person1.last_name} {person1.age}')

# Morty Smith 14
person2 = Person('Morty', 'Smith', 14)
print(f'Object person 2: {person2.first_name} {person2.last_name} {person2.age}')