from Square import *
from Rectangle import *

print('Creation of square object'.center(50,'-'))
square1 = Square(side=5,color='Red')
square1.side = -10
# print(square1.width)
# print(square1.height)
# print(square1.color)
print(f'Calculate square area: {square1.calculate_area()}')
print(square1)

# MRO - Method Resolution Order
# Is the order in which base classes are searched for a member during lookup.
# print(Square.mro())

print('Creation of rectangle object'.center(50,'-'))
rectangle1 = Rectangle(width=9,height=8,color='Green')
rectangle1.height = 8
print(f'Calculate rectangle area: {rectangle1.calculate_area()}')
print(rectangle1)