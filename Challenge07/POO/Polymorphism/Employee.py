# polymorphism
# The word polymorphism means having many forms. In programming, polymorphism means the same function name
# (but different signatures) being used for different types. The key difference is the data types and number of
# arguments used in function.
# https://www.geeksforgeeks.org/polymorphism-in-python/

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def __str__(self):
        return f'Employee: [Name: {self.name}, Salary: {self.salary}]'

    def show_details(self):
        return self.__str__()
