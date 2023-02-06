from keyboard import *
from monitor import *
from mouse import *

class Computer:
    count_computer = 0

    def __init__(self, name, monitor, keyboard, mouse):
        Computer.count_computer += 1
        self._id_computer = Computer.count_computer
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    def __str__(self):
        return f'''
    {self._name}: {self._id_computer}
    Monitor: {self._monitor}
    Keyboard: {self._keyboard}
    Mouse: {self._mouse}
'''

if __name__ == '__main__':
    keyboard1 = Keyboard('HP', 'USB')
    mouse1 = Mouse('HP', 'USB')
    monitor1 = Monitor('HP', 15)
    computer1 = Computer('HP', monitor1, keyboard1, mouse1)
    print(computer1)

    keyboard2 = Keyboard('Acer', 'Bluetooth')
    mouse2 = Mouse('Acer', 'Bluetooth')
    monitor2 = Monitor('Acer', 27)
    computer2 = Computer('Acer', monitor2, keyboard2, mouse2)
    print(computer2)