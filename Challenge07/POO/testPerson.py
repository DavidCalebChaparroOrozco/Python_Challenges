# Use of modules and classes
from encapsulationPerson import Person

if __name__ == '__main__':
    print('Object creation'.center(50,'-'))
    person1 = Person('Rick', 'Sanchez C-137', 70)
    person1.show_detail()
    # Main module check
    print(__name__)

    print('Object delete'.center(50,'-'))
    del person1