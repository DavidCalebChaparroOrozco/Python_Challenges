# Cube
class Cube:

    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def calculate_volume(self):
        return self.length * self.width * self.height

width = int(input('Enter the width: '))
length = int(input('Enter the length: '))
height = int(input('Enter the height: '))
rectangle1 = Cube(width,length, height)
print(f'Cube volume: {rectangle1.calculate_volume()}')