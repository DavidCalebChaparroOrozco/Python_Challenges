from input_device import *

class Mouse(inputDevice):

    count_mouse = 0

    def __init__(self, brand, type_input):
        Mouse.count_mouse += 1
        self._id_mouse = Mouse.count_mouse
        super().__init__(brand, type_input)

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

    def __str__(self):
        return f'Id: {self._id_mouse}, Brand: {self._brand}, Type Input: {self._type_input}'

if __name__ == '__main__':
    mouse1 = Mouse('HP', 'USB')
    print(mouse1)

    mouse2 = Mouse('Acer', 'Bluetooth')
    print(mouse2)