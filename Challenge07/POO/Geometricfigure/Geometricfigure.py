class GeometricFigure:
    def __init__(self, width, height):
        if self._valide_value(width):
            self._width = width
        else:
            self._width = 0
            print(f'Wrong width value {width}')
        if self._valide_value(height):
            self._height = height
        else:
            self._height = 0
            print(f'Wrong width value {height}')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if self._valide_value(width):
            self._width = width
        else:
            print(f'Wrong width value: {width}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if self._valide_value(height):
            self._height = height
        else:
            print(f'Wrong height value {height}')

    def __str__(self):
        return f'Geometric figure [Width: {self._width}, Height: {self._height}]'

    def _valide_value(self, value):
        return True if 0 < value < 10 else False