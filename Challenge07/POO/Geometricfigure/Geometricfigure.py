class GeometricFigure:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def first_name(self, width):
        self._width = width

    @height.setter
    def age(self, height):
        self._height = height

