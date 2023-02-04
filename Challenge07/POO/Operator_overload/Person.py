class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return f'{self.name} {other.name}'

    def __sub__(self, other):
        return self.age - other.age


Person1 = Person('Shaggy',17)
Person2 = Person('Vilma',15)
print(Person1 + Person2)

print(Person1 - Person2)
# obj1 + obj2
# obj1.__add__(obj2)