from Product import *

class Order:
    count_order = 0

    def __init__(self, products):
        Order.count_order += 1
        self._id_order = Order.count_order
        self._products = list(products)

    def add_product(self, product):
        self._products.append(product)

    def calculate_total(self):
        total = 0
        for product in self._products:
            total += product.price
        return total

    def __str__(self):
        products_str = ''
        for product in self._products:
            products_str += product.__str__() + '|'

        return f'Order: {self._id_order}, \nProducts: {products_str}'

if __name__ == '__main__':
    product1 = Product('T-Short', 100.00)
    product2 = Product('Shirt', 150.00)
    products1 = [product1, product2]
    order1 = Order(products1)
    print(order1)
    order2 = Order(products1)
    print(order2)