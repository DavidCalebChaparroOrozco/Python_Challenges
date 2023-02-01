# To put restrictions is to put a "_" to those attributes, this is called encapsulation.

# There is also another more restrictive way to not modify the attributes that would be with "__"
class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    # get: obtain/recover
    @property
    def last_name(self):
        print('Calling get last_name method')
        return self._last_name

    # set: place/change
    @last_name.setter
    def last_name(self, last_name):
        print('Calling set last_name method')
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def age(self):
        return self._age

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @age.setter
    def age(self, age):
        self._age = age

    def show_detail(self):
        print(f'Person: {self._first_name} {self._last_name} {self._age}')



# This is a bad practice
# person1._last_name = 'change'
# print(person1._last_name)

"""
For read-only attributes.
We can remove these lines of code:

    @last_name.setter
    def last_name(self, last_name):
        print('Calling set last_name method')
        self._last_name = last_name

But if we want to modify it if or if you remember to use:

person1._last_name = 'Sanchez C-137'
"""

# Encapsulation (get/set) / read-only attributes

if __name__ == '__main__':
    # Rick Sanchez C-137 70
    person1 = Person('Rick', 'Sanchez C-137', 70)

    # Morty Smith C-137 14
    person1.first_name = 'Morty'
    person1.last_name = 'Smith C-131'
    person1.age = 14
    person1.show_detail()
    # Main module check
    print(__name__)
