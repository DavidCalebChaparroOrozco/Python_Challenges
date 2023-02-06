class Monitor:
    count_monitor = 0
    def __init__(self, brand, size):
        Monitor.count_monitor += 1
        self._id_monitor = Monitor.count_monitor
        self._brand = brand
        self._size = size

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def __str__(self):
        return f'Id: {self._id_monitor}, Brand: {self._brand}, Size: {self._size}'

if __name__ == '__main__':
    monitor1 = Monitor('HP', 20)
    print(monitor1)

    monitor2 = Monitor('Acer', 30)
    print(monitor2)