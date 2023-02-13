class IdenticalNumbersException(Exception):

    def __init__(self, message):
        self._message = message