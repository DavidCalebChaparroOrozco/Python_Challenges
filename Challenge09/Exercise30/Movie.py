class Movie:
    def __init__(self, name, year):
        self._name = name
        self._year = year

    def __str__(self):
        return f'Movie: {self._name}, Year: {self._year}'

    @property
    def name(self):
        return self._name

    @property
    def year(self):
        return self._year

    @name.setter
    def name(self, name):
        self._name = name

    @year.setter
    def year(self, year):
        self._name = year