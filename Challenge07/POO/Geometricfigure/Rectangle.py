from Geometricfigure import *
from Color import *

class Rectangle(GeometricFigure, Color):
    def __init__(self, width, height, color):
        GeometricFigure.__init__(self, width, height)
        Color.__init__(self, color)

    def calculate_area(self):
        return self.height * self.width

    def __str__(self):
        return f'{GeometricFigure.__str__(self)} {Color.__str__(self)}'