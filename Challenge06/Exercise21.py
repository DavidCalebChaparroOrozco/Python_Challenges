# Print numbers in descending order using recursive functions.
# Can be any positive value, if negative values are passed, nothing is printed.

def print_number_recursive(number):
    if number >=1:
        print(number)
        print_number_recursive(number - 1)
    elif number == 0:
        return
    elif number <=0:
        print('Wrong value...')

numberA = int(input('Enter the number: '))
print_number_recursive(numberA)