from Order import *
from Product import *

product1 = Product('T-Short', 100.00)
product2 = Product('Shirt', 150.00)

product3 = Product('Socks', 20.00)
product4 = Product('Dress', 200.00)

products1 = [product1, product2]
order1 = Order(products1)
order1.add_product(product3)
order1.add_product(product4)
print(order1)
print(f'Total order 1: {order1.calculate_total()}')

products2 = [product3, product4]
order2 = Order(products2)
print(order2)
print(f'Total order 2: {order2.calculate_total()}')