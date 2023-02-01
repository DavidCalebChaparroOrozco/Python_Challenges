class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Overwriting of the __str__ method
    def __str__(self):  # str: override the class father(Person -> Object)
        return f'Person [Name: {self.name}, Age: {self.age}]'


class Employee(Person):
    def __init__(self, name, age, salary):
        # super: used to give access to methods and properties of a parent or sibling class.
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        return f'Employee: [Salary: {self.salary}] {super().__str__()}'

# employee1 = Employee('Gregory House', 45, 2000)
# print(employee1.name)
# print(employee1.age)
# print(employee1.salary)