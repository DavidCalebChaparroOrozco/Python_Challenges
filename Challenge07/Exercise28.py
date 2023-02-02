class Person:
    count_persons = 0

    @classmethod
    def generate_next_value(cls):
        cls.count_persons += 1
        return cls.count_persons

    def __init__(self, name, age):
        self.id_Persona = Person.generate_next_value()
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person [{self.id_Persona} {self.name} {self.age}]'

person1 = Person('Adan',930)
print(person1)
person2 = Person('Eve',930)
print(person2)
print(f'Value count person: {Person.count_persons}')

person3 = Person('Cain',930)
print(person3)

print(f'Count value person: {Person.count_persons}')

person4 = Person('Abel',72)
print(person4)
print(f'Count value person: {Person.count_persons}')