# Rectangle
class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.length * self.width

width = int(input('Enter the width: '))
length = int(input('Enter the length: '))
rectangle1 = Rectangle(width,length)
print(f'Rectangle area: {rectangle1.calculate_area()}')
