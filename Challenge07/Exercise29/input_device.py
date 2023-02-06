class inputDevice:
    def __init__(self, brand, type_input):
        self._brand = brand
        self._type_input = type_input

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def type_input(self):
        return self._type_input

    @type_input.setter
    def type_input(self, type_input):
        self._type_input = type_input