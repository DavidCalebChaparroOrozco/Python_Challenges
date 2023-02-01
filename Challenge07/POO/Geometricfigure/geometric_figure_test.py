from Square import *

square1 = Square(5,'Red')
# print(square1.width)
# print(square1.height)
# print(square1.color)
print(f'Calculate square area: {square1.calculate_area()}')

# MRO - Method Resolution Order
# Is the order in which base classes are searched for a member during lookup.
print(Square.mro())