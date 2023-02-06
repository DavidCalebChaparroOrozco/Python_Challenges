from computer import *
from order import *

keyboard1 = Keyboard('HP', 'USB')
mouse1 = Mouse('HP', 'USB')
monitor1 = Monitor('HP', 15)
computer1 = Computer('HP', monitor1, keyboard1, mouse1)

keyboard2 = Keyboard('Acer', 'Bluetooth')
mouse2 = Mouse('Acer', 'Bluetooth')
monitor2 = Monitor('Acer', 27)
computer2 = Computer('Acer', monitor2, keyboard2, mouse2)

keyboard3 = Keyboard('Gamer', 'Bluetooth')
mouse3 = Mouse('Gamer', 'Bluetooth')
monitor3 = Monitor('Gamer', 34)
computer3 = Computer('Gamer', monitor3, keyboard3, mouse3)

computers1 = [computer1, computer2]
order1 = Order(computers1)
print(order1)

order1.add_computer(computer3)
print(order1)

computers2 = [computer2, computer3]
order2 = Order(computers2)
print(order2)