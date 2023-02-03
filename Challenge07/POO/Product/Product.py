class Product:
    count_product = 0

    def __init__(self, name, price):
        Product.count_product += 1
        self._id_product = Product.count_product
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._first_name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def name(self, price):
        self._first_name = price

    def __str__(self):
        return f'Id product: {self._id_product}, Name: {self._name}, Price: {self._price}'

if __name__ == '__main__':
    product1 = Product('T-Short', 100.00)
    print(product1)
    product2 = Product('Shirt', 150.00)
    print(product2)