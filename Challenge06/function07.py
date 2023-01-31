def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

numberA = int(input('Enter the number: '))
result = factorial(numberA)
"""
3! = 3 * 2 * 1
"""
print(f'The factorial of number is {result} ')