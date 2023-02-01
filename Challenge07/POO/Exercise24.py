# Basic calculator
class Arithmetic:
    # DocString: Documentation of the class in Python
    """
    Class Arithmetic: to perform the operations add, subtract, multiply and divide
    """

    def __init__(self, numA, numB):
        self.numA = numA
        self.numB = numB

    def add(self):
        return float(self.numA + self.numB)

    def subtract(self):
        return float(self.numA - self.numB)

    def multiply(self):
        return float(self.numA * self.numB)

    def divide(self):
        if self.numB == 0:
            return 'Cannot divide by ZERO'
        return float(self.numA / self.numB)

arithmetic1 = Arithmetic(10, 5)
print('Basic calculator'.center(50,'-'))
print(f'Add: {arithmetic1.add()}')
print(f'Subtract: {arithmetic1.subtract()}')
print(f'Multiply: {arithmetic1.multiply()}')
print(f'Divide: {arithmetic1.divide():.3f}')