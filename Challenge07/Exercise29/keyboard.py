from input_device import *

class Keyboard(inputDevice):
    count_keyboard = 0

    def __init__(self, brand, type_input):
        Keyboard.count_keyboard += 1
        self._id_keyboard = Keyboard.count_keyboard
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
        return f'Id: {self._id_keyboard}, Brand: {self._brand}, Type input: {self._type_input}'

if __name__ == '__main__':
    keyword1 = Keyboard('HP', 'USB')
    print(keyword1)

    keyword2 = Keyboard('Gamer', 'Bluetooth')
    print(keyword2)