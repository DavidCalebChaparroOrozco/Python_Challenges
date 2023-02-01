from Geometricfigure import *
from Color import *

class Square(GeometricFigure, Color):
    def __init__(self, side, color):
        # super().__init__(side)
        GeometricFigure.__init__(self, side, side)
        Color.__init__(self, color)

    def calculate_area(self):
        return self.height * self.width


