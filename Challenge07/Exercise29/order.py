class Order:
    count_order = 0

    def __init__(self,computers):
        Order.count_order += 1
        self._id_order = Order.count_order
        self._computers = computers

    def add_computer(self, computer):
        self._computers.append(computer)

    def __str__(self):
        computers_str = ''
        for computer in self._computers:
            computers_str += computer.__str__()
        return f'''
Order: {self._id_order}
Computers: {computers_str}
        '''