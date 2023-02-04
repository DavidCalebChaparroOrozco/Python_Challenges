from Employee import *

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f'Manager [Department: {self.department}] {super().__str__()}'